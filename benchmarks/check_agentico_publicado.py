#!/usr/bin/env python3
"""¿Se publicó un modelo en el ranking sin haberle corrido la tarea agéntica?

POR QUÉ EXISTE (22-ago-2026)
----------------------------
Cristian, al ver GLM 5.3 recién publicado: *"¿de nuevo no usaste harbor antes de
publicar un modelo?"*. **De nuevo**, sí — y esa es la parte que importa. La primera vez
fueron 12 modelos, se corrigió a mano; la segunda, 5 GPT; la tercera, GLM 5.3 el mismo
día de su release. Tres veces el mismo hueco, arreglado tres veces sin dejar nada que
lo detecte.

Publicar un modelo sin tarea agéntica no rompe ninguna página: entra al ranking, se ve
completo, y lo único que pasa es que el eje agéntico y el wizard **no pueden
recomendarlo** — desaparece de la pregunta «para agentes» sin decir por qué. Es un hueco
que no se nota desde afuera, que es exactamente la clase que este repo caza.

QUÉ VERIFICA
------------
  A1  Todo modelo rankeado servido por OpenRouter tiene tarea agéntica medida.

LO QUE NO CUENTA COMO FALTA
---------------------------
Un modelo servido por otro proveedor (`openai_direct`, `claude_code`, NIM, Groq) NO
puede heredar el resultado de OpenRouter: es otro endpoint, con su config. Eso ya lo
decide `export_for_pages` y acá se respeta — se listan aparte, como deuda declarada, no
como fallo. Correrles Harbor exige lanzarlo por SU ruta, que es otro trabajo.

Uso:
    python benchmarks/check_agentico_publicado.py
    python benchmarks/check_agentico_publicado.py --duro   # exit 1 si falta alguno
"""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODELS_JSON = ROOT / "docs" / "data" / "models.json"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--duro", action="store_true",
                    help="exit 1 si algún rankeado por OpenRouter no tiene tarea agéntica")
    a = ap.parse_args()

    sys.path.insert(0, str(ROOT / "benchmarks"))
    from models import MODELS

    d = json.loads(MODELS_JSON.read_text())
    rank = [m for m in d["models"] if m.get("ranked")]
    faltan, otra_ruta = [], []
    for m in rank:
        if (m.get("agentico") or {}).get("tareas"):
            continue
        cfg = MODELS.get(m.get("key") or "", {})
        prov = cfg.get("provider", "openrouter")
        (faltan if prov == "openrouter" else otra_ruta).append((m["name"], cfg.get("id"), prov))

    con = len(rank) - len(faltan) - len(otra_ruta)
    print("TAREA AGÉNTICA EN LO PUBLICADO\n")
    print(f"  A1 · rankeados con tarea real ejecutada: {con}/{len(rank)}")
    if otra_ruta:
        print(f"\n  ℹ️  {len(otra_ruta)} servidos por otra ruta — no pueden heredar el "
              f"resultado de OpenRouter:")
        for n, i, p in otra_ruta:
            print(f"     {n:<24} {str(i):<18} ({p})")
    if not faltan:
        print("\n  ✅ todo rankeado por OpenRouter tiene su tarea agéntica medida.")
        return 0
    print(f"\n  ❌ {len(faltan)} rankeado(s) publicados SIN tarea agéntica:\n")
    for n, i, p in faltan:
        print(f"     {n:<24} {i}")
    print("\n     No rompe ninguna página: entran al ranking y se ven completos. Lo que")
    print("     pasa es que el eje agéntico y el wizard NO pueden recomendarlos, y nada")
    print("     lo dice. Correr:")
    print("       harbor run -p tareas-agente/<tarea> -a mini-swe-agent \\")
    print("         -m openrouter/<id> -k 3 -n 3 --agent-env \"OPENROUTER_API_KEY=$K\"")
    print("     y después `python benchmarks/export_harbor.py`.")
    return 1 if a.duro else 0


if __name__ == "__main__":
    sys.exit(main())
