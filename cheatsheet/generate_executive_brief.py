#!/usr/bin/env python3
"""
Genera el Executive Brief PDF mensual del benchmark.
4-6 páginas A4 landscape, diseño neo-brutalism synthwave terminal,
destinado a ser compartido y usado como referencia rápida.
"""

import base64
import io
import json
from datetime import datetime
from pathlib import Path

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
MONTH_EN = now.strftime("%B")

URL_CALC = "https://benchmarks.cristiantala.com/"
URL_REPO = "https://github.com/ctala/ai-benchmarks-alternativos"


def qr_b64(url: str, size: int = 180) -> str:
    qr = qrcode.QRCode(border=1, box_size=8)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#0a0a1a", back_color="#39ff14")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode()


def load_models() -> dict:
    p = ROOT / "docs" / "data" / "models.json"
    return json.loads(p.read_text())


def cost_per_call(m: dict) -> float:
    """Costo real por call del provider del modelo (desde cost_per_1k_calls_usd)."""
    return (m.get("cost_per_1k_calls_usd") or 0) / 1000


def openrouter_cost_per_call(m: dict, openrouter_lookup: dict) -> float | None:
    """Busca el costo equivalente en OpenRouter para normalizar comparaciones."""
    key = m.get("key", "")
    name = m.get("name", "")
    # Intenta match por key o por nombre base sin parentesis de provider
    name_base = name.split(" (")[0].strip()
    candidates = []
    for om in openrouter_lookup.values():
        om_key = om.get("key", "")
        om_name = om.get("name", "")
        om_name_base = om_name.split(" (")[0].strip()
        if key and key == om_key:
            candidates.append(om)
        elif name_base and name_base == om_name_base:
            candidates.append(om)
    if candidates:
        # Elige el de mayor runs para mayor confiabilidad
        best = max(candidates, key=lambda x: x.get("runs", 0))
        return cost_per_call(best)
    return None


def normalised_cost_per_call(m: dict, openrouter_lookup: dict | None = None) -> float | None:
    """Costo normalizado estricto: solo OpenRouter. Si no existe, devuelve None."""
    if openrouter_lookup:
        return openrouter_cost_per_call(m, openrouter_lookup)
    return None


def fmt_cost(m: dict, openrouter_lookup: dict | None = None) -> str:
    """Devuelve string formateado para costo por call usando SOLO OpenRouter.

    Si el modelo no tiene equivalente en OpenRouter, se marca como N/A para
    evitar comparaciones enganosas entre providers distintos.
    """
    or_cost = openrouter_cost_per_call(m, openrouter_lookup) if openrouter_lookup else None
    if or_cost is None:
        return "<span class='cost-note'>N/A en OpenRouter</span>"
    if or_cost == 0:
        return "gratis"
    if or_cost < 0.001:
        return f"${or_cost:.6f}/call"
    if or_cost < 0.01:
        return f"${or_cost:.4f}/call"
    return f"${or_cost:.3f}/call"


def bar_svg(value: float, max_val: float, color: str = "#39ff14", width: int = 260) -> str:
    pct = min(100, max(0, value / max_val * 100)) if max_val else 0
    return f'''<svg width="{width}" height="14" role="img" aria-label="bar">
        <rect x="0" y="0" width="{width}" height="14" fill="#1a0a2e" rx="3"/>
        <rect x="0" y="0" width="{width * pct / 100:.1f}" height="14" fill="{color}" rx="3"/>
    </svg>'''


def emerging_badge(m: dict) -> str:
    runs = m.get("runs", 0)
    if 5 <= runs < 50:
        return f'<span class="emerging" title="{runs} runs, datos preliminares">emergente</span>'
    return ""


def podium_card(rank: int, m: dict) -> str:
    colors = {1: "#39ff14", 2: "#00d4ff", 3: "#ff006e"}
    border = colors.get(rank, "#39ff14")
    badge = emerging_badge(m)
    return f'''<div class="podium-card" style="border-color:{border}">
        <div class="podium-rank" style="color:{border}">#{rank}</div>
        <div class="podium-name">{m["name"]} {badge}</div>
        <div class="podium-score">{m.get("score_global", 0):.2f}</div>
        <div class="podium-meta">{m.get("provider", "openrouter")} · quality {m.get("quality_avg") or "—"} · {m.get("runs", 0)} runs</div>
    </div>'''


def render(models: dict) -> str:
    # Modelos con base solida (>=50 runs) y emergentes (<50 runs, >=5 runs)
    ranked = [m for m in models["models"] if m.get("score_global") is not None and m.get("runs", 0) >= 50]
    ranked.sort(key=lambda x: -x["score_global"])
    emerging = [m for m in models["models"] if m.get("score_global") is not None and 5 <= m.get("runs", 0) < 50]
    emerging.sort(key=lambda x: -x["score_global"])
    total_runs = sum(m.get("runs", 0) for m in models["models"])
    tested_count = models.get("tested_count", len(ranked))
    total_models = models.get("total_models", len(models["models"]))

    # Para el brief usamos los datos mas llamativos: top solidos + top emergentes,
    # pero marcamos a los emergentes con un indicador. Excluimos modelos que
    # deliberadamente quedaron fuera de este lanzamiento.
    excluded_patterns = ("north-mini-code",)
    featured = sorted(
        [m for m in ranked + emerging if not any(p in m.get("id", "") for p in excluded_patterns)],
        key=lambda x: -x["score_global"]
    )

    top10 = featured[:12]
    top3 = featured[:3]

    # Lookup de modelos en OpenRouter para normalizar precios de referencia
    openrouter_lookup = {
        m.get("key", m.get("id", "")): m
        for m in models["models"]
        if m.get("provider") == "openrouter" and m.get("cost_per_1k_calls_usd") is not None
    }

    # Badges (usamos featured para capturar emergentes llamativos)
    by_quality = sorted(featured, key=lambda x: -(x.get("quality_avg") or 0))
    featured_with_or_cost = [m for m in featured if normalised_cost_per_call(m, openrouter_lookup) is not None]
    by_cost_eff = sorted(
        featured_with_or_cost,
        key=lambda x: -(x.get("score_global", 0) / (normalised_cost_per_call(x, openrouter_lookup) + 1e-9))
    )
    by_speed = sorted(featured, key=lambda x: -(x.get("tokens_per_second") or 0))
    by_cheap = sorted(
        featured_with_or_cost,
        key=lambda x: (normalised_cost_per_call(x, openrouter_lookup), -x.get("score_global", 0))
    )
    open_source = [m for m in featured if m.get("open_source")]
    top_os = sorted(open_source, key=lambda x: -x.get("score_global", 0))

    # Categorías
    pillars = ["Razonamiento", "Coding", "Contenido", "Agentes"]
    top_by_pillar = {}
    for p in pillars:
        top_by_pillar[p] = sorted(
            [m for m in ranked if (m.get("score_by_pillar") or {}).get(p)],
            key=lambda x: -x["score_by_pillar"][p]
        )[:5]

    # NIAH
    niah_models = []
    for m in models["models"]:
        suites = m.get("score_by_suite", {}) or {}
        niah_scores = [v for k, v in suites.items() if "niah" in k]
        if niah_scores:
            niah_models.append({"name": m["name"], "niah_avg": round(sum(niah_scores) / len(niah_scores), 2)})
    niah_models.sort(key=lambda x: -x["niah_avg"])

    # Security
    sec_models = []
    for m in models["models"]:
        suites = m.get("score_by_suite", {}) or {}
        if "prompt_injection_es" in suites:
            sec_models.append({"name": m["name"], "sec": suites["prompt_injection_es"]})
    sec_models.sort(key=lambda x: -x["sec"])

    max_score = top10[0]["score_global"] if top10 else 10

    qr_calc = qr_b64(URL_CALC)
    qr_repo = qr_b64(URL_REPO)

    # Insights dinámicos
    insights = []
    if top_os:
        badge = emerging_badge(top_os[0])
        insights.append(f"<strong>Mejor open-source:</strong> {top_os[0]['name']} {badge} ({top_os[0]['score_global']:.2f}) — opción sin vendor lock-in.")
    if by_cost_eff:
        badge = emerging_badge(by_cost_eff[0])
        insights.append(f"<strong>Mejor relación calidad/precio:</strong> {by_cost_eff[0]['name']} {badge} — score {by_cost_eff[0]['score_global']:.2f} a {fmt_cost(by_cost_eff[0], openrouter_lookup)}.")
    if by_speed:
        badge = emerging_badge(by_speed[0])
        insights.append(f"<strong>Mas rapido:</strong> {by_speed[0]['name']} {badge} a {by_speed[0].get('tokens_per_second', 0):.0f} tok/s.")
    if sec_models:
        insights.append(f"<strong>Seguridad:</strong> {sec_models[0]['name']} lidera prompt-injection ({sec_models[0]['sec']:.2f}); modelos cheap filtran ~2.0.")
    if emerging:
        badge = emerging_badge(emerging[0])
        insights.append(f"<strong>Dato llamativo:</strong> {emerging[0]['name']} {badge} ya alcanza {emerging[0]['score_global']:.2f} con solo {emerging[0]['runs']} runs.")

    # Recomendaciones por caso de uso: usamos modelos con base solida (>=50 runs)
    # para dar respuestas confiables; los emergentes quedan para ranking e insights.
    coding_top = sorted(
        [m for m in ranked if (m.get("score_by_pillar") or {}).get("Coding")],
        key=lambda x: -x["score_by_pillar"]["Coding"]
    )[:3]
    agentes_top = sorted(
        [m for m in ranked if (m.get("score_by_pillar") or {}).get("Agentes")],
        key=lambda x: -x["score_by_pillar"]["Agentes"]
    )[:3]
    contenido_top = sorted(
        [m for m in ranked if (m.get("score_by_pillar") or {}).get("Contenido")],
        key=lambda x: -x["score_by_pillar"]["Contenido"]
    )[:3]
    razonamiento_top = sorted(
        [m for m in ranked if (m.get("score_by_pillar") or {}).get("Razonamiento")],
        key=lambda x: -x["score_by_pillar"]["Razonamiento"]
    )[:3]

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>AI Model Benchmark Executive Brief — {MONTH} {YEAR}</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700;800&family=Inter:wght@400;600;700&display=swap');

@page {{
    size: A4 landscape;
    margin: 8mm;
    background: #0a0a1a;
}}

* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html, body {{ background: #0a0a1a; }}
body {{
    font-family: 'Inter', sans-serif;
    color: #ffffff;
    font-size: 9pt;
    line-height: 1.35;
}}

.page {{
    page-break-after: always;
    width: 274mm;
    height: 184mm;
    padding: 10mm;
    background: #0a0a1a;
    position: relative;
    overflow: hidden;
}}
.page:last-child {{ page-break-after: auto; }}

h1, h2, h3, h4 {{ font-family: 'JetBrains Mono', monospace; }}

.kicker {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 8pt;
    color: #39ff14;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 6px;
}}

/* P1 COVER */
.cover {{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}}
.cover-header {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
}}
.cover-title {{
    font-size: 42pt;
    color: #39ff14;
    text-shadow: 0 0 20px rgba(57, 255, 20, 0.45);
    line-height: 1.0;
}}
.cover-subtitle {{
    font-size: 14pt;
    color: #00d4ff;
    margin-top: 8px;
}}
.cover-month {{
    display: inline-block;
    font-size: 16pt;
    font-weight: 800;
    color: #0a0a1a;
    background: #ff006e;
    padding: 6px 16px;
    border-radius: 4px;
    margin-top: 10px;
}}
.cover-qr {{
    text-align: center;
    background: #1a1a2e;
    border: 1px solid #533483;
    border-radius: 6px;
    padding: 10px;
}}
.cover-qr img {{ width: 80px; height: 80px; }}
.cover-qr .url {{ font-family: 'JetBrains Mono', monospace; font-size: 7pt; color: #39ff14; margin-top: 4px; }}

.podium {{
    display: flex;
    gap: 16px;
    margin: 14px 0;
}}
.podium-card {{
    flex: 1;
    background: #1a1a2e;
    border: 2px solid;
    border-radius: 6px;
    padding: 14px 16px;
    text-align: center;
}}
.podium-rank {{ font-size: 24pt; font-weight: 800; }}
.podium-name {{ font-size: 13pt; font-weight: 700; color: #ffffff; margin: 6px 0; }}
.podium-score {{ font-size: 26pt; font-weight: 800; color: #39ff14; }}
.podium-meta {{ font-size: 7.5pt; color: #b0b0b0; margin-top: 4px; }}

.stats-row {{
    display: flex;
    gap: 12px;
}}
.stat-card {{
    flex: 1;
    background: #1a0a2e;
    border-left: 3px solid #39ff14;
    padding: 10px 12px;
    border-radius: 0 4px 4px 0;
}}
.stat-card .n {{ font-family: 'JetBrains Mono', monospace; font-size: 18pt; font-weight: 800; color: #39ff14; }}
.stat-card .l {{ font-size: 7.5pt; color: #b0b0b0; text-transform: uppercase; letter-spacing: 1px; }}

.cover-footer {{
    font-size: 8pt;
    color: #b0b0b0;
    text-align: center;
}}

/* P2 TOP 10 */
.two-col {{
    display: flex;
    gap: 16px;
    height: calc(100% - 40px);
}}
.two-col > div {{ flex: 1; }}

.section-title {{
    font-size: 18pt;
    color: #39ff14;
    border-bottom: 2px solid #39ff14;
    padding-bottom: 4px;
    margin-bottom: 10px;
}}

.top10-table {{ width: 100%; border-collapse: collapse; font-size: 8.5pt; }}
.top10-table td {{ padding: 5px 4px; border-bottom: 1px solid #1a0a2e; vertical-align: middle; }}
.top10-table tr:nth-child(even) {{ background: rgba(26,10,46,0.5); }}
.top10-table .rank {{ font-family: 'JetBrains Mono', monospace; color: #39ff14; font-weight: 700; width: 22px; }}
.top10-table .name {{ color: #ffffff; font-weight: 600; }}
.top10-table .score {{ font-family: 'JetBrains Mono', monospace; color: #39ff14; font-weight: 700; width: 36px; text-align: right; }}

.insight-list {{
    list-style: none;
    padding: 0;
}}
.insight-list li {{
    background: #1a1a2e;
    border-left: 3px solid #00d4ff;
    padding: 8px 12px;
    margin-bottom: 8px;
    border-radius: 0 4px 4px 0;
    font-size: 8.5pt;
}}

/* P3 USE CASES */
.use-grid {{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
    height: calc(100% - 40px);
}}
.use-card {{
    background: #1a1a2e;
    border: 1px solid #533483;
    border-top: 3px solid #39ff14;
    border-radius: 4px;
    padding: 12px;
}}
.use-card.cyan {{ border-top-color: #00d4ff; }}
.use-card.magenta {{ border-top-color: #ff006e; }}
.use-card.purple {{ border-top-color: #b59cff; }}
.use-title {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 11pt;
    color: #ffffff;
    margin-bottom: 8px;
}}
.use-pick {{
    font-size: 10pt;
    color: #39ff14;
    font-weight: 700;
    margin-bottom: 4px;
}}
.use-pick.cyan {{ color: #00d4ff; }}
.use-pick.magenta {{ color: #ff006e; }}
.use-pick.purple {{ color: #b59cff; }}
.use-meta {{ font-size: 7.5pt; color: #b0b0b0; margin-bottom: 6px; }}
.use-alt {{ font-size: 8pt; color: #dbdbe5; }}
.use-alt strong {{ color: #ffffff; }}

/* P4 CATEGORIES */
.three-col {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    margin-bottom: 12px;
}}
.cat-card {{
    background: #1a1a2e;
    border: 1px solid #533483;
    border-radius: 4px;
    padding: 10px;
}}
.cat-title {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 9.5pt;
    color: #00d4ff;
    margin-bottom: 6px;
}}
.cat-table {{ width: 100%; font-size: 8pt; border-collapse: collapse; }}
.cat-table td {{ padding: 3px 0; border-bottom: 1px solid #1a0a2e; }}
.cat-table .n {{ color: #39ff14; font-weight: 700; width: 16px; }}
.cat-table .s {{ font-family: 'JetBrains Mono', monospace; color: #39ff14; text-align: right; }}

.badge-row {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 10px;
}}
.badge {{
    background: #1a0a2e;
    border: 1px solid #39ff14;
    border-radius: 20px;
    padding: 5px 10px;
    font-size: 8pt;
    color: #39ff14;
}}
.badge.cyan {{ border-color: #00d4ff; color: #00d4ff; }}
.badge.magenta {{ border-color: #ff006e; color: #ff006e; }}
.badge.purple {{ border-color: #b59cff; color: #b59cff; }}

/* P5 PROVIDERS */
.providers-table {{
    width: 100%;
    font-size: 8pt;
    border-collapse: collapse;
    margin-bottom: 10px;
}}
.providers-table th {{
    background: #1a0a2e;
    color: #39ff14;
    font-family: 'JetBrains Mono', monospace;
    text-align: left;
    padding: 6px;
    border-bottom: 1px solid #533483;
}}
.providers-table td {{ padding: 5px 6px; border-bottom: 1px solid #1a0a2e; }}

.tip {{
    background: rgba(57, 255, 20, 0.08);
    border-left: 3px solid #39ff14;
    padding: 8px 12px;
    border-radius: 0 4px 4px 0;
    font-size: 8.5pt;
}}

/* P6 METHODOLOGY */
.formula-box {{
    background: #1a0a2e;
    border: 1px solid #39ff14;
    border-radius: 6px;
    padding: 12px;
    margin-bottom: 12px;
}}
.formula-title {{
    font-family: 'JetBrains Mono', monospace;
    color: #00d4ff;
    font-size: 10pt;
    margin-bottom: 6px;
}}
.formula-row {{
    display: flex;
    gap: 12px;
    font-size: 8.5pt;
    color: #dbdbe5;
    margin-bottom: 3px;
}}
.formula-pct {{ font-family: 'JetBrains Mono', monospace; color: #39ff14; font-weight: 700; width: 40px; }}

.cta-center {{
    text-align: center;
    margin-top: 16px;
}}
.cta-center img {{ width: 130px; height: 130px; }}
.cta-center .url {{ font-family: 'JetBrains Mono', monospace; color: #39ff14; font-size: 9pt; margin-top: 6px; }}

.footer-brand {{
    position: absolute;
    bottom: 8mm;
    left: 10mm;
    right: 10mm;
    text-align: center;
    font-family: 'JetBrains Mono', monospace;
    font-size: 8pt;
    color: #b0b0b0;
}}

.disclaimer {{
    font-size: 7.5pt;
    color: #b0b0b0;
    margin-top: 8px;
}}

.emerging {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 6.5pt;
    color: #ff006e;
    border: 1px solid #ff006e;
    border-radius: 10px;
    padding: 1px 6px;
    margin-left: 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}}

.why-list {{
    list-style: none;
    margin-top: 6px;
}}
.why-list li {{
    font-size: 7.5pt;
    color: #dbdbe5;
    margin-bottom: 3px;
    padding-left: 12px;
    position: relative;
}}
.why-list li::before {{
    content: "+";
    position: absolute;
    left: 0;
    color: #39ff14;
    font-weight: 700;
}}
.why-list li.why-not::before {{
    content: "-";
    color: #ff006e;
}}

.qr-row {{
    display: flex;
    gap: 16px;
    justify-content: center;
    margin-top: 8px;
}}
.qr-box {{
    text-align: center;
    background: #1a1a2e;
    border: 1px solid #533483;
    border-radius: 6px;
    padding: 8px 12px;
}}
.qr-box img {{ width: 70px; height: 70px; }}
.qr-box .url {{ font-family: 'JetBrains Mono', monospace; font-size: 6.5pt; color: #39ff14; margin-top: 3px; }}

.cost-note {{
    font-size: 6.5pt;
    color: #b0b0b0;
    font-weight: 400;
}}

.community {{
    text-align: center;
    font-family: 'JetBrains Mono', monospace;
    font-size: 8pt;
    color: #b59cff;
    margin-top: 8px;
}}
</style>
</head>
<body>

<!-- ============================================================ -->
<!-- P1 COVER -->
<!-- ============================================================ -->
<div class="page cover">
    <div class="cover-header">
        <div>
            <div class="kicker">// Benchmark de Modelos AI</div>
            <div class="cover-title">AI Model<br>Benchmark</div>
            <div class="cover-subtitle">Executive Brief para emprendedores hispanohablantes</div>
            <div class="cover-month">{MONTH} {YEAR}</div>
        </div>
        <div class="qr-row">
            <div class="qr-box">
                <img src="data:image/png;base64,{qr_calc}" alt="QR Calculadora">
                <div class="url">Calculadora</div>
            </div>
            <div class="qr-box">
                <img src="data:image/png;base64,{qr_repo}" alt="QR Repo">
                <div class="url">Repo + datos</div>
            </div>
        </div>
    </div>

    <div class="kicker" style="margin-top:10px;">// Top 3 modelos del mes</div>
    <div class="podium">
        {''.join(podium_card(i, m) for i, m in enumerate(top3, 1))}
    </div>

    <div class="stats-row">
        <div class="stat-card"><div class="n">{tested_count}</div><div class="l">Modelos testeados</div></div>
        <div class="stat-card"><div class="n">{total_models}</div><div class="l">En catálogo</div></div>
        <div class="stat-card"><div class="n">{total_runs:,}+</div><div class="l">Runs reales</div></div>
        <div class="stat-card"><div class="n">26</div><div class="l">Suites</div></div>
        <div class="stat-card"><div class="n">91</div><div class="l">Tests prácticos</div></div>
    </div>

    <div class="cover-footer">
        Medido desde Santiago, Chile · v3.0 · MIT · Datos abiertos · PRs y sugerencias bienvenidas en el repo.<br>
        Hecho con tests reales, cafeína y feedback de la comunidad hispanohablante.
    </div>
</div>

<!-- ============================================================ -->
<!-- P2 TOP 10 + INSIGHTS -->
<!-- ============================================================ -->
<div class="page">
    <div class="kicker">// Ranking global</div>
    <div class="section-title">Top 12 modelos</div>
    <div class="two-col">
        <div>
            <table class="top10-table">
"""
    for i, m in enumerate(top10, 1):
        html += f"""                <tr>
                    <td class="rank">#{i}</td>
                    <td class="name">{m['name']}</td>
                    <td>{bar_svg(m['score_global'], max_score, width=200)}</td>
                    <td class="score">{m['score_global']:.2f}</td>
                </tr>
"""

    html += f"""            </table>
            <p style="font-size:7.5pt;color:#b0b0b0;margin-top:8px;">
                Score compuesto v3.0: quality 70% + costo 15% + velocidad 7.5% + latencia 7.5%.
            </p>
        </div>
        <div>
            <div class="section-title" style="font-size:14pt;border-color:#00d4ff;color:#00d4ff;">Insights del mes</div>
            <ul class="insight-list">
                {''.join(f'<li>{x}</li>' for x in insights[:4])}
            </ul>

            <div class="section-title" style="font-size:14pt;border-color:#ff006e;color:#ff006e;margin-top:12px;">Nuevos este mes</div>
            <ul class="insight-list">
                <li><strong>Grok 4.3</strong> entra con score oficial {next((m['score_global'] for m in ranked if 'grok-4.3' in m['id'].lower()), 0):.2f} (metodologia v3.0 z-score; calidad promedio, costo elevado).</li>
                <li><strong>Nemotron 3 Ultra 550B</strong> ahora en OpenRouter: score {next((m['score_global'] for m in ranked if 'nemotron-3' in m['id'].lower()), 0):.2f} y costo competitivo.</li>
                <li><strong>North Mini Code</strong> quedo fuera de este lanzamiento por falta de endpoint de pago estable en OpenRouter.</li>
            </ul>
        </div>
    </div>
    <div class="footer-brand">Ver ranking completo en benchmarks.cristiantala.com</div>
</div>

<!-- ============================================================ -->
<!-- P3 USE CASES -->
<!-- ============================================================ -->
<div class="page">
    <div class="kicker">// Recomendaciones por caso de uso</div>
    <div class="section-title">Qué modelo usar</div>
    <div class="use-grid">
        <div class="use-card">
            <div class="use-title">Coding</div>
            <div class="use-pick">{coding_top[0]['name'] if coding_top else '—'} {emerging_badge(coding_top[0]) if coding_top else ''}</div>
            <div class="use-meta">Score coding {(coding_top[0].get('score_by_pillar') or {}).get('Coding', '—') if coding_top else '—'} · {fmt_cost(coding_top[0], openrouter_lookup) if coding_top else '—'}</div>
            <ul class="why-list">
                <li>Lidera la categoria con el score mas alto en coding del benchmark.</li>
                <li>{'Es open-source y ' if coding_top and coding_top[0].get('open_source') else ''}Costo ultra bajo en OpenRouter; ideal para plugins, scripts y tareas atomicas.</li>
                <li class="why-not">No usamos Qwen3-Coder-Next (#3 global, score 8.13) porque cuesta y {coding_top[0]['name'] if coding_top else 'este'} cubre la mayoria de tareas de codigo. Opus 4.8 es overkill y requiere suscripcion para coding atomico.</li>
            </ul>
            <div class="use-alt"><strong>Alternativas:</strong> {', '.join(m['name'] for m in coding_top[1:3]) if len(coding_top) > 1 else '—'}</div>
        </div>
        <div class="use-card cyan">
            <div class="use-title">Agentes / Operaciones</div>
            <div class="use-pick cyan">{agentes_top[0]['name'] if agentes_top else '—'} {emerging_badge(agentes_top[0]) if agentes_top else ''}</div>
            <div class="use-meta">Score agentes {(agentes_top[0].get('score_by_pillar') or {}).get('Agentes', '—') if agentes_top else '—'} · {fmt_cost(agentes_top[0], openrouter_lookup) if agentes_top else '—'}</div>
            <ul class="why-list">
                <li>Mejor score en tool calling, orquestacion y workflows operativos.</li>
                <li>{f"{agentes_top[0].get('tokens_per_second', 0):.0f} tok/s" if agentes_top and agentes_top[0].get('tokens_per_second') else 'Baja latencia'} para respuestas sincronicas con el usuario final.</li>
                <li class="why-not">No usamos Claude Haiku 4.5 (score agentes 7.85) porque requiere suscripcion de Anthropic; {agentes_top[0]['name'] if agentes_top else 'este'} entrega latencia baja sin costo fijo.</li>
            </ul>
            <div class="use-alt"><strong>Alternativas:</strong> {', '.join(m['name'] for m in agentes_top[1:3]) if len(agentes_top) > 1 else '—'}</div>
        </div>
        <div class="use-card magenta">
            <div class="use-title">Contenido / Marketing</div>
            <div class="use-pick magenta">{contenido_top[0]['name'] if contenido_top else '—'} {emerging_badge(contenido_top[0]) if contenido_top else ''}</div>
            <div class="use-meta">Score contenido {(contenido_top[0].get('score_by_pillar') or {}).get('Contenido', '—') if contenido_top else '—'} · {fmt_cost(contenido_top[0], openrouter_lookup) if contenido_top else '—'}</div>
            <ul class="why-list">
                <li>Lidera la categoria con el mejor score en generacion de contenido en espanol.</li>
                <li>Tono natural para copy, newsletters y redes sociales sin sonar robotico.</li>
                <li class="why-not">No usamos Llama 4 Scout (score contenido 8.35) porque {contenido_top[0]['name'] if contenido_top else 'este'} es mas rapido y mantiene un costo competitivo en su provider.</li>
            </ul>
            <div class="use-alt"><strong>Alternativas:</strong> {', '.join(m['name'] for m in contenido_top[1:3]) if len(contenido_top) > 1 else '—'}</div>
        </div>
        <div class="use-card purple">
            <div class="use-title">Razonamiento / Analisis</div>
            <div class="use-pick purple">{razonamiento_top[0]['name'] if razonamiento_top else '—'} {emerging_badge(razonamiento_top[0]) if razonamiento_top else ''}</div>
            <div class="use-meta">Score razonamiento {(razonamiento_top[0].get('score_by_pillar') or {}).get('Razonamiento', '—') if razonamiento_top else '—'} · {fmt_cost(razonamiento_top[0], openrouter_lookup) if razonamiento_top else '—'}</div>
            <ul class="why-list">
                <li>Mejor score en analisis de negocio, resumenes ejecutivos y toma de decisiones con datos.</li>
                <li>No somos solo un benchmark de codigo: razonamiento, contenido y agentes pesan igual.</li>
                <li class="why-not">No usamos Claude Opus 4.8 ni DeepSeek R1 para razonamiento estandar porque {razonamiento_top[0]['name'] if razonamiento_top else 'este'} es suficiente y evita el costo premium.</li>
            </ul>
            <div class="use-alt"><strong>Alternativas:</strong> {', '.join(m['name'] for m in razonamiento_top[1:3]) if len(razonamiento_top) > 1 else '—'}</div>
        </div>
    </div>
    <div class="footer-brand">Recomendaciones detalladas por presupuesto en el repo</div>
</div>

<!-- ============================================================ -->
<!-- P4 CATEGORIES + BADGES -->
<!-- ============================================================ -->
<div class="page">
    <div class="kicker">// Rankings por categoría</div>
    <div class="section-title">Top 5 por pilar</div>
    <div class="three-col">
"""
    for p in pillars:
        html += f'''<div class="cat-card">
            <div class="cat-title">{p}</div>
            <table class="cat-table">
'''
        for i, m in enumerate(top_by_pillar.get(p, [])[:5], 1):
            html += f'<tr><td class="n">#{i}</td><td>{m["name"][:26]}</td><td class="s">{m["score_by_pillar"][p]:.2f}</td></tr>\n'
        html += '''            </table>
        </div>
'''

    html += f'''
    </div>

    <div class="kicker" style="margin-top:8px;">// Badges especiales</div>
    <div class="badge-row">
        <div class="badge">Top global: {top3[0]['name'] if top3 else '—'}</div>
        <div class="badge cyan">Mejor calidad: {by_quality[0]['name'] if by_quality else '—'}</div>
        <div class="badge">Mas rapido: {by_speed[0]['name'] if by_speed else '—'} ({by_speed[0].get('tokens_per_second', 0):.0f} tok/s)</div>
        <div class="badge magenta">Seguridad: {sec_models[0]['name'] if sec_models else '—'}</div>
        <div class="badge purple">NIAH: {niah_models[0]['name'] if niah_models else '—'}</div>
        <div class="badge">Open-source: {top_os[0]['name'] if top_os else '—'}</div>
    </div>

    <div class="footer-brand">Explorá por categoría en benchmarks.cristiantala.com</div>
</div>

<!-- ============================================================ -->
<!-- P5 PROVIDERS -->
<!-- ============================================================ -->
<div class="page">
    <div class="kicker">// Proveedores y costos</div>
    <div class="section-title">Mapa de proveedores</div>
    <table class="providers-table">
        <thead>
            <tr><th>Provider</th><th>Tipo</th><th>Modelos clave</th><th>Costo</th><th>Notas</th></tr>
        </thead>
        <tbody>
            <tr><td><strong>NVIDIA NIM</strong></td><td>Free tier</td><td>DeepSeek V4 Flash, Gemma 4, Nemotron, Qwen 3-Next</td><td>$0</td><td>40 RPM, ideal para bajo volumen</td></tr>
            <tr><td><strong>Xiaomi MiMo</strong></td><td>Sub</td><td>MiMo V2.5 family</td><td>$14/mes</td><td>Español neutro fuerte</td></tr>
            <tr><td><strong>MiniMax</strong></td><td>Sub / API</td><td>M2.7 Highspeed</td><td>$19/mes o $0.30/$1.20</td><td>Ultra baja latencia</td></tr>
            <tr><td><strong>Ollama Cloud</strong></td><td>Sub</td><td>GPT-OSS 120B, DeepSeek V4, Qwen 3.5</td><td>$30/mes</td><td>5 modelos, alta fiabilidad</td></tr>
            <tr><td><strong>OpenRouter</strong></td><td>Aggregator</td><td>290+ modelos</td><td>Variable</td><td>1 API key, fallback automático</td></tr>
            <tr><td><strong>OpenAI / Anthropic / Google</strong></td><td>API directa</td><td>GPT, Claude, Gemini</td><td>Premium</td><td>Mejor calidad, costo alto</td></tr>
        </tbody>
    </table>

    <div class="tip">
        <strong>Estrategia recomendada:</strong> 1 sub barata (MiMo $14) para producción base + NVIDIA NIM gratis para modelos especializados + OpenRouter con $20-50 de crédito como fallback.
    </div>

    <div class="kicker" style="margin-top:12px;">// Estrategia por presupuesto</div>
    <div class="two-col" style="height:auto;margin-top:8px;">
        <div class="tip"><strong>~$0/mes:</strong> NIM gratis + Groq cheap + modelos locales.</div>
        <div class="tip"><strong>~$30-50/mes:</strong> MiMo + Ollama Cloud + NIM.</div>
    </div>

    <div class="footer-brand">Comparativa completa de proveedores en el repo</div>
</div>

<!-- ============================================================ -->
<!-- P6 METHODOLOGY + CTA -->
<!-- ============================================================ -->
<div class="page" style="display:flex;flex-direction:column;justify-content:center;align-items:center;">
    <div class="kicker">// Metodología v3.0</div>
    <div class="formula-box" style="width:80%;">
        <div class="formula-title">Cómo se calcula el score global</div>
        <div class="formula-row"><span class="formula-pct">70%</span>Calidad (formato + sustancia + LLM-as-Judge Phi-4 14B)</div>
        <div class="formula-row"><span class="formula-pct">15%</span>Costo (por provider exacto, curva inversa)</div>
        <div class="formula-row"><span class="formula-pct">7.5%</span>Velocidad (tokens por segundo)</div>
        <div class="formula-row"><span class="formula-pct">7.5%</span>Latencia (primer token, medido desde Chile)</div>
        <div class="formula-row"><span class="formula-pct">badge</span>Tool calling y seguridad se muestran como badges, no entran en el compuesto</div>
    </div>

    <div class="disclaimer" style="width:80%;text-align:center;margin-bottom:12px;">
        91 tests prácticos en español + long-context NIAH-ES + seguridad prompt_injection_es.<br>
        Este benchmark es complemento, no sustituto de HumanEval, MMLU, SWE-bench, LMSYS Arena.
    </div>

    <div class="qr-row">
        <div class="qr-box">
            <img src="data:image/png;base64,{qr_calc}" alt="QR Calculadora">
            <div class="url">Calculadora</div>
        </div>
        <div class="qr-box">
            <img src="data:image/png;base64,{qr_repo}" alt="QR Repo">
            <div class="url">Repo + datos</div>
        </div>
    </div>

    <div class="community">
        Hecho con tests reales, cafeína y feedback de la comunidad hispanohablante.<br>
        PRs, issues y sugerencias bienvenidas en {URL_REPO}
    </div>

    <div class="footer-brand">
        Cristian Tala · benchmarks.cristiantala.com · {MONTH} {YEAR} · v3.0 · MIT
    </div>
</div>

</body>
</html>'''

    return html


def main():
    models = load_models()
    html = render(models)

    out_dir = ROOT / "cheatsheet"
    out_dir.mkdir(exist_ok=True)
    html_file = out_dir / f"executive_brief_{YEAR}_{now.strftime('%m')}_v3.html"
    pdf_file = out_dir / f"AI_Model_Benchmark_ExecutiveBrief_{MONTH_EN}_{YEAR}.pdf"

    html_file.write_text(html)
    HTML(string=html).write_pdf(str(pdf_file))

    print(f"PDF generado: {pdf_file}")
    print(f"HTML guardado: {html_file}")


if __name__ == "__main__":
    main()
