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
from benchmarks.scoring import PRICING, compute_final_score, cost_score_log, DEFAULT_WEIGHTS

# Costo minimo por call para modelos gratis/free tier/suscripcion.
# Evita cost_score 10.0 artificial y hace comparables todos los modelos.
# $0.001/call = $1 por 1,000 calls, precio de referencia "cheap".
MIN_COST_PER_CALL = 0.001

# --- Umbrales de muestra (fuente unica; el resto del pipeline los importa) ---
# El benchmark tiene DOS umbrales distintos y confundirlos ya causo un bug:
# models.json rankeaba un modelo de 10 runs en el podio (#3) mientras las
# paginas pSEO -- que si filtran >=50 -- no lo mostraban. Misma data, dos
# rankings publicos contradictorios.
#
#   MIN_RUNS_TESTED (20) = cobertura suficiente para reportar el modelo.
#   MIN_RUNS_RANKED (50) = muestra suficiente para RANKEARLO contra otros.
#
# El de ranking es mas alto a proposito: con 3-12 runs la varianza permite que
# un modelo lidere por azar. generate_rankings.py y generate_comparison.py ya
# aplicaban 50; ahora el umbral vive aca y todos consumen el mismo.
MIN_RUNS_TESTED = 20
MIN_RUNS_RANKED = 50


def sample_tier(runs: int) -> str:
    """Confiabilidad de la muestra. 'solid' es el unico que entra al ranking oficial."""
    if runs >= MIN_RUNS_RANKED:
        return "solid"
    if runs >= MIN_RUNS_TESTED:
        return "partial"
    return "preliminary"


def _ci95(vals: list) -> float | None:
    """Margen de error al 95% de la media (1.96 * SE). None si no hay muestra."""
    import statistics as _s
    vals = [v for v in vals if v is not None]
    if len(vals) < 2:
        return None
    return round(1.96 * _s.pstdev(vals) / (len(vals) ** 0.5), 3)

# Merge cloud + local models para que DGX y otros locales aparezcan en la calculadora
MODELS = {**_CLOUD_MODELS, **OLLAMA_MODELS}


def _recalc_final(r: dict) -> float:
    """Recalcula el `final` de un run con los pesos default actuales.

    Útil cuando cambian los pesos en `scoring.py` — recalculamos sin re-correr
    los benchmarks. Usa los componentes raw guardados en cada run (quality,
    speed, latency, tool_calling, cost_usd).

    Si el run tiene costo normalizado OpenRouter (_cost_usd_or), se usa ese
    para que el score global sea comparable entre providers.
    """
    q = r.get("quality")
    s = r.get("speed", 0) or 0
    lat = r.get("latency", 0) or 0
    tc = r.get("tool_calling", 0) or 0
    cost = r.get("_cost_usd_or") or r.get("cost_usd", 0) or 0
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
    # Auditoria de negocio: es razonamiento aplicado con trampas verificables
    # (aritmetica que no cierra, causalidad falsa, metrica que mezcla poblaciones).
    "business_audit": "Razonamiento",
    # Planificacion estrategica: generar un plan VALIDO (restricciones, aritmetica,
    # activos reales, falsabilidad). Es razonamiento aplicado, no redaccion.
    "business_strategy": "Razonamiento",
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


# Una suite entra al `quality` (y por tanto al score) SOLO si la corrió al menos
# este porcentaje de los modelos con cobertura. Si no, se reporta aparte.
#
# EL BUG QUE ARREGLA (13-jul-2026): agregar una suite nueva PENALIZABA al que la
# corría primero. Las suites nuevas suelen ser más duras que la media (business_audit
# media ~5, contra 7.57 global), así que los 6 modelos del smoke test vieron caer su
# quality mientras los otros 92 seguían con la nota vieja. Claude Opus 4.8 bajó de
# 8.65 a 8.39 sin que el modelo cambiara: solo por haber sido de los primeros en
# rendir el examen difícil.
#
# Es el mismo problema, más silencioso, que ya arrastraban `tool_calling` (94%) y
# `agent_long_horizon` (60%): mezclar modelos evaluados sobre baterías distintas.
#
# Con el umbral, una suite nueva se acumula sin distorsionar hasta que la cobertura
# es amplia; ahí entra al score de todos a la vez, que es cuando compara de verdad.
MIN_SUITE_COVERAGE = 0.80


def suite_coverage(all_runs_by_model: dict, es_rankeable=None) -> dict:
    """{suite: fracción de los modelos QUE COMPITEN que ya rindieron esa suite}.

    El denominador son los modelos **rankeables**, no todos los que tienen ≥50 runs.
    La diferencia no es cosmética: 39 de los 98 modelos con ≥50 runs están RETIRADOS
    (su endpoint murió) o son VARIANTES DE PROVEEDOR (el mismo modelo servido por otra
    infra, que sacamos del ranking). El runner ya no los mide y **nunca** van a rendir
    una suite nueva.

    Dejarlos en el denominador los volvía un lastre permanente: `business_audit` marcaba
    67% de cobertura (bajo el umbral de 80%) y por lo tanto NO PUNTUABA — aunque el 80%
    de los modelos que de verdad compiten ya la habían rendido. La suite más
    discriminante del benchmark estaba condenada a no contar nunca, por culpa de
    modelos muertos que arrastraban la cuenta.
    """
    rankeable = es_rankeable or (lambda m: True)
    pool = [m for m, runs in all_runs_by_model.items()
            if len(runs) >= MIN_RUNS_RANKED and rankeable(m)]
    if not pool:
        return {}
    cov = defaultdict(set)
    for m in pool:
        for r in all_runs_by_model[m]:
            if r.get("success") and r.get("suite"):
                cov[r["suite"]].add(m)
    return {s: len(ms) / len(pool) for s, ms in cov.items()}


# Qué fórmula DEBE tener un run según su suite. Si tiene otra, no es comparable.
def _formula_esperada(suite: str, test_name: str | None = None) -> str:
    """Qué fórmula usa este TEST hoy. La regla es por test, no por suite.

    Una suite puede ser MIXTA. `news_seo_writing` tiene 3 tests con verdad verificable
    (¿el JSON es válido? ¿está en español? ¿inventó datos?) y 2 sin ella (¿el artículo es
    bueno?). Cada uno se puntúa distinto, y eso está bien:

        con expected_answer  → verificable   (quality = ¿acertó el hecho?)
        sin expected_answer  → juez-30-70    (no hay contra qué verificar)

    Exigir una sola fórmula para toda la suite era MI error: hacía que runs correctos
    parecieran incompatibles. NIAH tampoco es una categoría aparte — su quality también
    es answer_score (extrajo el dato o no).
    """
    from benchmarks.runner import ALL_TEST_SUITES
    if suite.startswith("niah"):
        return "verificable"
    # agent_long_horizon (multi_turn_script): se puntúa con RÚBRICA regex determinista
    # (no juez, no expected_answer). El runner estampa "verificable" correctamente; sin
    # este caso, la regla "sin expected_answer → juez-30-70" marcaba mal toda la suite.
    if suite.startswith("agent_long_horizon"):
        return "verificable"
    tests = ALL_TEST_SUITES.get(suite, [])
    if test_name:
        t = next((x for x in tests if x.get("name") == test_name), None)
        if t is not None:
            return "verificable" if t.get("expected_answer") else "juez-30-70"
    # Sin nombre de test: solo se puede afirmar si TODA la suite es verificable
    if tests and all(x.get("expected_answer") for x in tests):
        return "verificable"
    return "juez-30-70"


FORMULA_ESPERADA = _formula_esperada


def _misma_formula(r: dict) -> bool:
    """¿Este run se puntuó con la fórmula que su suite usa HOY?

    Un run sin la marca `scoring` es de antes de que existiera la procedencia (jul-2026):
    no se puede saber cómo se calculó y NO se puede promediar con los nuevos. El 43% del
    dataset estaba en esa situación, mezclando tres escalas distintas en un mismo número.

    Preferimos perder muestra a publicar un promedio de peras y manzanas.
    """
    s = r.get("suite")
    if not s:
        return False
    marca = r.get("scoring")
    if not marca:
        return False           # sin procedencia → fuera
    return marca == FORMULA_ESPERADA(s, r.get("test_name"))


def aggregate_metrics(runs, low_coverage_suites=frozenset()):
    """Reduce lista de runs a métricas: score, latencia, tok/s, por pilar y por suite.

    Recalcula `final` por run con los pesos default actuales — permite cambiar
    los pesos en `scoring.py` sin re-correr benchmarks. Además expone los
    componentes promedio (quality, cost_score, speed, latency, tool_calling)
    para mostrar en tablas y permitir que la calculadora aplique pesos custom.

    `low_coverage_suites`: suites que aún no corrió suficiente gente. Se EXCLUYEN
    del quality/score (pero siguen visibles en score_by_suite), para no castigar a
    los primeros en rendir el examen nuevo.
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

    def _is_tool_calling(r):
        return str(r.get("suite", "")) == "tool_calling"

    def _is_agentic(r):
        # Tareas multi-paso de horizonte largo. Es donde los premium (Luna/Sol/Fable) se
        # diferencian, así que SÍ cuenta en la calidad titular (no se saca del ranking).
        # Se expone ADEMÁS como eje propio (agentic_score) para que el wizard filtre por
        # casos de uso agénticos. Decisión de Cristian, 16-jul: "dentro + eje propio".
        return str(r.get("suite", "")).startswith("agent_long_horizon")

    def _is_low_coverage(r):
        # Suite que todavia no corrio suficiente gente: no puede entrar al score
        # sin castigar a los primeros que la rindieron. Ver MIN_SUITE_COVERAGE.
        return str(r.get("suite", "")) in low_coverage_suites

    # General = tareas prácticas. Excluye tres suites que son dimensiones SEPARADAS
    # y no deben contaminar `quality`:
    #   - niah (long-context) y prompt_injection (seguridad): medidas desigual entre modelos.
    #   - tool_calling: el README ya declara que va "fuera del score, como badge"
    #     (tiene su propio tool_calling_score_avg) -- pero el codigo lo estaba metiendo
    #     igual por la puerta de atras, via quality.
    #
    # Y ademas el juez lo mide AL REVES. En tool_calling la respuesta correcta ES la
    # llamada a la herramienta; el texto queda casi vacio. El juez SOLO LEE TEXTO, asi
    # que a un modelo que hace el tool call limpio le pone 1/5 ("no proporciona detalles
    # especificos") y a uno que ignora la herramienta y escribe un parrafo explicando,
    # le pone 7.5. Medido: los que llaman bien promedian ~5.2; los que no llaman, ~7.5.
    # Contaminaba quality entre -0.14 y -0.22 justo a los modelos que hacen bien tool
    # calling (12-jul-2026).
    general = [r for r in runs
               if not _is_niah(r) and not _is_security(r)
               and not _is_tool_calling(r) and not _is_low_coverage(r)]
    niah = [r for r in runs if _is_niah(r)]
    security = [r for r in runs if _is_security(r)]
    tool_runs = [r for r in runs if _is_tool_calling(r)]
    # Los runs agénticos también están en `general` (cuentan en la calidad titular);
    # esta lista adicional es solo para exponer el eje agentic_score, no los saca.
    agentic = [r for r in runs if _is_agentic(r)]

    # El score global también se promedia POR TEST (mismo sesgo que quality: repetir un
    # test fácil no debería subirte el score). _por_test se define más abajo, así que acá
    # se arma con la misma lógica.
    _acc_final = defaultdict(list)
    for _r in general:
        if _r.get("_final_recalc") is not None and _r.get("test_name"):
            _acc_final[_r["test_name"]].append(_r["_final_recalc"])
    finals_recalc = [sum(v) / len(v) for v in _acc_final.values()]

    judge_scores = [r.get("judge_score") for r in general if r.get("judge_score") is not None]
    speeds = [r.get("tokens_per_second", 0) for r in general if r.get("tokens_per_second", 0) > 0]
    latencies = [r.get("latency_total", 0) for r in general if r.get("latency_total", 0) > 0]
    in_tokens = sum(r.get("input_tokens", 0) or 0 for r in general)
    out_tokens = sum(r.get("output_tokens", 0) or 0 for r in general)

    def _por_test(rs, campo):
        """Promedia por TEST, no por run. Cada test pesa igual.

        Un modelo con 5 corridas de un test y 1 de otro tenía el primero pesando 5 veces
        más. Y el sesgo no es aleatorio: se repiten los tests que el modelo LOGRA
        completar, que tienden a ser los fáciles. De las 317 desviaciones medidas entre
        'media por run' y 'media por test', TODAS iban en la misma dirección: inflando.
        """
        acc = defaultdict(list)
        for r in rs:
            v = r.get(campo)
            tn = r.get("test_name")
            if v is not None and tn:
                acc[tn].append(v)
        return [sum(v) / len(v) for v in acc.values()] if acc else []

    # Componentes promedio (solo tareas prácticas, no-niah), promediados POR TEST.
    # Si existe _cost_score_or (normalizado OpenRouter) lo usamos; si no, fallback al cost_score original.
    qualities = _por_test(general, "quality")
    cost_scores = [
        r.get("_cost_score_or") if r.get("_cost_score_or") is not None else r.get("cost_score")
        for r in general
        if (r.get("_cost_score_or") is not None or r.get("cost_score") is not None)
    ]
    speed_scores = [r.get("speed") for r in general if r.get("speed") is not None]
    latency_scores = [r.get("latency") for r in general if r.get("latency") is not None]
    # El badge de tool calling se calcula sobre TODOS los runs (general + la suite
    # tool_calling, que ya no esta en general). Si se calculara solo sobre `general`,
    # sacar la suite del quality habria vaciado tambien el badge.
    tc_scores = [r.get("tool_calling") for r in (general + tool_runs)
                 if r.get("tool_calling") is not None]

    # Score por pilar (general) Y por suite (incluye niah para visibilidad)
    by_pillar = defaultdict(list)
    by_pillar_test = defaultdict(lambda: defaultdict(list))
    by_suite = defaultdict(list)
    # Dimensiones CRUDAS por pilar. Sin esto, score_by_pillar sale pre-horneado con
    # los pesos fijos 70/15/7.5/7.5 y la calculadora no puede recomponerlo con los
    # pesos del usuario: al elegir un pilar, los sliders se ignoraban en silencio
    # (app.js getScore) y la UI mostraba un ranking que NO era el que el usuario pidio.
    # Exportando las dimensiones crudas, "coding, y la latencia me da igual" pasa a
    # ser expresable.
    dims_by_pillar = defaultdict(lambda: defaultdict(list))
    DIMS = {"quality_avg": "quality", "speed_score_avg": "speed", "latency_score_avg": "latency"}

    # QUÉ TESTS RINDIÓ DE VERDAD, no cuántos.
    #
    # El promedio de una suite se calculaba sobre los tests que ESE modelo rindió. Si a
    # uno le faltaban 6 de 10, su nota salía de un examen más corto — y se publicaba al
    # lado de la de otro que rindió los 10, como si fueran comparables. No lo son.
    #
    # Caso real (14-jul-2026): publiqué "MiniMax M3 audita mejor que Claude Opus 4.8,
    # 8.24 vs 6.94". MiniMax había rendido **4 de los 10 tests**. En los 4 que ambos
    # rindieron, Opus GANA 10.00 a 9.00. El titular estaba invertido.
    #
    # Cristian lo cazó preguntando por qué GPT-5.6 Sol no le ganaba a Luna. Sol había
    # rendido 6 de 10.
    #
    # Un promedio sobre un examen incompleto no es una nota baja: es una nota que no
    # existe. Ahora se marca (`suites_incompletas`) y no se publica como comparable.
    tests_por_suite = defaultdict(set)

    for r in runs:
        suite = r.get("suite", "")
        if not suite or r.get("_final_recalc") is None:
            continue
        if r.get("test_name"):
            tests_por_suite[suite].add(r["test_name"])
        by_suite[suite].append(r["_final_recalc"])
        pillar = SUITE_TO_PILLAR.get(suite)
        if pillar:
            # (test → runs) para poder promediar por test, no por run
            by_pillar_test[pillar][r.get("test_name") or "?"].append(r["_final_recalc"])
            for out_key, raw_key in DIMS.items():
                v = r.get(raw_key)
                if v is not None:
                    dims_by_pillar[pillar][out_key].append(v)
            c = r.get("_cost_score_or") if r.get("_cost_score_or") is not None else r.get("cost_score")
            if c is not None:
                dims_by_pillar[pillar]["cost_score_avg"].append(c)
    # Cada test pesa igual dentro del pilar (ver _por_test)
    pillars = {
        p: round(sum(sum(v) / len(v) for v in tests.values()) / len(tests), 2)
        for p, tests in by_pillar_test.items() if tests
    }
    # {pilar: {quality_avg, cost_score_avg, speed_score_avg, latency_score_avg, quality_ci95}}
    pillar_dims = {}
    for p, dims in dims_by_pillar.items():
        entry = {k: round(sum(v) / len(v), 3) for k, v in dims.items() if v}
        # Margen de error de la calidad DENTRO del pilar → permite detectar empates
        # estadisticos por pilar, no solo en el global.
        entry["quality_ci95"] = _ci95(dims.get("quality_avg", []))
        pillar_dims[p] = entry
    # CADA TEST PESA IGUAL, sin importar cuántas veces se corrió.
    #
    # Antes el promedio de una suite era la media de todos los RUNS. Si un modelo tenía 5
    # corridas de un test y 1 de otro, el primero pesaba 5 veces más. Y no es aleatorio:
    # un modelo repite los tests que LOGRA completar, que tienden a ser los fáciles. Por
    # eso el sesgo va siempre en la misma dirección — las 317 desviaciones medidas son
    # TODAS positivas: el promedio por-run infla.
    #
    # Caso real: MiniMax M3 tenía 5 corridas de cada uno de los 4 tests de business_audit
    # que rindió, y cero de los 6 restantes. Claude Opus tenía 1 de cada uno de sus 10.
    # Comparar esos dos promedios no era comparar modelos.
    #
    # Ahora: se promedia cada test primero, y después los tests entre sí.
    # Las tablas POR-SUITE filtran procedencia (una suite mezcla runs de fórmulas
    # distintas si no). Este es el fix REAL del caso Sol-vs-Fable: la tabla por-tarea
    # se leía de una población y el ranking de otra. NO se filtra la calidad GLOBAL
    # (quality_avg) — hacerlo, sobre un dataset a medio marcar, computa la calidad de
    # cada modelo sobre un mix de suites distinto y colapsa el ranking (probado 15-jul).
    by_suite_test = defaultdict(lambda: defaultdict(list))
    for r in runs:
        s, tn = r.get("suite", ""), r.get("test_name")
        if s and tn and r.get("_final_recalc") is not None and _misma_formula(r):
            by_suite_test[s][tn].append(r["_final_recalc"])

    suites = {
        s: round(sum(sum(v) / len(v) for v in tests.values()) / len(tests), 2)
        for s, tests in by_suite_test.items() if tests
    }

    # CALIDAD PURA POR SUITE — sin costo ni velocidad.
    #
    # `score_by_suite` es el score COMPUESTO restringido a esa suite: incluye precio y
    # velocidad. El nombre engaña. Yo mismo lo leí como calidad y construí un titular
    # falso sobre él: "MiniMax M3 audita mejor que Claude Opus 4.8 (7.43 vs 6.94)".
    #
    # En calidad pura empatan (8.07 vs 8.20). MiniMax "ganaba" porque cuesta 20× menos.
    # Las dos cosas son ciertas y dicen cosas distintas: una responde "¿quién audita
    # mejor?" y la otra "¿qué me conviene pagar?". Confundirlas es publicar mentiras.
    calidad_por_suite = defaultdict(lambda: defaultdict(list))
    for r in runs:
        s, tn, q = r.get("suite"), r.get("test_name"), r.get("quality")
        if s and tn and q is not None and _misma_formula(r):
            calidad_por_suite[s][tn].append(q)
    quality_by_suite = {
        s: round(sum(sum(v) / len(v) for v in tests.values()) / len(tests), 2)
        for s, tests in calidad_por_suite.items() if tests
    }

    # Suites que el modelo NO terminó. Su promedio sale de un examen más corto que el de
    # los demás: se reporta, pero marcado — no se puede comparar contra quien rindió todo.
    from benchmarks.runner import ALL_TEST_SUITES as _TS
    incompletas = {
        s: {"rindio": len(tests_por_suite[s]), "total": len(_TS[s])}
        for s in suites
        if s in _TS and len(tests_por_suite[s]) < len(_TS[s])
    }

    scores = finals_recalc  # mantener naming downstream

    # Dimensión long-context separada (quality y final promedio de los niah)
    niah_q = [r.get("quality") for r in niah if r.get("quality") is not None]
    niah_f = [r["_final_recalc"] for r in niah if r.get("_final_recalc") is not None]
    agentic_q = [r.get("quality") for r in agentic if r.get("quality") is not None]
    agentic_f = [r["_final_recalc"] for r in agentic if r.get("_final_recalc") is not None]

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
        "runs": len(general),  # cobertura = tareas prácticas (umbral tested >=20)
        "total_runs": len(runs),  # todos los runs exitosos incluyendo niah y seguridad
        "score_global": round(sum(scores) / len(scores), 2) if scores else None,
        "score_by_pillar": pillars,
        # Dimensiones crudas por pilar -> permiten recomponer el score de un pilar
        # con los pesos del usuario (ver getScore en app.js).
        "dims_by_pillar": pillar_dims,
        # ⚠️ COMPUESTO (calidad + costo + velocidad). Para "¿quién es mejor EN esto?"
        # usá `quality_by_suite`. Ver el comentario en aggregate_metrics.
        "score_by_suite": suites,
        "quality_by_suite": quality_by_suite,
        # {suite: {rindio, total}} — las suites que este modelo NO terminó. Su promedio
        # sale de un examen más corto: NO es comparable con el de quien rindió todo.
        # Quien consuma score_by_suite tiene que mirar esto antes de comparar.
        "suites_incompletas": incompletas,
        # Componentes raw promedio (permite mostrar columnas separadas + recalcular pesos en calculadora)
        "quality_avg": round(sum(qualities) / len(qualities), 2) if qualities else None,
        # Incertidumbre de esa media. Sin esto, el ranking finge una precision que
        # no tiene: la calidad de los modelos top esta apelotonada (std entre
        # modelos ~0.60) y la dispersion DENTRO de un modelo es ~1.70. Publicar
        # 8.47 vs 8.44 como si fueran distintos es ruido con decimales.
        # quality_ci95 = margen de error de la media (1.96 * std / sqrt(n)).
        # Dos modelos cuyos intervalos se solapan EMPATAN: no hay evidencia de
        # que uno sea mejor. Lo consume el generador de bandas.
        "quality_ci95": _ci95(qualities),
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
        # --- Eje agéntico (agent_long_horizon: tareas multi-paso) ---
        # SÍ cuenta en quality_avg (es donde los premium se diferencian); esto lo expone
        # ADEMÁS como eje propio para que la calculadora filtre por casos de uso agénticos.
        "agentic_runs": len(agentic),
        "agentic_quality": round(sum(agentic_q) / len(agentic_q), 2) if agentic_q else None,
        "agentic_score": round(sum(agentic_f) / len(agentic_f), 2) if agentic_f else None,
        # --- Dimensión seguridad (prompt_injection_es: resistencia a fuga) ---
        "security_runs": len(security),
        "security_score": round(
            sum(r.get("quality") for r in security if r.get("quality") is not None)
            / max(1, sum(1 for r in security if r.get("quality") is not None)), 2
        ) if any(r.get("quality") is not None for r in security) else None,
        # Dimensión rehúso de política (Cristian, 15-jul): rehusar/bloquear secretos NO
        # penaliza seguridad (ahí es resistencia máxima, ya reflejado en security_score),
        # pero SÍ es limitación operativa para quien usa la API. Dimensión propia, el
        # usuario la pesa según su caso.
        "policy_refusal_rate": round(
            sum(1 for r in runs if r.get("empty_persistent") or r.get("api_refusal"))
            / max(1, len(runs)), 4),
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


def build_openrouter_lookup():
    """Construye lookup de configs OpenRouter por id y por nombre base.

    Permite normalizar el costo de cualquier modelo al precio OpenRouter,
    haciendo comparables modelos que corren en Groq, NIM, suscripciones, etc.
    """
    from collections import defaultdict
    or_configs = [c for c in MODELS.values() if c.get("provider", "openrouter") == "openrouter"]
    by_id = {}
    by_name_base = defaultdict(list)
    for c in or_configs:
        by_id[c["id"]] = c
        base = c.get("name", "").split("(")[0].strip()
        if base:
            by_name_base[base].append(c)
    return {"by_id": by_id, "by_name_base": dict(by_name_base)}


def _openrouter_config_for(cfg: dict, lookup: dict) -> dict | None:
    """Devuelve la config OpenRouter equivalente para un modelo dado."""
    model_id = cfg.get("id", "")
    name_base = cfg.get("name", "").split("(")[0].strip()

    # Match exacto por id
    if model_id and model_id in lookup["by_id"]:
        return lookup["by_id"][model_id]

    # Match por nombre base
    candidates = lookup["by_name_base"].get(name_base, [])
    if not candidates:
        return None

    # Descartar variantes free si hay alternativas de pago
    non_free = [c for c in candidates if ":free" not in c.get("id", "") and "(free)" not in c.get("name", "").lower()]
    if non_free:
        candidates = non_free

    # Elegir la version estandar: preferir la de mayor costo ( suele ser la version no-cuantizada)
    # o si hay una sola, usar esa.
    return max(candidates, key=lambda c: (c.get("cost_input", 0) or 0) + (c.get("cost_output", 0) or 0))


def _estimate_cost_openrouter(r: dict, or_cfg: dict) -> float:
    """Estima el costo USD de un run usando precios OpenRouter."""
    if or_cfg is None:
        return 0.0
    ci = or_cfg.get("cost_input", 0) or 0
    co = or_cfg.get("cost_output", 0) or 0
    inp = r.get("input_tokens", 0) or 0
    out = r.get("output_tokens", 0) or 0
    return (inp * ci + out * co) / 1_000_000


# --- Referencia de scoring CONGELADA (v4.0+) -------------------------------
# El z-score se estandariza contra una población de referencia FIJA (guardada en
# scoring_reference.json), no contra la población viva. Consecuencia: agregar un
# modelo nuevo NO recalcula el score de los demás — los números dejan de caducar
# solos. La referencia se recalcula (recalibra) SOLO de forma deliberada con
# `--recalibrate --scoring-version vX.Y`, al cortar una versión del benchmark.
# Sin archivo de referencia el export cae al comportamiento histórico (z-score
# vivo) y avisa: así una corrida sobre un dataset parcial nunca congela basura.
SCORING_REF_PATH = Path(__file__).parent.parent / "scoring_reference.json"


def _load_scoring_reference():
    """Referencia congelada (dict) o None si no existe / está incompleta."""
    try:
        ref = json.loads(SCORING_REF_PATH.read_text(encoding="utf-8"))
    except (FileNotFoundError, ValueError):
        return None
    if not all(k in ref for k in ("norm_stats", "norm_stats_by_pillar", "score_rescale")):
        return None
    return ref


def _persist_scoring_reference(norm_stats, norm_stats_by_pillar, score_rescale, version):
    """Congela la referencia de scoring en disco. Solo se llama en --recalibrate."""
    payload = {
        "version": version,
        "computed_at": __import__("datetime").datetime.now().isoformat(timespec="seconds"),
        "score_method": "zscore_frozen_v4",
        "norm_stats": norm_stats,
        "norm_stats_by_pillar": norm_stats_by_pillar,
        "score_rescale": score_rescale,
    }
    SCORING_REF_PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"🧊 scoring_reference.json congelado · versión={version} · {SCORING_REF_PATH}")


def build_export(recalibrate=False, scoring_version=None):
    by_id, by_id_and_name = load_all_results()
    or_lookup = build_openrouter_lookup()
    models_export = []

    # Cobertura por suite ANTES de agregar nada: una suite que corrió poca gente no
    # puede entrar al score, o castiga a los primeros que la rindieron.
    #
    # El denominador son los modelos QUE COMPITEN. Los retirados (endpoint muerto) y las
    # variantes de proveedor (el mismo modelo servido por otra infra) ya no se miden y
    # nunca van a rendir una suite nueva: dejarlos en la cuenta los vuelve un lastre
    # permanente. Con ellos adentro, business_audit marcaba 67% y NO PUNTUABA, aunque el
    # 80% de los que compiten ya la había rendido.
    _muertos = {
        (c["id"], c.get("name", k))
        for k, c in MODELS.items()
        if c.get("retired") or c.get("provider_variant")
    }
    _nombres_muertos = {n for _, n in _muertos}

    def _compite(key):
        if isinstance(key, tuple):
            return key not in _muertos and key[1] not in _nombres_muertos
        return True  # by_id: sin nombre no se puede desambiguar; no filtramos

    _cov = suite_coverage(by_id_and_name if by_id_and_name else by_id, _compite)
    low_coverage = {s for s, c in _cov.items() if c < MIN_SUITE_COVERAGE}
    # niah/security/tool_calling ya se excluyen por otras razones — no hace falta
    # duplicar el aviso por ellas.
    _already = {s for s in low_coverage
                if s.startswith("niah") or s.startswith("prompt_injection") or s == "tool_calling"}
    _new = sorted(low_coverage - _already)
    if _new:
        print("  ⚠️  Suites EXCLUIDAS del score por cobertura insuficiente "
              f"(<{MIN_SUITE_COVERAGE:.0%} de los modelos rankeados):")
        for s in _new:
            print(f"       · {s:<22} {_cov[s]:.0%} de cobertura — se reporta, no puntúa")
        print("     (entran al score cuando las corra suficiente gente; si no, "
              "castigarían al que las rinde primero)")

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

        # Normalizar costo de cada run a precios OpenRouter para comparabilidad.
        # Si no hay equivalente OpenRouter, usamos el costo real del provider
        # como aproximacion estandar (todos los modelos deben tener un costo).
        # Los modelos gratis/free tier reciben un costo minimo de $0.001/call
        # para evitar cost_score 10.0 artificial.
        or_cfg = _openrouter_config_for(cfg, or_lookup)
        for r in runs:
            if or_cfg is not None:
                cost_norm = _estimate_cost_openrouter(r, or_cfg)
            else:
                cost_norm = r.get("cost_usd") or 0.0
            cost_norm = max(cost_norm, MIN_COST_PER_CALL)
            r["_cost_usd_or"] = cost_norm
            r["_cost_score_or"] = cost_score_log(cost_norm)

        metrics = aggregate_metrics(runs, low_coverage) if runs else {
            "runs": 0,
            "total_runs": 0,
            "score_global": None,
            "score_by_pillar": {},
            "dims_by_pillar": {},
            "score_by_suite": {},
            "quality_ci95": None,
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

        # Exámenes incompletos que SÍ alimentan la calidad. Los pilares aparte (contexto
        # largo, seguridad) no cuentan acá: su score se reporta por separado y un examen
        # incompleto ahí se marca «no medido», no contamina el ranking.
        _PILARES_APARTE = ("niah", "prompt_injection")
        _incompletas_que_puntuan = {
            s: i for s, i in (metrics.get("suites_incompletas") or {}).items()
            if not s.startswith(_PILARES_APARTE)
        }

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
            "tested": metrics["runs"] >= MIN_RUNS_TESTED,  # cobertura suficiente para reportar
            # RANKEABLE = muestra sólida Y que todavía se pueda usar.
            #
            # Un modelo retirado por el proveedor NO es un candidato: el ranking existe
            # para ayudar a DECIDIR, y recomendar algo que no se puede llamar es el peor
            # fallo posible. Detectado el 13-jul-2026 en el backfill: 5 modelos devuelven
            # "deprecated" / "No endpoints found" en los 10 tests. Uno de ellos, Devstral
            # Small, estaba **#5 del ranking** — alguien lo habría integrado y se estrella.
            #
            # Se siguen exportando (los datos históricos valen: 161 runs de Devstral
            # alimentan el análisis de dispersión), pero fuera del ranking y de las
            # recomendaciones. Ver `retired` en models.py.
            "retired": bool(cfg.get("retired")),
            # Rankeable = muestra sólida, endpoint vivo, y medido en el PLANO COMÚN.
            # Una `provider_variant` (el mismo modelo servido por NIM/Groq/Ollama Cloud)
            # queda fuera: su velocidad y su latencia son de esa infra, no del modelo, y
            # dejarla competir haría que un modelo se enfrente a sí mismo en dos puestos.
            # Sus datos NO se borran — alimentan la comparación entre proveedores.
            "provider_variant": bool(cfg.get("provider_variant")),
            # Self-hosted: corre en la máquina del autor (DGX Spark, llama-server, Ollama).
            # Su velocidad es la de ESE hardware, no la del modelo. Compararlo en la misma
            # tabla que un modelo servido por un datacenter es el mismo error que mezclar
            # Groq (379 tok/s) con NIM (43 tok/s): no comparás modelos, comparás máquinas.
            # Responde otra pregunta —"¿puedo correrlo yo?"— y va en su propia tabla.
            "self_hosted": bool(cfg.get("self_hosted")),
            # EXAMEN INCOMPLETO ⟹ NO COMPITE.
            #
            # Un modelo que rindió 4 de los 10 tests de una suite tiene un promedio sacado
            # de otro examen. Publicarlo al lado de quien rindió los 10 no es comparar:
            # es inventar. Publiqué "MiniMax M3 audita mejor que Opus (8.24 vs 6.94)" y en
            # los 4 tests que ambos rindieron, Opus GANABA 10 a 9.
            #
            # Antes eso se publicaba igual. Ahora el modelo sale del ranking y se muestra
            # como «en evaluación» hasta que complete. Decir "todavía no sé" es honesto;
            # publicar un número que no se sostiene, no.
            #
            # Los pilares aparte (contexto largo, seguridad) NO bloquean: no alimentan la
            # calidad. Ahí el examen incompleto se marca «no medido» en ESE pilar.
            "examen_incompleto": bool(_incompletas_que_puntuan),
            "ranked": (
                metrics["runs"] >= MIN_RUNS_RANKED
                and not cfg.get("retired")
                and not cfg.get("provider_variant")
                and not cfg.get("self_hosted")
                and not _incompletas_que_puntuan
            ),
            "sample_tier": sample_tier(metrics["runs"]),   # solid | partial | preliminary
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
    # Las norm_stats se calculan sobre modelos con base solida (>=MIN_RUNS_RANKED)
    # para que el z-score no se distorsione por emergentes con alta varianza.
    _stable = [m for m in _tested if m["ranked"]]
    # (1) Referencia FRESCA desde la población viva. Es la semilla de una
    #     recalibración; si hay referencia congelada, se descarta más abajo.
    _fresh_norm = {}
    for col in Z_COLS:
        vals = [m[col] for m in _stable]
        mu = _st.mean(vals) if vals else 0.0
        sd = _st.pstdev(vals) if len(vals) > 1 else 1.0
        _fresh_norm[col] = {"mean": round(mu, 4), "std": round(sd if sd > 0 else 1.0, 4)}
    # norm_stats POR PILAR: para recomponer el score de un pilar con los pesos del
    # usuario hay que z-scorear dentro de ese pilar (la media/std de calidad en
    # Coding no es la misma que en Contenido). Se calculan sobre los `ranked`.
    _pillar_names = sorted({p for m in _stable for p in (m.get("dims_by_pillar") or {})})
    _fresh_pillar = {}
    for p in _pillar_names:
        stats_p = {}
        for col in Z_COLS:
            vals = [m["dims_by_pillar"][p][col] for m in _stable
                    if m.get("dims_by_pillar", {}).get(p, {}).get(col) is not None]
            if len(vals) > 1:
                mu = _st.mean(vals)
                sd = _st.pstdev(vals)
                stats_p[col] = {"mean": round(mu, 4), "std": round(sd if sd > 0 else 1.0, 4)}
        if stats_p:
            _fresh_pillar[p] = stats_p

    # (2) ¿Referencia CONGELADA o VIVA? Con --recalibrate se ignora el archivo y se
    #     usa (y persiste) la fresca. Sin archivo se cae al z-score vivo histórico.
    _frozen = None if recalibrate else _load_scoring_reference()
    _frozen_rescale = None
    if _frozen:
        norm_stats = _frozen["norm_stats"]
        norm_stats_by_pillar = _frozen["norm_stats_by_pillar"]
        _frozen_rescale = _frozen.get("score_rescale")
        scoring_version = _frozen.get("version")
        _score_method = _frozen.get("score_method", "zscore_frozen_v4")
    else:
        norm_stats = _fresh_norm
        norm_stats_by_pillar = _fresh_pillar
        _score_method = "zscore_frozen_v4" if recalibrate else "zscore_v2.9_live"
        if not recalibrate:
            print("⚠️  scoring_reference.json ausente → z-score VIVO (inestable, caduca al "
                  "medir). Corré --recalibrate --scoring-version vX.Y para congelar.")

    _wmap = {"quality_avg": DEFAULT_WEIGHTS["quality"], "cost_score_avg": DEFAULT_WEIGHTS["cost"],
             "speed_score_avg": DEFAULT_WEIGHTS["speed"], "latency_score_avg": DEFAULT_WEIGHTS["latency"]}
    # Pasada 1: z compuesto de cada modelo contra la referencia ACTIVA (frozen o viva).
    _zs = {}
    for m in models_export:
        if not _have(m):
            continue
        _zs[id(m)] = sum(w * ((m[col] - norm_stats[col]["mean"]) / norm_stats[col]["std"])
                         for col, w in _wmap.items())
    # Rescale: con referencia congelada usamos SU offset/slope (estable); si estamos
    # recalibrando (o sin archivo), la pendiente se decide mirando la población.
    # Pendiente base 3.3 (z=0 → 5.5; top ~z 0.9 → ≈8.4), PERO si el peor ranked cae
    # bajo 0.5 se comprime para que aterrice en 0.5 en vez de clampearse: con clamp
    # duro en 0, modelos reales terminaban EMPATADOS en 0.00 — un score que ya no
    # ordena ni informa. El piso 0.5 preserva el orden en la cola.
    _OFFSET, _FLOOR = 5.5, 0.5
    if _frozen_rescale:
        _OFFSET = _frozen_rescale.get("offset", 5.5)
        _slope = _frozen_rescale.get("slope", 3.3)
    else:
        _z_ranked_min = min((z for m, z in ((m, _zs.get(id(m))) for m in models_export)
                             if z is not None and m.get("ranked")), default=None)
        _slope = 3.3
        if _z_ranked_min is not None and _z_ranked_min < 0:
            _slope = min(3.3, (_OFFSET - _FLOOR) / abs(_z_ranked_min))
    for m in models_export:
        z_comp = _zs.get(id(m))
        if z_comp is None:
            continue
        m["score_global_linear"] = m.get("score_global")  # guardar el lineal por referencia
        m["score_global"] = round(max(0.0, min(10.0, _OFFSET + _slope * z_comp)), 2)

    # (3) Persistir la referencia SOLO en recalibración deliberada (evento de versión).
    if recalibrate:
        _persist_scoring_reference(norm_stats, norm_stats_by_pillar,
                                   {"offset": _OFFSET, "slope": round(_slope, 4)},
                                   scoring_version)

    # Sort: ranked (muestra solida) primero, luego tested, luego score desc.
    # Asi cualquier consumidor que tome los primeros N del array obtiene un
    # ranking valido sin tener que conocer los umbrales.
    models_export.sort(key=lambda m: (not m["ranked"], not m["tested"], -(m.get("score_global") or 0)))

    return {
        "generated_at": __import__("datetime").datetime.now().isoformat(timespec="seconds"),
        "total_models": len(models_export),
        "tested_count": sum(1 for m in models_export if m["tested"]),
        "ranked_count": sum(1 for m in models_export if m["ranked"]),
        # Umbrales explicitos: el consumidor no deberia adivinarlos ni hardcodearlos.
        "thresholds": {"tested_min_runs": MIN_RUNS_TESTED, "ranked_min_runs": MIN_RUNS_RANKED},
        "tokens_per_call_assumption": {"input": 300, "output": 1500},
        "default_weights": DEFAULT_WEIGHTS,  # los pesos aplicados en score_global
        # score_global = rescale(Σ w·z(dim)). La referencia (norm_stats + rescale) se
        # CONGELA por versión: no se mueve al medir un modelo nuevo. Ver scoring_reference.json.
        "score_method": _score_method,
        "scoring_version": scoring_version,  # etiqueta de la referencia congelada activa
        "norm_stats": norm_stats,  # mean/std por dimensión (para replicar el z-score en la calculadora)
        # mean/std por dimensión DENTRO de cada pilar → la calculadora puede
        # componer "pilar X con MIS pesos" en vez de servir un score pre-horneado.
        "norm_stats_by_pillar": norm_stats_by_pillar,
        # display = clamp(offset + slope·z_comp, 0, 10). La pendiente puede comprimirse
        # (< 3.3) para que el peor ranked aterrice en 0.5 y no se aplaste contra 0.
        "score_rescale": {"offset": _OFFSET, "slope": round(_slope, 4)},
        "subscriptions_catalog": SUBSCRIPTIONS,  # catálogo completo de suscripciones disponibles
        "models": models_export,
    }


def main():
    import argparse
    ap = argparse.ArgumentParser(description="Exporta models.json para el sitio del benchmark.")
    ap.add_argument("--recalibrate", action="store_true",
                    help="Recalcula y CONGELA la referencia de scoring (evento de versión).")
    ap.add_argument("--scoring-version", default=None,
                    help="Etiqueta de versión a estampar (obligatoria con --recalibrate).")
    a = ap.parse_args()
    if a.recalibrate and not a.scoring_version:
        ap.error("--recalibrate requiere --scoring-version vX.Y (ej. v4.0)")
    out_path = Path(__file__).parent.parent / "docs" / "data" / "models.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    export = build_export(recalibrate=a.recalibrate, scoring_version=a.scoring_version)
    out_path.write_text(json.dumps(export, indent=2, ensure_ascii=False))
    print(f"OK escrito: {out_path}")
    print(f"  Total modelos: {export['total_models']}")
    print(f"  Con cobertura (≥20 runs): {export['tested_count']}")


if __name__ == "__main__":
    main()
