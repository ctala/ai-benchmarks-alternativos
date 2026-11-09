#!/usr/bin/env python3
"""Solución de referencia: DERIVA la conciliación aplicando `politica-conciliacion.md`.

No trae la respuesta: si cambia un movimiento, una factura o un tipo de cambio, se recalcula.
"""
import csv, json, re
from pathlib import Path

APP = Path("/app") if Path("/app/cartola.csv").exists() else Path(__file__).parent.parent / "environment"
leer = lambda n: list(csv.DictReader(open(APP / n, encoding="utf-8")))

facturas = {f["folio"]: f for f in leer("facturas.csv")}
clientes = leer("clientes.csv")
tc = {r["fecha"]: float(r["dolar_observado"]) for r in leer("tipo_cambio.csv")}

# Grupo relacionado (regla 1b): matriz y filiales comparten un grupo.
raiz = {c["rut"]: (c["rut_matriz"] or c["rut"]) for c in clientes}
grupo = lambda rut: raiz.get(rut, rut)


def dolar(fecha):
    # Regla 3: el del día del abono; si no hay, el último día ANTERIOR con valor.
    previas = [f for f in tc if f <= fecha]
    return tc[max(previas)]


abonado = {k: 0.0 for k in facturas}
recibio = set()
no_conc = []
for m in leer("cartola.csv"):
    monto = float(m["monto_clp"])
    if monto < 0:  # Regla 4
        no_conc.append({"id_mov": m["id_mov"], "motivo": "cargo bancario, no es pago de cliente"})
        continue
    citados = [f for f in re.findall(r"F-\d{4}", m["descripcion"]) if f in facturas]
    validos = [f for f in citados
               if m["rut_contraparte"] and grupo(m["rut_contraparte"]) == grupo(facturas[f]["rut_cliente"])]
    if not validos:  # Regla 1: folio citado Y RUT del cliente o de su grupo
        motivo = ("no cita folio" if not citados else
                  "el RUT que paga no es del cliente ni de su grupo")
        no_conc.append({"id_mov": m["id_mov"], "motivo": motivo})
        continue
    restante_clp = monto
    orden = sorted(validos, key=lambda x: facturas[x]["fecha_emision"])  # Regla 2
    for i, f in enumerate(orden):
        fa = facturas[f]
        tasa = dolar(m["fecha"]) if fa["moneda"] == "USD" else 1.0
        disponible = restante_clp / tasa
        saldo = float(fa["monto"]) - abonado[f]
        # Se salda cada factura antes de pasar a la siguiente; la última recibe lo que quede.
        aplica = disponible if i == len(orden) - 1 else min(disponible, saldo)
        abonado[f] += aplica
        recibio.add(f)
        restante_clp -= aplica * tasa
        if restante_clp <= 0.5:
            break

salida = {"facturas": [], "no_conciliados": no_conc}
for folio, fa in facturas.items():
    saldo = round(float(fa["monto"]) - abonado[folio], 2)
    if -1 <= saldo <= 1 and folio in recibio:
        saldo = 0.0
    estado = "pendiente" if folio not in recibio else ("pagada" if saldo == 0 else "parcial")
    salida["facturas"].append({"folio": folio, "estado": estado, "saldo": saldo, "moneda": fa["moneda"]})

destino = Path("/app/conciliacion.json") if Path("/app").exists() else Path(__file__).parent / "conciliacion.json"
destino.write_text(json.dumps(salida, ensure_ascii=False, indent=2))
print(json.dumps(salida, ensure_ascii=False, indent=2))
