#!/usr/bin/env python3
"""Solución de referencia: DERIVA la cotización desde el tarifario y las reglas.

Antes era un JSON precomputado. `harbor check` lo marcó con razón: un artefacto final
no demuestra cómo se llegó al número, y si mañana cambia un precio del tarifario, la
solución queda muda en vez de recalcularse.
"""
import csv, json
from pathlib import Path

APP = Path("/app") if Path("/app/tarifario.csv").exists() else Path(__file__).parent.parent / "environment"
FACTOR_URGENCIA = 1.25          # "para fin de mes" · dentro de la banda 0,85-2,00

tarifa = {r["id"]: r for r in csv.DictReader(open(APP / "tarifario.csv", encoding="utf-8"))}

# Derivación, regla por regla:
#  · el cliente YA tiene diagnóstico          → DIAG fuera
#  · "implementación completa"                → IMPL-AVZ, que ABSORBE a IMPL-BAS
#  · "háganla ustedes desde cero"             → MIGRA (no MIGRA-REV: no es revisión)
#  · "conectar con nuestro ERP"               → INTEG
#  · certificación ISO 27001                  → NO está en el tarifario → fuera
pedidos = ["IMPL-AVZ", "MIGRA", "INTEG"]
absorbidos = {t["absorbe"] for t in tarifa.values() if t.get("absorbe")}

lineas = []
for sku in pedidos:
    if sku in absorbidos:
        continue
    ref = float(tarifa[sku]["precio_usd"])
    lineas.append({"sku": sku, "precio_referencia": ref,
                   "factor": FACTOR_URGENCIA, "total": round(ref * FACTOR_URGENCIA, 2)})

salida = {"lineas": lineas,
          "total_usd": round(sum(l["total"] for l in lineas), 2),
          "notas": [
              f"IMPL-BAS absorbida por IMPL-AVZ ({tarifa['IMPL-AVZ']['nota']}).",
              "DIAG no se cotiza: el cliente ya tiene diagnóstico de otra consultora.",
              "Certificación ISO 27001: no figura en el tarifario, requiere cotización humana.",
              f"Factor {FACTOR_URGENCIA} por urgencia de fin de mes, dentro de la banda 0,85-2,00.",
          ]}
destino = Path("/app/cotizacion.json") if Path("/app").exists() else Path(__file__).parent / "cotizacion.json"
destino.write_text(json.dumps(salida, ensure_ascii=False, indent=2))
print(json.dumps(salida, ensure_ascii=False, indent=2))
