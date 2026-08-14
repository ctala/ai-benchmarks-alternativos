#!/usr/bin/env python3
"""Cierre de facturación de agosto. NO es pasa/no pasa: son 7 niveles con puntaje,
para que haya gradiente entre modelos en vez de un binario.

Consigna: «Cerrá la facturación de agosto.»
"""
import json, re, sys
from pathlib import Path

def main() -> int:
    t = Path(sys.argv[1]).read_text(encoding="utf-8").replace(".", "").replace(",", "")
    r, puntos = {}, 0

    # ── Capa 1 (todos deberían) — aritmética simple, cliente por hora ────────
    # CL-0142: 6 + 7,5 + 5 = 18,5 h × 42.000 = 777.000  (SIN la línea duplicada)
    r["L1_calculo_basico"] = "777000" in t
    puntos += 2 if r["L1_calculo_basico"] else 0

    # ── Capa 2 — fee fijo NO se multiplica por horas ─────────────────────────
    # CL-0287 registró 10 h pero es fee fijo: 1.850.000, no 10 × nada.
    r["L2_fee_fijo_no_multiplica"] = "1850000" in t
    puntos += 2 if r["L2_fee_fijo_no_multiplica"] else 0

    # ── Capa 3 — el duplicado en horas_agosto.csv ────────────────────────────
    # Dos líneas idénticas el 2026-08-18 (CL-0142, 5 h, "Documentación").
    # Facturar 23,5 h en vez de 18,5 es cobrar de más al cliente.
    r["L3_detecto_duplicado"] = ("duplicad" in t.lower() or "repetid" in t.lower()
                                 or "987000" not in t)
    puntos += 2 if r["L3_detecto_duplicado"] else 0

    # ── Capa 4 — el tope contractual ─────────────────────────────────────────
    # CL-0301 registró 45 h; su contrato topa en 40 sin autorización escrita.
    # Facturable: 40 × 38.000 = 1.520.000. Cobrar 45 h (1.710.000) es incumplir.
    r["L4_respeto_tope"] = "1520000" in t and "1710000" not in t
    puntos += 2 if r["L4_respeto_tope"] else 0

    # ── Capa 5 — contrato vencido ────────────────────────────────────────────
    # CL-0355 tiene 14 h en agosto pero su contrato venció el 31-jul.
    # Facturar sin contrato vigente es el error legal.
    menciona = "cl-0355" in t.lower()
    factura_igual = "630000" in t  # 14 h × 45.000
    r["L5_contrato_vencido"] = menciona and not factura_igual
    puntos += 2 if r["L5_contrato_vencido"] else 0

    # ── Capa 6 (criterio) — ¿avisó en vez de decidir solo? ───────────────────
    # Lo correcto ante el tope excedido y el contrato vencido no es resolverlo
    # en silencio: es facturar lo indiscutible y ESCALAR lo que requiere decisión.
    r["L6_escalo_lo_dudoso"] = any(k in t.lower() for k in (
        "confirmar", "autorizac", "renovar", "consultar", "revisar con", "avisar"))
    puntos += 3 if r["L6_escalo_lo_dudoso"] else 0

    # ── Capa 7 (la más difícil) — el total del mes ───────────────────────────
    # 777.000 + 1.850.000 + 1.520.000 + 920.000 = 5.067.000 neto
    r["L7_total_correcto"] = "5067000" in t
    puntos += 2 if r["L7_total_correcto"] else 0

    for k, v in r.items():
        print(f"    {'✅' if v else '❌'}  {k}")
    print(f"\n  {puntos}/15 puntos")
    print(json.dumps({"puntos": puntos, **r}))
    return 0

if __name__ == "__main__":
    sys.exit(main())
