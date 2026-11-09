#!/usr/bin/env python3
"""Sincroniza con el ERP las ventas del último mes cerrado."""
import argparse, datetime as dt, os

import requests
from dateutil.relativedelta import relativedelta

p = argparse.ArgumentParser()
p.add_argument("--simular", action="store_true", help="no llama al ERP; muestra qué haría")
a = p.parse_args()

hoy = dt.date(2026, 11, 9)
desde = (hoy - relativedelta(months=1)).replace(day=1)
hasta = hoy.replace(day=1) - dt.timedelta(days=1)
url = os.environ.get("ERP_URL", "https://erp.elroble.example/api") + "/ventas"

if a.simular:
    print(f"[simulación] GET {url}?desde={desde}&hasta={hasta}")
else:
    requests.get(url, params={"desde": str(desde), "hasta": str(hasta)}, timeout=30).raise_for_status()
