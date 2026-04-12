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
    score_tool_calling,
    score_speed,
    score_latency,
    estimate_cost,
    compute_final_score,
)
from providers.adapters import UnifiedProvider, BenchmarkResult

# Importar tests
from benchmarks.tests import content_generation, tool_calling, task_management
from benchmarks.tests import code_generation, reasoning, summarization, presentation
from benchmarks.tests import startup_content

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


def evaluate_result(result: BenchmarkResult, test: dict, model_config: dict) -> dict:
    """Evalua un resultado y calcula scores."""
    # Score de calidad
    criteria = test.get("criteria", {})
    if criteria:
        quality = score_content_quality(result.response, criteria)
    else:
        quality = 5.0 if result.success else 0.0

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
    try:
        from benchmarks.config import OPENAI_API_KEY, OPENAI_BASE_URL
        if OPENAI_API_KEY:
            openai_direct = UnifiedProvider("openai", OPENAI_API_KEY, OPENAI_BASE_URL)
    except ImportError:
        pass

    ollama = None
    if INCLUDE_OLLAMA:
        ollama = UnifiedProvider("ollama", "ollama", "http://localhost:11434/v1")

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

    for model_key, model_config in models.items():
        model_id = model_config["id"]
        model_name = model_config["name"]
        is_local = model_config.get("tier") == "local"

        # Seleccionar provider segun configuracion del modelo
        if is_local and ollama:
            provider = ollama
        elif model_config.get("provider") == "minimax_direct" and minimax_direct:
            provider = minimax_direct
        elif model_config.get("provider") == "openai_direct" and openai_direct:
            provider = openai_direct
        else:
            provider = openrouter

        print(f"\n{'─' * 70}", flush=True)
        print(f"  MODELO: {model_name} ({model_id})", flush=True)
        print(f"{'─' * 70}", flush=True)

        for suite_name, tests in test_suites.items():
            for test in tests:
                run_scores = []

                for run_num in range(runs):
                    completed += 1
                    label = f"  [{completed}/{total_runs}] {suite_name}/{test['name']}"
                    print(f"{label}...", end=" ", flush=True)

                    result = run_single_test(provider, model_id, test, REQUEST_TIMEOUT)
                    scores = evaluate_result(result, test, model_config)
                    scores["suite"] = suite_name
                    scores["run"] = run_num + 1
                    scores["timestamp"] = timestamp
                    run_scores.append(scores)

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

    print(f"\n{'=' * 70}", flush=True)
    print(f"  COMPLETADO: {completed} runs, {errors} errores", flush=True)
    print(f"{'=' * 70}", flush=True)

    # Guardar resultados
    results_dir = Path(RESULTS_DIR)
    results_dir.mkdir(parents=True, exist_ok=True)
    results_file = results_dir / f"benchmark_{timestamp}.json"
    with open(results_file, "w") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)

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
    parser.add_argument("--list-models", action="store_true", help="Listar modelos disponibles")
    parser.add_argument("--list-tests", action="store_true", help="Listar tests disponibles")

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

    run_benchmark(args)


if __name__ == "__main__":
    main()
