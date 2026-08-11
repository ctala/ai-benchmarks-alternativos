#!/usr/bin/env python3
"""
Sincroniza los precios del catálogo contra la API de OpenRouter.

POR QUÉ EXISTE
--------------
Los precios se escribían a mano y caducan solos. Medido el 11-ago-2026: **32 de 87
modelos parseables tenían el precio equivocado**, y el costo pesa 15% del score global —
a diferencia de una suite constante, esto SÍ mueve el orden del ranking.

Los dos peores casos daban vuelta la lectura del modelo:

  · GPT-5.6 Luna  — config $1,00/$6,00  ·  real $0,10/$0,60   (sobre-costeado 10×)
  · DeepSeek V3.2 — config $0,14/$0,28  ·  real $0,26/$1,03   (sub-costeado 3,7×)

Luna es #1 del ranking mientras se le cobra 10× de más. Y publicábamos que V3.2 —el
modelo que corre en producción en Eco— era 3,7× más barato de lo que cuesta.

ESTO YA SE HIZO A MANO, Y VOLVIÓ
--------------------------------
No es la primera vez. Es la TERCERA:

  · **v2.6.3 (22-may-2026)** — "Corrección de precios verificada (OpenRouter API)".
    Mismo diagnóstico, textual: *"varios precios del catálogo estaban stale y `models.py`
    y el `PRICING` de `scoring.py` tenían drift"*. Se corrigieron 7 modelos **a mano**,
    en una tabla del CHANGELOG, y se creó `rescore_costs.py`.
  · **junio** — el ROADMAP registra "corregido drift de precio V4 Flash". Otro, a mano.
  · **11-ago-2026** — 41 modelos con drift. Varios son los MISMOS de la tabla de mayo.

El caso que lo prueba: **Grok 4.20** se corrigió en mayo de `$2/$6` a `$1.25/$2.50`.
El config del 11-ago decía `$2.00/$6.00` — **el valor exacto de antes de la corrección**.

Un precio a mano no solo caduca: **se revierte**. Por eso este archivo existe y por eso
el chequeo tiene que vivir en `check_consistency.py`, no en la memoria de nadie.

**El fix no es actualizar precios: es que dejen de escribirse a mano.**

UN SOLO PUNTO DE VERDAD
-----------------------
`benchmarks/models.py → MODELS[key]["cost_input"/"cost_output"]` es la fuente única del
precio, como ya declara el CLAUDE.md. Este script la alimenta desde OpenRouter y **nada
más escribe precios**. El resto del pipeline deriva de ahí:

  · `OR_COMPARISON_PRICING` (models.py) — NO es fuente paralela: es un post-proceso que
    solo aplica a modelos con costo 0 (los que corren gratis y se costean al equivalente
    OpenRouter para que la comparación sea justa). Se respeta y no se toca.
  · `PRICING` (scoring.py) — ERA una segunda fuente escrita a mano y divergía de MODELS
    en 25 ids. Ver `--check-pricing`: este script reporta la divergencia para que se
    derive de MODELS en vez de mantenerse aparte.
  · `rescore_costs.py` — propaga el precio del config a los runs históricos. Es el paso
    SIGUIENTE a este, ya existe, es idempotente y tiene --dry-run. No lo reimplementes.

CADENA COMPLETA
---------------
    sync_prices.py --apply      # 1. catálogo al día contra OpenRouter  (este script)
    rescore_costs.py --dry-run  # 2. ver impacto en runs históricos
    rescore_costs.py            # 3. aplicar
    export_for_pages.py         # 4. regenerar models.json del sitio

SALVAGUARDAS (por qué no puede romper el ranking)
-------------------------------------------------
  · Solo toca `cost_input`/`cost_output`. Nunca calidad, tokens, latencia ni scores.
  · **Nunca escribe $0** — regla dura del proyecto: un modelo a $0 infla el cost_score
    a ~10 y arruina la comparación, que es justo lo que la calculadora existe para evitar.
  · Solo modelos cuyo `id` matchea EXACTO en OpenRouter. Sin heurísticas de nombre.
  · Respeta `free_runtime`: esos corren gratis y se costean al equivalente OR a propósito.
  · Backup con timestamp antes de escribir.
  · Por defecto NO escribe: hay que pasar --apply.

Uso:
    python benchmarks/sync_prices.py                  # reporta el drift, no escribe
    python benchmarks/sync_prices.py --check-pricing  # + divergencia MODELS vs PRICING
    python benchmarks/sync_prices.py --apply          # escribe models.py (con backup)
    python benchmarks/sync_prices.py --tolerancia 0.05  # ignorar drift menor al 5%
"""
import argparse
import json
import re
import shutil
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

MODELS_PY = ROOT / "benchmarks" / "models.py"
# Los backups van a results/, que está gitignored: un .bak suelto al lado del fuente
# termina commiteado tarde o temprano.
BACKUPS = ROOT / "benchmarks" / "results" / "_backups"
OR_API = "https://openrouter.ai/api/v1/models"

# Bajo este valor no se considera drift: es ruido de redondeo del proveedor.
EPSILON = 0.011


def precios_openrouter() -> dict:
    """{id: (input_por_M, output_por_M)} desde la API pública (no requiere auth)."""
    with urllib.request.urlopen(OR_API, timeout=30) as r:
        data = json.load(r)["data"]
    out = {}
    for m in data:
        p = m.get("pricing") or {}
        try:
            pin = float(p.get("prompt") or 0) * 1e6
            pout = float(p.get("completion") or 0) * 1e6
        except (TypeError, ValueError):
            continue
        out[m["id"]] = (pin, pout)
    return out


def catalogo() -> dict:
    """{key: entrada} de MODELS + OLLAMA_MODELS, ya con el repricing aplicado."""
    from benchmarks.models import MODELS, OLLAMA_MODELS
    return {**MODELS, **OLLAMA_MODELS}


def detectar_drift(cat: dict, or_px: dict, tolerancia: float) -> list:
    """
    Devuelve [(key, nombre, id, (ci,co) config, (ci,co) real, motivo_skip)].

    `motivo_skip` no vacío = se reporta pero NO se toca.
    """
    filas = []
    for key, cfg in cat.items():
        mid = cfg.get("id")
        if not mid or mid not in or_px:
            continue
        ci = float(cfg.get("cost_input") or 0)
        co = float(cfg.get("cost_output") or 0)
        oi, oo = or_px[mid]

        if abs(oi - ci) <= EPSILON and abs(oo - co) <= EPSILON:
            continue

        # Drift relativo: si el mayor de los dos cambios está bajo la tolerancia, se ignora.
        rel = max(
            abs(oi - ci) / ci if ci else (1.0 if oi else 0.0),
            abs(oo - co) / co if co else (1.0 if oo else 0.0),
        )
        if rel < tolerancia:
            continue

        skip = ""
        if oi == 0 and oo == 0:
            skip = "OpenRouter reporta $0 — regla dura: nunca $0 en el ranking"
        elif cfg.get("free_runtime"):
            skip = "free_runtime: se costea al equivalente OR a propósito (OR_COMPARISON_PRICING)"

        filas.append((key, cfg.get("name", key), mid, (ci, co), (oi, oo), skip))
    return filas


def aplicar(filas: list) -> int:
    """
    Reescribe cost_input/cost_output en models.py, por bloque de modelo.

    Edición quirúrgica anclada en la **key** del dict (`"<key>": {`), NO en el `id`.

    ⚠️ Anclar por `id` fue un bug real de la primera versión: varias entradas comparten
    el mismo `id` (las variantes NIM / Ollama Cloud / suscripción / thinking del mismo
    modelo), así que `re.search` encontraba solo la primera y las demás quedaban sin
    corregir — silenciosamente. Es la misma clase de error que el #1 del post-mortem del
    16-jul ("indexar por `name` en vez de `key` colapsa duplicados"). La key es única por
    definición del dict: esa es la única ancla segura.
    """
    texto = MODELS_PY.read_text()
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = BACKUPS / f"models.py.bak-{stamp}"
    BACKUPS.mkdir(parents=True, exist_ok=True)
    shutil.copy(MODELS_PY, backup)
    print(f"  backup → {backup.relative_to(ROOT)}")

    cambios = 0
    for key, nombre, mid, (ci, co), (oi, oo), skip in filas:
        if skip:
            continue
        # Ventana del bloque: desde `"<key>": {` hasta la próxima key de primer nivel.
        m = re.search(r'^\s{4}"' + re.escape(key) + r'":\s*\{', texto, re.MULTILINE)
        if not m:
            print(f"  ⚠ sin ancla para {nombre} (key={key}) — se salta")
            continue
        ini = m.end()
        sig = re.search(r'^\s{4}"[^"]+":\s*\{', texto[ini:], re.MULTILINE)
        fin = ini + (sig.start() if sig else 3000)
        bloque = texto[ini:fin]

        nuevo, n1 = re.subn(r'("cost_input":\s*)[\d.]+', lambda mm: f"{mm.group(1)}{oi:g}", bloque, count=1)
        nuevo, n2 = re.subn(r'("cost_output":\s*)[\d.]+', lambda mm: f"{mm.group(1)}{oo:g}", nuevo, count=1)
        if not (n1 and n2):
            print(f"  ⚠ no se encontraron ambos campos de costo en {nombre} — se salta")
            continue

        texto = texto[:ini] + nuevo + texto[fin:]
        cambios += 1

    MODELS_PY.write_text(texto)
    return cambios


def check_pricing_dict() -> None:
    """Reporta la divergencia entre MODELS (fuente única) y el dict PRICING de scoring.py."""
    from benchmarks.scoring import PRICING
    cat = catalogo()
    por_id = {
        (c.get("id") or k): (float(c.get("cost_input") or 0), float(c.get("cost_output") or 0))
        for k, c in cat.items()
    }
    difs = [(k, PRICING[k], por_id[k]) for k in PRICING if k in por_id and PRICING[k] != por_id[k]]
    huerf = [k for k in PRICING if k not in por_id]
    ceros = [k for k, v in PRICING.items() if v == (0.0, 0.0)]

    print(f"\n── Segunda fuente de precio: dict PRICING (scoring.py) ──")
    print(f"  entradas: {len(PRICING)}  ·  divergen de MODELS: {len(difs)}  ·  huérfanas: {len(huerf)}")
    for k, p, m in difs[:15]:
        print(f"    {k:<44} PRICING {p}  vs  MODELS {m}")
    if ceros:
        print(f"  🔴 {len(ceros)} entradas en $0 (viola 'nunca $0 en el ranking'): {ceros[:5]}")
    print("\n  → PRICING debería DERIVARSE de MODELS, no mantenerse a mano.")
    print("    Solo lo consumen scoring.py (fallback) y rescore_costs.py (fallback por id).")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="escribir models.py (por defecto solo reporta)")
    ap.add_argument("--check-pricing", action="store_true", help="además, divergencia MODELS vs dict PRICING")
    ap.add_argument("--tolerancia", type=float, default=0.0, help="ignorar drift relativo menor a esto (0.05 = 5%%)")
    args = ap.parse_args()

    print("── Sync de precios contra OpenRouter ──")
    or_px = precios_openrouter()
    cat = catalogo()
    print(f"  OpenRouter: {len(or_px)} modelos  ·  catálogo: {len(cat)} entradas")

    filas = detectar_drift(cat, or_px, args.tolerancia)
    tocables = [f for f in filas if not f[5]]
    saltados = [f for f in filas if f[5]]

    if not filas:
        print("\n  ✓ sin drift. Nada que hacer.")
        return 0

    print(f"\n  DRIFT: {len(filas)} modelos  ({len(tocables)} a corregir · {len(saltados)} reportados sin tocar)\n")
    print(f"  {'MODELO':<34} {'CONFIG':>15} {'OPENROUTER':>15}   FACTOR")
    for _, nombre, _, (ci, co), (oi, oo), skip in sorted(filas, key=lambda f: -(f[3][1] / f[4][1] if f[4][1] else 0)):
        factor = f"{co / oo:.1f}× de más" if oo and co > oo else (f"{oo / co:.1f}× de menos" if co and oo > co else "—")
        marca = "  ⏭ " if skip else "    "
        print(f"{marca}{nombre[:34]:<34} {ci:>6.2f}/{co:<8.2f} {oi:>6.2f}/{oo:<8.2f}   {factor}")
    for _, nombre, _, _, _, skip in saltados:
        print(f"      ⏭ {nombre}: {skip}")

    if args.check_pricing:
        check_pricing_dict()

    if not args.apply:
        print(f"\n  (nada escrito — correr con --apply para aplicar los {len(tocables)})")
        return 0

    print(f"\n── Aplicando {len(tocables)} correcciones ──")
    n = aplicar(filas)
    print(f"  ✓ {n} modelos actualizados en models.py")
    print("\n  SIGUIENTE PASO (no lo hace este script):")
    print("    .venv/bin/python benchmarks/rescore_costs.py --dry-run")
    print("    .venv/bin/python benchmarks/rescore_costs.py")
    print("    .venv/bin/python benchmarks/export_for_pages.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
