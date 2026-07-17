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
# OG image representativa del benchmark (ranking real, no el logo personal) — generada por
# benchmarks/generate_og_image.py. Usada en og:image/twitter:image de todas las pSEO.
OG_IMAGE = f"{SITE}/og-benchmark.png"
PILLARS = ["Coding", "Contenido", "Razonamiento", "Agentes"]
# Qué mide cada pilar (para el V/S por tipo de trabajo) — descripciones del README
PILLAR_DESC = {
    "Coding": ("Coding", "generar código, JSON estructurado y debugging en tareas reales "
               "(plugins WordPress, scripts, templates de N8N)", "lo que hacés"),
    "Contenido": ("Contenido y marketing", "blogs, copy y textos largos en español neutro "
                  "(no traducción del inglés)", "lo que escribís"),
    "Razonamiento": ("Razonamiento", "matemáticas, lógica formal y planificación multi-paso", "cómo decide"),
    "Agentes": ("Agentes y operaciones", "multi-turno largo, tool calling y flujos tipo N8N / Hermes", "cómo opera"),
}

# --- Comparaciones a generar (cada una = una página pSEO) ---------------------
GPT = {"name": "ChatGPT (GPT)", "match": ["gpt-", "gpt5", "gpt-5", "chatgpt"], "exclude": ["oss"]}
COMPARISONS = [
    # CORRECCION (12-jul-2026): los "320/mes" con que se justifico esta pagina salieron
    # de la LOCATION EQUIVOCADA — eran de US/ingles (9.900/mes), no de España. En español
    # la frase exacta "grok vs chatgpt" da ~0; la intencion existe con otra sintaxis:
    # "grok o chatgpt" ~90/mes (ES), "que es mejor grok o chatgpt" ~50/mes. Total ~150/mes.
    # La pagina se mantiene (la intencion es real y no la cubre nadie), pero el intent_kw
    # apunta a la sintaxis que la gente SI usa en español. Leccion: verificar la location.
    # La gente busca el HEAD ("grok"), no la version ("grok 4.5" ~50/mes) -> familia vs familia.
    {
        "slug": "grok-vs-chatgpt",
        "a": {"name": "Grok (xAI)", "match": ["grok"]}, "b": GPT,
        "title": "Grok vs ChatGPT en 2026: comparación con benchmark real",
        "intent_kw": "grok o chatgpt, que es mejor grok o chatgpt, grok vs chatgpt, comparativa grok gpt, xai vs openai",
    },
    {
        "slug": "grok-vs-claude",
        "a": {"name": "Grok (xAI)", "match": ["grok"]},
        "b": {"name": "Claude", "match": ["claude", "opus", "sonnet", "haiku", "fable"]},
        "title": "Grok vs Claude en 2026: comparación con benchmark real",
        "intent_kw": "grok vs claude, grok o claude, comparativa grok claude, xai vs anthropic",
    },
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
        "slug": "deepseek-vs-claude",
        "a": {"name": "DeepSeek", "match": ["deepseek"]},
        "b": {"name": "Claude", "match": ["claude"]},
        "title": "DeepSeek vs Claude en 2026: comparación con benchmark real",
        "intent_kw": "deepseek vs claude, deepseek o claude, comparativa deepseek anthropic, claude vs deepseek",
    },
    {
        "slug": "deepseek-vs-gemini",
        "a": {"name": "DeepSeek", "match": ["deepseek"]},
        "b": {"name": "Gemini", "match": ["gemini"]},
        "title": "DeepSeek vs Gemini en 2026: comparación con benchmark real",
        "intent_kw": "deepseek vs gemini, deepseek o gemini, comparativa deepseek google, gemini vs deepseek",
    },
    {
        "slug": "qwen-vs-llama",
        "a": {"name": "Qwen", "match": ["qwen"]}, "b": {"name": "Llama", "match": ["llama"]},
        "title": "Qwen vs Llama en 2026: comparación open source con benchmark real",
        "intent_kw": "qwen vs llama, llama vs qwen, mejor llm open source, comparativa qwen llama, modelos open source",
    },
    # Fable 5 (línea Mythos de Anthropic, jun-2026) — spike de búsquedas post-lanzamiento.
    # Cobertura editorial: EP15 ELHDA + blog cristiantala.com/probe-fable-5-vs-opus-4-8/
    {
        "slug": "fable-5-vs-opus-4-8",
        "a": {"name": "Claude Fable 5", "match": ["fable"]},
        "b": {"name": "Claude Opus 4.8", "match": ["opus-4.8", "opus 4.8"]},
        "title": "Fable 5 vs Opus 4.8 en 2026: comparación con benchmark real",
        "intent_kw": "fable 5 vs opus 4.8, claude fable vs opus, fable 5 anthropic benchmark, fable 5 vale la pena, mythos 5 anthropic",
    },
    {
        "slug": "fable-5-vs-gpt-5-5",
        "a": {"name": "Claude Fable 5", "match": ["fable"]},
        "b": {"name": "GPT-5.5", "match": ["gpt-5.5"]},
        "title": "Fable 5 vs GPT-5.5 en 2026: comparación con benchmark real",
        "intent_kw": "fable 5 vs gpt 5.5, claude fable vs chatgpt, anthropic vs openai 2026, fable 5 benchmark español",
    },
    {
        # Los dos flagship-sobre-flagship de 2026: el tier que Anthropic vende SOBRE Opus
        # contra el que OpenAI vende SOBRE Terra. Cobertura editorial: pilar + post GPT-5.6.
        "slug": "fable-5-vs-gpt-5-6-sol",
        "a": {"name": "Claude Fable 5", "match": ["fable"]},
        "b": {"name": "GPT-5.6 Sol", "match": ["gpt-5.6 sol"]},
        "title": "Fable 5 vs GPT-5.6 Sol en 2026: los dos flagships premium, medidos",
        "intent_kw": "fable 5 vs gpt 5.6 sol, claude fable vs gpt 5.6, flagship anthropic vs openai, fable 5 o gpt 5.6, mejores modelos premium 2026",
    },
    # --- Fable 5: más comparaciones para captar búsquedas post-lanzamiento ---
    {
        "slug": "fable-5-vs-claude-sonnet-4-6",
        "a": {"name": "Claude Fable 5", "match": ["fable"]},
        "b": {"name": "Claude Sonnet 4.6", "match": ["claude-sonnet-4-6", "sonnet 4.6"]},
        "title": "Fable 5 vs Claude Sonnet 4.6 en 2026: comparación con benchmark real",
        "intent_kw": "fable 5 vs sonnet 4.6, claude fable vs sonnet, fable 5 anthropic comparativa, sonnet 4.6 vs fable",
    },
    {
        "slug": "fable-5-vs-minimax-m3",
        "a": {"name": "Claude Fable 5", "match": ["fable"]},
        "b": {"name": "MiniMax M3", "match": ["minimax-m3"]},
        "title": "Fable 5 vs MiniMax M3 en 2026: comparación con benchmark real",
        "intent_kw": "fable 5 vs minimax m3, claude fable vs minimax, fable 5 benchmark costo, minimax m3 vs fable 5",
    },
    {
        "slug": "fable-5-vs-deepseek-r1",
        "a": {"name": "Claude Fable 5", "match": ["fable"]},
        "b": {"name": "DeepSeek R1", "match": ["deepseek-r1"]},
        "title": "Fable 5 vs DeepSeek R1 en 2026: comparación con benchmark real",
        "intent_kw": "fable 5 vs deepseek r1, claude fable vs deepseek, fable 5 razonamiento, deepseek r1 vs fable 5",
    },
    # --- Nuevas comparaciones junio 2026 (modelos recién disponibles / por medir) ---
    {
        "slug": "nemotron-3-ultra-vs-deepseek-v4-flash",
        "a": {"name": "Nemotron 3 Ultra", "match": ["nemotron-3-ultra"]},
        "b": {"name": "DeepSeek V4 Flash", "match": ["deepseek-v4-flash"], "exclude": ["deepseek-ai"]},
        "title": "Nemotron 3 Ultra vs DeepSeek V4 Flash en 2026: comparación con benchmark real",
        "intent_kw": "nemotron 3 ultra vs deepseek v4 flash, nvidia vs deepseek, mejor modelo barato 2026, llm calidad precio",
    },
    {
        "slug": "glm-5.2-vs-glm-5.1",
        "a": {"name": "GLM 5.2", "match": ["glm-5.2"]},
        "b": {"name": "GLM 5.1", "match": ["glm-5.1"], "exclude": ["glm5"]},
        "title": "GLM 5.2 vs GLM 5.1 en 2026: comparación con benchmark real",
        "intent_kw": "glm 5.2 vs glm 5.1, zhipu glm 5.2, glm 5.2 benchmark, glm 5.1 vs 5.2, mejor glm",
    },
    {
        "slug": "glm-5.2-vs-claude-opus-4-8",
        "a": {"name": "GLM 5.2", "match": ["glm-5.2"]},
        "b": {"name": "Claude Opus 4.8", "match": ["claude-opus-4-8", "opus-4.8"], "exclude": ["opus-4.8-fast"]},
        "title": "GLM 5.2 vs Claude Opus 4.8 en 2026: comparación con benchmark real",
        "intent_kw": "glm 5.2 vs claude opus 4.8, zhipu vs anthropic, glm 5.2 benchmark español, opus 4.8 vs glm",
    },
    {
        "slug": "grok-4.3-vs-gpt-5-5",
        "a": {"name": "Grok 4.3", "match": ["grok-4.3"]},
        "b": {"name": "GPT-5.5", "match": ["gpt-5.5"]},
        "title": "Grok 4.3 vs GPT-5.5 en 2026: comparación con benchmark real",
        "intent_kw": "grok 4.3 vs gpt 5.5, xai vs openai, grok vs chatgpt, mejor modelo flagship 2026",
    },
    {
        "slug": "gemini-3.5-flash-vs-gemini-2.5-flash",
        "a": {"name": "Gemini 3.5 Flash", "match": ["gemini-3.5-flash"]},
        "b": {"name": "Gemini 2.5 Flash", "match": ["gemini-2.5-flash"]},
        "title": "Gemini 3.5 Flash vs Gemini 2.5 Flash en 2026: comparación con benchmark real",
        "intent_kw": "gemini 3.5 flash vs gemini 2.5 flash, google gemini comparativa, gemini flash 3.5 vs 2.5",
    },
    # --- Lote julio 2026: GPT-5.6 (Luna/Terra/Sol) y Grok 4.5 ---
    {
        "slug": "gpt-5.6-vs-gpt-5.5",
        "a": {"name": "GPT-5.6", "match": ["gpt-5.6"]},
        "b": {"name": "GPT-5.5", "match": ["gpt-5.5"], "exclude": ["gpt-5.5-pro"]},
        "title": "GPT-5.6 vs GPT-5.5 en 2026: comparación con benchmark real",
        "intent_kw": "gpt 5.6 vs gpt 5.5, openai gpt 5.6 benchmark, chatgpt 5.6 vs 5.5, gpt 5.6 vale la pena",
    },
    {
        "slug": "gpt-5.6-vs-claude-opus-4-8",
        "a": {"name": "GPT-5.6", "match": ["gpt-5.6"]},
        "b": {"name": "Claude Opus 4.8", "match": ["claude-opus-4.8", "opus 4.8"], "exclude": ["opus-4.8-fast"]},
        "title": "GPT-5.6 vs Claude Opus 4.8 en 2026: comparación con benchmark real",
        "intent_kw": "gpt 5.6 vs claude opus 4.8, openai vs anthropic 2026, mejor modelo flagship, gpt 5.6 o opus 4.8",
    },
    {
        "slug": "gpt-5.6-vs-deepseek-v4",
        "a": {"name": "GPT-5.6", "match": ["gpt-5.6"]},
        "b": {"name": "DeepSeek V4", "match": ["deepseek-v4"], "exclude": ["deepseek-v3", "deepseek-r1"]},
        "title": "GPT-5.6 vs DeepSeek V4 en 2026: comparación con benchmark real",
        "intent_kw": "gpt 5.6 vs deepseek v4, openai vs deepseek 2026, deepseek v4 vs chatgpt, comparativa flagship",
    },
    {
        "slug": "gpt-5.6-vs-gemini-3.5-flash",
        "a": {"name": "GPT-5.6", "match": ["gpt-5.6"]},
        "b": {"name": "Gemini 3.5 Flash", "match": ["gemini-3.5-flash"]},
        "title": "GPT-5.6 vs Gemini 3.5 Flash en 2026: comparación con benchmark real",
        "intent_kw": "gpt 5.6 vs gemini 3.5 flash, openai vs google 2026, gemini flash vs chatgpt, comparativa flash",
    },
    {
        "slug": "gpt-5.6-vs-minimax-m3",
        "a": {"name": "GPT-5.6", "match": ["gpt-5.6"]},
        "b": {"name": "MiniMax M3", "match": ["minimax-m3"], "exclude": ["m2.7"]},
        "title": "GPT-5.6 vs MiniMax M3 en 2026: comparación con benchmark real",
        "intent_kw": "gpt 5.6 vs minimax m3, openai vs minimax, agentes minimax vs chatgpt, comparativa agentes 2026",
    },
    {
        "slug": "gpt-5.6-vs-claude-sonnet-4-6",
        "a": {"name": "GPT-5.6", "match": ["gpt-5.6"]},
        "b": {"name": "Claude Sonnet 4.6", "match": ["claude-sonnet-4-6", "sonnet 4.6"]},
        "title": "GPT-5.6 vs Claude Sonnet 4.6 en 2026: comparación con benchmark real",
        "intent_kw": "gpt 5.6 vs claude sonnet 4.6, openai vs anthropic sonnet, chatgpt vs claude sonnet, comparativa 2026",
    },
    {
        "slug": "grok-4.5-vs-grok-4.3",
        "a": {"name": "Grok 4.5", "match": ["grok-4.5"]},
        "b": {"name": "Grok 4.3", "match": ["grok-4.3"]},
        "title": "Grok 4.5 vs Grok 4.3 en 2026: comparación con benchmark real",
        "intent_kw": "grok 4.5 vs grok 4.3, xai grok comparativa, grok 4.5 benchmark, grok 4.3 vs 4.5",
    },
    {
        "slug": "grok-4.5-vs-gpt-5-6",
        "a": {"name": "Grok 4.5", "match": ["grok-4.5"]},
        "b": {"name": "GPT-5.6", "match": ["gpt-5.6"]},
        "title": "Grok 4.5 vs GPT-5.6 en 2026: comparación con benchmark real",
        "intent_kw": "grok 4.5 vs gpt 5.6, xai vs openai 2026, grok vs chatgpt, grok 4.5 o gpt 5.6",
    },
    {
        "slug": "grok-4.5-vs-claude-sonnet-4-6",
        "a": {"name": "Grok 4.5", "match": ["grok-4.5"]},
        "b": {"name": "Claude Sonnet 4.6", "match": ["claude-sonnet-4-6", "sonnet 4.6"]},
        "title": "Grok 4.5 vs Claude Sonnet 4.6 en 2026: comparación con benchmark real",
        "intent_kw": "grok 4.5 vs claude sonnet 4.6, xai vs anthropic, grok vs claude, comparativa 2026",
    },
    # --- Comparables por tier (OpenAI vs Anthropic) ---
    {
        "slug": "gpt-5.6-vs-fable-5",
        "a": {"name": "GPT-5.6", "match": ["gpt-5.6"]},
        "b": {"name": "Claude Fable 5", "match": ["fable"]},
        "title": "GPT-5.6 vs Claude Fable 5 en 2026: comparación con benchmark real",
        "intent_kw": "gpt 5.6 vs fable 5, openai vs anthropic fable, chatgpt vs fable 5, fable 5 benchmark español",
    },
    {
        "slug": "gpt-5.6-luna-vs-claude-haiku-4-5",
        "a": {"name": "GPT-5.6 Luna", "match": ["gpt-5.6-luna"]},
        "b": {"name": "Claude Haiku 4.5", "match": ["claude-haiku-4.5", "haiku 4.5"]},
        "title": "GPT-5.6 Luna vs Claude Haiku 4.5 en 2026: comparación con benchmark real",
        "intent_kw": "gpt 5.6 luna vs claude haiku 4.5, modelo rapido barato 2026, chatgpt luna vs haiku, comparativa economica",
    },
    {
        "slug": "gpt-5.6-terra-vs-claude-sonnet-4-6",
        "a": {"name": "GPT-5.6 Terra", "match": ["gpt-5.6-terra"]},
        "b": {"name": "Claude Sonnet 4.6", "match": ["claude-sonnet-4-6", "sonnet 4.6"]},
        "title": "GPT-5.6 Terra vs Claude Sonnet 4.6 en 2026: comparación con benchmark real",
        "intent_kw": "gpt 5.6 terra vs claude sonnet 4.6, modelo medio openai anthropic, chatgpt terra vs sonnet",
    },
    {
        "slug": "gpt-5.6-sol-vs-claude-opus-4-8",
        "a": {"name": "GPT-5.6 Sol", "match": ["gpt-5.6-sol"]},
        "b": {"name": "Claude Opus 4.8", "match": ["claude-opus-4-8", "opus 4.8"], "exclude": ["opus-4.8-fast"]},
        "title": "GPT-5.6 Sol vs Claude Opus 4.8 en 2026: comparación con benchmark real",
        "intent_kw": "gpt 5.6 sol vs claude opus 4.8, mejor modelo flagship 2026, chatgpt sol vs opus, openai vs anthropic",
    },
    # --- Variantes GPT-5.6 entre sí ---
    {
        "slug": "gpt-5.6-luna-vs-terra",
        "a": {"name": "GPT-5.6 Luna", "match": ["gpt-5.6-luna"]},
        "b": {"name": "GPT-5.6 Terra", "match": ["gpt-5.6-terra"]},
        "title": "GPT-5.6 Luna vs Terra en 2026: comparación con benchmark real",
        "intent_kw": "gpt 5.6 luna vs terra, diferencia luna terra, chatgpt 5.6 comparativa, gpt 5.6 cual elegir",
    },
    {
        "slug": "gpt-5.6-terra-vs-sol",
        "a": {"name": "GPT-5.6 Terra", "match": ["gpt-5.6-terra"]},
        "b": {"name": "GPT-5.6 Sol", "match": ["gpt-5.6-sol"]},
        "title": "GPT-5.6 Terra vs Sol en 2026: comparación con benchmark real",
        "intent_kw": "gpt 5.6 terra vs sol, diferencia terra sol, chatgpt 5.6 comparativa, gpt 5.6 flagship",
    },
    {
        "slug": "gpt-5.6-luna-vs-sol",
        "a": {"name": "GPT-5.6 Luna", "match": ["gpt-5.6-luna"]},
        "b": {"name": "GPT-5.6 Sol", "match": ["gpt-5.6-sol"]},
        "title": "GPT-5.6 Luna vs Sol en 2026: comparación con benchmark real",
        "intent_kw": "gpt 5.6 luna vs sol, chatgpt 5.6 barato vs flagship, diferencia luna sol, gpt 5.6 comparativa",
    },
]


_JSON_CACHE = None


def load_json():
    global _JSON_CACHE
    if _JSON_CACHE is None:
        _JSON_CACHE = json.loads(MODELS_JSON.read_text())
    return _JSON_CACHE


def load_models(incluir_deprecados: bool = False):
    """Los modelos que se pueden RECOMENDAR. Los deprecados quedan fuera por defecto.

    Un modelo cuyo endpoint ya no existe no es un candidato: no lo podés llamar.
    Publicarlo en una página de recomendación es peor que no publicar nada — alguien lee
    "el #5, y barato", lo integra, y se estrella contra un 404.

    No es hipotético: Devstral Small estuvo **#5 del ranking** meses después de que
    Mistral apagara su endpoint, y hoy aparece en 11 páginas del sitio, incluidas
    /mejor-llm-barato/ y las cuatro de "alternativas a X". Todas recomendándolo.

    Sus números NO se borran: siguen en models.json y en la sección *Retirados* de
    MODELOS.md como estadística histórica (son mediciones reales, sirven para el análisis).
    Pero no compiten y no se recomiendan.

    Lo mismo con las variantes de proveedor: el mismo modelo servido por otra infra. Su
    fila canónica ya está; dejarlas entrar haría que un modelo compita contra sí mismo.

    `incluir_deprecados=True` para las vistas históricas (comparación entre proveedores).
    """
    d = load_json()
    todos = d if isinstance(d, list) else (d.get("models") or list(d.values())[0])
    if incluir_deprecados:
        return todos
    return [m for m in todos
            if not m.get("retired") and not m.get("provider_variant")]


def get_meta():
    return load_json()


def get_counts():
    d = load_json()
    models = d.get("models", []) if isinstance(d, dict) else d
    tested = [m for m in models if m.get("tested")]
    return {
        "total_models": d.get("total_models", len(models)) if isinstance(d, dict) else len(models),
        "tested_count": d.get("tested_count", len(tested)) if isinstance(d, dict) else len(tested),
        "total_runs": sum(m.get("runs", 0) for m in tested),
    }


def fmt_k(n):
    """Redondea hacia abajo a miles y devuelve '10.000+'."""
    return f"{(n // 1000) * 1000:,}".replace(",", ".") + "+"


def fmt_pct(w):
    p = w * 100
    return f"{int(p)}" if p == int(p) else f"{p:.1f}".replace(".", ",")


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
        # Mínimo de runs para confiabilidad (estándar del benchmark: ≥50 runs). Evita que un
        # outlier con 3-12 runs (varianza alta) aparezca liderando por azar.
        if (m.get("runs") or 0) < 50:
            continue
        # Requiere score por pilar: los variantes 'thinking' a veces traen score_global
        # pero no score_by_pillar → mostrarían 0.0 en la tabla. Sin pillars no entran a
        # una comparación por pilar (queda el variante hermano que sí los tiene).
        if sum((m.get("score_by_pillar") or {}).get(p) or 0 for p in PILLARS) <= 0:
            continue
        out.append(m)
    # Ordena por CALIDAD MEDIA en los 4 pilares, no por score_global.
    # Con el compuesto, /grok-vs-chatgpt/ ponia Grok 4.1 Fast arriba de Grok 4.5:
    # el barato encabezaba una pagina que promete decir cual es MEJOR.
    def _cap(m):
        vals = [pillar(m, p) for p in PILLARS]
        vals = [v for v in vals if v > 0]
        return sum(vals) / len(vals) if vals else 0
    return sorted(out, key=lambda m: -_cap(m))


def pillar(m, name):
    """CALIDAD del modelo en ese pilar. No el compuesto con costo y velocidad.

    Una comparacion "X vs Y" responde CUAL ES MEJOR. Mostrar el compuesto (que
    incluye costo) responde otra cosa y confunde: en /grok-vs-chatgpt/ el compuesto
    ponia a Grok 4.1 Fast (barato) por encima de Grok 4.5 (el nuevo), como si fuera
    mejor modelo. Era mas barato, no mejor.

    El costo no se pierde: va en su propia columna, y el funnel cierra con "de los
    que empatan en capacidad, el mas barato es X". Primero cual es mejor; despues
    cuanto cuesta.
    """
    d = (m.get("dims_by_pillar") or {}).get(name) or {}
    q = d.get("quality_avg")
    if q is not None:
        return q
    return (m.get("score_by_pillar") or {}).get(name) or 0  # fallback: modelos viejos sin dims


def versions_compared(a_name, b_name, A, B):
    """Dice EXACTAMENTE que versiones entran de cada lado.

    "Grok vs ChatGPT" agrupa 4 modelos de un lado y 8 del otro. Sin decir cuales, la
    comparacion es opaca: el lector no sabe si el "Grok" que mira es el 4.5 nuevo o el
    4.3 viejo (que saca 2.89). Y cambia la conclusion.

    Tambien fija la fecha de corte: los modelos salen todo el tiempo, y una comparacion
    de familias sin lista de versiones envejece sin que se note.
    """
    def names(arr):
        return ", ".join(f"<strong>{esc(m['name'])}</strong>" for m in arr[:6]) or "—"

    return f"""<p class="versions">
    <span class="versions-label">Versiones que entran en esta comparación</span>
    <span class="versions-row">{esc(a_name)}: {names(A)}{' <em>y ' + str(len(A) - 6) + ' más</em>' if len(A) > 6 else ''}</span>
    <span class="versions-row">{esc(b_name)}: {names(B)}{' <em>y ' + str(len(B) - 6) + ' más</em>' if len(B) > 6 else ''}</span>
    <span class="versions-fine">Solo entran modelos con ≥50 runs. Ordenados por <strong>calidad media</strong>
    en los 4 pilares — no por precio.</span>
  </p>"""


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
    c = get_counts()
    w = get_meta().get("default_weights", {})
    q = fmt_pct(w.get("quality", 0.7))
    co = fmt_pct(w.get("cost", 0.15))
    sp = fmt_pct(w.get("speed", 0.075))
    la = fmt_pct(w.get("latency", 0.075))
    tc = fmt_pct(w.get("tool_calling", 0))
    tc_text = "no suma al score global" if w.get("tool_calling", 0) == 0 else f"{tc}% al score global"
    items = "\n    ".join(
        f"<li><strong>{PILLAR_DESC[p][0]}</strong> — {PILLAR_DESC[p][1]}.</li>" for p in PILLARS)
    return f"""<section>
  <h2>¿Qué mide este benchmark?</h2>
  <p>No es un benchmark académico (para eso están MMLU, HumanEval o SWE-bench). Es un benchmark
  <strong>aplicado para emprendedores hispanohablantes</strong>: mide qué modelo conviene poner en
  producción para casos reales, con lo que los benchmarks oficiales no cubren — costo en provider real,
  velocidad, español neutro y agentes multi-turno.</p>
  <p>Contamos con <strong>{c['total_models']} modelos catalogados</strong>, <strong>{c['tested_count']} testeados</strong>
  y <strong>{fmt_k(c['total_runs'])} runs reales</strong> evaluados por un
  <strong>LLM-as-Judge local (Phi-4, de Microsoft — sin conflicto de interés)</strong>, en 4 pilares:</p>
  <ul>
    {items}
  </ul>
  <p><strong>Dos números distintos, no los confundas.</strong> Las tablas por tarea de esta página se
  ordenan por <strong>calidad en esa tarea</strong>: capacidad pura, sin mezclar precio. Es la respuesta a
  "¿quién lo hace mejor?".</p>
  <p>El <strong>score global</strong> es otra cosa: una función ponderada
  (<strong>calidad {q}% + costo {co}% + velocidad {sp}% + latencia {la}%</strong>) que responde
  "¿qué conviene poner en producción?". Ahí un modelo barato y rápido sí puede superar a uno más capaz
  pero caro. Los dos números sirven — para preguntas distintas.</p>
  <p>Tool calling va como <strong>insignia aparte</strong> ({tc_text}): indica si el modelo soporta
  herramientas, no su calidad. <strong>Límite conocido:</strong> el juez es Phi-4 (14B) y varios modelos
  evaluados son más capaces que él — ordena bien, pero comprime las diferencias en la cima. Leé un empate
  como "el juez no los distingue", no como "son idénticos".
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
  <div class="table-scroll"><table class="results-table">
    <thead><tr><th scope="col">Tu caso</th><th scope="col">Ganador</th></tr></thead>
    <tbody>
      {"".join(verdict_rows)}
    </tbody>
  </table></div>
  <p class="meta">Este cuadro muestra el mejor por <strong>calidad de cada pilar</strong> — pero el "ganador" real depende de <strong>tu</strong> prioridad: calidad, costo o velocidad. No sabemos tu caso, así que ajustá esos pesos en la <a href="/">calculadora</a> y obtené el ganador para vos.</p>
</section>""")
    # Cierre del funnel. Estas paginas de comparacion son las que reciben el trafico
    # de NOVEDAD (un modelo sale y la gente busca "X vs Y" esa misma semana), y hasta
    # ahora terminaban en una tabla: el lector decidia y se iba. El link a la comunidad
    # vivia solo en el nav.
    secs.append(funnel_block())
    return "\n".join(secs)


def funnel_block():
    """Ver generate_rankings.funnel_block. Duplicado minimo a proposito: este modulo
    es el que importa generate_rankings (no al reves), y no quiero un import circular.
    Regla dura: no inventar perks -- solo la comunidad gratis y el ranking que se mueve.
    """
    return """<section class="funnel">
  <h2>Antes de migrar, haz esto</h2>
  <p>Ya sabes cuál gana en el papel. No lo cambies a ciegas: toma <strong>el mejor de cada familia</strong>
  y pásales <strong>cinco prompts reales tuyos</strong>, de los que ya corres en producción. Una
  comparación general te dice quién arranca adelante; <strong>tu caso decide quién gana</strong>.
  Son veinte minutos y te ahorran una migración equivocada.</p>
  <p class="funnel-note">Y una advertencia: este resultado se recalcula con cada lote de modelos nuevos.
  Como el score de cada modelo es <em>relativo a todos los demás</em>, un modelo nuevo mueve a todos.
  El ganador de hoy puede no serlo el mes que viene.</p>
  <p><a href="https://www.skool.com/cagala-aprende-repite?utm_source=benchmarks&amp;utm_medium=pseo&amp;utm_campaign=comparacion" target="_blank" rel="noopener" class="cta-primary">
  Ver la comunidad →</a></p>
  <p class="funnel-fine">Cada vez que corro un lote nuevo, publico el recálculo ahí — con los datos
  crudos y lo que cambió de lugar. Es también donde hay gente tomando esta misma decisión.
  Entrar es gratis.</p>
</section>"""


def faq(a_name, b_name, A, B):
    a0, b0 = A[0], B[0]
    tests_k = fmt_k(get_counts()["total_runs"])
    winner = a0 if a0["score_global"] >= b0["score_global"] else b0
    qas = [
        (
            f"¿{a_name} o {b_name} es mejor en 2026?",
            f"Depende de la tarea. En el cómputo global de nuestro benchmark gana {winner.get('name')}, "
            f"pero el mejor por pilar cambia (ver arriba). La pregunta correcta es 'mejor para qué caso'.",
            f"Depende de la tarea. En el cómputo global de nuestro benchmark gana <strong>{esc(winner.get('name'))}</strong>, "
            f"pero el mejor por pilar cambia (ver arriba). La pregunta correcta es \"mejor para qué caso\".",
        ),
        (
            "¿Estos datos de dónde salen?",
            f"De un benchmark abierto con {tests_k} runs reales y LLM-as-Judge local (Phi-4, Microsoft, sin conflicto de interés). "
            "Código y resultados en GitHub.",
            f"De un benchmark abierto con {tests_k} runs reales y LLM-as-Judge local (Phi-4, Microsoft, sin conflicto de interés). "
            "Código y resultados en <a href=\"https://github.com/ctala/ai-benchmarks-alternativos\" target=\"_blank\" rel=\"noopener\">GitHub</a>.",
        ),
        (
            "¿Cuál es más barato para agentes con volumen?",
            "Mirá la columna de costo en la tabla. Para 1.000+ calls/mes, el costo por millón de tokens domina el ROI por encima de "
            "diferencias chicas de calidad. Filtralo por tu presupuesto en la calculadora.",
            "Mirá la columna de costo en la tabla. Para 1.000+ calls/mes, el costo por millón de tokens domina el ROI por encima de "
            "diferencias chicas de calidad. Filtralo por tu presupuesto en la <a href=\"/\">calculadora</a>.",
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
  <h2>Preguntas frecuentes</h2>
  {details}
</section>"""


def page_shell(title, desc, kw, url, body):
    """Shell HTML reusable (head + header + main + footer). Lo comparten comparaciones y rankings."""
    today = date.today().isoformat()
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
<meta property="og:image:alt" content="Ranking de modelos IA del benchmark de Cristian Tala">
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
<!-- GTM: MISMO container que cristiantala.com (GTM-N69D7XXH) para poder seguir el
     funnel cruzado blog -> benchmark -> comunidad desde un solo lugar.
     DIFERIDO igual que en el blog: carga en la primera interaccion o a los 3.5s de
     idle, para no meterlo en la ruta critica del LCP.
     Antes: 0 de 57 paginas tenian analytics. Habia 45 CTAs a la comunidad y CERO
     forma de saber si convertian (Regla #8 del repo: tracking desde el dia uno). -->
<script>
(function () {{
  var loaded = false;
  function loadGTM() {{
    if (loaded) return;
    loaded = true;
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({{ 'gtm.start': new Date().getTime(), event: 'gtm.js' }});
    var j = document.createElement('script');
    j.async = true;
    j.src = 'https://www.googletagmanager.com/gtm.js?id=GTM-N69D7XXH';
    document.head.appendChild(j);
  }}
  ['pointerdown', 'keydown', 'touchstart', 'scroll'].forEach(function (ev) {{
    addEventListener(ev, loadGTM, {{ once: true, passive: true }});
  }});
  setTimeout(loadGTM, 3500);
}})();
</script>
</head>
<body>
<!-- Eventos del funnel. Sin esto no se puede saber que pagina alimenta la comunidad. -->
<script>
(function () {{
  window.dataLayer = window.dataLayer || [];
  var page = location.pathname.replace(/^\\/|\\/$/g, '') || 'home';
  document.addEventListener('click', function (e) {{
    var a = e.target.closest && e.target.closest('a');
    if (!a) return;
    var href = a.getAttribute('href') || '';
    if (href.indexOf('skool.com') > -1) {{
      window.dataLayer.push({{
        event: 'cta_comunidad',
        cta_ubicacion: a.closest('.funnel') ? 'funnel' : (a.closest('header') ? 'nav' : 'otro'),
        pagina_pseo: page
      }});
    }} else if (href.indexOf('/?preset=') === 0 || href.indexOf('/?calls=') === 0) {{
      window.dataLayer.push({{ event: 'ir_a_calculadora', pagina_pseo: page }});
    }}
  }}, {{ passive: true }});
  // Llego a ver la tabla (la evidencia). Marca lectura real, no rebote.
  var t = document.querySelector('.results-table');
  if (t && 'IntersectionObserver' in window) {{
    var io = new IntersectionObserver(function (es) {{
      if (es[0].isIntersecting) {{
        window.dataLayer.push({{ event: 've_tabla', pagina_pseo: page }});
        io.disconnect();
      }}
    }}, {{ threshold: 0.25 }});
    io.observe(t);
  }}
}})();
</script>
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
{body}
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


def render(cfg, A, B):
    a_name, b_name = cfg["a"]["name"], cfg["b"]["name"]
    today = date.today().isoformat()
    tests_k = fmt_k(get_counts()["total_runs"])
    desc = (f"{a_name} vs {b_name} comparados con {tests_k} runs reales: coding, contenido, "
            f"razonamiento, agentes, costo y velocidad. Benchmark abierto en español.")
    url = f"{SITE}/{cfg['slug']}/"
    rows = "\n        ".join(row(i + 1, m, top=(i == 0)) for i, m in enumerate(A[:5] + B[:5]))
    body = f"""  <section class="hero">
    <h1>{esc(a_name)} vs {esc(b_name)}: cuál elegir en 2026 (benchmark real)</h1>
    <p class="lead">Comparamos las familias <strong>{esc(a_name)}</strong> y <strong>{esc(b_name)}</strong> con datos, no opiniones:
    <strong>{tests_k} runs reales</strong> evaluados con LLM-as-Judge Phi-4 local, en los 4 pilares del emprendedor
    (coding, contenido, razonamiento, agentes) + costo y velocidad reales.</p>
    {versions_compared(a_name, b_name, A, B)}
    <p class="meta">Última actualización: {today} ·
    <a href="https://github.com/ctala/ai-benchmarks-alternativos" target="_blank" rel="noopener">datos abiertos en GitHub</a></p>
  </section>
  <section class="results">
    <div class="results-header">
      <h2>{esc(a_name)} vs {esc(b_name)}: tabla comparativa</h2>
      <p class="meta">Score por pilar /10 = <strong>calidad en esa tarea</strong> (sin ponderar costo ni velocidad). Ordenado por calidad media, no por precio.</p>
    </div>
    <div class="table-scroll"><table class="results-table">
      <thead>
        <tr><th scope="col">#</th><th scope="col">Modelo</th><th scope="col">Global</th><th scope="col">Coding</th><th scope="col">Contenido</th><th scope="col">Razon.</th><th scope="col">Agentes</th><th scope="col">$ in/out per M</th><th scope="col">Velocidad</th></tr>
      </thead>
      <tbody>
        {rows}
      </tbody>
    </table></div>
    <p class="meta">Filtrá por presupuesto, calidad mínima o tarea en la <a href="/">calculadora interactiva</a>.</p>
  </section>
  {analysis(a_name, b_name, A, B)}
  {faq(a_name, b_name, A, B)}
  <section class="cta-block">
    <h2>Probá la calculadora con tu caso real</h2>
    <p>Filtrá {esc(a_name)}, {esc(b_name)} y 100+ modelos más por presupuesto, calidad y tipo de tarea. En 30 segundos encontrás el mejor para vos.</p>
    <a href="/" class="cta-primary">Ir a la calculadora →</a>
  </section>"""
    return page_shell(cfg["title"], desc, cfg["intent_kw"], url, body)


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
