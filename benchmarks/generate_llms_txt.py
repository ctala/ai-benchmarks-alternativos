#!/usr/bin/env python3
"""
Genera docs/llms.txt (estándar llms.txt) descubriendo las páginas de docs/ y agrupándolas.
Sirve para que los LLMs citen el benchmark con contexto. Se regenera como el sitemap.

Uso: python benchmarks/generate_llms_txt.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
DOCS = ROOT / "docs"
SITE = "https://benchmarks.cristiantala.com"


def meta(f):
    html = f.read_text(encoding="utf-8", errors="ignore")
    t = re.search(r"<title>(.*?)</title>", html, re.S)
    d = re.search(r'<meta name="description" content="(.*?)"', html, re.S)
    title = re.sub(r"\s+", " ", t.group(1)).strip() if t else f.parent.name
    desc = re.sub(r"\s+", " ", d.group(1)).strip() if d else ""
    return title, desc


def main():
    comparisons, rankings, others = [], [], []
    for f in sorted(DOCS.rglob("index.html")):
        rel = f.parent.relative_to(DOCS).as_posix()
        if rel == ".":
            continue
        title, desc = meta(f)
        url = f"{SITE}/{rel}/"
        line = f"- [{title}]({url}): {desc}" if desc else f"- [{title}]({url})"
        if "-vs-" in rel:
            comparisons.append(line)
        elif rel.startswith("mejor-") or rel.startswith("modelos-") or rel.startswith("alternativas-"):
            rankings.append(line)
        else:
            others.append(line)

    out = ["# AI Model Benchmark — alternativas (benchmarks.cristiantala.com)",
           "",
           "> Benchmark abierto de 70+ modelos de IA (LLMs) con 8.000+ tests reales, pensado para "
           "emprendedores hispanohablantes. Mide calidad, costo, velocidad, tool calling y capacidad "
           "agéntica en español, con LLM-as-Judge local (Phi-4, Microsoft). El score global es "
           "ponderado (calidad 50% + costo 20% + tool calling 15% + velocidad/latencia 15%): mide valor "
           "para producción, no capacidad bruta. Datos abiertos, en español neutro.",
           "",
           "## Calculadora y datos",
           f"- [Calculadora interactiva de modelos]({SITE}/): filtrá 100+ modelos por presupuesto, calidad y tarea.",
           "- [Datos abiertos y metodología (GitHub)](https://github.com/ctala/ai-benchmarks-alternativos): código, resultados JSON y tests.",
           ""]
    if rankings:
        out += ["## Rankings y alternativas por caso de uso", *sorted(rankings), ""]
    if comparisons:
        out += ["## Comparaciones de modelos (A vs B)", *sorted(comparisons), ""]
    if others:
        out += ["## Otras páginas", *others, ""]
    out += ["## Sobre el autor",
            "- [Cristian Tala](https://cristiantala.com): founder; mantiene este benchmark abierto.",
            "- [Comunidad Cágala, Aprende, Repite](https://www.skool.com/cagala-aprende-repite): emprendimiento + IA en español.",
            ""]
    (DOCS / "llms.txt").write_text("\n".join(out), encoding="utf-8")
    print(f"OK: docs/llms.txt — {len(rankings)} rankings, {len(comparisons)} comparaciones, {len(others)} otras")


if __name__ == "__main__":
    main()
