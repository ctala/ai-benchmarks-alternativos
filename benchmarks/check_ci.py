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
  CI1  El último estado del Action no lleva 2 días o más en rojo. Se cuenta en DÍAS desde
       el primer rojo posterior al último verde, no en fallos seguidos (ver abajo).
  CI2  Si el Action de `main` declara `schedule:`, tiene que haber corrido en los últimos
       2 días. Con el cron diario, el silencio también es un fallo: GitHub apaga los crons
       de un repo sin actividad y eso no deja ningún run rojo que ver.

POR QUÉ DÍAS Y NO RACHA (3-nov-2026, corte-v5 1.6)
--------------------------------------------------
Hasta hoy CI2 exigía 3 fallos seguidos, y el Action corría solo cuando un push tocaba
ciertos paths. El 11-oct falló UNA vez (`check_caminos`, por los PRs #26/#27 mergeados en
GitHub) y no volvió a correr hasta el 3-nov: 23 días en rojo con una racha de 1, que nunca
llegaba a 3 (AUDITORIA-GUARDRAILS-2026-11, H1). Además `qa.py` lo llamaba sin `--duro`, así
que devolvía 0 siempre y el QA imprimía ✅ encima de esos 23 días.

Ahora el Action corre en todo push a `main` y una vez al día, y este chequeo mira cuánto
lleva el último estado en rojo. Dos días son unas dos corridas del cron: margen para
arreglar un rojo de hoy sin alarma, y ninguno para que se olvide. Sigue INFORMATIVO en el
QA (depende de la red y de `gh`); lo que cambia es que sale con 1 cuando encuentra el
problema y el QA muestra ⚠️ (DECISIONES.md, 3-nov-2026).

CI2 se decide leyendo el YAML de `origin/main`, no el de la rama: el cron solo corre desde
la rama por defecto. Mientras el corte no se mergea, la rama declara `schedule:` y `main`
no, y exigir corridas diarias sería un ⚠️ diario por una ausencia esperada.

Requiere `gh` autenticado. Sin él, avisa y sale 0: no es un fallo del repo no tener el
CLI instalado.

Uso:
    python benchmarks/check_ci.py
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORKFLOW = "Regenerar artefactos auto-generados"
YAML = ".github/workflows/regenerate-auto-artifacts.yml"
DIAS_ROJO = 2         # CI1: días con el último estado en rojo que se toleran
DIAS_SILENCIO = 2     # CI2: días sin ninguna corrida, si hay cron declarado
ROJOS = {"failure", "timed_out", "startup_failure"}
# `cancelled`, `skipped` y `neutral` no dicen nada del estado del repo: se ignoran.


def _runs():
    """Las últimas corridas del Action, más nueva primero. None si `gh` no responde."""
    env = {k: v for k, v in os.environ.items() if k != "GITHUB_TOKEN"}
    try:
        r = subprocess.run(
            ["gh", "run", "list", "--workflow", WORKFLOW, "--limit", "30",
             "--json", "conclusion,createdAt,status,event"],
            capture_output=True, text=True, timeout=45, env=env, cwd=ROOT)
    except Exception:
        return None
    if r.returncode != 0:
        return None
    try:
        return json.loads(r.stdout or "[]")
    except json.JSONDecodeError:
        return None


def _yaml_de_main() -> str:
    """El YAML del Action tal como lo corre GitHub: el de `origin/main`."""
    r = subprocess.run(["git", "show", f"origin/main:{YAML}"],
                       capture_output=True, text=True, cwd=ROOT)
    return r.stdout if r.returncode == 0 else ""


def declara_schedule(yaml: str) -> bool:
    return re.search(r"^\s*schedule\s*:", yaml, re.M) is not None


def _fecha(s: str) -> datetime:
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def _ahora() -> datetime:
    return datetime.now(timezone.utc)


def main() -> int:
    argparse.ArgumentParser(description=__doc__.split("\n")[0]).parse_args()

    runs = _runs()
    if runs is None:
        print("  ⚠️  `gh` no disponible, sin autenticar o sin respuesta: se omite el chequeo del CI.")
        return 0
    ahora = _ahora()
    con_cron = declara_schedule(_yaml_de_main())
    print(f"CI — «{WORKFLOW}»" + (" · con cron diario en main" if con_cron else "") + "\n")

    problemas = []
    if con_cron:
        if not runs:
            problemas.append("main declara un cron y el Action no tiene ninguna corrida.")
        else:
            silencio = (ahora - _fecha(runs[0]["createdAt"])).total_seconds() / 86400
            if silencio >= DIAS_SILENCIO:
                problemas.append(f"main declara un cron diario y el Action no corre hace "
                                 f"{silencio:.0f} días: el seguro está apagado aunque nada esté rojo.")
    if not runs:
        print("  ⚠️  el Action no tiene runs registrados.")

    hechos = [x for x in runs if x.get("status", "completed") == "completed"
              and x.get("conclusion") in ROJOS | {"success"}]
    rojos = []
    for x in hechos:
        if x["conclusion"] == "success":
            break
        rojos.append(x)
    ultimo_ok = next((x for x in hechos if x["conclusion"] == "success"), None)
    if hechos:
        print(f"  últimas {len(hechos)} corridas con veredicto · "
              f"{sum(1 for x in hechos if x['conclusion'] == 'success')} en verde")
    if ultimo_ok:
        print(f"  último verde: {ultimo_ok['createdAt'][:10]}")
    if rojos:
        desde = _fecha(rojos[-1]["createdAt"])
        dias = (ahora - desde).total_seconds() / 86400
        msg = (f"el último estado del Action es ROJO desde el {desde.date()} "
               f"({dias:.0f} días, {len(rojos)} corrida(s))")
        if dias >= DIAS_ROJO:
            problemas.append(msg + f": pasó el margen de {DIAS_ROJO} días.")
        else:
            print(f"  ⚠️  {msg}; queda margen hasta los {DIAS_ROJO} días.")

    if not problemas:
        print("\n  ✅ el CI está vivo y no lleva días en rojo.")
        return 0
    for p in problemas:
        print(f"\n  ❌ {p}")
    print("\n     Es el seguro que regenera los artefactos cuando alguien no los")
    print("     regenera a mano. Mientras esté rojo o callado, ese seguro NO existe.")
    print("     Ver:  gh run list --workflow \"" + WORKFLOW + "\"")
    print("           gh run view <id> --log-failed")
    return 1


if __name__ == "__main__":
    sys.exit(main())
