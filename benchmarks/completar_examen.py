#!/usr/bin/env python3
"""Detecta y completa los exámenes a medias que dejan modelos FUERA del ranking.

POR QUÉ EXISTE (15-ago-2026)
----------------------------
Cristian, al ver que Nemotron 3 Super tenía 131 runs y no rankeaba: *"¿por qué no
detectamos estas falencias antes?"*

Porque el sistema **lo sabía y no lo decía**. `export_for_pages` guarda
`suites_incompletas` por modelo y bloquea el ranking cuando una suite que SÍ puntúa quedó
a medias —lo cual es correcto: un promedio construido sobre 1 de 4 tests no es comparable
con uno de 4 de 4—. Pero `MODELOS.md` los muestra en *«En evaluación»* sin el motivo, así
que dos situaciones opuestas se ven idénticas:

    «le faltan 50 runs»   → caro, lento, hay que decidir si vale la pena
    «le faltan 2 tests»   → centavos, minutos, es puro olvido

Medido el día que se escribió esto: **7 modelos bloqueados por 36 tests sueltos en
total**. Entre ellos **GPT-5.6 Luna Pro con calidad 8,60 — más alta que el #1 del ranking
publicado— afuera por DOS tests.**

Es el mismo patrón que el repo persigue hace tiempo: los detectores cazan AUSENCIA de
datos, y esto es *presencia de datos incompletos*, que pasa todos los chequeos.

Uso:
    python benchmarks/completar_examen.py                 # solo reporta
    python benchmarks/completar_examen.py --resume-file   # arma el JSON de resume
    python benchmarks/completar_examen.py --correr        # reporta y completa
"""

import argparse
import glob
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODELS_JSON = ROOT / "docs" / "data" / "models.json"
RESULTS = ROOT / "benchmarks" / "results"
PY = str(ROOT / ".venv" / "bin" / "python")

# Los pilares que se reportan aparte NO bloquean el ranking (su score va por separado),
# así que un examen incompleto ahí no es una falencia que corresponda completar acá.
PILARES_APARTE = ("niah", "prompt_injection")


def bloqueados() -> list[dict]:
    """Modelos con muestra suficiente que NO rankean por exámenes a medias."""
    d = json.loads(MODELS_JSON.read_text())
    out = []
    for m in d["models"]:
        if m.get("ranked") or not m.get("tested"):
            continue
        if m.get("retired") or m.get("provider_variant") or m.get("self_hosted"):
            continue
        if ":free" in (m.get("id") or "") or (m.get("runs") or 0) < 50:
            continue
        # NO proponer lo que la política dice que no se mide. El detector sabía detectar
        # el examen a medias y no conocía las reglas de QUÉ vale la pena medir, así que
        # proponía gastar en dos casos donde el gasto no sirve de nada:
        #
        #   · VARIANTES DE ESFUERZO (`-Pro` al mismo precio): no rankean por decisión del
        #     15-ago-2026. Completarles el examen no las mete al ranking — cuesta y no
        #     cambia nada. Eran 2 de los 7 que proponía, y los dos primeros de la lista.
        #   · MODELOS DE MÁS DE UN AÑO: el benchmark existe para decidir qué poner en
        #     producción HOY. Qwen 2.5 (sep-2024) pedía 18 tests, la mitad del total.
        #
        # Es el patrón de siempre acá: una decisión escrita que no llegó a la superficie
        # que la necesitaba.
        if "esfuerzo" in (m.get("notes") or "").lower():
            continue
        if m.get("no_medir") or m.get("legacy"):
            continue
        inc = {s: i for s, i in (m.get("suites_incompletas") or {}).items()
               if not s.startswith(PILARES_APARTE)}
        if inc:
            out.append({"key": m["key"], "name": m["name"], "id": m["id"],
                        "runs": m["runs"], "calidad": m.get("score_calidad"),
                        "incompletas": inc,
                        "faltan": sum(i["total"] - i["rindio"] for i in inc.values())})
    return sorted(out, key=lambda x: -(x["calidad"] or 0))


def armar_resume(model_id: str, destino: Path) -> int:
    """Consolida TODOS los runs existentes de un modelo en un solo JSON.

    `--resume` del runner saltea los tests ya completados, pero toma UN archivo. Los runs
    de un modelo viven repartidos en decenas de `benchmark_*.json`, así que hay que
    juntarlos primero. Sin esto, completar un examen significa re-correrlo entero y
    duplicar runs que ya estaban bien.
    """
    runs = []
    for f in glob.glob(str(RESULTS / "*.json")):
        try:
            d = json.load(open(f))
        except Exception:
            continue
        items = d if isinstance(d, list) else d.get("results", [])
        for r in items:
            if not isinstance(r, dict):
                continue
            if r.get("model_id") != model_id and r.get("model") != model_id:
                continue
            # SOLO los EXITOSOS. Consolidar también los fallidos hacía que este script no
            # pudiera hacer su único trabajo, y lo hacía en silencio.
            #
            # `--resume` saltea por `(model_id, suite, test)`. El export, en cambio, solo
            # cuenta runs con `success=True`. Un test que falló las cuatro veces aparece
            # así: **incompleto para el export y completo para el resume**. Resultado: el
            # runner lo saltea, el modelo sigue bloqueado, y el script imprime
            # «✅ exámenes completados» sin haber corrido un solo test.
            #
            # Medido el 16-ago-2026: los 3 modelos que se intentaron desbloquear crearon
            # sus directorios de respuestas VACÍOS y no hubo un solo run nuevo. GPT-5.5
            # tenía `social_engineering_attempt` con 4 corridas, las 4 con `success=False`
            # — justo el test que faltaba.
            if not r.get("success"):
                continue
            runs.append(r)
    destino.write_text(json.dumps({"results": runs}, ensure_ascii=False), encoding="utf-8")
    return len(runs)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--correr", action="store_true", help="completar los exámenes, no solo reportar")
    ap.add_argument("--modelos", nargs="*", help="limitar a estas keys")
    a = ap.parse_args()

    b = bloqueados()
    if a.modelos:
        b = [x for x in b if x["key"] in a.modelos]

    if not b:
        print("  ✅ ningún modelo con muestra suficiente está bloqueado por exámenes a medias.")
        return 0

    print(f"\n  ⚠️  {len(b)} modelo(s) con ≥50 runs FUERA del ranking por exámenes a medias:\n")
    total = 0
    for x in b:
        total += x["faltan"]
        print(f"  {x['name'][:34]:<36} calidad {str(x['calidad']):>5} · {x['runs']:>3} runs · "
              f"faltan {x['faltan']:>2} tests")
        for s, i in x["incompletas"].items():
            print(f"        {s:<26} {i['rindio']}/{i['total']}")
    print(f"\n  {total} tests sueltos para desbloquear a los {len(b)}.")
    print("  No es «falta medir»: es un examen empezado y no terminado, y cuesta centavos.")

    if not a.correr:
        print("\n  (solo reporte — correr con --correr para completarlos)")
        return 1

    # El archivo va en `results/` y se llama `benchmark_*`, NO en un subdirectorio.
    #
    # El runner hace `results_file = resume_path`: escribe SOBRE el archivo de resume. Y
    # `load_all_results()` solo lee `benchmark_*.json` del directorio `results/` —ni
    # subdirectorios, ni otros prefijos—. Con el resume en `_resume_tmp/resume_*.json`,
    # todo lo que este script midiera caía en un limbo que el pipeline no mira: los
    # modelos seguían bloqueados aunque los tests hubieran corrido perfecto.
    #
    # Es la otra mitad del fallo del 16-ago-2026: el primero impedía que los tests
    # corrieran; éste tiraba el resultado si corrían. Los dos en silencio.
    res = ROOT / "benchmarks" / "results"
    for x in b:
        rf = res / f"benchmark_completar_{x['key']}.json"
        n = armar_resume(x["id"], rf)
        suites = sorted(x["incompletas"])
        print(f"\n▶ {x['name']} — {n} runs previos consolidados, suites: {', '.join(suites)}")
        cmd = [PY, str(ROOT / "benchmarks" / "runner.py"), "--judge", "--judge-model", "phi4",
               "--models", x["key"], "--tests", *suites, "--resume", str(rf), "--sin-canario"]
        subprocess.run(cmd, cwd=ROOT)
    # VERIFICAR QUE ALGO CORRIÓ. La v1 imprimía «✅ exámenes completados» sin mirar nada,
    # y el 16-ago-2026 lo dijo después de no correr un solo test: los tres modelos
    # crearon su directorio de respuestas VACÍO y siguieron bloqueados. Un script que
    # reporta éxito sin comprobarlo es peor que uno que falla — hace perder el rastro.
    # Se verifica contra los RUNS EN DISCO, no contra `models.json`.
    #
    # La v1 llamaba a `bloqueados()`, que lee el JSON — y el JSON todavía es el de antes
    # del lote, porque regenerarlo es el paso siguiente. Resultado: dijo «los 3 SIGUEN
    # bloqueados» justo después de correr los 11 tests que los desbloqueaban. Un
    # verificador que mira la foto vieja acusa en falso, y eso gasta la confianza que el
    # verificador existe para dar.
    sigue = []
    for x in b:
        faltan = []
        for suite, inc in x["incompletas"].items():
            hechos = set()
            try:
                d = json.loads((RESULTS / f"benchmark_completar_{x['key']}.json").read_text())
                for r in (d if isinstance(d, list) else d.get("results", [])):
                    if r.get("suite") == suite and r.get("success") and r.get("test_name"):
                        hechos.add(r["test_name"])
            except Exception:
                pass
            if len(hechos) < inc["total"]:
                faltan.append(f"{suite} {len(hechos)}/{inc['total']}")
        if faltan:
            sigue.append(f"{x['name']}: {', '.join(faltan)}")
    if sigue:
        print(f"\n  ⚠️  {len(sigue)} modelo(s) siguen con el examen a medias EN DISCO:")
        for s in sigue:
            print(f"       {s}")
        print("     Los tests no corrieron o volvieron a fallar. Si la salida de arriba dice")
        print("     «SKIP (resume)», el consolidado está tapando el test que falta.")
        return 1
    print("\n  ✅ exámenes completados — corré `regenerate_all.py` para que entren al ranking.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
