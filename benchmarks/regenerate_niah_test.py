#!/usr/bin/env python3
"""
Regenera el prompt EXACTO de un test NIAH-ES desde el corpus + config.

Uso:
    # Listar todos los tests disponibles
    python benchmarks/regenerate_niah_test.py --list

    # Imprimir el prompt completo de un test específico
    python benchmarks/regenerate_niah_test.py --name niah_es_discount_code_4000_p25

    # Guardarlo en un archivo
    python benchmarks/regenerate_niah_test.py --name niah_es_discount_code_4000_p25 --output /tmp/test.txt

Por qué este script existe:
NIAH-ES tiene inputs muy largos (hasta 1MB por test en context 256K). Guardar
todos los prompts inflados en git sería absurdo (12 tests × 1MB × N modelos).
En su lugar, guardamos:
- corpus snapshot (~1.1MB total) en `benchmarks/tests/niah_es_corpus/`
- config de needles + posiciones + contextos en `benchmarks/tests/niah_es.py`

Cualquiera con el repo puede regenerar el prompt EXACTO de cualquier test.
Este script automatiza ese proceso para auditoría / reproducibilidad.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from benchmarks.tests import niah_es


def main():
    parser = argparse.ArgumentParser(description="Regenera prompts de tests NIAH-ES")
    parser.add_argument("--list", action="store_true", help="Listar todos los tests")
    parser.add_argument("--name", help="Nombre del test a regenerar")
    parser.add_argument("--output", help="Guardar el prompt en este archivo")
    args = parser.parse_args()

    if args.list:
        print(f"Total tests NIAH-ES: {len(niah_es.TESTS)}")
        for t in niah_es.TESTS:
            prompt = t["messages"][0]["content"]
            print(f"  {t['name']:<55} prompt={len(prompt)} chars")
        return 0

    if not args.name:
        parser.print_help()
        return 1

    test = next((t for t in niah_es.TESTS if t["name"] == args.name), None)
    if not test:
        print(f"ERROR: test '{args.name}' no encontrado", file=sys.stderr)
        return 1

    prompt = test["messages"][0]["content"]
    expected = test.get("expected_answer", {})

    output = (
        f"# Test NIAH-ES: {test['name']}\n\n"
        f"**Descripción**: {test['description']}\n\n"
        f"**Prompt longitud**: {len(prompt)} caracteres ({len(prompt) // 4} tokens estimados)\n\n"
        f"**Patterns esperados (regex)**:\n"
    )
    for p in expected.get("exact_patterns", []):
        output += f"- `{p}`\n"
    output += f"\n**Keywords esperados**:\n"
    for k in expected.get("keywords", []):
        output += f"- `{k}`\n"
    output += f"\n---\n\n## Prompt completo\n\n{prompt}\n"

    if args.output:
        Path(args.output).write_text(output)
        print(f"Prompt guardado en: {args.output}")
    else:
        sys.stdout.write(output)

    return 0


if __name__ == "__main__":
    sys.exit(main())
