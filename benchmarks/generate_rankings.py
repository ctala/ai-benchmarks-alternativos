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
)

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
        "intent_kw": "mejor llm para n8n, mejor modelo para agentes, llm para automatizacion, mejor ia para n8n, llm para openclaw",
        "criterion": "pillar", "pillar": "Agentes",
        "case": "agentes y operaciones (multi-turno largo, tool calling y flujos tipo N8N / OpenClaw)",
        "lead": "Para agentes en N8N u OpenClaw lo que importa no es solo \"inteligencia\": es tool calling fiable, "
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
    if crit == "cost":
        base = [m for m in base if (m.get("score_global") or 0) >= cfg.get("min_score", 6.8)]
        return sorted(base, key=lambda m: (m.get("cost_input_per_M") or 99) + (m.get("cost_output_per_M") or 99))
    if crit == "open_source":
        base = [m for m in base if m.get("open_source")]
        return sorted(base, key=lambda m: -(m.get("score_global") or 0))
    return sorted(base, key=lambda m: -(m.get("score_global") or 0))


def score_for(m, cfg):
    return pillar(m, cfg["pillar"]) if cfg["criterion"] == "pillar" else (m.get("score_global") or 0)


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
    return f"""<section>
  <h2>Por qué {esc(top1.get('name'))} lidera</h2>
  <p>{why} Recordá que el ranking pondera calidad + costo + velocidad — no es solo "el más inteligente",
  sino el que mejor rinde en producción para este caso.</p>
  <h3>Alternativas según tu situación</h3>
  <ul>
    {"".join(alts)}
  </ul>
  <p class="meta">El "mejor" depende de tu prioridad real (calidad, costo o velocidad). Ajustá esos pesos en la <a href="/">calculadora</a> para tu caso.</p>
</section>"""


def faq(cfg, ranked):
    top1 = ranked[0]
    return f"""<section class="faq">
  <h2>Preguntas frecuentes</h2>
  <details><summary><strong>¿Cuál es el mejor LLM para {cfg['case'].split('(')[0].strip()} hoy?</strong></summary>
  <p>Según nuestro benchmark, <strong>{esc(top1.get('name'))}</strong> lidera, pero el ranking completo (arriba) te deja
  elegir según tu presupuesto y prioridad. No hay un único "mejor" universal.</p></details>
  <details><summary><strong>¿De dónde salen estos datos?</strong></summary>
  <p>De un benchmark abierto con 8.000+ tests reales y LLM-as-Judge local (Phi-4, Microsoft, sin conflicto de interés).
  Código y resultados en <a href="https://github.com/ctala/ai-benchmarks-alternativos" target="_blank" rel="noopener">GitHub</a>.</p></details>
  <details><summary><strong>¿Cada cuánto se actualiza?</strong></summary>
  <p>Con cada lote de modelos nuevos. La fecha de actualización está al inicio. Filtrá la versión más reciente en la <a href="/">calculadora</a>.</p></details>
</section>"""


def render_ranking(cfg, models):
    ranked = rank_models(models, cfg)
    if not ranked:
        return None
    ranked = ranked[:8]
    url = f"{SITE}/{cfg['slug']}/"
    desc = (f"{cfg['h1']} con 8.000+ tests reales: ranking por {cfg['case']}, costo y velocidad. "
            f"Benchmark abierto en español. #1: {ranked[0].get('name')}.")
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
      <p class="meta">Score por pilar /10. {('Ordenado por el pilar relevante.' if cfg['criterion']=='pillar' else 'Ordenado por '+('costo.' if cfg['criterion']=='cost' else 'score global.'))}</p>
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
