#!/usr/bin/env python3
"""
Genera páginas pSEO de comparación "[Familia A] vs [Familia B]" en docs/<slug>/index.html
a partir de docs/data/models.json (data real del benchmark). HTML estático server-rendered
— mismo patrón que las landing actuales (no toca la calculadora ni usa app.js).

Es paso opcional del pipeline (ver CLAUDE.md). El generate_sitemap.py descubre las páginas
nuevas automáticamente (rglob index.html).

Uso:
    python benchmarks/generate_comparison.py            # genera todas las COMPARISONS de abajo
    python benchmarks/generate_comparison.py --slug gemini-vs-chatgpt   # solo una

Para agregar una comparación: añadir un dict a COMPARISONS. Cero HTML a mano.
"""
import argparse, json, html
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent.parent
DOCS = ROOT / "docs"
MODELS_JSON = DOCS / "data" / "models.json"
SITE = "https://benchmarks.cristiantala.com"
LOGO = "https://assets.nyx.cristiantala.com/2026/images/logo-cristian-tala-sanchez-2026.png"
LOGO_DARK = "https://assets.nyx.cristiantala.com/2026/images/logo-cristian-tala-sanchez-dark-2026.png"
PILLARS = ["Coding", "Contenido", "Razonamiento", "Agentes"]
# Qué mide cada pilar (para el V/S por tipo de trabajo) — descripciones del README
PILLAR_DESC = {
    "Coding": ("Coding", "generar código, JSON estructurado y debugging en tareas reales "
               "(plugins WordPress, scripts, templates de N8N)", "lo que hacés"),
    "Contenido": ("Contenido y marketing", "blogs, copy y textos largos en español neutro "
                  "(no traducción del inglés)", "lo que escribís"),
    "Razonamiento": ("Razonamiento", "matemáticas, lógica formal y planificación multi-paso", "cómo decide"),
    "Agentes": ("Agentes y operaciones", "multi-turno largo, tool calling y flujos tipo N8N / OpenClaw", "cómo opera"),
}

# --- Comparaciones a generar (cada una = una página pSEO) ---------------------
GPT = {"name": "ChatGPT (GPT)", "match": ["gpt-", "gpt5", "gpt-5", "chatgpt"], "exclude": ["oss"]}
COMPARISONS = [
    {
        "slug": "gemini-vs-chatgpt",
        "a": {"name": "Gemini", "match": ["gemini"]}, "b": GPT,
        "title": "Gemini vs ChatGPT en 2026: comparación con benchmark real",
        "intent_kw": "gemini vs chatgpt, comparativa gemini gpt, gemini o chatgpt, mejor ia google openai",
    },
    {
        "slug": "claude-vs-chatgpt",
        "a": {"name": "Claude", "match": ["claude"]}, "b": GPT,
        "title": "Claude vs ChatGPT en 2026: comparación con benchmark real",
        "intent_kw": "claude vs chatgpt, claude o gpt, comparativa claude gpt, anthropic vs openai, claude vs gpt 5",
    },
    {
        "slug": "gemini-vs-claude",
        "a": {"name": "Gemini", "match": ["gemini"]}, "b": {"name": "Claude", "match": ["claude"]},
        "title": "Gemini vs Claude en 2026: comparación con benchmark real",
        "intent_kw": "gemini vs claude, claude o gemini, comparativa gemini claude, google vs anthropic",
    },
    {
        "slug": "deepseek-vs-chatgpt",
        "a": {"name": "DeepSeek", "match": ["deepseek"]}, "b": GPT,
        "title": "DeepSeek vs ChatGPT en 2026: comparación con benchmark real",
        "intent_kw": "deepseek vs chatgpt, deepseek vs gpt, deepseek o gpt, comparativa deepseek openai",
    },
    {
        "slug": "qwen-vs-llama",
        "a": {"name": "Qwen", "match": ["qwen"]}, "b": {"name": "Llama", "match": ["llama"]},
        "title": "Qwen vs Llama en 2026: comparación open source con benchmark real",
        "intent_kw": "qwen vs llama, llama vs qwen, mejor llm open source, comparativa qwen llama, modelos open source",
    },
]


def load_models():
    d = json.loads(MODELS_JSON.read_text())
    return d if isinstance(d, list) else (d.get("models") or list(d.values())[0])


def family(models, cfg):
    out = []
    for m in models:
        blob = f"{m.get('name','')} {m.get('id','')} {m.get('key','')}".lower()
        if not any(k in blob for k in cfg["match"]):
            continue
        if any(x in blob for x in cfg.get("exclude", [])):
            continue
        if (m.get("score_global") or 0) <= 0:
            continue
        # Requiere score por pilar: los variantes 'thinking' a veces traen score_global
        # pero no score_by_pillar → mostrarían 0.0 en la tabla. Sin pillars no entran a
        # una comparación por pilar (queda el variante hermano que sí los tiene).
        if sum((m.get("score_by_pillar") or {}).get(p) or 0 for p in PILLARS) <= 0:
            continue
        out.append(m)
    return sorted(out, key=lambda m: -(m.get("score_global") or 0))


def pillar(m, name):
    return (m.get("score_by_pillar") or {}).get(name) or 0


def fmt_cost(m):
    return f"${m.get('cost_input_per_M',0):.2f} / ${m.get('cost_output_per_M',0):.2f}"


def esc(s):
    return html.escape(str(s))


def pcell(m, p):
    """Celda de pilar: '—' si no se midió (0), en vez de un 0.0 que parece mala nota."""
    v = pillar(m, p)
    return f"{v:.1f}" if v > 0 else "—"


def row(rank, m, top=False):
    nm = f"<strong>{esc(m.get('name'))}</strong>" if top else esc(m.get("name"))
    return (f"<tr><td>{rank}</td><td>{nm}</td><td>{m.get('score_global',0):.2f}</td>"
            f"<td>{pcell(m,'Coding')}</td><td>{pcell(m,'Contenido')}</td>"
            f"<td>{pcell(m,'Razonamiento')}</td><td>{pcell(m,'Agentes')}</td>"
            f"<td>{fmt_cost(m)}</td><td>{round(m.get('tokens_per_second') or 0)} tok/s</td></tr>")


def best_in(arr, pil):
    return max(arr, key=lambda m: pillar(m, pil)) if arr else None


def methodology():
    """Sección fija: qué mide el benchmark (autoridad / E-E-A-T)."""
    items = "\n    ".join(
        f"<li><strong>{PILLAR_DESC[p][0]}</strong> — {PILLAR_DESC[p][1]}.</li>" for p in PILLARS)
    return f"""<section>
  <h2>¿Qué mide este benchmark?</h2>
  <p>No es un benchmark académico (para eso están MMLU, HumanEval o SWE-bench). Es un benchmark
  <strong>aplicado para emprendedores hispanohablantes</strong>: mide qué modelo conviene poner en
  producción para casos reales, con lo que los benchmarks oficiales no cubren — costo en provider real,
  velocidad, español neutro y agentes multi-turno.</p>
  <p>Cada modelo corre <strong>8.000+ tests reales</strong> evaluados por un
  <strong>LLM-as-Judge local (Phi-4, de Microsoft — sin conflicto de interés)</strong>, en 4 pilares:</p>
  <ul>
    {items}
  </ul>
  <p>El <strong>score global</strong> es una función ponderada: calidad 50% + costo 20% + tool calling 15%
  + velocidad 7,5% + latencia 7,5%. Por eso un modelo barato y rápido puede ganarle a uno "más inteligente"
  pero caro — porque mide <em>valor para producción</em>, no solo capacidad bruta.
  <a href="https://github.com/ctala/ai-benchmarks-alternativos/blob/main/TESTS.md" target="_blank" rel="noopener">Metodología y tests completos</a>.</p>
</section>"""


def analysis(a_name, b_name, A, B):
    """V/S real por tipo de trabajo (data-driven, cero invención: todo sale de los scores)."""
    a0, b0 = A[0], B[0]
    winner = a0 if a0["score_global"] >= b0["score_global"] else b0
    loser = b0 if winner is a0 else a0
    secs = [methodology()]
    secs.append(f"""<section>
  <h2>Veredicto rápido</h2>
  <p>En el cómputo global gana <strong>{esc(winner.get('name'))}</strong> ({winner['score_global']:.2f} vs
  {loser['score_global']:.2f} de {esc(loser.get('name'))}) — empujado por costo y velocidad. Pero
  <strong>no hay ganador universal</strong>: cambia por tipo de trabajo. El enfrentamiento real, abajo.</p>
</section>""")

    secs.append(f"<section>\n  <h2>{esc(a_name)} vs {esc(b_name)} por tipo de trabajo</h2>")
    verdict_rows = []
    for pil in PILLARS:
        label, what, _ = PILLAR_DESC[pil]
        ba, bb = best_in(A, pil), best_in(B, pil)
        if not ba or not bb:
            continue
        diff = pillar(ba, pil) - pillar(bb, pil)
        if abs(diff) < 0.1:  # empate técnico en CALIDAD — la prioridad del lector desempata, no nosotros
            cheaper = ba if (ba.get("cost_input_per_M") or 99) <= (bb.get("cost_input_per_M") or 99) else bb
            other = bb if cheaper is ba else ba
            win_name = f"Empate — {esc(ba.get('name'))} o {esc(bb.get('name'))}"
            body = (f"Empate técnico en calidad: <strong>{esc(ba.get('name'))}</strong> y <strong>{esc(bb.get('name'))}</strong> "
                    f"rinden casi igual (≈{max(pillar(ba,pil),pillar(bb,pil)):.1f}/10). Acá no decidimos por vos: "
                    f"si te importa el costo, <strong>{esc(cheaper.get('name'))}</strong> sale {fmt_cost(cheaper)} por millón; "
                    f"si ya tenés {esc(other.get('name'))} en tu stack, no hay razón para cambiar — la calidad es la misma.")
        else:
            w = ba if diff > 0 else bb
            l = bb if w is ba else ba
            margin = abs(diff)
            strength = "claramente" if margin >= 0.5 else "por poco"
            win_name = f"{esc(w.get('name'))} (por calidad)"
            body = (f"En calidad pura de este pilar gana <strong>{esc(w.get('name'))}</strong> {strength}: {pillar(w,pil):.1f}/10 "
                    f"contra {pillar(l,pil):.1f}/10 de {esc(l.get('name'))} (Δ {margin:.1f}). A {fmt_cost(w)} por millón. "
                    f"Si tu prioridad es costo o velocidad, el ganador puede cambiar — ajustalo en la calculadora.")
        secs.append(f"""  <h3>{label}: ¿{esc(a_name)} o {esc(b_name)}?</h3>
  <p><em>Qué medimos: {what}.</em><br>{body}</p>""")
        verdict_rows.append(f"<tr><td>{label}</td><td><strong>{win_name}</strong></td></tr>")
    secs.append("</section>")

    # cost / speed
    cheap = min(A + B, key=lambda m: (m.get("cost_input_per_M") or 99) + (m.get("cost_output_per_M") or 99))
    fast = max(A + B, key=lambda m: m.get("tokens_per_second") or 0)
    verdict_rows.append(f"<tr><td>Costo más bajo</td><td><strong>{esc(cheap.get('name'))}</strong> ({fmt_cost(cheap)})</td></tr>")
    verdict_rows.append(f"<tr><td>Más rápido</td><td><strong>{esc(fast.get('name'))}</strong> ({round(fast.get('tokens_per_second') or 0)} tok/s)</td></tr>")

    # tabla resumen "ganador por caso"
    secs.append(f"""<section class="results">
  <div class="results-header"><h2>Resumen: quién gana según tu caso</h2></div>
  <table class="results-table">
    <thead><tr><th>Tu caso</th><th>Ganador</th></tr></thead>
    <tbody>
      {"".join(verdict_rows)}
    </tbody>
  </table>
  <p class="meta">Este cuadro muestra el mejor por <strong>calidad de cada pilar</strong> — pero el "ganador" real depende de <strong>tu</strong> prioridad: calidad, costo o velocidad. No sabemos tu caso, así que ajustá esos pesos en la <a href="/">calculadora</a> y obtené el ganador para vos.</p>
</section>""")
    return "\n".join(secs)


def faq(a_name, b_name, A, B):
    a0, b0 = A[0], B[0]
    return f"""<section class="faq">
  <h2>Preguntas frecuentes</h2>
  <details><summary><strong>¿{esc(a_name)} o {esc(b_name)} es mejor en 2026?</strong></summary>
  <p>Depende de la tarea. En el cómputo global de nuestro benchmark gana {esc((a0 if a0['score_global']>=b0['score_global'] else b0).get('name'))},
  pero el mejor por pilar cambia (ver arriba). La pregunta correcta es "mejor para qué caso".</p></details>
  <details><summary><strong>¿Estos datos de dónde salen?</strong></summary>
  <p>De un benchmark abierto con 8.000+ tests reales y LLM-as-Judge local (Phi-4, Microsoft, sin conflicto de interés).
  Código y resultados en <a href="https://github.com/ctala/ai-benchmarks-alternativos" target="_blank" rel="noopener">GitHub</a>.</p></details>
  <details><summary><strong>¿Cuál es más barato para agentes con volumen?</strong></summary>
  <p>Mirá la columna de costo en la tabla. Para 1.000+ calls/mes, el costo por millón de tokens domina el ROI por encima de
  diferencias chicas de calidad. Filtralo por tu presupuesto en la <a href="/">calculadora</a>.</p></details>
</section>"""


def render(cfg, A, B):
    a_name, b_name = cfg["a"]["name"], cfg["b"]["name"]
    today = date.today().isoformat()
    title = cfg["title"]
    desc = (f"{a_name} vs {b_name} comparados con 8.000+ tests reales: coding, contenido en español, "
            f"razonamiento, agentes, costo y velocidad. Benchmark abierto, datos en español.")
    url = f"{SITE}/{cfg['slug']}/"
    rows = "\n        ".join(row(i + 1, m, top=(i == 0)) for i, m in enumerate(A[:5] + B[:5]))
    jsonld = json.dumps({
        "@context": "https://schema.org", "@type": "Article", "headline": title,
        "description": desc, "author": {"@type": "Person", "name": "Cristian Tala", "url": "https://cristiantala.com"},
        "datePublished": today, "dateModified": today, "inLanguage": "es",
        "url": url, "mainEntityOfPage": url,
        "publisher": {"@type": "Person", "name": "Cristian Tala", "url": "https://cristiantala.com"},
    }, ensure_ascii=False, indent=2)
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="keywords" content="{esc(cfg['intent_kw'])}">
<meta name="author" content="Cristian Tala">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="article">
<meta property="og:locale" content="es_CL">
<meta property="og:image" content="{LOGO}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="{LOGO}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../style.css">
<script type="application/ld+json">
{jsonld}
</script>
</head>
<body>
<header>
  <div class="container header-inner">
    <a href="https://cristiantala.com" class="logo-link" target="_blank" rel="noopener">
      <img src="{LOGO_DARK}" alt="Cristian Tala" class="logo">
    </a>
    <nav>
      <a href="/">Calculadora</a>
      <a href="https://github.com/ctala/ai-benchmarks-alternativos" target="_blank" rel="noopener">Repo</a>
      <a href="https://www.skool.com/cagala-aprende-repite" target="_blank" rel="noopener" class="cta-mini">Comunidad</a>
    </nav>
  </div>
</header>
<main class="container">
  <section class="hero">
    <h1>{esc(a_name)} vs {esc(b_name)}: cuál elegir en 2026 (benchmark real)</h1>
    <p class="lead">Comparamos las familias <strong>{esc(a_name)}</strong> y <strong>{esc(b_name)}</strong> con datos, no opiniones:
    <strong>8.000+ tests reales</strong> evaluados con LLM-as-Judge Phi-4 local, en los 4 pilares del emprendedor
    (coding, contenido, razonamiento, agentes) + costo y velocidad reales.</p>
    <p class="meta">Última actualización: {today} ·
    <a href="https://github.com/ctala/ai-benchmarks-alternativos" target="_blank" rel="noopener">datos abiertos en GitHub</a></p>
  </section>
  <section class="results">
    <div class="results-header">
      <h2>{esc(a_name)} vs {esc(b_name)}: tabla comparativa</h2>
      <p class="meta">Score por pilar /10. Ordenado por score global ponderado.</p>
    </div>
    <table class="results-table">
      <thead>
        <tr><th>#</th><th>Modelo</th><th>Global</th><th>Coding</th><th>Contenido</th><th>Razon.</th><th>Agentes</th><th>$ in/out per M</th><th>Velocidad</th></tr>
      </thead>
      <tbody>
        {rows}
      </tbody>
    </table>
    <p class="meta">Filtrá por presupuesto, calidad mínima o tarea en la <a href="/">calculadora interactiva</a>.</p>
  </section>
  {analysis(a_name, b_name, A, B)}
  {faq(a_name, b_name, A, B)}
  <section class="cta-block">
    <h2>Probá la calculadora con tu caso real</h2>
    <p>Filtrá {esc(a_name)}, {esc(b_name)} y 100+ modelos más por presupuesto, calidad y tipo de tarea. En 30 segundos encontrás el mejor para vos.</p>
    <a href="/" class="cta-primary">Ir a la calculadora →</a>
  </section>
</main>
<footer>
  <div class="container">
    <p>Hecho por <a href="https://cristiantala.com" target="_blank" rel="noopener">Cristian Tala</a> ·
    <a href="https://github.com/ctala/ai-benchmarks-alternativos" target="_blank" rel="noopener">Código abierto en GitHub</a> ·
    <a href="https://www.skool.com/cagala-aprende-repite" target="_blank" rel="noopener">Skool</a></p>
  </div>
</footer>
</body>
</html>
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", help="Generar solo esta comparación")
    args = ap.parse_args()
    models = load_models()
    for cfg in COMPARISONS:
        if args.slug and cfg["slug"] != args.slug:
            continue
        A, B = family(models, cfg["a"]), family(models, cfg["b"])
        if not A or not B:
            print(f"⚠️  {cfg['slug']}: sin modelos (A={len(A)} B={len(B)})")
            continue
        outdir = DOCS / cfg["slug"]
        outdir.mkdir(exist_ok=True)
        (outdir / "index.html").write_text(render(cfg, A, B), encoding="utf-8")
        print(f"✓ {cfg['slug']}: {len(A)} {cfg['a']['name']} + {len(B)} {cfg['b']['name']} → docs/{cfg['slug']}/index.html")


if __name__ == "__main__":
    main()
