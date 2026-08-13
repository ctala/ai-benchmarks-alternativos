#!/usr/bin/env python3
"""Motor de referencia: calcula la cotización CORRECTA. Es la verdad de terreno.

No lo ve el agente — solo el verificador. El agente recibe `tarifario.csv`, `reglas.md`
y el encargo en prosa, y tiene que llegar al mismo número leyendo las reglas.
"""
import csv, json, sys
from pathlib import Path

BANDA_MIN, BANDA_MAX = 0.85, 2.00

def cargar(ruta="entorno/tarifario.csv"):
    with open(ruta, encoding="utf-8") as f:
        return {r["id"]: r for r in csv.DictReader(f)}

def cotizar(ids, catalogo, ajustes=None):
    """ids: servicios pedidos. ajustes: {id: factor} dentro de la banda."""
    ajustes = ajustes or {}
    absorbidos = {c["absorbe"] for c in catalogo.values() if c.get("absorbe")}
    lineas, notas = [], []
    for sid in ids:
        if sid in absorbidos and any(c.get("absorbe") == sid for c in
                                     (catalogo[i] for i in ids if i in catalogo)):
            notas.append(f"{sid}: absorbido, no se cobra aparte")
            continue
        s = catalogo.get(sid)
        if not s:
            notas.append(f"{sid}: no está en el tarifario → cotización humana")
            continue
        ref = float(s["precio_usd"])          # precio de REFERENCIA (regla 2)
        f = float(ajustes.get(sid, 1.0))
        if not (BANDA_MIN <= f <= BANDA_MAX):
            raise ValueError(f"ajuste {f} fuera de banda para {sid}")
        lineas.append({"id": sid, "servicio": s["servicio"],
                       "referencia": ref, "factor": f, "total": round(ref * f, 2)})
    return {"lineas": lineas, "total_usd": round(sum(l["total"] for l in lineas), 2),
            "notas": notas}

if __name__ == "__main__":
    cat = cargar()
    ids = sys.argv[1:] or ["IMPL-AVZ", "IMPL-BAS", "MIGRA-REV", "MIGRA", "INTEG"]
    print(json.dumps(cotizar(ids, cat), ensure_ascii=False, indent=2))
