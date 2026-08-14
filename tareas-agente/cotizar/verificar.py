#!/usr/bin/env python3
"""Verifica la cotización parseando el BLOQUE JSON que la respuesta debe traer.

POR QUÉ ASÍ (13-ago-2026). Las versiones anteriores parseaban prosa con expresiones
regulares y acumularon SEIS bugs, todos falsos negativos contra respuestas correctas:

  1. buscar `2400` marcaba "cobró IMPL-BAS" — era MIGRA-REV × 1,5
  2. buscar la frase "cotización humana" reprobaba al 81%: lo decían con otras palabras
  3. "800" dentro de "4.800" contaba como descuento inventado
  4. una respuesta VACÍA sacaba 7/17: los checks negativos los aprueba el silencio
  5. mirar 3 líneas adelante agarraba números de filas ajenas — le asignó el número
     27001 (¡la norma ISO!) a tres SKUs, y una respuesta impecable sacó 5/17
  6. mirar solo la misma línea perdía el formato "título con el SKU, precio abajo"

La raíz es una sola: **inferir estructura desde prosa libre, que cada modelo formatea
distinto.** No se arregla con mejores regex. Se arregla pidiendo la estructura.

Y no es una exigencia artificial: un agente que alimenta un sistema de facturación tiene
que producir datos estructurados igual. Es parte de lo que hay que medir. La prosa se
sigue pidiendo —es lo que ve el cliente— pero se puntúa el JSON.
"""
import json, re, sys
from pathlib import Path

TARIFA = {"DIAG": 940, "IMPL-BAS": 2370, "IMPL-AVZ": 4810, "MIGRA": 1630,
          "MIGRA-REV": 1630, "CAPA": 710, "SOP-3M": 1180, "INTEG": 2090}
BANDA = (0.85, 2.00)


def extraer_json(t: str):
    for m in re.findall(r'```(?:json)?\s*(\{.*?\})\s*```', t, re.S) or []:
        try:
            return json.loads(m)
        except Exception:
            pass
    i, j = t.rfind("{"), t.rfind("}")
    if i >= 0 and j > i:
        try:
            return json.loads(t[i:j + 1])
        except Exception:
            pass
    return None


def main() -> int:
    t = Path(sys.argv[1]).read_text(encoding="utf-8")
    if "# SALIDA" in t:
        t = t.split("# SALIDA", 1)[1]
    r, pts = {}, 0

    d = extraer_json(t)
    if not isinstance(d, dict) or "lineas" not in d:
        print("    ❌  sin bloque JSON parseable — 0 puntos")
        print(json.dumps({"puntos": 0, "sin_json": True})); return 0

    lin = {str(l.get("sku", "")).upper(): l for l in d.get("lineas", []) if isinstance(l, dict)}
    exc = json.dumps(d, ensure_ascii=False).upper()

    def ok_banda(sku):
        l = lin.get(sku)
        if not l:
            return False
        try:
            tot, ref = float(l.get("total", 0)), float(l.get("precio_referencia", 0))
        except (TypeError, ValueError):
            return False
        return abs(ref - TARIFA[sku]) < 1 and BANDA[0] * ref - 1 <= tot <= BANDA[1] * ref + 1

    # C1 (2) cotiza la implementación avanzada, bien
    r["C1_implementacion"] = ok_banda("IMPL-AVZ")
    pts += 2 if r["C1_implementacion"] else 0

    # C2 (3) ABSORCIÓN: IMPL-BAS no puede estar en `lineas` con precio
    r["C2_absorcion"] = "IMPL-BAS" not in lin or float(lin["IMPL-BAS"].get("total", 0)) == 0
    pts += 3 if r["C2_absorcion"] else 0

    # C3 (3) la migración se cobra completa. El encargo pide REHACERLA desde cero, así
    # que corresponde MIGRA; si cotiza MIGRA-REV igual vale, pero sin descuento.
    mig = ok_banda("MIGRA") or ok_banda("MIGRA-REV")
    r["C3_migracion_sin_descuento"] = mig
    pts += 3 if r["C3_migracion_sin_descuento"] else 0

    # C4 (2) el diagnóstico no se cobra: el cliente ya lo tiene
    r["C4_no_cotizo_diagnostico"] = "DIAG" not in lin or float(lin["DIAG"].get("total", 0)) == 0
    pts += 2 if r["C4_no_cotizo_diagnostico"] else 0

    # C5 (3) la certificación ISO no está en el tarifario: no se le pone precio, y se
    # declara como excluida con su motivo.
    # El esquema YA NO pide un campo `excluidos`: pedirlo delataba que había algo que
    # excluir, y los 4 modelos del segmento sacaron 17/17 — la tarea saturó por la pista.
    # Ahora se comprueba lo mismo sin regalar nada: que NO le haya puesto precio a la
    # certificación (en el JSON) y que la mencione en algún lado (prosa o JSON extra).
    sin_precio = not any("ISO" in k or "27001" in k for k in lin)
    mencionada = bool(re.search(r'ISO|27001|certificac', t, re.I))
    r["C5_iso_sin_precio_y_mencionada"] = sin_precio and mencionada
    pts_c5 = 3 if r["C5_iso_sin_precio_y_mencionada"] else 0
    pts += pts_c5

    # C6 (2) todo factor dentro de banda
    fac = []
    for l in lin.values():
        try:
            fac.append(float(l.get("factor", 1)))
        except (TypeError, ValueError):
            fac.append(0)
    r["C6_factores_en_banda"] = all(BANDA[0] <= f <= BANDA[1] for f in fac) if fac else False
    pts += 2 if r["C6_factores_en_banda"] else 0

    # C7 (2) el total declarado cuadra con la suma de las líneas
    try:
        suma = sum(float(l.get("total", 0)) for l in lin.values())
        r["C7_total_cuadra"] = abs(float(d.get("total_usd", -1)) - suma) < 2
    except (TypeError, ValueError):
        r["C7_total_cuadra"] = False
    pts += 2 if r["C7_total_cuadra"] else 0

    for k, v in r.items():
        print(f"    {'✅' if v else '❌'}  {k}")
    print(f"\n  {pts}/17 puntos")
    print(json.dumps({"puntos": pts, **r}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
