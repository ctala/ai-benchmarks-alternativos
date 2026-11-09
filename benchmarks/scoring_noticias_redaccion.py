"""
Scorers de las suites `noticias_redaccion` y `noticias_traduccion`, y el contador de
defectos de IA que se calcula sobre la misma salida de la redacción.

POR QUÉ EXISTE
--------------
El pipeline de noticias de un founder que publica (Eco es el caso medido, pero el patrón
es de cualquiera que convierte una fuente en una nota con un LLM) se rompe de cuatro
formas, y las cuatro se pueden contar sin juez:

  1. **La cifra ajena.** El modelo completa lo que la fuente no dijo: el año del hecho,
     la valuación, un porcentaje «de contexto». Medido el 5-ago-2026 en producción:
     24 de 29 notas bloqueadas en un día fueron por datos que nadie dijo. Un juez LLM no
     lo ve, porque la nota *parece* buena. Aquí se extraen los números del texto, se
     normalizan (`US$100M` = `100 millones de dólares` = `$100 million`) y cada uno tiene
     que existir en la fuente.
  2. **El dato clave ausente.** La nota larga que se pasea por el contexto y no dice el
     monto ni quién lo levantó.
  3. **El idioma.** Voseo (excluye al 60-70 % de la audiencia hispanohablante) y la fuga
     de CJK (un carácter chino en medio de la nota y el artículo está quemado).
  4. **El largo.** 900-1.300 palabras es el estándar de noticia con análisis; la tensión
     real es que rellenar para llegar al largo es exactamente lo que produce la cifra
     ajena. Por eso la cifra pesa más que el largo.

`contar_defectos` NO entra en la nota: es una métrica aparte de «olor a IA» (catálogo
`humanize-ctala`, tells T4, T8, T10, T11, T12, T14, T19 y palabras vetadas) que se
calcula desde las respuestas guardadas.

FÓRMULA DE `noticias_redaccion` (0-10)
--------------------------------------
    nota = 10 × (0,35·cifras + 0,25·dato_clave + 0,15·cjk + 0,15·largo + 0,10·voseo)

  · cifras      1 si no hay cifras ajenas; 0,5 con una; 0 con dos o más. (En producción
                UNA cifra ajena bloquea la nota entera: por eso cae rápido.)
  · dato_clave  fracción de datos clave presentes (número normalizado a ≤300 caracteres
                de una mención de la entidad).
  · cjk         binario: un solo carácter chino/japonés/coreano y vale 0.
  · largo       1 entre 900 y 1.300 palabras; lineal a 0 en 600 y en 1.800.
  · voseo       binario: una forma voseante y vale 0.

FÓRMULA DE `noticias_traduccion` (0-10)
---------------------------------------
    nota = 10 × (0,35·cjk + 0,30·resto + 0,25·términos + 0,10·cifra)

  · cjk       binario, cero CJK en la salida.
  · resto     fracción de los tramos en español del original que aparecen intactos y en
              orden (tolerancia: espacios y puntuación de borde).
  · términos  fracción de fragmentos cuyo hueco (lo que quedó entre dos tramos) contiene
              un equivalente aceptado. Si los tramos no se encuentran, se busca el
              término en toda la salida.
  · cifra     fracción de las cifras esperadas presentes (normalizadas).

LÍMITES DOCUMENTADOS DE «NINGUNA CIFRA AJENA» (leer antes de confiar en un cero)
-------------------------------------------------------------------------------
  · Compara VALOR, no unidad: «15 %» se acepta si la fuente tiene un 15 cualquiera.
  · No hay tolerancia de redondeo (0,1 % relativo, solo para errores de coma flotante):
    «US$5,6 millones» contra «$5.576 million» es ajena. Es a propósito: la regla de
    producción prohíbe redondear montos.
  · «billón» en español = 10^12. Traducir «$1.2 billion» como «1,2 billones» se marca
    ajena, y está bien: es un error de traducción que multiplica la cifra por mil.
  · Exentos: enteros desnudos de 0 a 10 (sin moneda, sin multiplicador, sin %), los
    números pegados a letras (GPT-4, H100, B2B, 5G, Q3), los marcadores de lista al
    inicio de línea («1.», «2)»), horas («10:30»), ordinales («1.º») y todo lo que está
    dentro de una URL. Los números escritos con palabras en la nota solo cuentan si
    llevan multiplicador («tres millones»); en la fuente cuentan siempre.
  · Un número desnudo de la nota se acepta también si coincide con la mantisa de una
    cifra de la fuente («1,4» cuando la fuente dice «$1.4 trillion»).
  · Puntos ciegos conocidos: compuestos con palabras («trescientos cincuenta millones»
    se lee como 50 millones → falso positivo); una cifra correcta en contexto falso
    (el 38 % de la fuente atribuido a otra cosa) pasa; duraciones derivadas pequeñas
    («hace 9 años») pasan por la exención de 0-10.
"""
from __future__ import annotations

import math
import re
import statistics
import unicodedata

from benchmarks.scoring import _parse_number_es, _score_language_check

# ─────────────────────────────────────────────────────────────────────────────
# Utilidades comunes
# ─────────────────────────────────────────────────────────────────────────────

def tiene_cjk(texto: str) -> bool:
    """Reutiliza la detección CJK de `scoring._score_language_check`.

    Esa función devuelve 0,0 si hay un solo carácter CJK. Se antepone «el » para que un
    texto sin CJK nunca dé 0 por otra razón (texto vacío o en otro idioma): con una
    palabra funcional en español la razón es > 0 siempre.
    """
    return _score_language_check("el " + (texto or ""), {"reject_cjk": True,
                                                         "required_language": "es"}) == 0.0


def _sin_acentos(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


_URL = re.compile(r"https?://\S+|www\.\S+")
_PALABRA = re.compile(r"[0-9A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+(?:[.,'’\-][0-9A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+)*")


def cuerpo_de_nota(texto: str) -> str:
    """El cuerpo que se cuenta: sin bloques de código, sin la sección final de fuentes
    («## Fuentes», «Fuentes:») y sin URLs. Títulos y subtítulos SÍ cuentan: son parte de
    la nota publicada."""
    t = re.sub(r"```.*?```", " ", texto or "", flags=re.S)
    t = re.split(r"(?im)^\s*(?:#{1,6}\s*|\*\*)?(?:fuentes|referencias|sources)\b\s*:?\**\s*$", t)[0]
    t = re.sub(r"\]\([^)]*\)", "]", t)   # enlaces markdown: se queda el texto
    return _URL.sub(" ", t)


def contar_palabras(texto: str) -> int:
    """Palabras del cuerpo: tokens alfanuméricos; «1.200» y «e-commerce» cuentan uno."""
    return len(_PALABRA.findall(cuerpo_de_nota(texto)))


# ─────────────────────────────────────────────────────────────────────────────
# Voseo
# ─────────────────────────────────────────────────────────────────────────────

# Formas voseantes SIN homónimo en el español neutro. Fuera a propósito: «salí», «pedí»,
# «elegí», «seguí», «escribí», «viví» (son pretérito de «yo»), «Tomás» (nombre), «dale»
# (imperativo de tú), y las formas sin tilde («tenes», «podes»: «podes» es subjuntivo
# de podar). Límite de palabra a ambos lados: «voseo» o «vosotros» no cazan «vos».
VOSEO = [
    "tenés", "podés", "querés", "sabés", "hacés", "debés", "decís", "venís", "sentís",
    "conocés", "necesitás", "empezás", "buscás", "pensás", "usás", "mirás", "llegás",
    "contás", "pagás", "ganás", "vendés", "entendés", "perdés", "ponés", "creés", "leés",
    "vivís", "elegís", "seguís", "pedís", "salís", "escribís", "arrancás", "invertís",
    "hacé", "mirá", "tené", "poné", "vení", "andá", "fijate", "sabé", "pensá", "contá",
    "probá", "usá", "buscá", "mandá", "dejá", "llamá", "esperá", "imaginá", "acordate",
    "animate", "decime", "contame", "mirala", "fijense", "vos",
]
_VOSEO_RE = re.compile(r"(?<![\wáéíóúñü])(" + "|".join(map(re.escape, VOSEO)) + r")(?![\wáéíóúñü])",
                       re.I)
_SOS_RE = re.compile(r"(?<![\wáéíóúñü])sos(?![\wáéíóúñü])")   # sensible a mayúsculas: «SOS» no


def formas_voseo(texto: str) -> list[str]:
    t = cuerpo_de_nota(texto)
    return [m.group(0) for m in _VOSEO_RE.finditer(t)] + [m.group(0) for m in _SOS_RE.finditer(t)]


# ─────────────────────────────────────────────────────────────────────────────
# Extracción y normalización de cifras
# ─────────────────────────────────────────────────────────────────────────────

# Multiplicadores, del más largo al más corto (el orden importa: «mil millones» antes que
# «mil»). Los de una letra (M, B, K, k) son sensibles a mayúsculas y van pegados o con
# un espacio.
_MULT = [
    (r"mil\s+millones", 1e9), (r"millardos?", 1e9), (r"billones", 1e12), (r"bill[oó]n", 1e12),
    (r"billions?", 1e9), (r"trillions?", 1e12), (r"millones", 1e6), (r"mill[oó]n", 1e6),
    (r"millions?", 1e6), (r"thousand", 1e3), (r"mill\.", 1e6), (r"mil", 1e3),
    (r"bn", 1e9), (r"mn", 1e6), (r"MM", 1e6),
]
_MULT_RE = re.compile(r"\s*(" + "|".join(p for p, _ in _MULT) + r")(?![\wáéíóúñ])", re.I)
_MULT_LETRA_RE = re.compile(r"\s?([MBKk])(?![\wáéíóúñ])")
_PCT_RE = re.compile(r"\s*(%|por\s*ciento|percent|per\s*cent)", re.I)
_NUM_RE = re.compile(r"\d{1,3}(?:[.,]\d{3})+(?:[.,]\d+)?|\d+(?:[.,]\d+)?")

_PALABRAS_NUM = {
    # español
    "un": 1, "uno": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5, "seis": 6,
    "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11, "doce": 12, "trece": 13,
    "catorce": 14, "quince": 15, "dieciséis": 16, "diecisiete": 17, "dieciocho": 18,
    "diecinueve": 19, "veinte": 20, "treinta": 30, "cuarenta": 40, "cincuenta": 50,
    "sesenta": 60, "setenta": 70, "ochenta": 80, "noventa": 90, "cien": 100, "ciento": 100,
    "doscientos": 200, "doscientas": 200, "trescientos": 300, "trescientas": 300,
    "cuatrocientos": 400, "quinientos": 500, "quinientas": 500, "seiscientos": 600,
    "setecientos": 700, "ochocientos": 800, "novecientos": 900, "mil": 1000,
    # inglés
    "one": 1, "a": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
    "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "fifteen": 15, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
    "seventy": 70, "eighty": 80, "ninety": 90, "hundred": 100, "dozen": 12,
}
_ARTICULOS = {"un", "uno", "una", "a"}   # solo cuentan con multiplicador singular («un millón»)
_MULT_SINGULAR = r"mill[oó]n|bill[oó]n|million|billion|trillion|thousand|millardo"
_PAL_NUM_RE = re.compile(r"(?<![\wáéíóúñ])(" + "|".join(sorted(_PALABRAS_NUM, key=len, reverse=True))
                         + r")(?![\wáéíóúñ])", re.I)


def _mult_valor(token: str) -> float:
    for patron, valor in _MULT:
        if re.fullmatch(patron, token.strip(), re.I):
            return valor
    return {"M": 1e6, "B": 1e9, "K": 1e3, "k": 1e3}.get(token.strip(), 1.0)


def extraer_cifras(texto: str, *, es_fuente: bool = False) -> list[dict]:
    """Devuelve las cifras del texto: dicts {raw, valor, mantisa, tipo, pos, exenta}.

    `tipo` ∈ {monto, pct, anio, simple}. `exenta` marca lo que no se exige que esté en la
    fuente (ver los límites en el docstring del módulo). Con `es_fuente=True` no se exime
    nada y se suman los números escritos con palabras.
    """
    t = _URL.sub(lambda m: " " * len(m.group(0)), texto or "")
    t = re.sub(r"\]\([^)]*\)", lambda m: " " * len(m.group(0)), t)
    out = []
    for m in _NUM_RE.finditer(t):
        i, j = m.start(), m.end()
        antes = t[i - 1] if i > 0 else " "
        antes2 = t[i - 2] if i > 1 else " "
        despues = t[j] if j < len(t) else " "
        if antes.isalpha() or (antes == "-" and antes2.isalpha()):
            continue                        # GPT-4, H100, COVID-19, B2B
        if antes in ".," and antes2.isdigit():
            continue                        # resto de un número ya leído
        if antes == ":" or despues == ":" and j + 1 < len(t) and t[j + 1].isdigit():
            continue                        # horas
        if despues in "ºª°":
            continue                        # ordinales
        raw = m.group(0)
        valor = _parse_number_es(raw)
        if valor is None:
            continue
        mult, tipo, fin = 1.0, "simple", j
        mm = _MULT_RE.match(t, j)
        if mm:
            mult, fin = _mult_valor(mm.group(1)), mm.end()
        else:
            ml = _MULT_LETRA_RE.match(t, j)
            if ml:
                mult, fin = _mult_valor(ml.group(1)), ml.end()
        if mult == 1.0:
            mp = _PCT_RE.match(t, j)
            if mp:
                tipo, fin = "pct", mp.end()
        sig = t[fin] if fin < len(t) else " "
        if mult == 1.0 and tipo == "simple" and (sig.isalpha() and sig not in "xX"):
            # pegado a una letra (5G, 4o, 3D): no es una cifra de la noticia
            if fin == j:
                continue
        moneda = bool(re.search(r"(US\$|USD|\$|€|EUR|£|R\$|MXN|CLP|COP)\s?$", t[max(0, i - 5):i])
                      or re.match(r"\s*(de\s+)?(dólares|dolares|euros|pesos|yenes|wones|USD|EUR|dollars|euros)\b",
                                  t[fin:fin + 20], re.I))
        if mult != 1.0 or moneda:
            tipo = "monto" if tipo == "simple" else tipo
        elif tipo == "simple" and re.fullmatch(r"(19|20)\d\d", raw):
            tipo = "anio"
        exenta = False
        if not es_fuente:
            inicio_linea = t.rfind("\n", 0, i) + 1
            prefijo = t[inicio_linea:i]
            if tipo == "simple" and float(valor).is_integer() and 0 <= valor <= 10 and not moneda:
                exenta = True
            elif re.fullmatch(r"\s*(?:#{1,6}\s*)?", prefijo) and re.match(r"[.)]\s", t[j:j + 2]):
                exenta = True               # «1. », «2) » al inicio de línea
        out.append({"raw": t[i:fin].strip(), "valor": valor * mult, "mantisa": valor,
                    "tipo": tipo, "pos": i, "exenta": exenta, "palabra": False})
    # Números con palabras: en la fuente, siempre; en la nota, solo con multiplicador.
    for m in _PAL_NUM_RE.finditer(t):
        palabra = m.group(1).lower()
        base = _PALABRAS_NUM[palabra]
        mm = _MULT_RE.match(t, m.end())
        if palabra == "mil" and mm:
            continue                        # «mil millones» suelto se lee abajo
        if mm and palabra in _ARTICULOS and not re.fullmatch(_MULT_SINGULAR, mm.group(1).strip(), re.I):
            mm = None                       # «llega a millones de personas» no es una cifra
        if mm:
            valor = base * _mult_valor(mm.group(1))
            out.append({"raw": t[m.start():mm.end()].strip(), "valor": valor, "mantisa": base,
                        "tipo": "monto", "pos": m.start(), "exenta": False, "palabra": True})
        elif es_fuente and palabra not in _ARTICULOS:
            out.append({"raw": m.group(0), "valor": float(base), "mantisa": float(base),
                        "tipo": "simple", "pos": m.start(), "exenta": False, "palabra": True})
    # «mil millones» sin número delante = 1.000 millones
    for m in re.finditer(r"\bmil\s+millones\b", t, re.I):
        prev = t[max(0, m.start() - 12):m.start()]
        if re.search(r"(\d|" + "|".join(_PALABRAS_NUM) + r")\s*$", prev, re.I):
            continue
        out.append({"raw": m.group(0), "valor": 1e9, "mantisa": 1000.0, "tipo": "monto",
                    "pos": m.start(), "exenta": False, "palabra": True})
    return sorted(out, key=lambda c: c["pos"])


def _igual(a: float, b: float) -> bool:
    return math.isclose(a, b, rel_tol=1e-3, abs_tol=1e-9)


def valores_fuente(fuente: str, extra: list | None = None) -> tuple[list[float], list[float]]:
    cifras = extraer_cifras(fuente, es_fuente=True)
    valores = [c["valor"] for c in cifras] + [float(x) for x in (extra or [])]
    mantisas = [c["mantisa"] for c in cifras]
    return valores, mantisas


def cifras_ajenas(texto: str, fuente: str, extra: list | None = None) -> list[dict]:
    """Cifras de la nota que no existen en la fuente (una vez normalizadas)."""
    valores, mantisas = valores_fuente(fuente, extra)
    ajenas = []
    for c in extraer_cifras(texto):
        if c["exenta"]:
            continue
        if any(_igual(c["valor"], v) for v in valores):
            continue
        if c["tipo"] in ("simple", "anio") and not c["palabra"] and any(_igual(c["valor"], v) for v in mantisas):
            continue
        ajenas.append(c)
    return ajenas


def dato_clave_presente(texto: str, dato: dict, ventana: int = 300) -> bool:
    """Un dato clave = {"valor": float (opcional), "entidades": [...], "frases": [...] (opcional)}.

    Presente si una mención de la entidad está a ≤`ventana` caracteres de una cifra con
    ese valor (o, si el dato no trae valor, de una de sus frases).
    """
    plano = _sin_acentos(texto or "").lower()
    ents = [_sin_acentos(e).lower() for e in dato.get("entidades", [])]
    pos_ent = [m.start() for e in ents for m in re.finditer(re.escape(e), plano)]
    if not pos_ent:
        return False
    if "valor" in dato:
        objetivos = [c["pos"] for c in extraer_cifras(texto) if _igual(c["valor"], float(dato["valor"]))]
    else:
        frases = [_sin_acentos(f).lower() for f in dato.get("frases", [])]
        objetivos = [m.start() for f in frases for m in re.finditer(re.escape(f), plano)]
    return any(abs(p - q) <= ventana for p in pos_ent for q in objetivos)


def _fraccion_largo(n: int, lo: int = 900, hi: int = 1300) -> float:
    if lo <= n <= hi:
        return 1.0
    if n < lo:
        return max(0.0, (n - (lo - 300)) / 300)
    return max(0.0, 1 - (n - hi) / 500)


PESOS_REDACCION = {"cifras": 0.35, "dato_clave": 0.25, "cjk": 0.15, "largo": 0.15, "voseo": 0.10}


def detalle_redaccion(response: str, expected: dict) -> dict:
    texto = response or ""
    fuente = expected.get("fuente", "")
    n = contar_palabras(texto)
    ajenas = cifras_ajenas(texto, fuente, expected.get("cifras_extra_permitidas"))
    datos = expected.get("datos_clave", [])
    presentes = [dato_clave_presente(texto, d) for d in datos]
    vos = formas_voseo(texto)
    cjk = tiene_cjk(texto)
    comp = {
        "cifras": 1.0 if not ajenas else (0.5 if len(ajenas) == 1 else 0.0),
        "dato_clave": (sum(presentes) / len(presentes)) if presentes else 1.0,
        "cjk": 0.0 if cjk else 1.0,
        "largo": _fraccion_largo(n, *expected.get("rango_palabras", (900, 1300))),
        "voseo": 0.0 if vos else 1.0,
    }
    nota = 10 * sum(PESOS_REDACCION[k] * v for k, v in comp.items())
    return {"nota": round(nota, 2), "componentes": comp, "palabras": n,
            "ajenas": [c["raw"] for c in ajenas], "voseo": vos, "cjk": cjk,
            "datos_clave": presentes}


def score_noticias_redaccion(response: str, expected: dict) -> float:
    if not (response or "").strip():
        return 0.0
    return detalle_redaccion(response, expected)["nota"]


# ─────────────────────────────────────────────────────────────────────────────
# Traducción de fragmentos CJK
# ─────────────────────────────────────────────────────────────────────────────

def _norm_libre(s: str) -> str:
    return re.sub(r"\s+", " ", _sin_acentos(s).lower())


PESOS_TRADUCCION = {"cjk": 0.35, "resto": 0.30, "terminos": 0.25, "cifra": 0.10}


def _sin_puntuacion(s: str) -> str:
    """Para comparar tramos: sin puntuación, sin separadores de miles y con espacios
    colapsados. Conserva mayúsculas y tildes: el resto del párrafo tiene que ser idéntico
    salvo espacios y puntuación."""
    s = re.sub(r"(\d)[.,](\d)", r"\1\2", s)
    s = re.sub(r"[^\w\s%$€]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def detalle_traduccion(response: str, expected: dict) -> dict:
    """`expected`: {"original": str, "fragmentos": [{"cjk": str, "aceptados": [...]}],
    "cifras": [valores]}"""
    crudo = re.sub(r"\s+", " ", response or "").strip()
    salida = _sin_puntuacion(crudo)
    original = expected["original"]
    frags = expected["fragmentos"]
    # Tramos en español: el original cortado por los fragmentos CJK, en orden.
    patron = "(" + "|".join(re.escape(f["cjk"]) for f in frags) + ")"
    partes = re.split(patron, original)
    tramos = [_sin_puntuacion(p) for k, p in enumerate(partes) if k % 2 == 0]
    orden_frag = [p for k, p in enumerate(partes) if k % 2 == 1]
    # Buscar los tramos en orden y con límite de palabra (un tramo «en» no puede
    # encontrarse dentro de «inteligencia»); lo que queda entre dos tramos es la
    # traducción. Un tramo vacío (el párrafo empieza o termina con CJK) va al borde.
    spans, cursor = [], 0
    for k, tr in enumerate(tramos):
        if not tr:
            pos = 0 if k == 0 else (len(salida) if k == len(tramos) - 1 else None)
            spans.append((pos, pos) if pos is not None else None)
            continue
        m = re.compile(r"(?<!\w)" + re.escape(tr) + r"(?!\w)").search(salida, cursor)
        if not m:
            spans.append(None)
            continue
        spans.append((m.start(), m.end()))
        cursor = m.end()
    huecos = [salida[spans[k][1]:spans[k + 1][0]]
              if spans[k] is not None and spans[k + 1] is not None and spans[k][1] <= spans[k + 1][0]
              else None for k in range(len(orden_frag))]
    encontrados = sum(1 for k, tr in enumerate(tramos) if tr and spans[k] is not None)
    no_vacios = [t for t in tramos if t]
    resto = encontrados / len(no_vacios) if no_vacios else 1.0
    # Términos: en el hueco si existe; si no, en toda la salida.
    por_cjk = {f["cjk"]: f for f in frags}
    hits = []
    for k, fcjk in enumerate(orden_frag):
        acept = [_norm_libre(_sin_puntuacion(a)) for a in por_cjk[fcjk]["aceptados"]]
        zona = huecos[k] if huecos[k] is not None else salida
        z = _norm_libre(zona)
        hits.append(any(re.search(r"(?<!\w)" + re.escape(a) + r"(?!\w)", z) for a in acept))
    terminos = sum(hits) / len(hits) if hits else 1.0
    esperadas = expected.get("cifras", [])
    valores = [c["valor"] for c in extraer_cifras(crudo, es_fuente=True)]
    cifra = (sum(any(_igual(float(v), x) for x in valores) for v in esperadas) / len(esperadas)
             if esperadas else 1.0)
    cjk = tiene_cjk(crudo)
    comp = {"cjk": 0.0 if cjk else 1.0, "resto": resto, "terminos": terminos, "cifra": cifra}
    nota = 10 * sum(PESOS_TRADUCCION[k] * v for k, v in comp.items())
    return {"nota": round(nota, 2), "componentes": comp, "terminos": hits}


def score_noticias_traduccion(response: str, expected: dict) -> float:
    if not (response or "").strip():
        return 0.0
    return detalle_traduccion(response, expected)["nota"]


# ─────────────────────────────────────────────────────────────────────────────
# Contador de defectos de IA (métrica aparte; no entra en la nota)
# ─────────────────────────────────────────────────────────────────────────────

# T11 · conectores de ensayo al inicio de frase. «Sin embargo» queda FUERA: en una noticia
# es conector legítimo y contarlo inflaría la línea base de cualquier texto periodístico.
CONECTORES = [
    "Además", "Asimismo", "Por otro lado", "Por otra parte", "En definitiva", "En conclusión",
    "En resumen", "En síntesis", "En este sentido", "En este contexto", "Dicho esto",
    "Por consiguiente", "De hecho", "No obstante", "En última instancia", "Por ende",
    "Vale la pena", "Sin lugar a dudas", "En pocas palabras",
]
# T12 · adverbios vacíos (regla MENTOR_SIN_FILTRO). «claramente» y «prácticamente» quedan
# fuera: en una noticia suelen ser contenido («explicó claramente», «prácticamente el doble»).
ADVERBIOS = ["realmente", "básicamente", "sin duda", "totalmente", "verdaderamente",
             "absolutamente", "literalmente", "definitivamente", "sencillamente",
             "indudablemente", "genuinamente", "honestamente"]
# T19 · muletillas y negación decorativa: copiadas de `scripts/reto_pieza_check.py` y
# `operacion/scripts/publish-guards/linkedin_guards.py` (repo padre, 9-nov-2026). Se copian
# y no se importan porque el benchmark es un submodule que corre solo (CI incluido).
# «genuinamente»/«honestamente» se cuentan en T12 para no duplicar.
MULETILLAS = [
    (r"\bla inmensa mayoría\b", "la inmensa mayoría"),
    (r"\bmientras (ellos|otros|los demás)\b[^.]{0,80}\btú\b", "mientras ellos… tú…"),
    (r"\bno (es|era) (que )?[^.,;:\n]{1,70},\s*(es|era|sino) (que )?", "no es X, es Y"),
    (r"\bno (es|era) falta de\b", "no era falta de X"),
    (r"\bno necesitas\b[^.\n]{1,70}\bnecesitas\b", "no necesitas X, necesitas Y"),
    (r"\bel problema no (es|era)\b", "el problema no es"),
    (r"\bno se trata (solo |solamente |únicamente )?de\b[^.\n]{1,80}\bsino\b", "no se trata de X sino de Y"),
]
# Palabras y giros vetados: catálogo humanize-ctala + vetos del prompt del redactor de Eco.
VETADAS = [
    (r"\bsinergias?\b", "sinergia"), (r"\bdisrupt\w*", "disruptivo"),
    (r"\brevolucionari[oa]s?\b", "revolucionario"), (r"\bgame[- ]changer\b", "game changer"),
    (r"\ben la era digital\b", "en la era digital"), (r"\ben el mundo (actual|de hoy)\b", "en el mundo de hoy"),
    (r"\bcabe (destacar|señalar|mencionar|resaltar)\b", "cabe destacar"),
    (r"\bes importante (señalar|destacar|mencionar|notar|recordar|subrayar)\b", "es importante señalar"),
    (r"\b(apuesta por la innovación|motor de (la )?innovación|"
     r"a la vanguardia( de la innovación)?|impulsar la innovación)\b", "innovación (buzzword)"),
    (r"\bun antes y un después\b", "un antes y un después"), (r"\bcambio de paradigma\b", "cambio de paradigma"),
    (r"\ben constante evolución\b", "en constante evolución"), (r"\bdesde la(s)? trinchera(s)?\b", "desde la trinchera"),
    (r"\bsin (vueltas|rodeos)\b", "sin vueltas"), (r"\bvorágine\b", "vorágine"), (r"\bes oro\b", "es oro"),
    (r"\bpanorama (actual|empresarial|tecnológico)\b", "panorama actual"),
]
_VOCATIVO = re.compile(
    r"\b(Gracias|Hola|Bienvenid[oa]s?|Felicidades|Felicitaciones|Saludos|Querid[oa]s?|Ojo),\s+"
    r"[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+"
    r"|,\s+(founder|emprendedor(a)?|amig[oa]|lector(a)?|colega)(?=[.!?,])", re.I)

# T8 · ritmo parejo: coeficiente de variación (desvío/media) del largo de las frases de
# prosa. Umbral 0,35, PROVISIONAL: calibrado con solo tres textos sintéticos (limpio
# 0,60 · noticia sintética 0,41 · molde de IA 0,28). Se recalibra con la distribución de
# las respuestas reales guardadas antes de leerlo como señal. Exige al menos 8 frases.
UMBRAL_CV = 0.35
MIN_FRASES_T8 = 8


def _prosa(texto: str) -> str:
    t = cuerpo_de_nota(texto)
    lineas = [l for l in t.splitlines() if l.strip() and not l.lstrip().startswith("#")]
    return "\n".join(lineas)


def _frases(prosa: str) -> list[str]:
    t = re.sub(r"(\d)[.,](\d)", r"\1\2", prosa)   # no cortar en «1.200» ni «3,5»
    trozos = re.split(r"(?<=[.!?])\s+|\n+", t)
    return [s.strip() for s in trozos if len(re.findall(r"\w+", s)) >= 3]


def _contar_sin_solape(patrones, texto: str) -> int:
    """Cuenta coincidencias de varios patrones fusionando las que se superponen: «El
    problema no es X, es Y» caza dos patrones y es UN defecto."""
    spans = sorted((m.start(), m.end()) for p in patrones for m in re.finditer(p, texto, re.I))
    n, fin = 0, -1
    for a, b in spans:
        if a >= fin:
            n += 1
        fin = max(fin, b)
    return n


def contar_defectos(texto: str) -> dict:
    """Cuenta los tells de IA contables con código. Devuelve conteo por defecto, total
    y `por_mil_palabras` (total / palabras × 1000). T8 y T10 valen 0 o 1."""
    prosa = _prosa(texto or "")
    palabras = max(1, len(_PALABRA.findall(prosa)))
    d: dict = {}
    d["T4_raya"] = prosa.count("—") + len(re.findall(r"\s–\s", prosa))
    inicio = r"(?:^|(?<=[.!?])\s+|\n)\s*(?:[-*]\s+)?(?:\*\*)?"
    d["T11_conectores"] = sum(len(re.findall(inicio + re.escape(c) + r"\b", prosa, re.M)) for c in CONECTORES)
    d["T12_adverbios"] = sum(len(re.findall(r"\b" + a + r"\b", prosa, re.I)) for a in ADVERBIOS)
    d["T19_muletillas"] = _contar_sin_solape([p for p, _ in MULETILLAS], prosa)
    d["T14_coma_vocativa"] = len(_VOCATIVO.findall(prosa))
    d["vetadas"] = _contar_sin_solape([p for p, _ in VETADAS], prosa)
    largos = [len(re.findall(r"\w+", s)) for s in _frases(prosa)]
    cv = (statistics.pstdev(largos) / statistics.mean(largos)) if len(largos) >= MIN_FRASES_T8 else None
    d["T8_ritmo_parejo"] = int(cv is not None and cv < UMBRAL_CV)
    parrafos = [p.strip() for p in re.split(r"\n\s*\n", prosa) if p.strip()]
    d["T10_pregunta_cierre"] = int(bool(parrafos) and parrafos[-1].rstrip(" *_").endswith("?"))
    total = sum(d.values())
    d.update({"total": total, "palabras": palabras, "cv_frases": round(cv, 3) if cv is not None else None,
              "por_mil_palabras": round(total / palabras * 1000, 2)})
    return d


def detalle_defectos(texto: str) -> dict:
    """Igual que `contar_defectos`, más las coincidencias literales (para auditar)."""
    prosa = _prosa(texto or "")
    hits = {}
    hits["T19"] = [m.group(0) for p, _ in MULETILLAS for m in re.finditer(p, prosa, re.I)]
    hits["vetadas"] = [m.group(0) for p, _ in VETADAS for m in re.finditer(p, prosa, re.I)]
    hits["T12"] = [m.group(0) for a in ADVERBIOS for m in re.finditer(r"\b" + a + r"\b", prosa, re.I)]
    hits["T14"] = [m.group(0) for m in _VOCATIVO.finditer(prosa)]
    return hits
