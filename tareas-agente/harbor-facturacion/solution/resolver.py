#!/usr/bin/env python3
"""Solución de referencia: DERIVA el cierre de facturación desde los datos.

No es un JSON precomputado — si cambia una tarifa o una hora, se recalcula.
"""
import csv, json
from collections import defaultdict
from pathlib import Path

APP = Path("/app") if Path("/app/clientes.csv").exists() else Path(__file__).parent.parent / "environment"
cli = {r["id"]: r for r in csv.DictReader(open(APP / "clientes.csv", encoding="utf-8"))}

# Horas, DEDUPLICADAS: hay una línea repetida en el registro (CL-0142, 18-ago, 5h,
# "Documentación"). Facturarla es cobrarle de más al cliente.
vistas, horas, dudosas = set(), defaultdict(float), []
for r in csv.DictReader(open(APP / "horas_agosto.csv", encoding="utf-8")):
    clave = (r["fecha"], r["cliente_id"], r["horas"], r["detalle"])
    if clave in vistas:
        # Regla «Registros dudosos»: se puede facturar o no, pero siempre va a observaciones.
        dudosas.append({"cliente_id": r["cliente_id"],
                        "detalle": f"línea repetida el {r['fecha']} ({r['horas']} h, {r['detalle']}): "
                                   "no se facturó; confirmar si fueron dos sesiones."})
        continue
    vistas.add(clave)
    horas[r["cliente_id"]] += float(r["horas"])

facturas, notas = [], list(dudosas)
for cid, c in cli.items():
    # Contrato vencido → NO se factura. CL-0355 venció el 31-jul y no se renovó.
    if c["contrato_hasta"] < "2026-08-01":
        if horas.get(cid):
            notas.append({"cliente_id": cid,
                          "detalle": f"{horas[cid]:g} h registradas pero contrato vencido el "
                                     f"{c['contrato_hasta']}: no se factura, requiere renovación."})
        continue

    if c["modalidad"] == "fee_fijo":
        # El fee NO se multiplica por horas: se cobra igual haya 0 o 10 horas.
        facturas.append({"cliente_id": cid, "neto_usd": float(c["fee_mensual"])})
        continue

    h = horas.get(cid, 0)
    tope = float(c["tope_mensual_horas"]) if c["tope_mensual_horas"] else None
    if tope and h > tope:
        notas.append({"cliente_id": cid,
                      "detalle": f"{h:g} h registradas, tope contractual {tope:g} h sin autorización "
                                 f"escrita: se facturan {tope:g}; las {h - tope:g} restantes requieren "
                                 "autorización del cliente."})
        h = tope
    if h:
        facturas.append({"cliente_id": cid, "neto_usd": round(h * float(c["tarifa_hora"]), 2)})

salida = {"facturas": facturas,
          "total_neto_usd": round(sum(f["neto_usd"] for f in facturas), 2),
          "observaciones": notas}
destino = Path("/app/facturacion.json") if Path("/app").exists() else Path(__file__).parent / "facturacion.json"
destino.write_text(json.dumps(salida, ensure_ascii=False, indent=2))
print(json.dumps(salida, ensure_ascii=False, indent=2))
