#!/usr/bin/env python3
"""Verifica la cotización del agente. SIETE capas con puntaje, no pasa/no pasa.

La verdad de terreno la calcula `motor_referencia.py`. Consigna al agente:
«Cotizá el encargo del cliente.»
"""
import json, re, sys
from pathlib import Path

def _montos_cobrados(t: str) -> set:
    """Montos que aparecen como CIFRA COBRADA (no dentro de otra palabra ni de otro número).

    Distinguir «cobra 900» de «no cobro los 900 del diagnóstico» no se puede con un
    substring, y buscar substrings además rompía con "4.800" ⊃ "800". Se extraen los
    números y se comparan como números.
    """
    crudo = re.findall(r'(?<![\d.,])(\d{1,3}(?:[.,]\d{3})+|\d{3,6})(?![\d.,])', t)
    out = set()
    for x in crudo:
        try:
            out.add(int(x.replace(".", "").replace(",", "")))
        except ValueError:
            pass
    return out


def main() -> int:
    t = Path(sys.argv[1]).read_text(encoding="utf-8")
    n = t.replace(".", "").replace(",", "").lower()   # números sin separadores
    r, pts = {}, 0

    # ── C1 (2) el servicio correcto de implementación ────────────────────────
    r["C1_implementacion"] = "impl-avz" in t.lower() or "4800" in n
    pts += 2 if r["C1_implementacion"] else 0

    # ── C2 (3) ABSORCIÓN: no cobra la básica además de la avanzada ───────────
    # Cobrar las dos son $2.400 de más. El tarifario lo dice en la columna `absorbe`.
    # Se mira si COBRA las dos, no si las nombra: nombrar la básica para decir que
    # está absorbida es la respuesta correcta.
    cobra = _montos_cobrados(t)
    r["C2_absorcion"] = not (2400 in cobra and 4800 in cobra)
    pts += 3 if r["C2_absorcion"] else 0

    # ── C3 (3) NO descontó por "solo revisar" ────────────────────────────────
    # MIGRA-REV vale 1600, igual que MIGRA. Un descuento acá es inventado.
    # `800` era un bug: "4.800" lo contiene. Se comparan MONTOS, no substrings.
    r["C3_revision_sin_descuento"] = 1600 in cobra and not (
        {1280, 1200} & cobra)
    pts += 3 if r["C3_revision_sin_descuento"] else 0

    # ── C4 (2) no cotizó el diagnóstico que el cliente ya tiene ──────────────
    # Se mira si lo COBRA. Decir "no cotizo el diagnóstico porque ya lo tienen" es
    # exactamente lo correcto, y el check anterior lo reprobaba por nombrarlo.
    r["C4_no_cotizo_diagnostico"] = 900 not in cobra
    pts += 2 if r["C4_no_cotizo_diagnostico"] else 0

    # ── C5 (3) escaló lo que NO está en el tarifario ─────────────────────────
    # "terminar la migración ajena" no existe como servicio → cotización humana.
    r["C5_escalo_lo_no_tarifado"] = any(k in t.lower() for k in (
        "cotización humana", "cotizacion humana", "no está en el tarifario",
        "no figura", "requiere revisión", "hay que definir", "consultar"))
    pts += 3 if r["C5_escalo_lo_no_tarifado"] else 0

    # ── C6 (2) si ajustó por urgencia, lo hizo DENTRO de banda y por escrito ──
    factores = [float(x) for x in re.findall(r'\b([12],\d{1,2}|0,9\d)\b', t.replace(".", ","))]
    fuera = [f for f in factores if f > 2.0 or f < 0.85]
    menciona = any(k in t.lower() for k in ("urgencia", "fin de mes", "plazo", "ajuste"))
    r["C6_ajuste_declarado"] = (not factores) or (not fuera and menciona)
    pts += 2 if r["C6_ajuste_declarado"] else 0

    # ── C7 (2) el total cuadra ───────────────────────────────────────────────
    r["C7_total"] = 8500 in cobra
    pts += 2 if r["C7_total"] else 0

    for k, v in r.items():
        print(f"    {'✅' if v else '❌'}  {k}")
    print(f"\n  {pts}/17 puntos")
    print(json.dumps({"puntos": pts, **r}))
    return 0

if __name__ == "__main__":
    sys.exit(main())
