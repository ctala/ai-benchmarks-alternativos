#!/usr/bin/env python3
"""
Genera el CheatSheet PDF con branding de cristiantala.com
Usa WeasyPrint para convertir HTML a PDF.
"""

import json
from datetime import datetime
from pathlib import Path
from weasyprint import HTML

now = datetime.now()
month_name = now.strftime("%B")
year = now.year

# Cargar resultados
all_results = []
for f in sorted(Path("benchmarks/results").glob("benchmark_*.json")):
    with open(f) as fh:
        all_results.extend(json.load(fh))

# Deduplicar
seen = {}
for r in all_results:
    key = f"{r['model']}|{r['test_name']}"
    seen[key] = r
results = list(seen.values())

# Agrupar
models = {}
for r in results:
    m = r["model"]
    if m not in models:
        models[m] = {"scores": [], "tps": [], "lat": [], "cost": [], "err": 0, "tot": 0}
    models[m]["tot"] += 1
    if r.get("success"):
        models[m]["scores"].append(r["final"])
        models[m]["tps"].append(r["tokens_per_second"])
        models[m]["lat"].append(r["latency_total"])
        models[m]["cost"].append(r.get("cost_usd", 0))
    else:
        models[m]["err"] += 1

ranked = []
for m, d in models.items():
    if d["scores"] and len(d["scores"]) >= 5:
        ranked.append({
            "name": m,
            "score": round(sum(d["scores"]) / len(d["scores"]), 2),
            "tps": round(sum(d["tps"]) / len(d["tps"])),
            "lat": round(sum(d["lat"]) / len(d["lat"]), 1),
            "cost": round(sum(d["cost"]) / len(d["cost"]), 5),
            "ok": f"{d['tot']-d['err']}/{d['tot']}",
        })

ranked.sort(key=lambda x: x["score"], reverse=True)

# Info de open source
open_source_map = {
    "Devstral Small": ("Si", "Apache 2.0"),
    "DeepSeek V3.2": ("Si", "MIT"),
    "Llama 4 Maverick": ("Si", "Llama Community"),
    "Qwen3 Coder": ("Si", "Apache 2.0"),
    "Qwen 3.6 Plus": ("Si", "Apache 2.0"),
    "Gemma 4 26B MoE (3.8B activos)": ("Si", "Apache 2.0"),
    "Gemma 4 31B": ("Si", "Apache 2.0"),
    "Mistral Large": ("Si", "Apache 2.0"),
    "MiniMax M2.7": ("Parcial", "MIT (M2.5)"),
    "MiniMax M2.7 (directo)": ("Parcial", "MIT (M2.5)"),
    "MiniMax M2.7 Highspeed": ("Parcial", "MIT (M2.5)"),
    "Kimi K2": ("No", "-"),
    "Kimi K2.5": ("No", "-"),
}


def get_os(name):
    return open_source_map.get(name, ("No", "-"))


def ranking_rows():
    rows = ""
    for i, m in enumerate(ranked, 1):
        os_status, license = get_os(m["name"])
        os_class = "os-yes" if os_status == "Si" else "os-partial" if os_status == "Parcial" else "os-no"
        highlight = ' class="top3"' if i <= 3 else ""
        rows += f"""<tr{highlight}>
            <td class="rank">{i}</td>
            <td class="model-name">{m['name']}</td>
            <td class="score">{m['score']}</td>
            <td>{m['tps']}</td>
            <td>{m['lat']}s</td>
            <td>${m['cost']}</td>
            <td class="{os_class}">{os_status}</td>
        </tr>\n"""
    return rows


html_content = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Inter:wght@400;600;700&display=swap');

@page {{
    size: A4 landscape;
    margin: 10mm;
    background: #0a0a1a;
    @bottom-center {{
        content: "cristiantala.com | Benchmark de Modelos AI | {month_name} {year}";
        font-family: 'Inter', sans-serif;
        font-size: 8pt;
        color: #b0b0b0;
    }}
    @bottom-right {{
        content: counter(page) " / " counter(pages);
        font-family: 'JetBrains Mono', monospace;
        font-size: 8pt;
        color: #39ff14;
    }}
}}

* {{ margin: 0; padding: 0; box-sizing: border-box; }}

html {{
    background: #0a0a1a;
}}

body {{
    font-family: 'Inter', sans-serif;
    background: #0a0a1a;
    color: #ffffff;
    font-size: 9pt;
    line-height: 1.4;
}}

/* ===== PAGE 1: COVER ===== */
.cover {{
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 170mm;
    text-align: center;
    background: linear-gradient(180deg, #0a0a1a 0%, #1a0a2e 50%, #0a0a1a 100%);
}}

.cover h1 {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 28pt;
    color: #39ff14;
    text-transform: uppercase;
    letter-spacing: 3px;
    margin-bottom: 8px;
}}

.cover .subtitle {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 14pt;
    color: #00d4ff;
    margin-bottom: 25px;
}}

.cover .meta {{
    font-size: 10pt;
    color: #b0b0b0;
    margin-top: 10px;
}}

.cover .stats {{
    display: flex;
    justify-content: center;
    gap: 40px;
    margin-top: 25px;
}}

.cover .stat-box {{
    text-align: center;
    padding: 10px 20px;
    border: 1px solid #39ff14;
    border-radius: 6px;
}}

.cover .stat-number {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 24pt;
    color: #39ff14;
    display: block;
}}

.cover .stat-label {{
    font-size: 8pt;
    color: #b0b0b0;
    text-transform: uppercase;
}}

/* ===== GENERAL ===== */
.page {{
    page-break-after: always;
}}

h2 {{
    font-family: 'JetBrains Mono', monospace;
    color: #39ff14;
    font-size: 14pt;
    margin-bottom: 10px;
    padding-bottom: 4px;
    border-bottom: 2px solid #39ff1444;
}}

h3 {{
    font-family: 'JetBrains Mono', monospace;
    color: #00d4ff;
    font-size: 11pt;
    margin: 12px 0 6px 0;
}}

/* ===== TABLES ===== */
table {{
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0;
    font-size: 8pt;
}}

th {{
    font-family: 'JetBrains Mono', monospace;
    background: #1a0a2e;
    color: #00d4ff;
    padding: 5px 6px;
    text-align: left;
    font-size: 7pt;
    text-transform: uppercase;
    border-bottom: 2px solid #39ff14;
}}

td {{
    padding: 4px 6px;
    border-bottom: 1px solid #1a0a2e;
}}

tr:nth-child(even) {{ background: #0f0f25; }}
tr.top3 {{ background: #1a0a2e; }}
tr.top3 td {{ font-weight: 600; }}

.rank {{ font-family: 'JetBrains Mono', monospace; color: #39ff14; font-weight: 700; text-align: center; }}
.score {{ font-family: 'JetBrains Mono', monospace; color: #39ff14; font-weight: 700; }}
.model-name {{ font-weight: 600; }}

.os-yes {{ color: #39ff14; font-weight: 600; }}
.os-partial {{ color: #ffa500; }}
.os-no {{ color: #b0b0b0; }}

/* ===== RECOMMENDATION BOXES ===== */
.rec-grid {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin: 8px 0;
}}

.rec-box {{
    flex: 1 1 30%;
    background: #1a0a2e;
    border: 1px solid #39ff1444;
    border-radius: 6px;
    padding: 8px 10px;
}}

.rec-box .rec-title {{
    font-family: 'JetBrains Mono', monospace;
    color: #00d4ff;
    font-size: 8pt;
    text-transform: uppercase;
    margin-bottom: 3px;
}}

.rec-box .rec-model {{
    font-family: 'JetBrains Mono', monospace;
    color: #39ff14;
    font-size: 10pt;
    font-weight: 700;
}}

.rec-box .rec-why {{
    font-size: 7pt;
    color: #b0b0b0;
    margin-top: 2px;
}}

/* ===== NOTES ===== */
.note {{
    background: #1a0a2e;
    border-left: 3px solid #ff006e;
    padding: 6px 10px;
    margin: 8px 0;
    font-size: 8pt;
    color: #b0b0b0;
}}

.note strong {{ color: #ff006e; }}

.two-col {{
    display: flex;
    gap: 15px;
}}

.two-col > div {{
    flex: 1;
}}

.footer-url {{
    text-align: center;
    font-family: 'JetBrains Mono', monospace;
    color: #00d4ff;
    font-size: 9pt;
    margin-top: 15px;
}}
</style>
</head>
<body>

<!-- ===== PAGE 1: COVER ===== -->
<div class="cover">
    <h1>AI Model Benchmark</h1>
    <div class="subtitle">Guia Definitiva para Elegir tu Modelo de IA</div>
    <p class="meta">{len(ranked)} modelos probados con {len(seen)} tests reales | {month_name} {year}</p>
    <div class="stats">
        <div class="stat-box">
            <span class="stat-number">21</span>
            <span class="stat-label">Modelos</span>
        </div>
        <div class="stat-box">
            <span class="stat-number">27</span>
            <span class="stat-label">Tests</span>
        </div>
        <div class="stat-box">
            <span class="stat-number">8</span>
            <span class="stat-label">Categorias</span>
        </div>
        <div class="stat-box">
            <span class="stat-number">567</span>
            <span class="stat-label">Runs totales</span>
        </div>
    </div>
    <p class="meta" style="margin-top: 15px;">Medido desde Chile via OpenRouter, OpenAI API y MiniMax API</p>

    <div style="margin-top: 18px; text-align: left; max-width: 650px; background: #1a0a2e; border: 1px solid #39ff1444; border-radius: 6px; padding: 10px 14px;">
        <p style="font-family: 'JetBrains Mono', monospace; color: #00d4ff; font-size: 9pt; margin-bottom: 5px;">Como se calcula el Score</p>
        <p style="font-size: 8pt; color: #b0b0b0; line-height: 1.5;">
            <span style="color:#39ff14; font-family:'JetBrains Mono',monospace;">35%</span> Calidad (formato, estructura, seguimiento de instrucciones)<br>
            <span style="color:#39ff14; font-family:'JetBrains Mono',monospace;">25%</span> Tool Calling (precision de function calling para agentes)<br>
            <span style="color:#39ff14; font-family:'JetBrains Mono',monospace;">15%</span> Costo (menos costo = mejor score)<br>
            <span style="color:#39ff14; font-family:'JetBrains Mono',monospace;">15%</span> Disponibilidad (rate limits, cuotas)<br>
            <span style="color:#39ff14; font-family:'JetBrains Mono',monospace;">5%</span> Velocidad (tokens por segundo)<br>
            <span style="color:#39ff14; font-family:'JetBrains Mono',monospace;">5%</span> Latencia (tiempo hasta primera respuesta)
        </p>
        <p style="font-size: 7pt; color: #ff006e; margin-top: 5px;">
            Nota: El scoring automatico evalua formato y estructura, no profundidad de razonamiento.
            Modelos como Claude Opus destacan en areas que este scoring no captura bien.
        </p>
    </div>

    <div class="footer-url" style="margin-top: 12px;">cristiantala.com</div>
</div>

<!-- ===== PAGE 2: METODOLOGIA ===== -->
<div class="page">
    <h2>Metodologia del Experimento</h2>

    <div class="two-col">
        <div>
            <h3>Diseno del Experimento</h3>
            <table>
                <thead><tr><th>Parametro</th><th>Valor</th></tr></thead>
                <tbody>
                    <tr><td>Modelos evaluados</td><td><strong>17 modelos unicos</strong></td></tr>
                    <tr><td>Tests totales</td><td><strong>41 tests en 11 suites</strong></td></tr>
                    <tr><td>Runs ejecutados</td><td><strong>800+</strong></td></tr>
                    <tr><td>Ubicacion</td><td>Santiago, Chile</td></tr>
                    <tr><td>APIs usadas</td><td>OpenRouter, OpenAI, MiniMax</td></tr>
                    <tr><td>Temperatura</td><td>0.7 (todos los modelos)</td></tr>
                    <tr><td>Max tokens</td><td>2048</td></tr>
                    <tr><td>Timeout</td><td>120 segundos por request</td></tr>
                    <tr><td>Fecha</td><td>11-12 {month_name} {year}</td></tr>
                </tbody>
            </table>

            <h3>Suites de Tests</h3>
            <table>
                <thead><tr><th>Suite</th><th>Tests</th><th>Que Mide</th></tr></thead>
                <tbody>
                    <tr><td>deep_reasoning</td><td>6</td><td>Matematica, logica, causal, etica</td></tr>
                    <tr><td>customer_support</td><td>4</td><td>Empatia, clasificacion, seguridad</td></tr>
                    <tr><td>structured_output</td><td>4</td><td>JSON valido, arrays, anidado</td></tr>
                    <tr><td>tool_calling</td><td>4</td><td>Function calling para agentes</td></tr>
                    <tr><td>content_generation</td><td>4</td><td>Blog, email, social media</td></tr>
                    <tr><td>startup_content</td><td>5</td><td>Blog startup, cursos, workshops</td></tr>
                    <tr><td>code_generation</td><td>4</td><td>Python, N8N, SQL, debug</td></tr>
                    <tr><td>reasoning</td><td>3</td><td>Analisis negocio, logica</td></tr>
                    <tr><td>task_management</td><td>3</td><td>Planning, action items</td></tr>
                    <tr><td>summarization</td><td>2</td><td>Resumen, extraccion datos</td></tr>
                    <tr><td>presentation</td><td>2</td><td>Slides, reportes</td></tr>
                </tbody>
            </table>
        </div>
        <div>
            <h3>Que Mide el Score (y que NO mide)</h3>

            <div class="rec-box" style="margin-bottom: 8px;">
                <div class="rec-title" style="color: #39ff14;">SI mide</div>
                <div class="rec-why" style="color: #ffffff; font-size: 8pt;">
                    - Seguimiento de instrucciones<br>
                    - Formato y estructura de la respuesta<br>
                    - Precision de tool calling / function calling<br>
                    - Velocidad de generacion (tok/s)<br>
                    - Latencia hasta primera respuesta<br>
                    - Eficiencia de costo por llamada
                </div>
            </div>

            <div class="rec-box" style="border-color: #ff006e44;">
                <div class="rec-title" style="color: #ff006e;">NO mide (limitaciones)</div>
                <div class="rec-why" style="color: #ffffff; font-size: 8pt;">
                    - Profundidad de razonamiento<br>
                    - Creatividad y originalidad<br>
                    - Precision factual / alucinaciones<br>
                    - Calidad subjetiva del contenido<br>
                    - Rendimiento en contextos muy largos<br>
                    - Consistencia entre multiples runs
                </div>
            </div>

            <div class="note" style="margin-top: 10px;">
                <strong>Sobre la latencia:</strong> Medida desde Chile.
                La latencia absoluta varia segun ubicacion, pero la
                comparacion relativa entre modelos es valida ya que
                todos se miden desde el mismo punto.
                Los tok/s y calidad NO se ven afectados por la ubicacion.
            </div>

            <div class="note">
                <strong>Sobre Claude Opus:</strong> Aparece bajo en el ranking
                general porque el scoring automatico no captura la profundidad
                de su razonamiento. En customer_support sube a #2, demostrando
                que cada modelo tiene su fortaleza.
            </div>
        </div>
    </div>
</div>

<!-- ===== PAGE 3: RANKING GLOBAL ===== -->
<div class="page">
    <h2>Ranking Global - Todos los Modelos</h2>
    <table>
        <thead>
            <tr>
                <th>#</th>
                <th>Modelo</th>
                <th>Score</th>
                <th>tok/s</th>
                <th>Latencia</th>
                <th>Costo/call</th>
                <th>Open Source</th>
            </tr>
        </thead>
        <tbody>
            {ranking_rows()}
        </tbody>
    </table>

    <div class="note">
        <strong>Sobre el scoring:</strong> Evalua formato, estructura, tool calling y velocidad de forma automatica.
        No captura profundidad de razonamiento ni calidad subjetiva del contenido.
        Modelos como Claude Opus destacan en areas que este scoring no mide bien.
    </div>
</div>

<!-- ===== PAGE 4: RANKINGS POR CATEGORIA ===== -->
<div class="page">
    <h2>Rankings por Categoria (Top 5 por area)</h2>

    <div class="two-col">
        <div>
            <h3>Razonamiento (deep reasoning + reasoning)</h3>
            <table>
                <thead><tr><th>#</th><th>Modelo</th><th>Score</th></tr></thead>
                <tbody>
                    <tr class="top3"><td class="rank">1</td><td>DeepSeek V3.2</td><td class="score">7.65</td></tr>
                    <tr class="top3"><td class="rank">2</td><td>Devstral Small</td><td class="score">7.64</td></tr>
                    <tr class="top3"><td class="rank">3</td><td>GPT-4.1</td><td class="score">7.45</td></tr>
                    <tr><td class="rank">4</td><td>GPT-4.1 Mini</td><td>7.36</td></tr>
                    <tr><td class="rank">5</td><td>Gemini 2.5 Flash</td><td>7.30</td></tr>
                </tbody>
            </table>

            <h3>Agentes (tool calling + customer support)</h3>
            <table>
                <thead><tr><th>#</th><th>Modelo</th><th>Score</th></tr></thead>
                <tbody>
                    <tr class="top3"><td class="rank">1</td><td>Devstral Small</td><td class="score">7.21</td></tr>
                    <tr class="top3"><td class="rank">2</td><td>GPT-5.4 Mini</td><td class="score">7.13</td></tr>
                    <tr class="top3"><td class="rank">3</td><td>Claude Opus 4.6</td><td class="score">7.02</td></tr>
                    <tr><td class="rank">4</td><td>Claude Sonnet 4.6</td><td>7.02</td></tr>
                    <tr><td class="rank">5</td><td>Kimi K2</td><td>6.86</td></tr>
                </tbody>
            </table>

            <h3>Codigo</h3>
            <table>
                <thead><tr><th>#</th><th>Modelo</th><th>Score</th></tr></thead>
                <tbody>
                    <tr class="top3"><td class="rank">1</td><td>Devstral Small</td><td class="score">7.65</td></tr>
                    <tr class="top3"><td class="rank">2</td><td>GPT-4.1</td><td class="score">7.37</td></tr>
                    <tr class="top3"><td class="rank">3</td><td>DeepSeek V3.2</td><td class="score">7.34</td></tr>
                    <tr><td class="rank">4</td><td>GPT-4.1 Mini</td><td>7.33</td></tr>
                    <tr><td class="rank">5</td><td>Mistral Large</td><td>7.24</td></tr>
                </tbody>
            </table>
        </div>
        <div>
            <h3>Contenido (content + startup + presentation)</h3>
            <table>
                <thead><tr><th>#</th><th>Modelo</th><th>Score</th></tr></thead>
                <tbody>
                    <tr class="top3"><td class="rank">1</td><td>Devstral Small</td><td class="score">7.37</td></tr>
                    <tr class="top3"><td class="rank">2</td><td>GPT-4.1 Mini</td><td class="score">7.21</td></tr>
                    <tr class="top3"><td class="rank">3</td><td>GPT-4.1</td><td class="score">7.14</td></tr>
                    <tr><td class="rank">4</td><td>DeepSeek V3.2</td><td>7.06</td></tr>
                    <tr><td class="rank">5</td><td>Gemini Flash Lite</td><td>6.96</td></tr>
                </tbody>
            </table>

            <h3>Productividad (task mgmt + summarization)</h3>
            <table>
                <thead><tr><th>#</th><th>Modelo</th><th>Score</th></tr></thead>
                <tbody>
                    <tr class="top3"><td class="rank">1</td><td>Devstral Small</td><td class="score">7.39</td></tr>
                    <tr class="top3"><td class="rank">2</td><td>GPT-4.1</td><td class="score">7.26</td></tr>
                    <tr class="top3"><td class="rank">3</td><td>Gemini Flash Lite</td><td class="score">7.13</td></tr>
                    <tr><td class="rank">4</td><td>DeepSeek V3.2</td><td>7.12</td></tr>
                    <tr><td class="rank">5</td><td>GPT-4.1 Mini</td><td>7.01</td></tr>
                </tbody>
            </table>

            <h3>Datos Estructurados (JSON)</h3>
            <table>
                <thead><tr><th>#</th><th>Modelo</th><th>Score</th></tr></thead>
                <tbody>
                    <tr class="top3"><td class="rank">1</td><td>Devstral Small</td><td class="score">7.33</td></tr>
                    <tr class="top3"><td class="rank">2</td><td>Gemini Flash Lite</td><td class="score">7.33</td></tr>
                    <tr class="top3"><td class="rank">3</td><td>GPT-4.1</td><td class="score">7.22</td></tr>
                    <tr><td class="rank">4</td><td>GPT-4.1 Mini</td><td>7.17</td></tr>
                    <tr><td class="rank">5</td><td>Mistral Large</td><td>7.14</td></tr>
                </tbody>
            </table>
        </div>
    </div>

    <div class="note">
        <strong>Insight clave:</strong> No existe un "mejor modelo para todo". Claude Opus es #3 en Agentes
        pero #16 en JSON. DeepSeek lidera en Razonamiento pero cae en Soporte. Elige segun tu caso de uso.
    </div>
</div>

<!-- ===== PAGE 5: RECOMENDACIONES POR CASO DE USO ===== -->
<div class="page">
    <h2>Que Modelo Usar: Recomendaciones por Caso de Uso</h2>

    <h3>Para Agentes (N8N / OpenClaw)</h3>
    <div class="rec-grid">
        <div class="rec-box">
            <div class="rec-title">Agente Economico</div>
            <div class="rec-model">DeepSeek V3.2</div>
            <div class="rec-why">#4 global, $0.14/$0.28 per M, MIT open-source</div>
        </div>
        <div class="rec-box">
            <div class="rec-title">Agente Rapido</div>
            <div class="rec-model">Devstral Small</div>
            <div class="rec-why">#1 global, 171 tok/s, Apache 2.0</div>
        </div>
        <div class="rec-box">
            <div class="rec-title">Agente con Suscripcion Fija</div>
            <div class="rec-model">MiniMax M2.7</div>
            <div class="rec-why">$20-69/mes, tool calling SOTA, imagenes incluidas</div>
        </div>
    </div>

    <h3>Para Generacion de Contenido</h3>
    <div class="rec-grid">
        <div class="rec-box">
            <div class="rec-title">Blog / Newsletter</div>
            <div class="rec-model">GPT-4.1</div>
            <div class="rec-why">#2 global, excelente en espanol, via API OpenAI</div>
        </div>
        <div class="rec-box">
            <div class="rec-title">Contenido en Espanol</div>
            <div class="rec-model">DeepSeek V3.2</div>
            <div class="rec-why">#4 global, excelente en espanol, $0.14/$0.28 per M</div>
        </div>
        <div class="rec-box">
            <div class="rec-title">Alto Volumen / Batch</div>
            <div class="rec-model">Gemini 2.5 Flash Lite</div>
            <div class="rec-why">212 tok/s, 4.7s latencia, $0.10/$0.40 per M</div>
        </div>
    </div>

    <h3>Para Coding y Automatizacion</h3>
    <div class="rec-grid">
        <div class="rec-box">
            <div class="rec-title">Coding General</div>
            <div class="rec-model">Devstral Small</div>
            <div class="rec-why">#1, especializado en codigo, Apache 2.0</div>
        </div>
        <div class="rec-box">
            <div class="rec-title">Coding Open-Source Local</div>
            <div class="rec-model">MiniMax M2.5</div>
            <div class="rec-why">80.2% SWE-Bench, MIT, cabe en DGX Spark</div>
        </div>
        <div class="rec-box">
            <div class="rec-title">Coding IDE (Cursor/VSCode)</div>
            <div class="rec-model">Qwen3 Coder</div>
            <div class="rec-why">#12, Apache 2.0, bueno para automatizaciones</div>
        </div>
    </div>

    <h3>Para Maxima Calidad (sin importar costo)</h3>
    <div class="rec-grid">
        <div class="rec-box">
            <div class="rec-title">Razonamiento Profundo</div>
            <div class="rec-model">Claude Opus 4.6</div>
            <div class="rec-why">#1 en Arena (1504 Elo), $15/$75 per M</div>
        </div>
        <div class="rec-box">
            <div class="rec-title">Tool Calling Premium</div>
            <div class="rec-model">GPT-5.4 Mini</div>
            <div class="rec-why">Score 7.5 en tool calling, 142 tok/s</div>
        </div>
        <div class="rec-box">
            <div class="rec-title">Open-Source Premium</div>
            <div class="rec-model">Llama 4 Maverick</div>
            <div class="rec-why">#10, empata con Claude Sonnet, open-source</div>
        </div>
    </div>
</div>

<!-- ===== PAGE 4: PRECIOS Y SUSCRIPCIONES ===== -->
<div class="page">
    <h2>Comparativa de Precios y Suscripciones</h2>

    <div class="two-col">
        <div>
            <h3>Pay-as-you-go (por millon de tokens)</h3>
            <table>
                <thead><tr><th>Modelo</th><th>Input/M</th><th>Output/M</th><th>Open Source</th></tr></thead>
                <tbody>
                    <tr><td>Mistral Nemo</td><td>$0.02</td><td>$0.02</td><td class="os-yes">Apache 2.0</td></tr>
                    <tr><td>Devstral Small</td><td>$0.10</td><td>$0.30</td><td class="os-yes">Apache 2.0</td></tr>
                    <tr><td>Gemini Flash Lite</td><td>$0.10</td><td>$0.40</td><td class="os-no">No</td></tr>
                    <tr><td>DeepSeek V3.2</td><td>$0.14</td><td>$0.28</td><td class="os-yes">MIT</td></tr>
                    <tr><td>MiniMax M2.7</td><td>$0.30</td><td>$1.20</td><td class="os-partial">Parcial</td></tr>
                    <tr><td>GPT-4.1 Mini</td><td>$0.40</td><td>$1.60</td><td class="os-no">No</td></tr>
                    <tr><td>Llama 4 Maverick</td><td>$0.50</td><td>$1.00</td><td class="os-yes">Llama</td></tr>
                    <tr><td>GPT-4.1</td><td>$2.00</td><td>$8.00</td><td class="os-no">No</td></tr>
                    <tr><td>GPT-4o</td><td>$2.50</td><td>$10.00</td><td class="os-no">No</td></tr>
                    <tr><td>Claude Sonnet 4.6</td><td>$3.00</td><td>$15.00</td><td class="os-no">No</td></tr>
                    <tr><td>Claude Opus 4.6</td><td>$15.00</td><td>$75.00</td><td class="os-no">No</td></tr>
                </tbody>
            </table>
        </div>
        <div>
            <h3>Suscripciones Mensuales Fijas</h3>
            <table>
                <thead><tr><th>Servicio</th><th>Precio</th><th>Mejor Modelo</th></tr></thead>
                <tbody>
                    <tr><td>MiniMax Starter</td><td>$10/mes</td><td>M2.1</td></tr>
                    <tr><td>Mistral Le Chat</td><td>~$15/mes</td><td>Mistral Large</td></tr>
                    <tr><td>MiniMax Agent Pro</td><td>$19/mes</td><td>M2.7</td></tr>
                    <tr><td>Google AI Pro</td><td>$20/mes</td><td>Gemini 2.5 Pro</td></tr>
                    <tr><td>ChatGPT Plus</td><td>$20/mes</td><td>GPT-4o</td></tr>
                    <tr><td>MiniMax Coding Plus</td><td>$20/mes</td><td>M2.1</td></tr>
                    <tr><td>Ollama Cloud Pro</td><td>$20/mes</td><td>Todos open-source</td></tr>
                    <tr><td>Claude Pro</td><td>$20/mes</td><td>Sonnet 4.5 (solo chat)</td></tr>
                    <tr><td>SuperGrok</td><td>$30/mes</td><td>Grok 4.20</td></tr>
                    <tr><td>Qwen Coding Pro</td><td>$50/mes</td><td>Qwen-Coder-Max</td></tr>
                    <tr><td>MiniMax Agent Pro+</td><td>$69/mes</td><td>M2.7</td></tr>
                    <tr><td>Ollama Cloud Max</td><td>$100/mes</td><td>Todos open-source</td></tr>
                    <tr><td>ChatGPT Pro</td><td>$200/mes</td><td>GPT-5.2, o3</td></tr>
                </tbody>
            </table>
        </div>
    </div>
</div>

<!-- ===== PAGE 5: ESTRATEGIA LOCAL + NUBE ===== -->
<div class="page">
    <h2>Estrategia Local + Nube (NVIDIA DGX Spark 128GB)</h2>

    <h3>Modelos Open-Source para Correr Local</h3>
    <table>
        <thead><tr><th>Modelo</th><th>RAM</th><th>Licencia</th><th>Calidad</th><th>Contexto</th><th>Ideal para</th></tr></thead>
        <tbody>
            <tr><td>Gemma 4 E4B</td><td>4 GB</td><td>Apache 2.0</td><td>Buena</td><td>128K</td><td>Edge/mobile</td></tr>
            <tr><td>Mistral Nemo 12B</td><td>8 GB</td><td>Apache 2.0</td><td>Buena</td><td>128K</td><td>Tareas simples</td></tr>
            <tr><td>Phi-4 14B</td><td>10 GB</td><td>MIT</td><td>Buena</td><td>16K</td><td>Razonamiento compacto</td></tr>
            <tr><td>Gemma 4 26B MoE</td><td>16 GB</td><td>Apache 2.0</td><td>Muy buena</td><td>256K</td><td>Solo 3.8B activos, rapido</td></tr>
            <tr><td>Qwen 3.5 25B</td><td>16 GB</td><td>Apache 2.0</td><td>Muy buena</td><td>128K</td><td>General, multiidioma</td></tr>
            <tr><td>Gemma 4 31B</td><td>20 GB</td><td>Apache 2.0</td><td>Excelente</td><td>256K</td><td>#3 open en Arena</td></tr>
            <tr><td>Llama 3.3 70B</td><td>40 GB</td><td>Llama</td><td>Muy buena</td><td>128K</td><td>Clasico confiable</td></tr>
            <tr><td>Qwen 3.5 72B</td><td>42 GB</td><td>Apache 2.0</td><td>Excelente</td><td>128K</td><td>Top coding local</td></tr>
            <tr><td>Llama 4 Maverick</td><td>~60 GB</td><td>Llama</td><td>Excelente</td><td>128K</td><td>Multimodal</td></tr>
            <tr><td>MiniMax M2.5</td><td>~90 GB</td><td>MIT</td><td>Excelente</td><td>128K</td><td>80.2% SWE-Bench</td></tr>
        </tbody>
    </table>

    <h3>Regla de Routing: Cuando Usar Local vs Nube</h3>
    <div class="rec-grid">
        <div class="rec-box">
            <div class="rec-title">Usar LOCAL cuando</div>
            <div class="rec-why" style="color: #39ff14;">
                - Privacidad es critica<br>
                - No hay internet confiable<br>
                - Coding/debug largo<br>
                - Presupuesto $0<br>
                - Fine-tuning necesario
            </div>
        </div>
        <div class="rec-box">
            <div class="rec-title">Usar NUBE cuando</div>
            <div class="rec-why" style="color: #00d4ff;">
                - Velocidad maxima (Devstral 171 tok/s)<br>
                - Tool calling para agentes<br>
                - Contexto >128K tokens<br>
                - Imagenes/audio (MiniMax)<br>
                - Fallback si local falla
            </div>
        </div>
        <div class="rec-box">
            <div class="rec-title">Combo Optimo ($0/mes)</div>
            <div class="rec-why" style="color: #ffffff;">
                <strong>Local:</strong> Gemma 4 26B MoE (rapido)<br>
                + Qwen 3.5 72B (calidad)<br>
                <strong>Nube:</strong> DeepSeek V3.2 (backup)<br>
                Costo: $0 + electricidad
            </div>
        </div>
    </div>

    <h3>Escenarios de Costo</h3>
    <table>
        <thead><tr><th>Escenario</th><th>Local</th><th>Nube</th><th>Costo/mes</th></tr></thead>
        <tbody>
            <tr><td>Solo local, independencia total</td><td>Gemma 4 + Qwen 72B</td><td>Ninguna</td><td><strong>$0</strong></td></tr>
            <tr><td>Local + backup nube</td><td>Qwen 72B</td><td>DeepSeek V3.2 paygo</td><td><strong>~$5</strong></td></tr>
            <tr><td>Agente 24/7 alta calidad</td><td>MiniMax M2.5</td><td>MiniMax Agent Pro</td><td><strong>$19</strong></td></tr>
            <tr><td>Maximo rendimiento</td><td>MiniMax M2.5</td><td>OpenRouter + Qwen Pro</td><td><strong>~$65</strong></td></tr>
        </tbody>
    </table>
</div>

<!-- ===== PAGE 6: PROVEEDORES ===== -->
<div class="page">
    <h2>Mapa de Proveedores</h2>

    <div class="two-col">
        <div>
            <h3>Propietarios</h3>
            <table>
                <thead><tr><th>Proveedor</th><th>Pais</th><th>Mejor Modelo</th><th>Fortaleza</th></tr></thead>
                <tbody>
                    <tr><td>OpenAI</td><td>USA</td><td>GPT-4.1</td><td>Tool calling, ecosistema</td></tr>
                    <tr><td>Anthropic</td><td>USA</td><td>Opus 4.6</td><td>Razonamiento, coding</td></tr>
                    <tr><td>Google</td><td>USA</td><td>Gemini 2.5 Pro</td><td>Velocidad, multimodal</td></tr>
                    <tr><td>xAI</td><td>USA</td><td>Grok 4.20</td><td>RPM alto, X integration</td></tr>
                    <tr><td>Moonshot</td><td>China</td><td>Kimi K2</td><td>Contexto largo</td></tr>
                </tbody>
            </table>

            <h3>Open Source</h3>
            <table>
                <thead><tr><th>Proveedor</th><th>Pais</th><th>Mejor Modelo</th><th>Licencia</th></tr></thead>
                <tbody>
                    <tr><td>Mistral</td><td>Francia</td><td>Devstral (#1!)</td><td>Apache 2.0</td></tr>
                    <tr><td>DeepSeek</td><td>China</td><td>V3.2</td><td>MIT</td></tr>
                    <tr><td>Meta</td><td>USA</td><td>Llama 4 Maverick</td><td>Llama Community</td></tr>
                    <tr><td>Alibaba</td><td>China</td><td>Qwen 3.6 Plus</td><td>Apache 2.0</td></tr>
                    <tr><td>Google</td><td>USA</td><td>Gemma 4 31B</td><td>Apache 2.0</td></tr>
                    <tr><td>MiniMax</td><td>China</td><td>M2.5 (MIT)</td><td>MIT</td></tr>
                    <tr><td>Microsoft</td><td>USA</td><td>Phi-4</td><td>MIT</td></tr>
                </tbody>
            </table>
        </div>
        <div>
            <h3>Infraestructura (sirven modelos)</h3>
            <table>
                <thead><tr><th>Servicio</th><th>Ventaja</th><th>Modelos</th></tr></thead>
                <tbody>
                    <tr><td>OpenRouter</td><td>1 API key, 290+ modelos</td><td>Todos</td></tr>
                    <tr><td>Ollama</td><td>Local + Cloud</td><td>Open-source</td></tr>
                    <tr><td>Groq</td><td>544 tok/s (LPU)</td><td>Llama, Mixtral</td></tr>
                    <tr><td>Cerebras</td><td>1800 tok/s record</td><td>Llama</td></tr>
                </tbody>
            </table>

            <h3>Rate Limits (riesgo de corte)</h3>
            <table>
                <thead><tr><th>Proveedor</th><th>RPM</th><th>TPM</th><th>Riesgo</th></tr></thead>
                <tbody>
                    <tr><td>Qwen (Alibaba)</td><td>15,000</td><td>10M</td><td class="os-yes">Muy bajo</td></tr>
                    <tr><td>xAI</td><td>1,200</td><td>-</td><td class="os-yes">Bajo</td></tr>
                    <tr><td>Google Gemini</td><td>1,000</td><td>4M</td><td class="os-yes">Bajo</td></tr>
                    <tr><td>OpenAI</td><td>500</td><td>800K</td><td class="os-yes">Bajo</td></tr>
                    <tr><td>Ollama (local)</td><td>Ilimitado</td><td>Ilimitado</td><td class="os-yes">Ninguno</td></tr>
                    <tr><td>Groq</td><td>30</td><td>100K</td><td class="os-no">Alto</td></tr>
                </tbody>
            </table>

            <div class="note" style="margin-top: 15px;">
                <strong>Tip:</strong> Para agentes N8N/OpenClaw, usa OpenRouter con fallback automatico:
                Devstral -> DeepSeek V3.2 -> Llama 3.3 (gratis).
                Una sola API key para todo.
            </div>
        </div>
    </div>

    <div class="footer-url" style="margin-top: 20px;">
        cristiantala.com | {month_name} {year}
    </div>
</div>

</body>
</html>"""

# Generar PDF con mes en el nombre
output_dir = Path("cheatsheet")
output_dir.mkdir(exist_ok=True)

html_file = output_dir / f"cheatsheet_{year}_{now.strftime('%m')}.html"
pdf_file = output_dir / f"AI_Model_Benchmark_CheatSheet_{month_name}_{year}.pdf"

with open(html_file, "w") as f:
    f.write(html_content)

HTML(string=html_content).write_pdf(str(pdf_file))

print(f"PDF generado: {pdf_file}")
print(f"HTML guardado: {html_file}")
