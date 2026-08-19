#!/usr/bin/env python3
"""¿Alcanza el presupuesto para el lote que estás por lanzar?

POR QUÉ EXISTE (18-ago-2026)
----------------------------
La noche del 17 se lanzaron once mediciones en paralelo y **a las 20:57 se agotó el
límite de la API key de OpenRouter**. No falló un modelo: falló el juez, que es lo que
puntúa TODO. El efecto en cadena, en tres minutos:

    Claude Opus 5      murió con «el verificador semántico no respondió» (52 de 143 tests)
    n3 y n4            ni arrancaron: el runner se negó a medir sin juez (bien)
    n1 y n2            siguieron una hora entregando HTTP 403 como runs fallidos

Lo caro no fue la plata: fue que el lote **murió a mitad** en vez de no arrancar. Cuatro
exámenes quedaron incompletos y hay que re-correrlos.

Y la condición era perfectamente conocible de antemano: una llamada a `/api/v1/key`
devuelve cuánto queda. El canario ya verificaba que los modelos respondan; nadie
verificaba que hubiera con qué pagarles. Es el patrón de siempre acá — una condición
conocida sin instrumento que la vigile.

EL DETALLE QUE COSTÓ UNA HORA MÁS
---------------------------------
Al recargar la cuenta el 403 siguió, porque **el tope era de la KEY y no del saldo**:
`limit: 250` con `limit_reset: "monthly"`. Recargar créditos no toca ese número. Por eso
este chequeo reporta las dos cosas por separado y dice cuál es la que bloquea.

Uso:
    python benchmarks/check_presupuesto.py                 # cuánto queda
    python benchmarks/check_presupuesto.py --necesito 30   # exit 1 si no alcanza
"""

import argparse
import json
import os
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
try:
    from dotenv import load_dotenv
    load_dotenv(ROOT / ".env")
except Exception:
    pass


def estado() -> dict | None:
    k = os.getenv("OPENROUTER_API_KEY")
    if not k:
        return None
    req = urllib.request.Request("https://openrouter.ai/api/v1/key",
                                 headers={"Authorization": f"Bearer {k}"})
    try:
        return json.load(urllib.request.urlopen(req, timeout=25))["data"]
    except Exception as e:
        return {"_error": str(e)[:160]}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--necesito", type=float, default=None,
                    help="USD que va a costar el lote; exit 1 si no alcanza")
    a = ap.parse_args()

    d = estado()
    if d is None:
        print("  ⚠️  sin OPENROUTER_API_KEY: no se puede verificar presupuesto.")
        return 0
    if "_error" in d:
        print(f"  ⚠️  no se pudo consultar el saldo: {d['_error']}")
        return 0

    limite = d.get("limit")
    resta = d.get("limit_remaining")
    print("PRESUPUESTO — OpenRouter\n")
    print(f"  gastado hoy      ${d.get('usage_daily', 0):>8.2f}")
    print(f"  gastado semana   ${d.get('usage_weekly', 0):>8.2f}")
    print(f"  gastado mes      ${d.get('usage_monthly', 0):>8.2f}")
    if limite is None:
        print("\n  límite de la key: sin tope declarado (manda el saldo de la cuenta).")
        return 0
    print(f"\n  tope de ESTA key ${limite:>8.2f}  (reset {d.get('limit_reset') or '—'})")
    print(f"  disponible       ${(resta or 0):>8.2f}")

    if resta is not None and resta <= 0:
        print("\n  🔴 la KEY llegó a su tope. Ojo: recargar la CUENTA no lo cambia —")
        print("     el límite es de la key. Subilo o quitalo en")
        print("     openrouter.ai/settings/keys, o usá una key sin tope.")
        return 1
    if a.necesito is not None and resta is not None and resta < a.necesito:
        print(f"\n  🔴 el lote necesita ~${a.necesito:.2f} y quedan ${resta:.2f}.")
        print("     Un lote que muere a mitad deja exámenes incompletos que hay que")
        print("     re-correr: es más caro que no lanzarlo.")
        return 1
    if a.necesito is not None:
        print(f"\n  ✅ el lote (~${a.necesito:.2f}) entra en lo disponible.")
    else:
        print("\n  ✅ hay presupuesto.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
