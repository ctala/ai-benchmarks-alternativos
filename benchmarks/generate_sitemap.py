#!/usr/bin/env python3
"""
Genera docs/sitemap.xml automaticamente.

Lista:
1. Todos los index.html bajo docs/ (calculadora + landing pages)
2. MDs criticos del repo en GitHub (README, MODELOS, TESTS, AGENTS, etc.)

Para cada URL toma lastmod del ultimo commit git que toco el archivo
(fallback: fecha actual si el archivo no esta versionado todavia).

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

import subprocess
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
    ("RECOMENDACIONES.md", 0.8),
    ("MODELOS.md", 0.7),
    ("TESTS.md", 0.7),
    ("DESCUBRIMIENTOS.md", 0.6),
    ("CHANGELOG.md", 0.5),
]

PRIORITY_OVERRIDES = {
    "/": 1.0,
}


def git_lastmod(path: Path) -> str:
    """Devuelve fecha YYYY-MM-DD del ultimo commit que toco el archivo. Fallback: hoy."""
    try:
        out = subprocess.check_output(
            ["git", "log", "-1", "--format=%cs", "--", str(path)],
            cwd=ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
        if out:
            return out
    except subprocess.CalledProcessError:
        pass
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def docs_pages():
    """Itera sobre todos los index.html bajo docs/, devuelve (url, file_path, priority)."""
    pages = []
    for f in sorted(DOCS.rglob("index.html")):
        rel_dir = f.parent.relative_to(DOCS).as_posix()
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
    return out


def build_sitemap() -> str:
    lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    entries = docs_pages() + repo_mds()
    # Repo URL como entrada propia (no es archivo, lastmod del README)
    readme_lastmod = git_lastmod(ROOT / "README.md")
    repo_url_entry = ("https://github.com/ctala/ai-benchmarks-alternativos", None, 0.9, readme_lastmod)

    # Render docs + mds
    for url, path, priority in entries:
        lastmod = git_lastmod(path)
        lines.append("  <url>")
        lines.append(f"    <loc>{escape(url)}</loc>")
        lines.append(f"    <lastmod>{lastmod}</lastmod>")
        lines.append("    <changefreq>weekly</changefreq>")
        lines.append(f"    <priority>{priority}</priority>")
        lines.append("  </url>")

    # Repo root al final
    url, _, priority, lastmod = repo_url_entry
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
