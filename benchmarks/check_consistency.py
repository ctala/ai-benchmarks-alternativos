#!/usr/bin/env python3
"""
Detecta scores hardcodeados en los docs vivos que ya no coinciden con la fuente.

EL BUG QUE ESTE SCRIPT EVITA
----------------------------
El `score_global` es un z-score normalizado contra toda la poblacion de modelos.
Consecuencia contra-intuitiva: **medir un modelo nuevo cambia el score de TODOS
los modelos anteriores.** Cualquier cifra escrita a mano en un doc queda obsoleta
sola, sin que nadie toque ese doc.

Julio 2026, real: el README publicaba Grok 4.5 = 6.99 y GPT-5.6 Luna = 7.92,
mientras el sitio (generado desde models.json) mostraba 5.84 y 8.14. Dos numeros
publicos distintos para el mismo modelo, en un proyecto cuyo unico activo es la
credibilidad de sus numeros.

DOCS VIVOS vs HISTORICOS
------------------------
- Vivos (se validan): describen el estado ACTUAL. Deben coincidir con la fuente.
- Historicos (se ignoran): CHANGELOG y DATASHEETs son snapshots con fecha. Un
  CHANGELOG que dice "en v3.1.1 el score era 6.99" es CORRECTO aunque hoy sea
  otro. Reescribir la historia seria el bug, no el fix.

Uso:
    python benchmarks/check_consistency.py          # reporta drift, exit 1 si hay
    python benchmarks/check_consistency.py -v       # muestra tambien lo que valida OK
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
MODELS_JSON = ROOT / "docs" / "data" / "models.json"

# Docs que describen el estado ACTUAL -> deben coincidir con models.json.
LIVE_DOCS = [
    "README.md",
    "MODELOS.md",
    "CLAUDE.md",
    "AGENTS.md",
    "RECOMENDACIONES.md",
    "COMPARATIVA.md",
]

# Docs vivos que además recomiendan modelos por nombre. Se revisan por MODELOS
# RETIRADOS (no por scores: varios son narrativos y sus cifras son de contexto).
# Auditado el 13-ago-2026: DIEZ documentos citaban modelos que ya no existen —
# Devstral Small entre ellos, que es el incidente que el propio CLAUDE.md documenta
# como conocido (llegó a ser #5 del ranking meses después de que su endpoint muriera).
# Un doc que recomienda un modelo muerto manda a alguien a integrarlo y estrellarse.
DOCS_QUE_RECOMIENDAN = LIVE_DOCS + [
    "COMPARATIVA.md", "SUSCRIPCIONES.md", "PACKS.md", "CASOS_DE_USO.md",
    "PROVEEDORES.md", "BENCHMARKS_EXTERNOS.md", "THINKING_EXPLAINED.md",
]

# Snapshots con fecha: conservan el valor del momento a proposito. No se tocan.
HISTORICAL_DOCS = ["CHANGELOG.md", "DATASHEET_", "INSIGHTS.md", "ESTADO_SESION.md"]

# ── LAS PÁGINAS DEL SITIO ─────────────────────────────────────────────────────
#
# POR QUÉ (14-ago-2026). Este chequeo cubría SEIS archivos `.md` y ni un solo HTML.
# Pero el sitio tiene 66 páginas y **3 de ellas no las genera nadie**: son a mano, con
# cifras escritas a mano. Llevaban 28 días sin tocarse, estaban en el sitemap, y
# `glm-5.2-explicado` publicaba «GLM 5.2 score global 6.93» cuando hoy es 6.20.
#
# Es la peor clase de superficie sin instrumento, porque **es la que ve Google**: los
# .md los lee quien entra al repo; estas páginas las lee quien busca en un buscador.
#
# Se chequean TODAS las páginas, generadas incluidas, a propósito. Una generada es
# consistente por construcción, así que no debería reportar nada — y si reporta, es un
# bug del generador, que también quiero saber. Nada de listar a mano cuáles son "las de
# a mano": esa lista sería otra superficie que se desincroniza.
def _paginas_del_sitio() -> list[Path]:
    docs = ROOT / "docs"
    if not docs.exists():
        return []
    out = []
    for p in sorted(docs.rglob("index.html")):
        t = p.read_text(errors="replace")
        # Los stubs de redirección (noindex + meta refresh) no publican cifras.
        if 'http-equiv="refresh"' in t and "noindex" in t:
            continue
        # Las GENERADAS llevan marca de origen (la pone `page_shell`): se rehacen desde
        # models.json en cada pipeline, así que no pueden caducar. Se saltan para que el
        # aviso de "sin verificar" señale SOLO lo que de verdad hay que vigilar — las
        # hechas a mano. Sin este filtro salían 42 avisos y el ruido tapaba a las 3 que
        # importaban.
        if "generado-por: benchmarks/" in t:
            continue
        # La calculadora (docs/index.html) no trata de UN modelo: los sirve a todos desde
        # models.json. No hay sujeto que atribuir, y su consistencia la cubre
        # `check_calculator.py` + el QA funcional.
        if p.parent == (ROOT / "docs"):
            continue
        out.append(p)
    return out


def _a_texto(html: str) -> str:
    """HTML → texto plano conservando los saltos de línea.

    El chequeo es por LÍNEA (un score y el modelo al que pertenece tienen que estar
    juntos para poder atribuirlo). Si se aplastaran los saltos, una página entera sería
    una sola línea con 40 modelos y 47 cifras: imposible decir cuál es de quién, que es
    exactamente el falso positivo que la versión .md ya aprendió a evitar.
    """
    html = re.sub(r"<(script|style)\b[^>]*>.*?</\1>", " ", html,
                  flags=re.S | re.I)
    html = re.sub(r"<[^>]+>", " ", html)
    html = html.replace("&nbsp;", " ").replace("&amp;", "&")
    return re.sub(r"[ \t]+", " ", html)

# Tolerancia: los docs redondean (8.1 vs 8.14). Solo marcamos drift real.
TOLERANCE = 0.05

# Claim de score EXPLICITO: la palabra "score" seguida del numero.
#   "score **5.84**"  "score global 7.2"  "score: 8.1"
# Deliberadamente estricto. Capturar cualquier numero de la linea daba 67
# falsos positivos: se comia el "4.5" de "Grok 4.5" como si fuera un score, y
# en lineas que listan varios modelos cruzaba todos los numeros contra todos.
SCORE_CLAIM_RE = re.compile(
    r"score\s*(?:global\s*)?[:=]?\s*\**\s*(\d{1,2}\.\d{1,2})\b", re.IGNORECASE
)


def load_models() -> dict:
    data = json.loads(MODELS_JSON.read_text())
    return {m["name"]: m for m in data.get("models", []) if m.get("score_global") is not None}


def plausible_values(m: dict) -> list[float]:
    """Valores que legitimamente pueden citarse de este modelo."""
    vals = []
    for key in ("score_global", "quality_avg", "score_global_linear"):
        v = m.get(key)
        if v is not None:
            vals.append(float(v))
    for v in (m.get("score_by_pillar") or {}).values():
        if v is not None:
            vals.append(float(v))
    return vals




# ── Páginas HTML: atribución por PÁGINA, no por línea ────────────────────────
#
# POR QUÉ (14-ago-2026). El chequeo de los .md atribuye un score al modelo nombrado en
# LA MISMA LÍNEA. En prosa markdown eso funciona; en HTML no, y se midió por qué:
#
#   «score global de 6.93»      → el regex no admite el "de", y la línea nombra 3 modelos
#   «score_global 6.93»         → el guion bajo rompe el patrón `score global`
#   «Score global 6.93 8.07»    → matchea, pero el nombre está en la cabecera de la tabla
#
# Las tres son la misma causa: en una página el nombre del modelo vive en el título o en
# un encabezado, lejos del número. Pero eso mismo da la solución — **la página es SOBRE
# un modelo**, y eso está en el slug. Así que se atribuye por página y se busca en todo
# el texto. Una comparación (`a-vs-b`) tiene dos sujetos: la cifra vale si coincide con
# cualquiera de los dos (conservador, pero sigue cazando la que no es de ninguno).
SCORE_EN_PAGINA_RE = re.compile(
    r"score[\s_]*(?:global|de calidad)?\s*(?:de\s+)?[:=]?\s*\**\s*(\d{1,2}\.\d{1,2})\b",
    re.IGNORECASE)


# Páginas cuyo slug NO permite deducir el modelo. Renombrar el slug rompería URLs que
# ya están indexadas, así que la atribución va acá, explícita. Es una lista corta y a
# mano — pero el chequeo AVISA de toda página sin sujeto, así que una que falte se nota
# sola en vez de pasar en silencio.
SUJETOS_EXPLICITOS = {
    "minimax-vs-kimi": ["MiniMax M3", "Kimi K2.6"],
    "diffusiongemma-vs-gemma-4": ["DiffusionGemma 26B-A4B (DGX Spark Q8_0)",
                                 "Gemma 4 26B MoE (3.8B activos)"],
}


def _sujetos_de_pagina(pg: Path, models: dict) -> list:
    """Modelos de los que trata la página, deducidos del slug."""
    if pg.parent.name in SUJETOS_EXPLICITOS:
        return [models[n] for n in SUJETOS_EXPLICITOS[pg.parent.name] if n in models]
    slug = pg.parent.name.lower().replace("_", "-")
    hallados = []
    for nombre, m in models.items():
        # "GLM 5.2" → "glm-5-2" / "glm-5.2"; se prueban las dos formas
        base = nombre.lower().replace(" ", "-")
        for cand in (base, base.replace(".", "-"), base.replace(".", "")):
            if cand and cand in slug:
                hallados.append(m)
                break
    # el match más largo gana: "glm-5.2" antes que "glm-5"
    hallados.sort(key=lambda m: -len(m["name"]))
    return hallados[:2]


def check_pagina(pg: Path, models: dict) -> list[str]:
    sujetos = _sujetos_de_pagina(pg, models)
    if not sujetos:
        # NO se devuelve vacío en silencio. Una página sin sujeto detectable queda SIN
        # VERIFICAR, y "verde porque no miré" es indistinguible de "verde porque está
        # bien" — que es exactamente el modo de falla que este chequeo vino a matar.
        # Medido: `diffusiongemma-vs-gemma-4` y `minimax-vs-kimi` caían acá.
        return [f"__SIN_SUJETO__{pg.parent.name}"]
    texto = _a_texto(pg.read_text(errors="replace"))
    # QUÉ CUENTA COMO VALOR VÁLIDO — y por qué NO son todos.
    #
    # La primera versión aceptaba `plausible_values` + seguridad + **las 20 y pico de
    # suites**. Medido: eso dejaba 54-67 valores distintos, que con tolerancia ±0,05
    # cubren entre el 54% y el 67% del rango 0-10. O sea que se le escapaban dos de cada
    # tres cifras caducas por azar — las de GLM 5.2 las cazó de suerte, porque 6,93 y
    # 2,53 cayeron en el hueco. Un detector que acepta dos tercios del espacio no es un
    # detector.
    #
    # Ahora entran los TITULARES (global, calidad, seguridad, pilares) siempre, y una
    # suite solo si su nombre aparece en la página — que es cuando citarla es legítimo.
    validos = set()
    texto_pg = _a_texto(pg.read_text(errors="replace"))
    bajo = texto_pg.lower()
    for m in sujetos:
        for k in ("score_global", "score_calidad", "quality_avg", "security_score"):
            if m.get(k) is not None:
                validos.add(round(float(m[k]), 2))
        for v in (m.get("score_by_pillar") or {}).values():
            if v is not None:
                validos.add(round(float(v), 2))
        for suite, v in (m.get("score_by_suite") or {}).items():
            if v is None:
                continue
            etiqueta = suite.replace("_", " ").replace(" es", "").strip()
            if suite.lower() in bajo or etiqueta.lower() in bajo:
                validos.add(round(float(v), 2))
    hallazgos = []
    vistos = set()
    for cifra in SCORE_EN_PAGINA_RE.findall(texto):
        v = round(float(cifra), 2)
        if v in vistos:
            continue
        vistos.add(v)
        if not any(abs(v - ok) <= TOLERANCE for ok in validos):
            quien = " / ".join(m["name"] for m in sujetos)
            # Se muestran los valores PRINCIPALES, no los 65 de todas las suites: un
            # mensaje que hay que leer con lupa no se lee.
            claves = []
            for m in sujetos:
                for et, k in (("global", "score_global"), ("calidad", "score_calidad"),
                              ("seguridad", "security_score")):
                    if m.get(k) is not None:
                        claves.append(f"{m['name']} {et} {float(m[k]):.2f}")
            hallazgos.append(
                f"{pg.parent.name}/index.html: publica {v} y no coincide con ningún "
                f"score de {quien} — hoy: {' · '.join(claves)}")
    return hallazgos


def check_doc(path: Path, models: dict, verbose: bool = False) -> list[str]:
    findings = []
    if not path.exists():
        return findings

    crudo = path.read_text(errors="replace")
    if path.suffix.lower() in (".html", ".htm"):
        crudo = _a_texto(crudo)

    for lineno, line in enumerate(crudo.splitlines(), 1):
        if "score" not in line.lower():
            continue

        # Que modelos se nombran en esta linea (match mas largo primero, para que
        # "GPT-5.6 Luna" gane sobre un hipotetico "GPT-5.6").
        mentioned = sorted(
            (n for n in models if n in line), key=len, reverse=True
        )
        if not mentioned:
            continue
        # Linea que lista VARIOS modelos: no se puede atribuir que numero es de
        # quien. Es una enumeracion narrativa, no un claim puntual. La saltamos.
        if len(mentioned) > 1:
            continue

        name = mentioned[0]
        m = models[name]

        # Sacar el nombre del texto antes de buscar numeros: si no, "Grok 4.5"
        # aporta un "4.5" que parece un score y no lo es.
        clean = line.replace(name, " ")
        claims = [float(n) for n in SCORE_CLAIM_RE.findall(clean)]
        if not claims:
            continue

        ok_vals = plausible_values(m)
        for n in claims:
            if any(abs(n - v) <= TOLERANCE for v in ok_vals):
                if verbose:
                    print(f"  OK  {path.name}:{lineno} — {name} = {n}")
                continue
            findings.append(
                f"{path.name}:{lineno} — «{name}» se publica con score {n}, "
                f"pero la fuente dice {m['score_global']} "
                f"(quality {m.get('quality_avg')}). → {line.strip()[:90]}"
            )
    return findings


def _chequear_retirados(root) -> list[str]:
    """¿Algún doc vivo sigue recomendando un modelo que ya no se puede usar?

    Es distinto del chequeo de scores: acá no importa si la cifra caducó, importa que
    el modelo NO EXISTE. El caso canónico es Devstral Small — estuvo #5 del ranking y
    en 11 páginas del sitio meses después de que Mistral apagara su endpoint.
    """
    import json as _json
    data = _json.loads((root / "docs" / "data" / "models.json").read_text())
    retirados = {m["name"]: m.get("retired_at") for m in data.get("models", [])
                 if isinstance(m, dict) and m.get("retired_at")}
    hallazgos = []
    for doc in dict.fromkeys(DOCS_QUE_RECOMIENDAN):
        p = root / doc
        if not p.exists():
            continue
        txt = p.read_text(encoding="utf-8", errors="ignore")
        # Distinguir RECOMENDAR de NOMBRAR. Varios docs citan a Devstral Small a
        # propósito —es el incidente que enseña por qué existe check_endpoints— y
        # marcarlos sería ruido que entrena a ignorar el guardrail. Si cerca de la
        # mención hay una marca de retiro, es narrativa deliberada.
        MARCAS = ("retir", "murió", "murio", "muerto", "deprec", "ya no existe",
                  "ya no", "desapareci", "apagó", "apago", "404", "histórico", "historico")
        citados = []
        for n in retirados:
            if not n or n not in txt:
                continue
            deliberadas = 0
            total = 0
            for i in range(len(txt)):
                i = txt.find(n, i if i else 0)
                if i < 0:
                    break
                total += 1
                ctx = txt[max(0, i - 250): i + 250].lower()
                if any(mk in ctx for mk in MARCAS):
                    deliberadas += 1
                if total > 12:
                    break
            # Solo alarma si hay menciones SIN contexto de retiro.
            if total > deliberadas:
                citados.append(n)
        if citados:
            hallazgos.append(
                f"{doc}: cita {len(citados)} modelo(s) RETIRADO(s) — "
                f"{', '.join(sorted(citados)[:4])}"
                + (" …" if len(citados) > 4 else "")
            )
    return hallazgos


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args()

    if not MODELS_JSON.exists():
        sys.exit(f"ERROR: falta {MODELS_JSON}. Corré export_for_pages.py primero.")

    models = load_models()
    all_findings = []
    for doc in LIVE_DOCS:
        all_findings += check_doc(ROOT / doc, models, args.verbose)

    # Las PÁGINAS del sitio, que hasta el 14-ago-2026 no miraba nadie. Se revisan todas
    # —generadas incluidas— a propósito: una generada es consistente por construcción y
    # no debería reportar nada; si reporta, es un bug del generador y también quiero
    # saberlo. Listar a mano cuáles son "las de a mano" sería otra superficie que se
    # desincroniza.
    paginas = _paginas_del_sitio()
    for pg in paginas:
        all_findings += check_pagina(pg, models)

    sin_sujeto = [f[len("__SIN_SUJETO__"):] for f in all_findings
                  if f.startswith("__SIN_SUJETO__")]
    all_findings = [f for f in all_findings if not f.startswith("__SIN_SUJETO__")]

    print(f"Validando {len(LIVE_DOCS)} docs vivos + {len(paginas)} páginas del sitio "
          f"contra models.json ({len(models)} modelos con score)…")
    if sin_sujeto:
        print(f"\n⚠️  {len(sin_sujeto)} página(s) SIN VERIFICAR — no se pudo deducir de qué "
              f"modelo tratan a partir del slug:")
        for x in sin_sujeto:
            print(f"    · {x}")
        print("    No es que estén bien: es que nadie las miró. Renombrá el slug para que "
              "contenga\n    el nombre del modelo, o agregá la atribución a mano.")
    print(f"(Ignorados por diseño — son snapshots con fecha: {', '.join(HISTORICAL_DOCS)})\n")

    # AVISO, no bloqueo: un doc que recomienda un modelo retirado es un problema real
    # —el caso Devstral Small— pero limpiarlo es trabajo editorial, no algo que un
    # pipeline deba exigir antes de dejar publicar una regeneración. Se reporta cada
    # vez para que no se olvide, y la decisión de cuándo limpiarlo es humana.
    retirados = _chequear_retirados(ROOT)
    if retirados:
        print(f"⚠️  {len(retirados)} doc(s) mencionan modelos RETIRADOS sin decir que lo están:")
        for r in retirados:
            print(f"    · {r}")
        print("    Un modelo que no se puede usar no es un candidato. Si la mención es")
        print("    deliberada (contar el incidente), agregá la palabra 'retirado' cerca.\n")

    if not all_findings:
        print("✅ Sin drift: los docs vivos coinciden con la fuente.")
        return 0

    print(f"❌ {len(all_findings)} score(s) desactualizado(s) en docs vivos:\n")
    for f in all_findings:
        print(f"  · {f}")
    print(
        "\nFix: corré `python benchmarks/regenerate_all.py` (regenera lo auto-generable) "
        "y corregí a mano las menciones narrativas que queden."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
