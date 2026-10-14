#!/usr/bin/env python3
"""
Agrega el campo 'jubilado' a los modelos en models.py basándose en
docs/jubilacion-2026-10.json.

Este script NO modifica models.py directamente. Imprime las claves
que deberían marcarse como jubilado para actualización manual o
para uso en export_for_pages.py.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    jubilacion_path = ROOT / "docs" / "jubilacion-2026-10.json"
    
    with open(jubilacion_path) as f:
        data = json.load(f)
    
    # Conjuntos de modelos jubilados
    dominados = {m["key"] for m in data["listas"]["dominados_jubilados"]}
    retired = {m["key"] for m in data["listas"]["retired"]}
    provider_variant = {m["key"] for m in data["listas"]["provider_variant"]}
    sin_runs = {m["key"] for m in data["listas"]["sin_runs"]}
    
    all_jubilados = dominados | retired | provider_variant | sin_runs
    
    print(f"Total modelos jubilados: {len(all_jubilados)}")
    print(f"  - Dominados: {len(dominados)}")
    print(f"  - Retired: {len(retired)}")
    print(f"  - Provider variant: {len(provider_variant)}")
    print(f"  - Sin runs: {len(sin_runs)}")
    print()
    
    # Verificar totales
    expected = data["jubilados"]
    if len(all_jubilados) != expected:
        print(f"⚠️  Warning: Se esperaban {expected} jubilados pero se encontraron {len(all_jubilados)}")
    else:
        print(f"✓ Total coincide con jubilacion-2026-10.json: {expected}")
    
    print()
    print("=" * 80)
    print("Para uso en export_for_pages.py y otros generadores:")
    print("=" * 80)
    print()
    
    # Generar código Python para usar en otros scripts
    print("# Conjunto de modelos jubilados (no se vuelven a medir)")
    print("JUBILADOS = {")
    for key in sorted(all_jubilados):
        motivo = ""
        if key in dominados:
            motivo = "dominado"
        elif key in retired:
            motivo = "retired"
        elif key in provider_variant:
            motivo = "provider_variant"
        elif key in sin_runs:
            motivo = "sin_runs"
        print(f'    "{key}",  # {motivo}')
    print("}")
    
    print()
    print("=" * 80)
    print("Modelos activos (para verificación):")
    print("=" * 80)
    activos = {m["key"] for m in data["listas"]["activos"]}
    print(f"Total activos: {len(activos)}")
    
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
