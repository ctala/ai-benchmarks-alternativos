#!/usr/bin/env python3
"""
Genera docs/data/models.json para la calculadora HTML en GitHub Pages.

Consolida:
- Metadata desde benchmarks/config.py (MODELS dict): tier, pricing, license, provider, notas
- Métricas desde benchmarks/results/*.json (todos los lotes): score promedio,
  tok/s, latencia, tasa de éxito por suite/pilar
- Recalcula costo con PRICING actualizado (más fiable que cost_usd guardado)

El JSON resultante se commitea con el repo y se sirve estáticamente desde
GitHub Pages en https://benchmarks.cristiantala.com/data/models.json

Uso:
    python benchmarks/export_for_pages.py
"""

import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from benchmarks.config import MODELS as _CLOUD_MODELS
from benchmarks.models import OLLAMA_MODELS, SUBSCRIPTIONS
from benchmarks.scoring import PRICING, compute_final_score, DEFAULT_WEIGHTS

# Merge cloud + local models para que DGX y otros locales aparezcan en la calculadora
MODELS = {**_CLOUD_MODELS, **OLLAMA_MODELS}


def _recalc_final(r: dict) -> float:
    """Recalcula el `final` de un run con los pesos default actuales.

    Útil cuando cambian los pesos en `scoring.py` — recalculamos sin re-correr
    los benchmarks. Usa los componentes raw guardados en cada run (quality,
    speed, latency, tool_calling, cost_usd).
    """
    q = r.get("quality")
    s = r.get("speed", 0) or 0
    lat = r.get("latency", 0) or 0
    tc = r.get("tool_calling", 0) or 0
    cost = r.get("cost_usd", 0) or 0
    if q is None:
        return r.get("final", 0) or 0
    scores = compute_final_score(q, s, lat, tc, cost)
    return scores["final"]


# Mapeo suite → pilar (mismo orden que en generate_tests_md.py)
SUITE_TO_PILLAR = {
    "reasoning": "Razonamiento",
    "deep_reasoning": "Razonamiento",
    "hallucination": "Razonamiento",
    "strategy": "Razonamiento",
    "code_generation": "Coding",
    "structured_output": "Coding",
    "string_precision": "Coding",
    "ocr_extraction": "Coding",
    "content_generation": "Contenido",
    "summarization": "Contenido",
    "presentation": "Contenido",
    "startup_content": "Contenido",
    "creativity": "Contenido",
    "news_seo_writing": "Contenido",
    "sales_outreach": "Contenido",
    "translation": "Contenido",
    "tool_calling": "Agentes",
    "task_management": "Agentes",
    "customer_support": "Agentes",
    "orchestration": "Agentes",
    "multi_turn": "Agentes",
    "policy_adherence": "Agentes",
    "agent_capabilities": "Agentes",
}


def load_all_results():
    """Carga y consolida todos los runs exitosos de benchmark JSONs.

    Agrupa por (model_id, model_name) para distinguir variantes thinking que
    comparten el mismo id base (ej. claude-opus-4.7 vs claude-opus-4.7-thinking
    ambos tienen id `anthropic/claude-opus-4-7`).
    """
    results_dir = Path(__file__).parent / "results"
    by_id = defaultdict(list)        # match por id (compat)
    by_id_and_name = defaultdict(list)  # match por (id, name) para thinking variants

    for fn in sorted(os.listdir(results_dir)):
        if not (fn.startswith("benchmark_") and fn.endswith(".json")):
            continue
        try:
            data = json.loads((results_dir / fn).read_text())
        except Exception:
            continue
        results = data if isinstance(data, list) else data.get("results", [])
        for r in results:
            if not r.get("success"):
                continue
            mid = r.get("model_id") or "?"
            mname = r.get("model") or ""
            by_id[mid].append(r)
            by_id_and_name[(mid, mname)].append(r)
    return by_id, by_id_and_name


def aggregate_metrics(runs):
    """Reduce lista de runs a métricas: score, latencia, tok/s, por pilar y por suite.

    Recalcula `final` por run con los pesos default actuales — permite cambiar
    los pesos en `scoring.py` sin re-correr benchmarks. Además expone los
    componentes promedio (quality, cost_score, speed, latency, tool_calling)
    para mostrar en tablas y permitir que la calculadora aplique pesos custom.
    """
    # Recalcular final por run con los pesos actuales (para TODOS, así by_suite
    # puede exponer también el long-context).
    for r in runs:
        if r.get("final") is None:
            continue
        r["_final_recalc"] = _recalc_final(r)

    # Long-context (niah_*) es una DIMENSIÓN APARTE, no parte del score general.
    # Decisión 2 jun 2026: las suites niah son 256K/1M ctx (~54% del conteo de
    # tests) y se midieron desigual entre modelos → distorsionaban el ranking.
    # El score general usa solo tareas prácticas (no-niah); long-context se
    # reporta por separado para quien lo necesite.
    def _is_niah(r):
        return str(r.get("suite", "")).startswith("niah")

    def _is_security(r):
        return str(r.get("suite", "")).startswith("prompt_injection")

    # General = tareas prácticas (excluye long-context y seguridad, que son
    # dimensiones separadas medidas desigual entre modelos).
    general = [r for r in runs if not _is_niah(r) and not _is_security(r)]
    niah = [r for r in runs if _is_niah(r)]
    security = [r for r in runs if _is_security(r)]

    finals_recalc = [r["_final_recalc"] for r in general if r.get("_final_recalc") is not None]

    judge_scores = [r.get("judge_score") for r in general if r.get("judge_score") is not None]
    speeds = [r.get("tokens_per_second", 0) for r in general if r.get("tokens_per_second", 0) > 0]
    latencies = [r.get("latency_total", 0) for r in general if r.get("latency_total", 0) > 0]
    in_tokens = sum(r.get("input_tokens", 0) or 0 for r in general)
    out_tokens = sum(r.get("output_tokens", 0) or 0 for r in general)

    # Componentes promedio (solo tareas prácticas, no-niah)
    qualities = [r.get("quality") for r in general if r.get("quality") is not None]
    cost_scores = [r.get("cost_score") for r in general if r.get("cost_score") is not None]
    speed_scores = [r.get("speed") for r in general if r.get("speed") is not None]
    latency_scores = [r.get("latency") for r in general if r.get("latency") is not None]
    tc_scores = [r.get("tool_calling") for r in general if r.get("tool_calling") is not None]

    # Score por pilar (general) Y por suite (incluye niah para visibilidad)
    by_pillar = defaultdict(list)
    by_suite = defaultdict(list)
    for r in runs:
        suite = r.get("suite", "")
        if not suite or r.get("_final_recalc") is None:
            continue
        by_suite[suite].append(r["_final_recalc"])
        pillar = SUITE_TO_PILLAR.get(suite)
        if pillar:
            by_pillar[pillar].append(r["_final_recalc"])
    pillars = {p: round(sum(s) / len(s), 2) for p, s in by_pillar.items() if s}
    suites = {s: round(sum(v) / len(v), 2) for s, v in by_suite.items() if v}
    scores = finals_recalc  # mantener naming downstream

    # Dimensión long-context separada (quality y final promedio de los niah)
    niah_q = [r.get("quality") for r in niah if r.get("quality") is not None]
    niah_f = [r["_final_recalc"] for r in niah if r.get("_final_recalc") is not None]

    # Long-context POR TAMAÑO DE CONTEXTO (evita comparar peras con manzanas:
    # un modelo de 64K no debe "ganarle" a uno de 1M por promediar solo contextos
    # chicos). Los errores de contexto-excedido ya están excluidos (success=False),
    # así que un tamaño sin runs exitosos = N/A, no 0.
    # IMPORTANTE: la curva por tamaño SOLO usa los needles comunes a TODOS los
    # tamaños (bridge_length, library_volumes), porque la grilla escalonada usa
    # más needles en los tramos chicos. Mezclar needles distintos por tamaño crea
    # rankings FALSOS (hallazgo 2 jun: "Gemini 3.5 peor", "zigzag DeepSeek" eran
    # artefactos del needle, no del modelo). Comparación limpia = mismos needles.
    COMMON_NEEDLES = ("bridge_length", "library_volumes")
    by_ctx = defaultdict(list)
    for r in niah:
        if r.get("quality") is None:
            continue
        tn = str(r.get("test_name", ""))
        if not any(("_" + n + "_") in tn for n in COMMON_NEEDLES):
            continue
        m = re.search(r"_(\d{3,7})_p\d", tn)
        if m:
            by_ctx[int(m.group(1))].append(r["quality"])
    long_context_by_size = {
        str(c): round(sum(v) / len(v), 2) for c, v in sorted(by_ctx.items()) if v
    }
    # "Contexto efectivo": el mayor tamaño donde el retrieval se mantiene ≥7.0.
    # Es la métrica JUSTA de capacidad long-context (premia llegar más lejos,
    # no promediar contextos fáciles).
    PASS = 7.0
    effective_ctx = None
    for c in sorted(by_ctx):
        avg = sum(by_ctx[c]) / len(by_ctx[c])
        if avg >= PASS:
            effective_ctx = c

    return {
        "runs": len(general),  # cobertura = tareas prácticas (umbral tested >=50)
        "total_runs": len(runs),  # todos los runs exitosos incluyendo niah y seguridad
        "score_global": round(sum(scores) / len(scores), 2) if scores else None,
        "score_by_pillar": pillars,
        "score_by_suite": suites,
        # Componentes raw promedio (permite mostrar columnas separadas + recalcular pesos en calculadora)
        "quality_avg": round(sum(qualities) / len(qualities), 2) if qualities else None,
        "cost_score_avg": round(sum(cost_scores) / len(cost_scores), 2) if cost_scores else None,
        "speed_score_avg": round(sum(speed_scores) / len(speed_scores), 2) if speed_scores else None,
        "latency_score_avg": round(sum(latency_scores) / len(latency_scores), 2) if latency_scores else None,
        "tool_calling_score_avg": round(sum(tc_scores) / len(tc_scores), 2) if tc_scores else None,
        "judge_score_avg": round(sum(judge_scores) / len(judge_scores), 2) if judge_scores else None,
        "tokens_per_second": round(sum(speeds) / len(speeds), 1) if speeds else None,
        "latency_avg_s": round(sum(latencies) / len(latencies), 2) if latencies else None,
        "total_input_tokens": in_tokens,
        "total_output_tokens": out_tokens,
        # --- Dimensión long-context (niah_es), separada del score general ---
        "long_context_runs": len(niah),
        "long_context_quality": round(sum(niah_q) / len(niah_q), 2) if niah_q else None,
        "long_context_score": round(sum(niah_f) / len(niah_f), 2) if niah_f else None,
        # Retrieval por tamaño de contexto + contexto efectivo (comparación justa)
        "long_context_by_size": long_context_by_size,
        "effective_context": effective_ctx,
        # --- Dimensión seguridad (prompt_injection_es: resistencia a fuga) ---
        "security_runs": len(security),
        "security_score": round(
            sum(r.get("quality") for r in security if r.get("quality") is not None)
            / max(1, sum(1 for r in security if r.get("quality") is not None)), 2
        ) if any(r.get("quality") is not None for r in security) else None,
    }


def _infer_capabilities(cfg, cfg_key):
    """Infiere flags tool_calling/thinking/multimodal del config y patrones del id.

    Permite override manual: si el cfg define el campo, lo respeta.
    Si no, infiere basado en patrones conocidos.
    """
    model_id = cfg.get("id", "").lower()
    name = cfg.get("name", "").lower()
    notes = cfg.get("notes", "").lower()
    haystack = f"{model_id} {name} {cfg_key.lower()}"

    # Thinking models (en sync con providers/adapters.py THINKING_MODELS)
    thinking_patterns = [
        "gpt-5", "o1", "o3", "glm-5", "kimi-k2.6", "kimi-k2.5",
        "nemotron", "gemini-2.5-pro", "gemini-3-pro", "gemini-3.1-pro",
        "deepseek-v4", "deepseek-r", "gemma4", "gemma-4",
        "qwen3-next-80b-a3b-thinking", "thinking",
        "magistral",  # Mistral con razonamiento
    ]
    thinking = cfg.get("thinking")
    if thinking is None:
        thinking = any(p in haystack for p in thinking_patterns)

    # Multimodal: tiene visión/audio/video además de texto
    multimodal_patterns = [
        "omni", "vision", "vl", "multimodal",
        "gemini",  # Todo Gemini es multimodal
        "gpt-4o", "gpt-5",  # GPT-4o+ multimodal
        "claude-opus", "claude-sonnet",  # Claude 3+ multimodal (vision)
        "mimo-v2.5", "mimo-v2-omni",  # MiMo Xiaomi multimodal
        "llama-4",  # Llama 4 multimodal
    ]
    multimodal = cfg.get("multimodal")
    if multimodal is None:
        multimodal = any(p in haystack for p in multimodal_patterns)

    # Tool calling: la mayoría sí, raras excepciones
    no_tool_patterns = [
        "tts", "voice", "embed", "rerank", "moderation",  # modelos especializados sin tools
        "phi-4", "phi-3",  # Phi (no soporta tool calling estándar)
        "deepseek-coder-6.7b",  # legacy sin tools
    ]
    tool_calling = cfg.get("tool_calling")
    if tool_calling is None:
        tool_calling = not any(p in haystack for p in no_tool_patterns)

    return {
        "tool_calling": bool(tool_calling),
        "thinking": bool(thinking),
        "multimodal": bool(multimodal),
    }


def build_export():
    by_id, by_id_and_name = load_all_results()
    models_export = []

    # ids usados por >1 config (variantes que comparten el mismo model id, p.ej.
    # Gemma 4 12B con/sin reasoning en llama-server) → siempre match estricto por
    # (id, name) para que cada variante reciba SOLO sus propios runs y no se fusionen.
    from collections import Counter as _Counter
    _id_counts = _Counter(c["id"] for c in MODELS.values())

    for cfg_key, cfg in MODELS.items():
        model_id = cfg["id"]
        cfg_name = cfg.get("name", cfg_key)

        # Variantes thinking (force_reasoning=True) o cualquier id compartido por
        # >1 config → matching estricto por (id, name) para no heredar/fusionar runs.
        if cfg.get("force_reasoning") or _id_counts[model_id] > 1:
            runs = by_id_and_name.get((model_id, cfg_name), [])
        else:
            # Modelos normales: match por id, excluir runs cuyo `model` name
            # contenga "(thinking)" para no contaminar al modelo base con runs
            # de la variante thinking.
            all_runs = by_id.get(model_id, [])
            runs = [r for r in all_runs if "(thinking)" not in (r.get("model") or "")]
            if not runs:
                runs = by_id.get(cfg_key, [])

        metrics = aggregate_metrics(runs) if runs else {
            "runs": 0,
            "total_runs": 0,
            "score_global": None,
            "score_by_pillar": {},
            "score_by_suite": {},
            "judge_score_avg": None,
            "tokens_per_second": None,
            "latency_avg_s": None,
            "total_input_tokens": 0,
            "total_output_tokens": 0,
        }

        # Costo por 1000 calls asumiendo 300 input + 1500 output tokens/call
        ci = cfg.get("cost_input", 0) or 0
        co = cfg.get("cost_output", 0) or 0
        cost_per_1k_calls = (300_000 * ci + 1_500_000 * co) / 1_000_000

        capabilities = _infer_capabilities(cfg, cfg_key)

        # Expandir suscripciones: las keys del cfg → info completa para el JSON
        sub_keys = cfg.get("subscriptions", []) or []
        subscriptions_expanded = [
            {
                "key": k,
                "name": SUBSCRIPTIONS[k]["name"],
                "plan": SUBSCRIPTIONS[k]["plan"],
                "price_month_usd": SUBSCRIPTIONS[k]["price_month_usd"],
                "url": SUBSCRIPTIONS[k]["url"],
                "notes": SUBSCRIPTIONS[k]["notes"],
            }
            for k in sub_keys if k in SUBSCRIPTIONS
        ]

        models_export.append({
            "key": cfg_key,
            "id": model_id,
            "name": cfg.get("name", cfg_key),
            "tier": cfg.get("tier", "?"),
            "provider": cfg.get("provider", "openrouter"),
            "open_source": cfg.get("open_source", False),
            "license": cfg.get("license", ""),
            "cost_input_per_M": ci,
            "cost_output_per_M": co,
            "cost_per_1k_calls_usd": round(cost_per_1k_calls, 3),
            "context_window": cfg.get("context_window"),
            "subscriptions": subscriptions_expanded,
            "notes": cfg.get("notes", ""),
            "tested": metrics["runs"] >= 50,  # >= 50 runs = cobertura completa
            **capabilities,  # tool_calling, thinking, multimodal
            **metrics,
        })

    # --- v2.9: score_global Z-SCOREADO ---
    # Recomputa score_global estandarizando cada dimensión (z-score) sobre los
    # modelos tested → el peso pasa a ser la influencia REAL. Antes el costo
    # dominaba de facto por su mayor varianza (1.85) vs la calidad apelotonada
    # (0.59). tool_calling sale del compuesto (no discrimina; va de badge).
    # norm_stats se guarda para que la calculadora replique el z-score client-side.
    import statistics as _st
    Z_COLS = {"quality_avg": "quality", "cost_score_avg": "cost",
              "speed_score_avg": "speed", "latency_score_avg": "latency"}
    _have = lambda m: m["tested"] and all(m.get(c) is not None for c in Z_COLS)
    _tested = [m for m in models_export if _have(m)]
    norm_stats = {}
    for col in Z_COLS:
        vals = [m[col] for m in _tested]
        mu = _st.mean(vals) if vals else 0.0
        sd = _st.pstdev(vals) if len(vals) > 1 else 1.0
        norm_stats[col] = {"mean": round(mu, 4), "std": round(sd if sd > 0 else 1.0, 4)}
    _wmap = {"quality_avg": DEFAULT_WEIGHTS["quality"], "cost_score_avg": DEFAULT_WEIGHTS["cost"],
             "speed_score_avg": DEFAULT_WEIGHTS["speed"], "latency_score_avg": DEFAULT_WEIGHTS["latency"]}
    for m in models_export:
        if not _have(m):
            continue
        z_comp = sum(w * ((m[col] - norm_stats[col]["mean"]) / norm_stats[col]["std"])
                     for col, w in _wmap.items())
        m["score_global_linear"] = m.get("score_global")  # guardar el lineal por referencia
        # rescale a 0-10: z=0 (promedio) → 5.5; pendiente 3.3 → el top (~z 0.9) ≈ 8.4,
        # spread similar al score viejo para no confundir. Solo afecta el número, no el orden.
        m["score_global"] = round(max(0.0, min(10.0, 5.5 + 3.3 * z_comp)), 2)

    # Sort: tested first, then by score desc
    models_export.sort(key=lambda m: (not m["tested"], -(m.get("score_global") or 0)))

    return {
        "generated_at": __import__("datetime").datetime.now().isoformat(timespec="seconds"),
        "total_models": len(models_export),
        "tested_count": sum(1 for m in models_export if m["tested"]),
        "tokens_per_call_assumption": {"input": 300, "output": 1500},
        "default_weights": DEFAULT_WEIGHTS,  # los pesos aplicados en score_global
        "score_method": "zscore_v2.9",  # score_global = rescale(Σ w·z(dim)); ver norm_stats
        "norm_stats": norm_stats,  # mean/std por dimensión (para replicar el z-score en la calculadora)
        "score_rescale": {"offset": 5.5, "slope": 3.3},  # display = clamp(offset + slope·z_comp, 0, 10)
        "subscriptions_catalog": SUBSCRIPTIONS,  # catálogo completo de suscripciones disponibles
        "models": models_export,
    }


def main():
    out_path = Path(__file__).parent.parent / "docs" / "data" / "models.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    export = build_export()
    out_path.write_text(json.dumps(export, indent=2, ensure_ascii=False))
    print(f"OK escrito: {out_path}")
    print(f"  Total modelos: {export['total_models']}")
    print(f"  Con cobertura (≥50 runs): {export['tested_count']}")


if __name__ == "__main__":
    main()
