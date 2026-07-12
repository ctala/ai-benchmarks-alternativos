#!/usr/bin/env python3
"""
Genera páginas pSEO de ranking "Mejor LLM para [caso]" en docs/<slug>/index.html
a partir de docs/data/models.json (data real del benchmark). Reusa el shell y los
helpers de generate_comparison.py (no duplica HTML ni lógica de datos).

Tipo de página distinto a las comparaciones: ranking filtrado por un criterio
(pilar, suite, costo o licencia), no un cara a cara [A] vs [B].

IMPORTANTE: cada vez que se agreguen modelos nuevos o cambien los scores,
volver a correr este script para mantener actualizados los rankings por
dimensión individual. También se puede usar el pipeline maestro
regenerate_all.py.

Uso:
    python benchmarks/generate_rankings.py             # todos
    python benchmarks/generate_rankings.py --slug mejor-llm-para-programar
"""
import argparse
import json
from datetime import date
from generate_comparison import (
    load_models, pillar, fmt_cost, esc, methodology, page_shell, SITE, DOCS, PILLARS,
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
        "what": "coding",
        "lead": "¿Qué modelo de IA conviene para programar en 2026? Lo medimos con tests de coding reales "
                "(plugins, scripts, templates de N8N), no con benchmarks de juguete. Ranking por calidad de código.",
        "use_cases": ["plugins WordPress", "scripts Python y Bash", "templates JSON para N8N", "debugging de errores reales", "refactor de código existente"],
        "why": "En producción el código tiene que compilar, integrarse con tu stack y mantenerse. Un modelo que genera código elegante pero con errores de sintaxis o que no respeta tu API te cuesta más tiempo del que ahorra.",
        "related": ["modelos-n8n", "mejor-llm-para-tool-calling", "alternativas-claude"],
    },
    {
        "slug": "mejor-llm-para-n8n",
        "title": "Mejor LLM para N8N y agentes en 2026: ranking con benchmark real",
        "h1": "Mejor LLM para N8N y agentes (2026)",
        "intent_kw": "mejor llm para n8n, mejor modelo para agentes, llm para automatizacion, mejor ia para n8n, llm para hermes",
        "criterion": "pillar", "pillar": "Agentes",
        "case": "agentes y operaciones (multi-turno largo, tool calling y flujos tipo N8N / Hermes)",
        "what": "agentes y operaciones",
        "lead": "Para agentes en N8N o Hermes lo que importa no es solo \"inteligencia\": es tool calling fiable, "
                "multi-turno y costo por call. Ranking por capacidad agéntica medida en multi-turno real.",
        "use_cases": ["workflows de N8N", "agentes Hermes", "chatbots de soporte", "orquestación multi-paso", "extracción de datos con herramientas"],
        "why": "Un agente que falla en el tercer turno o llama mal una función genera más trabajo manual que hacer la tarea a mano. Acá medimos estabilidad multi-turno y adherencia a schemas.",
        "related": ["mejor-llm-para-tool-calling", "modelos-n8n", "mejor-llm-para-agentes"],
    },
    {
        "slug": "mejor-llm-en-espanol",
        "title": "Mejor LLM para contenido en español en 2026: ranking con benchmark real",
        "h1": "Mejor LLM para contenido en español (2026)",
        "intent_kw": "mejor llm en español, mejor ia para escribir en español, modelo para contenido español, mejor ia para redactar",
        "criterion": "pillar", "pillar": "Contenido",
        "case": "contenido y marketing en español neutro (blogs, copy y textos largos, no traducción del inglés)",
        "what": "contenido en español",
        "lead": "La mayoría de los rankings miden contenido en inglés. Acá medimos español neutro real: blogs, "
                "copy y textos largos. Ranking por calidad de escritura en español.",
        "use_cases": ["blogs técnicos", "newsletters", "copy de landing pages", "posts para redes", "documentación en español"],
        "why": "Muchos modelos suenan bien en inglés pero traducen mal al español o usan modismos que no funcionan en toda Latinoamérica. Medimos español neutro, tecnicismos y estructura.",
        "related": ["mejor-llm-para-contenido", "alternativas-chatgpt", "modelos-baratos-emprendedores"],
    },
    {
        "slug": "mejor-llm-barato",
        "title": "LLM más baratos en 2026 (con buena calidad): ranking con benchmark real",
        "h1": "LLM más baratos con buena calidad (2026)",
        "intent_kw": "llm más barato, modelos de ia baratos, llm economico, mejor llm barato, ia barata para agentes",
        "criterion": "cost", "min_score": 6.8,
        "case": "presupuesto ajustado (mejor relación calidad/precio para volumen real)",
        "what": "relación calidad/precio",
        "lead": "El modelo más caro casi nunca es el que necesitás. Filtramos los que rinden bien (score global ≥ 6,8) "
                "y los ordenamos del más barato al más caro. Ideal para agentes con 1.000+ calls/mes.",
        "use_cases": ["agentes con alto volumen", "startups con presupuesto ajustado", "procesamiento batch", "prototipos que escalan", "calls diarios masivos"],
        "why": "Cuando pasás de cientos a miles de calls por mes, el costo por millón de tokens pasa a ser más importante que ganar 0.2 puntos de calidad. El ranking refleja eso.",
        "related": ["modelos-baratos-emprendedores", "mejor-llm-para-n8n", "mejor-llm-open-source"],
    },
    {
        "slug": "mejor-llm-open-source",
        "title": "Mejor LLM open source en 2026: ranking con benchmark real",
        "h1": "Mejor LLM open source (2026)",
        "intent_kw": "mejor llm open source, mejor modelo open source, llm codigo abierto, mejor ia open source, modelos open source local",
        "criterion": "open_source",
        "case": "open source (pesos abiertos — corrés local o en cualquier provider, sin lock-in)",
        "what": "modelos open source",
        "lead": "Si querés correr local o evitar lock-in, estos son los mejores modelos de pesos abiertos según el "
                "benchmark — ordenados por score global. Verificamos la licencia (cuidado con los \"Plus\" propietarios).",
        "use_cases": ["ejecución local", "privacidad de datos", "evitar vendor lock-in", "finetuning propio", "deploy en infraestructura propia"],
        "why": "Open source no es solo filosofía: es soberanía sobre tus datos, costos predecibles y la posibilidad de correr local cuando la privacidad lo exige.",
        "related": ["modelos-open-source-local", "qwen-vs-llama", "mejor-llm-barato"],
    },
    {
        "slug": "mejor-llm-para-razonamiento",
        "title": "Mejor LLM para razonamiento 2026: ranking con benchmark",
        "h1": "Mejor LLM para razonamiento (2026)",
        "intent_kw": "mejor llm para razonamiento, mejor ia para razonar, modelo razonamiento logico, llm razonamiento matematico",
        "criterion": "pillar", "pillar": "Razonamiento",
        "case": "razonamiento (math, lógica y planning)",
        "what": "razonamiento",
        "lead": "¿Qué modelo de IA razona mejor en 2026? Ranking por el pilar de razonamiento del benchmark: "
                "matemáticas, lógica formal, análisis causal y planificación multi-paso en español.",
        "use_cases": ["análisis de negocio", "matemáticas y lógica formal", "planificación con restricciones", "resúmenes ejecutivos con inferencias", "toma de decisiones estructurada"],
        "why": "Para tareas de razonamiento no sirve una respuesta que suena bien pero es incorrecta. Medimos precisión lógica, coherencia causal y capacidad de mantener el hilo en problemas complejos.",
        "related": ["mejor-llm-para-resumir-textos", "gpt-5.6-vs-claude-opus-4-8", "alternativas-chatgpt"],
    },
    {
        "slug": "mejor-llm-para-contenido",
        "title": "Mejor LLM para contenido y marketing en 2026: ranking con benchmark real",
        "h1": "Mejor LLM para contenido y marketing (2026)",
        "intent_kw": "mejor llm para contenido, mejor ia para marketing, modelo para escribir blogs, mejor ia para copywriting, llm para contenido",
        "criterion": "pillar", "pillar": "Contenido",
        "case": "contenido y marketing (blogs, copy, newsletters y textos largos en español neutro)",
        "what": "contenido y marketing",
        "lead": "¿Qué modelo escribe mejor contenido en español en 2026? Ranking por el pilar de contenido del benchmark: "
                "blogs, copy, newsletters y textos largos con tono natural para hispanohablantes.",
        "use_cases": ["blogs SEO", "copy de marketing", "newsletters B2B", "posts para redes sociales", "guiones y presentaciones"],
        "why": "El contenido genérico no vende ni posiciona. Medimos estructura, tono natural, uso correcto de tecnicismos y capacidad de seguir instrucciones de estilo en español neutro.",
        "related": ["mejor-llm-en-espanol", "modelos-baratos-emprendedores", "alternativas-chatgpt"],
    },
    {
        "slug": "mejor-llm-para-agentes",
        "title": "Mejor LLM para agentes y automatizaciones en 2026: ranking con benchmark",
        "h1": "Mejor LLM para agentes y automatizaciones (2026)",
        "intent_kw": "mejor llm para agentes, mejor ia para automatizacion, modelo para n8n, llm para hermes, agentes ia 2026",
        "criterion": "pillar", "pillar": "Agentes",
        "case": "agentes y operaciones (multi-turno, tool calling y orquestación de flujos)",
        "what": "agentes y operaciones",
        "lead": "Para agentes y flujos automatizados no alcanza con 'inteligencia': importa multi-turno estable, "
                "tool calling confiable y costo por conversación. Ranking por el pilar Agentes.",
        "use_cases": ["agentes autónomos", "workflows multi-step", "soporte al cliente", "extracción con herramientas", "routing y clasificación"],
        "why": "Un agente es una cadena de decisiones. Si falla en el segundo o tercer paso, todo el flujo se rompe. Medimos estabilidad multi-turno, coherencia de estado y uso correcto de herramientas.",
        "related": ["mejor-llm-para-n8n", "mejor-llm-para-tool-calling", "alternativas-claude"],
    },
    {
        "slug": "mejor-llm-para-tool-calling",
        "title": "Mejor LLM para tool calling en 2026: ranking con benchmark real",
        "h1": "Mejor LLM para tool calling (2026)",
        "intent_kw": "mejor llm para tool calling, mejor ia para funciones, modelo para llamar apis, llm function calling, agentes tool use",
        "criterion": "suite", "suite": "tool_calling",
        "case": "tool calling (llamada correcta de funciones y estructura JSON fiable)",
        "what": "tool calling",
        "lead": "El tool calling puede arruinar un agente: una función mal llamada es peor que una respuesta lenta. "
                "Ranking por la suite específica de tool calling del benchmark.",
        "use_cases": ["llamadas a APIs externas", "agentes con funciones definidas", "workflows N8N/Hermes", "validación de schemas JSON", "extracción estructurada"],
        "why": "El 80% de los errores de un agente viene de tool calling malformado: parámetros incorrectos, funciones inventadas o JSON roto. Medimos exactitud en la invocación, no solo si el modelo dice que soporta herramientas.",
        "related": ["mejor-llm-para-n8n", "mejor-llm-para-agentes", "modelos-n8n"],
    },
    {
        "slug": "mejor-llm-para-resumir-textos",
        "title": "Mejor LLM para resumir textos en 2026: ranking con benchmark",
        "h1": "Mejor LLM para resumir textos (2026)",
        "intent_kw": "mejor llm para resumir, mejor ia para resumir textos, modelo para summarization, resumen automatico ia, llm resumen",
        "criterion": "suite", "suite": "summarization",
        "case": "summarization (resumir textos largos sin perder información clave)",
        "what": "summarization",
        "lead": "Resumir no es solo acortar: es conservar lo importante y descartar el ruido. "
                "Ranking por la suite de summarization del benchmark.",
        "use_cases": ["resumen de documentos largos", "síntesis de reuniones", "abstracts", "digest de noticias", "resumen de soporte al cliente"],
        "why": "Un mal resumen pierde datos críticos o inventa conclusiones. Medimos fidelidad al original, compresión proporcional y coherencia del resumen en español.",
        "related": ["mejor-llm-para-razonamiento", "alternativas-claude", "mejor-llm-para-contenido"],
    },
]


# --- Modelos frontier que el usuario suele buscar -----------------------------
FRONTIER_PATTERNS = {
    "GPT-5.6 Luna": ["gpt-5.6-luna"],
    "GPT-5.6 Terra": ["gpt-5.6-terra"],
    "GPT-5.6 Sol": ["gpt-5.6-sol"],
    "Claude Opus 4.8": ["claude-opus-4.8"],
    "Claude Fable 5": ["claude-fable-5"],
    "Grok 4.5": ["grok-4.5"],
    "GPT-5.5": ["gpt-5.5"],
}


def has_pillars(m):
    return sum((m.get("score_by_pillar") or {}).get(p) or 0 for p in PILLARS) > 0


def rank_models(models, cfg):
    # ≥50 runs (estándar del benchmark) → un outlier con 3-12 runs no lidera por azar
    base = [m for m in models if (m.get("score_global") or 0) > 0 and (m.get("runs") or 0) >= 50 and has_pillars(m)]
    crit = cfg["criterion"]
    if crit == "pillar":
        pil = cfg["pillar"]
        # Ordena por CAPACIDAD en la tarea, no por el compuesto con costo/velocidad.
        # Ver pillar_quality() para por qué.
        base = [m for m in base if pillar_quality(m, pil) > 0]
        return sorted(base, key=lambda m: -pillar_quality(m, pil))
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


def pillar_quality(m, name):
    """Capacidad PURA del modelo en ese pilar. Sin costo, sin velocidad, sin latencia.

    Alguien que busca "mejor LLM para contenido" pregunta quien ESCRIBE MEJOR, no
    quien tiene mejor relacion calidad/precio. Ordenar esa pagina por un compuesto
    que incluye costo y velocidad responde otra pregunta -- y respondia mal:

      "mejor llm para contenido" ordenado por el compuesto:  1. GPT-OSS 20B (Groq)
      ordenado por capacidad real de escribir:               1. MiniMax M3 (9.17)

    El compuesto coronaba a los modelos rapidos y baratos de Groq en una pagina que
    promete decir quien escribe mejor, y hundia al #6 a DeepSeek V4 Flash, que tenia
    la mejor calidad de contenido del lote. Mismo efecto en Agentes: Llama 3.1 8B
    aparecia sobre Opus 4.8 -- no por ser mejor agente, sino por ser barato y rapido.

    El costo NO desaparece: se muestra como columna, y el veredicto de bandas dice
    "de los que empatan en capacidad, el mas barato es X". Primero se mide el poder;
    despues se decide con el precio. En ese orden.
    """
    return ((m.get("dims_by_pillar") or {}).get(name) or {}).get("quality_avg") or 0


def score_for(m, cfg):
    if cfg["criterion"] == "pillar":
        return pillar_quality(m, cfg["pillar"])
    if cfg["criterion"] == "suite":
        return suite(m, cfg["suite"])
    return m.get("score_global") or 0


def score_label(cfg):
    if cfg["criterion"] == "pillar":
        return f"Calidad en {cfg['pillar']}"   # capacidad pura, sin costo ni velocidad
    if cfg["criterion"] == "suite":
        return cfg["suite"].replace("_", " ").title()
    return "Score global"


def table_head(cfg):
    base_cols = '<th scope="col">#</th><th scope="col">Modelo</th>'
    if cfg["criterion"] == "suite":
        # La suite no está en los 4 pilares, así que va una columna aparte.
        base_cols += f'<th scope="col">{esc(score_label(cfg))}</th>'
    elif cfg["criterion"] == "pillar":
        # Para pilares, la columna del pilar relevante ya está entre Coding/Contenido/Razon./Agentes.
        pass
    else:
        base_cols += '<th scope="col">Global</th>'
    base_cols += '<th scope="col">Coding</th><th scope="col">Contenido</th><th scope="col">Razon.</th><th scope="col">Agentes</th>'
    base_cols += '<th scope="col">$ in/out per M</th><th scope="col">Velocidad</th>'
    return f'<div class="table-scroll"><table class="results-table">\n      <thead>\n        <tr>{base_cols}</tr>\n      </thead>'


def row_ranking(rank, m, cfg, top=False):
    """Fila de tabla que incluye la columna del score relevante para el ranking."""
    nm = f"<strong>{esc(m.get('name'))}</strong>" if top else esc(m.get("name"))
    relevant = score_for(m, cfg)
    if cfg["criterion"] == "suite":
        # Ranking por suite: mostrar score de la suite + pilares auxiliares.
        return (f"<tr><td>{rank}</td><td>{nm}</td><td>{relevant:.1f}</td>"
                f"<td>{pcell(m,'Coding')}</td><td>{pcell(m,'Contenido')}</td>"
                f"<td>{pcell(m,'Razonamiento')}</td><td>{pcell(m,'Agentes')}</td>"
                f"<td>{fmt_cost(m)}</td><td>{round(m.get('tokens_per_second') or 0)} tok/s</td></tr>")
    # Ranking por pilar/costo/open_source: solo pilares y global (si aplica).
    global_col = f"<td>{m.get('score_global',0):.2f}</td>" if cfg["criterion"] != "pillar" else ""
    return (f"<tr><td>{rank}</td><td>{nm}</td>{global_col}"
            f"<td>{pcell(m,'Coding')}</td><td>{pcell(m,'Contenido')}</td>"
            f"<td>{pcell(m,'Razonamiento')}</td><td>{pcell(m,'Agentes')}</td>"
            f"<td>{fmt_cost(m)}</td><td>{round(m.get('tokens_per_second') or 0)} tok/s</td></tr>")


def pcell(m, p):
    """Celda de pilar = CALIDAD en ese pilar (capacidad), no el compuesto con costo.

    Antes mostraba score_by_pillar (compuesto): la fila decía 7.1 para un modelo cuya
    calidad real escribiendo era 9.17. La tabla contradecía su propio encabezado.
    """
    v = pillar_quality(m, p)
    return f"{v:.1f}" if v > 0 else "—"


def cost_for_calls(m, calls=1000, in_tok=300, out_tok=1500):
    """Costo estimado en USD para N calls con los tokens por call por defecto del benchmark."""
    if not m:
        return 0.0
    cost_per_call = (in_tok * (m.get("cost_input_per_M") or 0) + out_tok * (m.get("cost_output_per_M") or 0)) / 1_000_000
    return cost_per_call * calls


def fmt_usd(n):
    if n >= 100:
        return f"${n:,.0f}"
    return f"${n:.2f}"


def reading_guide(cfg, ranked):
    top1 = ranked[0]
    second = ranked[1] if len(ranked) > 1 else None
    diff = score_for(top1, cfg) - score_for(second, cfg) if second else 0
    s1 = score_for(top1, cfg)
    if diff >= 0.5:
        gap_text = f"<strong>{esc(top1.get('name'))}</strong> lidera con una ventaja clara ({s1:.1f}/10 vs {score_for(second, cfg):.1f}/10)"
    elif diff >= 0.2:
        gap_text = f"<strong>{esc(top1.get('name'))}</strong> lidera, pero la diferencia con el segundo es pequeña ({s1:.1f}/10 vs {score_for(second, cfg):.1f}/10)"
    else:
        gap_text = f"hay empate técnico en la cima (todos rondan los {s1:.1f}/10): el mejor depende de tu prioridad"
    cases = ", ".join(cfg["use_cases"])
    return f"""<section>
  <h2>Cómo interpretar este ranking de {esc(cfg['what'])}</h2>
  <p>Este ranking no mide "inteligencia general" ni el score global ponderado. Mide qué modelo rinde mejor para
  <strong>{esc(cfg['what'])}</strong> en casos reales: {cases}. El orden depende únicamente del score de esa
  tarea puntual, no del costo, la velocidad ni la latencia.</p>
  <p>En esta dimensión {gap_text}. Eso no significa que sea el único
  válido: si tu prioridad es costo, velocidad o privacidad, el orden puede cambiar. El score global del benchmark
  pondera calidad 70% + costo 15% + velocidad 7,5% + latencia 7,5%, pero acá estamos mirando solo la calidad de la
  tarea. Ajustá esos pesos en la <a href="/">calculadora</a> para tu caso.</p>
  <p>Los modelos que aparecen tienen al menos 50 runs, lo que reduce el ruido de outlier con poca muestra.</p>
</section>"""


def top3_explained(cfg, ranked):
    parts = []
    for i, m in enumerate(ranked[:3], 1):
        score = score_for(m, cfg)
        provider = esc(m.get("provider", ""))
        oss = "open source" if m.get("open_source") else "propietario"
        if i == 1:
            angle = "Es la opción a vencer en esta dimensión"
        elif i == 2:
            angle = "Es la alternativa más sólida si el primero no encaja en tu stack"
        else:
            angle = "Es una tercera opción competitiva, especialmente si valorás otro factor además de la calidad pura"
        closing = ". Tiene pesos abiertos, así que podés correrlo en varios providers o local." if m.get('open_source') else ". Es propietario, pero puede valer la pena si ya integraste su ecosistema."
        parts.append(f"""  <h3>{i}. {esc(m.get('name'))} — {score:.1f}/10</h3>
  <p>{esc(m.get('name'))} ({provider}, {oss}) cuesta {fmt_cost(m)} por millón de tokens y rinde a
  {round(m.get('tokens_per_second') or 0)} tok/s. Su score en {esc(score_label(cfg))} es {score:.1f}/10.
  {angle}{closing}</p>""")
    return f"""<section>
  <h2>Top 3 explicado: por qué están arriba</h2>
{chr(10).join(parts)}
</section>"""


def cost_comparison(cfg, ranked):
    top3 = ranked[:3]
    rows = []
    for m in top3:
        cost_1k = cost_for_calls(m, 1000)
        cost_10k = cost_for_calls(m, 10000)
        rows.append(f"<tr><td>{esc(m.get('name'))}</td><td>{fmt_cost(m)}</td><td>{fmt_usd(cost_1k)}</td><td>{fmt_usd(cost_10k)}</td></tr>")
    return f"""<section class="results">
  <div class="results-header"><h2>Costo real para volumen</h2></div>
  <p>Estimación para 1.000 y 10.000 calls/mes (asumiendo 300 tokens de input y 1.500 de output por call, promedio del benchmark):</p>
  <div class="table-scroll"><table class="results-table">
    <thead><tr><th scope="col">Modelo</th><th scope="col">$ por M tokens</th><th scope="col">1.000 calls/mes</th><th scope="col">10.000 calls/mes</th></tr></thead>
    <tbody>
      {''.join(rows)}
    </tbody>
  </table></div>
  <p class="meta">Para volumen alto, un modelo 2× más barato puede ahorrarte más de lo que pierdes en calidad. Validá con tu caso real en la <a href="/">calculadora</a>.</p>
</section>"""


def frontier_in_dimension(cfg, models):
    """Menciona dónde quedan los modelos frontier en esta dimensión."""
    ranked = rank_models(models, cfg)
    by_name = {}
    for label, patterns in FRONTIER_PATTERNS.items():
        for m in models:
            blob = f"{m.get('name','')} {m.get('key','')}".lower()
            if any(p in blob for p in patterns):
                if m.get("score_global") and (m.get("runs") or 0) >= 50:
                    by_name[label] = m
                    break
    if not by_name:
        return ""
    items = []
    for label, m in sorted(by_name.items()):
        pos = next((i + 1 for i, x in enumerate(ranked) if x.get("key") == m.get("key")), None)
        score = score_for(m, cfg)
        if pos and pos <= 10:
            text = f"<strong>{esc(label)}</strong> está en el top 10 (#{pos}) con {score:.1f}/10."
        elif pos:
            text = f"<strong>{esc(label)}</strong> queda #{pos} con {score:.1f}/10."
        else:
            text = f"<strong>{esc(label)}</strong> no califica en este filtro (score {score:.1f}/10 o runs insuficientes)."
        items.append(f"<li>{text} Cuesta {fmt_cost(m)} por millón.</li>")
    return f"""<section>
  <h2>¿Dónde quedan los modelos frontier?</h2>
  <p>Muchos lectores buscan comparar GPT-5.6, Claude Opus/Fable o Grok. En esta dimensión estos son sus scores reales del benchmark:</p>
  <ul>
    {''.join(items)}
  </ul>
  <p class="meta">Si te interesa una comparación cara a cara, probá las <a href="/gpt-5.6-vs-claude-opus-4-8/">comparativas específicas</a> o ajustá los pesos en la calculadora.</p>
</section>"""


RELATED_TITLES = {
    "modelos-n8n": "Modelos para N8N",
    "mejor-llm-para-tool-calling": "Mejor LLM para tool calling",
    "mejor-llm-para-agentes": "Mejor LLM para agentes",
    "mejor-llm-para-n8n": "Mejor LLM para N8N",
    "mejor-llm-para-programar": "Mejor LLM para programar",
    "mejor-llm-para-razonamiento": "Mejor LLM para razonamiento",
    "mejor-llm-para-contenido": "Mejor LLM para contenido",
    "mejor-llm-para-resumir-textos": "Mejor LLM para resumir textos",
    "mejor-llm-barato": "LLM más baratos",
    "mejor-llm-open-source": "Mejor LLM open source",
    "mejor-llm-en-espanol": "Mejor LLM en español",
    "modelos-baratos-emprendedores": "Modelos baratos para emprendedores",
    "modelos-open-source-local": "Modelos open-source local",
    "alternativas-claude": "Alternativas a Claude",
    "alternativas-chatgpt": "Alternativas a ChatGPT",
    "alternativas-gemini": "Alternativas a Gemini",
    "alternativas-deepseek": "Alternativas a DeepSeek",
    "qwen-vs-llama": "Qwen vs Llama",
    "gpt-5.6-vs-claude-opus-4-8": "GPT-5.6 vs Claude Opus 4.8",
}


def related_pages(cfg):
    links = cfg.get("related", [])
    if not links:
        return ""
    items = []
    for slug in links:
        title = RELATED_TITLES.get(slug, slug.replace("-", " ").title())
        items.append(f'<li><a href="/{slug}/">{esc(title)}</a></li>')
    return f"""<section>
  <h2>Comparaciones relacionadas</h2>
  <ul>
    {''.join(items)}
  </ul>
</section>"""


def analysis(cfg, ranked):
    top1 = ranked[0]
    s1 = score_for(top1, cfg)
    why = (f"<strong>{esc(top1.get('name'))}</strong> encabeza el ranking para {cfg['case']} "
           f"con {s1:.1f}/10, a {fmt_cost(top1)} por millón de tokens "
           f"({round(top1.get('tokens_per_second') or 0)} tok/s, {esc(top1.get('provider',''))}).")
    w = get_meta().get("default_weights", {})
    q = fmt_pct(w.get("quality", 0.7))
    co = fmt_pct(w.get("cost", 0.15))
    sp = fmt_pct(w.get("speed", 0.075))
    la = fmt_pct(w.get("latency", 0.075))
    return f"""<section>
  <h2>Por qué {esc(top1.get('name'))} lidera</h2>
  <p>{why} Recordá que el score global v3.0 pondera calidad {q}% + costo {co}% + velocidad {sp}% + latencia {la}% — no es solo "el más inteligente",
  sino el que mejor rinde en producción para este caso.</p>
  <h3>Cuándo conviene este modelo</h3>
  <ul>
    <li>Si tu prioridad es <strong>{esc(cfg['what'])}</strong> y querés el mejor score de esta dimensión.</li>
    <li>Si tu volumen es medio/bajo (cientos a miles de calls/mes) y el costo no domina.</li>
    <li>{'Si querés pesos abiertos y flexibilidad de provider.' if top1.get('open_source') else 'Si ya usás este provider o no te importa el lock-in.'}</li>
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
            f"Según nuestro benchmark, {top1.get('name')} lidera en {cfg['what']} con {score_for(top1, cfg):.1f}/10, "
            "pero el ranking completo te deja elegir según tu presupuesto y prioridad. No hay un único 'mejor' universal.",
            f"Según nuestro benchmark, <strong>{esc(top1.get('name'))}</strong> lidera en {esc(cfg['what'])} "
            f"con {score_for(top1, cfg):.1f}/10, pero el ranking completo te deja elegir según tu presupuesto y prioridad. "
            "No hay un único 'mejor' universal.",
        ),
        (
            f"¿Por qué un modelo barato gana en {cfg['what']} a modelos frontier?",
            "Porque el score global pondera calidad, costo, velocidad y latencia. Un modelo más barato y rápido puede tener "
            "mejor valor de producción que uno caro y lento, aunque el frontier tenga más capacidad bruta en algunas tareas.",
            "Porque el score global pondera calidad, costo, velocidad y latencia. Un modelo más barato y rápido puede tener "
            "mejor valor de producción que uno caro y lento, aunque el frontier tenga más capacidad bruta en algunas tareas.",
        ),
        (
            f"¿Para qué casos NO sirve el #1 de este ranking?",
            f"Si tu caso es muy distinto a {cfg['what']} —por ejemplo, necesitás razonamiento profundo, tool calling crítico o privacidad extrema— "
            "probablemente haya mejores opciones. Usá la calculadora para ajustar pesos por caso.",
            f"Si tu caso es muy distinto a {esc(cfg['what'])} —por ejemplo, necesitás razonamiento profundo, tool calling crítico o privacidad extrema— "
            "probablemente haya mejores opciones. Usá la <a href=\"/\">calculadora</a> para ajustar pesos por caso.",
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
    schema_script = f'<script type="application/ld+json">\n{json.dumps(schema, ensure_ascii=False, indent=2)}\n</script>'
    details = "\n  ".join(
        f'<details><summary><strong>{esc(q)}</strong></summary>\n  <p>{a_html}</p></details>'
        for q, _, a_html in qas
    )
    return f"""<section class="faq">
  {schema_script}
  <h2>Preguntas frecuentes sobre {esc(cfg['what'])}</h2>
  {details}
</section>"""


def dataset_schema(cfg, ranked):
    """Schema.org Dataset para reforzar indexación de datos del ranking."""
    c = get_counts()
    return {
        "@context": "https://schema.org",
        "@type": "Dataset",
        "name": f"Ranking de {esc(cfg['what'])} - Benchmark Alternativos",
        "description": f"Ranking de modelos LLM para {esc(cfg['what'])} basado en {fmt_k(c['total_runs'])} runs reales.",
        "url": f"{SITE}/{cfg['slug']}/",
        "creator": {"@type": "Person", "name": "Cristian Tala", "url": "https://cristiantala.com"},
        "datePublished": date.today().isoformat(),
        "dateModified": date.today().isoformat(),
        "license": "https://opensource.org/licenses/MIT",
        "distribution": [
            {"@type": "DataDownload", "encodingFormat": "application/json",
             "contentUrl": "https://github.com/ctala/ai-benchmarks-alternativos/tree/main/benchmarks/results"}
        ],
    }


def verdict_block(cfg, models):
    """El veredicto, ANTES de la tabla. La tabla pasa a ser evidencia, no output.

    Antes, estas paginas terminaban en una tabla muda y diferian la decision al
    lector ("depende de tu caso", "ajustalo en la calculadora"). El emprendedor
    se iba con datos y sin decision.

    Lo que hace posible decidir: los modelos de la cima EMPATAN estadisticamente
    en calidad (sus IC95 no se distinguen), asi que la decision real es de COSTO.
    """
    from bands import verdict as _verdict

    pil = cfg.get("pillar") if cfg.get("criterion") == "pillar" else None
    v = _verdict([m for m in models if (m.get("runs") or 0) >= 50], pil, calls_per_month=3000)
    if not v or "best" not in v:
        return ""

    b = v["best"]
    cards = [
        f"""<div class="verdict-card verdict-best">
        <span class="verdict-tag">Usá este</span>
        <strong>{esc(b['name'])}</strong>
        <span class="verdict-cost">≈${b['cost_month']:,.0f}/mes</span>
        <span class="verdict-note">calidad {b['quality']:.2f}/10 · el más barato de los que empatan arriba</span>
      </div>"""
    ]
    if "priciest" in v:
        p = v["priciest"]
        cards.append(f"""<div class="verdict-card verdict-costly">
        <span class="verdict-tag">Lo que te ahorrás</span>
        <strong>{esc(p['name'])}</strong>
        <span class="verdict-cost">≈${p['cost_month']:,.0f}/mes</span>
        <span class="verdict-note">{p['times']}× más caro por {p['quality_gap']:+.2f} de calidad — una diferencia que está dentro del margen de error</span>
      </div>""")
    if "local" in v:
        l = v["local"]
        cards.append(f"""<div class="verdict-card">
        <span class="verdict-tag">Si tenés hardware propio</span>
        <strong>{esc(l['name'])}</strong>
        <span class="verdict-cost">≈${l['cost_month']:,.0f}/mes</span>
        <span class="verdict-note">calidad {l['quality']:.2f}/10 · corre local, sin API</span>
      </div>""")

    # El CTA lleva el contexto a la calculadora. Antes era href="/" a secas y el
    # usuario que venia buscando "agentes" aterrizaba en score global por default,
    # teniendo que reconstruir a mano el caso de uso que ya habia declarado.
    preset = {"Agentes": "agentes", "Coding": "coding",
              "Contenido": "contenido", "Razonamiento": "calidad"}.get(pil or "", "")
    qs = f"?preset={preset}&amp;calls=3000" if preset else "?calls=3000"

    return f"""  <section class="verdict">
    <h2>La respuesta corta</h2>
    <p class="verdict-lead"><strong>{v['band_size']} modelos empatan</strong> en calidad para esta tarea:
    la diferencia entre ellos es más chica que el margen de error de la medición.
    Cuando la calidad empata, <strong>la decisión es de precio</strong>.</p>
    <div class="verdict-grid">
      {''.join(cards)}
    </div>
    <p class="verdict-foot">Cálculo sobre <strong>3.000 llamadas/mes</strong> (≈100 por día: una respuesta
    de agente o un borrador de texto por llamada). ¿Otro volumen o te importa la velocidad?
    Ajustalo en la <a href="/{qs}">calculadora</a>.
    La tabla de abajo es la evidencia completa.</p>
  </section>
"""


def render_ranking(cfg, models):
    ranked = rank_models(models, cfg)
    if not ranked:
        return None
    ranked = ranked[:8]
    url = f"{SITE}/{cfg['slug']}/"
    tests_k = fmt_k(get_counts()["total_runs"])
    desc = (f"{cfg['h1']} con {tests_k} runs reales: ranking por {cfg['case']}. "
            f"Incluye costos para volumen, análisis del top 3 y posición de modelos frontier. #1: {ranked[0].get('name')}.")
    today = date.today().isoformat()
    rows = "\n        ".join(row_ranking(i + 1, m, cfg, top=(i == 0)) for i, m in enumerate(ranked))
    dataset_ld = json.dumps(dataset_schema(cfg, ranked), ensure_ascii=False, indent=2)
    body = f"""  <section class="hero">
    <h1>{esc(cfg['h1'])}</h1>
    <p class="lead">{cfg['lead']}</p>
    <p class="meta">Última actualización: {today} ·
    <a href="https://github.com/ctala/ai-benchmarks-alternativos" target="_blank" rel="noopener">datos abiertos en GitHub</a></p>
  </section>
{verdict_block(cfg, models)}
  <section class="results">
    <div class="results-header">
      <h2>Ranking: {esc(cfg['h1'])}</h2>
      <p class="meta">{({'pillar':'Ordenado por <strong>capacidad pura en esta tarea</strong>: solo calidad, sin ponderar costo ni velocidad. Quien busca el mejor para esta tarea pregunta quién la hace mejor — el precio se muestra aparte, para decidir después.','suite':'Ordenado por calidad en esta suite, sin ponderar costo ni velocidad.','cost':'Ordenado por costo total (input + output) con score global ≥ 6,8.','open_source':'Ordenado por score global, filtrando solo modelos open source.'}[cfg['criterion']])}</p>
    </div>
    {table_head(cfg)}
      <tbody>
        {rows}
      </tbody>
    </table></div>
    <p class="meta">Filtrá por presupuesto, calidad mínima o tarea en la <a href="/">calculadora interactiva</a>.</p>
  </section>
  {reading_guide(cfg, ranked)}
  {top3_explained(cfg, ranked)}
  {analysis(cfg, ranked)}
  {cost_comparison(cfg, ranked)}
  {frontier_in_dimension(cfg, models)}
  {methodology()}
  {related_pages(cfg)}
  <script type="application/ld+json">
{dataset_ld}
  </script>
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
