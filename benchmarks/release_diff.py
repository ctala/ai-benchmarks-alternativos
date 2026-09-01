#!/usr/bin/env python3
"""
Qué cambió entre dos versiones del benchmark, ordenado por impacto en una DECISIÓN.

POR QUÉ EXISTE
--------------
El release mensual se escribía a mano: alguien releía el CHANGELOG, se acordaba de lo
que había pasado y redactaba el DATASHEET. Dos problemas, los dos reales:

  1. **Lo que se olvida no se publica.** El 12-ago-2026 descubrimos que Nemotron Super
     49B v1.5 —#8 del ranking, recomendado en 10 páginas del sitio— llevaba tiempo
     muerto. Nadie lo iba a recordar en el resumen del mes, porque nadie lo sabía.
  2. **Lo que se escribe a mano caduca.** Es la misma lección de los scores hardcodeados
     (v3.1.2, julio 2026: el README publicaba Grok 4.5 = 6.99 y el sitio 5.84).

El dato ya está: `docs/data/models.json` se commitea con cada release, así que **git
guarda un snapshot completo por versión**. Este script los compara.

EL ORDEN IMPORTA — y no es alfabético ni por score
--------------------------------------------------
Las secciones salen ordenadas por **cuánto le cambian la decisión a quien lee**:

  1. Los que ya no se pueden usar   → si lo integraste, se te rompe HOY
  2. Los que cambiaron de precio    → te cambia el costo del mes que viene
  3. Los que se movieron de puesto  → cambia tu elección si estabas por decidir
  4. Los que entraron               → una opción nueva que no tenías
  5. Los que resucitaron            → volvió algo que dábamos por perdido

Un modelo que muere vale más titular que uno que sube 0,3 puntos. La tabla ordenada por
score dice lo contrario, y por eso no se usa acá.

Uso:
    python benchmarks/release_diff.py                      # último tag → estado actual
    python benchmarks/release_diff.py --desde v4.0.0       # desde un tag concreto
    python benchmarks/release_diff.py --desde v4.0.0 --hasta v4.1.0
    python benchmarks/release_diff.py --umbral 0.2         # solo movimientos ≥0,2
    python benchmarks/release_diff.py -o DATASHEET_2026-08.md   # escribe a un archivo
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODELS_JSON_REL = "docs/data/models.json"

# Bajo esto, un movimiento de score es ruido y no entra al resumen.
UMBRAL_SCORE = 0.10
# Bajo esto, un cambio de precio es redondeo del proveedor, no una noticia.
UMBRAL_PRECIO_REL = 0.05


def _git(*args: str) -> str:
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(f"git {' '.join(args)} falló:\n{r.stderr.strip()}")
    return r.stdout


def ultimo_tag() -> str:
    tags = _git("tag", "--sort=-v:refname").split()
    if not tags:
        raise SystemExit(
            "No hay ningún tag en el repo. Este script compara VERSIONES: creá el primero\n"
            "  git tag -a v4.0.0 -m 'primera versión' <commit>\n"
            "o pasá --desde <commit>."
        )
    return tags[0]


def snapshot(ref: str | None) -> dict:
    """models.json en un ref de git. `None` = el archivo del working tree (estado actual)."""
    if ref is None:
        p = ROOT / MODELS_JSON_REL
        if not p.exists():
            raise SystemExit(f"No existe {p}. Corré export_for_pages.py primero.")
        data = json.loads(p.read_text())
    else:
        data = json.loads(_git("show", f"{ref}:{MODELS_JSON_REL}"))
    # SIEMPRE por `key`. Indexar por `name` colapsa las entradas que comparten nombre
    # (la directa y su twin `or-`, las variantes de proveedor) y te deja leyendo la que
    # quedó última — que puede ser la vacía. Es el error #1 del post-mortem del 16-jul,
    # que llegó a borrar una sección correcta del pilar del blog.
    return {m["key"]: m for m in data.get("models", [])}


def _puestos(snap: dict) -> dict:
    rank = sorted((m for m in snap.values() if m.get("ranked")),
                  key=lambda x: -(x.get("quality_avg") or 0))
    return {m["key"]: i for i, m in enumerate(rank, 1)}


def _fmt_precio(m: dict) -> str:
    ci, co = m.get("cost_input_per_M"), m.get("cost_output_per_M")
    return f"${ci}/{co}" if ci is not None and co is not None else "—"


def construir(a: dict, b: dict, umbral: float) -> list[str]:
    pa, pb = _puestos(a), _puestos(b)
    L: list[str] = []

    # ── 1. Murieron ──────────────────────────────────────────────────────────
    murieron = [k for k in b if b[k].get("retired") and not a.get(k, {}).get("retired")]
    if murieron:
        L += ["### ⚠️ Ya no se pueden usar", "",
              "Si integraste alguno de estos, **se te rompe hoy**. Sus datos quedan en el "
              "histórico, pero salen del ranking y de las recomendaciones.", "",
              "| Modelo | Estaba | Runs | Causa | Sigue vivo en |", "|---|---|---:|---|---|"]
        vivos_por_id = {}
        for m in b.values():
            if not m.get("retired"):
                vivos_por_id.setdefault(m.get("id"), []).append(m)
        for k in sorted(murieron, key=lambda x: pa.get(x, 999)):
            m = b[k]
            pos = f"#{pa[k]}" if k in pa else "fuera del ranking"
            otras = [o for o in vivos_por_id.get(m.get("id"), []) if o["key"] != k]
            alt = f"✅ {max(otras, key=lambda x: x.get('runs') or 0)['name']}" if otras else "—"
            L += [f"| **{m['name']}** | {pos} | {m.get('runs', 0)} | "
                  f"{m.get('retired_reason') or '—'} | {alt} |"]
        L += [""]

    # ── 2. Cambió el precio ──────────────────────────────────────────────────
    precios = []
    for k in set(a) & set(b):
        for campo in ("cost_input_per_M", "cost_output_per_M"):
            va, vb = a[k].get(campo), b[k].get(campo)
            if va and vb and abs(vb - va) / va >= UMBRAL_PRECIO_REL:
                precios.append(k)
                break
    if precios:
        L += ["### 💰 Cambió el precio", "",
              "El costo pesa 15% del score, así que esto **sí mueve el orden**.", "",
              "| Modelo | Antes | Ahora | Factor |", "|---|---|---|---|"]
        for k in sorted(precios, key=lambda x: pb.get(x, 999)):
            va, vb = a[k].get("cost_output_per_M") or 0, b[k].get("cost_output_per_M") or 0
            factor = (f"**{va / vb:.1f}× más barato**" if vb and va > vb else
                      f"{vb / va:.1f}× más caro" if va and vb > va else "—")
            L += [f"| {b[k]['name']} | {_fmt_precio(a[k])} | {_fmt_precio(b[k])} | {factor} |"]
        L += [""]

    # ── 3. Se movieron de puesto ─────────────────────────────────────────────
    # 1-sep-2026 · sólo entra quien CAMBIÓ SU NOTA, no quien cambió de puesto.
    #
    # Antes bastaba con moverse 3 lugares, y eso llenaba la sección de ruido: al entrar
    # tres modelos nuevos arriba, cuarenta bajaron un escalón con «(+0.00)» al lado. Un
    # lector ve cuarenta filas y cree que pasó algo; lo único que pasó es que la lista es
    # más larga. El puesto es relativo a quién más hay; la nota es del modelo.
    movs = []
    for k in set(pa) & set(pb):
        d = (b[k].get("quality_avg") or 0) - (a[k].get("quality_avg") or 0)
        if abs(d) >= umbral:
            movs.append((k, d))
    if movs:
        L += ["### 📊 Se movieron en el ranking", "",
              "| Modelo | Puesto | Score |", "|---|---|---|"]
        for k, d in sorted(movs, key=lambda t: pb[t[0]]):
            flecha = "↑" if pb[k] < pa[k] else "↓" if pb[k] > pa[k] else "="
            L += [f"| {b[k]['name']} | #{pa[k]} → **#{pb[k]}** {flecha} | "
                  f"{a[k].get('quality_avg'):.2f} → {b[k].get('quality_avg'):.2f} ({d:+.2f}) |"]
        L += [""]

    # ── 4. Entraron ──────────────────────────────────────────────────────────
    nuevos = [k for k in b if k not in a]
    if nuevos:
        L += ["### 🆕 Modelos nuevos", "",
              "| Modelo | Precio $/M | Runs | Estado |", "|---|---|---:|---|"]
        for k in sorted(nuevos, key=lambda x: -(b[x].get("quality_avg") or -1)):
            m = b[k]
            estado = (f"**#{pb[k]} del ranking**, calidad {m['quality_avg']:.2f}" if k in pb
                      else f"en evaluación ({m.get('runs', 0)} runs, piso 50)" if m.get("tested")
                      else "sin medir todavía")
            L += [f"| **{m['name']}** | {_fmt_precio(m)} | {m.get('runs', 0)} | {estado} |"]
        L += [""]

    # ── 5. Resucitaron ───────────────────────────────────────────────────────
    revividos = [k for k in set(a) & set(b) if a[k].get("retired") and not b[k].get("retired")]
    if revividos:
        L += ["### 🔄 Volvieron", "",
              "Estaban retirados y un proveedor los volvió a servir. El retiro no es "
              "definitivo: se re-verifica con `check_endpoints.py --recheck-retired`.", ""]
        L += [f"- **{b[k]['name']}** — retirado el {a[k].get('retired_at') or '?'}, "
              f"hoy responde ({b[k].get('runs', 0)} runs históricos)" for k in revividos]
        L += [""]

    return L


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--desde", default=None, help="tag/commit inicial (default: último tag)")
    ap.add_argument("--hasta", default=None, help="tag/commit final (default: estado actual)")
    ap.add_argument("--umbral", type=float, default=UMBRAL_SCORE,
                    help=f"movimiento mínimo de score a reportar (default {UMBRAL_SCORE})")
    ap.add_argument("-o", "--output", default=None, help="escribir a un archivo en vez de stdout")
    args = ap.parse_args()

    desde = args.desde or ultimo_tag()
    a, b = snapshot(desde), snapshot(args.hasta)
    etiqueta_b = args.hasta or "estado actual"

    ra = sum(1 for m in a.values() if m.get("ranked"))
    rb = sum(1 for m in b.values() if m.get("ranked"))
    cab = [f"## Qué cambió: `{desde}` → `{etiqueta_b}`", "",
           f"> Catálogo {len(a)} → **{len(b)}** · rankeados {ra} → **{rb}** · "
           f"generado por `benchmarks/release_diff.py` desde `{MODELS_JSON_REL}`.", ""]

    cuerpo = construir(a, b, args.umbral)
    if not cuerpo:
        cuerpo = ["_Sin cambios que afecten una decisión entre estas dos versiones._", ""]
    texto = "\n".join(cab + cuerpo)

    if args.output:
        Path(args.output).write_text(texto)
        print(f"escrito → {args.output}")
    else:
        print(texto)
    return 0


if __name__ == "__main__":
    sys.exit(main())
