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

Y EL INVERSO, QUE DIO VERDE EN FALSO (14-sep-2026)
--------------------------------------------------
Después de aquello el chequeo quedó mirando SÓLO la key. El 14-sep decía «✅ hay
presupuesto» con **$720 libres en la key y $16,81 de saldo en la cuenta** (1.950
cargados, 1.933 usados): el primer lote de más de $17 habría muerto a mitad igual que el
17-ago, con este chequeo en verde. Son dos topes y manda el MENOR, así que ahora se
consultan los dos (`/api/v1/key` y `/api/v1/credits`) y se dice cuál bloquea.

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


def _consultar(ruta: str, k: str) -> dict:
    req = urllib.request.Request(f"https://openrouter.ai/api/v1/{ruta}",
                                 headers={"Authorization": f"Bearer {k}"})
    try:
        return json.load(urllib.request.urlopen(req, timeout=25))["data"]
    except Exception as e:
        return {"_error": str(e)[:160]}


def estado() -> tuple[dict, dict] | None:
    """(datos de la key, saldo de la cuenta), o None si no hay key."""
    k = os.getenv("OPENROUTER_API_KEY")
    if not k:
        return None
    return _consultar("key", k), _consultar("credits", k)


def disponible(key: dict, cuenta: dict) -> tuple[float | None, str | None]:
    """(USD que de verdad se pueden gastar, qué los limita: "key" o "cuenta").

    Pura, para poder probarla sin red. La key puede tener tope propio y la cuenta tiene
    su saldo: se gasta hasta el MENOR de los dos. Mirar uno solo ya falló dos veces, una
    en cada dirección.
    """
    topes = []
    if key.get("limit") is not None and key.get("limit_remaining") is not None:
        topes.append((float(key["limit_remaining"]), "key"))
    if cuenta.get("total_credits") is not None:
        saldo = float(cuenta["total_credits"]) - float(cuenta.get("total_usage") or 0)
        topes.append((saldo, "cuenta"))
    return min(topes) if topes else (None, None)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--necesito", type=float, default=None,
                    help="USD que va a costar el lote; exit 1 si no alcanza")
    a = ap.parse_args()

    e = estado()
    if e is None:
        print("  ⚠️  sin OPENROUTER_API_KEY: no se puede verificar presupuesto.")
        return 0
    key, cuenta = e
    if "_error" in key:
        print(f"  ⚠️  no se pudo consultar la key: {key['_error']}")
        return 0

    print("PRESUPUESTO — OpenRouter\n")
    print(f"  gastado hoy      ${key.get('usage_daily', 0):>8.2f}")
    print(f"  gastado semana   ${key.get('usage_weekly', 0):>8.2f}")
    print(f"  gastado mes      ${key.get('usage_monthly', 0):>8.2f}")
    print()
    if key.get("limit") is None:
        print("  tope de ESTA key sin tope declarado")
    else:
        print(f"  tope de ESTA key ${key['limit']:>8.2f}  (reset {key.get('limit_reset') or '—'})")
        print(f"  queda en la key  ${(key.get('limit_remaining') or 0):>8.2f}")
    if "_error" in cuenta:
        print(f"  ⚠️  no se pudo consultar el saldo de la cuenta: {cuenta['_error']}")
        cuenta = {}
    elif cuenta.get("total_credits") is not None:
        saldo = float(cuenta["total_credits"]) - float(cuenta.get("total_usage") or 0)
        print(f"  saldo de cuenta  ${saldo:>8.2f}  "
              f"({cuenta['total_credits']:,.0f} cargados, {cuenta.get('total_usage') or 0:,.2f} usados)")

    resta, limita = disponible(key, cuenta)
    if resta is None:
        print("\n  ⚠️  ni tope de key ni saldo de cuenta legibles: no se puede verificar.")
        return 0
    print(f"  disponible       ${resta:>8.2f}  ← manda la {limita}")

    if resta <= 0:
        if limita == "key":
            print("\n  🔴 la KEY llegó a su tope. Ojo: recargar la CUENTA no lo cambia —")
            print("     el límite es de la key. Súbelo o quítalo en")
            print("     openrouter.ai/settings/keys, o usa una key sin tope.")
        else:
            print("\n  🔴 la CUENTA se quedó sin saldo: recargar en openrouter.ai/settings/credits.")
        return 1
    if a.necesito is not None and resta < a.necesito:
        print(f"\n  🔴 el lote necesita ~${a.necesito:.2f} y quedan ${resta:.2f} (limita la {limita}).")
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
