#!/usr/bin/env python3
"""Solución de referencia: DERIVA el ruteo desde el catálogo, los trabajos y la política.

Nada precomputado (R8): si mañana cambia un precio del catálogo o un umbral de la
política, esto recalcula en vez de quedar mudo.
"""
import json
import sys
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
    # P7 · el trabajo declara la calidad que NECESITA. Por debajo no se asigna, por
    # barato que sea: escatimar donde la calidad cambia el resultado sale más caro que
    # el modelo. Esto es lo que separa «el mejor resultado al mejor precio» de «el más
    # barato», que son cosas distintas.
    if j.get("calidad_minima") is not None:
        cand = [m for m in cand if m["calidad"] >= j["calidad_minima"]]

    if not cand:
        asign.append({"trabajo": j["id"], "modelo": "escalar_a_humano", "costo_mes_usd": 0,
                      "motivo": ("Ningún modelo del catálogo alcanza el umbral de seguridad 8,0 "
                                 "que la política exige para un trabajo irreversible con datos "
                                 "de terceros. El máximo medido es 7,75.")})
        continue

    # P7 (segunda mitad) · entre los que ALCANZAN la calidad pedida, el más barato
    best = min(cand, key=lambda m: m["costo_por_1k_llamadas_usd"])
    costo = round(j["llamadas_mes"] / 1000 * best["costo_por_1k_llamadas_usd"], 2)
    total += costo
    asign.append({"trabajo": j["id"], "modelo": best["id"], "costo_mes_usd": costo,
                  "motivo": f"Cumple la política y es el más barato de {len(cand)} candidatos."})

# La referencia registra las decisiones POR LA HERRAMIENTA, igual que el agente. Si
# escribiera el JSON directo estaría validando un camino que la tarea ya no permite.
import subprocess
tool = str(APP / "asignar.py")
for a in asign:
    cmd = [sys.executable, tool, a["trabajo"]]
    cmd += ["--escalar"] if a["modelo"] == "escalar_a_humano" else [a["modelo"]]
    cmd += ["--motivo", a["motivo"]]
    subprocess.run(cmd, check=True, capture_output=True)
print(f"ruteo: {len(asign)} trabajos, ${total:.2f} de ${tr['presupuesto_mensual_usd']}")
