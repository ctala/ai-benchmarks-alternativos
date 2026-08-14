#!/usr/bin/env python3
"""Genera el catálogo ANONIMIZADO del entorno desde nuestras mediciones reales.

POR QUÉ ANÓNIMO. Cristian propuso construir esta tarea con los resultados de las
anteriores. Es la idea correcta —los números son medidos y verificables en vez de
inventados— pero con los nombres reales un modelo puede rutear **por reputación**:
«Claude es bueno, le mando esto» acierta sin haber leído la tabla. Eso mediría memoria,
no criterio. Con `Modelo A/B/C…` la única forma de acertar es usar los datos.

POR QUÉ SE CONGELA. El catálogo se genera UNA vez y el snapshot se commitea. Si se
regenerara con cada medición, la tarea cambiaría sola: el `task_checksum` se movería y
todas las corridas previas dejarían de ser comparables (R17). Regenerar es un acto
deliberado que crea una versión nueva de la tarea, no un efecto secundario.

Uso:  python solution/generar_catalogo.py   # escribe environment/catalogo.json
"""
import json
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
SALIDA = Path(__file__).resolve().parent.parent / "environment" / "catalogo.json"

models = json.loads((RAIZ / "docs/data/models.json").read_text())
agentico = json.loads((RAIZ / "tareas-agente/resultados.json").read_text())["tareas"]
cotizar = agentico.get("harbor-cotizar", {}).get("modelos", {})

# Se eligen 8 modelos que cubran el espacio de decisión: barato-flojo, barato-bueno,
# caro-bueno, rápido, lento, inseguro, sin herramientas. Sin variedad no hay decisión
# que tomar y la tarea se vuelve trivial.
cands = [m for m in models["models"]
         if m.get("ranked") and m.get("cost_per_1k_calls_usd") is not None
         and m.get("latency_avg_s") is not None and m.get("score_calidad") is not None]

def pick(f, usados):
    xs = [m for m in cands if m["id"] not in usados]
    return max(xs, key=f) if xs else None

usados, elegidos = set(), []

# Se FUERZA la inclusión de uno que medimos que NO puede correr dentro de un agente.
# Sin él, los 8 declararían soportar herramientas y la decisión "esto no lo puede hacer
# ninguno de los que sirven" no existiría. `tool_calling` es capacidad DECLARADA —la
# declaran todos los rankeados—; `sirve_para_agentes` es lo que se midió ejecutando.
no_apto = next((m for m in models["models"]
                if m.get("sirve_para_agentes") is False and m.get("ranked")
                and m.get("cost_per_1k_calls_usd") is not None
                and m.get("latency_avg_s") is not None), None)
if no_apto:
    usados.add(no_apto["id"]); elegidos.append(no_apto)
criterios = [
    ("el más barato", lambda m: -m["cost_per_1k_calls_usd"]),
    ("el de mejor calidad", lambda m: m["score_calidad"]),
    ("el más rápido", lambda m: -m["latency_avg_s"]),
    ("el más inseguro con datos", lambda m: -(m.get("security_score") or 99)),
    ("el mejor en la tarea real", lambda m: (cotizar.get(m["id"], {}).get("media") or 0)),
    ("el más lento", lambda m: m["latency_avg_s"]),
    ("el peor en la tarea real", lambda m: -(cotizar.get(m["id"], {}).get("media") or 99)),
    ("calidad alta y barato", lambda m: m["score_calidad"] - m["cost_per_1k_calls_usd"]),
]
for _, f in criterios:
    m = pick(f, usados)
    if m:
        usados.add(m["id"]); elegidos.append(m)

filas = []
for i, m in enumerate(elegidos):
    c = cotizar.get(m["id"], {})
    filas.append({
        "id": f"modelo-{chr(65 + i)}",
        "calidad": m["score_calidad"],
        "costo_por_1k_llamadas_usd": m["cost_per_1k_calls_usd"],
        "latencia_seg": round(m["latency_avg_s"], 1),
        "seguridad": m.get("security_score"),
        # Lo MEDIDO, no lo declarado: `tool_calling` lo declaran los 79 rankeados y por
        # eso no distingue a nadie. `sirve_para_agentes` sale de haberlo visto ejecutar.
        "corre_dentro_de_un_agente": m.get("sirve_para_agentes"),
        "tarea_real_reward": c.get("media"),
        "tarea_real_piso": c.get("piso"),
    })

SALIDA.write_text(json.dumps({
    "_nota": ("Catálogo anonimizado. Las cifras son mediciones reales del benchmark "
              "ai-benchmarks-alternativos; los nombres se ocultan a propósito para que "
              "la decisión salga de los datos y no de la reputación del proveedor."),
    "generado": date.today().isoformat(),
    "escala": {"calidad": "0-10", "seguridad": "0-10, más alto = resiste mejor fuga de datos",
               "tarea_real_reward": "0-1, fracción de una tarea de negocio completada dentro de un agente"},
    "modelos": filas,
}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"catálogo: {len(filas)} modelos anonimizados")
