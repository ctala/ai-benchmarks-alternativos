#!/usr/bin/env python3
"""¿El Action que regenera los artefactos está vivo, o lleva semanas en rojo?

POR QUÉ EXISTE (22-ago-2026)
----------------------------
Cristian reenvió un correo de GitHub: *«Run failed: Regenerar artefactos
auto-generados»*. Al mirarlo, **el último run verde había sido el 13 de julio: 40 días
antes, con 52 de los últimos 60 en rojo.**

Ese Action es el seguro del repo — el que regenera `models.json`, MODELOS.md, el
sitemap y corre los guardrails cuando a alguien se le olvida hacerlo a mano. Llevaba mes
y medio sin correr, y todo ese tiempo el `README.md` de CLAUDE.md seguía diciendo «si
olvidás los pasos manualmente, el bot regenera los artefactos al hacer push».

La causa técnica fue trivial (`export_for_pages.py` importa una CONSTANTE de
`providers/adapters.py`, y ese módulo hace `from openai import OpenAI` en su cabecera:
el Action no instalaba el SDK). Lo que no fue trivial es **por qué nadie se enteró en 40
días**: el aviso llega por correo, a una bandeja con 118.000 mensajes. Un canal que se
pierde en el ruido es un canal que no existe.

Por eso este chequeo vive acá, en el QA local, donde sí se mira: el estado del CI tiene
que ser visible desde donde se trabaja, no solo desde una notificación que se archiva
sola.

QUÉ VERIFICA
------------
  CI1  El último run del Action de artefactos no está en rojo.
  CI2  No hay una racha de fallos (≥3) — un rojo aislado puede ser un flake de red;
       tres seguidos es algo roto.

Requiere `gh` autenticado. Sin él, avisa y sale 0: no es un fallo del repo no tener el
CLI instalado.

Uso:
    python benchmarks/check_ci.py
    python benchmarks/check_ci.py --duro    # exit 1 si el CI está en rojo
"""

import argparse
import json
import os
import subprocess
import sys

WORKFLOW = "Regenerar artefactos auto-generados"
RACHA_MALA = 3


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--duro", action="store_true")
    a = ap.parse_args()

    env = {k: v for k, v in os.environ.items() if k != "GITHUB_TOKEN"}
    try:
        r = subprocess.run(
            ["gh", "run", "list", "--workflow", WORKFLOW, "--limit", "20",
             "--json", "conclusion,createdAt,headSha"],
            capture_output=True, text=True, timeout=45, env=env)
    except Exception as e:
        print(f"  ⚠️  no se pudo consultar el CI ({type(e).__name__}): se omite.")
        return 0
    if r.returncode != 0:
        print("  ⚠️  `gh` no disponible o sin autenticar: se omite el chequeo del CI.")
        return 0
    try:
        runs = json.loads(r.stdout or "[]")
    except json.JSONDecodeError:
        print("  ⚠️  respuesta inesperada de `gh`: se omite.")
        return 0
    if not runs:
        print("  ⚠️  el Action no tiene runs registrados.")
        return 0

    hechos = [x for x in runs if x.get("conclusion")]
    racha = 0
    for x in hechos:
        if x["conclusion"] == "failure":
            racha += 1
        else:
            break
    ok = sum(1 for x in hechos if x["conclusion"] == "success")
    ultimo_ok = next((x for x in hechos if x["conclusion"] == "success"), None)

    print(f"CI — «{WORKFLOW}»\n")
    print(f"  últimos {len(hechos)} runs: {ok} en verde · racha de fallos actual: {racha}")
    if ultimo_ok:
        print(f"  último verde: {ultimo_ok['createdAt'][:10]}")
    if racha == 0:
        print("\n  ✅ el CI está en verde.")
        return 0
    print(f"\n  ❌ el Action lleva {racha} run(s) seguidos en rojo"
          + (f", y el último verde fue el {ultimo_ok['createdAt'][:10]}." if ultimo_ok
             else " y no hay ninguno verde a la vista."))
    print("\n     Es el seguro que regenera los artefactos cuando alguien no los")
    print("     regenera a mano. Mientras esté rojo, ese seguro NO existe.")
    print("     Ver:  gh run list --workflow \"" + WORKFLOW + "\"")
    print("           gh run view <id> --log-failed")
    return 1 if (a.duro and racha >= RACHA_MALA) else 0


if __name__ == "__main__":
    sys.exit(main())
