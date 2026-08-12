#!/usr/bin/env python3
"""
Genera PROMPTS.md — el texto EXACTO de cada test del benchmark, con su huella.

POR QUÉ EXISTE
--------------
"No me sirve el resultado si no sé lo que se envió" (Cristian, 12-ago-2026). La
trazabilidad era el objetivo desde el principio y estaba a medias: se guardaba la
respuesta de cada test y no la pregunta.

El `.md` de cada run ya guarda su entrada desde hoy, pero eso solo cubre las corridas
NUEVAS y duplica el mismo texto en miles de archivos. Este catálogo resuelve lo otro:
**una sola copia, versionada en git, del texto exacto de cada prompt**, con el `prompt_sha`
que lo liga a los runs.

Entonces la cadena de trazabilidad queda cerrada:

    run en el JSON  ──prompt_sha──>  PROMPTS.md  ──git log──>  historia del prompt

Si alguien cambia un prompt, el hash del catálogo cambia y deja de coincidir con el de los
runs viejos. Eso es exactamente lo que la regla dura "no modificar prompts de tests"
pedía y nadie verificaba.

QUÉ NO ENTRA, Y POR QUÉ
-----------------------
`niah_es` genera su prompt: un haystack de hasta 800.000 tokens por test. Escribirlo sería
inviable (cientos de MB) y además inútil: es determinista a partir del corpus commiteado
más `needle` y `posición`. Va la RECETA, que lo regenera idéntico.

Uso:
    python benchmarks/generate_prompts_catalog.py           # imprime a stdout
    python benchmarks/generate_prompts_catalog.py -o PROMPTS.md
"""
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from benchmarks.runner import ALL_TEST_SUITES, _prompt_sha  # noqa: E402


def _bloque(texto: str) -> str:
    """Cita el texto sin que sus backticks rompan el markdown del catálogo."""
    t = (texto or "").rstrip()
    cerca = "`" * max(4, max((len(m) for m in __import__("re").findall(r"`+", t)), default=0) + 1)
    return f"{cerca}\n{t}\n{cerca}"


def construir() -> str:
    L = [
        "# Prompts del benchmark — texto exacto",
        "",
        "> **Auto-generado por `benchmarks/generate_prompts_catalog.py`. No editar a mano.**",
        "",
        "Este archivo existe porque **un resultado sin su entrada no es auditable**: no se",
        "puede reproducir ni discutir. Cada test se lista con el texto exacto que recibe el",
        "modelo y con su `prompt_sha`, la misma huella que cada run guarda en el JSON.",
        "",
        "**Cómo se usa:** tomá el `prompt_sha` de un run y buscalo acá. Si no aparece, ese run",
        "se midió con un prompt que ya no existe — y entonces **no es comparable** con los",
        "actuales, por más que el nombre del test sea el mismo.",
        "",
        "**`niah_es` no lleva su texto**: el haystack llega a 800.000 tokens por test. Va la",
        "receta de generación, que lo reconstruye idéntico desde el corpus commiteado.",
        "",
    ]
    total = 0
    for suite, tests in sorted(ALL_TEST_SUITES.items()):
        L += [f"## `{suite}` — {len(tests)} tests", ""]
        for t in tests:
            sha = _prompt_sha(t)
            total += 1
            L += [f"### {t.get('name','?')}", "",
                  f"- `prompt_sha`: **`{sha}`**",
                  f"- {t.get('description','(sin descripción)')}"]
            tipo = (t.get("expected_answer") or {}).get("type")
            if tipo:
                L.append(f"- verificador: `{tipo}`")
            L.append("")

            if t.get("context_tokens"):          # niah: receta, no cuerpo
                L += ["**Entrada generada (no almacenada):**", "",
                      f"- `context_tokens`: {t.get('context_tokens')}",
                      f"- `needle_idx`: {t.get('needle_idx')} · `position_pct`: {t.get('position_pct')}",
                      "- corpus commiteado en `benchmarks/tests/niah_es_corpus/`", ""]
            elif t.get("type") == "multi_turn_script":
                L += ["**System:**", "", _bloque(t.get("system_prompt", "")), "",
                      f"**Guion del usuario ({len(t.get('script', []))} turnos):**", ""]
                for i, paso in enumerate(t.get("script", []), 1):
                    u = paso.get("user", "") if isinstance(paso, dict) else str(paso)
                    L += [f"*Turno {i}:*", "", _bloque(u), ""]
            else:
                for m in t.get("messages", []):
                    L += [f"**{m.get('role','?').capitalize()}:**", "", _bloque(str(m.get("content", ""))), ""]
    L.insert(3, f"**{total} tests en {len(ALL_TEST_SUITES)} suites.**\n")
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--output", default=None)
    a = ap.parse_args()
    txt = construir()
    if a.output:
        Path(a.output).write_text(txt)
        print(f"escrito → {a.output} ({len(txt)/1024:.0f} KB)")
    else:
        print(txt)
    return 0


if __name__ == "__main__":
    sys.exit(main())
