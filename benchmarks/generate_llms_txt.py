#!/usr/bin/env python3
"""
Genera sitio/legado/llms.txt (estándar llms.txt) descubriendo las páginas de sitio/legado/ y agrupándolas.
Sirve para que los LLMs citen el benchmark con contexto. Se regenera como el sitemap.

Uso: python benchmarks/generate_llms_txt.py
"""
import json, re
from pathlib import Path

ROOT = Path(__file__).parent.parent
DOCS = ROOT / "sitio" / "legado"
MODELS_JSON = DOCS / "data" / "models.json"
SITE = "https://benchmarks.cristiantala.com"


def meta(f):
    html = f.read_text(encoding="utf-8", errors="ignore")
    t = re.search(r"<title>(.*?)</title>", html, re.S)
    d = re.search(r'<meta name="description" content="(.*?)"', html, re.S)
    title = re.sub(r"\s+", " ", t.group(1)).strip() if t else f.parent.name
    desc = re.sub(r"\s+", " ", d.group(1)).strip() if d else ""
    return title, desc


def _fmt_pct(w):
    p = w * 100
    return f"{int(p)}" if p == int(p) else f"{p:.1f}".replace(".", ",")


def main():
    # 11-nov-2026 (motor-sitio 2.3): las páginas salen del registro y solo los destinos. Antes
    # recorría sitio/legado/ y listaba 20 URLs que el registro declara redirect.
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import registro_paginas as rp
    comparisons, rankings, others = [], [], []
    for e in sorted(rp.paginas(), key=lambda e: e["url"]):
        if not e["indexable"] or e["url"] == "/":  # 12-nov-2026: ni redirects ni noindex (fichas)
            continue
        rel = e["url"].strip("/")
        f = DOCS / rel / "index.html"
        title, desc = meta(f)
        url = f"{SITE}/{rel}/"
        line = f"- [{title}]({url}): {desc}" if desc else f"- [{title}]({url})"
        if "-vs-" in rel:
            comparisons.append(line)
        elif rel.startswith("mejor-") or rel.startswith("modelos-") or rel.startswith("alternativas-"):
            rankings.append(line)
        else:
            others.append(line)

    data = json.loads(MODELS_JSON.read_text(encoding="utf-8"))
    total_models = data.get("total_models", 0)
    tested_count = data.get("tested_count", 0)
    # "runs reales" — la cuenta vive en conteos.ejecuciones (16-sep-2026): antes cada
    # generador la repetía con su propio fallback y podían dar números distintos.
    try:
        from benchmarks.conteos import ejecuciones
    except ImportError:  # corrido como script desde benchmarks/
        from conteos import ejecuciones
    total_runs = ejecuciones(data)
    runs_k = f"{(total_runs // 1000) * 1000:,}".replace(",", ".")
    w = data.get("default_weights", {})
    q = _fmt_pct(w.get("quality", 0.7))
    co = _fmt_pct(w.get("cost", 0.15))
    sp = _fmt_pct(w.get("speed", 0.075))
    la = _fmt_pct(w.get("latency", 0.075))
    tc = w.get("tool_calling", 0)
    tc_text = "no entra en el score global" if tc == 0 else f"{_fmt_pct(tc)}% del score"

    out = ["# AI Model Benchmark — alternativas (benchmarks.cristiantala.com)",
           "",
           f"> Benchmark abierto de {total_models} modelos de IA (LLMs) catalogados, {tested_count} "
           f"testeados y {runs_k}+ runs reales, pensado para emprendedores hispanohablantes. "
           "Mide calidad, costo, velocidad, tool calling y capacidad agéntica en español, con "
           f"LLM-as-Judge (Phi-4, de Microsoft, vía OpenRouter). El score global {data.get('scoring_version', 'v4.0')} es ponderado (calidad {q}% + "
           f"costo {co}% + velocidad {sp}% + latencia {la}%); tool calling es insignia aparte "
           f"({tc_text}): mide valor para producción, no capacidad bruta. Datos abiertos, en español neutro.",
           "",
           "## Calculadora y datos",
           f"- [Calculadora interactiva de modelos]({SITE}/): filtra 100+ modelos por presupuesto, calidad y tarea.",
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
            "- [Comunidad Cágala, Aprende, Repite](https://go.aprenderepite.com/benchmark): emprendimiento + IA en español.",
            ""]
    (DOCS / "llms.txt").write_text("\n".join(out), encoding="utf-8")
    print(f"OK: sitio/legado/llms.txt — {len(rankings)} rankings, {len(comparisons)} comparaciones, {len(others)} otras")


if __name__ == "__main__":
    main()
