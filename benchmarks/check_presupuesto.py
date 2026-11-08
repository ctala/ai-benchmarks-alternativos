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

Y LO QUE EL SALDO NO VE: LAS RUTAS BYOK (6-nov-2026)
---------------------------------------------------
Anthropic por OpenRouter va con la API key propia de Cristian (BYOK): el costo se cobra en
la cuenta de Anthropic y el saldo de OpenRouter solo baja la comisión. La remedición de los
Claude 5.5 costó $13,79 a precio de lista y el saldo bajó $0,34; el vigilante del tope, que
leía el delta del saldo, no vio el gasto. Ahora el gasto de un lote es el delta del saldo
(lo que paga OpenRouter, juez incluido) MÁS lo de las rutas de `RUTAS_BYOK` contado por
tokens × precio de lista, en los runs del runner y en los intentos de Harbor.

Uso:
    python benchmarks/check_presupuesto.py                 # cuánto queda
    python benchmarks/check_presupuesto.py --necesito 30   # exit 1 si no alcanza (OpenRouter)
    python benchmarks/check_presupuesto.py --gasto-lote <usado_base> \
        --runs 'benchmarks/results/benchmark_X_*.json' --harbor 'jobs/v5__*' --tope 15
                                                           # exit 3 si el lote pasó el tope
"""

import argparse
import glob
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


# proveedor (como lo registra OpenRouter, sin mayúsculas) → por qué no pasa por el saldo.
RUTAS_BYOK = {
    "anthropic": "API key propia de Anthropic en OpenRouter: se cobra en la cuenta de "
                 "Anthropic, no en el saldo de OpenRouter (6-nov-2026)",
}


def es_byok(proveedor: str | None) -> bool:
    return bool(proveedor) and str(proveedor).strip().casefold() in RUTAS_BYOK


def _precios() -> dict[str, tuple[float, float]]:
    sys.path.insert(0, str(ROOT / "benchmarks"))
    from models import MODELS, OLLAMA_MODELS
    return {c["id"]: (c["cost_input"], c.get("cost_output") or 0)
            for c in {**OLLAMA_MODELS, **MODELS}.values()
            if c.get("id") and c.get("cost_input") is not None}


def gasto_byok_runs(runs: list[dict], precios: dict) -> float:
    """USD de los runs servidos por una ruta BYOK: tokens × precio de lista. Pura.

    Un proveedor multi-turno se registra `A|B`: cuenta si alguno de los tramos es BYOK
    (para un tope, contar de más es seguro; contar de menos es lo que falló)."""
    total = 0.0
    for r in runs:
        provs = str(r.get("upstream_provider") or "").split("|")
        if not any(es_byok(p) for p in provs):
            continue
        pi, po = precios.get(r.get("model_id"), (0.0, 0.0))
        total += (r.get("input_tokens") or 0) / 1e6 * pi + (r.get("output_tokens") or 0) / 1e6 * po
    return total


def gasto_byok_harbor(intentos: list[tuple[str, str]]) -> float:
    """USD de los intentos de Harbor servidos por una ruta BYOK. `intentos` son pares
    (texto de la trayectoria, id del modelo). Usa el mismo costeo que `export_harbor`
    (tokens × precio del catálogo) y el proveedor que la trayectoria registra."""
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from benchmarks import export_harbor as eh
    total = 0.0
    for tray, modelo in intentos:
        if any(es_byok(p) for p in eh._proveedores(tray)):
            total += eh._costo(tray, modelo)[0] or 0.0
    return total


def _intentos_harbor(patrones: list[str]) -> list[tuple[str, str]]:
    out = []
    for pat in patrones:
        for job in sorted(Path(x) for x in glob.glob(str(ROOT / pat))):
            for trial in sorted(job.glob("*__*")):
                tp = trial / "agent" / "mini-swe-agent.trajectory.json"
                cp = trial / "config.json"
                if not (tp.exists() and cp.exists()):
                    continue
                try:
                    modelo = (json.loads(cp.read_text()).get("agent") or {}).get("model_name") or ""
                except Exception:
                    continue
                out.append((tp.read_text(errors="replace"), modelo.replace("openrouter/", "")))
    return out


def gasto_lote(usado_base: float, usado_ahora: float, runs_globs: list[str],
               harbor_globs: list[str]) -> dict:
    """{'openrouter', 'byok_runs', 'byok_harbor', 'total'} en USD."""
    runs = []
    for pat in runs_globs:
        for f in sorted(Path(x) for x in glob.glob(str(ROOT / pat))):
            try:
                runs += json.loads(f.read_text()).get("results") or []
            except Exception:
                continue
    br = gasto_byok_runs(runs, _precios())
    bh = gasto_byok_harbor(_intentos_harbor(harbor_globs))
    orr = max(0.0, usado_ahora - usado_base)
    return {"openrouter": orr, "byok_runs": br, "byok_harbor": bh, "total": orr + br + bh}


def main_gasto_lote(a) -> int:
    if a.usado_ahora is not None:
        ahora = a.usado_ahora
    else:
        e = estado()
        if e is None or "_error" in e[1] or e[1].get("total_usage") is None:
            print("  🔴 no se pudo leer el uso de OpenRouter: el tope no se puede vigilar")
            return 2
        ahora = float(e[1]["total_usage"])
    g = gasto_lote(a.gasto_lote, ahora, a.runs or [], a.harbor or [])
    print(f"gasto_lote total=${g['total']:.2f} · openrouter=${g['openrouter']:.2f} · "
          f"byok_runs=${g['byok_runs']:.2f} · byok_harbor=${g['byok_harbor']:.2f}")
    if a.tope is not None and g["total"] > a.tope:
        print(f"  🔴 TOPE_SUPERADO: ${g['total']:.2f} > ${a.tope:.2f}")
        return 3
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--necesito", type=float, default=None,
                    help="USD que va a costar el lote; exit 1 si no alcanza")
    ap.add_argument("--gasto-lote", type=float, default=None, metavar="USADO_BASE",
                    help="gasto del lote desde este `total_usage` de OpenRouter, más las rutas "
                         "BYOK contadas por tokens × precio de lista")
    ap.add_argument("--runs", nargs="*", help="globs de archivos del runner del lote")
    ap.add_argument("--harbor", nargs="*", help="globs de trabajos de Harbor del lote (jobs/...)")
    ap.add_argument("--tope", type=float, default=None, help="exit 3 si el gasto del lote lo pasa")
    ap.add_argument("--usado-ahora", type=float, default=None, help=argparse.SUPPRESS)
    a = ap.parse_args()
    if a.gasto_lote is not None:
        return main_gasto_lote(a)

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
        print(f"     Ojo: lo de las rutas BYOK ({', '.join(RUTAS_BYOK)}) no sale de este saldo;")
        print(f"     el tope del lote lo vigila `--gasto-lote`, que sí lo cuenta.")
    else:
        print("\n  ✅ hay presupuesto.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
