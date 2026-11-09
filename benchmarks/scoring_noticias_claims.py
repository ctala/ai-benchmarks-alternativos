"""Scorers de las suites `noticias_extraccion` y `noticias_verificacion` — sin juez, 0-10.

POR QUÉ EXISTE (9-nov-2026)
---------------------------
Las dos suites miden los dos eslabones del gate de datos de cualquier pipeline que publica
noticias: sacar TODAS las afirmaciones verificables de una fuente y decidir, una por una,
si la fuente las respalda. Las suites hermanas que ya existen saturaron
(`extraer_claims` 94-97 % de respuestas perfectas, `verificar_claim` 63 %) porque sus
casos eran cortos y su scorer premiaba encontrar una cadena literal. Aquí la verdad es
POR CONSTRUCCIÓN — quien escribió la fuente sabe qué afirma — y el scorer la mide sin
pedirle opinión a otro modelo:

  · `noticias_extraccion`: RECALL sobre las afirmaciones plantadas, reconocidas por
    ANCLAS (una cifra normalizada, una entidad, una fecha) en vez de por texto literal;
    descuento por cifras que no existen en la fuente (inventadas o calculadas), y
    acierto del campo `nucleo`.
  · `noticias_verificacion`: veredictos correctos / afirmaciones enviadas. Una afirmación
    sin veredicto es un error — es el fallo real de producción (notas de 9-11 claims que
    devolvieron cero veredictos y se publicaron sin verificar). CONTRADICE y
    NO_RESPALDADO NO son intercambiables: confundirlos cuenta como error.

CABLEADO (no se hace aquí; lo hace quien registre las suites)
-----------------------------------------------------------
`scoring.score_expected_answer` debe despachar:
    "noticias_extraccion"   → score_noticias_extraccion(response, expected)
    "noticias_verificacion" → score_noticias_verificacion(response, expected)
Este módulo NO importa `scoring.py` (evita el import circular): trae su propio extractor
de JSON, con la misma tolerancia (```json, preámbulo, primer objeto balanceado).

LÍMITES CONOCIDOS DE LA NORMALIZACIÓN DE CIFRAS (`normalizar_cifras`)
---------------------------------------------------------------------
  · «1.200» y «1,200» se leen como MIL DOSCIENTOS (separador seguido de exactamente 3
    dígitos = miles). Un «1.250 billion» en inglés se leería 1.250 × 10⁹. No ocurre en
    las fuentes de las suites, que controlamos.
  · «billón/billones» se lee 10¹² (castellano correcto). Un modelo que traduce
    «$1.2 billion» como «1,2 billones» publica un error de mil veces y aquí no empareja.
  · Los sufijos de una letra (M, B, K) y «MM»/«bn» solo multiplican si hay una moneda
    pegada a la cifra (US$, USD, $, €, EUR…): «70B parámetros» no son 70 mil millones.
  · Formatos mexicanos tipo «3 mil 400 millones» no se reconstruyen (se leen 3 mil y 400
    millones por separado). «MDD» sí se lee como millones.
  · Cifras en palabras («tres países», «seven months») no se leen como número: las
    anclas de cantidades chicas usan alternativas de texto, no cifras.
  · Tolerancia relativa 0,5 %: «US$414 millones» empareja con «$414.41 million».
"""

from __future__ import annotations

import json
import re
import unicodedata

# ── utilidades de texto ──────────────────────────────────────────────────────


def _sin_acentos(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


def normalizar_texto(s: str) -> str:
    """minúsculas, sin acentos, espacios colapsados (para buscar entidades y fechas)."""
    s = _sin_acentos(str(s or "")).lower()
    s = s.replace(" ", " ").replace(" ", " ")
    return re.sub(r"\s+", " ", s).strip()


def extraer_json(texto: str):
    """Primer objeto/array JSON parseable del texto, o None (misma tolerancia que scoring.py)."""
    if not texto:
        return None
    t = str(texto).strip()
    candidatos = []
    m = re.search(r"```(?:json)?\s*(.+?)```", t, re.S | re.I)
    if m:
        candidatos.append(m.group(1).strip())
    candidatos.append(t)
    for abre, cierra in (("{", "}"), ("[", "]")):
        i = t.find(abre)
        if i >= 0:
            prof = 0
            en_str = False
            esc = False
            for j in range(i, len(t)):
                ch = t[j]
                if en_str:
                    if esc:
                        esc = False
                    elif ch == "\\":
                        esc = True
                    elif ch == '"':
                        en_str = False
                    continue
                if ch == '"':
                    en_str = True
                elif ch == abre:
                    prof += 1
                elif ch == cierra:
                    prof -= 1
                    if prof == 0:
                        candidatos.append(t[i:j + 1])
                        break
    for c in candidatos:
        try:
            return json.loads(c)
        except (ValueError, TypeError):
            continue
    return None


# ── normalización de cifras ──────────────────────────────────────────────────

_MONEDA = r"(?:US\$|U\$S|USD|R\$|MXN|CLP|ARS|COP|EUR|GBP|\$|€|£)"

# Multiplicadores por PALABRA: aplican siempre. El orden importa (lo más largo primero).
_MULT_PALABRA = [
    (r"miles\s+de\s+millones", 1e9),
    (r"mil\s+millones", 1e9),
    (r"billones|bill[oó]n", 1e12),
    (r"trillions?", 1e12),
    (r"billions?", 1e9),
    (r"millones|mill[oó]n|millions?|mdd|mmdd", 1e6),
    (r"thousands?", 1e3),
    (r"mil", 1e3),
]
# Multiplicadores por SUFIJO corto: solo con moneda pegada (US$1.2B, €385M, $700m, US$100MM).
_MULT_SUFIJO = [
    (r"bn|bln|b", 1e9),
    (r"mm|mn|m", 1e6),
    (r"k", 1e3),
]

_NUM = r"\d{1,3}(?:[.,   ]\d{3})+(?:[.,]\d+)?|\d+(?:[.,]\d+)?"
_RE_CIFRA = re.compile(
    r"(?<![\w.,])(?P<mon>" + _MONEDA + r")?\s?(?P<num>" + _NUM + r")"
    r"(?P<resto>\s*(?:"
    + "|".join(p for p, _ in _MULT_PALABRA)
    + r")\b|(?:" + "|".join(p for p, _ in _MULT_SUFIJO) + r")\b)?",
    re.I,
)


def _parse_num(s: str) -> float | None:
    s = s.replace(" ", " ").replace(" ", " ")
    # Espacios como separador de miles («1 200 000»): solo si son grupos de 3.
    if " " in s:
        if re.fullmatch(r"\d{1,3}(?: \d{3})+(?:[.,]\d+)?", s):
            s = s.replace(" ", "")
        else:
            s = s.split(" ")[0]
    tiene_p, tiene_c = "." in s, "," in s
    if tiene_p and tiene_c:
        dec = "." if s.rfind(".") > s.rfind(",") else ","
        mil = "," if dec == "." else "."
        s = s.replace(mil, "").replace(dec, ".")
    elif tiene_p or tiene_c:
        sep = "." if tiene_p else ","
        partes = s.split(sep)
        if len(partes) > 2:
            s = s.replace(sep, "")                      # 1.200.000 / 1,200,000
        elif len(partes[1]) == 3:
            s = s.replace(sep, "")                      # 1.200 / 1,200 → miles
        else:
            s = s.replace(sep, ".")                     # 4,2 / 1.25 → decimal
    try:
        return float(s)
    except ValueError:
        return None


def normalizar_cifras(texto: str) -> list[float]:
    """Todas las cifras del texto como números absolutos.

    «US$100M», «USD 100 millones», «100 millones de dólares», «$100 million» → 1e8.
    «US$1.2B», «1.200 millones», «1,2 mil millones» → 1.2e9.  «100 mil» → 1e5 (≠ 1e8).
    """
    out: list[float] = []
    if not texto:
        return out
    t = str(texto)
    for m in _RE_CIFRA.finditer(t):
        base = _parse_num(m.group("num"))
        if base is None:
            continue
        mult = 1.0
        resto = (m.group("resto") or "").strip().lower()
        if resto:
            hecho = False
            for pat, val in _MULT_PALABRA:
                if re.fullmatch(pat, resto, re.I):
                    mult, hecho = val, True
                    break
            if not hecho and m.group("mon"):
                for pat, val in _MULT_SUFIJO:
                    if re.fullmatch(pat, resto, re.I):
                        mult = val
                        break
        out.append(base * mult)
    return out


def _cerca(a: float, b: float, tol: float = 0.005) -> bool:
    if a == b:
        return True
    return abs(a - b) <= tol * max(abs(a), abs(b))


# ── anclas ───────────────────────────────────────────────────────────────────
# Un claim plantado tiene `anclas`: lista de GRUPOS; basta que un grupo se cumpla entero.
# Cada condición es {"num": valor} (alguna cifra del claim ≈ valor) o
# {"txt": [alternativas]} (alguna alternativa aparece, normalizada, en el claim).
# {"no_num": [...]} / {"no_txt": [...]} desambiguan: el claim NO trae esa cifra/texto, para
# que «SoftBank lideró la ronda de 2019 de US$150M» no cuente como «SoftBank lideró ESTA».


def _cumple(cond: dict, texto_norm: str, cifras: list[float]) -> bool:
    if "num" in cond:
        return any(_cerca(c, float(cond["num"])) for c in cifras)
    if "txt" in cond:
        return any(normalizar_texto(a) in texto_norm for a in cond["txt"])
    if "no_num" in cond:        # desambigua: el claim NO trae esta cifra (es otro dato)
        return not any(_cerca(c, float(v)) for c in cifras for v in cond["no_num"])
    if "no_txt" in cond:
        return not any(normalizar_texto(a) in texto_norm for a in cond["no_txt"])
    raise ValueError(f"condición de ancla desconocida: {cond!r}")


def claim_coincide(anclas: list[list[dict]], texto: str) -> bool:
    tn = normalizar_texto(texto)
    cifras = normalizar_cifras(texto)
    return any(all(_cumple(c, tn, cifras) for c in grupo) for grupo in anclas)


def _como_bool(v) -> bool | None:
    if isinstance(v, bool):
        return v
    if isinstance(v, str):
        v = normalizar_texto(v)
        if v in ("true", "si", "yes", "1", "verdadero"):
            return True
        if v in ("false", "no", "0", "falso"):
            return False
    if isinstance(v, (int, float)):
        return bool(v)
    return None


def _lista_claims(data) -> list[dict] | None:
    if isinstance(data, dict):
        lista = data.get("claims")
        if lista is None:
            lista = next((v for v in data.values() if isinstance(v, list)), None)
    else:
        lista = data
    if not isinstance(lista, list):
        return None
    out = []
    for it in lista:
        if isinstance(it, dict):
            txt = it.get("texto") or it.get("text") or it.get("claim") or ""
            out.append({"texto": str(txt), "nucleo": _como_bool(it.get("nucleo"))})
        elif isinstance(it, str):
            out.append({"texto": it, "nucleo": None})
    return out


# Pesos de la nota de extracción (suman 10 con todo perfecto).
PESO_RECALL = 8.5
PESO_NUCLEO = 1.5
DESCUENTO_INVENTADA = 1.0       # por claim con una cifra que no está en la fuente
TOPE_DESCUENTO = 3.0
CIFRA_MINIMA_INVENTADA = 13     # cifras ≤ 12 (meses, días, «Q1», conteos) no se juzgan


def detalle_extraccion(response: str, expected: dict) -> dict:
    """Desglose de la nota (útil para auditar un run y para las pruebas)."""
    plantados = expected.get("plantados") or []
    data = extraer_json(response)
    claims = _lista_claims(data) if data is not None else None
    if not plantados or claims is None:
        return {"nota": 0.0, "recall": 0.0, "encontrados": [], "faltantes": [p.get("id") for p in plantados],
                "inventados": [], "nucleo_ok": 0.0, "parseo": claims is not None}

    encontrados, faltantes, nucleo_hits = [], [], []
    for p in plantados:
        match = [c for c in claims if claim_coincide(p["anclas"], c["texto"])]
        if not match:
            faltantes.append(p["id"])
            continue
        encontrados.append(p["id"])
        esperado = bool(p.get("nucleo"))
        nucleo_hits.append(any(c["nucleo"] is esperado for c in match))

    cifras_fuente = expected.get("cifras_fuente")
    if cifras_fuente is None:
        cifras_fuente = normalizar_cifras(expected.get("fuente", ""))
    inventados = []
    for c in claims:
        for x in normalizar_cifras(c["texto"]):
            if x <= CIFRA_MINIMA_INVENTADA:
                continue
            if not any(_cerca(x, y) for y in cifras_fuente):
                inventados.append(c["texto"])
                break

    recall = len(encontrados) / len(plantados)
    nucleo_ok = (sum(nucleo_hits) / len(nucleo_hits)) if nucleo_hits else 0.0
    nota = PESO_RECALL * recall + PESO_NUCLEO * nucleo_ok * recall
    nota -= min(TOPE_DESCUENTO, DESCUENTO_INVENTADA * len(inventados))
    return {"nota": round(max(0.0, min(10.0, nota)), 2), "recall": round(recall, 3),
            "encontrados": encontrados, "faltantes": faltantes, "inventados": inventados,
            "nucleo_ok": round(nucleo_ok, 3), "parseo": True}


def score_noticias_extraccion(response: str, expected: dict) -> float:
    """Nota 0-10: 8,5 × recall + 1,5 × (acierto de `nucleo` × recall) − 1 por claim con
    cifra inventada (tope 3). El núcleo se pondera por el recall para que extraer 1 de 10
    con el núcleo bien marcado no sume 1,5 gratis. JSON que no parsea → 0."""
    return detalle_extraccion(response, expected)["nota"]


# ── verificación ─────────────────────────────────────────────────────────────

VEREDICTOS = ("RESPALDADO", "NO_RESPALDADO", "CONTRADICE")
_SINONIMOS = {
    "RESPALDADO": "RESPALDADO", "RESPALDA": "RESPALDADO", "SUPPORTED": "RESPALDADO",
    "NO_RESPALDADO": "NO_RESPALDADO", "SIN_RESPALDO": "NO_RESPALDADO",
    "NO_RESPALDA": "NO_RESPALDADO", "NOT_SUPPORTED": "NO_RESPALDADO",
    "CONTRADICE": "CONTRADICE", "CONTRADICHO": "CONTRADICE", "CONTRADICTED": "CONTRADICE",
    "CONTRADICTS": "CONTRADICE",
}


def normalizar_veredicto(v) -> str | None:
    s = _sin_acentos(str(v or "")).upper().strip()
    s = re.sub(r"[\s\-]+", "_", s)
    return _SINONIMOS.get(s)


def _id(v) -> str | None:
    m = re.search(r"\d+", str(v if v is not None else ""))
    return str(int(m.group())) if m else None


def detalle_verificacion(response: str, expected: dict) -> dict:
    esperados = {str(k): v for k, v in (expected.get("esperados") or {}).items()}
    data = extraer_json(response)
    lista = None
    if isinstance(data, dict):
        lista = data.get("veredictos")
        if lista is None:
            lista = next((v for v in data.values() if isinstance(v, list)), None)
    elif isinstance(data, list):
        lista = data
    devueltos: dict[str, str | None] = {}
    if isinstance(lista, list):
        for it in lista:
            if isinstance(it, dict):
                k = _id(it.get("id"))
                if k is not None and k not in devueltos:          # el primero manda
                    devueltos[k] = normalizar_veredicto(it.get("veredicto"))
    errores = {}
    for k, v in esperados.items():
        got = devueltos.get(k)
        if got != v:
            errores[k] = {"esperado": v, "devuelto": got}
    total = len(esperados)
    aciertos = total - len(errores)
    nota = round(10.0 * aciertos / total, 2) if total and isinstance(lista, list) else 0.0
    return {"nota": nota, "aciertos": aciertos, "total": total, "errores": errores,
            "devueltos": len(devueltos)}


def score_noticias_verificacion(response: str, expected: dict) -> float:
    """Nota 0-10 = 10 × veredictos correctos / afirmaciones enviadas. Faltante = error;
    CONTRADICE↔NO_RESPALDADO = error; JSON que no parsea → 0."""
    return detalle_verificacion(response, expected)["nota"]
