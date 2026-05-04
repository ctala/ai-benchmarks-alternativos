#!/usr/bin/env python3
"""
Genera el CheatSheet PDF con branding de cristiantala.com
Usa WeasyPrint para convertir HTML a PDF.
"""

import json
import locale
from datetime import datetime
from pathlib import Path
from weasyprint import HTML

# Forzar locale español para mes (Mayo en lugar de May)
try:
    locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
except locale.Error:
    try:
        locale.setlocale(locale.LC_TIME, "es_CL.UTF-8")
    except locale.Error:
        pass  # fallback a inglés

now = datetime.now()
_MONTHS_ES = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
    5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre",
}
month_name = _MONTHS_ES.get(now.month, now.strftime("%B"))
year = now.year

# Cargar resultados — soporta ambos formatos: list directa (legacy) y
# {"results": [...], "metadata": {}} (formato nuevo del runner desde abril 2026)
all_results = []
for f in sorted(Path("benchmarks/results").glob("benchmark_*.json")):
    with open(f) as fh:
        data = json.load(fh)
        all_results.extend(data if isinstance(data, list) else data.get("results", []))

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
    <p style="font-family: 'JetBrains Mono', monospace; font-size: 22pt; font-weight: 700; color: #ff006e; text-shadow: 0 0 12px rgba(255,0,110,0.6); margin-top: 8px; margin-bottom: 8px; letter-spacing: 2px;">{month_name} {year}</p>
    <p class="meta">{len(ranked)} modelos con cobertura | {len(seen):,}+ tests reales | v2.6.0</p>
    <div class="stats">
        <div class="stat-box">
            <span class="stat-number">{len(ranked)}</span>
            <span class="stat-label">Modelos</span>
        </div>
        <div class="stat-box">
            <span class="stat-number">25</span>
            <span class="stat-label">Suites</span>
        </div>
        <div class="stat-box">
            <span class="stat-number">148</span>
            <span class="stat-label">Tests/modelo</span>
        </div>
        <div class="stat-box">
            <span class="stat-number">{len(seen):,}+</span>
            <span class="stat-label">Runs totales</span>
        </div>
    </div>
    <p class="meta" style="margin-top: 15px;">Medido desde Santiago, Chile | 8 providers (OpenRouter, OpenAI, Anthropic, Groq, NVIDIA NIM, Xiaomi, Ollama Cloud, MiniMax)</p>

    <div style="margin-top: 18px; text-align: left; max-width: 650px; background: #1a0a2e; border: 1px solid #39ff1444; border-radius: 6px; padding: 10px 14px;">
        <p style="font-family: 'JetBrains Mono', monospace; color: #00d4ff; font-size: 9pt; margin-bottom: 5px;">Como se calcula el Score (v2.6.0, mayo 2026)</p>
        <p style="font-size: 8pt; color: #b0b0b0; line-height: 1.5;">
            <span style="color:#39ff14; font-family:'JetBrains Mono',monospace;">50%</span> Calidad (formato + sustancia + LLM-as-Judge Phi-4 local, MIT)<br>
            <span style="color:#39ff14; font-family:'JetBrains Mono',monospace;">20%</span> Costo (curva log inversa: $0.001/call=8.0, $0.01=5.0, $0.10=2.0)<br>
            <span style="color:#39ff14; font-family:'JetBrains Mono',monospace;">15%</span> Tool Calling (precision de function calling para agentes)<br>
            <span style="color:#39ff14; font-family:'JetBrains Mono',monospace;">7.5%</span> Velocidad (tokens por segundo)<br>
            <span style="color:#39ff14; font-family:'JetBrains Mono',monospace;">7.5%</span> Latencia (tiempo hasta primera respuesta)
        </p>
        <p style="font-size: 7pt; color: #ff006e; margin-top: 5px;">
            Nota: El scoring automatico tiene limitaciones. No captura profundidad subjetiva
            de razonamiento ni calidad editorial humana. Ver pagina de Metodologia.
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
                    <tr><td>Modelos evaluados</td><td><strong>{len(ranked)} modelos unicos con cobertura</strong></td></tr>
                    <tr><td>Tests por modelo</td><td><strong>91 single-turn (23 suites) + 12 agent_long_horizon + 45 niah_es_lite</strong></td></tr>
                    <tr><td>Runs ejecutados</td><td><strong>{len(seen):,}+ runs preservados</strong></td></tr>
                    <tr><td>Ubicacion</td><td>Santiago, Chile</td></tr>
                    <tr><td>APIs/Providers usados</td><td>OpenRouter, OpenAI, Anthropic, Groq, NVIDIA NIM, Xiaomi MiMo, Ollama Cloud, MiniMax</td></tr>
                    <tr><td>Juez LLM-as-Judge</td><td>Phi-4 14B local (Microsoft, MIT) — cero conflicto de interes</td></tr>
                    <tr><td>Temperatura</td><td>0.7 (default para no-thinking)</td></tr>
                    <tr><td>Max tokens</td><td>2048 base, x4 multiplier para thinking models</td></tr>
                    <tr><td>Timeout HTTP</td><td>360s read timeout</td></tr>
                    <tr><td>Snapshot</td><td>{month_name} {year}</td></tr>
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
                    <tr><td>hallucination</td><td>3</td><td>Precision factual, trampas</td></tr>
                    <tr><td>creativity</td><td>4</td><td>Originalidad, cliches, profundidad</td></tr>
                </tbody>
            </table>
        </div>
        <div>
            <h3>Que Mide el Score (y que NO mide)</h3>

            <div class="rec-box" style="margin-bottom: 8px;">
                <div class="rec-title" style="color: #39ff14;">SI mide (13 suites, 48 tests)</div>
                <div class="rec-why" style="color: #ffffff; font-size: 8pt;">
                    - Seguimiento de instrucciones y formato<br>
                    - Precision de tool calling / function calling<br>
                    - Creatividad y originalidad (penaliza cliches)<br>
                    - Precision factual / alucinaciones (trampas verificables)<br>
                    - Soporte al cliente (empatia, seguridad)<br>
                    - Salida JSON estructurada<br>
                    - Velocidad (tok/s) y latencia<br>
                    - Eficiencia de costo por llamada
                </div>
            </div>

            <div class="rec-box" style="border-color: #ff006e44;">
                <div class="rec-title" style="color: #ff006e;">NO mide (limitaciones)</div>
                <div class="rec-why" style="color: #ffffff; font-size: 8pt;">
                    - Profundidad subjetiva de razonamiento<br>
                    - Calidad editorial humana del contenido<br>
                    - Rendimiento en contextos muy largos (>128K)<br>
                    - Consistencia entre multiples runs<br>
                    - Rendimiento multimodal (imagenes/audio)
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
                <strong>Sobre Claude Opus:</strong> Sube a #9 global gracias
                a los tests de honestidad (Sonnet #1) y soporte al cliente (Opus #3 en agentes).
                Cada modelo tiene su fortaleza segun el caso de uso.
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
        Ver pagina de Metodologia para detalles de que mide y que no mide.
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

    <h3>Alucinaciones (precision factual)</h3>
    <table>
        <thead><tr><th>#</th><th>Modelo</th><th>Score</th><th>Notas</th></tr></thead>
        <tbody>
            <tr class="top3"><td class="rank">1</td><td>Claude Sonnet 4.6</td><td class="score">7.62</td><td>Mas honesto del benchmark</td></tr>
            <tr class="top3"><td class="rank">2</td><td>Mistral Large</td><td class="score">7.52</td><td>Muy confiable</td></tr>
            <tr class="top3"><td class="rank">3</td><td>Gemini Flash Lite</td><td class="score">7.47</td><td>Rapido Y honesto</td></tr>
            <tr><td class="rank">4</td><td>Claude Opus 4.6</td><td>7.45</td><td>Anthropic = honestidad</td></tr>
            <tr><td class="rank">...</td><td>MiniMax M2.7</td><td>7.02</td><td></td></tr>
            <tr><td class="rank">...</td><td style="color:#ff006e">Qwen 3.6 Plus</td><td style="color:#ff006e">6.50</td><td style="color:#ff006e">Mas propenso a alucinar</td></tr>
        </tbody>
    </table>

    <h3>Creatividad y originalidad</h3>
    <table>
        <thead><tr><th>#</th><th>Modelo</th><th>Score</th><th>Notas</th></tr></thead>
        <tbody>
            <tr class="top3"><td class="rank">1</td><td>Devstral Small</td><td class="score">6.93</td><td>Menos cliches</td></tr>
            <tr class="top3"><td class="rank">2</td><td>Gemini 2.5 Flash</td><td class="score">6.85</td><td>Sorprendente creatividad</td></tr>
            <tr class="top3"><td class="rank">3</td><td>DeepSeek V3.2</td><td class="score">6.75</td><td>Bueno y barato</td></tr>
            <tr><td class="rank">...</td><td>Claude Opus 4.6</td><td>6.47</td><td></td></tr>
            <tr><td class="rank">...</td><td style="color:#ff006e">GPT-5.4</td><td style="color:#ff006e">5.56</td><td style="color:#ff006e">Generico</td></tr>
            <tr><td class="rank">...</td><td style="color:#ff006e">MiniMax M2.7</td><td style="color:#ff006e">5.19</td><td style="color:#ff006e">Muy generico, cliches</td></tr>
        </tbody>
    </table>

    <div class="note">
        <strong>Insight clave:</strong> No existe un "mejor modelo para todo". Claude es #1 en honestidad
        pero #16 en JSON. MiniMax es bueno para agentes pero ultimo en creatividad. Elige segun tu caso de uso.
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
                Devstral -> DeepSeek V4 Flash NIM (gratis) -> MiMo V2.5 Xiaomi sub.
                Una sola API key para top 3 vias por costo.
            </div>
        </div>
    </div>

    <div class="footer-url" style="margin-top: 20px;">
        cristiantala.com | {month_name} {year}
    </div>
</div>

<!-- ===== INSIGHTS DESTACADOS DEL MES ===== -->
<div class="page">
    <h2>Hallazgos clave de {month_name} {year}</h2>
    <p style="margin-bottom: 12px; font-size: 9pt; color: #b0b0b0;">
        Insights cuantitativos del benchmark v2.6.0 — basados en {len(seen):,}+ runs reales en {len(ranked)} modelos.
    </p>

    <div class="two-col">
        <div>
            <h3>1. Provider matters cuantificado</h3>
            <p style="font-size: 9pt;">
                Mismo modelo en provider directo vs OpenRouter: <strong>+0.16 a +0.25 puntos</strong>.
                Confirmado en 4 proveedores (Xiaomi direct, Groq direct, NIM gratis, MiniMax direct).
                Para producción: <strong>provider directo siempre cuando esté disponible</strong>.
            </p>

            <h3>2. Thinking forzado EMPEORA agéntica multi-turn</h3>
            <p style="font-size: 9pt;">
                En 8/9 modelos hybrid medidos con <code>reasoning=high</code> en agent_long_horizon,
                el score baja vs sin thinking: Opus 4.7 -0.67, Sonnet 4.6 -0.50, Hermes 4 70B -0.54.
                Solo Kimi K2.5 sube (+0.73). <strong>Para N8N/OpenClaw: NO actives thinking default</strong>.
            </p>

            <h3>3. Why Opus 4.7 NO está en top 10 de nuestro benchmark</h3>
            <p style="font-size: 9pt;">
                Opus 4.7 saca quality 8.08 (top 6 entre todos), pero <strong>40-100x mas caro y 5-10x mas lento</strong>
                que las alternativas. El score compuesto pondera costo+speed → cae fuera del top 10.
                Para investigación académica: <strong>SI uses Opus</strong>. Para producción a volumen LATAM con presupuesto: alternativas top.
            </p>

            <h3>4. Modelo gigante NO siempre gana</h3>
            <p style="font-size: 9pt;">
                Mistral Large 3 (675B params) saca 6.89. Nemotron Nano 9B v2 saca 6.91.
                <strong>Modelo 75x más pequeño rinde más</strong> en NIM benchmark.
            </p>
        </div>
        <div>
            <h3>5. "1M context declarado" ≠ retrieval efectivo</h3>
            <p style="font-size: 9pt;">
                Solo <strong>GPT-4.1 procesa 1M tokens efectivamente</strong> via OpenAI/OpenRouter.
                Llama 4 Scout (10M declarado), DeepSeek V4 Flash (1M), Gemini 3.1 Pro (1M) —
                todos cap por sus providers a 128K-256K real.
            </p>

            <h3>6. DeepSeek V4 Pro NIM NO funciona en producción</h3>
            <p style="font-size: 9pt;">
                Cascada 504 reproducible <strong>2 veces</strong> (28 abril + 3 mayo). NIM gateway
                no maneja modelo gigante con prompts largos. Para V4 Pro:
                <strong>OpenRouter pagado o Ollama Cloud sub</strong> (97% éxito).
            </p>

            <h3>7. MiMo Xiaomi sub family — mejor C/B en español</h3>
            <p style="font-size: 9pt;">
                <strong>4 modelos MiMo en top 10</strong> (V2-Omni, V2.5, V2.5-Pro, V2-Flash).
                Sub $14/mes da acceso a 4 modelos competentes con español neutro fuerte.
                Mejor opción para emprendedores LATAM con presupuesto fijo predecible.
            </p>

            <h3>8. Devstral Small lidera NIAH-ES</h3>
            <p style="font-size: 9pt;">
                Specialist coding model gana retrieval en español neutro: <strong>7.25 vs Opus 4.7 4.98</strong>.
                <strong>+2.27 puntos a 1/450 del costo</strong>. Para tasks de extracción de info
                con contexto &lt;128K: Devstral es la mejor opción.
            </p>

            <h3>9. Limitación honesta: NO medimos debugging real</h3>
            <p style="font-size: 9pt;">
                Caso reportado: MiniMax M2.7 NO pudo resolver bug en VPS Hetzner. Opus 4.7 sí en minutos.
                Para debugging agentic real (Docker, K8s, networking), <strong>mira SWE-bench Verified</strong>
                (Opus 4.7 = 87.6% top 1 globalmente).
            </p>
        </div>
    </div>

    <div class="note" style="margin-top: 15px;">
        <strong>📍 Recordatorio importante</strong>: este benchmark NO sustituye a los oficiales (HumanEval, MMLU, GSM8K, SWE-bench, NIAH inglés). Es un <strong>complemento</strong> para emprendedores hispanohablantes que deciden producción real (N8N, OpenClaw, Hermes, blogs LATAM, agentes). Para investigación académica: prioriza los oficiales. Para producción aplicada en español: este suma datos no cubiertos por los académicos (costo provider real, latencia LATAM, español neutro, agentes multi-turno).
    </div>

    <div class="footer-url" style="margin-top: 20px;">
        cristiantala.com | {month_name} {year} | github.com/ctala/ai-benchmarks-alternativos
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
