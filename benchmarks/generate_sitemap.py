#!/usr/bin/env python3
"""
Genera docs/sitemap.xml automaticamente.

Lista:
1. Todos los index.html bajo docs/ (calculadora + landing pages)
2. MDs criticos del repo en GitHub (README, MODELOS, TESTS, AGENTS, etc.)

Para cada URL toma lastmod de la ultima modificacion del archivo (mtime): tras
regenerar, las paginas reescritas quedan con la fecha de regeneracion (hoy), una
senal de frescura honesta y coherente con dateModified del JSON-LD. Las paginas
que no se regeneran conservan su fecha real. Fallback: hoy.

Uso:
    python benchmarks/generate_sitemap.py        # genera docs/sitemap.xml

Pesos por defecto (ajustables en PRIORITY_OVERRIDES):
- / -> 1.0 (calculadora)
- /alternativas-* y /modelos-* -> 0.9 (landing pages SEO core)
- otros bajo /docs -> 0.7
- READMEs y guias del repo (AGENTS, RECOMENDACIONES) -> 0.8
- MODELOS, TESTS, DESCUBRIMIENTOS -> 0.7
- CHANGELOG -> 0.5
"""

from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).parent.parent
DOCS = ROOT / "docs"
SITE_BASE = "https://benchmarks.cristiantala.com"
GH_BASE = "https://github.com/ctala/ai-benchmarks-alternativos/blob/main"

# MDs del repo que vale la pena indexar (con prioridad SEO)
REPO_MDS = [
    ("README.md", 0.9),
    ("AGENTS.md", 0.8),
    ("INSIGHTS.md", 0.8),
    ("ARQUITECTURA.md", 0.7),
    ("RECOMENDACIONES.md", 0.8),
    ("MODELOS.md", 0.7),
    ("TESTS.md", 0.7),
    ("DESCUBRIMIENTOS.md", 0.6),
    ("CHANGELOG.md", 0.5),
]

# Carpetas con MDs que se descubren automaticamente (cualquier *.md)
REPO_MD_DIRS = [
    ("tutoriales", 0.7),
]

PRIORITY_OVERRIDES = {
    "/": 1.0,
}


def file_lastmod(path: Path) -> str:
    """Fecha (YYYY-MM-DD, hora local) de la ultima escritura del archivo. Tras regenerar,
    las paginas reescritas quedan con la fecha de regeneracion (hoy) -> coherente con el
    dateModified del JSON-LD. Se usa hora local (naive) para alinear con date.today().
    Fallback: hoy."""
    try:
        return datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m-%d")
    except OSError:
        return datetime.now(timezone.utc).strftime("%Y-%m-%d")


# Paginas que NO van al sitemap: son redirects/noindex, no contenido.
# grok-4.3-vs-gpt-5.5 (con punto) es un huerfano de una version vieja del
# generador — el slug vivo es "-5-5". Las dos servian el MISMO contenido con
# canonical self-referencial: duplicado puro. La de punto quedo como redirect.
SITEMAP_EXCLUDE = {"grok-4.3-vs-gpt-5.5"}


def docs_pages():
    """Itera sobre todos los index.html bajo docs/, devuelve (url, file_path, priority)."""
    pages = []
    for f in sorted(DOCS.rglob("index.html")):
        rel_dir = f.parent.relative_to(DOCS).as_posix()
        if rel_dir in SITEMAP_EXCLUDE:
            continue
        if rel_dir == ".":
            url = f"{SITE_BASE}/"
            priority = PRIORITY_OVERRIDES.get("/", 1.0)
        else:
            url = f"{SITE_BASE}/{rel_dir}/"
            # Landing pages priority
            if rel_dir.startswith("alternativas-") or rel_dir.startswith("modelos-"):
                priority = 0.9
            else:
                priority = 0.7
        pages.append((url, f, priority))
    return pages


def repo_mds():
    """Lista de MDs en root del repo con sus paths absolutos y priority."""
    out = []
    for name, priority in REPO_MDS:
        path = ROOT / name
        if path.exists():
            url = f"{GH_BASE}/{name}"
            out.append((url, path, priority))
    # Carpetas con MDs descubiertos automaticamente
    for dirname, priority in REPO_MD_DIRS:
        d = ROOT / dirname
        if not d.exists():
            continue
        for path in sorted(d.glob("*.md")):
            rel = path.relative_to(ROOT).as_posix()
            url = f"{GH_BASE}/{rel}"
            out.append((url, path, priority))
    return out


def build_sitemap() -> str:
    lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    # IMPORTANTE: un sitemap.xml solo puede listar URLs del PROPIO dominio.
    # Las URLs github.com/.../blob/... las rechaza Google Search Console
    # ("URL no permitida — no se puede enviar esta URL para un sitemap"), porque
    # benchmarks.cristiantala.com no es dueño de github.com. Los .md del repo se
    # descubren por sus enlaces desde las páginas del dominio, NO desde este sitemap.
    # (repo_mds() se conserva por si en el futuro se publica un sitemap aparte para GitHub.)
    entries = docs_pages()

    for url, path, priority in entries:
        lastmod = file_lastmod(path)
        lines.append("  <url>")
        lines.append(f"    <loc>{escape(url)}</loc>")
        lines.append(f"    <lastmod>{lastmod}</lastmod>")
        lines.append("    <changefreq>weekly</changefreq>")
        lines.append(f"    <priority>{priority}</priority>")
        lines.append("  </url>")

    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


def main():
    out = DOCS / "sitemap.xml"
    content = build_sitemap()
    out.write_text(content, encoding="utf-8")

    # Contar URLs para reporte
    n = content.count("<url>")
    print(f"OK: docs/sitemap.xml con {n} URLs (docs/ landing pages + MDs del repo)")


if __name__ == "__main__":
    main()
