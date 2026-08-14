#!/usr/bin/env python3
"""
Guardrail de versión: que las 6 superficies que la declaran digan lo mismo.

POR QUÉ EXISTE (13-ago-2026)
----------------------------
Cristian: *"parte del problema es la falta de control de cambios y versiones."* Medido
en ese momento, la versión vivía en seis lugares y **dos estaban desfasados**:

    scoring_reference.json  v4.1
    docs/data/models.json   v4.1
    CHANGELOG.md            v4.1.0
    docs/index.html         v4.1
    git tag                 v4.0.0   ← nunca se taggeó v4.1
    README.md               v4.0     ← quedó viejo

Ninguno de esos desfases rompe nada: el sitio carga, el pipeline pasa, los auditores
dan verde. Simplemente **el repo dice tres versiones distintas de sí mismo** y quien
lea el README se lleva la vieja. Es el mismo patrón de siempre acá — una regla escrita
(«bumpear la versión») sin nada que la verifique.

QUÉ VERIFICA
------------
V1. Las fuentes de datos y docs vivos declaran la MISMA versión.
V2. Existe un git tag para la versión declarada. Sin tag no hay punto de retorno: no
    se puede reconstruir qué se publicó ni comparar contra el release anterior.
V3. El CHANGELOG tiene entrada para la versión declarada. Publicar sin entrada es
    exactamente lo que pasó con v4.1 hasta que Cristian lo marcó.

Uso:
    python benchmarks/check_version.py         # exit 1 si hay desfase
    python benchmarks/check_version.py --tag   # además, crea el tag faltante
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _norm(v: str | None) -> str | None:
    """v4.1.0 y v4.1 son la misma versión declarada. El CHANGELOG usa semver completo
    (v4.1.0) y el scoring usa la línea (v4.1): comparar crudo daría un falso positivo."""
    if not v:
        return None
    m = re.match(r"v?(\d+)\.(\d+)", v)
    return f"v{m.group(1)}.{m.group(2)}" if m else v


# ── EL REGISTRO DE SUPERFICIES ────────────────────────────────────────────────
#
# Ésta es la lista, y es la ÚNICA. Antes vivía repartida entre una docstring que
# decía "seis" y un `_leer()` que leía cuatro — y las dos que faltaban estaban
# desalineadas, claro. El 14-ago aparecieron TRES superficies no listadas en una
# sola sesión (README y los dos campos del schema.org).
#
# El problema nunca fue el olvido: era que **la lista no existía en ninguna parte
# verificable**. Un comentario en prosa no es un registro. Ahora agregar una
# superficie es agregar una fila acá, `SUPERFICIES.md` se genera de esta lista, y
# la doc no puede desincronizarse del chequeo porque no es una copia.
#
#   archivo · patrón (regex con 1 grupo, o clave si es JSON) · por qué importa
SUPERFICIES = [
    {"archivo": "scoring_reference.json", "json_key": "version",
     "que_es": "la referencia congelada del score",
     "por_que": "es la fuente de la calibración; si miente, todo score publicado queda sin origen"},
    {"archivo": "docs/data/models.json", "json_key": "scoring_version",
     "que_es": "el dataset que sirve el sitio",
     "por_que": "es lo que consume la calculadora y cualquiera que baje los datos"},
    {"archivo": "CHANGELOG.md", "patron": r"^## \[(v[\d.]+)\]",
     "que_es": "la entrada más reciente",
     "por_que": "publicar sin entrada es publicar sin traza. Pasó con v4.1"},
    {"archivo": "README.md", "patron": r"^\*\*Versi[oó]n?\s+(v?[\d.]+)\*\*",
     "que_es": "el encabezado",
     "por_que": "es lo primero que ve un humano y lo que GitHub muestra en la home del repo. "
                "El 14-ago decía «Version 3.1.1»: cuatro releases atrás"},
    {"archivo": "docs/index.html", "patron": r"Dataset <strong>(v[\d.]+)",
     "que_es": "el hero de la calculadora",
     "por_que": "es la versión que lee un visitante del sitio"},
    {"archivo": "docs/index.html", "patron": r'"version":\s*"(v[\d.]+)"',
     "etiqueta": "schema.org:version",
     "que_es": "el Dataset de schema.org",
     "por_que": "es lo que leen Google y los crawlers de IA. El 14-ago decía v4.0 "
                "mientras el hero decía v4.1, y nada fallaba"},
    {"archivo": "docs/index.html", "patron": r'"softwareVersion":\s*"(v[\d.]+)"',
     "etiqueta": "schema.org:softwareVersion",
     "que_es": "el SoftwareApplication de schema.org",
     "por_que": "ídem: superficie de buscadores, invisible para quien mira la página"},
    # Además de éstas, V2 exige un git tag y V3 una entrada en el CHANGELOG.
]


def _leer() -> dict:
    fuentes: dict[str, str | None] = {}
    for s in SUPERFICIES:
        p = ROOT / s["archivo"]
        etiqueta = s.get("etiqueta") or s["archivo"].split("/")[-1]
        if not p.exists():
            continue
        if "json_key" in s:
            try:
                fuentes[etiqueta] = json.loads(p.read_text()).get(s["json_key"])
            except Exception:
                fuentes[etiqueta] = None
        else:
            m = re.search(s["patron"], p.read_text(), re.M | re.I)
            fuentes[etiqueta] = m.group(1) if m else None
    return fuentes


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", action="store_true",
                    help="crear el git tag faltante para la versión declarada")
    args = ap.parse_args()

    fuentes = _leer()
    if not fuentes:
        print("✗ no encontré ninguna fuente de versión")
        return 1

    normadas = {k: _norm(v) for k, v in fuentes.items()}
    distintas = set(v for v in normadas.values() if v)

    print("  versión declarada por cada superficie:")
    for k, v in fuentes.items():
        print(f"     {k:<26} {v or '(no declara)'}")

    fallos = []

    # ── V1 · todas coinciden ────────────────────────────────────────────────
    if len(distintas) > 1:
        fallos.append(f"V1 · el repo declara {len(distintas)} versiones distintas de sí "
                      f"mismo: {sorted(distintas)}. Quien lea la superficie equivocada se "
                      f"lleva la vieja.")
    declarada = max(distintas, key=lambda v: [int(x) for x in v[1:].split(".")]) if distintas else None

    # ── V2 · existe el tag ──────────────────────────────────────────────────
    tags = subprocess.run(["git", "tag", "--list"], cwd=ROOT,
                          capture_output=True, text=True).stdout.split()
    tiene_tag = any(_norm(t) == declarada for t in tags)
    if declarada and not tiene_tag:
        if args.tag:
            nombre = fuentes.get("CHANGELOG.md") or declarada
            subprocess.run(["git", "tag", "-a", nombre, "-m",
                            f"Release {nombre}"], cwd=ROOT, check=True)
            print(f"\n  ✓ tag {nombre} creado (falta `git push --tags`)")
            tiene_tag = True
        else:
            fallos.append(f"V2 · no hay git tag para {declarada}. Sin tag no hay punto de "
                          f"retorno: no se puede reconstruir qué se publicó. "
                          f"Correr con --tag para crearlo.")

    # ── V3 · el CHANGELOG la registra ───────────────────────────────────────
    if declarada and _norm(fuentes.get("CHANGELOG.md")) != declarada:
        fallos.append(f"V3 · el CHANGELOG no tiene entrada para {declarada}. Se publicó "
                      f"sin dejar traza de qué cambió.")

    print()
    for f in fallos:
        print(f"    ❌ {f}")
    if fallos:
        print(f"\n  ❌ Control de versión roto ({len(fallos)} problema/s).")
        return 1
    print(f"  ✅ Las {len(fuentes)} superficies declaran {declarada}, con tag y CHANGELOG.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
