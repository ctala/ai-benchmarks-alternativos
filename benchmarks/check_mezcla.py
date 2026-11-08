#!/usr/bin/env python3
"""¿Algún rankeado rindió su examen en más de un proveedor o cuantización?

POR QUÉ EXISTE (corte-v5 6.5 · DECISIONES, 4-nov-2026: «mismo modelo, mismas condiciones»)
----------------------------------------------------------------------------------------
OpenRouter rutea cada request al proveedor que esté disponible. Sin proveedor fijo, el
examen de un modelo abierto queda repartido: el 4-nov, 40 de los 47 abiertos rankeados
tenían runs de más de un proveedor, con cuantizaciones de `int4` a `bf16`. Su nota es la
de una mezcla, y nada lo decía. Este chequeo lo dice.

QUÉ VERIFICA
------------
M1. Por rankeado, el último run de cada test del índice: más de un `upstream_provider`
    o más de una cuantización conocida es ROJO.
M2. Runs sin proveedor registrado: en un ABIERTO es rojo (criterio estricto: la
    cuantización cambia por proveedor); en un CERRADO se publica como «proveedor no
    registrado» y no es rojo (fecha de corte: el campo existe desde el 14-ago).
M3. Harbor: un abierto cuyas tareas agénticas las sirvió más de un proveedor es rojo.

Nace INFORMATIVO (sale con 0 aunque haya rojos): el 4-nov daba rojo en la mayoría de los
rankeados, y un bloqueante que nace en rojo se aprende a ignorar. Pasa a bloqueante en
5.2.a, después de la ventana de medición. `qa.py` lo corre como informativo.

Uso:  python benchmarks/check_mezcla.py [--detalle]
"""
import argparse
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "benchmarks"))

DESCONOCIDAS = {None, "", "unknown", "?"}


def normalizar_proveedor(p: str | None) -> str | None:
    """El mismo proveedor escrito de dos formas es UN proveedor.

    6-nov-2026: GPT-5.5 salía mezclado con «openai ×57, OpenAI ×20». Es OpenAI en los
    dos casos: la API directa registra el slug en minúscula y OpenRouter el nombre
    visible. Se compara sin mayúsculas ni espacios en los bordes; los nombres de verdad
    distintos («Google» y «Google AI Studio») siguen siendo distintos.
    """
    if not p or not str(p).strip():
        return None
    return str(p).strip().casefold()


def veredicto(runs: list[dict], abierto: bool, cuant_de=lambda r: r.get("cuantizacion"),
              harbor: list[str] | None = None) -> tuple[str, list[str]]:
    """('limpio' | 'mezclado' | 'no_registrado', motivos). Función pura.

    `runs` son los últimos runs del índice de UN modelo. `cuant_de` resuelve la
    cuantización de un run (la del run si la trae; si no, la del censo).
    """
    motivos = []
    provs = Counter(normalizar_proveedor(r.get("upstream_provider")) for r in runs)
    sin = provs.pop(None, 0)
    if len(provs) > 1:
        motivos.append("proveedores: " + ", ".join(f"{p} ×{n}" for p, n in provs.most_common()))
    quants = {q for q in (cuant_de(r) for r in runs) if q not in DESCONOCIDAS}
    if len(quants) > 1:
        motivos.append("cuantizaciones: " + ", ".join(sorted(quants)))
    if sin and abierto:
        motivos.append(f"{sin} run(s) sin proveedor registrado (abierto: criterio estricto)")
    if harbor and len(set(harbor)) > 1 and abierto:
        motivos.append("Harbor: " + ", ".join(sorted(set(harbor))))
    if motivos:
        return "mezclado", motivos
    if sin:
        return "no_registrado", [f"{sin} run(s) sin proveedor registrado (cerrado)"]
    return "limpio", []


def _ultimos(runs: list[dict], idx: set[str]) -> list[dict]:
    u = {}
    for r in runs:
        if r.get("suite") not in idx:
            continue
        k = (r.get("suite"), r.get("test_name"))
        if k not in u or str(r.get("timestamp")) > str(u[k].get("timestamp")):
            u[k] = r
    return list(u.values())


def _harbor_por_id() -> dict[str, list[str]]:
    p = ROOT / "tareas-agente" / "resultados.json"
    if not p.exists():
        return {}
    out: dict[str, list[str]] = {}
    for t in json.loads(p.read_text()).get("tareas", {}).values():
        for mid, fila in t.get("modelos", {}).items():
            out.setdefault(mid, []).extend(fila.get("proveedores") or [])
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--detalle", action="store_true")
    a = ap.parse_args()

    from benchmarks import suites, proveedor_fijo
    from benchmarks.models import MODELS, OLLAMA_MODELS
    from benchmarks.export_for_pages import load_all_results
    cat = {**OLLAMA_MODELS, **MODELS}
    d = json.loads((ROOT / "docs" / "data" / "models.json").read_text())
    rank = [m for m in d["models"] if m.get("ranked")]
    if not rank:
        print("❌ M0 models.json no trae rankeados: el detector está ciego")
        return 1
    _, por_id_nombre = load_all_results()
    harbor = _harbor_por_id()
    idx = suites.del_examen()  # todo lo que se rinde (7-nov-2026)

    leidos, estados = 0, {}
    for m in rank:
        c = cat[m["key"]]
        runs = _ultimos(por_id_nombre.get((c["id"], c["name"]), []), idx)
        leidos += len(runs)
        cuant = lambda r, mid=c["id"]: (r.get("cuantizacion")
                                        or proveedor_fijo.cuantizacion_de(mid, r.get("upstream_provider")))
        estados[m["key"]] = veredicto(runs, bool(m.get("open_source")), cuant,
                                      harbor.get(c["id"]))
    if leidos == 0:
        print("❌ M0 no se leyó ningún run: el detector está ciego")
        return 1

    n = Counter(e for e, _ in estados.values())
    print(f"RUNS MEZCLADOS · {len(rank)} rankeados, {leidos} runs del índice leídos\n")
    print(f"  limpios: {n['limpio']} · proveedor no registrado (cerrados): "
          f"{n['no_registrado']} · mezclados: {n['mezclado']}")
    if a.detalle:
        for k, (e, mot) in sorted(estados.items()):
            if e != "limpio":
                print(f"   {'❌' if e == 'mezclado' else 'ℹ️ '} {k}: {'; '.join(mot)}")
    if n["mezclado"]:
        print(f"\n  ⚠️  {n['mezclado']} rankeado(s) con examen mezclado. INFORMATIVO hasta "
              f"5.2.a (corte-v5): la ventana de v5 los re-mide en proveedor fijo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
