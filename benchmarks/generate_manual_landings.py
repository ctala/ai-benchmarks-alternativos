#!/usr/bin/env python3
"""
Genera/actualiza las landings manuales de docs/ a partir de docs/data/models.json.

Landings mantenidas:
  - docs/alternativas-chatgpt/index.html
  - docs/alternativas-claude/index.html
  - docs/alternativas-gemini/index.html
  - docs/modelos-n8n/index.html
  - docs/modelos-baratos-emprendedores/index.html
  - docs/modelos-open-source-local/index.html

Landings nuevas (pSEO):
  - docs/alternativas-deepseek/index.html
  - docs/deepseek-vs-claude/index.html
  - docs/deepseek-vs-gemini/index.html
  - docs/mejor-llm-para-razonamiento/index.html

Incluye marcadores <!-- AUTO:... --> para que sync_doc_counts.py sincronice counts.
Metodología v3.0: calidad 70% + costo 15% + velocidad 7,5% + latencia 7,5%;
tool_calling es badge, no entra en el score.

Uso:
    python benchmarks/generate_manual_landings.py
"""
import argparse
import html
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent.parent
DOCS = ROOT / "docs"
MODELS_JSON = DOCS / "data" / "models.json"
SITE = "https://benchmarks.cristiantala.com"
LOGO = "https://assets.nyx.cristiantala.com/2026/images/logo-cristian-tala-sanchez-2026.png"
LOGO_DARK = "https://assets.nyx.cristiantala.com/2026/images/logo-cristian-tala-sanchez-dark-2026.png"
OG_IMAGE = f"{SITE}/og-benchmark.png"
TODAY = date.today().isoformat()


def load_data():
    return json.loads(MODELS_JSON.read_text(encoding="utf-8"))


def counts(data):
    return {
        "total_models": data["total_models"],
        "tested_count": data["tested_count"],
        "tests_marketing": _round_marketing(sum(m.get("runs", 0) for m in data["models"] if m.get("tested"))),
    }


def _round_marketing(n: int) -> str:
    if n < 1000:
        return str(n)
    floor_k = (n // 1000) * 1000
    return f"{floor_k:,}+"


def esc(s):
    return html.escape(str(s))


def fmt_cost(m):
    return f"${m.get('cost_input_per_M', 0):.2f} / ${m.get('cost_output_per_M', 0):.2f}"


def fmt_provider_speed(m):
    provider = m.get("provider", "")
    speed = m.get("tokens_per_second") or 0
    if speed:
        return f"{provider} ({round(speed)} tok/s)"
    return provider


def fmt_license(m):
    if m.get("open_source"):
        return m.get("license") or "Open source"
    return "Propietaria"


def fmt_pillar(m, name):
    v = (m.get("score_by_pillar") or {}).get(name) or 0
    return f"{v:.2f}" if v > 0 else "—"


def fmt_runs(m):
    return str(m.get("runs", 0))


def header(title, desc, kw, url, og_alt=None, extra_head=""):
    jsonld = json.dumps({
        "@context": "https://schema.org", "@type": "Article", "headline": title,
        "description": desc, "author": {"@type": "Person", "name": "Cristian Tala", "url": "https://cristiantala.com"},
        "datePublished": TODAY, "dateModified": TODAY, "inLanguage": "es",
        "url": url, "mainEntityOfPage": url,
        "publisher": {"@type": "Person", "name": "Cristian Tala", "url": "https://cristiantala.com"},
    }, ensure_ascii=False, indent=2)
    og_alt = og_alt or "Ranking de modelos IA del benchmark de Cristian Tala"
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="keywords" content="{esc(kw)}">
<meta name="author" content="Cristian Tala">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="article">
<meta property="og:locale" content="es_CL">
<meta property="og:image" content="{OG_IMAGE}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{esc(og_alt)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{OG_IMAGE}">
<link rel="icon" type="image/png" href="{LOGO}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../style.css">
<script type="application/ld+json">
{jsonld}
</script>
{extra_head}
</head>
<body>

<header>
  <div class="container header-inner">
    <a href="https://cristiantala.com" class="logo-link" target="_blank" rel="noopener">
      <img src="{LOGO_DARK}" alt="Cristian Tala" class="logo">
    </a>
    <nav aria-label="Principal">
      <a href="/">Calculadora</a>
      <a href="https://github.com/ctala/ai-benchmarks-alternativos" target="_blank" rel="noopener">Repo</a>
      <a href="https://www.skool.com/cagala-aprende-repite" target="_blank" rel="noopener" class="cta-mini">Comunidad</a>
    </nav>
  </div>
</header>

<main class="container">
"""


FOOTER = """
</main>

<footer>
  <div class="container">
    <p>
      Hecho por <a href="https://cristiantala.com" target="_blank" rel="noopener">Cristian Tala</a> ·
      <a href="https://github.com/ctala/ai-benchmarks-alternativos" target="_blank" rel="noopener">Código abierto en GitHub</a> ·
      <a href="https://www.skool.com/cagala-aprende-repite" target="_blank" rel="noopener">Skool</a>
    </p>
  </div>
</footer>

</body>
</html>
"""


def methodology_block(c):
    return f"""<section>
  <h2>¿Qué mide este benchmark?</h2>
  <p>No es un benchmark académico: es un benchmark <strong>aplicado para emprendedores hispanohablantes</strong>.
  Medimos qué modelo conviene poner en producción para casos reales, con lo que los benchmarks oficiales no cubren —
  costo en provider real, velocidad, español neutro y agentes multi-turno.</p>
  <p>Contamos con <strong><!-- AUTO:total_models -->{c['total_models']}<!-- /AUTO --> modelos catalogados</strong>,
  <strong><!-- AUTO:tested_count -->{c['tested_count']}<!-- /AUTO --> testeados</strong> y
  <strong><!-- AUTO:tests_marketing -->{c['tests_marketing']}<!-- /AUTO --> tests reales</strong> evaluados por un
  <strong>LLM-as-Judge local (Phi-4, de Microsoft — sin conflicto de interés)</strong>, en 4 pilares:</p>
  <ul>
    <li><strong>Coding</strong> — generar código, JSON estructurado y debugging en tareas reales (plugins WordPress, scripts, templates de N8N).</li>
    <li><strong>Contenido</strong> — blogs, copy y textos largos en español neutro (no traducción del inglés).</li>
    <li><strong>Razonamiento</strong> — matemáticas, lógica formal y planificación multi-paso.</li>
    <li><strong>Agentes</strong> — multi-turno largo, tool calling y flujos tipo N8N / Hermes.</li>
  </ul>
  <p>El <strong>score global v3.0</strong> es una función ponderada: <strong>calidad 70% + costo 15% + velocidad 7,5% + latencia 7,5%</strong>.
  Tool calling se reporta como badge de capacidad, no entra en el score. Mide <em>valor para producción</em>, no solo capacidad bruta.
  <a href="https://github.com/ctala/ai-benchmarks-alternativos/blob/main/TESTS.md" target="_blank" rel="noopener">Metodología y tests completos</a>.</p>
</section>"""


def cta_block(links):
    return f"""<section class="cta-block">
  <h2>Probá la calculadora con tu caso real</h2>
  <p>Filtrá por presupuesto mensual, calidad mínima, velocidad requerida y tipo de tarea. En 30 segundos encontrás el mejor para vos.</p>
  <a href="/" class="cta-primary">Ir a la calculadora →</a>
  <p class="meta" style="margin-top: 1rem;">Ver también: {" · ".join(links)}</p>
</section>"""


def row_alt(rank, m):
    top = rank == 1
    name = f"<strong>{esc(m['name'])}</strong>" if top else esc(m['name'])
    return (f"<tr><td>{rank}</td><td>{name}</td><td>{m['score_global']:.2f}</td>"
            f"<td>{fmt_cost(m)}</td><td>{esc(fmt_license(m))}</td><td>{esc(fmt_provider_speed(m))}</td></tr>")


def table_alt(models, c):
    rows = "\n        ".join(row_alt(i + 1, m) for i, m in enumerate(models))
    return f"""<table class="results-table">
      <thead>
        <tr><th scope="col">#</th><th scope="col">Modelo</th><th scope="col">Score</th><th scope="col">$ in/out per M</th><th scope="col">License</th><th scope="col">Provider</th></tr>
      </thead>
      <tbody>
        {rows}
      </tbody>
    </table>"""


def faq_schema(questions):
    main = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in questions]
    return json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": main}, ensure_ascii=False, indent=2)


def faq_html(questions):
    items = "\n    ".join(f"<details><summary><strong>{esc(q)}</strong></summary><p>{esc(a)}</p></details>" for q, a in questions)
    return f"<section class=\"faq\">\n  <h2>Preguntas frecuentes</h2>\n  {items}\n</section>"


# ---------------------------------------------------------------------------
# Landing: alternativas-chatgpt
# ---------------------------------------------------------------------------
def gen_alternativas_chatgpt(data):
    models = data["models"]
    c = counts(data)
    # Alternativas = todo modelo testeado que no sea de OpenAI (provider openai) salvo GPT-OSS open source.
    alts = [m for m in models if m.get("tested") and m.get("score_global", 0) > 0
            and (m.get("provider") != "openai" or "gpt-oss" in m["name"].lower())]
    alts = sorted(alts, key=lambda m: -m["score_global"])[:10]

    title = "Alternativas a ChatGPT en 2026: 10 modelos comparados con benchmark real"
    desc = ("¿Buscas alternativas a ChatGPT/GPT-4/GPT-5 para agentes, coding o contenido en español? "
            "Comparamos 10 modelos con 10,000+ tests reales: DeepSeek, Claude, Llama, Devstral, Gemini, Mistral, Qwen y más. Datos abiertos.")
    kw = ("alternativas ChatGPT, alternativas GPT-4, alternativas GPT-5, ChatGPT vs Claude, ChatGPT vs Gemini, "
          "ChatGPT vs DeepSeek, OpenAI alternativas, GPT alternativas español, modelos similares ChatGPT, ChatGPT API alternativa")
    url = f"{SITE}/alternativas-chatgpt/"
    og_alt = "Top alternativas a ChatGPT comparadas con benchmark real"

    body = f"""  <section class="hero">
    <h1>Alternativas a ChatGPT: 10 modelos comparados con benchmark real (Junio 2026)</h1>
    <p class="lead">
      Si pagás $20/mes de ChatGPT Plus o usás GPT-4/GPT-5 vía API, estas son las alternativas reales —
      probadas con <strong><!-- AUTO:tested_count -->{c['tested_count']}<!-- /AUTO --> modelos testeados</strong>
      y LLM-as-Judge Phi-4 local. Sin opiniones, sin marketing: sólo datos.
    </p>
    <p class="lead" style="margin-top: 1rem;">
      ⚠️ <strong>Importante</strong>: no existe una "alternativa a ChatGPT" universal. Depende de tu
      tarea: <em>coding de scripts</em> ≠ <em>plugins WordPress</em> ≠ <em>proyectos grandes</em>.
      <em>Blog técnico</em> ≠ <em>copy de marketing</em> ≠ <em>soporte al cliente</em>.
    </p>
    <p class="meta">
      Última actualización: {TODAY} ·
      <a href="https://github.com/ctala/ai-benchmarks-alternativos" target="_blank" rel="noopener">datos abiertos en GitHub</a>
    </p>
  </section>

  <section class="results">
    <div class="results-header">
      <h2>Top 10 alternativas a ChatGPT (ranking global)</h2>
      <p class="meta">Score ponderado v3.0: calidad 70% + costo 15% + velocidad 7,5% + latencia 7,5%.</p>
    </div>

    {table_alt(alts, c)}

    <p class="meta">
      Para filtrar por presupuesto, calidad mínima o tarea específica usá la
      <a href="/">calculadora interactiva</a>.
    </p>
  </section>

  <section>
    <h2>¿Qué alternativa a ChatGPT elegir según tu caso?</h2>

    <h3>Si reemplazás ChatGPT Plus para uso personal/exploratorio</h3>
    <p>
      Para chat conversacional <strong>Claude Haiku 4.5</strong> o <strong>Gemini 2.5 Flash Lite</strong>
      cubren prácticamente todo lo que hace GPT-4 Plus. Si querés gratis, <strong>NVIDIA NIM</strong>
      ofrece 135+ modelos a 40 RPM.
    </p>

    <h3>Si pagás GPT-4 / GPT-5 API para tu app o agente</h3>
    <p>
      Donde el ahorro es brutal: <strong>Mistral Small 4</strong> ($0.15/$0.60) y
      <strong>Devstral Small</strong> ($0.10/$0.30) cubren 80% de los casos a una fracción del costo de GPT-4.1.
      Para volumen &gt;5,000 calls/mes el cambio paga decenas de USD/mes.
    </p>

    <h3>Si usás ChatGPT para coding</h3>
    <p>
      <strong>Plugins WordPress, scripts, automatizaciones</strong> → Devstral Small basta.
      <strong>Templates N8N (JSON workflows)</strong> → Llama 3.3 70B Groq es óptimo (ver <a href="/modelos-n8n/">modelos para N8N</a>).
      <strong>Proyectos grandes con arquitectura compleja</strong> → solo aquí GPT-5.5 o Claude Opus 4.8 justifican el costo.
    </p>

    <h3>Si usás ChatGPT para contenido en español</h3>
    <p>
      <strong>Qwen 3.6 Max</strong> y <strong>Gemini 3.1 Flash Lite</strong> superan a GPT-4 en
      blog técnico y contenido de actualidad startup en español. Caso real: Cristian usa modelos Qwen en producción para
      <a href="https://ecosistemastartup.com" target="_blank" rel="noopener">ecosistemastartup.com</a>.
    </p>

    <h3>Si usás ChatGPT para agentes (con tool calling)</h3>
    <p>
      <strong>Llama 3.3 70B en Groq</strong> + <strong>Hermes 4 70B</strong> son los más sólidos para
      tool calling estructurado. La velocidad de Groq (240+ tok/s) hace que agentes con muchas iteraciones
      se sientan instantáneos.
    </p>
  </section>
"""
    faqs = [
        ("¿Hay alguna alternativa a ChatGPT que sea gratis?",
         "Sí — NVIDIA NIM ofrece 135+ modelos gratis con 40 RPM. Para uso local sin costos de API: Mistral Small 4, Devstral Small o Llama 3.3 70B corren en hardware decente (≥32GB RAM unified)."),
        ("¿ChatGPT Plus o suscripción Anthropic — cuál conviene?",
         "Depende del uso. Si usás chat conversacional sin volumen, ChatGPT Plus a $20 sigue siendo competitivo. Si construís agentes/herramientas: ninguna suscripción mensual gana — usá API direct con modelos open-source que cuestan ~$0.30 per M output tokens."),
        ("¿GPT-5 es necesario o puedo usar alternativas más baratas?",
         "GPT-5 (y GPT-5.5) brillan en razonamiento profundo, planning multi-step y código complejo de proyectos grandes. Para 80% de tareas estándar son overkill: Devstral Small a 1/100 del costo cubre el caso."),
        ("¿Las alternativas a ChatGPT soportan tool calling y function calling?",
         "Sí — Llama 3.3, Mistral Small 4, Devstral, Hermes 4 y Qwen soportan tool calling OpenAI-compatible. El benchmark testea esto como badge; modelos sin soporte robusto se identifican claramente."),
        ("¿Puedo usar alternativas a ChatGPT vía OpenRouter sin cambiar mi código?",
         "Sí — OpenRouter expone API compatible con OpenAI. Cambiás base_url y api_key, y elegís modelos por su ID (ej. mistralai/mistral-small-2603). Tu código de OpenAI SDK funciona igual."),
    ]
    body += faq_html(faqs)
    body += cta_block([
        '<a href="/alternativas-claude/">alternativas a Claude</a>',
        '<a href="/alternativas-gemini/">alternativas a Gemini</a>',
        '<a href="/alternativas-deepseek/">alternativas a DeepSeek</a>',
        '<a href="/modelos-n8n/">modelos para N8N</a>',
        '<a href="/modelos-open-source-local/">open-source local</a>',
    ])
    extra = f"<script type=\"application/ld+json\">\n{faq_schema(faqs)}\n</script>"
    return header(title, desc, kw, url, og_alt=og_alt, extra_head=extra) + body + FOOTER


# ---------------------------------------------------------------------------
# Landing: alternativas-claude
# ---------------------------------------------------------------------------
def gen_alternativas_claude(data):
    models = data["models"]
    c = counts(data)
    alts = [m for m in models if m.get("tested") and m.get("score_global", 0) > 0 and m.get("provider") != "anthropic"]
    alts = sorted(alts, key=lambda m: -m["score_global"])[:10]

    title = "Alternativas a Claude en 2026: 10 modelos comparados con benchmark real"
    desc = ("¿Buscas alternativas a Claude por precio o por el cambio en la suscripción Pro? "
            "Comparamos 10 modelos con 10,000+ tests reales: DeepSeek, Devstral, Mistral, Llama, GPT-OSS, Gemini, Qwen y más. Datos abiertos.")
    kw = ("alternativas Claude, Claude alternatives, modelos similares Claude, Claude vs GPT, Claude vs Gemini, "
          "Claude vs Llama, Claude Code alternativa, Anthropic alternativas, agentes IA sin Claude")
    url = f"{SITE}/alternativas-claude/"
    og_alt = "Top alternativas a Claude comparadas con benchmark real"

    body = f"""  <section class="hero">
    <h1>Alternativas a Claude: 10 modelos comparados con benchmark real (Junio 2026)</h1>
    <p class="lead">
      Si usás Claude para coding, agentes N8N o Hermes, o generación de contenido, estas son las
      alternativas reales — no opiniones, datos: <strong><!-- AUTO:tested_count -->{c['tested_count']}<!-- /AUTO --> modelos testeados</strong>,
      evaluados con LLM-as-Judge Phi-4 local.
    </p>
    <p class="lead" style="margin-top: 1rem;">
      ⚠️ <strong>Importante</strong>: no existe un "mejor modelo" universal. "Coding" significa cosas
      muy distintas si desarrollás plugins de WordPress, templates de N8N, scripts de automatización
      o proyectos grandes.
    </p>
    <p class="meta">
      Última actualización: {TODAY} ·
      <a href="https://github.com/ctala/ai-benchmarks-alternativos" target="_blank" rel="noopener">datos abiertos en GitHub</a>
    </p>
  </section>

  <section class="results">
    <div class="results-header">
      <h2>Top 10 alternativas a Claude (ranking global)</h2>
      <p class="meta">Score ponderado v3.0: calidad 70% + costo 15% + velocidad 7,5% + latencia 7,5%.</p>
    </div>

    {table_alt(alts, c)}

    <p class="meta">
      Para filtrar por presupuesto, calidad mínima o tarea específica usá la
      <a href="/">calculadora interactiva</a>.
    </p>
  </section>

  <section>
    <h2>¿Qué alternativa a Claude elegir según tu caso?</h2>

    <h3>Si reemplazas Claude Code (coding profesional)</h3>
    <p>
      <strong>Devstral 2</strong> y <strong>Devstral Small</strong> son las opciones top.
      Ambas Apache 2.0 — podés correrlas local en hardware decente. Devstral 2 supera a GPT-4.1 en
      generación de código y JSON estructurado a una fracción del costo de Claude Opus.
    </p>

    <h3>Si usás Claude para agentes N8N o Hermes</h3>
    <p>
      <strong>Llama 3.3 70B en Groq</strong> domina por velocidad (240+ tok/s — mucho más rápido que
      Claude Sonnet) y precio ($0.59 input vs $3.00+ de Sonnet). Para agentes con muchas calls/mes
      el ahorro es sustancial. Ver más en <a href="/modelos-n8n/">modelos para N8N</a>.
    </p>

    <h3>Si querés open-source para correr local</h3>
    <p>
      <strong>Mistral Small 4</strong> (Apache 2.0, 24B) es la mejor relación performance/tamaño.
      Para hardware con más RAM (≥80GB), <strong>Qwen 3.6 Max</strong> o <strong>DeepSeek V4 Flash</strong>
      compiten con modelos premium. Detalles en <a href="/modelos-open-source-local/">modelos open-source local</a>.
    </p>

    <h3>Si querés contenido en español</h3>
    <p>
      <strong>Gemini 3.1 Flash Lite</strong> y <strong>Qwen 3.6 Max</strong> superan a Claude Haiku
      en blogs, traducciones y marketing en español. La diferencia se vuelve significativa en textos largos.
    </p>

    <h3>Si necesitás razonamiento profundo</h3>
    <p>
      Para razonamiento de élite (matemáticas, lógica formal, deep planning), Claude Opus 4.8 sigue arriba —
      pero por margen menor al que el marketing sugiere. Las alternativas reales son <strong>DeepSeek R1</strong>
      y <strong>Hermes 4 70B</strong> (hybrid reasoning, mucho más barato).
    </p>
  </section>
"""
    faqs = [
        ("¿Por qué dejar de usar Claude?",
         "No necesariamente 'dejar' — más bien usar la herramienta correcta por caso. Claude Opus es excelente pero su costo (~$5-25 per M tokens) hace que para agentes con volumen real (1,000+ calls/mes) se vuelva insostenible. Modelos como Devstral Small ($0.10/$0.30) cubren el 80% de casos a 1/50 del costo."),
        ("¿Hay alguna alternativa a Claude que sea mejor en TODO?",
         "No. Cada modelo tiene perfil distinto: Llama 3.3 Groq gana en velocidad, Devstral en coding, Gemini/Qwen en contenido español, GPT-5.5 en razonamiento profundo. La pregunta correcta es 'alternativa a Claude para qué'."),
        ("¿Las alternativas a Claude soportan tool calling?",
         "Sí — Devstral, Mistral Small 4, Llama 3.3, Hermes 4 y Qwen soportan tool calling estructurado. El benchmark testea esto como badge; modelos sin tool calling robusto se identifican claramente."),
        ("¿Qué pasa con Claude Sonnet 4.6 / Opus 4.8?",
         "Están en el benchmark global. Ranquean alto en tareas premium, pero su precio los saca de competencia para volumen. Si tu uso es <100 calls/día y no te importa el costo, Claude sigue siendo válido. Para volumen, las alternativas listadas dan mejor ROI."),
        ("¿Puedo correr alternativas a Claude local sin GPU dedicada?",
         "Sí — Mistral Small 4 corre cómodamente en Mac M-series con 32GB RAM. Devstral Small también. Para modelos más grandes (Llama 70B, Qwen 3.6 Max) necesitás 64GB+ unified memory o GPU dedicada. Detalles en /modelos-open-source-local/."),
    ]
    body += faq_html(faqs)
    body += cta_block([
        '<a href="/alternativas-chatgpt/">alternativas a ChatGPT</a>',
        '<a href="/alternativas-gemini/">alternativas a Gemini</a>',
        '<a href="/alternativas-deepseek/">alternativas a DeepSeek</a>',
        '<a href="/modelos-n8n/">modelos para N8N</a>',
        '<a href="/modelos-open-source-local/">open-source local</a>',
    ])
    extra = f"<script type=\"application/ld+json\">\n{faq_schema(faqs)}\n</script>"
    return header(title, desc, kw, url, og_alt=og_alt, extra_head=extra) + body + FOOTER


# ---------------------------------------------------------------------------
# Landing: alternativas-gemini
# ---------------------------------------------------------------------------
def gen_alternativas_gemini(data):
    models = data["models"]
    c = counts(data)
    alts = [m for m in models if m.get("tested") and m.get("score_global", 0) > 0 and m.get("provider") != "google"]
    alts = sorted(alts, key=lambda m: -m["score_global"])[:10]

    title = "Alternativas a Gemini en 2026: 10 modelos comparados con benchmark real"
    desc = ("¿Buscás alternativas a Gemini 2.5/3.1 Flash, Flash Lite o Pro de Google? "
            "Comparamos 10 modelos con 10,000+ tests reales: DeepSeek, Claude, GPT, Llama, Devstral, Mistral, Qwen y más. Datos abiertos en español.")
    kw = ("alternativas Gemini, alternativas Gemini Flash, Gemini Pro alternativas, Gemini vs Claude, Gemini vs GPT, "
          "Google AI alternativas, modelos similares Gemini, Gemini API alternativa, Gemini español")
    url = f"{SITE}/alternativas-gemini/"
    og_alt = "Top alternativas a Gemini comparadas con benchmark real"

    body = f"""  <section class="hero">
    <h1>Alternativas a Gemini: 10 modelos comparados con benchmark real (Junio 2026)</h1>
    <p class="lead">
      Si usás Gemini 2.5 Flash, 3.1 Flash Lite o Gemini Pro para agentes, contenido o coding,
      estas son las alternativas reales — probadas con <strong><!-- AUTO:tested_count -->{c['tested_count']}<!-- /AUTO --> modelos testeados</strong> y
      LLM-as-Judge Phi-4 local. Datos, no opiniones.
    </p>
    <p class="lead" style="margin-top: 1rem;">
      ⚠️ <strong>Importante</strong>: no existe un "mejor reemplazo de Gemini" universal. La elección
      depende de tu tarea: traducciones, blog técnico, copy de marketing, plugins WordPress y templates N8N son problemas distintos.
    </p>
    <p class="meta">
      Última actualización: {TODAY} ·
      <a href="https://github.com/ctala/ai-benchmarks-alternativos" target="_blank" rel="noopener">datos abiertos en GitHub</a>
    </p>
  </section>

  <section class="results">
    <div class="results-header">
      <h2>Top 10 alternativas a Gemini (ranking global)</h2>
      <p class="meta">Score ponderado v3.0: calidad 70% + costo 15% + velocidad 7,5% + latencia 7,5%.</p>
    </div>

    {table_alt(alts, c)}

    <p class="meta">
      Para filtrar por presupuesto, calidad mínima o tarea específica usá la
      <a href="/">calculadora interactiva</a>.
    </p>
  </section>

  <section>
    <h2>¿Qué alternativa a Gemini elegir según tu caso?</h2>

    <h3>Si usás Gemini Flash Lite por la velocidad/costo</h3>
    <p>
      <strong>Llama 3.3 70B en Groq</strong> tiene 240+ tok/s avg (más rápido que Flash Lite) a precio
      similar. <strong>Mistral Small 4</strong> es la opción más barata con calidad superior.
    </p>

    <h3>Si usás Gemini Pro para razonamiento</h3>
    <p>
      <strong>DeepSeek R1</strong> y <strong>Hermes 4 70B</strong> (hybrid reasoning) cubren bien
      razonamiento multi-step. Para razonamiento de élite (matemáticas formales, planning complejo)
      <strong>Claude Opus 4.8</strong> o <strong>GPT-5.5</strong> son superiores pero a costo premium.
    </p>

    <h3>Si usás Gemini para multimodal (imágenes/audio)</h3>
    <p>
      Para multimodal real (visión, OCR, audio), <strong>Gemini sigue siendo el rey</strong>.
      Las alternativas multimodales open-source (Llama 4 Vision, Qwen 3 VL) están bien pero el delta
      sigue siendo notorio. Esta versión del benchmark se enfoca en text-only — multimodal está en roadmap.
    </p>

    <h3>Si usás Gemini para contenido en español</h3>
    <p>
      <strong>Qwen 3.6 Max</strong> es el modelo que destaca en producción para contenido de actualidad startup.
      <strong>Mistral Small 4</strong> y <strong>Llama 3.3 Groq</strong> también dan resultados sólidos en blog técnico y newsletters.
    </p>

    <h3>Si usás Gemini para coding</h3>
    <p>
      <strong>Plugins WordPress, scripts, automatizaciones</strong> → Devstral Small basta.
      <strong>Templates N8N</strong> → Llama 3.3 70B Groq (ver <a href="/modelos-n8n/">modelos para N8N</a>).
      <strong>Proyectos grandes con arquitectura</strong> → GPT-5.5 o Claude Opus 4.8 cuando justifica el costo.
    </p>

    <h3>Si usás Gemini para agentes con tool calling</h3>
    <p>
      <strong>Llama 3.3 70B Groq</strong> + <strong>Hermes 4 70B</strong> son los más sólidos.
      Detalles en <a href="/modelos-n8n/">modelos para N8N</a>.
    </p>
  </section>
"""
    faqs = [
        ("¿Qué alternativa a Gemini Flash Lite es realmente equivalente?",
         "Llama 3.3 70B en Groq es el match más cercano: precio similar, velocidad superior (240+ tok/s), calidad ligeramente mejor en español. Gemini Flash Lite gana en latencia bajo cargas globales y multimodal."),
        ("¿Hay alguna alternativa a Gemini gratis?",
         "NVIDIA NIM ofrece 135+ modelos gratis con 40 RPM. Para local sin costos: Mistral Small 4 corre en 32GB RAM."),
        ("¿Gemini 3.1 Flash Lite vale más que las alternativas?",
         "Gemini 3.1 Flash Lite ranquea alto. Pero DeepSeek V4 Flash, Mistral Small 4 y Llama 3.3 70B Groq lo superan en score absoluto para text-only. Si tu caso es contenido o coding estándar, las alternativas ganan. Si necesitás contexto >100K tokens o multimodal, Gemini sigue."),
        ("¿Las alternativas a Gemini soportan contexto largo?",
         "Gemini sigue dominando contexto largo (1M+ tokens). Alternativas con contexto &gt;128K viables: Claude Opus 4.8 (1M), GPT-5.5 (256K+), Llama 4 (1M). Para context típico (8K-32K) casi todas las alternativas listadas son válidas."),
        ("¿Vale la pena migrar de Gemini API a alternativas?",
         "Depende del volumen y caso. Para >5,000 calls/mes en text-only, sí — el ahorro a Mistral Small 4 o Devstral es de 60-90% manteniendo calidad similar. Para <1,000 calls/mes o casos multimodales, no vale el costo del switch."),
    ]
    body += faq_html(faqs)
    body += cta_block([
        '<a href="/alternativas-chatgpt/">alternativas a ChatGPT</a>',
        '<a href="/alternativas-claude/">alternativas a Claude</a>',
        '<a href="/alternativas-deepseek/">alternativas a DeepSeek</a>',
        '<a href="/modelos-n8n/">modelos para N8N</a>',
        '<a href="/modelos-open-source-local/">open-source local</a>',
    ])
    extra = f"<script type=\"application/ld+json\">\n{faq_schema(faqs)}\n</script>"
    return header(title, desc, kw, url, og_alt=og_alt, extra_head=extra) + body + FOOTER


# ---------------------------------------------------------------------------
# Landing: modelos-n8n
# ---------------------------------------------------------------------------
def row_n8n(rank, m):
    top = rank == 1
    name = f"<strong>{esc(m['name'])}</strong>" if top else esc(m['name'])
    speed = m.get("tokens_per_second") or 0
    speed_str = f"{round(speed)} ⚡" if speed >= 200 else (f"{round(speed)}" if speed else "—")
    return (f"<tr><td>{rank}</td><td>{name}</td><td>{m['score_global']:.2f}</td>"
            f"<td>{fmt_cost(m)}</td><td>{speed_str}</td><td>{esc(fmt_license(m))}</td></tr>")


def gen_modelos_n8n(data):
    models = data["models"]
    c = counts(data)
    n8n = [m for m in models if m.get("tested") and ((m.get("score_by_pillar") or {}).get("Agentes", 0) > 0)]
    n8n = sorted(n8n, key=lambda m: -m["score_by_pillar"]["Agentes"])[:10]

    title = "Mejores modelos IA para agentes N8N: comparativa con benchmark real (2026)"
    desc = ("Qué modelo IA usar en tu agente N8N: 10 modelos comparados con tests reales de tool calling, "
            "JSON estructurado y workflows. Llama 3.3 Groq, Mistral Small 4, Devstral, Hermes 4 y más. Datos abiertos en español.")
    kw = ("modelos IA N8N, mejor modelo agente N8N, N8N AI agent, N8N OpenRouter, N8N tool calling, "
          "modelo barato N8N, agente automation IA, workflow IA español")
    url = f"{SITE}/modelos-n8n/"
    og_alt = "Top modelos IA para agentes N8N según benchmark real"

    rows = "\n        ".join(row_n8n(i + 1, m) for i, m in enumerate(n8n))
    table = f"""<table class="results-table">
      <thead>
        <tr><th scope="col">#</th><th scope="col">Modelo</th><th scope="col">Score</th><th scope="col">$ in/out per M</th><th scope="col">Tok/s</th><th scope="col">License</th></tr>
      </thead>
      <tbody>
        {rows}
      </tbody>
    </table>"""

    body = f"""  <section class="hero">
    <h1>Mejores modelos IA para agentes N8N: comparativa con benchmark real (Junio 2026)</h1>
    <p class="lead">
      Si construís agentes en N8N o Hermes, elegir el modelo correcto importa más que casi
      cualquier otro factor: una decisión equivocada puede 10× tu factura mensual sin mejorar la calidad
      visible. Acá: <strong>10 modelos comparados con tests reales de tool calling, JSON workflows y latencia</strong>.
    </p>
    <p class="lead" style="margin-top: 1rem;">
      ⚠️ <strong>Nota</strong>: "agente N8N" no es una sola cosa. Difiere si tu workflow tiene 1 LLM
      call vs 20 encadenadas, si necesita parsing estructurado vs texto libre, si la latencia importa al
      usuario o es batch nocturno.
    </p>
    <p class="meta">
      Última actualización: {TODAY} ·
      <a href="https://github.com/ctala/ai-benchmarks-alternativos" target="_blank" rel="noopener">datos abiertos en GitHub</a>
    </p>
  </section>

  <section class="results">
    <div class="results-header">
      <h2>Top 10 modelos para N8N (priorizando tool calling + velocidad)</h2>
      <p class="meta">Ordenados por score en el pilar Agentes. Tool calling es badge de capacidad, no entra en el score global v3.0.</p>
    </div>

    {table}

    <p class="meta">
      Filtrá por tu volumen y restricciones en la <a href="/">calculadora interactiva</a>.
    </p>
  </section>

  <section>
    <h2>¿Qué modelo elegir según tu agente N8N?</h2>

    <h3>Si tu agente hace 100-500 calls/día con tool calling crítico</h3>
    <p>
      <strong>Llama 3.1 8B Instant (Groq)</strong> es la elección dominante. 367 tok/s significa que workflows
      con 5-10 LLM calls encadenados se sienten instantáneos. El JSON output es robusto — testeado en
      <code>code_generation/n8n_workflow_json</code>.
    </p>

    <h3>Si construís un SaaS con miles de calls/mes</h3>
    <p>
      <strong>Mistral Small 4</strong> ($0.15/$0.60) o <strong>Devstral Small</strong> ($0.10/$0.30)
      son los más eficientes. Para 10,000 calls/mes a 1,800 tokens promedio: Mistral ~$11/mes,
      Devstral ~$5/mes vs ~$162/mes con Claude Sonnet 4.6.
    </p>

    <h3>Si tu agente requiere razonamiento (no solo tool calling)</h3>
    <p>
      <strong>Hermes 4 70B</strong> tiene "hybrid reasoning" — combina respuestas rápidas con modo
      razonamiento profundo cuando lo amerita. <strong>DeepSeek R1</strong> es backup sólido si necesitás reasoning puro.
    </p>

    <h3>Si querés open-source para correr local + N8N self-hosted</h3>
    <p>
      <strong>Mistral Small 4</strong> (Apache 2.0, 24B) cabe en hardware modesto y soporta tool calling
      OpenAI-compatible. <strong>Devstral Small</strong> es alternativa también Apache 2.0. Para más detalles
      sobre setup local: <a href="/modelos-open-source-local/">modelos open-source local</a>.
    </p>

    <h3>Si N8N corre en un servidor con poco budget</h3>
    <p>
      <strong>NVIDIA NIM</strong> ofrece 135+ modelos GRATIS con 40 RPM — más que suficiente para
      agentes con uso secuencial moderado. Modelos disponibles: Llama 3.3, Mistral Small, Nemotron Ultra.
    </p>
  </section>

  <section>
    <h2>Caso real: agente de Cristian para ecosistemastartup.com</h2>
    <p>
      Cristian Tala (autor del benchmark) usa N8N para automatizar la generación de contenido de su blog
      <a href="https://ecosistemastartup.com" target="_blank" rel="noopener">ecosistemastartup.com</a>.
      El agente investiga noticias del ecosistema startup chileno/latinoamericano, sintetiza y genera
      borradores. Modelo en producción: <strong>Qwen 3.5 397B Cloud</strong> via Ollama Cloud
      (incluido en suscripción ~$30/mes, sin costo por call).
    </p>
    <p>
      Por qué no eligió uno del top 5 del benchmark global: el caso de uso es <em>contenido largo en
      español sobre actualidad</em>, donde Qwen 3.5 supera en context preservation y tono natural.
      <strong>Lección</strong>: el ranking global es referencia, pero validá en tu caso real.
    </p>
  </section>
"""
    faqs = [
        ("¿Cómo configuro un modelo del benchmark en N8N?",
         "N8N tiene nodo 'OpenAI Chat Model' — usa cualquier endpoint OpenAI-compatible. Configurá: baseURL: https://openrouter.ai/api/v1 (o Groq, NVIDIA NIM, Ollama Cloud), tu API key y el model del benchmark. Ejemplo: mistralai/mistral-small-2603."),
        ("¿Qué pasa si el modelo open-source que elijo deja de funcionar?",
         "Modelos open-source en OpenRouter pueden deprecar. Estrategia: tener un fallback configurado. N8N permite chains con if/error — primer modelo Mistral Small 4, fallback a Llama 3.3 Groq, fallback final a GPT-4.1."),
        ("¿Tool calling funciona igual en todos los modelos del benchmark?",
         "No. Tool calling es OpenAI-compatible en mayoría pero la robustez varía. El benchmark mide esto como badge; los del top 10 de agentes tienen tool calling testado robusto."),
        ("¿Cuánto cuesta correr un agente N8N con 1000 calls/día?",
         "Asumiendo 300 input + 1500 output tokens promedio (~30K calls/mes): Llama 3.3 Groq ~$25/mes, Mistral Small 4 ~$32/mes, Devstral Small ~$15/mes, Claude Sonnet 4.6 ~$162/mes. El benchmark es la diferencia entre $15 y $162 por la misma calidad práctica."),
        ("¿Debería usar un modelo distinto por nodo en N8N?",
         "Sí, es buena práctica. Routing/clasificación con Gemini Flash Lite (rápido, barato), generación con Llama 3.3 Groq, validación final con GPT-4.1 si es crítico. Stack híbrido suele superar al single-modelo en costo y calidad."),
    ]
    body += faq_html(faqs)
    body += cta_block([
        '<a href="/alternativas-claude/">alternativas a Claude</a>',
        '<a href="/alternativas-chatgpt/">alternativas a ChatGPT</a>',
        '<a href="/alternativas-gemini/">alternativas a Gemini</a>',
        '<a href="/modelos-open-source-local/">open-source local</a>',
    ])
    extra = f"<script type=\"application/ld+json\">\n{faq_schema(faqs)}\n</script>"
    return header(title, desc, kw, url, og_alt=og_alt, extra_head=extra) + body + FOOTER


# ---------------------------------------------------------------------------
# Landing: modelos-baratos-emprendedores
# ---------------------------------------------------------------------------
def row_cheap(rank, m):
    top = rank == 1
    name = f"<strong>{esc(m['name'])}</strong>" if top else esc(m['name'])
    cost_1k = m.get("cost_per_1k_calls_usd") or 0
    cost_str = f"~${cost_1k * 5:.2f}" if cost_1k else "—"
    return (f"<tr><td>{rank}</td><td>{name}</td><td>{m['score_global']:.2f}</td>"
            f"<td>{fmt_cost(m)}</td><td>{cost_str}</td><td>{esc(fmt_license(m))}</td></tr>")


def gen_modelos_baratos(data):
    models = data["models"]
    c = counts(data)
    cheap = [m for m in models if m.get("tested") and m.get("score_global", 0) >= 6.8
             and m.get("cost_input_per_M", 99) <= 1.0 and m.get("cost_output_per_M", 99) <= 2.0]
    cheap = sorted(cheap, key=lambda m: -m["score_global"])[:10]

    title = "Modelos IA baratos para emprendedores: mejores alternativas low-cost (2026)"
    desc = ("Modelos IA accesibles para emprendedores latinoamericanos: comparativa de los más baratos "
            "(<$1.00/M tokens) con calidad real. DeepSeek, Devstral, MiMo, Mistral, Llama, Gemini Lite y opciones gratis.")
    kw = ("modelos IA baratos, IA low cost emprendedores, AI sin presupuesto, OpenRouter barato, modelo IA gratis, "
          "NVIDIA NIM gratis, Devstral Small, MiMo, modelo IA Latinoamerica")
    url = f"{SITE}/modelos-baratos-emprendedores/"
    og_alt = "Modelos IA baratos para emprendedores según benchmark real"

    rows = "\n        ".join(row_cheap(i + 1, m) for i, m in enumerate(cheap))
    table = f"""<table class="results-table">
      <thead>
        <tr><th scope="col">#</th><th scope="col">Modelo</th><th scope="col">Score</th><th scope="col">$ in/out per M</th><th scope="col">$/mes (5K calls)*</th><th scope="col">License</th></tr>
      </thead>
      <tbody>
        {rows}
      </tbody>
    </table>"""

    body = f"""  <section class="hero">
    <h1>Modelos IA baratos para emprendedores: mejores alternativas low-cost (Junio 2026)</h1>
    <p class="lead">
      Si emprendés en Latinoamérica sin venture capital, cada $50/mes en API cuenta. Esta página
      compara los modelos IA <strong>realmente baratos</strong> (&lt;$1.00 input, &lt;$2.00 output per M tokens)
      con calidad medida — no opiniones de marketing. Más opciones <strong>gratis</strong> al final.
    </p>
    <p class="lead" style="margin-top: 1rem;">
      ⚠️ <strong>Importante</strong>: barato no significa malo. DeepSeek V4 Flash ($0.10/$0.20) ranquea #1
      global, superando a modelos 50× más caros. El precio premium ya no garantiza calidad superior.
    </p>
    <p class="meta">
      Última actualización: {TODAY} ·
      <a href="https://github.com/ctala/ai-benchmarks-alternativos" target="_blank" rel="noopener">datos abiertos en GitHub</a>
    </p>
  </section>

  <section class="results">
    <div class="results-header">
      <h2>Top 10 modelos baratos (orden por calidad/precio)</h2>
      <p class="meta">Filtrados a ≤$1.00 input, ≤$2.00 output per M tokens y score ≥ 6,8.</p>
    </div>

    {table}

    <p class="meta">* Asumiendo 300 input + 1500 output tokens promedio per call, 5,000 calls/mes.</p>
  </section>

  <section>
    <h2>Opciones GRATIS para emprendedores</h2>

    <h3>NVIDIA NIM (135+ modelos, 40 RPM)</h3>
    <p>
      Catálogo gratis con 40 requests/minuto — más que suficiente para uso secuencial moderado.
      Joyas disponibles: <strong>Llama 3.3 70B</strong>, <strong>Mistral Small</strong>,
      <strong>Nemotron Ultra 253B</strong>, <strong>Qwen 3-Next 80B</strong>. API OpenAI-compatible.
      Sólo necesitás registrarte en <code>build.nvidia.com</code>.
    </p>

    <h3>Ollama Cloud (suscripción ~$30/mes, calls ilimitadas)</h3>
    <p>
      Si tu uso es alto (&gt;10K calls/mes), suscripción es más barata que API per-call.
      Modelos premium incluidos: <strong>Qwen 3.5 397B</strong> (Apache 2.0). Caso de Cristian:
      usa Qwen 3.5 397B Cloud en producción para
      <a href="https://ecosistemastartup.com" target="_blank" rel="noopener">ecosistemastartup.com</a>.
    </p>

    <h3>Local con Ollama (cero costos por call, una vez setupeado)</h3>
    <p>
      <strong>Mistral Small 4</strong> en Mac M-series 32GB. <strong>Devstral Small</strong> incluso
      en 16GB. Cero costo per call, privacidad total. Tradeoff: velocidad ~30-50 tok/s vs 240+ tok/s
      Groq. Para batch jobs es perfecto. Detalles en
      <a href="/modelos-open-source-local/">modelos open-source local</a>.
    </p>

    <h3>Free tier de OpenRouter (limitado, en flux constante)</h3>
    <p>
      OpenRouter tiene tier gratis pero los modelos free deprecan rápido. No depender solo de free tier para producción
      — usar como fallback secundario.
    </p>
  </section>

  <section>
    <h2>Stack barato recomendado por caso de uso</h2>

    <h3>Emprendedor solopreneur, presupuesto $20/mes total</h3>
    <ul>
      <li><strong>Devstral Small</strong> via OpenRouter para todo: coding, contenido, agentes</li>
      <li>Volumen sostenible: ~30,000 calls/mes con $20 budget</li>
      <li>Backup gratis: NVIDIA NIM con Llama 3.3 70B</li>
    </ul>

    <h3>Startup con producto en MVP, $50-100/mes</h3>
    <ul>
      <li><strong>Mistral Small 4</strong> (calidad principal) + <strong>Llama 3.3 Groq</strong> (latencia crítica)</li>
      <li>Routing/clasificación con Gemini 2.5 Flash Lite (más barato aún)</li>
      <li>Volumen sostenible: ~50K-100K calls/mes</li>
    </ul>

    <h3>Negocio establecido escalando, $200-500/mes</h3>
    <ul>
      <li><strong>Llama 3.3 70B Groq</strong> (calidad + velocidad) como principal</li>
      <li><strong>GPT-4.1</strong> sólo para casos críticos identificados</li>
      <li>Local con DGX Spark cuando volumen &gt;$300/mes en API</li>
    </ul>

    <h3>Generación de contenido masiva</h3>
    <ul>
      <li><strong>Ollama Cloud sub</strong> ($30/mes) con Qwen 3.5 397B → calls ilimitadas</li>
      <li>Caso real: Cristian genera contenido de
        <a href="https://ecosistemastartup.com" target="_blank" rel="noopener">ecosistemastartup.com</a>
        completo desde aquí
      </li>
    </ul>
  </section>
"""
    faqs = [
        ("¿Los modelos baratos son inferiores a Claude Opus o GPT-5?",
         "Para razonamiento profundo y proyectos grandes, sí: Claude Opus 4.8 y GPT-5.5 mantienen ventaja. Para 80% de tareas estándar (contenido, agentes, coding mediano), DeepSeek V4 Flash o Mistral Small 4 a 1/100 del costo de Opus dan resultados prácticamente equivalentes. El benchmark cuantifica el delta exacto."),
        ("¿Vale la pena pagar por suscripciones (Ollama Cloud, OpenRouter, ChatGPT Plus)?",
         "Ollama Cloud (~$30/mes calls ilimitadas a Qwen 3.5 397B): sí si volumen >5K calls/mes. OpenRouter pre-paid: solo paga lo que usás, no hay suscripción mensual. ChatGPT Plus ($20/mes): solo si usás chat conversacional sin construir agentes/herramientas. Para producto: API direct con modelos baratos gana siempre."),
        ("¿Cómo manejo límites de rate y errores con modelos baratos?",
         "Patrón fallback chain: principal Mistral Small 4, si falla Devstral Small, si falla Llama 3.3 Groq, último recurso GPT-4.1. N8N permite implementar esto con nodos If/Error nativos. Robustez sin pagar premium por defecto."),
        ("¿Qué moneda paga en estos servicios? ¿Hay opción local sin tarjeta de crédito?",
         "OpenRouter, OpenAI, Anthropic: tarjeta USD. NVIDIA NIM: gratis con email. Ollama Cloud: requiere tarjeta. Local con Ollama: cero costos, sólo hardware. Para Latinoamérica con limitaciones de moneda, opciones gratis (NVIDIA NIM) + local son el fallback principal."),
        ("¿Cómo empiezo si nunca usé estos modelos antes?",
         "Pasos: 1) Crear cuenta en OpenRouter ($5 mínimo), 2) Probar Devstral Small ($0.10/$0.30) con tu caso real, 3) Si funciona, escalar volumen, 4) Si calidad insuficiente, subir a Mistral Small 4 o Llama 3.3 Groq."),
    ]
    body += faq_html(faqs)
    body += cta_block([
        '<a href="/alternativas-claude/">alternativas a Claude</a>',
        '<a href="/alternativas-chatgpt/">alternativas a ChatGPT</a>',
        '<a href="/alternativas-gemini/">alternativas a Gemini</a>',
        '<a href="/modelos-n8n/">modelos para N8N</a>',
        '<a href="/modelos-open-source-local/">open-source local</a>',
    ])
    extra = f"<script type=\"application/ld+json\">\n{faq_schema(faqs)}\n</script>"
    return header(title, desc, kw, url, og_alt=og_alt, extra_head=extra) + body + FOOTER


# ---------------------------------------------------------------------------
# Landing: modelos-open-source-local
# ---------------------------------------------------------------------------
def gen_modelos_open_source_local(data):
    models = data["models"]
    c = counts(data)
    oss = [m for m in models if m.get("tested") and m.get("open_source") and m.get("score_global", 0) > 0]
    oss = sorted(oss, key=lambda m: -m["score_global"])[:10]

    title = "Modelos IA open-source para correr local: comparativa por hardware (2026)"
    desc = ("¿Qué modelo IA open-source correr local en Mac M-series, NVIDIA DGX Spark o GPU dedicada? "
            "Comparativa de Devstral, Mistral, Llama, Qwen, DeepSeek, GPT-OSS por RAM/VRAM con benchmark real de 10,000+ tests.")
    kw = ("modelos IA local, LLM open source local, Ollama Mac M3, DGX Spark modelos, Mistral Small local, "
          "Llama 70B local, GPT-OSS local, modelo IA sin API, modelo IA gratis local")
    url = f"{SITE}/modelos-open-source-local/"
    og_alt = "Modelos IA open-source para correr local según benchmark real"

    body = f"""  <section class="hero">
    <h1>Modelos IA open-source para correr local: comparativa por hardware (Junio 2026)</h1>
    <p class="lead">
      Correr modelos local te da: cero costos por call, privacidad total de datos, y latencia sin
      red. Pero la pregunta correcta no es "qué modelo es el mejor" sino <strong>"qué modelo cabe en
      mi hardware y rinde para mi caso"</strong>. Esta página cruza el benchmark con requisitos de RAM/VRAM
      reales para Mac M-series, NVIDIA DGX Spark, GPUs dedicadas y servers.
    </p>
    <p class="lead" style="margin-top: 1rem;">
      ⚠️ <strong>Importante</strong>: "open-source" tiene matices. Apache 2.0 (Mistral, Devstral, Qwen
      base, DeepSeek) podés usar comercialmente sin restricción. Llama tiene cláusulas (limitada para 700M+
      MAU). Verificá la licencia para tu caso comercial.
    </p>
    <p class="meta">
      Última actualización: {TODAY} ·
      <a href="https://github.com/ctala/ai-benchmarks-alternativos" target="_blank" rel="noopener">datos abiertos en GitHub</a>
    </p>
  </section>

  <section class="results">
    <div class="results-header">
      <h2>Mejores modelos open-source por hardware</h2>
    </div>

    <h3>Mac M2/M3/M4 con 16GB RAM</h3>
    <table class="results-table">
      <thead><tr><th scope="col">Modelo</th><th scope="col">Quant</th><th scope="col">Score</th><th scope="col">License</th><th scope="col">Notas</th></tr></thead>
      <tbody>
        <tr><td><strong>Devstral Small (24B)</strong></td><td>Q4_K_M (~14GB)</td><td>7.95</td><td>Apache 2.0</td><td>Tight pero corre</td></tr>
        <tr><td><strong>Mistral Small 4 (24B)</strong></td><td>Q4_K_M (~14GB)</td><td>7.62</td><td>Apache 2.0</td><td>Mejor calidad/tamaño</td></tr>
        <tr><td>DeepSeek V4 Flash (236B/21B activos)</td><td>Q4_K_M (~140GB)</td><td>8.28*</td><td>MIT</td><td>* Score cloud, no cabe en 16GB</td></tr>
        <tr><td>Phi-4 (14B)</td><td>Q4_K_M (~9GB)</td><td>—</td><td>MIT</td><td>Excelente para judge tasks</td></tr>
      </tbody>
    </table>

    <h3>Mac M-series 32GB RAM</h3>
    <table class="results-table">
      <thead><tr><th scope="col">Modelo</th><th scope="col">Quant</th><th scope="col">Score</th><th scope="col">License</th><th scope="col">Notas</th></tr></thead>
      <tbody>
        <tr><td><strong>Mistral Small 4 (24B)</strong></td><td>Q5_K_M (~17GB)</td><td>7.62</td><td>Apache 2.0</td><td>Top calidad/recursos</td></tr>
        <tr><td><strong>Devstral 2 (Dic 2025)</strong></td><td>Q5_K_M (~22GB)</td><td>—</td><td>Apache 2.0</td><td>Coding profesional</td></tr>
        <tr><td>Qwen 3.6 35B base</td><td>Q4_K_M (~22GB)</td><td>7.32</td><td>Apache 2.0</td><td>Versatil</td></tr>
        <tr><td>Llama 3.3 70B</td><td>Q3_K_M (~30GB)</td><td>7.70*</td><td>Llama 3</td><td>* Score con Groq, no local</td></tr>
      </tbody>
    </table>

    <h3>NVIDIA DGX Spark (128GB unified) o servers GPU 80GB+</h3>
    <table class="results-table">
      <thead><tr><th scope="col">Modelo</th><th scope="col">Quant</th><th scope="col">Score</th><th scope="col">License</th><th scope="col">Notas</th></tr></thead>
      <tbody>
        <tr><td><strong>DeepSeek V4 Flash</strong></td><td>Q4_K_M (~140GB)</td><td>8.28</td><td>MIT</td><td>Top open-source large</td></tr>
        <tr><td><strong>Qwen 3.6 35B base</strong></td><td>Q5_K_M (~25GB)</td><td>7.32</td><td>Apache 2.0</td><td>Balance calidad/tamaño</td></tr>
        <tr><td><strong>Llama 3.3 70B</strong></td><td>Q5_K_M (~50GB)</td><td>7.70*</td><td>Llama 3</td><td>* Score Groq, local más lento</td></tr>
        <tr><td>Nemotron Ultra 253B</td><td>Q4_K_M (~150GB)</td><td>—</td><td>Open weights</td><td>Demasiado grande para Spark</td></tr>
      </tbody>
    </table>

    <p class="meta">Score = del benchmark cloud. Local con misma quantization da scores similares pero menor velocidad.</p>
  </section>

  <section>
    <h2>¿Qué modelo elegir según tu caso local?</h2>

    <h3>Privacidad de datos crítica (LegalTech, HealthTech)</h3>
    <p>
      <strong>Mistral Small 4</strong> (Apache 2.0) cubre el 80% de casos sin que ningún byte salga
      de tu hardware. Para modelos más grandes con alguna privacidad: <strong>DeepSeek V4 Flash</strong>
      en DGX Spark o server GPU.
    </p>

    <h3>Coding offline para tus proyectos</h3>
    <p>
      <strong>Devstral Small</strong> (24B Apache 2.0) en Mac M-series 16GB+. Para proyectos grandes:
      <strong>Devstral 2</strong> en 32GB+. Ambos optimizados para código.
    </p>

    <h3>Generación de contenido en español sin API costs</h3>
    <p>
      <strong>Qwen 3.6 35B base</strong> (Apache 2.0) en Mac M-series. Para mejor calidad y hardware
      potente: <strong>Qwen 3.5 397B Cloud</strong> via Ollama Cloud (incluido en suscripción ~$30/mes
      sin costo per call). Caso real: Cristian usa este último para
      <a href="https://ecosistemastartup.com" target="_blank" rel="noopener">ecosistemastartup.com</a>.
    </p>

    <h3>Agente N8N self-hosted</h3>
    <p>
      <strong>Mistral Small 4</strong> via Ollama (puerto 11434) — N8N apunta su nodo OpenAI Chat al
      <code>localhost:11434/v1</code>. Cero latencia de red, cero costo per call. Detalles en
      <a href="/modelos-n8n/">modelos para N8N</a>.
    </p>

    <h3>LLM-as-Judge / evaluación de outputs</h3>
    <p>
      <strong>Phi-4</strong> (Microsoft, 14B, MIT) — exactamente lo que usa este benchmark como juez.
      Cero conflicto de interés (no es de ningún proveedor evaluado), cabe en 9GB y la rúbrica está
      en español publicada en el repo.
    </p>
  </section>
"""
    faqs = [
        ("¿Cómo instalo Ollama y descargo un modelo?",
         "Mac/Linux: curl -fsSL https://ollama.com/install.sh | sh. Después ollama pull mistral-small:24b-instruct-2503-q5_K_M. Para correr: ollama run mistral-small. API OpenAI-compatible expuesta en http://localhost:11434/v1."),
        ("¿Qué pasa con la velocidad local vs API?",
         "Local en Mac M3 Max ~30-50 tok/s, en M4 Max ~50-70 tok/s. Comparado con Groq (240+ tok/s) o Gemini Flash (145+ tok/s) es mucho más lento. Pero la latencia de primer token (TTFT) local es 0ms vs ~200-500ms del API — para chat conversacional la sensación es similar."),
        ("¿Open-source local sirve para producción comercial?",
         "Sí, con Apache 2.0/MIT (Mistral, Devstral, Qwen base, DeepSeek, Phi-4). Llama 3 tiene cláusula de >700M MAU pero para 99% de startups latinas no es problema. Verificá siempre la licencia del modelo específico antes de comercializar."),
        ("¿NVIDIA DGX Spark vale la pena para emprendedores?",
         "Depende del volumen. DGX Spark (~$3,000) cuesta ~$80/mes amortizado a 3 años. Si tu uso de API es >$80/mes Y los datos son sensibles, sí. Si es <$50/mes, OpenRouter sigue ganando."),
        ("¿Quantization Q3 vs Q4 vs Q5 — cuánto pierdo?",
         "Q5_K_M: pérdida casi imperceptible (~1-2% en métricas). Q4_K_M: pérdida ~3-5%, balance recomendado. Q3_K_M: pérdida 8-15%, sólo si necesitás meter el modelo en RAM justa. Para casos comerciales, mantenete en Q4 o Q5."),
        ("¿Cómo combino modelos local con APIs cuando local no alcanza?",
         "Pattern de 'fallback chain': tu app intenta local primero (Ollama), si timeout o error cae a API (OpenRouter, Groq). N8N permite esto con nodos If/Error. Ahorra costos en 80% de casos y mantiene robustez."),
    ]
    body += faq_html(faqs)
    body += cta_block([
        '<a href="/alternativas-claude/">alternativas a Claude</a>',
        '<a href="/alternativas-chatgpt/">alternativas a ChatGPT</a>',
        '<a href="/alternativas-gemini/">alternativas a Gemini</a>',
        '<a href="/modelos-n8n/">modelos para N8N</a>',
    ])
    extra = f"<script type=\"application/ld+json\">\n{faq_schema(faqs)}\n</script>"
    return header(title, desc, kw, url, og_alt=og_alt, extra_head=extra) + body + FOOTER


# ---------------------------------------------------------------------------
# Landing: alternativas-deepseek (nueva)
# ---------------------------------------------------------------------------
def gen_alternativas_deepseek(data):
    models = data["models"]
    c = counts(data)
    alts = [m for m in models if m.get("tested") and m.get("score_global", 0) > 0 and "deepseek" not in m["name"].lower()]
    alts = sorted(alts, key=lambda m: -m["score_global"])[:10]

    title = "Alternativas a DeepSeek 2026: 10 modelos con benchmark"
    desc = ("Ranking de alternativas a DeepSeek con datos reales. 144 modelos, 92 testeados, 10.000+ tests. "
            "Filtrá por calidad, costo y velocidad.")
    kw = ("alternativas DeepSeek, DeepSeek vs Claude, DeepSeek vs Qwen, DeepSeek vs Llama, "
          "modelos similares DeepSeek, reemplazo DeepSeek, DeepSeek API alternativa")
    url = f"{SITE}/alternativas-deepseek/"
    og_alt = "Top alternativas a DeepSeek comparadas con benchmark real"

    body = f"""  <section class="hero">
    <h1>Alternativas a DeepSeek: 10 modelos comparados con benchmark real (Junio 2026)</h1>
    <p class="lead">
      DeepSeek lidera el ranking global, pero no es la única opción. Si necesitás diversificar proveedores,
      mejorar latencia o encontrar un modelo con licencia más permisiva, estas son las alternativas reales —
      <strong><!-- AUTO:tested_count -->{c['tested_count']}<!-- /AUTO --> modelos testeados</strong> con LLM-as-Judge Phi-4 local.
    </p>
    <p class="meta">
      Última actualización: {TODAY} ·
      <a href="https://github.com/ctala/ai-benchmarks-alternativos" target="_blank" rel="noopener">datos abiertos en GitHub</a>
    </p>
  </section>

  <section class="results">
    <div class="results-header">
      <h2>Top 10 alternativas a DeepSeek (ranking global)</h2>
      <p class="meta">Score ponderado v3.0: calidad 70% + costo 15% + velocidad 7,5% + latencia 7,5%.</p>
    </div>

    {table_alt(alts, c)}

    <p class="meta">
      Para filtrar por presupuesto, calidad mínima o tarea específica usá la
      <a href="/">calculadora interactiva</a>.
    </p>
  </section>

  <section>
    <h2>¿Por qué buscar alternativas a DeepSeek?</h2>
    <ul>
      <li><strong>Diversificación de proveedor</strong>: no depender de un solo endpoint crítico para tu producto.</li>
      <li><strong>Latencia</strong>: Llama 3.3 70B en Groq entrega 240+ tok/s, ideal para agentes interactivos.</li>
      <li><strong>Licencia</strong>: DeepSeek es MIT, pero si necesitás Apache 2.0, Mistral/Devstral/Qwen base son mejores.</li>
      <li><strong>Contexto y multimodal</strong>: Gemini y Claude dominan contexto largo y visión nativa.</li>
    </ul>

    <h3>Si reemplazás DeepSeek V4 Flash por latencia</h3>
    <p>
      <strong>Llama 4 Scout 17B (Groq)</strong> es la alternativa más rápida (240+ tok/s) con score global 7.76
      y precio similar ($0.11/$0.34).
    </p>

    <h3>Si reemplazás DeepSeek R1 por razonamiento</h3>
    <p>
      <strong>Claude Opus 4.8</strong> y <strong>Hermes 4 70B</strong> cubren reasoning profundo. Devstral Small
      lidera el pilar Razonamiento (8.39) a costo mínimo.
    </p>

    <h3>Si querés alternativa open-source con mejor soporte comercial</h3>
    <p>
      <strong>Qwen3-Coder-Next</strong> (Apache 2.0) y <strong>Mistral Small 4</strong> (Apache 2.0) ofrecen
      ecosistemas más maduros para despliegue empresarial.
    </p>
  </section>
"""
    faqs = [
        ("¿Cuál es la mejor alternativa a DeepSeek V4 Flash?",
         "Para velocidad y costo: Llama 4 Scout 17B (Groq). Para calidad de coding: Qwen3-Coder-Next. Para calidad general sin preocuparte por costo: Claude Opus 4.8."),
        ("¿DeepSeek R1 tiene buena alternativa en razonamiento?",
         "Sí: Claude Opus 4.8, Hermes 4 70B y Devstral Small (que lidera el pilar Razonamiento en el benchmark)."),
        ("¿Las alternativas a DeepSeek son más caras?",
         "Algunas sí, pero no necesariamente mejores. DeepSeek V4 Flash es #1 global porque combina calidad 8.28 con costo $0.10/$0.20. Alternativas con score similar suelen costar más, salvo Llama 4 Scout."),
    ]
    body += faq_html(faqs)
    body += cta_block([
        '<a href="/deepseek-vs-claude/">DeepSeek vs Claude</a>',
        '<a href="/deepseek-vs-gemini/">DeepSeek vs Gemini</a>',
        '<a href="/alternativas-chatgpt/">alternativas a ChatGPT</a>',
        '<a href="/modelos-n8n/">modelos para N8N</a>',
    ])
    extra = f"<script type=\"application/ld+json\">\n{faq_schema(faqs)}\n</script>"
    return header(title, desc, kw, url, og_alt=og_alt, extra_head=extra) + body + FOOTER

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
LANDINGS = [
    ("alternativas-chatgpt", gen_alternativas_chatgpt),
    ("alternativas-claude", gen_alternativas_claude),
    ("alternativas-gemini", gen_alternativas_gemini),
    ("modelos-n8n", gen_modelos_n8n),
    ("modelos-baratos-emprendedores", gen_modelos_baratos),
    ("modelos-open-source-local", gen_modelos_open_source_local),
    ("alternativas-deepseek", gen_alternativas_deepseek),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", help="Generar solo esta landing")
    args = ap.parse_args()
    data = load_data()
    for slug, fn in LANDINGS:
        if args.slug and slug != args.slug:
            continue
        out = fn(data)
        d = DOCS / slug
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(out, encoding="utf-8")
        print(f"✓ {slug} → docs/{slug}/index.html")


if __name__ == "__main__":
    main()
