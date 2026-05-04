#!/usr/bin/env python3
"""
Genera el CheatSheet PDF mensual del benchmark.

Reescritura limpia (mayo 2026) reemplazando generate_pdf.py legacy.
Cambios vs legacy:
- Data-driven (sin hardcodes de v1.0)
- Mes en español (Enero/Febrero/.../Diciembre)
- Mayo destacado en cover con color
- 9+ secciones reordenadas para valor descendente
- Suscripciones incluyen MiMo Xiaomi $14, Ollama Cloud $30, MiniMax $19, Anthropic $20
- Estrategia local generalizada por VRAM (8/16/24/32/128GB)
- Mapa de proveedores actualizado
- Hallazgos con fechas
- Pagina final con CTA + QR a calculadora + comunidad Skool
- "Guiño" en cada ranking: ver completo en repo/calculadora
"""

import base64
import io
import json
from datetime import datetime
from pathlib import Path
from collections import defaultdict

import qrcode
from weasyprint import HTML

ROOT = Path(__file__).parent.parent

_MONTHS_ES = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
    5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre",
}

now = datetime.now()
MONTH = _MONTHS_ES[now.month]
YEAR = now.year

URL_CALC = "https://benchmarks.cristiantala.com/"
URL_REPO = "https://github.com/ctala/ai-benchmarks-alternativos"
URL_SKOOL = "https://www.skool.com/cagala-aprende-repite"


def qr_b64(url: str, size: int = 200) -> str:
    """QR code as base64 PNG embedable."""
    qr = qrcode.QRCode(border=1, box_size=8)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#0a0a1a", back_color="#39ff14")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode()


# ============================================================
# CARGA DE DATOS
# ============================================================

def load_models() -> dict:
    """Carga docs/data/models.json (single source of truth)."""
    p = ROOT / "docs" / "data" / "models.json"
    return json.loads(p.read_text())


def load_runs() -> list:
    """Carga todos los runs preservados (para counts agregados)."""
    runs_dir = ROOT / "benchmarks" / "results"
    all_runs = []
    seen = set()
    for f in sorted(runs_dir.glob("benchmark_*.json")):
        try:
            data = json.loads(f.read_text())
            results = data if isinstance(data, list) else data.get("results", [])
            for r in results:
                key = f"{r.get('model_id','?')}|{r.get('test_name','?')}|{r.get('timestamp','?')}"
                if key not in seen:
                    seen.add(key)
                    all_runs.append(r)
        except Exception:
            continue
    return all_runs


# ============================================================
# RENDER
# ============================================================

CSS = """
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Inter:wght@400;600;700&display=swap');

@page {
    size: A4 landscape;
    margin: 10mm;
    background: #0a0a1a;
    @bottom-center {
        content: "cristiantala.com | Benchmark de Modelos AI | """ + MONTH + ' ' + str(YEAR) + """";
        font-family: 'Inter', sans-serif;
        font-size: 8pt;
        color: #b0b0b0;
    }
    @bottom-right {
        content: counter(page) " / " counter(pages);
        font-family: 'JetBrains Mono', monospace;
        font-size: 8pt;
        color: #39ff14;
    }
}

* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { background: #0a0a1a; }
body {
    font-family: 'Inter', sans-serif;
    color: #ffffff;
    font-size: 9pt;
    line-height: 1.4;
}

.page {
    page-break-after: always;
    padding: 5mm;
    min-height: 175mm;
}
.page:last-child { page-break-after: auto; }

h1, h2, h3, h4 { font-family: 'JetBrains Mono', monospace; }

h2 {
    color: #39ff14;
    font-size: 16pt;
    border-bottom: 2px solid #39ff14;
    padding-bottom: 6px;
    margin-bottom: 12px;
}
h3 {
    color: #00d4ff;
    font-size: 11pt;
    margin-top: 12px;
    margin-bottom: 6px;
}
h4 {
    color: #b59cff;
    font-size: 9.5pt;
    margin-top: 8px;
    margin-bottom: 4px;
}

p { margin-bottom: 6px; }

table {
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0;
    font-size: 8.5pt;
}
th {
    background: #1a0a2e;
    color: #39ff14;
    font-family: 'JetBrains Mono', monospace;
    font-size: 8pt;
    text-align: left;
    padding: 6px;
    border-bottom: 1px solid #533483;
}
td {
    padding: 5px 6px;
    border-bottom: 1px solid #1a0a2e;
    color: #e0e0e0;
}
tbody tr:nth-child(even) { background: rgba(26, 10, 46, 0.5); }

.two-col { display: flex; gap: 14px; }
.two-col > div { flex: 1; }

.three-col { display: flex; gap: 12px; }
.three-col > div { flex: 1; }

.note {
    background: #1a0a2e;
    border-left: 3px solid #ff006e;
    padding: 8px 12px;
    margin: 10px 0;
    font-size: 8.5pt;
    border-radius: 0 4px 4px 0;
}
.tip {
    background: rgba(57, 255, 20, 0.08);
    border-left: 3px solid #39ff14;
    padding: 8px 12px;
    margin: 10px 0;
    font-size: 8.5pt;
    border-radius: 0 4px 4px 0;
}
.warning {
    background: rgba(255, 0, 110, 0.08);
    border-left: 3px solid #ff006e;
    padding: 8px 12px;
    margin: 10px 0;
    font-size: 8.5pt;
    border-radius: 0 4px 4px 0;
}

.os-yes { color: #39ff14; font-weight: 600; }
.os-no { color: #ff006e; font-weight: 600; }

code { font-family: 'JetBrains Mono', monospace; color: #00d4ff; font-size: 8.5pt; }
strong { color: #ffffff; }

.guino {
    text-align: center;
    font-size: 8pt;
    color: #b59cff;
    font-style: italic;
    margin-top: 8px;
}

/* COVER */
.cover {
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 175mm;
    text-align: center;
    background: linear-gradient(180deg, #0a0a1a 0%, #1a0a2e 50%, #0a0a1a 100%);
}
.cover h1 {
    font-family: 'JetBrains Mono', monospace;
    font-size: 38pt;
    color: #39ff14;
    text-shadow: 0 0 16px rgba(57, 255, 20, 0.5);
    margin-bottom: 6px;
}
.cover .subtitle {
    font-family: 'JetBrains Mono', monospace;
    font-size: 14pt;
    color: #00d4ff;
    margin-bottom: 18px;
}
.cover .month {
    font-family: 'JetBrains Mono', monospace;
    font-size: 26pt;
    font-weight: 700;
    color: #ff006e;
    text-shadow: 0 0 18px rgba(255, 0, 110, 0.6);
    letter-spacing: 3px;
    margin: 8px 0 16px;
    padding: 10px 24px;
    border: 2px solid #ff006e;
    border-radius: 6px;
    display: inline-block;
}
.cover .meta {
    font-size: 10pt;
    color: #b0b0b0;
    margin-bottom: 14px;
}
.cover .stats {
    display: flex;
    gap: 30px;
    margin: 18px 0;
}
.cover .stat-box {
    text-align: center;
    background: #1a0a2e;
    border: 1px solid #533483;
    border-radius: 6px;
    padding: 12px 18px;
    min-width: 100px;
}
.cover .stat-number {
    font-family: 'JetBrains Mono', monospace;
    font-size: 20pt;
    font-weight: 700;
    color: #39ff14;
    display: block;
}
.cover .stat-label {
    font-size: 8pt;
    color: #b0b0b0;
    text-transform: uppercase;
    letter-spacing: 1px;
}
.score-formula {
    margin-top: 18px;
    text-align: left;
    max-width: 700px;
    background: #1a0a2e;
    border: 1px solid #39ff1444;
    border-radius: 6px;
    padding: 12px 16px;
}
.score-formula .title {
    font-family: 'JetBrains Mono', monospace;
    color: #00d4ff;
    font-size: 9pt;
    margin-bottom: 6px;
}
.score-formula .row {
    font-size: 8.5pt;
    color: #b0b0b0;
    line-height: 1.6;
}
.score-formula .pct {
    color: #39ff14;
    font-family: 'JetBrains Mono', monospace;
    font-weight: 700;
    margin-right: 6px;
}

/* QR */
.qr-container {
    display: flex;
    justify-content: center;
    gap: 40px;
    margin: 20px 0;
}
.qr-box {
    text-align: center;
    background: #1a0a2e;
    border: 1px solid #533483;
    border-radius: 8px;
    padding: 16px;
    width: 220px;
}
.qr-box img {
    width: 180px;
    height: 180px;
    border-radius: 4px;
}
.qr-box .qr-label {
    font-family: 'JetBrains Mono', monospace;
    color: #39ff14;
    font-size: 10pt;
    margin-top: 10px;
    margin-bottom: 4px;
}
.qr-box .qr-url {
    font-family: 'JetBrains Mono', monospace;
    color: #00d4ff;
    font-size: 7pt;
    word-break: break-all;
}
"""


def render(models: dict, runs: list) -> str:
    """Renderiza el HTML completo del cheatsheet."""

    # Métricas agregadas
    ranked = [m for m in models["models"] if m.get("score_global") is not None and m.get("runs", 0) >= 50]
    ranked.sort(key=lambda x: -x["score_global"])
    total_runs = sum(m.get("runs", 0) for m in models["models"])

    # Top 10 score compuesto
    top10 = ranked[:10]
    # Top 10 quality only (sin pesar costo)
    top_quality = sorted(ranked, key=lambda x: -(x.get("quality_avg") or 0))[:10]

    # Top NIAH-ES (modelos con suite niah_es o niah_es_lite)
    niah_models = []
    for m in models["models"]:
        suites = m.get("score_by_suite", {}) or {}
        niah_scores = [v for k, v in suites.items() if "niah" in k]
        if niah_scores:
            niah_models.append({
                "name": m["name"],
                "niah_avg": round(sum(niah_scores) / len(niah_scores), 2),
            })
    niah_models.sort(key=lambda x: -x["niah_avg"])

    # Top agent_long_horizon
    alh_models = []
    for m in models["models"]:
        suites = m.get("score_by_suite", {}) or {}
        if "agent_long_horizon" in suites:
            alh_models.append({"name": m["name"], "alh": suites["agent_long_horizon"]})
    alh_models.sort(key=lambda x: -x["alh"])

    qr_calc = qr_b64(URL_CALC)
    qr_skool = qr_b64(URL_SKOOL)

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>AI Model Benchmark CheatSheet — {MONTH} {YEAR}</title>
<style>{CSS}</style>
</head>
<body>

<!-- ============================================================ -->
<!-- COVER (P1) -->
<!-- ============================================================ -->
<div class="cover">
    <h1>AI Model Benchmark</h1>
    <div class="subtitle">Guia para Emprendedores Hispanohablantes</div>
    <div class="month">{MONTH} {YEAR}</div>
    <p class="meta">{len(ranked)} modelos con cobertura ≥50 runs · {total_runs:,}+ runs preservados · v2.6.0</p>

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
            <span class="stat-number">{total_runs:,}+</span>
            <span class="stat-label">Runs totales</span>
        </div>
    </div>

    <p class="meta">Medido desde Santiago, Chile · 8 providers (OpenRouter, OpenAI, Anthropic, Groq, NVIDIA NIM, Xiaomi, Ollama Cloud, MiniMax)</p>

    <div class="score-formula">
        <div class="title">Como se calcula el Score (v2.6.0)</div>
        <div class="row"><span class="pct">50%</span>Calidad (formato + sustancia + LLM-as-Judge Phi-4 14B local, MIT)</div>
        <div class="row"><span class="pct">20%</span>Costo (curva log inversa: $0.001/call=8.0, $0.01=5.0, $0.10=2.0)</div>
        <div class="row"><span class="pct">15%</span>Tool Calling (precision de function calling para agentes)</div>
        <div class="row"><span class="pct">7.5%</span>Velocidad (tokens por segundo)</div>
        <div class="row"><span class="pct">7.5%</span>Latencia (tiempo hasta primera respuesta)</div>
    </div>

    <p class="meta" style="margin-top: 14px; font-size: 8pt; max-width: 700px;">
        📍 <strong>Disclaimer</strong>: este benchmark NO sustituye a HumanEval, MMLU, GSM8K, SWE-bench, NIAH inglés, MT-Bench, LMSYS Arena.
        Es <strong>complemento</strong> para emprendedores hispanohablantes que deciden producción real (N8N, OpenClaw, Hermes, blogs LATAM, agentes).
    </p>
</div>

<!-- ============================================================ -->
<!-- HALLAZGOS CLAVE DEL MES (P2) -->
<!-- ============================================================ -->
<div class="page">
    <h2>Hallazgos clave de {MONTH} {YEAR}</h2>
    <p style="font-size: 9pt; color: #b0b0b0; margin-bottom: 12px;">
        Insights cuantitativos del benchmark v2.6.0. Cada hallazgo con fecha de descubrimiento o validación.
    </p>

    <div class="two-col">
        <div>
            <h3>1. Provider matters cuantificado <span style="font-size:8pt;color:#b0b0b0;">(28-30 abril 2026)</span></h3>
            <p style="font-size:9pt;">Mismo modelo en provider directo vs OpenRouter: <strong>+0.16 a +0.25 puntos</strong>.
            Confirmado en 4 proveedores (Xiaomi direct, Groq direct, NIM gratis, MiniMax direct).
            <strong>Para producción: provider directo cuando esté disponible</strong>.</p>

            <h3>2. Thinking forzado EMPEORA agéntica multi-turn <span style="font-size:8pt;color:#b0b0b0;">(29-30 abril 2026)</span></h3>
            <p style="font-size:9pt;">8/9 modelos hybrid bajan vs sin thinking: Opus 4.7 -0.67, Sonnet 4.6 -0.50,
            Hermes 4 70B -0.54. Solo Kimi K2.5 sube (+0.73). <strong>Para N8N/OpenClaw: NO actives thinking default</strong>.</p>

            <h3>3. Why Opus 4.7 NO está en top 10 <span style="font-size:8pt;color:#b0b0b0;">(29 abril 2026)</span></h3>
            <p style="font-size:9pt;">Opus 4.7 quality 8.08 (top 6 entre todos), pero <strong>40-100x más caro y 5-10x más lento</strong>.
            Score compuesto pondera costo+speed → fuera del top 10. Para producción a volumen LATAM con presupuesto: alternativas.</p>

            <h3>4. Modelo gigante NO siempre gana <span style="font-size:8pt;color:#b0b0b0;">(28 abril 2026)</span></h3>
            <p style="font-size:9pt;">Mistral Large 3 (675B params) saca 6.89. Nemotron Nano 9B v2 saca 6.91.
            <strong>Modelo 75x más pequeño rinde más</strong>.</p>

            <h3>5. "1M context declarado" ≠ retrieval efectivo <span style="font-size:8pt;color:#b0b0b0;">(1 mayo 2026)</span></h3>
            <p style="font-size:9pt;">Solo <strong>GPT-4.1 procesa 1M tokens efectivamente</strong> via OpenAI/OpenRouter.
            Llama 4 Scout (10M declarado), DeepSeek V4 Flash (1M), Gemini 3.1 Pro (1M) — todos cap por providers a 128K-256K real.</p>
        </div>
        <div>
            <h3>6. DeepSeek V4 Pro NIM NO funciona en producción <span style="font-size:8pt;color:#b0b0b0;">(28 abr + 3 mayo 2026)</span></h3>
            <p style="font-size:9pt;">Cascada 504 reproducible <strong>2 veces</strong>. NIM gateway no maneja modelo gigante con prompts largos.
            Para V4 Pro: <strong>OpenRouter pagado o Ollama Cloud sub</strong> (97% éxito).</p>

            <h3>7. MiMo Xiaomi sub family — mejor C/B en español <span style="font-size:8pt;color:#b0b0b0;">(2-3 mayo 2026)</span></h3>
            <p style="font-size:9pt;"><strong>4 modelos MiMo en top 10</strong> (V2-Omni, V2.5, V2.5-Pro, V2-Flash).
            Sub <strong>$14/mes</strong> da acceso a 4 modelos competentes con español neutro fuerte.
            Mejor opción para emprendedores LATAM con presupuesto fijo predecible.</p>

            <h3>8. Devstral Small lidera NIAH-ES <span style="font-size:8pt;color:#b0b0b0;">(30 abr + 3 mayo 2026)</span></h3>
            <p style="font-size:9pt;">Specialist coding model gana retrieval en español: <strong>7.25 vs Opus 4.7 4.98</strong>.
            <strong>+2.27 puntos a 1/450 del costo</strong>. Tasks de extracción info con contexto &lt;128K: Devstral.</p>

            <h3>9. Limitación honesta: NO medimos debugging real <span style="font-size:8pt;color:#b0b0b0;">(30 abril 2026)</span></h3>
            <p style="font-size:9pt;">Caso reportado: MiniMax M2.7 NO pudo resolver bug en VPS Hetzner. Opus 4.7 sí en minutos.
            Para debugging agentic real, mira <strong>SWE-bench Verified</strong> (Opus 4.7 = 87.6% top 1 globalmente).</p>

            <h3>10. GPT-5.5 cobertura completa <span style="font-size:8pt;color:#b0b0b0;">(3 mayo 2026)</span></h3>
            <p style="font-size:9pt;">GPT-5.5 single-turn 6.32 (regresión vs GPT-5.4 7.23) + agent_long_horizon + NIAH-ES completos.
            Confirma patrón: thinking puede empeorar en aplicación real.</p>
        </div>
    </div>

    <p class="guino">Ver hallazgos completos con datos cuantitativos: {URL_REPO}/blob/main/INSIGHTS.md</p>
</div>

<!-- ============================================================ -->
<!-- TOP 10 RANKING GLOBAL (P3) -->
<!-- ============================================================ -->
<div class="page">
    <h2>Top 10 Score Compuesto</h2>
    <table>
        <thead>
            <tr><th>#</th><th>Modelo</th><th>Score</th><th>Calidad</th><th>Costo$</th><th>Tool</th><th>Speed</th><th>Lat</th><th>Provider</th></tr>
        </thead>
        <tbody>
"""

    for i, m in enumerate(top10, 1):
        html += f"""            <tr>
                <td>{i}</td>
                <td><strong>{m["name"]}</strong></td>
                <td><strong>{m.get("score_global"):.2f}</strong></td>
                <td>{m.get("quality_avg") or "—"}</td>
                <td>{m.get("cost_score_avg") or "—"}</td>
                <td>{m.get("tool_calling_score_avg") or "—"}</td>
                <td>{m.get("speed_score_avg") or "—"}</td>
                <td>{m.get("latency_score_avg") or "—"}</td>
                <td>{m.get("provider", "openrouter")}</td>
            </tr>\n"""

    html += """        </tbody>
    </table>

    <h3>Top 5 Quality (sin pesar costo)</h3>
    <table>
        <thead><tr><th>#</th><th>Modelo</th><th>Quality</th><th>Final compuesto</th></tr></thead>
        <tbody>
"""
    for i, m in enumerate(top_quality[:5], 1):
        html += f"""            <tr>
                <td>{i}</td><td>{m["name"]}</td>
                <td><strong>{m.get("quality_avg")}</strong></td>
                <td>{m.get("score_global"):.2f}</td>
            </tr>\n"""

    html += f"""        </tbody>
    </table>

    <div class="tip">
        <strong>Lectura</strong>: el ranking compuesto pondera quality+costo+speed+latencia.
        Si solo te importa <strong>quality</strong> (e.g. trabajo crítico sin presupuesto), mira la segunda tabla:
        Opus/Gemini/Hermes 4 suben fuerte. Si el costo importa: top compuesto.
    </div>

    <p class="guino">Ranking completo de {len(ranked)} modelos en {URL_CALC} · datos crudos en {URL_REPO}</p>
</div>

<!-- ============================================================ -->
<!-- RECOMENDACIONES POR CASO DE USO (P4) -->
<!-- ============================================================ -->
<div class="page">
    <h2>Que Modelo Usar — Por Caso de Uso</h2>
    <p style="font-size: 9pt; color: #b0b0b0; margin-bottom: 10px;">
        Recomendaciones basadas en los datos del benchmark + cross-reference con SWE-bench / NIAH inglés.
        <strong>Stack agente recomendado</strong>: 1 LLM cabecera (orquestador) + N skills especializados.
    </p>

    <div class="two-col">
        <div>
            <h3>Agente cabecera (N8N / OpenClaw / Hermes)</h3>
            <table>
                <thead><tr><th>Recomendación</th><th>Score agéntico</th><th>Costo</th></tr></thead>
                <tbody>
                    <tr><td>🥇 GPT-OSS 120B (Ollama Cloud)</td><td><strong>8.15</strong> (#1 ALH)</td><td>$30/mes sub</td></tr>
                    <tr><td>🥈 Llama 3.3 70B Groq</td><td>7.60</td><td>$0.59/$0.79 per M</td></tr>
                    <tr><td>🥉 MiMo V2.5 (Xiaomi sub)</td><td>7.65</td><td>$14/mes sub</td></tr>
                </tbody>
            </table>

            <h3>Skill: Coding (workflows N8N, plugins, scripts)</h3>
            <table>
                <thead><tr><th>Modelo</th><th>Notas</th></tr></thead>
                <tbody>
                    <tr><td><strong>Devstral Small</strong></td><td>Apache 2.0 · #1 NIAH-ES · Specialist · $0.10/$0.30</td></tr>
                    <tr><td>Devstral 2 (Dic 2025)</td><td>Apache 2.0 · 256K context</td></tr>
                </tbody>
            </table>

            <h3>Skill: Content (blog, social, newsletter)</h3>
            <table>
                <thead><tr><th>Modelo</th><th>Notas</th></tr></thead>
                <tbody>
                    <tr><td><strong>MiMo V2.5 (Xiaomi sub)</strong></td><td>Sub $14/mes · español neutro fuerte</td></tr>
                    <tr><td>Gemini 3.1 Flash Lite</td><td>$0.25/$1.50 · Google directo</td></tr>
                </tbody>
            </table>
        </div>
        <div>
            <h3>Skill: Customer Support multi-turn</h3>
            <table>
                <thead><tr><th>Modelo</th><th>Notas</th></tr></thead>
                <tbody>
                    <tr><td><strong>GPT-OSS 120B Cloud</strong></td><td>#1 agent_long_horizon (8.15)</td></tr>
                    <tr><td>Llama 3.3 70B Groq</td><td>Latencia ultra baja (270 tok/s)</td></tr>
                </tbody>
            </table>

            <h3>Skill: Research con tools (Perplexity-style)</h3>
            <table>
                <thead><tr><th>Modelo</th><th>Notas</th></tr></thead>
                <tbody>
                    <tr><td><strong>DeepSeek V4 Flash (NIM)</strong></td><td>GRATIS · 40 RPM · 1M context</td></tr>
                    <tr><td>Mistral Small 4</td><td>$0.15/$0.60 · top quality</td></tr>
                </tbody>
            </table>

            <h3>Skill: Long-context retrieval (>32K tokens)</h3>
            <table>
                <thead><tr><th>Modelo</th><th>Notas</th></tr></thead>
                <tbody>
                    <tr><td><strong>GPT-4.1</strong></td><td>Único modelo confirmado a 1M efectivo</td></tr>
                    <tr><td>Gemini 3.1 Pro</td><td>Más estable a 256K (5.37 avg)</td></tr>
                </tbody>
            </table>

            <h3>Para debugging agentic real</h3>
            <div class="warning">
                <strong>NO usar nuestro ranking</strong> — usa SWE-bench Verified.
                Top: Opus 4.7 (87.6%), Sonnet 4.6 (77.2%), GPT-5.x. Caso real reportado: solo Opus resolvió bug Docker complejo.
            </div>
        </div>
    </div>

    <p class="guino">Recomendaciones detalladas por plataforma + tarea + presupuesto: {URL_REPO}/blob/main/RECOMENDACIONES.md</p>
</div>

<!-- ============================================================ -->
<!-- RANKINGS POR CATEGORIA (P5) -->
<!-- ============================================================ -->
<div class="page">
    <h2>Rankings por Categoria — Top 5 por área</h2>

    <div class="three-col">
        <div>
            <h3>Razonamiento (single-turn)</h3>
            <table><thead><tr><th>#</th><th>Modelo</th><th>Score</th></tr></thead><tbody>
"""
    # Razonamiento por pilar
    razonamiento = sorted(
        [m for m in ranked if (m.get("score_by_pillar") or {}).get("Razonamiento")],
        key=lambda x: -x["score_by_pillar"]["Razonamiento"]
    )[:5]
    for i, m in enumerate(razonamiento, 1):
        html += f'<tr><td>{i}</td><td>{m["name"][:20]}</td><td><strong>{m["score_by_pillar"]["Razonamiento"]:.2f}</strong></td></tr>\n'

    html += """            </tbody></table>

            <h3>Coding</h3>
            <table><thead><tr><th>#</th><th>Modelo</th><th>Score</th></tr></thead><tbody>
"""
    coding = sorted(
        [m for m in ranked if (m.get("score_by_pillar") or {}).get("Coding")],
        key=lambda x: -x["score_by_pillar"]["Coding"]
    )[:5]
    for i, m in enumerate(coding, 1):
        html += f'<tr><td>{i}</td><td>{m["name"][:20]}</td><td><strong>{m["score_by_pillar"]["Coding"]:.2f}</strong></td></tr>\n'

    html += """            </tbody></table>
        </div>
        <div>
            <h3>Contenido / Marketing</h3>
            <table><thead><tr><th>#</th><th>Modelo</th><th>Score</th></tr></thead><tbody>
"""
    contenido = sorted(
        [m for m in ranked if (m.get("score_by_pillar") or {}).get("Contenido")],
        key=lambda x: -x["score_by_pillar"]["Contenido"]
    )[:5]
    for i, m in enumerate(contenido, 1):
        html += f'<tr><td>{i}</td><td>{m["name"][:20]}</td><td><strong>{m["score_by_pillar"]["Contenido"]:.2f}</strong></td></tr>\n'

    html += """            </tbody></table>

            <h3>Agentes / Operaciones</h3>
            <table><thead><tr><th>#</th><th>Modelo</th><th>Score</th></tr></thead><tbody>
"""
    agentes = sorted(
        [m for m in ranked if (m.get("score_by_pillar") or {}).get("Agentes")],
        key=lambda x: -x["score_by_pillar"]["Agentes"]
    )[:5]
    for i, m in enumerate(agentes, 1):
        html += f'<tr><td>{i}</td><td>{m["name"][:20]}</td><td><strong>{m["score_by_pillar"]["Agentes"]:.2f}</strong></td></tr>\n'

    html += """            </tbody></table>
        </div>
        <div>
            <h3>Multi-step (agent_long_horizon)</h3>
            <table><thead><tr><th>#</th><th>Modelo</th><th>Score</th></tr></thead><tbody>
"""
    for i, m in enumerate(alh_models[:5], 1):
        html += f'<tr><td>{i}</td><td>{m["name"][:20]}</td><td><strong>{m["alh"]:.2f}</strong></td></tr>\n'

    html += """            </tbody></table>

            <h3>Aguja-en-Pajar (NIAH-ES)</h3>
            <table><thead><tr><th>#</th><th>Modelo</th><th>Score</th></tr></thead><tbody>
"""
    for i, m in enumerate(niah_models[:5], 1):
        html += f'<tr><td>{i}</td><td>{m["name"][:20]}</td><td><strong>{m["niah_avg"]:.2f}</strong></td></tr>\n'

    html += f"""            </tbody></table>
        </div>
    </div>

    <p class="guino">Ranking completo + drill-down por subcategorías en {URL_CALC}</p>
</div>

<!-- ============================================================ -->
<!-- PRECIOS Y SUSCRIPCIONES (P6) -->
<!-- ============================================================ -->
<div class="page">
    <h2>Precios y Suscripciones</h2>

    <div class="two-col">
        <div>
            <h3>Pay-as-you-go (por millón de tokens)</h3>
            <table>
                <thead><tr><th>Modelo</th><th>Input $/M</th><th>Output $/M</th></tr></thead>
                <tbody>
                    <tr><td>Llama 3.3 70B Groq</td><td>$0.59</td><td>$0.79</td></tr>
                    <tr><td>Llama 3.1 8B Groq</td><td>$0.05</td><td>$0.08</td></tr>
                    <tr><td>Devstral Small</td><td>$0.10</td><td>$0.30</td></tr>
                    <tr><td>Mistral Small 4</td><td>$0.15</td><td>$0.60</td></tr>
                    <tr><td>Gemini 3.1 Flash Lite</td><td>$0.25</td><td>$1.50</td></tr>
                    <tr><td>Grok 4.1 Fast</td><td>$0.20</td><td>$0.50</td></tr>
                    <tr><td>GPT-4.1</td><td>$2.50</td><td>$10.00</td></tr>
                    <tr><td>Claude Sonnet 4.6</td><td>$3.00</td><td>$15.00</td></tr>
                    <tr><td>Claude Opus 4.7</td><td>$15.00</td><td>$75.00</td></tr>
                </tbody>
            </table>

            <h3>NIM Gratis (NVIDIA)</h3>
            <p style="font-size:9pt;">Acceso a <strong>20+ modelos gratis</strong> con rate limit 40 RPM.
            Suficiente para producción de bajo volumen y benchmarks. Modelos: DeepSeek V4 Flash, Gemma 4 31B, Llama Nemotron family, Qwen 3-Next, Mistral Large 3, etc.</p>
        </div>
        <div>
            <h3>Suscripciones Mensuales Fijas</h3>
            <table>
                <thead><tr><th>Plan</th><th>Precio</th><th>Modelos</th></tr></thead>
                <tbody>
                    <tr><td><strong>Xiaomi MiMo Standard</strong></td><td><strong>$14/mes</strong></td><td>4 modelos: V2.5, V2.5-Pro, V2-Pro, V2-Omni · 200M credits/mes</td></tr>
                    <tr><td>MiniMax Agent Pro</td><td>$19/mes</td><td>M2.7 Highspeed · generosos límites</td></tr>
                    <tr><td>Anthropic Pro</td><td>$20/mes</td><td>Claude (web only, NO API)</td></tr>
                    <tr><td>Ollama Cloud Pro</td><td>$30/mes</td><td>5 modelos: GPT-OSS 120B, DeepSeek V4 Pro/Flash, Qwen 3.5 397B/default</td></tr>
                </tbody>
            </table>

            <h3>Estrategia de costo recomendada</h3>
            <div class="tip">
                <strong>Si tienes ~$0/mes y bajo volumen</strong>: NIM gratis (40 RPM) + modelos open en Groq direct cheap.<br>
                <strong>Si tienes ~$14/mes</strong>: Sub Xiaomi MiMo (4 modelos en español neutro fuerte).<br>
                <strong>Si tienes ~$30-50/mes</strong>: Sub Ollama Cloud + Sub Xiaomi (cobertura completa).<br>
                <strong>Si tienes &gt;$100/mes</strong>: Pay-as-you-go en OpenRouter con fallback automático.
            </div>
        </div>
    </div>

    <p class="guino">Detalle de suscripciones + cuándo conviene cada una: {URL_REPO}/blob/main/SUSCRIPCIONES.md</p>
</div>

<!-- ============================================================ -->
<!-- ESTRATEGIA LOCAL (P7) - GENERALIZADA POR VRAM -->
<!-- ============================================================ -->
<div class="page">
    <h2>Estrategia Local — segun VRAM/RAM disponible</h2>
    <p style="font-size:9pt; color:#b0b0b0; margin-bottom:10px;">
        Modelos open-source para correr en hardware propio. Recomendaciones por capacidad disponible
        (Mac Apple Silicon usa unified memory; PCs con GPU dedicada usan VRAM; servidores con AI accelerator usan unified RAM como DGX Spark 128GB).
    </p>

    <div class="two-col">
        <div>
            <h3>≤8 GB (laptops básicas, RTX 3060)</h3>
            <table>
                <thead><tr><th>Modelo</th><th>Tamaño Q4</th></tr></thead>
                <tbody>
                    <tr><td>Llama 3.1 8B</td><td>~4.5 GB</td></tr>
                    <tr><td>Phi-4 14B (juez Phi-4)</td><td>~8 GB</td></tr>
                    <tr><td>Mistral 7B / DeepSeek-Coder 6.7B</td><td>~4-5 GB</td></tr>
                </tbody>
            </table>

            <h3>16 GB (M2/M3 base, RTX 4070)</h3>
            <table>
                <thead><tr><th>Modelo</th><th>Tamaño Q4</th></tr></thead>
                <tbody>
                    <tr><td>Gemma 4 26B MoE</td><td>~14 GB</td></tr>
                    <tr><td>Qwen 3.5 25B</td><td>~13 GB</td></tr>
                    <tr><td>Devstral Small (Mistral 24B)</td><td>~13 GB</td></tr>
                </tbody>
            </table>

            <h3>24-32 GB (M2 Pro/Max, RTX 4090)</h3>
            <table>
                <thead><tr><th>Modelo</th><th>Tamaño Q4</th></tr></thead>
                <tbody>
                    <tr><td>Gemma 4 31B</td><td>~18 GB</td></tr>
                    <tr><td>Nemotron 3 Nano 30B</td><td>~17 GB</td></tr>
                    <tr><td>Qwen 3.5 32B</td><td>~17 GB</td></tr>
                </tbody>
            </table>
        </div>
        <div>
            <h3>48-64 GB (M3 Max, M3 Ultra)</h3>
            <table>
                <thead><tr><th>Modelo</th><th>Tamaño Q4</th></tr></thead>
                <tbody>
                    <tr><td>Llama 3.3 70B</td><td>~40 GB</td></tr>
                    <tr><td>Qwen 3.5 72B</td><td>~40 GB</td></tr>
                    <tr><td>MiniMax M2.5</td><td>~50 GB</td></tr>
                </tbody>
            </table>

            <h3>128 GB (Mac Studio M3 Ultra, NVIDIA DGX Spark)</h3>
            <table>
                <thead><tr><th>Modelo</th><th>Tamaño Q4</th></tr></thead>
                <tbody>
                    <tr><td>Nemotron 3 Super 120B</td><td>~80 GB ✓</td></tr>
                    <tr><td>Llama 4 Maverick</td><td>~110 GB</td></tr>
                    <tr><td>DeepSeek V3.2</td><td>~120 GB</td></tr>
                </tbody>
            </table>

            <h3>256 GB+ (servidores dedicados)</h3>
            <p style="font-size:9pt;">Modelos gigantes 600B+: Mistral Large 3 675B, Qwen 3.5 397B (necesitan >256GB Q4). Generalmente no rentables vs API a este tamaño.</p>

            <h3>Cuándo usar local vs nube</h3>
            <div class="tip">
                <strong>Local SI</strong>: privacidad de datos · sin latencia red · costo $0 por call · soberanía.<br>
                <strong>Nube SI</strong>: mejor calidad (modelos &gt; tu hardware) · sin setup ni mantenimiento · escalable.
            </div>
        </div>
    </div>

    <p class="guino">Modelos validados localmente + scripts setup: {URL_REPO}/blob/main/MODELOS.md</p>
</div>

<!-- ============================================================ -->
<!-- MAPA DE PROVEEDORES (P8) -->
<!-- ============================================================ -->
<div class="page">
    <h2>Mapa de Proveedores</h2>
    <p style="font-size:9pt; color:#b0b0b0; margin-bottom:10px;">
        8 providers cubiertos en mayo 2026. Ordenados por costo (de más barato a más caro).
    </p>

    <table>
        <thead>
            <tr><th>Provider</th><th>Tipo</th><th>Modelos clave</th><th>Costo</th><th>Rate limit</th><th>Notas</th></tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>NVIDIA NIM</strong></td>
                <td>Free tier</td>
                <td>20+ modelos: DeepSeek V4 Flash, Gemma 4 31B, Llama-Nemotron, Mistral Large 3, Qwen 3-Next</td>
                <td class="os-yes">$0</td>
                <td>40 RPM</td>
                <td>NIM Pro saturado para gigantes (504 cascada)</td>
            </tr>
            <tr>
                <td><strong>Local (Ollama)</strong></td>
                <td>Self-hosted</td>
                <td>Modelos open-source bajo tu HW</td>
                <td class="os-yes">$0 (HW propio)</td>
                <td>Tu HW</td>
                <td>Ver "Estrategia Local" según VRAM</td>
            </tr>
            <tr>
                <td><strong>Xiaomi MiMo</strong></td>
                <td>Sub mensual</td>
                <td>4 modelos MiMo (V2.5, V2.5-Pro, V2-Pro, V2-Omni)</td>
                <td class="os-yes">$14/mes</td>
                <td>200M credits/mes</td>
                <td>Mejor C/B en español neutro</td>
            </tr>
            <tr>
                <td><strong>MiniMax</strong></td>
                <td>Sub + API</td>
                <td>M2.7 Highspeed</td>
                <td class="os-yes">$19/mes sub o $0.30/$1.20 per M</td>
                <td>Generosos</td>
                <td>Ultra baja latencia (Highspeed)</td>
            </tr>
            <tr>
                <td><strong>Ollama Cloud</strong></td>
                <td>Sub mensual</td>
                <td>5 modelos: GPT-OSS 120B, DeepSeek V4 Pro/Flash, Qwen 3.5 397B</td>
                <td class="os-yes">$30/mes</td>
                <td>Variable</td>
                <td>97% éxito en V4 Pro (vs NIM 0%)</td>
            </tr>
            <tr>
                <td><strong>Groq direct</strong></td>
                <td>Pay-as-you-go</td>
                <td>Llama family, GPT-OSS 20B</td>
                <td class="os-yes">$0.05-1.36/M</td>
                <td>30 RPM (alto riesgo)</td>
                <td>Ultra rápido (270+ tok/s)</td>
            </tr>
            <tr>
                <td><strong>OpenRouter</strong></td>
                <td>Aggregator</td>
                <td>290+ modelos via 1 API key</td>
                <td>Variable (margen +5-15% vs direct)</td>
                <td>Bajo</td>
                <td>Cap 256K en algunos modelos 1M</td>
            </tr>
            <tr>
                <td><strong>OpenAI directo</strong></td>
                <td>Pay-as-you-go</td>
                <td>GPT-4.1, GPT-5.x family</td>
                <td>$2.50-75/M</td>
                <td>Bajo</td>
                <td>Único confirmado a 1M effective</td>
            </tr>
            <tr>
                <td><strong>Anthropic API</strong></td>
                <td>Pay-as-you-go</td>
                <td>Claude Opus/Sonnet/Haiku 4.x</td>
                <td>$0.25-75/M</td>
                <td>Bajo</td>
                <td>SOTA SWE-bench. Sub Pro $20 NO da API</td>
            </tr>
            <tr>
                <td><strong>Google AI Studio</strong></td>
                <td>Pay-as-you-go</td>
                <td>Gemini 2.5/3.x Flash/Pro</td>
                <td>$0.10-12/M</td>
                <td>Bajo</td>
                <td>Mejor a 256K context (NIAH 5.37)</td>
            </tr>
        </tbody>
    </table>

    <div class="tip" style="margin-top: 12px;">
        <strong>Estrategia recomendada</strong>: 1 sub barata (MiMo Xiaomi $14) para producción base + NIM gratis para modelos especializados + 1 cuenta OpenRouter como fallback con $20-50 de credit para emergencias.
    </div>

    <p class="guino">Comparativa detallada de proveedores: {URL_REPO}/blob/main/PROVEEDORES.md</p>
</div>

<!-- ============================================================ -->
<!-- METODOLOGIA + QUE MEDIMOS (P9) - referencia al final -->
<!-- ============================================================ -->
<div class="page">
    <h2>Metodologia — Que Medimos (y que NO)</h2>

    <div class="two-col">
        <div>
            <h3>148 tests por modelo en 25 suites</h3>
            <table>
                <thead><tr><th>Tipo</th><th>Suites</th><th>Tests</th></tr></thead>
                <tbody>
                    <tr><td><strong>Single-turn (4 pilares)</strong></td><td>23</td><td>91</td></tr>
                    <tr><td><strong>Multi-step (agent_long_horizon)</strong> 🆕</td><td>1</td><td>12</td></tr>
                    <tr><td><strong>Aguja en pajar (NIAH-ES)</strong> 🆕</td><td>2</td><td>45 (lite) o 60 (full)</td></tr>
                    <tr><td><strong>Aguja en pajar 1M (NIAH-ES 1M)</strong> 🆕</td><td>1</td><td>15</td></tr>
                </tbody>
            </table>

            <h3>4 pilares aplicados (single-turn)</h3>
            <table>
                <thead><tr><th>Pilar</th><th>Suites</th></tr></thead>
                <tbody>
                    <tr><td><strong>Razonamiento</strong></td><td>reasoning, deep_reasoning, hallucination, strategy</td></tr>
                    <tr><td><strong>Coding</strong></td><td>code_generation, structured_output, string_precision, ocr_extraction</td></tr>
                    <tr><td><strong>Contenido</strong></td><td>content_generation, summarization, presentation, startup_content, creativity, news_seo_writing, sales_outreach, translation</td></tr>
                    <tr><td><strong>Agentes</strong></td><td>tool_calling, task_management, customer_support, orchestration, multi_turn, policy_adherence, agent_capabilities</td></tr>
                </tbody>
            </table>
        </div>
        <div>
            <h3>Suites nuevas (mayo 2026)</h3>
            <p style="font-size:9pt;"><strong>agent_long_horizon</strong> (multi-step): 12 tests con conversaciones de 8+ turnos. Mide context retention, skill orchestration, interruption recovery, goal persistence. Plantilla rígida (script de usuario pre-escrito) para reproducibilidad. Tools simulados via stubs.</p>
            <p style="font-size:9pt;"><strong>NIAH-ES</strong> (Needle-in-a-Haystack en español): primer NIAH público en español neutro LATAM. 5 needles × 4 contextos (4K-256K) × 3 posiciones. Mide retrieval de info específica en documentos largos. Datos LATAM realistas (códigos, fechas, identificadores).</p>

            <h3>Que SI medimos</h3>
            <ul style="font-size:9pt; padding-left: 20px;">
                <li>✅ <strong>Calidad</strong> (50%): formato + sustancia + LLM-as-Judge Phi-4 14B local</li>
                <li>✅ <strong>Costo real</strong> (20%): por provider exacto, curva log inversa</li>
                <li>✅ <strong>Tool calling</strong> (15%): function calling para agentes</li>
                <li>✅ <strong>Velocidad</strong> (7.5%): tokens por segundo</li>
                <li>✅ <strong>Latencia</strong> (7.5%): primer token (medida desde Chile)</li>
                <li>✅ Multi-turn long-horizon (8+ turnos)</li>
                <li>✅ Long-context retrieval hasta 256K (1M parcial)</li>
            </ul>

            <h3>Que NO medimos</h3>
            <ul style="font-size:9pt; padding-left: 20px;">
                <li>❌ Debugging agentic real (Docker/K8s) — usa <strong>SWE-bench Verified</strong></li>
                <li>❌ Capacidades fundamentales generales — usa <strong>HumanEval/MMLU/GSM8K</strong></li>
                <li>❌ Multimodal (imágenes/audio) — limitado</li>
                <li>❌ Consistencia entre runs (single shot N=1)</li>
                <li>❌ Razonamiento puro complejo — usa <strong>GPQA Diamond/AIME</strong></li>
            </ul>

            <div class="warning">
                <strong>📍 Recordatorio</strong>: este benchmark es <strong>complemento</strong>, no sustituto.
                Para producción aplicada en español neutro LATAM agrega data que los académicos no cubren.
                Para investigación académica, prioriza los oficiales.
            </div>
        </div>
    </div>

    <p class="guino">Metodología completa + reproducibilidad: {URL_REPO}/blob/main/CLAUDE.md</p>
</div>

<!-- ============================================================ -->
<!-- CTA FINAL CON QR (P10) -->
<!-- ============================================================ -->
<div class="page" style="display: flex; flex-direction: column; justify-content: center; align-items: center;">
    <h1 style="font-family: 'JetBrains Mono', monospace; color: #39ff14; font-size: 28pt; text-align: center; margin-bottom: 8px;">¿Te sirvió este cheatsheet?</h1>
    <p style="font-size: 14pt; color: #00d4ff; text-align: center; margin-bottom: 24px;">Llévatelo a producción, aporta datos o únete a la comunidad</p>

    <div class="qr-container">
        <div class="qr-box">
            <img src="data:image/png;base64,{qr_calc}" alt="QR Calculadora">
            <div class="qr-label">🎛 Calculadora interactiva</div>
            <div class="qr-url">{URL_CALC}</div>
            <p style="font-size: 8pt; color: #b0b0b0; margin-top: 8px; line-height: 1.4;">
                Filtra por presupuesto, calidad, velocidad. Top {len(ranked)} modelos actualizados.
            </p>
        </div>
        <div class="qr-box">
            <img src="data:image/png;base64,{qr_skool}" alt="QR Comunidad">
            <div class="qr-label">👥 Comunidad Skool</div>
            <div class="qr-url">{URL_SKOOL}</div>
            <p style="font-size: 8pt; color: #b0b0b0; margin-top: 8px; line-height: 1.4;">
                <strong>Cágala, Aprende, Repite</strong> — workshops, casos reales, stack de emprendedores LATAM.
            </p>
        </div>
    </div>

    <div style="margin-top: 24px; text-align: center; max-width: 700px;">
        <h3 style="color: #b59cff; margin-bottom: 10px;">Cómo aportar al benchmark</h3>
        <p style="font-size: 9.5pt; color: #b0b0b0; line-height: 1.6;">
            <strong>1. Reporta tu caso real</strong> · ¿Modelo X resolvió/falló en tu producción? Compártelo en la comunidad o GitHub Issues.<br>
            <strong>2. Sugiere tests nuevos</strong> · El benchmark es open-source MIT. Pull requests bienvenidos.<br>
            <strong>3. Replica los benchmarks</strong> · Repo público, datos crudos versionados, scripts reproducibles.<br>
            <strong>4. Comparte hallazgos</strong> · Si encontrás un patrón en tu uso, documentalo en INSIGHTS.md.
        </p>
    </div>

    <div style="margin-top: 30px; text-align: center;">
        <p style="font-family: 'JetBrains Mono', monospace; color: #39ff14; font-size: 12pt;">
            github.com/ctala/ai-benchmarks-alternativos
        </p>
        <p style="font-family: 'JetBrains Mono', monospace; color: #00d4ff; font-size: 10pt; margin-top: 4px;">
            cristiantala.com · {MONTH} {YEAR} · v2.6.0 · MIT
        </p>
    </div>

    <p style="text-align:center; font-size: 8pt; color: #b59cff; margin-top: 18px; max-width: 600px;">
        Este benchmark se mantiene gracias a tiempo personal de Cristian Tala Sánchez (Chile) + suscripciones $45/mes.
        Si te ayudó, comparte el repo. Si querés contribuir, las contribuciones de comunidad se documentan en CHANGELOG.
    </p>
</div>

</body>
</html>"""

    return html


# ============================================================
# MAIN
# ============================================================

def main():
    models = load_models()
    runs = load_runs()
    html = render(models, runs)

    out_dir = ROOT / "cheatsheet"
    out_dir.mkdir(exist_ok=True)
    html_file = out_dir / f"cheatsheet_{YEAR}_{now.strftime('%m')}_v2.html"
    pdf_file = out_dir / f"AI_Model_Benchmark_CheatSheet_{MONTH}_{YEAR}.pdf"

    html_file.write_text(html)
    HTML(string=html).write_pdf(str(pdf_file))

    print(f"PDF generado: {pdf_file}")
    print(f"HTML guardado: {html_file}")
    print(f"  Páginas estimadas: 10 (cover + 9 secciones)")


if __name__ == "__main__":
    main()
