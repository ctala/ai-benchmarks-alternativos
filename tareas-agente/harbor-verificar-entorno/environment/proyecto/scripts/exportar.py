#!/usr/bin/env python3
"""Reporte mensual de ventas por categoría desde datos/ventas.csv."""
import argparse, csv
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

p = argparse.ArgumentParser()
p.add_argument("--mes", required=True, help="AAAA-MM")
p.add_argument("--salida", required=True, help="ruta del CSV de salida")
a = p.parse_args()

tot, n = defaultdict(int), defaultdict(int)
for r in csv.DictReader(open(RAIZ / "datos" / "ventas.csv", encoding="utf-8")):
    if r["fecha"].startswith(a.mes):
        tot[r["categoria"]] += int(r["monto_clp"])
        n[r["categoria"]] += 1

salida = Path(a.salida)
salida.parent.mkdir(parents=True, exist_ok=True)
with open(salida, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["mes", "categoria", "ventas", "monto_clp"])
    for c in sorted(tot):
        w.writerow([a.mes, c, n[c], tot[c]])
print(f"{salida}: {len(tot)} categorías")
