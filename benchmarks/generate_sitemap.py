#!/usr/bin/env python3
"""
Genera docs/sitemap.xml automaticamente.

Lista:
1. Todos los index.html bajo docs/ (calculadora + landing pages)
2. MDs criticos del repo en GitHub (README, MODELOS, TESTS, AGENTS, etc.)

Para cada URL, lastmod es la fecha del ultimo commit que toco el archivo (`git log`), y
hoy si el archivo tiene cambios sin commitear o no esta versionado. Nunca el mtime.

Por que (3-nov-2026, corte-v5 2.6): con mtime, el Action fechaba con el dia de la
corrida paginas que no cambiaban desde agosto, porque `actions/checkout` escribe todos
los archivos al clonar. Cada corrida movia un `lastmod` y el local lo devolvia: la
ficha de `or-qwen3-next-thinking` iba y volvia entre 2026-08-20 y el dia del Action
(commit 5ffb51406). La fecha del commit es la misma en cualquier clon completo; en un
clon superficial seria falsa, y por eso el script se niega a correr ahi.

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
from datetime import date
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


def _git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True,
                          check=True).stdout


def fechas_git(raiz: Path = DOCS) -> dict[str, str]:
    """ruta relativa al repo → fecha (AAAA-MM-DD) del ultimo commit que la toco.

    Una sola pasada por el log en vez de un `git log` por pagina (son ~190). `%cs` es la
    fecha del committer en su propia zona: no depende de la maquina que regenera.
    """
    if _git("rev-parse", "--is-shallow-repository").strip() == "true":
        raise SystemExit("generate_sitemap: clon superficial; el lastmod saldria falso. "
                         "En el Action, checkout con fetch-depth: 0.")
    rel = raiz.relative_to(ROOT).as_posix()
    fechas, actual = {}, None
    for linea in _git("log", "--format=\x01%cs", "--name-only", "--", rel).splitlines():
        if linea.startswith("\x01"):
            actual = linea[1:]
        elif linea and linea not in fechas:
            fechas[linea] = actual
    return fechas


def sin_commitear(raiz: Path = DOCS) -> set[str]:
    """Rutas con cambios respecto de HEAD o sin versionar: su lastmod es hoy."""
    rel = raiz.relative_to(ROOT).as_posix()
    salida = _git("status", "--porcelain", "--untracked-files=all", "--", rel)
    return {ln[3:].split(" -> ")[-1] for ln in salida.splitlines() if ln.strip()}


def file_lastmod(path: Path, fechas: dict[str, str], sucias: set[str]) -> str:
    rel = path.relative_to(ROOT).as_posix()
    if rel in sucias or rel not in fechas:
        return date.today().isoformat()
    return fechas[rel]


def docs_pages():
    """(url, archivo, priority) de cada DESTINO del registro de páginas.

    11-nov-2026 (motor-sitio 2.3): antes recorría los `index.html` de docs/, con una lista a
    mano de exclusiones. Así entraban al sitemap páginas que el registro ya declara redirect:
    19, entre ellas `/fable-5-vs-deepseek-r1/`, que en vivo ya es un meta refresh. Un sitemap
    que lista redirects le pide a Google indexar lo que la página misma marca `noindex`. Ahora
    la lista sale del registro y solo lleva destinos; el archivo se usa para la fecha.
    """
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import registro_paginas as rp
    pages = []
    for e in sorted(rp.paginas(), key=lambda e: e["url"]):
        if e["redirect_a"]:
            continue
        url = e["url"]
        f = DOCS / "index.html" if url == "/" else DOCS / url.strip("/") / "index.html"
        if url == "/":
            priority = PRIORITY_OVERRIDES.get("/", 1.0)
        elif url.startswith(("/alternativas-", "/modelos-")):
            priority = 0.9
        else:
            priority = 0.7
        pages.append((f"{SITE_BASE}{url}", f, priority))
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
    fechas, sucias = fechas_git(), sin_commitear()

    for url, path, priority in entries:
        lastmod = file_lastmod(path, fechas, sucias)
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
