#!/usr/bin/env python3
"""Regenera las tablas del pilar del blog desde `docs/data/models.json`.

POR QUÉ EXISTE (16-sep-2026)
----------------------------
El pilar (`benchmark-de-modelos-de-ia-2026-...`) es la página VIVA del benchmark, y sus dos
tablas se mantenían a mano. El 15-sep hubo que verificar ~40 cifras una por una, y la que
estaba mal —«Tencent Hy3 es #1 del ranking global entero»— llevaba semanas publicada: dejó
de ser cierta cuando entraron modelos nuevos, y nada lo dijo.

La regla del repo es la misma de siempre: **lo que se genera no se verifica, se regenera.**
El README ya lo hace con su ranking (`generate_readme_ranking.py`); esto es lo mismo para
el post. La prosa sigue a cargo de `check_blog_consistency.py`, que caza las cifras sueltas.

NO lo corre `regenerate_all.py` a propósito: el blog es otro repo y otras sesiones empujan
su `main`. Un generador que escribe ahí en silencio publica sin que nadie lo revise — que
es exactamente lo que pasó el 15-sep. Se corre a mano, y el hook de pre-push del blog usa
`--check` para que el post no pueda quedar desfasado sin que nadie se entere.

Uso:
    python benchmarks/generate_blog_tablas.py             # escribe las tablas en el post
    python benchmarks/generate_blog_tablas.py --check     # exit 1 si el post no coincide
    python benchmarks/generate_blog_tablas.py --blog /ruta/al/blog
"""

import argparse
import json
import re
import sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODELS_JSON = ROOT / "docs" / "data" / "models.json"
DEFAULT_BLOG = Path.home() / "Playground" / "sitios" / "cristiantala-blog"
POST = ("src/content/blog/"
        "benchmark-de-modelos-de-ia-2026-probe-25-modelos-con-125-tests-reales.md")

BLOQUES = {
    "TOP10": {
        "cabecera": "| # | Modelo | Calidad | $/1k llamadas | Open source |",
        "columnas": "| --- | --- | --- | --- | --- |",
        "negritas": 3,   # el podio va en negrita, como se publicó siempre
    },
    "OPENSOURCE": {
        "cabecera": "| # | Modelo | Calidad | $/1k llamadas | Licencia |",
        "columnas": "| --- | --- | --- | --- | --- |",
        "negritas": 2,
    },
}


def usd(x) -> str:
    """$7.02, $0.80, $39.00 — media vuelta arriba, como se leen los precios."""
    if x is None:
        return "—"
    return "$" + str(Decimal(str(x)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def rankeados(data: dict) -> list[dict]:
    """Por índice de calidad, que es el titular desde v4.1 — no por el compuesto."""
    return sorted([m for m in data["models"] if m.get("ranked")],
                  key=lambda m: -(m.get("quality_avg") or 0))


def _fila(i: int, m: dict, ultima_col: str, negrita: bool) -> str:
    celdas = [m["name"], f"{m['quality_avg']:.2f}", usd(m.get("cost_per_1k_calls_usd")),
              ultima_col]
    if negrita:
        celdas = [f"**{c}**" for c in celdas]
    return "| " + " | ".join([str(i)] + celdas) + " |"


def tabla(nombre: str, data: dict) -> str:
    cfg = BLOQUES[nombre]
    ms = rankeados(data)
    if nombre == "OPENSOURCE":
        ms = [m for m in ms if m.get("open_source")][:10]
        ultima = [m.get("license") or "Abierta" for m in ms]
    else:
        ms = ms[:10]
        ultima = ["Sí" if m.get("open_source") else "No" for m in ms]
    filas = [_fila(i, m, u, i <= cfg["negritas"])
             for i, (m, u) in enumerate(zip(ms, ultima), 1)]
    return "\n".join([f"<!-- AUTO-{nombre}-START -->", cfg["cabecera"], cfg["columnas"],
                      *filas, f"<!-- AUTO-{nombre}-END -->"])


def aplicar(texto: str, data: dict) -> tuple[str, list[str]]:
    """Devuelve (texto nuevo, bloques que cambiaron). Falta un marcador → error ruidoso."""
    cambiados = []
    for nombre in BLOQUES:
        ini, fin = f"<!-- AUTO-{nombre}-START -->", f"<!-- AUTO-{nombre}-END -->"
        if ini not in texto or fin not in texto:
            raise SystemExit(
                f"ERROR: no encontré los marcadores {ini} / {fin} en el post.\n"
                "Envolvé la tabla con ellos para que este script la mantenga.")
        nuevo = tabla(nombre, data)
        anterior = re.search(rf"{re.escape(ini)}.*?{re.escape(fin)}", texto, re.DOTALL).group()
        if anterior != nuevo:
            cambiados.append(nombre)
            texto = texto.replace(anterior, nuevo)
    return texto, cambiados


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--blog", default=str(DEFAULT_BLOG))
    ap.add_argument("--check", action="store_true",
                    help="no escribe: exit 1 si el post no refleja los datos de hoy")
    args = ap.parse_args()

    post = Path(args.blog) / POST
    if not post.exists():
        # El blog es otro repo y puede no estar clonado (CI). Sin él no hay nada que
        # verificar, y fallar por eso sería un rojo que no dice nada sobre los datos.
        print(f"  ⏭️  sin el repo del blog en {args.blog}: nada que verificar")
        return 0
    if not MODELS_JSON.exists():
        sys.exit("Falta docs/data/models.json — corré export_for_pages.py primero")

    data = json.loads(MODELS_JSON.read_text())
    texto = post.read_text()
    nuevo, cambiados = aplicar(texto, data)

    if not cambiados:
        print(f"  ✅ las tablas del pilar coinciden con models.json "
              f"({data['ranked_count']} rankeados)")
        return 0
    if args.check:
        print(f"  ❌ el pilar no refleja los datos de hoy: {', '.join(cambiados)}")
        print("     Corré `python benchmarks/generate_blog_tablas.py` y revisá el diff "
              "(la prosa alrededor puede citar cifras que también hay que mover).")
        return 1
    post.write_text(nuevo)
    print(f"  ✓ {post.name}: {', '.join(cambiados)} regenerado(s)")
    print("     Ojo: la prosa NO se regenera. Corré check_blog_consistency.py antes de publicar.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
