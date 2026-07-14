#!/usr/bin/env python3
"""
Genera páginas "¿qué tier de <familia> elegir?" — TODAS las variantes de una misma
familia en una sola página, no de a pares.

POR QUE EXISTE
--------------
Las comparaciones existentes son A-vs-B: /gpt-5.6-luna-vs-sol/, /luna-vs-terra/,
/terra-vs-sol/. Tres páginas para responder a medias la pregunta que la gente hace
de verdad, que no es "Luna o Sol" sino **"¿cuál de los tres tomo?"**.

Quien acaba de decidir usar GPT-5.6 no quiere un cara a cara: quiere que alguien le
diga qué tier contratar. Esta página responde eso.

QUE LA HACE DISTINTA DE UN RANKING
----------------------------------
Dentro de una familia el proveedor vende una escalera: más caro = mejor. Esta página
audita esa escalera dimensión por dimensión y muestra dónde se cumple y dónde no.
En GPT-5.6 el resultado es que la escalera **solo** se cumple en seguridad — y esa
dimensión ni siquiera entra en el score global. Es el hallazgo, y es reutilizable:
la misma pregunta aplica a la familia Claude (Haiku/Sonnet/Opus) o Gemini.

Uso:
    python benchmarks/generate_variants.py
    python benchmarks/generate_variants.py --slug gpt-5.6-luna-terra-sol
"""
import argparse
from datetime import date

from generate_comparison import (
    load_models, fmt_cost, esc, methodology, page_shell, SITE, DOCS, PILLARS,
    get_counts, fmt_k, pillar, funnel_block,
)

# Familias a generar. Añadir una = un dict acá, cero HTML a mano.
FAMILIES = [
    {
        "slug": "gpt-5.6-luna-terra-sol",
        "family": "GPT-5.6",
        "match": ["gpt-5.6"],
        "title": "GPT-5.6: Luna, Terra o Sol — cuál elegir en 2026 (benchmark real)",
        "h1": "GPT-5.6: ¿Luna, Terra o Sol?",
        "intent_kw": ("gpt 5.6 luna terra sol, cual gpt 5.6 usar, gpt 5.6 luna o sol, "
                      "diferencia gpt 5.6 luna terra sol, que tier de gpt 5.6 elegir, gpt 5.6 precio"),
        "lead": ("OpenAI vende tres tiers de GPT-5.6 y da por supuesto que el caro es el mejor. "
                 "Los medimos con la misma suite, 103 corridas cada uno. Esto es lo que pasa cuando "
                 "los pones a trabajar."),
        # Post del blog que desarrolla el hallazgo (cross-link, no duplica)
        "post": ("https://cristiantala.com/gpt-5-6-luna-terra-sol-cual-elegir/",
                 "El análisis completo: por qué “empatan” no es una opinión"),
    },
    {
        "slug": "claude-haiku-sonnet-opus",
        "family": "Claude",
        "match": ["claude", "opus", "sonnet", "haiku", "fable"],
        "title": "Claude: Haiku, Sonnet, Opus o Fable — cuál elegir en 2026 (benchmark real)",
        "h1": "Claude: ¿Haiku, Sonnet, Opus o Fable?",
        # Volumen real (DataForSEO, ES+MX, jul-2026): "claude sonnet vs opus" + su
        # variante de orden suman ~720/mes. Ese es el head; lo demás es cola.
        "intent_kw": ("claude sonnet vs opus, claude opus vs sonnet, claude haiku vs sonnet, "
                      "cual claude usar, claude opus vale la pena, que modelo de claude elegir"),
        "lead": ("Anthropic tiene una escalera de precios de 10× entre su modelo de entrada y el de arriba. "
                 "La medimos toda con la misma suite. Si la calidad subiera igual que el precio, "
                 "esta página no existiría."),
    },
    {
        # Caso raro y por eso interesante: las tres cuestan LO MISMO. No hay escalera
        # de precio que auditar — el que gana, gana gratis.
        "slug": "minimax-m2-7-o-m3",
        "family": "MiniMax",
        "match": ["minimax"],
        "title": "MiniMax M2.7 o M3: cuál usar en 2026 (benchmark real)",
        "h1": "MiniMax: ¿M2.7 o M3?",
        # "minimax m3" hace ~530/mes (ES+MX) y NO tiene pagina propia. Es el head:
        # la gente busca el modelo, no la comparacion. Va primero.
        "intent_kw": ("minimax m3, minimax m3 opiniones, minimax m3 precio, minimax m3 vs m2.7, "
                      "cual minimax usar, minimax m3 benchmark español"),
        "lead": ("Acá no hay dilema de precio: las variantes de MiniMax cuestan prácticamente lo mismo. "
                 "La única pregunta es cuál rinde más — y la respuesta es más clara de lo que suele ser."),
    },
    {
        "slug": "gemini-flash-o-pro",
        "family": "Gemini",
        "match": ["gemini"],
        "title": "Gemini Flash o Pro: cuál conviene en 2026 (benchmark real)",
        "h1": "Gemini: ¿Flash o Pro?",
        "intent_kw": ("gemini flash vs pro, gemini 2.5 pro vale la pena, cual gemini usar, "
                      "gemini flash lite vs pro, diferencia gemini flash pro"),
        "lead": ("Google vende Pro como el tier serio y Flash como el barato. Los medimos a todos "
                 "con la misma suite. El resultado no es el que sugiere el precio."),
    },
    {
        "slug": "grok-4-1-vs-4-5",
        "family": "Grok",
        "match": ["grok"],
        "title": "Grok 4.1, 4.20, 4.3 o 4.5: cuál usar en 2026 (benchmark real)",
        "h1": "Grok: ¿cuál de las versiones?",
        "intent_kw": ("grok 4.5 vs 4.1, grok 4.5 vale la pena, cual grok usar, "
                      "grok 4.1 fast opiniones, grok 4.5 benchmark"),
        "lead": ("xAI sacó versiones nuevas de Grok una detrás de otra. Las medimos todas con la misma "
                 "suite, y el orden en que quedan no es el orden en que salieron."),
    },
    {
        "slug": "deepseek-v4-flash-o-r1",
        "family": "DeepSeek",
        "match": ["deepseek"],
        "title": "DeepSeek V4 Flash, R1 o Pro: cuál usar en 2026 (benchmark real)",
        "h1": "DeepSeek: ¿V4 Flash, R1 o Pro?",
        "intent_kw": ("deepseek v4 flash vs r1, cual deepseek usar, deepseek r1 vale la pena, "
                      "deepseek v4 pro opiniones, deepseek benchmark español"),
        "lead": ("DeepSeek tiene varias líneas y la diferencia de precio entre ellas es de 12×. "
                 "Las medimos con la misma suite para ver si esa diferencia se nota donde importa."),
    },
]

# Dimensiones que se reportan APARTE del score global (README). En una familia son
# justo donde puede esconderse la única diferencia real entre tiers.
EXTRA_DIMS = [
    ("security_score", "Resiste prompt injection", "Aguanta instrucciones escondidas en el texto que lee"),
    ("long_context_score", "Contexto largo", "Recupera datos de documentos extensos"),
    ("tool_calling_score_avg", "Tool calling", "Llama herramientas bien formadas"),
]


def _base_name(name: str) -> str:
    """'Claude Opus 4.8 (suscripción)' -> 'claude opus 4.8'.

    El mismo modelo aparece medido por dos vías (API y suscripción). Para el lector
    son el MISMO modelo: mostrarlo dos veces en una tabla de "cuál elijo" no informa,
    confunde. Se deduplica y se queda la medición con más runs.
    """
    import re as _re
    return _re.sub(r"\s*\(.*?\)\s*", "", name or "").strip().lower()


def variants_of(models, cfg):
    """Variantes de la familia con muestra sólida, deduplicadas, por precio ascendente."""
    cand = []
    for m in models:
        blob = f"{m.get('name','')} {m.get('key','')} {m.get('id','')}".lower()
        if not any(p in blob for p in cfg["match"]):
            continue
        if any(x in blob for x in cfg.get("exclude", [])):
            continue
        if (m.get("runs") or 0) < 50 or not m.get("score_global"):
            continue
        cand.append(m)

    best = {}
    for m in cand:
        k = _base_name(m.get("name", ""))
        cur = best.get(k)
        if cur is None or (m.get("runs") or 0) > (cur.get("runs") or 0):
            best[k] = m
    return sorted(best.values(), key=lambda m: m.get("cost_per_1k_calls_usd") or 0)


def month(m, calls=3000):
    c = m.get("cost_per_1k_calls_usd")
    return c * calls / 1000 if c is not None else None


def short(m, cfg):
    """'GPT-5.6 Luna' -> 'Luna'. La familia ya está en el H1."""
    return (m.get("name") or "").replace(cfg["family"], "").strip() or m.get("name")


# Las categorías donde de verdad se ve la diferencia. Suites, no pilares: el pilar
# promedia y esconde. "Razonamiento" mezcla auditar un P&L con resolver un acertijo.
SUITES_ESCALERA = [
    ("business_audit",      "Auditar un negocio",      "Encontrar el error en un P&L, la causalidad falsa, la métrica envenenada"),
    ("business_strategy",   "Planificar",              "Armar un plan cuya aritmética cierre y respete las restricciones"),
    ("content_verificable", "Escribir con restricciones", "No repetir el dato falso del brief, no meter el CTA prohibido"),
    ("deep_reasoning",      "Razonamiento profundo",   "Matemática, lógica formal, estimaciones Fermi"),
    ("code_generation",     "Código",                  "Generar y corregir código que funcione"),
    ("agent_long_horizon",  "Agentes largos",          "Mantener el hilo y las restricciones a lo largo de muchos turnos"),
    ("multi_turn",          "Multi-turno",             "Conversaciones de ida y vuelta sin perder el contexto"),
    ("tool_calling",        "Tool calling",            "Llamar herramientas con los parámetros correctos"),
]


def ladder_block(vs, cfg):
    """¿Dónde compra algo el precio? La auditoría, tier por tier y categoría por categoría.

    QUÉ CAMBIÓ (14-jul-2026, y por qué importa)
    -------------------------------------------
    Antes esto comparaba SOLO el más barato contra el más caro, sobre PILARES, usando
    `score_by_suite`. Tres errores, y cada uno mentía distinto:

    1. Ignoraba el tier del medio. En GPT-5.6, Terra es el único que gana en planificar.
    2. El pilar promedia y esconde: "Razonamiento" mezcla auditar un P&L con un acertijo
       lógico. Sol es peor en uno y mejor en el otro; el promedio dice "empatan".
    3. `score_by_suite` es el score COMPUESTO: incluye precio. Usarlo para responder
       "¿quién es mejor EN esto?" hace que el barato gane por ser barato. Publiqué un
       titular falso por leer esa columna como si fuera calidad.

    Ahora: los tres tiers, por suite, en CALIDAD PURA (`quality_by_suite`). El precio se
    mira aparte, que es donde corresponde.
    """
    cheapest, priciest = vs[0], vs[-1]
    rows, gana_caro, empates = [], [], 0

    def q(m, suite):
        return (m.get("quality_by_suite") or {}).get(suite)

    for suite, label, desc in SUITES_ESCALERA:
        vals = [(m, q(m, suite)) for m in vs]
        if any(v is None for _, v in vals):
            continue
        mejor = max(vals, key=lambda x: x[1])[0]
        spread = max(v for _, v in vals) - min(v for _, v in vals)

        if spread < 0.25:
            cls, veredicto = "lad-tie", "Empatan — el precio no compra nada"
            empates += 1
        elif mejor is priciest:
            cls, veredicto = "lad-yes", "El precio compra algo"
            gana_caro.append(label)
        elif mejor is cheapest:
            cls, veredicto = "lad-no", "Va al revés: gana el barato"
        else:
            cls, veredicto = "lad-tie", "Gana " + short(mejor, cfg)

        celdas = ""
        for m, v in vals:
            td = '<td class="win">' if m is mejor else "<td>"
            celdas += td + "{:.2f}</td>".format(v)

        rows.append(
            '<tr class="' + cls + '"><td><strong>' + esc(label) + "</strong>"
            + '<span class="lad-desc">' + esc(desc) + "</span></td>"
            + celdas
            + '<td class="lad-verdict">' + esc(veredicto) + "</td></tr>"
        )

    cols = ""
    for m in vs:
        precio = m.get("cost_per_1k_calls_usd") or 0
        cols += ("<th>" + esc(short(m, cfg))
                 + '<span class="lad-price">${:.2f}</span></th>'.format(precio))

    tabla = ('<div class="table-scroll"><table class="results-table ladder">'
             "<thead><tr><th>Qué le pedís</th>" + cols
             + "<th>¿El precio compra algo?</th></tr></thead>"
             + "<tbody>" + "".join(rows) + "</tbody></table></div>")

    n = len(rows)
    barato = cheapest.get("cost_per_1k_calls_usd") or 0.01
    mult = (priciest.get("cost_per_1k_calls_usd") or 0) / max(0.01, barato)

    if gana_caro:
        lede = (
            '<p class="verdict-lead"><strong>' + esc(short(priciest, cfg))
            + " cuesta {:.0f} veces más que ".format(mult) + esc(short(cheapest, cfg))
            + ".</strong> Y sí compra algo — pero solo en <strong>"
            + "{} de {}</strong> categorías: ".format(len(gana_caro), n)
            + esc(", ".join(gana_caro).lower()) + ".</p>"
            + "<p>En las otras {}, o empatan o <strong>gana el barato</strong>. ".format(n - len(gana_caro))
            + "Si tu trabajo cae justo en esas {}, el tier de arriba te da algo real. ".format(len(gana_caro))
            + "Si no, estás pagando {:.0f}× por menos.</p>".format(mult)
        )
    else:
        lede = (
            '<p class="verdict-lead"><strong>' + esc(short(priciest, cfg))
            + " cuesta {:.0f} veces más que ".format(mult) + esc(short(cheapest, cfg))
            + " y no gana en ninguna categoría.</strong> La escalera de precios no está "
            + "comprada con calidad: está comprada con otra cosa (contexto, límites de uso, "
            + "prioridad en cola).</p>"
        )

    nota = ('<p class="meta">Los números son <strong>calidad pura</strong>: sin costo, sin '
            "velocidad. Cada categoría se compara sobre los <strong>mismos tests</strong> "
            "rendidos por los tres. Un promedio sacado de exámenes distintos no compara "
            "modelos — compara exámenes.</p>")

    return lede + tabla + nota
def render(cfg, models):
    vs = variants_of(models, cfg)
    if len(vs) < 2:
        return None

    cheapest, priciest = vs[0], vs[-1]
    best_q = max(vs, key=lambda m: m.get("quality_avg") or 0)
    today = date.today().isoformat()
    tests_k = fmt_k(get_counts()["total_runs"])
    url = f"{SITE}/{cfg['slug']}/"
    desc = (f"{cfg['family']}: comparamos sus {len(vs)} tiers con {tests_k} runs reales. "
            f"Cuál conviene, cuánto cuesta cada uno al mes y en qué caso vale pagar el caro.")

    # Tabla principal: todos los tiers, precio ascendente.
    rows = []
    for m in vs:
        is_cheap = m is cheapest
        badge = ' <span class="row-badge">← el más barato</span>' if is_cheap else ""
        tr_cls = ' class="win"' if is_cheap else ""
        rows.append(
            f'<tr{tr_cls}><td><strong>{esc(short(m, cfg))}</strong>{badge}</td>'
            f'<td>{(m.get("quality_avg") or 0):.2f}</td>'
            f'<td>{pillar(m,"Coding"):.1f}</td><td>{pillar(m,"Contenido"):.1f}</td>'
            f'<td>{pillar(m,"Razonamiento"):.1f}</td><td>{pillar(m,"Agentes"):.1f}</td>'
            f'<td>≈${month(m):,.0f}/mes</td>'
            f'<td>{(m.get("latency_avg_s") or 0):.1f}s</td>'
            f'<td>{(m.get("score_global") or 0):.2f}</td></tr>'
        )

    gap = (best_q.get("quality_avg") or 0) - (cheapest.get("quality_avg") or 0)
    times = (month(priciest) / month(cheapest)) if month(cheapest) else None
    tie = abs(gap) <= 0.30

    verdict = f"""  <section class="verdict">
    <h2>La respuesta corta</h2>
    <p class="verdict-lead">{'Los ' + str(len(vs)) + ' tiers <strong>empatan en calidad</strong>: la diferencia entre ellos es más chica que el margen de error de la medición.' if tie else 'El tier de más calidad es <strong>' + esc(short(best_q, cfg)) + '</strong>.'}
    {'Y el más caro cuesta <strong>' + f'{times:.0f}×' + '</strong> lo que el más barato.' if times and times >= 2 else ''}</p>
    <div class="verdict-grid">
      <div class="verdict-card verdict-best">
        <span class="verdict-tag">Empieza por este</span>
        <strong>{esc(short(cheapest, cfg))}</strong>
        <span class="verdict-cost">≈${month(cheapest):,.0f}/mes</span>
        <span class="verdict-note">calidad {(cheapest.get('quality_avg') or 0):.2f}/10 · {(cheapest.get('latency_avg_s') or 0):.1f}s de respuesta</span>
      </div>
      <div class="verdict-card verdict-costly">
        <span class="verdict-tag">El flagship</span>
        <strong>{esc(short(priciest, cfg))}</strong>
        <span class="verdict-cost">≈${month(priciest):,.0f}/mes</span>
        <span class="verdict-note">calidad {(priciest.get('quality_avg') or 0):.2f}/10 · {(priciest.get('latency_avg_s') or 0):.1f}s. {'La misma calidad, más lento y más caro.' if tie else ''}</span>
      </div>
    </div>
    <p class="verdict-foot">Costos a <strong>3.000 llamadas/mes</strong> (≈100 por día).
    Ajústalo a tu volumen en la <a href="/?calls=3000">calculadora</a>.
    Y baja un poco: <strong>hay un caso donde el caro sí vale la pena</strong>, y no es el que te venden.</p>
  </section>
"""

    body = f"""  <section class="hero">
    <h1>{esc(cfg['h1'])}</h1>
    <p class="lead">{esc(cfg['lead'])}</p>
    <p class="meta">Última actualización: {today} ·
    <a href="https://github.com/ctala/ai-benchmarks-alternativos" target="_blank" rel="noopener">datos abiertos en GitHub</a></p>
  </section>
{verdict}
  <section class="results">
    <div class="results-header">
      <h2>Los {len(vs)} tiers, uno al lado del otro</h2>
      <p class="meta">Ordenados <strong>por precio</strong>, del más barato al más caro — para que veas
      si la calidad sube con él. Los pilares son <strong>calidad pura</strong> en esa tarea, sin mezclar costo.</p>
    </div>
    <div class="table-scroll"><table class="results-table">
      <thead><tr>
        <th scope="col">Tier</th><th scope="col">Calidad</th>
        <th scope="col">Coding</th><th scope="col">Contenido</th>
        <th scope="col">Razon.</th><th scope="col">Agentes</th>
        <th scope="col">Costo/mes</th><th scope="col">Latencia</th><th scope="col">Score</th>
      </tr></thead>
      <tbody>
        {''.join(rows)}
      </tbody>
    </table></div>
  </section>
{ladder_block(vs, cfg)}
  <section>
    <h2>Cómo leer esto sin equivocarte</h2>
    <p>Que dos tiers <strong>empaten</strong> no significa que sean idénticos: significa que
    <strong>esta medición no los distingue</strong>. Con 103 corridas, cada número tiene un margen
    alrededor; cuando ese margen se solapa, la diferencia que ves es ruido, no señal. Si volviera a
    correr el test mañana, el orden podría darse vuelta sin que nada haya cambiado en los modelos.</p>
    <p>La consecuencia práctica es simple: <strong>si la calidad empata, la decisión es de precio y
    de velocidad</strong>. Y si el proveedor quiere que pagues más, que te diga exactamente qué compras
    — con su margen de error al lado.</p>
    {f'<p><a href="{cfg["post"][0]}">{esc(cfg["post"][1])} →</a></p>' if cfg.get("post") else ""}
  </section>
{funnel_block()}
{methodology()}
"""
    return page_shell(cfg["title"], desc, cfg["intent_kw"], url, body)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", help="Genera solo esta familia")
    args = ap.parse_args()

    models = load_models()
    for cfg in FAMILIES:
        if args.slug and cfg["slug"] != args.slug:
            continue
        html = render(cfg, models)
        if not html:
            print(f"✗ {cfg['slug']}: menos de 2 variantes con ≥50 runs")
            continue
        out = DOCS / cfg["slug"]
        out.mkdir(parents=True, exist_ok=True)
        (out / "index.html").write_text(html)
        n = len(variants_of(models, cfg))
        print(f"✓ {cfg['slug']}: {n} tiers → docs/{cfg['slug']}/index.html")


if __name__ == "__main__":
    main()
