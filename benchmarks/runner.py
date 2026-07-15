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
from providers.adapters import UnifiedProvider, OpenAIResponsesProvider, ClaudeCodeProvider, DiffusionGemmaProvider, BenchmarkResult

# Importar tests
from benchmarks.tests import content_generation, tool_calling, task_management
from benchmarks.tests import code_generation, reasoning, summarization, presentation
from benchmarks.tests import startup_content, deep_reasoning, customer_support, structured_output
from benchmarks.tests import hallucination, creativity, string_precision, news_seo_writing
from benchmarks.tests import ocr_extraction, orchestration, multi_turn, policy_adherence
from benchmarks.tests import agent_capabilities, strategy, sales_outreach, translation
# Suite nueva (jul-2026): tareas de negocio REALES con trampas objetivas plantadas.
# Existe porque el juez comprime en tareas faciles (content_generation: media 4.73/5,
# std 0.25 -> no distingue un 8B de Opus). Las de aca se pueden fallar de forma
# verificable: o cazas el error aritmetico / la causalidad falsa, o no.
from benchmarks.tests import business_audit
# Suite nueva (jul-2026): PLANIFICAR un negocio, no auditarlo. Auditar es verificar
# (hay una respuesta correcta escondida); planificar es generar (no la hay). Se mide
# la VALIDEZ del plan, no su belleza: restricciones respetadas, aritmetica que cierra,
# activos que existen de verdad, y si propone como MATAR la idea o solo como construirla.
from benchmarks.tests import business_strategy
# Suite nueva (jul-2026): generación de contenido que se PUEDE FALLAR.
# content_generation pedía "escribe un blog post sobre las ventajas de la IA": no hay
# forma de equivocarse, y los datos lo confirman (media 9.37/10, desv 0.70 — no distingue
# un 8B de Opus). Acá el brief trae una trampa verificable: un dato falso plantado, una
# restricción enterrada, dos fuentes que se contradicen, una audiencia que ya sabe, un CTA
# prohibido. Un modelo que escribe precioso y cae en cualquiera te hace publicar basura
# con confianza — que es justo lo que el juez LLM no ve, porque el texto PARECE bueno.
from benchmarks.tests import content_verificable
from benchmarks.tests import agent_long_horizon
from benchmarks.tests import niah_es
from benchmarks.tests import niah_es_1m
from benchmarks.tests import niah_es_lite
from benchmarks.tests import prompt_injection_es

console = Console()

# Redacción de secretos en artefactos auditables (responses .md + JSON).
# Los modelos a veces alucinan webhooks de Slack o claves en tests de
# orquestación/n8n; GitHub push-protection los bloquea. Redactamos al guardar
# para que el repo público quede limpio sin perder el valor de la respuesta.
import re as _re
_SECRET_PATTERNS = [
    (_re.compile(r'https://hooks\.slack\.com/services/[A-Za-z0-9/_+=-]+'),
     'https://hooks.slack.com/services/REDACTED'),
    (_re.compile(r'https://discord(?:app)?\.com/api/webhooks/[A-Za-z0-9/_-]+'),
     'https://discord.com/api/webhooks/REDACTED'),
    (_re.compile(r'sk-(?:or-v1|proj|cp|ant)-[A-Za-z0-9_-]{8,}'), 'REDACTED-SECRET'),
    (_re.compile(r'xox[baprs]-[A-Za-z0-9-]{10,}'), 'REDACTED-SLACK-TOKEN'),
]

def _redact_secrets(text):
    if not text or not isinstance(text, str):
        return text
    for pat, repl in _SECRET_PATTERNS:
        text = pat.sub(repl, text)
    return text

ALL_TEST_SUITES = {
    "business_audit": business_audit.TESTS,
    "business_strategy": business_strategy.TESTS,
    "content_verificable": content_verificable.TESTS,
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
    "agent_long_horizon": agent_long_horizon.TESTS,
    "niah_es": niah_es.TESTS,
    # niah_es_1m / niah_es_lite superseded por el grid escalonado de niah_es v3
    # (8K-1M con skip por context window). Imports conservados por compat.
    "prompt_injection_es": prompt_injection_es.TESTS,
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
    model_config: dict | None = None,
) -> BenchmarkResult:
    """Ejecuta un solo test contra un modelo.

    Si model_config tiene force_reasoning=True (modelos hybrid como Hermes 4,
    Kimi K2.5), el adapter activa reasoning vía OpenRouter extra_body.
    """
    tools = test.get("tools")

    # NO PODER HACER UN TEST **ES** EL RESULTADO.
    #
    # Hermes 4 (70B y 405B) no soportan tool calling en OpenRouter: los tests que exigen
    # herramientas devuelven "No endpoints found". Eso se contaba como ERROR, el examen
    # quedaba incompleto, y el modelo salía del ranking marcado «en evaluación».
    #
    # Pero no está pendiente de medir: ya sabemos el resultado. Un modelo que no puede
    # llamar herramientas NO PUEDE hacer trabajo de agente. Marcarlo "no rendido" esconde
    # exactamente lo que el lector necesita saber.
    #
    # Ahora saca 0 en esos tests, con la razón anotada. Es la verdad, y compite con ella.
    if tools and (model_config or {}).get("sin_tools"):
        r = BenchmarkResult(
            provider="capability-gap", model=model_id, test_name=test["name"],
            prompt=(test["messages"][-1].get("content", "") or "")[:200],
        )
        r.success = True
        r.response = ""
        r.metadata = {"capability_gap": "el modelo no soporta tool calling"}
        return r

    force_reasoning = bool((model_config or {}).get("force_reasoning", False))
    result = provider.chat(
        model=model_id,
        messages=test["messages"],
        tools=tools,
        temperature=0.7,
        max_tokens=2048,
        timeout=timeout,
        force_reasoning=force_reasoning,
    )
    result.test_name = test["name"]
    # Una respuesta VACÍA nunca pasa de largo. Hay DOS casos y hay que distinguirlos:
    #
    # (a) HIPO transitorio (provider, thinking sin budget): reintentar lo resuelve.
    #     Así Fable 5 publicó un examen inválido (22/143 vacíos con success=True) y 29
    #     vacíos de 7 modelos rankeados vivían en los promedios (14/15-jul-2026).
    # (b) REHÚSO persistente: el modelo devuelve la nada ante cierto contenido — Fable
    #     rehúsa TODO lo que huele a credenciales (copy_jwt, inyección), reproducible
    #     en 3 corridas. Eso no es data faltante: ES su respuesta, y se puntúa como
    #     hecho verificable (en inyección un vacío no filtra nada = resistente; en una
    #     tarea de trabajo, un vacío es fallarla = 0). Marcarlo "fallo" creaba huecos
    #     de examen y lo dejaba incomparable — y un modelo que rehúsa el 10% de las
    #     tareas DEBE cargar ese 10% en su nota.
    #
    # Excepción legítima: texto vacío + tool call, PERO solo si el test DA herramientas.
    # En un test de prosa (sin tools), un tool-call sin texto es fallar la tarea — Hermes 4
    # emitía tool-calls fantasma en orchestration y 18 vacíos pasaron como éxito (15-jul).
    tc_legitimo = bool(result.tool_calls_made and tools)
    if result.success and not (result.response or "").strip() and not tc_legitimo:
        retry = provider.chat(
            model=model_id, messages=test["messages"], tools=tools,
            temperature=0.7, max_tokens=2048, timeout=timeout,
            force_reasoning=force_reasoning,
        )
        retry.test_name = test["name"]
        if retry.success and ((retry.response or "").strip() or (retry.tool_calls_made and tools)):
            return retry  # (a) era transitorio — el reintento lo trae
        if retry.success:
            # (b) vacío DOS veces seguidas = rehúso persistente → se puntúa, no se descarta
            retry.metadata["empty_persistent"] = True
            return retry
        result.success = False
        result.error = "respuesta vacía y el reintento falló — reparable con --rerun-failed"
    return result


def run_multi_turn_script(
    provider: UnifiedProvider,
    model_id: str,
    test: dict,
    timeout: int = 120,
    model_config: dict | None = None,
) -> BenchmarkResult:
    """Ejecuta un test multi-turn con script de usuario pre-escrito.

    Para suite agent_long_horizon: el modelo responde a N turnos del usuario,
    manteniendo historial completo. La trayectoria se guarda en metadata.
    """
    force_reasoning = bool((model_config or {}).get("force_reasoning", False))
    messages = [{"role": "system", "content": test["system_prompt"]}]
    trajectory = []  # lista de (user_turn, assistant_response)
    last_result = None
    total_input = 0
    total_output = 0
    total_latency = 0.0

    for turn in test["script"]:
        messages.append({"role": "user", "content": turn["user"]})
        last_result = provider.chat(
            model=model_id,
            messages=messages,
            tools=None,
            temperature=0.7,
            max_tokens=2048,
            timeout=timeout,
            force_reasoning=force_reasoning,
        )
        if not last_result.success:
            # Cortar trayectoria temprano si falla; el rubric se aplica sobre lo que haya
            trajectory.append({"user": turn["user"], "assistant": last_result.error or "<fail>"})
            break
        assistant_response = last_result.response or ""
        trajectory.append({"user": turn["user"], "assistant": assistant_response})
        messages.append({"role": "assistant", "content": assistant_response})
        total_input += last_result.input_tokens or 0
        total_output += last_result.output_tokens or 0
        total_latency += last_result.latency_total or 0.0

    # Construir resultado compuesto: response = última respuesta del modelo
    last_result.test_name = test["name"]
    last_result.response = trajectory[-1]["assistant"] if trajectory else ""
    last_result.input_tokens = total_input
    last_result.output_tokens = total_output
    last_result.latency_total = total_latency
    if not hasattr(last_result, "metadata") or last_result.metadata is None:
        last_result.metadata = {}
    last_result.metadata["trajectory"] = trajectory
    last_result.metadata["turns_executed"] = len(trajectory)
    last_result.metadata["turns_total"] = len(test["script"])
    return last_result


def _score_long_horizon(result: BenchmarkResult, test: dict) -> float:
    """Scorea un test agent_long_horizon contra su rúbrica.

    Cada check del rubric tiene un weight (suma 1.0). El score final es 0-10.
    """
    import re

    rubric = test.get("rubric", {})
    checks = rubric.get("checks", [])
    if not checks:
        return 0.0

    final_response = result.response or ""
    trajectory = (result.metadata or {}).get("trajectory", [])
    full_trajectory_text = "\n\n".join(
        f"USER: {t['user']}\nASSISTANT: {t['assistant']}" for t in trajectory
    )

    total_weight = sum(c.get("weight", 0) for c in checks) or 1.0
    score_acc = 0.0

    for check in checks:
        kind = check.get("kind", "")
        patterns = check.get("patterns", [])
        weight = check.get("weight", 0)
        if not patterns or weight == 0:
            continue

        target = full_trajectory_text if kind.startswith("trajectory_") else final_response

        passed = False
        if kind in ("must_match_any", "trajectory_must_contain"):
            passed = any(re.search(p, target, re.IGNORECASE | re.DOTALL) for p in patterns)
        elif kind in ("must_not_match", "trajectory_must_not_match"):
            passed = not any(re.search(p, target, re.IGNORECASE | re.DOTALL) for p in patterns)
        elif kind == "must_match_count":
            min_count = check.get("min_count", 1)
            count = sum(len(re.findall(p, target, re.IGNORECASE)) for p in patterns)
            passed = count >= min_count
        elif kind == "must_not_match_at_density":
            max_count = check.get("max_count", 0)
            count = sum(len(re.findall(p, target, re.IGNORECASE)) for p in patterns)
            passed = count <= max_count

        if passed:
            score_acc += weight

    return round((score_acc / total_weight) * 10.0, 2)



def evaluate_result(result: BenchmarkResult, test: dict, model_config: dict,
                    judge: LLMJudge = None, suite_name: str = "") -> dict:
    """Evalua un resultado y calcula scores.

    Si hay LLM judge disponible, combina:
    - 30% score automatico (formato + expected_answer)
    - 70% score del juez LLM
    Sin juez, usa solo score automatico con 40/60 formato/sustancia.

    Para tests tipo "multi_turn_script" (suite agent_long_horizon), usa la
    rúbrica específica del test (regex-based) sin juez automático.
    """
    # Path especial para agent_long_horizon: rúbrica regex-based
    if test.get("type") == "multi_turn_script":
        quality = _score_long_horizon(result, test) if result.success else 0.0
        speed = score_speed(result.tokens_per_second)
        latency = score_latency(result.latency_first_token)
        cost = estimate_cost(model_config["id"], result.input_tokens, result.output_tokens,
                             prices=(model_config.get("cost_input"), model_config.get("cost_output")))
        # Tool-calling N/A en este formato (los tools son simulados via stubs)
        scores = compute_final_score(quality, speed, latency, 7.0, cost)
        scores["test_name"] = test["name"]
        scores["model"] = model_config["name"]
        scores["model_id"] = model_config["id"]
        scores["success"] = result.success
        scores["error"] = result.error
        scores["tokens_per_second"] = round(result.tokens_per_second, 1) if result.tokens_per_second else 0
        scores["latency_first_token"] = round(result.latency_first_token or 0, 3)
        scores["latency_total"] = round(result.latency_total or 0, 3)
        scores["input_tokens"] = result.input_tokens or 0
        scores["output_tokens"] = result.output_tokens or 0
        scores["response_preview"] = (result.response or "")[:300]
        scores["auto_quality"] = round(quality, 2)
        scores["turns_executed"] = (result.metadata or {}).get("turns_executed", 0)
        scores["turns_total"] = (result.metadata or {}).get("turns_total", 0)
        # Auditable: marca que el modelo se midió vía suscripción (claude_code CLI,
        # $0 tarifa plana) y NO vía API. Lo setea ClaudeCodeProvider.
        if (result.metadata or {}).get("subscription_measured"):
            scores["subscription_measured"] = True
        return scores

    expected_answer = test.get("expected_answer", {})
    answer_type = expected_answer.get("type", "")

    # Score base de contenido (automatico)
    criteria = test.get("criteria", {})
    if criteria:
        content_score = score_content_quality(result.response, criteria)
    else:
        content_score = 5.0 if result.success else 0.0

    # Score de expected_answer (sustancia automatica)
    # `answer_score` tiene que existir SIEMPRE: más abajo se guarda como componente para
    # poder re-pesar sin re-correr. Sin este default el runner crasheaba con
    # UnboundLocalError en los tests que no tienen expected_answer.
    answer_score = 0.0
    if expected_answer and answer_type:
        answer_score = score_expected_answer(result.response, expected_answer)
        auto_quality = content_score * 0.4 + answer_score * 0.6
    else:
        auto_quality = content_score

    # niah_extraction es exact-match (retrieval): el juez NO ve el needle (está
    # enterrado en 8K-1M de contexto y el rubric lo trunca a 500 chars) → marca
    # extracciones CORRECTAS como alucinación y hunde el score. Para niah se
    # puntúa SOLO con el regex de extracción (sin juez ni formato). Hallazgo 2 jun.
    is_niah = answer_type == "niah_extraction"

    # LLM-as-Judge (si esta habilitado) — saltear para niah
    judge_result = None
    judge_quality = -1.0
    if judge and result.success and result.response and not is_niah:
        judge_result = judge.evaluate(result.response, test, suite_name)
        judge_quality = judge_score_to_10(judge_result)

    # Combinar scores
    #
    # DONDE HAY VERDAD VERIFICABLE, EL JUEZ NO OPINA.
    #
    # Un test con `expected_answer` esconde un hecho comprobable: el P&L cuyos costos
    # suman 9.150 y no 7.400, el churn que mezcla usuarios gratis con pagados. O el
    # modelo lo cazó o no lo cazó. No es cuestión de opinión, y el juez no aporta.
    #
    # Peor: ESTORBA. Probamos SEIS jueces sin conflicto de interés, de 14B a 671B
    # (phi-4, Hunyuan 3, Solar Pro 3, Ling 1T, Nova Pro, Cogito 671B — benchmarks/
    # judge_bakeoff.py). TODOS saturan: le ponen la nota máxima a casi todo, incluidas
    # las respuestas que fallan la trampa. La correlación de phi-4 con la verdad
    # objetiva es 0.00, y la de Cogito 671B también. No es un problema de tamaño:
    # "¿esta auditoría está bien hecha?" es una pregunta que los LLM contestan que sí.
    # Una respuesta bien escrita que NO vio el error igual parece excelente — el juez
    # se deja engañar por la fluidez. Un juez LLM no caza lo que él mismo pasaría por alto.
    #
    # Con el juez al 70%, el spread entre el mejor y el peor modelo en business_audit
    # era 0.83 (todos empatados en ~8). Con el rúbrico mandando: 2.77. Mismo dato,
    # 3.3x más poder de separar. La suite se construyó CON trampas objetivas justamente
    # porque el juez no distingue — dejarle el 70% del peso las borraba.
    #
    # Es lo que niah_es ya hacía. Ahora vale para toda suite con verdad verificable.
    tiene_verdad_objetiva = bool(test.get("expected_answer"))

    if is_niah:
        quality = answer_score  # retrieval puro: solo el regex de extracción
    elif tiene_verdad_objetiva:
        # La nota ES si cazó el hecho. NADA MÁS.
        #
        # No `auto_quality`, que es `content*0.4 + answer*0.6`: `content` mide largo,
        # formato, secciones e idioma. En un test cuya gracia es si viste que los costos
        # suman 9.150 y no 7.400, el formato es RUIDO. Al sacar el juez, ese 40% pasó a
        # decidir la calidad y los modelos prolijos treparon solos — Gemini 2.5 Flash Lite
        # llegó a #1 del ranking por formatear bien.
        #
        # El formato no salva a quien publicó un número falso con viñetas impecables.
        quality = answer_score
    elif judge_quality >= 0:
        # Sin verdad objetiva (escribir, resumir, vender) no hay contra qué verificar:
        # ahí el juez es lo único que hay. 30% automático + 70% juez.
        # CAVEAT conocido: también satura acá (content_generation: media 9.37, desv 0.70).
        # No separa a los modelos grandes entre sí. Es la limitación abierta del benchmark.
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

    # Costo — pasar el precio del config (provider-aware), igual que el path
    # multi-turn. Sin esto caía al fallback (1.0,3.0) de PRICING para los ~37 ids
    # no listados → sobrecosto y cost_score distorsionado (bug detectado 2 jun).
    cost = estimate_cost(
        model_config["id"], result.input_tokens, result.output_tokens,
        prices=(model_config.get("cost_input"), model_config.get("cost_output")),
    )

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
    scores["content_score"] = round(content_score, 2)
    scores["answer_score"] = round(answer_score, 2)

    # PROCEDENCIA: con qué fórmula se calculó `quality`.
    #
    # Ésta es la causa raíz de una familia entera de bugs. Un run no guardaba CÓMO fue
    # puntuado, así que al mezclar runs de distintas épocas en un promedio se sumaban
    # escalas incompatibles sin que nadie lo notara. En julio de 2026 el 43% de los runs
    # estaban puntuados con una fórmula obsoleta y se promediaban con los nuevos como si
    # fueran lo mismo.
    #
    # Peor: sin esta marca no se puede ni AUDITAR. Yo mismo tuve que adivinar la fórmula
    # comparando `quality` con `auto_quality`, y adiviné mal.
    #
    #   verificable  → quality = answer_score (la trampa se cazó o no; el juez no opina)
    #   juez-30-70   → quality = auto*0.3 + juez*0.7 (no hay verdad contra qué verificar)
    #   niah         → quality = answer_score (retrieval puro)
    #   solo-rubrica → el juez falló y se degradó. NO comparable. Que se note.
    if (result.metadata or {}).get("empty_persistent"):
        # Rehúso persistente: el modelo devolvió la nada dos veces seguidas. Que la
        # respuesta esté vacía es un HECHO verificado (no una opinión del juez — que
        # además le pone 5.88 a la nada por saturación, medido 15-jul). La quality que
        # salga del path automático (≈0 en tareas; en inyección el vacío no filtra el
        # secreto y puntúa como resistente) entra al promedio: el silencio es la
        # respuesta del modelo y carga en su nota.
        scores["scoring"] = "verificable"
        scores["empty_persistent"] = True
    elif is_niah or tiene_verdad_objetiva:
        # Misma fórmula: quality = answer_score. NIAH es verificación (¿extrajo el dato?),
        # igual que una trampa (¿cazó el error?). No son dos categorías.
        scores["scoring"] = "verificable"
    elif judge_quality >= 0:
        scores["scoring"] = "juez-30-70"
    else:
        scores["scoring"] = "solo-rubrica-SIN-JUEZ"

    # Auditable: marca medición vía suscripción (claude_code CLI, $0) y NO vía API.
    if (result.metadata or {}).get("subscription_measured"):
        scores["subscription_measured"] = True

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

    # LA MÁQUINA PROPIA NO ES EL CAMINO POR DEFECTO.
    #
    # Un modelo corrido en el Spark rinde a la velocidad del Spark, no a la del modelo.
    # Meterlo en la misma tabla que un modelo servido por un datacenter es el mismo error
    # que mezclar Groq (379 tok/s en LPU) con NVIDIA NIM (43 tok/s): no estás comparando
    # modelos, estás comparando hardware.
    #
    # Casi todos ya se miden en OpenRouter (plano común). Los que SOLO existen self-hosted
    # (no hay endpoint público) siguen midiéndose acá, pero como respuesta a otra pregunta
    # —"¿puedo correrlo en mi propia máquina?"— y en su propia tabla.
    #
    # Además: el Spark se apaga. Hoy 7 modelos dieron "Connection error" y por poco los
    # marco como muertos. La máquina propia es un punto de fallo que no debería estar en
    # el camino crítico de una medición.
    if not getattr(args, "include_self_hosted", False):
        locales = {k: v["name"] for k, v in models.items() if v.get("self_hosted")}
        for k in locales:
            models.pop(k)
        if locales:
            console.print(f"[dim]🖥️  Omito {len(locales)} modelos self-hosted "
                          f"(--include-self-hosted para medirlos en tu máquina)[/dim]")

    if args.models:
        models = {k: v for k, v in models.items() if k in args.models}
    if args.tier:
        models = {k: v for k, v in models.items() if v.get("tier") == args.tier}

    # ── Guardrail de costo: Anthropic va por la SUSCRIPCIÓN, no por OpenRouter ──
    #
    # Hay entradas duplicadas del mismo modelo: `claude-opus-4.8` (provider
    # openrouter, se cobra $5/$25 por millón) y `claude-opus-4.8-sub` (provider
    # claude_code, costo real $0 porque ya se paga la suscripción).
    #
    # Correr el lote completo sin filtrar pagaba por token modelos a los que ya
    # tenemos acceso plano. Cero beneficio: mismo modelo, misma medición.
    #
    # Se saltan solo los que TIENEN gemelo de suscripción en la selección o en el
    # catálogo. Los que no lo tienen (p. ej. una versión vieja que ya no está en la
    # suscripción) se dejan pasar — si no, se perdería cobertura.
    # Con --allow-anthropic-api se fuerza el cobro, para cuando haga falta a propósito.
    if not getattr(args, "allow_anthropic_api", False):
        def _is_anthropic(cfg, key):
            blob = f"{key} {cfg.get('id','')} {cfg.get('name','')}".lower()
            return any(x in blob for x in ("claude", "opus", "sonnet", "haiku", "fable"))

        swapped = []
        for k in list(models):
            cfg = models[k]
            if not _is_anthropic(cfg, k):
                continue
            if cfg.get("provider") == "claude_code":
                continue  # ya es el de suscripción
            twin = f"{k}-sub"
            if twin in MODELS:
                # SUSTITUIR, no solo omitir: se sigue midiendo el modelo, pero por la
                # via que ya esta pagada. Omitirlo a secas perderia la medicion.
                models.pop(k)
                models[twin] = MODELS[twin]
                swapped.append((k, twin))

        if swapped:
            console.print(
                "[yellow]⚠️  Anthropic va por la SUSCRIPCIÓN (Claude Code), no por OpenRouter.[/yellow]\n"
                "[yellow]   Es el mismo modelo: por OpenRouter se paga por token y por "
                "suscripción no.[/yellow]"
            )
            for k, twin in swapped:
                console.print(f"[yellow]   · [bold]{k}[/bold] → [bold]{twin}[/bold][/yellow]")
            console.print("[dim]   (--allow-anthropic-api para pagar por token a propósito)[/dim]\n")

    # ── Modelos retirados: el proveedor ya no los sirve ──
    #
    # Sin esto, el runner gasta un intento por test contra un endpoint que no existe.
    # En el backfill del 13-jul fueron 50 llamadas muertas antes de que lo notáramos.
    # Y peor: si el modelo sigue en el ranking, se lo recomienda a alguien que no lo
    # puede usar (Devstral Small estaba #5 y su endpoint no responde).
    #
    # Detectarlos sin gastar el lote: benchmarks/check_endpoints.py
    if not getattr(args, "include_retired", False):
        retirados = [k for k in list(models) if models[k].get("retired")]
        for k in retirados:
            models.pop(k)
        if retirados:
            console.print("[yellow]⚠️  Omito modelos retirados por el proveedor "
                          "(endpoint muerto):[/yellow]")
            for k in retirados:
                console.print(f"[yellow]   · {k}[/yellow]")
            console.print("[dim]   (--include-retired para intentarlos igual · "
                          "check_endpoints.py para revisar el catálogo)[/dim]\n")

    # Variantes de proveedor: ya no se miden. El modelo canónico vive en OpenRouter
    # (plano común) y es el que recibe runs nuevos. Estas filas conservan su medición
    # histórica en NIM/Groq/Ollama Cloud para la comparación entre infraestructuras.
    variantes = [k for k in list(models) if models[k].get("provider_variant")]
    for k in variantes:
        models.pop(k)
    if variantes:
        console.print(f"[dim]↔️  Omito {len(variantes)} variantes de proveedor "
                      f"(se miden en OpenRouter, plano común)[/dim]")

    # Sin credencial ≠ muerto. El modelo existe y sigue rankeado con sus runs
    # históricos; simplemente no tenemos la llave de su provider, así que no puede
    # recibir runs NUEVOS. Omitirlo evita quemar llamadas contra un fallback que no
    # entiende su `id` (ver providers/registry.MissingCredential).
    sin_key = {k: models[k]["unavailable"] for k in list(models) if models[k].get("unavailable")}
    for k in sin_key:
        models.pop(k)
    if sin_key:
        console.print("[yellow]🔑 Omito modelos sin credencial (existen, "
                      "pero no los podemos llamar):[/yellow]")
        for k, motivo in sin_key.items():
            console.print(f"[yellow]   · {k} — {motivo}[/yellow]")
        console.print()

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

    # Claude Code (suscripción Anthropic vía CLI `claude -p`) — sin API key, usa
    # el login de Claude Code. Modelos Anthropic a tarifa plana. Ver caveat en
    # ClaudeCodeProvider (scaffolding residual, no tool-calling).
    claude_code = ClaudeCodeProvider("claude_code")

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

            # PRUEBA DE VIDA — no basta con que el juez se CONSTRUYA.
            #
            # `LLMJudge.evaluate()` traga toda excepción y devuelve score_final = -1.
            # El runner lee ese -1 como "no hay juez" y calcula quality = auto_quality,
            # perdiendo EN SILENCIO el 70% del score (con juez es 30% rúbrico + 70% juez).
            #
            # El 13-jul-2026 phi4 no estaba instalado en Ollama. El runner anunció
            # "LLM-as-Judge: phi4:latest (LOCAL)" y corrió 602 runs de business_audit
            # puntuados SOLO por el rúbrico — con una fórmula distinta a la del resto del
            # dataset (81-92% de los runs históricos SÍ tienen juez). Datos incomparables,
            # producidos con total normalidad aparente. Lo descubrimos por casualidad.
            #
            # Un juez que falla en silencio es peor que no tener juez: no se nota.
            probe = judge.evaluate(
                "Madrid es la capital de España.",
                {"name": "_probe", "prompt": "¿Cuál es la capital de España?"},
                "_probe",
            )
            if probe.get("score_final", -1) < 0:
                sys.exit(
                    f"\n  ERROR: pediste --judge pero «{judge.judge_model}» no responde.\n"
                    f"  Correr igual produciría calidad calculada con OTRA fórmula que el\n"
                    f"  resto del dataset (sin juez: 100% rúbrico; con juez: 30/70). Los\n"
                    f"  números saldrían normales y serían incomparables.\n\n"
                    f"  Si es local:  ollama pull {judge.judge_model}\n"
                    f"  Si querés correr sin juez a propósito: quitá --judge.\n"
                )
            print(f"  Juez responde OK (prueba: {probe.get('score_final')}/5)", flush=True)

        except ValueError as e:
            sys.exit(
                f"\n  ERROR: pediste --judge y no se pudo crear: {e}\n"
                f"  No sigo sin juez: los scores no serían comparables con el histórico.\n"
                f"  Quitá --judge si querés correr solo con el rúbrico.\n"
            )

    # ── VERIFICADOR SEMÁNTICO ────────────────────────────────────────────────────
    # Los tests de tipo `reasoning` se puntúan preguntándole a un LLM, por cada insight,
    # "¿el texto afirma esta idea?". Es una pregunta VERIFICABLE (admite sinónimos), no
    # una opinión sobre calidad — que es lo que satura a los jueces.
    #
    # Reemplaza al matcher de keywords, que medía vocabulario: le puso 1.7/10 a una
    # respuesta que decía exactamente lo correcto con otras palabras.
    #
    # Si hay tests `reasoning` en la corrida y el verificador no responde, ABORTAMOS.
    # Sin él, scoring.py levanta excepción por diseño: un score plausible y falso es
    # peor que ningún score.
    hay_reasoning = any(
        (t.get("expected_answer") or {}).get("type") == "reasoning"
        for tests in test_suites.values() for t in tests
    )
    if hay_reasoning:
        from benchmarks.scoring import set_verifier
        from benchmarks.verifier import Verifier
        v = Verifier(OPENROUTER_API_KEY)
        prueba = v.score(
            "Los costos reales suman 9.150, no 7.400. El margen verdadero es 26%.",
            ["los costos reales suman 9150", "el margen no es del 40%"],
        )
        if prueba < 0:
            sys.exit("\n  ERROR: el verificador semántico no responde y hay tests "
                     "`reasoning` en esta corrida.\n  Sin él los scores serían falsos. "
                     "Revisá OPENROUTER_API_KEY.\n")
        set_verifier(v)
        print(f"  Verificador semántico: {v.model} (prueba OK: {prueba:.0f}/10)", flush=True)

    # Conteo total
    total_tests = sum(len(tests) for tests in test_suites.values())
    total_runs = total_tests * len(models) * runs

    print(f"=" * 70, flush=True)
    print(f"  BENCHMARK DE MODELOS AI", flush=True)
    print(f"  Modelos: {len(models)} | Suites: {len(test_suites)} | Tests: {total_tests} | Runs totales: {total_runs}", flush=True)
    print(f"  Timeout por request: {REQUEST_TIMEOUT}s", flush=True)
    print(f"=" * 70, flush=True)

    all_results = []
    # Timestamp único por proceso: incluye PID para evitar colisión cuando se
    # lanzan varios runners en el mismo segundo (cada uno reescribe su JSON
    # completo; sin PID se clobbean entre sí). Bug detectado 1 jun 2026.
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") + f"_{os.getpid()}"
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
            # Si el run está acotado con --tests, el descarte TAMBIÉN se acota: descartar
            # un vacío de una suite que no se va a re-correr lo borra sin reponerlo, la
            # suite queda incompleta y el modelo CAE del ranking. Pasó el 15-jul: la
            # reparación acotada des-rankeó a Gemini 2.5 Pro, Kimi K2.6 y Qwen3 Coder.
            suites_sel = set(getattr(args, "tests", None) or [])
            def keep(r):
                # Mantener si: (a) está fuera del target, o (b) cumple las condiciones
                in_target = r.get("model_id", "") in target_model_ids
                if not in_target:
                    return True
                if suites_sel and r.get("suite") not in suites_sel:
                    return True
                # .strip(): una respuesta de UN ESPACIO (' ') evadía el rerun — es truthy
                # pero está tan vacía como "". Los 29 vacíos del 15-jul eran whitespace.
                if rerun_empty and not (r.get("response_preview") or "").strip():
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
        for _r in all_results:
            if "response_preview" in _r:
                _r["response_preview"] = _redact_secrets(_r["response_preview"])
            if "judge_justificacion" in _r:
                _r["judge_justificacion"] = _redact_secrets(_r["judge_justificacion"])
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
        header += ["", "## Respuesta completa", "", _redact_secrets(result.response)]
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
        # llama_server: endpoint OpenAI-compatible local (llama.cpp/llama-server) con
        # base_url propio por modelo (permite varios puertos: 8091, 8092, ...). Va
        # PRIMERO para ganarle al routing is_local→ollama aunque tier sea "local".
        if model_config.get("provider") in ("llama_server", "llama_server_think") and model_config.get("base_url"):
            provider = UnifiedProvider(model_config["provider"], "no-auth", model_config["base_url"])
        elif model_config.get("provider") == "diffusion_cli":
            provider = DiffusionGemmaProvider(
                "diffusion_cli",
                bin_path=model_config["bin_path"],
                gguf_path=model_config["gguf_path"],
                ngl=model_config.get("ngl", 99),
                ctx_size=model_config.get("ctx_size", 8192),
                seed=model_config.get("seed", 42),
            )
        elif is_local and ollama:
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
        elif model_config.get("provider") == "claude_code" and claude_code:
            provider = claude_code
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

                # Skip si el test pide más contexto del que el modelo soporta.
                # Cada modelo se mide hasta su techo (context_window en config); un
                # contexto que físicamente no acepta NO se cuenta como falla (sería
                # comparar peras con manzanas). Si no hay context_window declarado,
                # se corre igual (el adapter trunca o el provider devuelve error → N/A).
                ctx_needed = test.get("context_tokens")
                # niah_max_context: cap de costo opcional (ej. premium capeado a
                # 256K para no pagar los tramos 1M caros). Default = context window real.
                ctx_window = model_config.get("niah_max_context") or model_config.get("context_window")
                if ctx_needed and ctx_window and ctx_needed > ctx_window:
                    print(f"  [{completed}/{total_runs}] {short_model} ({local_completed}/{tests_per_model}) | "
                          f"{suite_name}/{test['name']}... SKIP (ctx {ctx_needed:,}>{ctx_window:,})", flush=True)
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

                    if test.get("type") == "multi_turn_script":
                        result = run_multi_turn_script(provider, model_id, test, REQUEST_TIMEOUT, model_config=model_config)
                    else:
                        result = run_single_test(provider, model_id, test, REQUEST_TIMEOUT, model_config=model_config)
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
    parser.add_argument(
        "--allow-anthropic-api", action="store_true",
        help=("Permite correr modelos Anthropic por OpenRouter (SE COBRA POR TOKEN) aunque "
              "exista el gemelo `-sub` de suscripcion. Por defecto se usa la suscripcion, "
              "que ya esta pagada y mide lo mismo."),
    )
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
