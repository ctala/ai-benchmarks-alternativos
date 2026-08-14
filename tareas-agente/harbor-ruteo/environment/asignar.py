#!/usr/bin/env python3
"""Herramienta de asignación. Es la ÚNICA forma de registrar una decisión de ruteo.

POR QUÉ EXISTE ESTA HERRAMIENTA (14-ago-2026)
---------------------------------------------
La v1 de esta tarea pedía escribir `/app/ruteo.json` a mano. El sub-segmento mostró el
problema: los 4 modelos que entregaron sacaron **11 de 11 en las decisiones de ruteo**, y
los 2 que fallaron lo hicieron por **sintaxis JSON** y por un script Python con las
comillas mal cerradas. Toda la dificultad estaba en el formato.

El criterio `essential_difficulty` de la rúbrica de Terminal-Bench Science rechaza
exactamente eso: *la dificultad debe venir del razonamiento, no de minucias de formato.*

La solución la da τ-bench: el agente **llama herramientas** que mutan un estado, en vez
de redactar el artefacto. Acá esa herramienta es este CLI. Escribir mal el JSON deja de
ser posible; lo único que queda es **decidir bien**.

Uso:
    python /app/asignar.py --estado
    python /app/asignar.py J-01 modelo-B --motivo "trivial y de alto volumen"
    python /app/asignar.py J-05 --escalar --motivo "ningún modelo alcanza el umbral"
"""
import argparse
import json
import sys
from pathlib import Path

APP = Path(__file__).resolve().parent
SALIDA = APP / "ruteo.json"


def _cargar(nombre):
    return json.loads((APP / nombre).read_text(encoding="utf-8"))


def _estado():
    return json.loads(SALIDA.read_text(encoding="utf-8")) if SALIDA.exists() \
        else {"asignaciones": [], "costo_total_usd": 0.0}


def main() -> int:
    ap = argparse.ArgumentParser(description="Registra una asignación de trabajo a modelo.")
    ap.add_argument("trabajo", nargs="?", help="id del trabajo, p. ej. J-01")
    ap.add_argument("modelo", nargs="?", help="id del modelo del catálogo")
    ap.add_argument("--escalar", action="store_true",
                    help="marca el trabajo para revisión humana en vez de asignarlo")
    ap.add_argument("--motivo", default="", help="por qué se decidió así")
    ap.add_argument("--estado", action="store_true", help="muestra lo asignado hasta ahora")
    a = ap.parse_args()

    cat = {m["id"]: m for m in _cargar("catalogo.json")["modelos"]}
    tr = _cargar("trabajos.json")
    trabajos = {j["id"]: j for j in tr["trabajos"]}
    d = _estado()

    if a.estado or not a.trabajo:
        pend = [j for j in trabajos if j not in {x["trabajo"] for x in d["asignaciones"]}]
        print(json.dumps({**d, "sin_asignar": pend,
                          "presupuesto_mensual_usd": tr["presupuesto_mensual_usd"]},
                         indent=2, ensure_ascii=False))
        return 0

    # Validación de entrada: la herramienta se comporta como una API real y rechaza lo
    # que no existe. Un id inventado tiene que fallar acá, ruidoso, no colarse al
    # artefacto y aparecer después como una decisión.
    if a.trabajo not in trabajos:
        print(f"ERROR: el trabajo {a.trabajo!r} no existe. Son: {', '.join(trabajos)}",
              file=sys.stderr)
        return 2
    if not a.escalar:
        if not a.modelo:
            print("ERROR: falta el modelo, o usá --escalar", file=sys.stderr)
            return 2
        if a.modelo not in cat:
            print(f"ERROR: el modelo {a.modelo!r} no está en el catálogo. "
                  f"Son: {', '.join(cat)}", file=sys.stderr)
            return 2

    j = trabajos[a.trabajo]
    if a.escalar:
        fila = {"trabajo": a.trabajo, "modelo": "escalar_a_humano",
                "costo_mes_usd": 0.0, "motivo": a.motivo}
    else:
        # El costo lo calcula la herramienta: es aritmética, no criterio, y hacérsela
        # calcular al modelo mezclaba dos habilidades en un mismo número.
        costo = round(j["llamadas_mes"] / 1000 * cat[a.modelo]["costo_por_1k_llamadas_usd"], 2)
        fila = {"trabajo": a.trabajo, "modelo": a.modelo,
                "costo_mes_usd": costo, "motivo": a.motivo}

    d["asignaciones"] = [x for x in d["asignaciones"] if x["trabajo"] != a.trabajo] + [fila]
    d["asignaciones"].sort(key=lambda x: x["trabajo"])
    d["costo_total_usd"] = round(sum(x["costo_mes_usd"] for x in d["asignaciones"]), 2)
    SALIDA.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    resto = tr["presupuesto_mensual_usd"] - d["costo_total_usd"]
    print(f"{a.trabajo} → {fila['modelo']}  (${fila['costo_mes_usd']}/mes)")
    print(f"total ${d['costo_total_usd']} de ${tr['presupuesto_mensual_usd']} · "
          f"queda ${resto:.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
