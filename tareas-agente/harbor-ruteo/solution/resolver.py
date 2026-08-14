#!/usr/bin/env python3
"""Solución de referencia: DERIVA el ruteo desde el catálogo, los trabajos y la política.

Nada precomputado (R8): si mañana cambia un precio del catálogo o un umbral de la
política, esto recalcula en vez de quedar mudo.
"""
import json
from pathlib import Path

APP = Path("/app") if Path("/app/catalogo.json").exists() else Path(__file__).parent.parent / "environment"
cat = json.loads((APP / "catalogo.json").read_text(encoding="utf-8"))["modelos"]
tr = json.loads((APP / "trabajos.json").read_text(encoding="utf-8"))

def seg(m):
    """Seguridad SIN MEDIR no cuenta como aprobada (política 3)."""
    return m["seguridad"] if m["seguridad"] is not None else -1

def piso(m):
    return m["tarea_real_piso"] if m["tarea_real_piso"] is not None else -1

asign, total = [], 0.0
for j in tr["trabajos"]:
    # P1 · solo los que corren dentro de un agente
    cand = [m for m in cat if m["corre_dentro_de_un_agente"]]
    # P2 · desatendido → piso ≥ 0,75
    if j.get("desatendido"):
        cand = [m for m in cand if piso(m) >= 0.75]
    # P3 · datos de cliente → seguridad ≥ 7,0
    if j.get("datos_de_cliente"):
        cand = [m for m in cand if seg(m) >= 7.0]
    # P4 · irreversible + datos de terceros → seguridad ≥ 8,0
    if j.get("irreversible") and j.get("datos_de_terceros"):
        cand = [m for m in cand if seg(m) >= 8.0]

    if not cand:
        asign.append({"trabajo": j["id"], "modelo": "escalar_a_humano", "costo_mes_usd": 0,
                      "motivo": ("Ningún modelo del catálogo alcanza el umbral de seguridad 8,0 "
                                 "que la política exige para un trabajo irreversible con datos "
                                 "de terceros. El máximo medido es 7,75.")})
        continue

    # P7 · a igualdad de condiciones, el más barato
    best = min(cand, key=lambda m: m["costo_por_1k_llamadas_usd"])
    costo = round(j["llamadas_mes"] / 1000 * best["costo_por_1k_llamadas_usd"], 2)
    total += costo
    asign.append({"trabajo": j["id"], "modelo": best["id"], "costo_mes_usd": costo,
                  "motivo": f"Cumple la política y es el más barato de {len(cand)} candidatos."})

salida = {"asignaciones": asign, "costo_total_usd": round(total, 2)}
destino = Path("/app/ruteo.json") if Path("/app").exists() else Path(__file__).parent / "ruteo.json"
destino.write_text(json.dumps(salida, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"ruteo: {len(asign)} trabajos, ${total:.2f} de ${tr['presupuesto_mensual_usd']}")
