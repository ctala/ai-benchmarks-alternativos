#!/usr/bin/env python3
"""
Motor principal de benchmarks.
Ejecuta todos los tests contra todos los modelos configurados via OpenRouter.

Uso:
    python benchmarks/runner.py                    # Todos los tests, todos los modelos
    python benchmarks/runner.py --models deepseek-v3 minimax-m2.7  # Solo modelos especificos
    python benchmarks/runner.py --tests tool_calling content_generation  # Solo tests especificos
    python benchmarks/runner.py --tier cheap        # Solo modelos de un tier
    python benchmarks/runner.py --quick             # 1 run por test (rapido)
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

from openai import OpenAI
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.panel import Panel

# Agregar el directorio padre al path
sys.path.insert(0, str(Path(__file__).parent.parent))

from benchmarks.scoring import (
    score_content_quality,
    score_expected_answer,
    score_tool_calling,
    score_speed,
    score_latency,
    estimate_cost,
    compute_final_score,
)
from benchmarks.llm_judge import LLMJudge, create_judge, judge_score_to_10, JUDGE_PRESETS
from providers.adapters import UnifiedProvider, OpenAIResponsesProvider, BenchmarkResult

# Importar tests
from benchmarks.tests import content_generation, tool_calling, task_management
from benchmarks.tests import code_generation, reasoning, summarization, presentation
from benchmarks.tests import startup_content, deep_reasoning, customer_support, structured_output
from benchmarks.tests import hallucination, creativity, string_precision, news_seo_writing
from benchmarks.tests import ocr_extraction, orchestration, multi_turn, policy_adherence
from benchmarks.tests import agent_capabilities, strategy, sales_outreach, translation

console = Console()

ALL_TEST_SUITES = {
    "content_generation": content_generation.TESTS,
    "tool_calling": tool_calling.TESTS,
    "task_management": task_management.TESTS,
    "code_generation": code_generation.TESTS,
    "reasoning": reasoning.TESTS,
    "summarization": summarization.TESTS,
    "presentation": presentation.TESTS,
    "startup_content": startup_content.TESTS,
    "deep_reasoning": deep_reasoning.TESTS,
    "customer_support": customer_support.TESTS,
    "structured_output": structured_output.TESTS,
    "hallucination": hallucination.TESTS,
    "creativity": creativity.TESTS,
    "string_precision": string_precision.TESTS,
    "news_seo_writing": news_seo_writing.TESTS,
    "ocr_extraction": ocr_extraction.TESTS,
    "orchestration": orchestration.TESTS,
    "multi_turn": multi_turn.TESTS,
    "policy_adherence": policy_adherence.TESTS,
    "agent_capabilities": agent_capabilities.TESTS,
    "strategy": strategy.TESTS,
    "sales_outreach": sales_outreach.TESTS,
    "translation": translation.TESTS,
}


def load_config():
    """Carga la configuracion. Primero intenta config.py, si no existe usa env vars."""
    try:
        from benchmarks import config
        return config
    except ImportError:
        console.print("[yellow]No se encontro benchmarks/config.py[/yellow]")
        api_key = os.environ.get("OPENROUTER_API_KEY")
        if not api_key:
            console.print("[red]Configura OPENROUTER_API_KEY o copia config.example.py a config.py[/red]")
            sys.exit(1)

        # Crear config minima desde env
        class EnvConfig:
            OPENROUTER_API_KEY = api_key
            RUNS_PER_TEST = 3
            REQUEST_TIMEOUT = 120
            RESULTS_DIR = "benchmarks/results"
            INCLUDE_OLLAMA = False

        # Importar modelos del ejemplo
        from benchmarks.config_example_loader import MODELS
        EnvConfig.MODELS = MODELS
        return EnvConfig


def run_single_test(
    provider: UnifiedProvider,
    model_id: str,
    test: dict,
    timeout: int = 120,
) -> BenchmarkResult:
    """Ejecuta un solo test contra un modelo."""
    tools = test.get("tools")
    result = provider.chat(
        model=model_id,
        messages=test["messages"],
        tools=tools,
        temperature=0.7,
        max_tokens=2048,
        timeout=timeout,
    )
    result.test_name = test["name"]
    return result



def evaluate_result(result: BenchmarkResult, test: dict, model_config: dict,
                    judge: LLMJudge = None, suite_name: str = "") -> dict:
    """Evalua un resultado y calcula scores.

    Si hay LLM judge disponible, combina:
    - 30% score automatico (formato + expected_answer)
    - 70% score del juez LLM
    Sin juez, usa solo score automatico con 40/60 formato/sustancia.
    """
    expected_answer = test.get("expected_answer", {})
    answer_type = expected_answer.get("type", "")

    # Score base de contenido (automatico)
    criteria = test.get("criteria", {})
    if criteria:
        content_score = score_content_quality(result.response, criteria)
    else:
        content_score = 5.0 if result.success else 0.0

    # Score de expected_answer (sustancia automatica)
    if expected_answer and answer_type:
        answer_score = score_expected_answer(result.response, expected_answer)
        auto_quality = content_score * 0.4 + answer_score * 0.6
    else:
        auto_quality = content_score

    # LLM-as-Judge (si esta habilitado)
    judge_result = None
    judge_quality = -1.0
    if judge and result.success and result.response:
        judge_result = judge.evaluate(result.response, test, suite_name)
        judge_quality = judge_score_to_10(judge_result)

    # Combinar scores
    if judge_quality >= 0:
        # Con juez: 30% automatico + 70% juez
        quality = auto_quality * 0.3 + judge_quality * 0.7
    else:
        quality = auto_quality

    # Score de tool calling
    expected_tools = test.get("expected_tools", None)
    if expected_tools is not None:
        tc_score = score_tool_calling(result, expected_tools)
    else:
        tc_score = 7.0  # N/A, puntaje neutral

    # Speed y latency
    speed = score_speed(result.tokens_per_second)
    latency = score_latency(result.latency_first_token)

    # Costo
    cost = estimate_cost(model_config["id"], result.input_tokens, result.output_tokens)

    # Score final
    scores = compute_final_score(quality, speed, latency, tc_score, cost)
    scores["test_name"] = test["name"]
    scores["model"] = model_config["name"]
    scores["model_id"] = model_config["id"]
    scores["success"] = result.success
    scores["error"] = result.error
    scores["tokens_per_second"] = round(result.tokens_per_second, 1)
    scores["latency_first_token"] = round(result.latency_first_token, 3)
    scores["latency_total"] = round(result.latency_total, 3)
    scores["input_tokens"] = result.input_tokens
    scores["output_tokens"] = result.output_tokens
    scores["response_preview"] = result.response[:300] if result.response else ""
    scores["auto_quality"] = round(auto_quality, 2)

    # Guardar datos del juez si disponible
    if judge_result and judge_quality >= 0:
        scores["judge_score"] = judge_result.get("score_final", -1)
        scores["judge_precision"] = judge_result.get("precision", 0)
        scores["judge_relevancia"] = judge_result.get("relevancia", 0)
        scores["judge_profundidad"] = judge_result.get("profundidad", 0)
        scores["judge_claridad"] = judge_result.get("claridad", 0)
        scores["judge_utilidad"] = judge_result.get("utilidad", 0)
        scores["judge_justificacion"] = judge_result.get("justificacion", "")

    return scores


def run_benchmark(args):
    """Ejecuta el benchmark completo."""
    try:
        from benchmarks.config import OPENROUTER_API_KEY, MODELS, RUNS_PER_TEST, REQUEST_TIMEOUT, RESULTS_DIR, INCLUDE_OLLAMA
    except ImportError:
        console.print("[red]Copia benchmarks/config.example.py a benchmarks/config.py y agrega tu API key[/red]")
        sys.exit(1)

    # Filtrar modelos
    models = dict(MODELS)
    if INCLUDE_OLLAMA:
        try:
            from benchmarks.config import OLLAMA_MODELS
            models.update(OLLAMA_MODELS)
        except ImportError:
            pass

    if args.models:
        models = {k: v for k, v in models.items() if k in args.models}
    if args.tier:
        models = {k: v for k, v in models.items() if v.get("tier") == args.tier}

    if not models:
        console.print("[red]No hay modelos seleccionados[/red]")
        sys.exit(1)

    # Filtrar tests
    test_suites = dict(ALL_TEST_SUITES)
    if args.tests:
        test_suites = {k: v for k, v in test_suites.items() if k in args.tests}

    runs = 1 if args.quick else RUNS_PER_TEST

    # Setup providers
    openrouter = UnifiedProvider("openrouter", OPENROUTER_API_KEY, "https://openrouter.ai/api/v1")

    # MiniMax directa (para modelos highspeed)
    minimax_direct = None
    try:
        from benchmarks.config import MINIMAX_API_KEY, MINIMAX_BASE_URL
        if MINIMAX_API_KEY:
            minimax_direct = UnifiedProvider("minimax", MINIMAX_API_KEY, MINIMAX_BASE_URL)
    except ImportError:
        pass

    # OpenAI directo (para GPT-5.4, GPT-5.4-mini)
    openai_direct = None
    # OpenAI Responses API (para gpt-5.5-pro, o1-pro — endpoint /v1/responses)
    openai_responses = None
    try:
        from benchmarks.config import OPENAI_API_KEY, OPENAI_BASE_URL
        if OPENAI_API_KEY:
            openai_direct = UnifiedProvider("openai", OPENAI_API_KEY, OPENAI_BASE_URL)
            openai_responses = OpenAIResponsesProvider("openai_responses", OPENAI_API_KEY, OPENAI_BASE_URL)
    except ImportError:
        pass

    ollama = None
    if INCLUDE_OLLAMA:
        # OLLAMA_BASE_URL puede apuntar a localhost o a una DGX/server remoto
        # (ej. http://192.168.88.190:11434/v1 para DGX Spark via LAN)
        ollama_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")
        ollama = UnifiedProvider("ollama", "ollama", ollama_url)

    # Ollama Cloud (requiere suscripción y API key en OLLAMA_CLOUD_API_KEY)
    ollama_cloud = None
    try:
        from benchmarks.config import OLLAMA_CLOUD_API_KEY
        OLLAMA_CLOUD_BASE_URL = "https://ollama.com/v1"
        try:
            from benchmarks.config import OLLAMA_CLOUD_BASE_URL as _url_override
            OLLAMA_CLOUD_BASE_URL = _url_override
        except ImportError:
            pass
        if OLLAMA_CLOUD_API_KEY:
            ollama_cloud = UnifiedProvider("ollama_cloud", OLLAMA_CLOUD_API_KEY, OLLAMA_CLOUD_BASE_URL)
    except ImportError:
        pass

    # Groq directo (LPU, super rápido, OpenAI-compatible)
    groq_direct = None
    try:
        from benchmarks.config import GROQ_API_KEY, GROQ_BASE_URL
        if GROQ_API_KEY:
            groq_direct = UnifiedProvider("groq", GROQ_API_KEY, GROQ_BASE_URL)
    except ImportError:
        pass

    # NVIDIA NIM (catálogo de 100+ modelos, gratis con 40 RPM — ideal para benchmarks)
    nvidia_nim = None
    try:
        from benchmarks.config import NVIDIA_NIM_API_KEY, NVIDIA_NIM_BASE_URL
        if NVIDIA_NIM_API_KEY:
            nvidia_nim = UnifiedProvider("nvidia_nim", NVIDIA_NIM_API_KEY, NVIDIA_NIM_BASE_URL)
    except ImportError:
        pass

    # NVIDIA NIM Local — containers NIM corriendo en hardware propio (DGX Spark,
    # GPU server). OpenAI-compatible. No requiere API key real (string dummy).
    # Setup: Docker pull nvcr.io/nim/<vendor>/<model> + run con --gpus all.
    # Cada modelo escucha en su propio puerto (default 8000). Para multiples
    # modelos usar puertos distintos y NIM_LOCAL_BASE_URL apunta a uno o un
    # router (LiteLLM, OpenRouter local, etc).
    nim_local = None
    try:
        from benchmarks.config import NIM_LOCAL_BASE_URL
        if NIM_LOCAL_BASE_URL:
            # Key dummy: NIM local no la valida, pero el SDK la requiere
            nim_local = UnifiedProvider("nim_local", "nim-local-no-auth", NIM_LOCAL_BASE_URL)
    except ImportError:
        pass

    # Xiaomi MiMo Token Plan (suscripción mensual con 8 modelos: V2.5-Pro, V2.5, V2-Pro,
    # V2-Omni, TTS variantes. OpenAI-compatible. 1 token = 1 credit en V2.5, 2 credits
    # en V2.5-Pro. Off-peak 16-24 UTC = 0.8x consumption)
    xiaomi_direct = None
    try:
        from benchmarks.config import XIAOMI_API_KEY
        XIAOMI_BASE_URL = "https://token-plan-sgp.xiaomimimo.com/v1"
        try:
            from benchmarks.config import XIAOMI_BASE_URL as _xiaomi_url_override
            XIAOMI_BASE_URL = _xiaomi_url_override
        except ImportError:
            pass
        if XIAOMI_API_KEY:
            xiaomi_direct = UnifiedProvider("xiaomi", XIAOMI_API_KEY, XIAOMI_BASE_URL)
    except ImportError:
        pass

    # LLM-as-Judge (opcional)
    # Prioridad: 1) modelo especificado, 2) Ollama local (Gemma 4), 3) Haiku via OpenRouter
    judge = None
    if args.judge:
        try:
            judge = create_judge(
                api_key=OPENROUTER_API_KEY,
                judge_model=args.judge_model,
                prefer_local=True,
            )
            local_tag = " (LOCAL)" if judge.is_local else f" (API, ~${0.07:.2f}/modelo)"
            print(f"  LLM-as-Judge: {judge.judge_model}{local_tag}", flush=True)
        except ValueError as e:
            print(f"  [WARN] No se pudo crear juez: {e}", flush=True)
            print(f"  Continuando sin LLM-as-Judge...", flush=True)

    # Conteo total
    total_tests = sum(len(tests) for tests in test_suites.values())
    total_runs = total_tests * len(models) * runs

    print(f"=" * 70, flush=True)
    print(f"  BENCHMARK DE MODELOS AI", flush=True)
    print(f"  Modelos: {len(models)} | Suites: {len(test_suites)} | Tests: {total_tests} | Runs totales: {total_runs}", flush=True)
    print(f"  Timeout por request: {REQUEST_TIMEOUT}s", flush=True)
    print(f"=" * 70, flush=True)

    all_results = []
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    completed = 0
    errors = 0
    benchmark_start = time.time()
    # Ventana móvil de los últimos N tests para estimar ETA
    recent_test_seconds: list[float] = []

    def _fmt_duration(secs: float) -> str:
        if secs < 60:
            return f"{secs:.0f}s"
        if secs < 3600:
            return f"{secs // 60:.0f}m{secs % 60:.0f}s"
        h = secs // 3600
        m = (secs % 3600) // 60
        return f"{h:.0f}h{m:02.0f}m"

    def _short_name(name: str, max_len: int = 28) -> str:
        return name if len(name) <= max_len else name[: max_len - 1] + "…"

    # Setup del archivo de resultados para guardado incremental
    results_dir = Path(RESULTS_DIR)
    results_dir.mkdir(parents=True, exist_ok=True)
    results_file = results_dir / f"benchmark_{timestamp}.json"

    # --resume: cargar resultados previos y saltear tests ya completados
    done_keys: set[tuple[str, str, str]] = set()
    if getattr(args, "resume", None):
        resume_path = Path(args.resume)
        if not resume_path.exists():
            console.print(f"[red]--resume: archivo no existe: {resume_path}[/red]")
            sys.exit(1)
        with open(resume_path) as f:
            prev = json.load(f)
        prev_results = prev.get("results", [])
        prev_meta = prev.get("metadata", {})
        timestamp = prev_meta.get("timestamp", timestamp)
        results_file = resume_path  # sobreescribe el mismo archivo

        # --rerun-empty: descartar runs con response_preview vacío
        # --rerun-failed: descartar runs con success=False (timeouts, errores)
        # Sólo afectan a los modelos que entran en este run (filtrado por --models si aplica)
        rerun_empty = getattr(args, "rerun_empty", False)
        rerun_failed = getattr(args, "rerun_failed", False)
        if rerun_empty or rerun_failed:
            target_model_ids = {m["id"] for m in models.values()}
            def keep(r):
                # Mantener si: (a) está fuera del target, o (b) cumple las condiciones
                in_target = r.get("model_id", "") in target_model_ids
                if not in_target:
                    return True
                if rerun_empty and not r.get("response_preview", ""):
                    return False  # vacío en target → re-correr
                if rerun_failed and not r.get("success", False):
                    return False  # failed en target → re-correr
                return True
            kept = [r for r in prev_results if keep(r)]
            dropped = len(prev_results) - len(kept)
            all_results = kept
            flags_msg = []
            if rerun_empty: flags_msg.append("vacíos")
            if rerun_failed: flags_msg.append("failed")
            console.print(f"[yellow]--rerun-{'/'.join(flags_msg)}: {dropped} runs descartados de los modelos seleccionados[/yellow]")
        else:
            all_results = prev_results

        completed = prev_meta.get("total_runs", len(all_results))
        # Recontar errores actuales (los que siguen en all_results)
        errors = sum(1 for r in all_results if not r.get("success", False))
        for r in all_results:
            done_keys.add((r.get("model_id", ""), r.get("suite", ""), r.get("test_name", "")))
        console.print(f"[cyan]--resume: {len(all_results)} tests ya completados cargados de {resume_path.name}[/cyan]")

    def _dump_results(partial: bool):
        """Vuelca resultados al JSON. Se llama tras cada modelo y al final."""
        output = {
            "metadata": {
                "timestamp": timestamp,
                "total_runs": completed,
                "errors": errors,
                "judge": judge.get_stats() if judge else None,
                "partial": partial,
            },
            "results": all_results,
        }
        with open(results_file, "w") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)

    # Directorio para respuestas completas (output auditable por test)
    responses_dir = results_dir / "responses" / timestamp
    responses_dir.mkdir(parents=True, exist_ok=True)

    def _safe_slug(s: str) -> str:
        return "".join(c if c.isalnum() or c in "-_." else "_" for c in s)[:80]

    def _save_response(result, scores, model_key, suite, test_name):
        """Guarda la respuesta completa del modelo en un archivo .md auditable."""
        if not getattr(result, "response", None):
            return
        fname = f"{_safe_slug(model_key)}__{_safe_slug(suite)}__{_safe_slug(test_name)}.md"
        path = responses_dir / fname
        header = [
            f"# {scores.get('model','?')} — {suite}/{test_name}",
            "",
            f"- model_id: `{scores.get('model_id','?')}`",
            f"- success: {scores.get('success')}  | final: {scores.get('final')} | quality: {scores.get('quality')}",
            f"- latency_total: {scores.get('latency_total')}s | tokens_per_second: {scores.get('tokens_per_second')}",
            f"- input_tokens: {scores.get('input_tokens')} | output_tokens: {scores.get('output_tokens')}",
        ]
        if scores.get("judge_score", -1) >= 0:
            header.append(f"- judge_score: {scores.get('judge_score')} | justificación: {scores.get('judge_justificacion','')}")
        if scores.get("error"):
            header.append(f"- error: {scores.get('error')}")
        header += ["", "## Respuesta completa", "", result.response]
        # Garantizar que el directorio existe (defensa contra race conditions
        # o cwd inesperados — el primer mkdir en linea 436 puede no alcanzar
        # si el script se ejecuta desde fuera de la raiz del repo)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            f.write("\n".join(header))
        scores["response_file"] = str(path.relative_to(results_dir.parent))

    # Progreso local por modelo: tests totales de este modelo
    tests_per_model = sum(len(t) for t in test_suites.values())

    for model_idx, (model_key, model_config) in enumerate(models.items(), 1):
        model_id = model_config["id"]
        model_name = model_config["name"]
        short_model = _short_name(model_name)
        is_local = model_config.get("tier") == "local"

        # Seleccionar provider segun configuracion del modelo
        if is_local and ollama:
            provider = ollama
        elif model_config.get("provider") == "ollama_cloud" and ollama_cloud:
            provider = ollama_cloud
        elif model_config.get("provider") == "groq_direct" and groq_direct:
            provider = groq_direct
        elif model_config.get("provider") == "minimax_direct" and minimax_direct:
            provider = minimax_direct
        elif model_config.get("provider") == "openai_direct" and openai_direct:
            provider = openai_direct
        elif model_config.get("provider") == "openai_responses" and openai_responses:
            provider = openai_responses
        elif model_config.get("provider") == "nvidia_nim" and nvidia_nim:
            provider = nvidia_nim
        elif model_config.get("provider") == "xiaomi_direct" and xiaomi_direct:
            provider = xiaomi_direct
        elif model_config.get("provider") == "nim_local" and nim_local:
            provider = nim_local
        else:
            provider = openrouter

        print(f"\n{'─' * 70}", flush=True)
        print(f"  MODELO [{model_idx}/{len(models)}]: {model_name} ({model_id})", flush=True)
        print(f"{'─' * 70}", flush=True)

        local_completed = 0  # contador local por modelo

        for suite_name, tests in test_suites.items():
            for test in tests:
                local_completed += 1
                test_desc = test.get("description", "")
                test_desc_short = _short_name(test_desc, 40) if test_desc else ""

                # Skip si ya fue completado (resume)
                if (model_id, suite_name, test["name"]) in done_keys:
                    completed += 1
                    print(f"  [{completed}/{total_runs}] {short_model} ({local_completed}/{tests_per_model}) | "
                          f"{suite_name}/{test['name']}... SKIP (resume)", flush=True)
                    continue

                run_scores = []

                for run_num in range(runs):
                    completed += 1
                    t_start = time.time()
                    # ETA basado en promedio móvil de los últimos ~20 tests
                    window = recent_test_seconds[-20:]
                    if window:
                        avg_s = sum(window) / len(window)
                        eta_secs = avg_s * (total_runs - completed + 1)
                        eta_str = _fmt_duration(eta_secs)
                    else:
                        eta_str = "?"
                    elapsed_str = _fmt_duration(time.time() - benchmark_start)

                    label = (f"  [{completed}/{total_runs}] {short_model} ({local_completed}/{tests_per_model}) | "
                             f"{suite_name}/{test['name']}")
                    if test_desc_short:
                        label += f" — {test_desc_short}"
                    label += f" [elapsed {elapsed_str} | eta {eta_str}]"
                    print(f"{label}...", end=" ", flush=True)

                    result = run_single_test(provider, model_id, test, REQUEST_TIMEOUT)
                    scores = evaluate_result(result, test, model_config, judge=judge, suite_name=suite_name)
                    scores["suite"] = suite_name
                    scores["run"] = run_num + 1
                    scores["timestamp"] = timestamp
                    _save_response(result, scores, model_key, suite_name, test["name"])
                    run_scores.append(scores)

                    # Registrar duración real en ventana móvil
                    recent_test_seconds.append(time.time() - t_start)

                    if result.success:
                        tps = f"{result.tokens_per_second:.0f} tok/s" if result.tokens_per_second else "?"
                        print(f"OK ({result.latency_total:.1f}s, {tps}, score:{scores['final']:.1f})", flush=True)
                    else:
                        errors += 1
                        err_short = result.error[:60] if result.error else "unknown"
                        print(f"ERROR ({result.latency_total:.1f}s) {err_short}", flush=True)

                    # Pausa entre requests para no saturar rate limits
                    if not is_local:
                        time.sleep(0.5)

                # Promediar runs
                if len(run_scores) > 1:
                    avg_scores = average_scores(run_scores)
                    all_results.append(avg_scores)
                else:
                    all_results.append(run_scores[0])

                # Checkpoint incremental tras cada test (silencioso para no ruidar el log)
                _dump_results(partial=True)

        # Checkpoint visible al cerrar cada modelo
        print(f"  [checkpoint] {len(all_results)} resultados guardados en {results_file.name}", flush=True)

    print(f"\n{'=' * 70}", flush=True)
    print(f"  COMPLETADO: {completed} runs, {errors} errores", flush=True)
    if judge:
        stats = judge.get_stats()
        print(f"  LLM-as-Judge: {stats['evaluations']} evaluaciones, costo ~${stats['estimated_cost_usd']:.4f}", flush=True)
    print(f"{'=' * 70}", flush=True)

    # Guardar resultados (final, marca partial=False)
    _dump_results(partial=False)

    console.print(f"\n[green]Resultados guardados en {results_file}[/green]")

    # Mostrar tabla de resultados
    display_results(all_results)

    return all_results


def average_scores(scores_list: list[dict]) -> dict:
    """Promedia los scores de multiples runs."""
    avg = dict(scores_list[0])  # Copiar estructura
    numeric_keys = [
        "quality", "cost_score", "cost_usd", "speed", "latency",
        "tool_calling", "final", "tokens_per_second",
        "latency_first_token", "latency_total",
    ]
    for key in numeric_keys:
        values = [s[key] for s in scores_list if key in s]
        if values:
            avg[key] = round(sum(values) / len(values), 3)

    avg["runs_averaged"] = len(scores_list)
    avg["success"] = all(s.get("success", False) for s in scores_list)
    return avg


def display_results(results: list[dict]):
    """Muestra los resultados en una tabla bonita."""
    # Agrupar por modelo
    model_scores = {}
    for r in results:
        model = r["model"]
        if model not in model_scores:
            model_scores[model] = []
        model_scores[model].append(r)

    # Tabla resumen
    table = Table(title="Resultados del Benchmark", show_lines=True)
    table.add_column("Modelo", style="cyan", no_wrap=True)
    table.add_column("Final", style="bold green", justify="right")
    table.add_column("Calidad", justify="right")
    table.add_column("Tool Call", justify="right")
    table.add_column("Velocidad", justify="right")
    table.add_column("Latencia", justify="right")
    table.add_column("Costo", justify="right")
    table.add_column("tok/s", justify="right")
    table.add_column("Costo/call", justify="right")
    table.add_column("Exitos", justify="right")

    ranked = []
    for model, scores in model_scores.items():
        avg_final = sum(s["final"] for s in scores) / len(scores)
        avg_quality = sum(s["quality"] for s in scores) / len(scores)
        avg_tc = sum(s["tool_calling"] for s in scores) / len(scores)
        avg_speed = sum(s["speed"] for s in scores) / len(scores)
        avg_lat = sum(s["latency"] for s in scores) / len(scores)
        avg_cost = sum(s["cost_score"] for s in scores) / len(scores)
        avg_tps = sum(s["tokens_per_second"] for s in scores) / len(scores)
        avg_cost_usd = sum(s["cost_usd"] for s in scores) / len(scores)
        success_rate = sum(1 for s in scores if s["success"]) / len(scores) * 100

        ranked.append((model, avg_final, avg_quality, avg_tc, avg_speed, avg_lat,
                       avg_cost, avg_tps, avg_cost_usd, success_rate))

    ranked.sort(key=lambda x: x[1], reverse=True)

    for i, (model, final, quality, tc, speed, lat, cost, tps, cost_usd, success) in enumerate(ranked):
        medal = "🥇 " if i == 0 else "🥈 " if i == 1 else "🥉 " if i == 2 else "   "
        table.add_row(
            f"{medal}{model}",
            f"{final:.2f}",
            f"{quality:.1f}",
            f"{tc:.1f}",
            f"{speed:.1f}",
            f"{lat:.1f}",
            f"{cost:.1f}",
            f"{tps:.0f}",
            f"${cost_usd:.4f}",
            f"{success:.0f}%",
        )

    console.print()
    console.print(table)

    # Tabla por test suite
    console.print()
    suite_table = Table(title="Detalle por Categoria", show_lines=True)
    suite_table.add_column("Categoria", style="cyan")
    suite_table.add_column("Mejor Modelo", style="green")
    suite_table.add_column("Score", justify="right")
    suite_table.add_column("2do Mejor", style="yellow")
    suite_table.add_column("Score", justify="right")

    suites = {}
    for r in results:
        suite = r["suite"]
        model = r["model"]
        if suite not in suites:
            suites[suite] = {}
        if model not in suites[suite]:
            suites[suite][model] = []
        suites[suite][model].append(r["final"])

    for suite, models in suites.items():
        avg_by_model = [(m, sum(s)/len(s)) for m, s in models.items()]
        avg_by_model.sort(key=lambda x: x[1], reverse=True)
        best = avg_by_model[0] if avg_by_model else ("N/A", 0)
        second = avg_by_model[1] if len(avg_by_model) > 1 else ("N/A", 0)
        suite_table.add_row(suite, best[0], f"{best[1]:.2f}", second[0], f"{second[1]:.2f}")

    console.print(suite_table)


def main():
    parser = argparse.ArgumentParser(description="Benchmark de modelos AI via OpenRouter")
    parser.add_argument("--models", nargs="+", help="Modelos especificos a evaluar (keys del config)")
    parser.add_argument("--tests", nargs="+", help="Test suites a ejecutar",
                       choices=list(ALL_TEST_SUITES.keys()))
    parser.add_argument("--tier", help="Solo modelos de un tier",
                       choices=["free", "ultra_cheap", "cheap", "medium", "premium", "local"])
    parser.add_argument("--quick", action="store_true", help="1 run por test (rapido)")
    parser.add_argument("--judge", action="store_true",
                       help="Usar LLM-as-Judge (Gemma 4 local si Ollama disponible, sino Claude Haiku)")
    parser.add_argument("--judge-model", type=str, default=None,
                       help="Preset (gemma4, glm4, qwen3.5, haiku, gemini-flash) o model ID directo")
    parser.add_argument("--list-judges", action="store_true", help="Listar jueces disponibles")
    parser.add_argument("--list-models", action="store_true", help="Listar modelos disponibles")
    parser.add_argument("--list-tests", action="store_true", help="Listar tests disponibles")
    parser.add_argument("--resume", type=str, default=None,
                       help="Path a un benchmark_*.json previo: carga resultados y saltea tests ya completados (mismo archivo se sobreescribe)")
    parser.add_argument("--rerun-empty", action="store_true",
                       help="Con --resume: re-correr los tests que tienen response_preview vacío (típicamente thinking models que agotaron max_tokens en reasoning)")
    parser.add_argument("--rerun-failed", action="store_true",
                       help="Con --resume: re-correr los tests que fallaron (timeouts, errores 4xx/5xx). Compatible con --rerun-empty.")

    args = parser.parse_args()

    if args.list_models:
        try:
            from benchmarks.config import MODELS
            console.print("[bold]Modelos configurados:[/bold]")
            for key, m in MODELS.items():
                console.print(f"  {key}: {m['name']} ({m['id']}) - tier: {m['tier']}")
        except ImportError:
            console.print("[red]Copia config.example.py a config.py primero[/red]")
        return

    if args.list_tests:
        console.print("[bold]Test suites disponibles:[/bold]")
        for suite, tests in ALL_TEST_SUITES.items():
            console.print(f"\n  [cyan]{suite}[/cyan] ({len(tests)} tests):")
            for t in tests:
                console.print(f"    - {t['name']}: {t['description']}")
        return

    if args.list_judges:
        from benchmarks.llm_judge import _check_ollama_available
        ollama_ok = _check_ollama_available()
        console.print("[bold]Modelos juez disponibles:[/bold]\n")
        for name, preset in JUDGE_PRESETS.items():
            local = preset["provider"] == "ollama"
            status = "[green]disponible[/green]" if (local and ollama_ok) or not local else "[red]Ollama no detectado[/red]"
            console.print(f"  [cyan]{name}[/cyan]: {preset['description']}")
            console.print(f"    Modelo: {preset['model']} | Estado: {status}")
        console.print(f"\n  Ollama: {'[green]corriendo[/green]' if ollama_ok else '[yellow]no detectado[/yellow]'}")
        console.print("\n  Uso: --judge --judge-model gemma4")
        console.print("  Tambien acepta model IDs: --judge-model google/gemini-2.5-flash")
        return

    run_benchmark(args)


if __name__ == "__main__":
    main()
