#!/usr/bin/env python3
"""El censo de POR DÓNDE se puede consumir cada modelo del ranking.

POR QUÉ EXISTE (19-sep-2026)
----------------------------
Cristian, usando Qwen por un token plan servido desde Singapur: *«una vez que ya definas
el modelo que quieres, la idea es que sea aún más eficiente con un token plan, una coding
subscription… si uno eligiera qwen3.8 como su modelo por defecto, cuál sería la mejor
manera de usarlo, contra qué proveedor»*.

El benchmark respondía la mitad de la pregunta. Decía **qué modelo** y cuánto cuesta por
token en OpenRouter, y nada sobre **cómo consumirlo**. Y esa mitad no es menor:

  · 76 de 102 modelos rankeados los sirve MÁS DE UN proveedor (GLM 5.3: treinta y cuatro).
  · 21 no tienen elección: un solo proveedor. `Qwen 3.8 Flash` es uno — sale de Alibaba o
    no sale, y por eso te toca su infraestructura.
  · El precio NO es lo único que cambia. En `Qwen 3.8 27B` va de $0,10 a $0,25 el millón
    de entrada, pero el de $0,10 sirve en **fp4** y el de $0,15 en **bf16**. Y en
    `Qwen 3.8 2.4T` los siete proveedores cobran EXACTAMENTE lo mismo ($2/$6) sirviendo
    fp4 con 262K de contexto unos y fp8 con 1M otros. Mismo precio, producto distinto.

Eso último explica lo que el repo ya había medido sin poder atribuirlo: que el mismo
modelo rinda distinto según quién lo sirva (ver `/mismo-modelo-distinto-proveedor/`). No
es «el proveedor»: es la cuantización y el contexto con que te lo entregan.

POR QUÉ NO VA EN `regenerate_all`
---------------------------------
Hace una llamada HTTP por modelo. El pipeline maestro no puede depender de una API
externa: un timeout de OpenRouter dejaría el repo sin poder regenerar artefactos que no
tienen nada que ver. Se corre a demanda; el QA sólo mira la FECHA (sin red) y avisa
cuando el censo envejece — que es exactamente como se pudrió `SUSCRIPCIONES.md`, con
precios de abril vivos en septiembre.

Uso:
    python benchmarks/generate_censo_proveedores.py           # consulta y escribe
    python benchmarks/generate_censo_proveedores.py --check   # solo la fecha, sin red
"""

import argparse
import json
import sys
import time
import urllib.request
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODELS_JSON = ROOT / "docs" / "data" / "models.json"
SALIDA = ROOT / "docs" / "data" / "censo_proveedores.json"
API = "https://openrouter.ai/api/v1/models/{id}/endpoints"

# Los precios y la cuantización de un endpoint cambian sin aviso. Un mes es el plazo en el
# que un dato así todavía sirve para decidir; más allá, es un rumor con formato de tabla.
CADUCIDAD_DIAS = 30
PAUSA_S = 0.25          # cortesía con la API pública: ~100 modelos = ~30 s


def _consultar(model_id: str) -> list[dict]:
    with urllib.request.urlopen(API.format(id=model_id), timeout=20) as r:
        data = json.loads(r.read()).get("data") or {}
    fuera = []
    for e in data.get("endpoints") or []:
        p = e.get("pricing") or {}
        fuera.append({
            "proveedor": e.get("provider_name"),
            "precio_in_por_M": round(float(p.get("prompt") or 0) * 1e6, 4),
            "precio_out_por_M": round(float(p.get("completion") or 0) * 1e6, 4),
            "contexto": e.get("context_length"),
            "cuantizacion": e.get("quantization"),
        })
    return sorted(fuera, key=lambda x: (x["precio_in_por_M"], x["precio_out_por_M"]))


def construir() -> dict:
    d = json.loads(MODELS_JSON.read_text())
    rankeados = [m for m in d["models"] if m.get("ranked")]
    modelos, sin_datos = {}, []
    for m in rankeados:
        mid = str(m.get("id") or "")
        # Un id sin exactamente un "/" no es un slug de OpenRouter: son los medidos por la
        # API del fabricante (MiniMax, Xiaomi) o por suscripción. No es un error: es que
        # ese modelo no se consume por ahí, y el censo tiene que decirlo en vez de omitirlo.
        if mid.count("/") != 1:
            sin_datos.append({"modelo": m["name"], "id": mid, "motivo": "no se sirve por OpenRouter"})
            continue
        try:
            eps = _consultar(mid)
        except Exception as ex:
            sin_datos.append({"modelo": m["name"], "id": mid, "motivo": f"{type(ex).__name__}"})
            continue
        modelos[m["key"]] = {"nombre": m["name"], "id": mid, "endpoints": eps}
        time.sleep(PAUSA_S)

    proveedores = defaultdict(lambda: {"modelos": 0, "cuantizaciones": Counter()})
    for v in modelos.values():
        for e in v["endpoints"]:
            p = proveedores[e["proveedor"]]
            p["modelos"] += 1
            p["cuantizaciones"][str(e["cuantizacion"])] += 1
    prov_out = {k: {"modelos": v["modelos"], "cuantizaciones": dict(v["cuantizaciones"])}
                for k, v in sorted(proveedores.items(), key=lambda kv: -kv[1]["modelos"])}

    return {
        "consultado_at": datetime.now().isoformat(timespec="seconds"),
        "fuente": "https://openrouter.ai/api/v1/models/{id}/endpoints",
        "caducidad_dias": CADUCIDAD_DIAS,
        "totales": {
            "modelos_rankeados": len(rankeados),
            "modelos_con_censo": len(modelos),
            "proveedores_distintos": len(prov_out),
            "modelos_con_un_solo_proveedor": sum(1 for v in modelos.values() if len(v["endpoints"]) == 1),
        },
        "proveedores": prov_out,
        "modelos": modelos,
        "sin_datos": sin_datos,
    }


def edad_dias() -> int | None:
    if not SALIDA.exists():
        return None
    try:
        c = json.loads(SALIDA.read_text()).get("consultado_at")
        return (date.today() - datetime.fromisoformat(c).date()).days
    except Exception:
        return None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true",
                    help="solo verifica la FECHA del censo (no toca la red)")
    a = ap.parse_args()

    if a.check:
        d = edad_dias()
        if d is None:
            print(f"  ⏭️  sin censo en {SALIDA.name}: nadie sabe por dónde se puede "
                  f"consumir cada modelo. Correr sin --check.")
            return 0
        if d > CADUCIDAD_DIAS:
            print(f"  ⚠️  el censo de proveedores tiene {d} días (máximo {CADUCIDAD_DIAS}): "
                  f"precios y cuantizaciones cambian sin aviso. Regeneralo antes de citarlo.")
            return 0
        print(f"  ✅ censo de proveedores al día ({d} días)")
        return 0

    censo = construir()
    SALIDA.write_text(json.dumps(censo, ensure_ascii=False, indent=1), encoding="utf-8")
    t = censo["totales"]
    print(f"  ✅ {SALIDA.relative_to(ROOT)} · {t['modelos_con_censo']}/{t['modelos_rankeados']} "
          f"modelos · {t['proveedores_distintos']} proveedores distintos")
    print(f"     {t['modelos_con_un_solo_proveedor']} modelos tienen UN SOLO proveedor (sin elección)")
    if censo["sin_datos"]:
        print(f"     {len(censo['sin_datos'])} sin censo (no se sirven por OpenRouter)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
