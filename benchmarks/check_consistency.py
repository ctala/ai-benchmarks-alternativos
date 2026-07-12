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

# Snapshots con fecha: conservan el valor del momento a proposito. No se tocan.
HISTORICAL_DOCS = ["CHANGELOG.md", "DATASHEET_", "INSIGHTS.md", "ESTADO_SESION.md"]

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


def check_doc(path: Path, models: dict, verbose: bool = False) -> list[str]:
    findings = []
    if not path.exists():
        return findings

    for lineno, line in enumerate(path.read_text().splitlines(), 1):
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

    print(f"Validando {len(LIVE_DOCS)} docs vivos contra models.json "
          f"({len(models)} modelos con score)…")
    print(f"(Ignorados por diseño — son snapshots con fecha: {', '.join(HISTORICAL_DOCS)})\n")

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
