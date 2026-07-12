#!/usr/bin/env python3
"""
Genera páginas pSEO de ranking "Mejor LLM para [caso]" en docs/<slug>/index.html
a partir de docs/data/models.json (data real del benchmark). Reusa el shell y los
helpers de generate_comparison.py (no duplica HTML ni lógica de datos).

Tipo de página distinto a las comparaciones: ranking filtrado por un criterio
(pilar, costo o licencia), no un cara a cara [A] vs [B].

Uso:
    python benchmarks/generate_rankings.py             # todos
    python benchmarks/generate_rankings.py --slug mejor-llm-para-programar
"""
import argparse
from datetime import date
from generate_comparison import (
    load_models, pillar, fmt_cost, esc, row, methodology, page_shell, SITE, DOCS, PILLARS,
    get_counts, fmt_k, get_meta, fmt_pct,
)


# --- Helpers para rankings por suite específica --------------------------------
def suite(m, name: str) -> float:
    return (m.get("score_by_suite") or {}).get(name) or 0

# --- Rankings a generar -------------------------------------------------------
RANKINGS = [
    {
        "slug": "mejor-llm-para-programar",
        "title": "Mejor LLM para programar en 2026: ranking con benchmark real",
        "h1": "Mejor LLM para programar (2026)",
        "intent_kw": "mejor llm para programar, mejor ia para programar, mejor modelo para coding, mejor ia para codigo, llm para programar",
        "criterion": "pillar", "pillar": "Coding",
        "case": "coding (generar código, JSON estructurado y debugging en tareas reales)",
        "lead": "¿Qué modelo de IA conviene para programar en 2026? Lo medimos con tests de coding reales "
                "(plugins, scripts, templates de N8N), no con benchmarks de juguete. Ranking por calidad de código.",
    },
    {
        "slug": "mejor-llm-para-n8n",
        "title": "Mejor LLM para N8N y agentes en 2026: ranking con benchmark real",
        "h1": "Mejor LLM para N8N y agentes (2026)",
        "intent_kw": "mejor llm para n8n, mejor modelo para agentes, llm para automatizacion, mejor ia para n8n, llm para hermes",
        "criterion": "pillar", "pillar": "Agentes",
        "case": "agentes y operaciones (multi-turno largo, tool calling y flujos tipo N8N / Hermes)",
        "lead": "Para agentes en N8N o Hermes lo que importa no es solo \"inteligencia\": es tool calling fiable, "
                "multi-turno y costo por call. Ranking por capacidad agéntica medida en multi-turno real.",
    },
    {
        "slug": "mejor-llm-en-espanol",
        "title": "Mejor LLM para contenido en español en 2026: ranking con benchmark real",
        "h1": "Mejor LLM para contenido en español (2026)",
        "intent_kw": "mejor llm en español, mejor ia para escribir en español, modelo para contenido español, mejor ia para redactar",
        "criterion": "pillar", "pillar": "Contenido",
        "case": "contenido y marketing en español neutro (blogs, copy y textos largos, no traducción del inglés)",
        "lead": "La mayoría de los rankings miden contenido en inglés. Acá medimos español neutro real: blogs, "
                "copy y textos largos. Ranking por calidad de escritura en español.",
    },
    {
        "slug": "mejor-llm-barato",
        "title": "LLM más baratos en 2026 (con buena calidad): ranking con benchmark real",
        "h1": "LLM más baratos con buena calidad (2026)",
        "intent_kw": "llm más barato, modelos de ia baratos, llm economico, mejor llm barato, ia barata para agentes",
        "criterion": "cost", "min_score": 6.8,
        "case": "presupuesto ajustado (mejor relación calidad/precio para volumen real)",
        "lead": "El modelo más caro casi nunca es el que necesitás. Filtramos los que rinden bien (score global ≥ 6,8) "
                "y los ordenamos del más barato al más caro. Ideal para agentes con 1.000+ calls/mes.",
    },
    {
        "slug": "mejor-llm-open-source",
        "title": "Mejor LLM open source en 2026: ranking con benchmark real",
        "h1": "Mejor LLM open source (2026)",
        "intent_kw": "mejor llm open source, mejor modelo open source, llm codigo abierto, mejor ia open source, modelos open source local",
        "criterion": "open_source",
        "case": "open source (pesos abiertos — corrés local o en cualquier provider, sin lock-in)",
        "lead": "Si querés correr local o evitar lock-in, estos son los mejores modelos de pesos abiertos según el "
                "benchmark — ordenados por score global. Verificamos la licencia (cuidado con los \"Plus\" propietarios).",
    },
    {
        "slug": "mejor-llm-para-razonamiento",
        "title": "Mejor LLM para razonamiento 2026: ranking con benchmark",
        "h1": "Mejor LLM para razonamiento (2026)",
        "intent_kw": "mejor llm para razonamiento, mejor ia para razonar, modelo razonamiento logico, llm razonamiento matematico",
        "criterion": "pillar", "pillar": "Razonamiento",
        "case": "razonamiento (math, lógica y planning)",
        "lead": "¿Qué modelo de IA razona mejor en 2026? Ranking por el pilar de razonamiento del benchmark: "
                "matemáticas, lógica formal, análisis causal y planificación multi-paso en español.",
    },
    {
        "slug": "mejor-llm-para-contenido",
        "title": "Mejor LLM para contenido y marketing en 2026: ranking con benchmark real",
        "h1": "Mejor LLM para contenido y marketing (2026)",
        "intent_kw": "mejor llm para contenido, mejor ia para marketing, modelo para escribir blogs, mejor ia para copywriting, llm para contenido",
        "criterion": "pillar", "pillar": "Contenido",
        "case": "contenido y marketing (blogs, copy, newsletters y textos largos en español neutro)",
        "lead": "¿Qué modelo escribe mejor contenido en español en 2026? Ranking por el pilar de contenido del benchmark: "
                "blogs, copy, newsletters y textos largos con tono natural para hispanohablantes.",
    },
    {
        "slug": "mejor-llm-para-agentes",
        "title": "Mejor LLM para agentes y automatizaciones en 2026: ranking con benchmark",
        "h1": "Mejor LLM para agentes y automatizaciones (2026)",
        "intent_kw": "mejor llm para agentes, mejor ia para automatizacion, modelo para n8n, llm para hermes, agentes ia 2026",
        "criterion": "pillar", "pillar": "Agentes",
        "case": "agentes y operaciones (multi-turno, tool calling y orquestación de flujos)",
        "lead": "Para agentes y flujos automatizados no alcanza con 'inteligencia': importa multi-turno estable, "
                "tool calling confiable y costo por conversación. Ranking por el pilar Agentes.",
    },
    {
        "slug": "mejor-llm-para-tool-calling",
        "title": "Mejor LLM para tool calling en 2026: ranking con benchmark real",
        "h1": "Mejor LLM para tool calling (2026)",
        "intent_kw": "mejor llm para tool calling, mejor ia para funciones, modelo para llamar apis, llm function calling, agentes tool use",
        "criterion": "suite", "suite": "tool_calling",
        "case": "tool calling (llamada correcta de funciones y estructura JSON fiable)",
        "lead": "El tool calling puede arruinar un agente: una función mal llamada es peor que una respuesta lenta. "
                "Ranking por la suite específica de tool calling del benchmark.",
    },
    {
        "slug": "mejor-llm-para-resumir-textos",
        "title": "Mejor LLM para resumir textos en 2026: ranking con benchmark",
        "h1": "Mejor LLM para resumir textos (2026)",
        "intent_kw": "mejor llm para resumir, mejor ia para resumir textos, modelo para summarization, resumen automatico ia, llm resumen",
        "criterion": "suite", "suite": "summarization",
        "case": "summarization (resumir textos largos sin perder información clave)",
        "lead": "Resumir no es solo acortar: es conservar lo importante y descartar el ruido. "
                "Ranking por la suite de summarization del benchmark.",
    },
]


def has_pillars(m):
    return sum((m.get("score_by_pillar") or {}).get(p) or 0 for p in PILLARS) > 0


def rank_models(models, cfg):
    # ≥50 runs (estándar del benchmark) → un outlier con 3-12 runs no lidera por azar
    base = [m for m in models if (m.get("score_global") or 0) > 0 and (m.get("runs") or 0) >= 50 and has_pillars(m)]
    crit = cfg["criterion"]
    if crit == "pillar":
        pil = cfg["pillar"]
        base = [m for m in base if pillar(m, pil) > 0]
        return sorted(base, key=lambda m: -pillar(m, pil))
    if crit == "suite":
        sname = cfg["suite"]
        base = [m for m in base if suite(m, sname) > 0]
        return sorted(base, key=lambda m: -suite(m, sname))
    if crit == "cost":
        base = [m for m in base if (m.get("score_global") or 0) >= cfg.get("min_score", 6.8)]
        return sorted(base, key=lambda m: (m.get("cost_input_per_M") or 99) + (m.get("cost_output_per_M") or 99))
    if crit == "open_source":
        base = [m for m in base if m.get("open_source")]
        return sorted(base, key=lambda m: -(m.get("score_global") or 0))
    return sorted(base, key=lambda m: -(m.get("score_global") or 0))


def score_for(m, cfg):
    if cfg["criterion"] == "pillar":
        return pillar(m, cfg["pillar"])
    if cfg["criterion"] == "suite":
        return suite(m, cfg["suite"])
    return m.get("score_global") or 0


def analysis(cfg, ranked):
    top1 = ranked[0]
    rest = ranked[1:3]
    s1 = score_for(top1, cfg)
    why = (f"<strong>{esc(top1.get('name'))}</strong> encabeza el ranking para {cfg['case']} "
           f"con {s1:.1f}/10, a {fmt_cost(top1)} por millón de tokens "
           f"({round(top1.get('tokens_per_second') or 0)} tok/s, {esc(top1.get('provider',''))}).")
    alts = []
    for m in rest:
        tag = "open source" if m.get("open_source") else "propietario"
        alts.append(f"<li><strong>{esc(m.get('name'))}</strong> ({score_for(m, cfg):.1f}/10, {fmt_cost(m)}, {tag}) — "
                    f"buena alternativa si {'querés pesos abiertos' if m.get('open_source') else 'ya está en tu stack o priorizás otro factor'}.</li>")
    w = get_meta().get("default_weights", {})
    q = fmt_pct(w.get("quality", 0.7))
    co = fmt_pct(w.get("cost", 0.15))
    sp = fmt_pct(w.get("speed", 0.075))
    la = fmt_pct(w.get("latency", 0.075))
    return f"""<section>
  <h2>Por qué {esc(top1.get('name'))} lidera</h2>
  <p>{why} Recordá que el score global v3.0 pondera calidad {q}% + costo {co}% + velocidad {sp}% + latencia {la}% — no es solo "el más inteligente",
  sino el que mejor rinde en producción para este caso.</p>
  <h3>Alternativas según tu situación</h3>
  <ul>
    {"".join(alts)}
  </ul>
  <p class="meta">El "mejor" depende de tu prioridad real (calidad, costo o velocidad). Ajustá esos pesos en la <a href="/">calculadora</a> para tu caso.</p>
</section>"""


def faq(cfg, ranked):
    top1 = ranked[0]
    tests_k = fmt_k(get_counts()["total_runs"])
    label = cfg['case'].split('(')[0].strip()
    qas = [
        (
            f"¿Cuál es el mejor LLM para {label} hoy?",
            f"Según nuestro benchmark, {top1.get('name')} lidera, pero el ranking completo te deja "
            "elegir según tu presupuesto y prioridad. No hay un único 'mejor' universal.",
            f"Según nuestro benchmark, <strong>{esc(top1.get('name'))}</strong> lidera, pero el ranking completo (arriba) te deja\n  "
            "elegir según tu presupuesto y prioridad. No hay un único \"mejor\" universal.",
        ),
        (
            "¿De dónde salen estos datos?",
            f"De un benchmark abierto con {tests_k} runs reales y LLM-as-Judge local (Phi-4, Microsoft, sin conflicto de interés). "
            "Código y resultados en GitHub.",
            f"De un benchmark abierto con {tests_k} runs reales y LLM-as-Judge local (Phi-4, Microsoft, sin conflicto de interés). "
            "Código y resultados en <a href=\"https://github.com/ctala/ai-benchmarks-alternativos\" target=\"_blank\" rel=\"noopener\">GitHub</a>.",
        ),
        (
            "¿Cada cuánto se actualiza?",
            "Con cada lote de modelos nuevos. La fecha de actualización está al inicio. Filtrá la versión más reciente en la calculadora.",
            "Con cada lote de modelos nuevos. La fecha de actualización está al inicio. Filtrá la versión más reciente en la <a href=\"/\">calculadora</a>.",
        ),
    ]
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a_plain}}
            for q, a_plain, _ in qas
        ],
    }
    import json
    schema_script = f'<script type="application/ld+json">\n{json.dumps(schema, ensure_ascii=False, indent=2)}\n</script>'
    details = "\n  ".join(
        f'<details><summary><strong>{esc(q)}</strong></summary>\n  <p>{a_html}</p></details>'
        for q, _, a_html in qas
    )
    return f"""<section class="faq">
  {schema_script}
  <h2>Preguntas frecuentes</h2>
  {details}
</section>"""


def render_ranking(cfg, models):
    ranked = rank_models(models, cfg)
    if not ranked:
        return None
    ranked = ranked[:8]
    url = f"{SITE}/{cfg['slug']}/"
    tests_k = fmt_k(get_counts()["total_runs"])
    desc = (f"{cfg['h1']} con {tests_k} runs reales: ranking por {cfg['case']}. "
            f"Benchmark abierto. #1: {ranked[0].get('name')}.")
    today = date.today().isoformat()
    rows = "\n        ".join(row(i + 1, m, top=(i == 0)) for i, m in enumerate(ranked))
    body = f"""  <section class="hero">
    <h1>{esc(cfg['h1'])}</h1>
    <p class="lead">{cfg['lead']}</p>
    <p class="meta">Última actualización: {today} ·
    <a href="https://github.com/ctala/ai-benchmarks-alternativos" target="_blank" rel="noopener">datos abiertos en GitHub</a></p>
  </section>
  <section class="results">
    <div class="results-header">
      <h2>Ranking: {esc(cfg['h1'])}</h2>
      <p class="meta">{({'pillar':'Score por pilar /10.','suite':'Score por suite /10.','cost':'Ordenado por costo.','open_source':'Ordenado por score global.'}[cfg['criterion']])} {('Ordenado por el pilar relevante.' if cfg['criterion']=='pillar' else ('Ordenado por la suite relevante.' if cfg['criterion']=='suite' else ''))}</p>
    </div>
    <table class="results-table">
      <thead>
        <tr><th scope="col">#</th><th scope="col">Modelo</th><th scope="col">Global</th><th scope="col">Coding</th><th scope="col">Contenido</th><th scope="col">Razon.</th><th scope="col">Agentes</th><th scope="col">$ in/out per M</th><th scope="col">Velocidad</th></tr>
      </thead>
      <tbody>
        {rows}
      </tbody>
    </table>
    <p class="meta">Filtrá por presupuesto, calidad mínima o tarea en la <a href="/">calculadora interactiva</a>.</p>
  </section>
  {methodology()}
  {analysis(cfg, ranked)}
  {faq(cfg, ranked)}
  <section class="cta-block">
    <h2>Probá la calculadora con tu caso real</h2>
    <p>Ajustá presupuesto, calidad mínima y tipo de tarea sobre 100+ modelos. En 30 segundos tenés tu ranking personalizado.</p>
    <a href="/" class="cta-primary">Ir a la calculadora →</a>
  </section>"""
    return page_shell(cfg["title"], desc, cfg["intent_kw"], url, body)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug")
    args = ap.parse_args()
    models = load_models()
    for cfg in RANKINGS:
        if args.slug and cfg["slug"] != args.slug:
            continue
        out = render_ranking(cfg, models)
        if not out:
            print(f"⚠️  {cfg['slug']}: sin modelos para el criterio")
            continue
        d = DOCS / cfg["slug"]
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(out, encoding="utf-8")
        n = len(rank_models(models, cfg)[:8])
        print(f"✓ {cfg['slug']}: top {n} → docs/{cfg['slug']}/index.html")


if __name__ == "__main__":
    main()
