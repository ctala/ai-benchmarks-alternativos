#!/usr/bin/env python3
"""Verifica la cotización del agente. SIETE capas con puntaje, no pasa/no pasa.

La verdad de terreno la calcula `motor_referencia.py`. Consigna al agente:
«Cotizá el encargo del cliente.»
"""
import json, re, sys
from pathlib import Path

def _sumas_posibles(precios: set) -> set:
    """Totales que se pueden formar sumando ítems del tarifario, con o sin ajuste.
    Sirve para no marcar un TOTAL legítimo como precio inventado."""
    from itertools import combinations
    out = set()
    ps = sorted(precios)
    for n in range(1, 5):
        for combo in combinations(ps, n):
            base = sum(combo)
            for f in [x / 100 for x in range(85, 201, 5)]:
                out.add(round(base * f))
    return out


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
    # El archivo guarda ENTRADA y SALIDA (trazabilidad). Se puntúa solo la salida: si no,
    # el enunciado —que menciona los precios del tarifario— contaría como si el modelo los
    # hubiera escrito.
    if "# SALIDA" in t:
        t = t.split("# SALIDA", 1)[1]
    n = t.replace(".", "").replace(",", "").lower()   # números sin separadores
    r, pts = {}, 0

    # Una respuesta VACÍA no puede puntuar. Los checks negativos —"no cotizó el
    # diagnóstico", "no cobró las dos implementaciones"— los aprueba el silencio, así
    # que el vacío sacaba 7/17. Un scorer que premia no responder está roto, y fue lo
    # que hizo que seis modelos empataran en 7,0 con varianza cero. (13-ago-2026)
    if len(t.strip()) < 80:
        print("    ❌  respuesta vacía o truncada — 0 puntos")
        print(json.dumps({"puntos": 0, "vacia": True}))
        return 0

    cobra = _montos_cobrados(t)

    # ── C1 (2) el servicio correcto de implementación ────────────────────────
    # También vale si cotizó la avanzada ajustada (4.800 × factor dentro de banda).
    r["C1_implementacion"] = ("impl-avz" in t.lower() or 4800 in cobra
                              or any(abs(c - 4800 * f) < 1 for c in cobra
                                     for f in [x / 100 for x in range(85, 201)]))
    pts += 2 if r["C1_implementacion"] else 0

    # ── C2 (3) ABSORCIÓN: no cobra la básica además de la avanzada ───────────
    # Cobrar las dos son $2.400 de más. El tarifario lo dice en la columna `absorbe`.
    # Se mira si COBRA las dos, no si las nombra: nombrar la básica para decir que
    # está absorbida es la respuesta correcta.
    r["C2_absorcion"] = not (2400 in cobra and 4800 in cobra)
    pts += 3 if r["C2_absorcion"] else 0

    # ── C3 (3) NO descontó por "solo revisar" ────────────────────────────────
    # MIGRA-REV vale 1600, igual que MIGRA. Un descuento acá es inventado.
    # `800` era un bug: "4.800" lo contiene. Se comparan MONTOS, no substrings.
    # El 1.600 puede aparecer como referencia o ajustado. Lo que NO puede aparecer es
    # un valor por DEBAJO de 1.600×0,85: eso sería el descuento por "solo revisar".
    ref_rev = [c for c in cobra if abs(c - 1600) < 1
               or any(abs(c - 1600 * f) < 1 for f in [x / 100 for x in range(85, 201)])]
    r["C3_revision_sin_descuento"] = bool(ref_rev) and not ({1280, 1200} & cobra)
    pts += 3 if r["C3_revision_sin_descuento"] else 0

    # ── C4 (2) no cotizó el diagnóstico que el cliente ya tiene ──────────────
    # Se mira si lo COBRA. Decir "no cotizo el diagnóstico porque ya lo tienen" es
    # exactamente lo correcto, y el check anterior lo reprobaba por nombrarlo.
    r["C4_no_cotizo_diagnostico"] = 900 not in cobra
    pts += 2 if r["C4_no_cotizo_diagnostico"] else 0

    # ── C5 (3) escaló lo que NO está en el tarifario ─────────────────────────
    # "terminar la migración ajena" no existe como servicio → cotización humana.
    # BUG que esto corrige (4º del día, y el que produjo la conclusión equivocada de
    # que "ningún modelo sirve"): buscaba FRASES EXACTAS ("cotización humana", "no está
    # en el tarifario") y fallaba en el 81% de las corridas. Los modelos SÍ lo señalaban,
    # con otras palabras: GPT-5.6 Luna escribió *"el tarifario contempla la revisión de
    # una migración ajena, pero no especifica un servicio separado para terminar o
    # corregir una migración iniciada"* — impecable, y reprobado.
    #
    # Se verifica lo que HIZO, no cómo lo dijo: el fallo real es INVENTAR un precio para
    # el trabajo no tarifado. Si todos los montos cobrados salen del tarifario (solos o
    # ajustados dentro de banda), no inventó nada. Eso es objetivo y no depende del
    # vocabulario. Es el mismo arreglo que C3 y C4: mirar la acción, no la prosa.
    PRECIOS = {900, 2400, 4800, 1600, 700, 1200, 2100}
    def _del_tarifario(c):
        return any(abs(c - base * f) < 1 for base in PRECIOS
                   for f in [x / 100 for x in range(85, 201)])
    montos_grandes = [c for c in cobra if c >= 500 and c != 8500]
    inventados = [c for c in montos_grandes
                  if not _del_tarifario(c) and not any(
                      abs(c - s) < 1 for s in _sumas_posibles(PRECIOS))]
    r["C5_escalo_lo_no_tarifado"] = not inventados
    pts += 3 if r["C5_escalo_lo_no_tarifado"] else 0

    # ── C6 (2) si ajustó por urgencia, lo hizo DENTRO de banda y por escrito ──
    # El factor puede venir como "1,25" o "1.25". Se normaliza la coma decimal antes
    # de convertir — `float("1,25")` revienta, y reventaba con la respuesta real.
    factores = [float(x.replace(",", "."))
                for x in re.findall(r'\b([12][.,]\d{1,2}|0[.,]9\d)\b', t)]
    fuera = [f for f in factores if f > 2.0 or f < 0.85]
    menciona = any(k in t.lower() for k in ("urgencia", "fin de mes", "plazo", "ajuste"))
    r["C6_ajuste_declarado"] = (not factores) or (not fuera and menciona)
    pts += 2 if r["C6_ajuste_declarado"] else 0

    # ── C7 (2) el total cuadra — CON o SIN ajuste de urgencia ────────────────
    # BUG que esto corrige (13-ago): exigía exactamente 8.500, o sea el total SIN
    # ajuste. Pero la regla 2 permite ajustar por urgencia dentro de 0,85-2,00, y el
    # encargo dice "lo necesitamos para fin de mes". GPT-5.6 Luna aplicó 1,25 sobre el
    # precio de referencia, lo declaró con su motivo, y sacó el total correcto: 10.625.
    # Mi check lo reprobó por aplicar BIEN la regla. Tercera vez en el día que un
    # verificador mío castiga el comportamiento correcto.
    BASE = 8500
    r["C7_total"] = any(abs(c - BASE * f) < 1
                        for c in cobra
                        for f in [x / 100 for x in range(85, 201)])
    pts += 2 if r["C7_total"] else 0

    for k, v in r.items():
        print(f"    {'✅' if v else '❌'}  {k}")
    print(f"\n  {pts}/17 puntos")
    print(json.dumps({"puntos": pts, **r}))
    return 0

if __name__ == "__main__":
    sys.exit(main())
