#!/usr/bin/env python3
"""Lanza un lote de Harbor con el estándar del examen y repite los intentos que cortó el proveedor.

POR QUÉ (DECISIONES, 9-nov-2026, ventana v6.1, Cristian)
--------------------------------------------------------
Un intento que el PROVEEDOR corta (429 o 5xx que sobrevive a los reintentos de litellm) no
es una nota del modelo. `export_harbor.error_del_proveedor` lo descarta entero, sin nota
parcial, leyendo solo la salida de la llamada al modelo (nunca los logs del entorno: el 429
de Postmark de `harbor-incidente` es un señuelo). Este lanzador cierra el otro lado: repite
esos intentos hasta `--tope` rondas. Si tras el tope sigue sin k intentos válidos, la tarea
queda con los que haya, y sin ninguno queda `sin_dato_proveedor`: nunca 0.

El reporte del lote (`jobs/<prefijo>__reintentos.json` y la salida) dice cuántos intentos
se repitieron y en qué modelos.

No llama a ningún modelo: invoca `harbor run`, el camino sancionado para las tareas
agénticas (CLAUDE.md, regla 6). El estándar es el de siempre: mini-swe-agent 2.4.6,
proveedor fijo (`jobs/_proveedor_fijo/`, de `proveedor_fijo.py --harbor`) y k = 3.

Uso:
    python benchmarks/lote_harbor.py --prefijo v61 --modelos z-ai/glm-5.3 openai/gpt-oss-20b \\
        --tareas harbor-conciliar harbor-incidente [--k 3] [--tope 2] [--paralelo 4]
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from benchmarks import export_harbor as eh  # noqa: E402

HARBOR = str(Path.home() / ".local" / "bin" / "harbor")
VERSION_AGENTE = "2.4.6"
TOPE_REINTENTOS = 2


def _clave() -> str:
    for ln in (ROOT / ".env").read_text(encoding="utf-8").splitlines():
        if ln.startswith("OPENROUTER_API_KEY="):
            return ln.split("=", 1)[1].strip().strip('"')
    raise SystemExit("falta OPENROUTER_API_KEY en .env")


def contar(job_dir: Path) -> tuple[int, int]:
    """(intentos válidos, intentos cortados por el proveedor) de un job de Harbor.

    Válido = terminó con reward y no lo cortó el proveedor. Un intento sin reward por otra
    causa (timeout del harness) no es válido ni se cuenta como corte: no se repite acá."""
    validos = cortados = 0
    for trial in job_dir.glob("*__*"):
        tray = trial / "agent" / "mini-swe-agent.trajectory.json"
        texto = tray.read_text(errors="replace") if tray.exists() else ""
        if eh.error_del_proveedor(texto):
            cortados += 1
        elif (trial / "verifier" / "reward.txt").exists():
            validos += 1
    return validos, cortados


def _correr(modelo: str, tarea: str, k: int, job: str, clave: str, jobs: Path) -> None:
    yaml = ROOT / "jobs" / "_proveedor_fijo" / (modelo.replace("/", "__") + ".yaml")
    if not yaml.exists():
        raise SystemExit(f"falta {yaml.relative_to(ROOT)}: `proveedor_fijo.py {modelo} --harbor`")
    subprocess.run([HARBOR, "run", "-p", str(ROOT / "tareas-agente" / tarea), "-a", "mini-swe-agent",
                    "-m", f"openrouter/{modelo}", "--ak", f"version={VERSION_AGENTE}",
                    "--ak", f"config_file={yaml}", "-k", str(k), "-n", str(k),
                    "--agent-env", f"OPENROUTER_API_KEY={clave}", "-o", str(jobs),
                    "--job-name", job, "-q"],
                   cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def par(modelo: str, tarea: str, prefijo: str, k: int, tope: int, clave: str, jobs: Path,
        correr=_correr) -> dict:
    """Corre k intentos de (modelo, tarea) y repite los cortados por el proveedor hasta `tope`."""
    base = f"{prefijo}__{modelo.split('/')[-1]}__{tarea}"
    if not (jobs / base / "result.json").exists():
        correr(modelo, tarea, k, base, clave, jobs)
    validos, cortados = contar(jobs / base)
    repetidos, ronda, ultimos = 0, 0, cortados
    # Solo se repite lo que cortó el proveedor en la ronda anterior: un faltante por otra
    # causa (timeout del harness) no se repite acá.
    while validos < k and ultimos and ronda < tope:
        ronda += 1
        falta = min(k - validos, ultimos)
        job = f"{base}__r{ronda}"
        if not (jobs / job / "result.json").exists():
            correr(modelo, tarea, falta, job, clave, jobs)
        repetidos += falta
        v, ultimos = contar(jobs / job)
        validos += v
        cortados += ultimos
    return {"modelo": modelo, "tarea": tarea, "validos": validos, "cortados": cortados,
            "repetidos": repetidos, "rondas": ronda,
            "estado": "sin_dato_proveedor" if validos == 0 and cortados else
                      "completo" if validos >= k else "incompleto"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prefijo", required=True)
    ap.add_argument("--modelos", nargs="+", required=True, help="ids de OpenRouter")
    ap.add_argument("--tareas", nargs="+", required=True)
    ap.add_argument("--k", type=int, default=3)
    ap.add_argument("--tope", type=int, default=TOPE_REINTENTOS)
    ap.add_argument("--paralelo", type=int, default=4)
    ap.add_argument("--jobs", default=str(ROOT / "jobs"))
    a = ap.parse_args()
    jobs = Path(a.jobs)
    clave = _clave()
    pares = [(m, t) for m in a.modelos for t in a.tareas]
    with ThreadPoolExecutor(max_workers=a.paralelo) as ex:
        filas = list(ex.map(lambda p: par(p[0], p[1], a.prefijo, a.k, a.tope, clave, jobs), pares))
    for f in filas:
        print(f"  {f['modelo']:<40} {f['tarea']:<26} válidos {f['validos']}/{a.k}"
              + (f" · cortados {f['cortados']}, repetidos {f['repetidos']}" if f["cortados"] else "")
              + ("" if f["estado"] == "completo" else f"  ⚠️ {f['estado']}"))
    rep = [f for f in filas if f["repetidos"]]
    por_modelo: dict[str, int] = {}
    for f in rep:
        por_modelo[f["modelo"]] = por_modelo.get(f["modelo"], 0) + f["repetidos"]
    print(f"\n  REINTENTOS POR CORTE DEL PROVEEDOR: {sum(por_modelo.values())} intentos en "
          f"{len(por_modelo)} modelos" + "".join(f"\n    {m}: {n}" for m, n in sorted(por_modelo.items())))
    sin = [f for f in filas if f["estado"] == "sin_dato_proveedor"]
    if sin:
        print(f"  SIN DATO tras el tope ({a.tope}): " + ", ".join(f"{f['modelo']}·{f['tarea']}" for f in sin))
    (jobs / f"{a.prefijo}__reintentos.json").write_text(json.dumps(
        {"k": a.k, "tope": a.tope, "repetidos_por_modelo": por_modelo, "pares": filas},
        indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
