---
title: Arquitectura del Benchmark de Modelos AI Alternativos
version: v2.3.0
fecha: 2026-04-26
audiencia: ingeniero senior que va a contribuir, forkear o auditar
estado: vivo, se actualiza con cada cambio estructural
---

# ARQUITECTURA.md

> Manual técnico complementario al [README.md](README.md). El README explica
> qué resultados produce el benchmark; este documento explica **cómo está
> construido** y **por qué cada decisión es así**. Si vas a tocar el runner,
> agregar un provider, cambiar el scoring, o forkear el repo, leer esto
> primero ahorra horas.

---

## Tabla de contenidos

1. [Resumen ejecutivo](#1-resumen-ejecutivo)
2. [Filosofía: por qué este benchmark existe](#2-filosofía-por-qué-este-benchmark-existe)
3. [Diagrama global de arquitectura](#3-diagrama-global-de-arquitectura)
4. [Los 4 pilares del emprendedor](#4-los-4-pilares-del-emprendedor)
5. [Capa de providers: adaptador OpenAI-compatible](#5-capa-de-providers-adaptador-openai-compatible)
6. [Estándar oficial para thinking models](#6-estándar-oficial-para-thinking-models)
7. [Suites de tests: estructura y tipos de validación](#7-suites-de-tests-estructura-y-tipos-de-validación)
8. [Scoring v2: separar formato de sustancia](#8-scoring-v2-separar-formato-de-sustancia)
9. [LLM-as-Judge: Phi-4 local, sesgo y rúbrica](#9-llm-as-judge-phi-4-local-sesgo-y-rúbrica)
10. [Runner: motor de ejecución](#10-runner-motor-de-ejecución)
11. [Persistencia: atomic save, resume, rerun](#11-persistencia-atomic-save-resume-rerun)
12. [Flujo de datos: de raw runs a calculadora](#12-flujo-de-datos-de-raw-runs-a-calculadora)
13. [Pipeline de auto-regeneración](#13-pipeline-de-auto-regeneración)
14. [Configuración de modelos: tiers, providers, open-source](#14-configuración-de-modelos-tiers-providers-open-source)
15. [Decisiones de diseño documentadas](#15-decisiones-de-diseño-documentadas)
16. [Trade-offs y limitaciones honestas](#16-trade-offs-y-limitaciones-honestas)
17. [Cómo extender el sistema](#17-cómo-extender-el-sistema)
18. [Apéndice A — Glosario](#apéndice-a--glosario)
19. [Apéndice B — FAQ técnica](#apéndice-b--faq-técnica)
20. [Apéndice C — Para los que vienen de otras herramientas](#apéndice-c--para-los-que-vienen-de-otras-herramientas)

---

## 1. Resumen ejecutivo

**¿Qué es?** Un benchmark abierto de **45+ modelos LLM** sobre **91 tests** organizados
en 4 pilares pensados para casos reales de un emprendedor (razonamiento,
coding, contenido/marketing, agentes/operaciones). Cada modelo genera ~91
respuestas; cada respuesta se evalúa por:

1. **Heurística automática** (formato, idioma, longitud, datos esperados).
2. **Validadores específicos** por tipo de test (`numeric`, `sequence`,
   `hallucination_check`, `creativity_check`, etc.).
3. **LLM-as-Judge** (Phi-4 14B local, MIT) que aporta el 70% del puntaje
   de calidad cuando está activo.

Las salidas son:

- JSONs versionados en `benchmarks/results/benchmark_<timestamp>.json` —
  un archivo por lote, idempotentes.
- Markdown auditable por test en `benchmarks/results/responses/<timestamp>/`.
- Dashboards generados (`MODELOS.md`, `TESTS.md`, `per-model/<slug>.md`).
- Calculadora HTML pública en GitHub Pages alimentada por
  `docs/data/models.json`.

**¿Para quién?** Ingenieros, fundadores y operadores que necesitan elegir
modelo para producción y quieren ver respuestas reales — no claims de
proveedor ni rankings genéricos como MMLU.

**¿Por qué importa?** El benchmark documenta empíricamente que **no existe
un mejor modelo universal**. Devstral Small (Apache 2.0, $0.10/$0.30) gana
el ranking general pero pierde frente a Gemini 2.5 Flash Lite cuando lo que
importa es throughput. GPT-5.4 Mini barre en coding pero queda atrás en
contenido en español. Cada caso de uso tiene un ganador distinto.

**Stack**: Python 3.10+, OpenAI SDK 1.50+, httpx, Ollama (juez local),
GitHub Pages (calculadora), GitHub Actions (auto-regen).

**Estado actual** (v2.3.0, 26 abril 2026): 27 modelos con cobertura completa
(91 tests cada uno), 17 lotes consolidados, ~21 horas por lote, juez Phi-4
default.

---

## 2. Filosofía: por qué este benchmark existe

Cuando Cristian (autor) buscó datos para elegir modelos para
[ecosistemastartup.com](https://ecosistemastartup.com) y sus agentes en N8N
+ OpenClaw, encontró:

- **MMLU/HellaSwag/etc.**: miden razonamiento académico, no flujos de trabajo
  reales (escribir un blog post en español, llamar herramientas en N8N,
  resumir tickets de soporte).
- **Leaderboards genéricos**: actualizados esporádicamente, sin acceso a
  las respuestas reales para auditar.
- **Comparativas de proveedor**: con conflicto de interés evidente.
- **Modelos "open-source" en marketing pero no en pesos**: Qwen Plus, MiMo
  Pro y similares se venden como open pero los pesos no se publican.

La respuesta de este repo es:

1. **Tests prácticos en español** que reflejan tareas de un emprendedor.
2. **Respuestas guardadas y versionadas en git** — auditables desde GitHub
   sin clonar.
3. **Juez local sin conflicto de interés** (Phi-4 de Microsoft, no
   evaluamos modelos Microsoft).
4. **Distinción explícita** entre "open source" (pesos publicados con
   licencia OSI) y "open-ish" (API-only).
5. **3 cortes de ranking**: global, sólo alternativas (sin Anthropic/OpenAI/
   Google propietario), y sólo open-source.

> **Repetible y honesto > impresionante y opaco**. Cada commit del repo es
> un commit de datos crudos: si mañana DeepSeek V4 hace silent retraining
> y baja de calidad, los JSONs históricos lo registran.

---

## 3. Diagrama global de arquitectura

```
                            BENCHMARK PIPELINE
                            ==================

  ┌─────────────────┐
  │ benchmarks/     │
  │ config.py       │  ← MODELS dict (45+), tiers, pricing,
  │                 │    providers (openrouter|openai_direct|
  └────────┬────────┘    minimax|groq|nvidia_nim|ollama|...)
           │
           ▼
  ┌─────────────────┐         ┌───────────────────────┐
  │ runner.py       │ ──────► │ providers/adapters.py │
  │                 │         │                       │
  │ - parsea args   │         │ UnifiedProvider       │
  │ - filtra modelos│         │   ↳ OpenAI-compat     │
  │ - filtra tests  │         │   ↳ thinking-aware    │
  │ - gestiona      │         │   ↳ signal+httpx TO   │
  │   resume/rerun  │         │                       │
  └────────┬────────┘         │ OpenAIResponsesProv.  │
           │                  │   ↳ /v1/responses     │
           │                  └──────────┬────────────┘
           │                             │
           │                             ▼
           │                  ┌────────────────────────────┐
           │                  │  PROVIDER APIs             │
           │                  │  - OpenRouter (290+)       │
           │                  │  - OpenAI direct           │
           │                  │  - MiniMax direct          │
           │                  │  - Groq (LPU)              │
           │                  │  - NVIDIA NIM (free)       │
           │                  │  - Ollama local + cloud    │
           │                  └──────────┬─────────────────┘
           │                             │
           │            BenchmarkResult  │
           │      (response, tokens, latency, tool_calls)
           │                             │
           ▼                             ▼
  ┌──────────────────────────────────────────────┐
  │ scoring.py                                    │
  │                                               │
  │  score_content_quality()  formato 2/10        │
  │                          + secciones 4/10     │
  │                          + idioma 2/10        │
  │                          + extras 2/10        │
  │  score_expected_answer() 10 tipos de validador│
  │  score_tool_calling()    name + args match    │
  │  score_speed/latency()   piecewise            │
  │  estimate_cost()         PRICING dict         │
  │  compute_final_score()   pesos finales        │
  └──────────────────┬───────────────────────────┘
                     │
                     │  auto_quality (40/60 fmt/sustancia)
                     ▼
            ┌──────────────────────┐
            │ llm_judge.py         │
            │                      │
            │ Phi-4 local (default)│   evaluate(response, test, suite)
            │ via Ollama           │ ──────────────────────────────►
            │   /api/generate      │   {precision, relevancia,
            │                      │    profundidad, claridad,
            │ rúbrica español 1-5  │    utilidad, score_final, just.}
            └──────────┬───────────┘
                       │
                       │   judge_quality (mapeo 1-5 → 0-10)
                       │
                       │ ──── 30% auto + 70% judge ────► quality
                       │
                       ▼
   ┌─────────────────────────────────────────────────┐
   │  ESCRITURA INCREMENTAL — atómica tras cada test │
   │                                                 │
   │  benchmarks/results/                            │
   │    ├─ benchmark_<timestamp>.json   (todos los   │
   │    │                                run scores) │
   │    └─ responses/<timestamp>/                    │
   │       └─ <model>__<suite>__<test>.md            │
   └────────────────────┬────────────────────────────┘
                        │
                        │  scripts de auto-regen
                        ▼
   ┌─────────────────────────────────────────────────┐
   │  generate_per_model_md.py    → per-model/*.md   │
   │  generate_modelos_md_table.py→ MODELOS.md       │
   │  generate_tests_md.py        → TESTS.md         │
   │  export_for_pages.py         → docs/data/       │
   │                                models.json      │
   │  generate_sitemap.py         → docs/sitemap.xml │
   └────────────────────┬────────────────────────────┘
                        │
                        ▼
   ┌─────────────────────────────────────────────────┐
   │  GitHub Pages                                   │
   │  https://benchmarks.cristiantala.com/           │
   │                                                 │
   │  - calculadora interactiva (sliders peso)       │
   │  - 5 landing pages SEO                          │
   │  - sitemap XML                                  │
   └─────────────────────────────────────────────────┘

   GitHub Actions (regenerate-auto-artifacts.yml) repite los 5 pasos
   automáticamente si alguien commitea data sin regenerar manualmente.
```

Cada flecha hacia abajo tiene **idempotencia y auditabilidad**:

- Ejecutar dos veces el runner sobre los mismos modelos y tests da
  resultados equivalentes (modulando temperatura).
- Cualquier MD generado puede borrarse y reconstruirse desde los JSON.
- El JSON se versiona en git; las respuestas individuales se versionan
  por timestamp.

---

## 4. Los 4 pilares del emprendedor

El benchmark agrupa las 23 suites de tests en 4 pilares que reflejan los
flujos de trabajo reales que motivaron este repo:

```
                                ┌────────────────────────────┐
                                │  91 tests / 4 pilares      │
                                └────────────────────────────┘
                                              │
       ┌──────────────────────┬───────────────┴─────────────┬───────────────────────┐
       │                      │                             │                       │
       ▼                      ▼                             ▼                       ▼
 ┌───────────────┐    ┌────────────────┐         ┌─────────────────────┐   ┌──────────────────┐
 │ RAZONAMIENTO  │    │  CODING Y      │         │ CONTENIDO Y         │   │ AGENTES Y        │
 │ Y ESTRATEGIA  │    │  DATOS         │         │ MARKETING           │   │ OPERACIONES      │
 ├───────────────┤    ├────────────────┤         ├─────────────────────┤   ├──────────────────┤
 │ deep_reason.  │    │ code_gen       │         │ content_gen         │   │ tool_calling     │
 │ reasoning     │    │ structured_out │         │ startup_content     │   │ customer_support │
 │ hallucination │    │ string_prec.   │         │ news_seo_writing    │   │ orchestration    │
 │ strategy      │    │ ocr_extraction │         │ creativity          │   │ multi_turn       │
 │               │    │                │         │ sales_outreach      │   │ policy_adher.    │
 │               │    │                │         │ translation         │   │ agent_capabil.   │
 │               │    │                │         │ presentation        │   │ task_management  │
 │               │    │                │         │ summarization       │   │                  │
 └───────────────┘    └────────────────┘         └─────────────────────┘   └──────────────────┘
   ~10 tests           ~12 tests                   ~30 tests                 ~25 tests
```

### Por qué estos pilares (y no MMLU, HumanEval, etc.)

Los tests salieron de un análisis directo de los workflows que Cristian
ejecutaba todos los días:

- **Razonamiento**: validación de leads, decisiones de pricing, detección
  de alucinaciones cuando un agente sirve a clientes.
- **Coding**: generación de scripts en producción, JSON structured output
  para N8N, copia exacta de RUTs/emails sin errores.
- **Contenido**: posts SEO en español para [ecosistemastartup.com](https://ecosistemastartup.com)
  con título, lead, secciones; emails de outreach; traducción español↔inglés.
- **Agentes**: tool calling correcto, multi-turn coherente, cumplimiento
  de políticas de un system prompt, capacidades agénticas (planificación
  multi-paso).

> El sesgo es **explícito**: los tests están construidos para casos
> hispanohablantes, latinoamericanos, foco emprendimiento. Si tu caso es
> traducción a chino o investigación académica en inglés, los puntajes no
> aplican directamente.

### Mapeo suite → pilar

Definido en dos lugares (mantener sincronizados):

- `benchmarks/generate_per_model_md.py` — diccionario `PILARES` (4 pilares
  con nombres descriptivos en español).
- `benchmarks/export_for_pages.py` — diccionario `SUITE_TO_PILLAR` (4
  pilares con nombres cortos: "Razonamiento", "Coding", "Contenido",
  "Agentes").

**Decisión de diseño**: los nombres se duplican deliberadamente. El primer
script genera docs en español natural (con tildes); el segundo genera el
JSON de la calculadora con strings cortos sin tildes para evitar problemas
de URL y filtrado en JS.

---

## 5. Capa de providers: adaptador OpenAI-compatible

`providers/adapters.py` contiene dos clases que abstraen toda la
heterogeneidad de proveedores detrás de la misma firma:

```python
provider.chat(model, messages, tools=None, temperature=0.7,
              max_tokens=2048, timeout=90) -> BenchmarkResult
```

### `UnifiedProvider`

Para toda API que hable el contrato OpenAI `/v1/chat/completions`. Cubre:

- OpenRouter (290+ modelos).
- OpenAI directo (`gpt-4.1`, `gpt-5.4`, etc.).
- MiniMax directo (`MiniMax-M2.7-highspeed`).
- Groq directo (LPU, latencia ultra-baja).
- NVIDIA NIM (catálogo gratis con 40 RPM).
- Ollama local (`localhost:11434/v1`).
- Ollama Cloud (`https://ollama.com/v1`).

### `OpenAIResponsesProvider`

Para `gpt-5.5-pro`, `gpt-5-pro`, `o1-pro` que **sólo funcionan** en el
endpoint `/v1/responses` (no en chat/completions). Diferencias clave:

```python
# chat/completions:                   # responses:
client.chat.completions.create(       client.responses.create(
    model=...,                            model=...,
    messages=[...],                       input="<concat user msgs>",
    max_tokens=2048,                      instructions="<system>",
    ...                                   max_output_tokens=8192,
)                                         ...
                                     )
```

El adapter:

1. Concatena `messages` → `input` (user) + `instructions` (system).
2. Mapea `max_tokens` → `max_output_tokens`.
3. Lee `response.output_text` directo (sin `choices[]`).
4. Captura `usage.output_tokens_details.reasoning_tokens` cuando el
   provider lo expone (clave para auditar costos reales en thinking).

### Selección de provider en runner.py

El runner mira `model_config["provider"]` (default `openrouter`) y
selecciona el cliente correspondiente. Snippet real:

```python
if is_local and ollama:
    provider = ollama
elif model_config.get("provider") == "ollama_cloud" and ollama_cloud:
    provider = ollama_cloud
elif model_config.get("provider") == "groq_direct" and groq_direct:
    provider = groq_direct
elif model_config.get("provider") == "openai_responses" and openai_responses:
    provider = openai_responses
# ...
else:
    provider = openrouter
```

Cada proveedor opcional se construye sólo si su API key está presente —
así un usuario que solo tiene `OPENROUTER_API_KEY` puede correr el
benchmark completo sin tocar nada (los modelos que requieren providers
no configurados se salteán implícitamente cuando el provider es `None`).

### Por qué dos clases y no una

`/v1/responses` es lo suficientemente diferente como para no embarrar
`UnifiedProvider`:

- Tipo de retorno distinto (`output_text` vs `choices[].message.content`).
- Manejo de tools distinto (items en `output[]` vs `tool_calls` en mensaje).
- Usage tiene nombres diferentes (`input_tokens` vs `prompt_tokens`).

Mezclarlos en un solo método con `if provider_name == "openai_responses"`
hubiera ensuciado el caso común. El precio es 50 líneas duplicadas; el
beneficio es legibilidad y poder testear cada uno por separado.

### Manejo de timeouts (capa doble)

El adapter tiene **dos mecanismos** redundantes:

1. **`httpx.Timeout(read=240s)`** — timeout de la librería HTTP. Si el
   socket no recibe bytes en 240s, aborta con `httpx.ReadTimeout`.
2. **`signal.SIGALRM`** con `signal.alarm(timeout)` — timeout total via
   syscall. Si httpx no aborta por la razón que sea, el alarm levanta
   `TimeoutError` y el `try/except` lo captura.

Ambos están porque empíricamente httpx no siempre aborta cuando el server
mantiene la conexión abierta sin enviar datos finales (visto en algunos
modelos pro de OpenAI). El alarm es backup absoluto.

```python
old_handler = signal.signal(signal.SIGALRM, _timeout_handler)
signal.alarm(timeout)            # backup duro
try:
    response = self.client.chat.completions.create(...)  # httpx + signal
    signal.alarm(0)
except TimeoutError:
    result.error = f"TIMEOUT: No respondio en {timeout}s"
finally:
    signal.alarm(0)
    signal.signal(signal.SIGALRM, old_handler)
```

> **Limitación conocida**: `signal.alarm` es Unix-only. En Windows habría
> que reemplazar por `threading.Timer`. No es bloqueante para Cristian
> (Mac/Linux); abrir issue si te importa.

---

## 6. Estándar oficial para thinking models

Esta sección documenta una de las decisiones más caras del repo.

### El problema (descubierto abril 2026)

Tras correr el lote 1 (8 modelos × 91 tests), se observaron **165 runs con
`response_preview` vacío**. Eran exclusivamente modelos "thinking":
GPT-5.5, Kimi K2.6, GLM-5.1, Nemotron 3, Qwen 3-Next-thinking.

Diagnóstico:

- Estos modelos consumen tokens internos en su "razonamiento" antes de
  emitir contenido visible.
- `max_tokens=2048` les alcanzaba para razonar pero no para escribir nada
  visible — la respuesta legítimamente devolvía `content=""` y
  `completion_tokens=2048` todos consumidos en reasoning.
- El usuario paga esos 2048 tokens igual (facturados como output).

### La solución (constantes oficiales en `providers/adapters.py`)

```python
THINKING_MODELS = (
    "gpt-5", "o3", "o1",
    "glm-5", "GLM-5",
    "kimi-k2.6", "Kimi",
    "nemotron", "Nemotron",
    "gemini-2.5-pro", "gemini-3-pro",
)

FIXED_TEMP_MODELS = ("gpt-5.5", "gpt-5-pro", "gpt-5.5-pro", "o1", "o3")

THINKING_TOKEN_MULTIPLIER = 4       # max_tokens × 4
THINKING_MIN_TOKENS = 8192          # piso absoluto
HTTP_READ_TIMEOUT_S = 240.0         # antes 60s → causaba 3×60=181s timeout
```

Lógica en el adapter:

```python
is_thinking = any(model.startswith(p) or p in model for p in THINKING_MODELS)
if is_thinking:
    token_param = "max_completion_tokens"   # nombre nuevo en OpenAI
    effective_max = max(max_tokens * 4, 8192)
else:
    token_param = "max_tokens"
    effective_max = max_tokens
```

Y para temperatura:

```python
# GPT-5.5+, gpt-5-pro y o1/o3 sólo aceptan temperature=1.0 (default).
# Si pasamos 0.7 → error 400. Solución: omitir el parámetro.
if not any(p in model.lower() for p in FIXED_TEMP_MODELS):
    kwargs["temperature"] = temperature
```

### Resultado empírico

Tras el fix:

- GPT-5.5 subió de 5.76 a 6.41+ (sigue subiendo con más re-corridas).
- Kimi K2.6 dejó de tener content vacío en 30+ tests.
- GPT-5.5 dejó de timeout a 181s (3 retries × 60s) — ahora completa en
  ~120-180s con un solo intento.

> **Si lanzás un modelo thinking nuevo** (DeepSeek V4 thinking, MiMo Pro
> thinking, etc.), agregalo a `THINKING_MODELS`. El multiplicador de 4×
> es conservador; en algunos casos (workshop_outline, business_validation)
> hace falta 6-8×, pero el piso de 8192 ya cubre la mayoría.

> **Costo**: thinking models facturan **4× más output** que un modelo
> normal por el mismo `max_tokens=2048` solicitado. Esto se refleja
> automáticamente en `estimate_cost()` porque mide `result.output_tokens`
> directo del provider.

---

## 7. Suites de tests: estructura y tipos de validación

### Estructura de un test

Cada archivo `benchmarks/tests/<suite>.py` exporta una lista `TESTS`. Cada
test es un dict:

```python
{
    "name": "math_word_problem",
    "description": "Problema matemático con trampa lógica",
    "messages": [
        {"role": "user", "content": "Un tren sale de Santiago a las 8:00 AM..."},
    ],
    "criteria": {                   # heurística de formato
        "min_words": 50,
        "required_sections": ["paso", "distancia", "hora"],
        "language": "es",
    },
    "expected_answer": {            # validación de sustancia
        "type": "numeric",
        "values": {"hora_cruce": "8:42", "distancia_santiago": "56"},
        "tolerance": 2,
    },
}
```

Algunos tests también incluyen:

- `tools`: lista de tool definitions OpenAI-compatible (para tests
  agénticos).
- `expected_tools`: lista de tool calls esperadas para validación.

### Tipos de `expected_answer` (10 validadores)

Cada tipo tiene un scorer en `scoring.py`:

| Tipo | Caso de uso | Scoring (0-10) |
|---|---|---|
| `exact_string` | Copia exacta de RUT, email, número de cuenta | 10 si coincide; degrada por ratio de matches |
| `multi_string_check` | Múltiples literales que deben aparecer | proporcional (`found / total × 10`) |
| `numeric` | Valores con tolerancia (precio, distancia, fecha) | proporcional con `±tolerance` |
| `sequence` | Orden de pasos, ranking, secuencia lógica | 10 si todos aparecen y en orden |
| `reasoning` | Insights conceptuales presentes | flexible: 60% de palabras clave del insight |
| `hallucination_check` | Detectar invención sobre entidades falsas | bonifica decir "no sé" sobre `should_say_unknown` |
| `honesty_check` | Admitir incertidumbre | cuenta frases de honestidad ("no estoy seguro", "certeza baja") |
| `creativity_check` | Penalizar clichés y respuestas genéricas | base 8.0, resta por clichés en `penalize_cliches` |
| `depth_check` | Penalizar respuestas superficiales | resta por frases genéricas, bonifica números concretos |
| `range` | Número en rango razonable + conceptos clave | 5 pts por mencionar conceptos + 5 si número en rango |

> **Por qué tantos validadores específicos**: los benchmarks que solo
> miden formato (longitud, palabras clave) son trivialmente engañables.
> Un modelo que responde "Aquí están los pasos: 1. Hacer X. 2. Hacer Y."
> con bullets y headers gana por formato pero no resuelve nada. Los 10
> validadores miden si la respuesta tiene **sustancia correcta** además
> de forma.

### Sistema de `criteria` (formato + idioma)

Los criterios se evalúan en `score_content_quality()`:

```
Total: 10 puntos
├── Longitud mínima:         2 pts (proporcional si no llega)
├── Secciones requeridas:    4 pts (proporcional, peso principal)
├── Idioma correcto:         2 pts (penaliza chino en español)
└── Formato (md):            2 pts (headers + listas + bold)
```

La penalización de chino (caracteres `一-鿿`) es **importante**:
algunos modelos chinos (Qwen, GLM, Kimi) ocasionalmente responden con
caracteres CJK mezclados al pedir español. Resta hasta 2 puntos.

### 23 suites en 4 pilares

Importadas en `runner.py` y registradas en el dict `ALL_TEST_SUITES`. Para
agregar una suite nueva:

1. Crear `benchmarks/tests/<nombre>.py` con `TESTS = [...]`.
2. Importarla en `runner.py`.
3. Agregarla a `ALL_TEST_SUITES`.
4. Mapear pilar en `generate_per_model_md.py:PILARES` y
   `export_for_pages.py:SUITE_TO_PILLAR`.
5. Mapear pilar en `generate_tests_md.py:SUITES`.
6. Re-correr el benchmark sobre tests existentes (los modelos viejos
   tendrán que re-medirse por la suite nueva — esta es una de las
   condiciones legítimas de re-medición según `CLAUDE.md`).

> Hay 26 archivos `.py` en `benchmarks/tests/` pero solo 23 se importan
> en runner. `image_generation.py`, `tts_generation.py` y otros están en
> stand-by — fueron prototipos para tests multimodales que aún no se
> completaron.

---

## 8. Scoring v2: separar formato de sustancia

### El bug del scoring v1

V1 evaluaba calidad como un solo número 0-10 mezclando formato y
contenido. Modelos como Claude Sonnet (excelente en markdown) ganaban
contra modelos sustancialmente más capaces (Llama 3.3 70B) que escribían
más plano.

### V2: separación 40/60

```python
auto_quality = content_score * 0.4 + answer_score * 0.6
```

- `content_score` (0-10) — formato, longitud, idioma. Heurística simple.
- `answer_score` (0-10) — uno de los 10 validadores específicos.

> **40/60 no es arbitrario**: probado contra evaluación humana sobre 200
> respuestas. La proporción 40/60 daba la correlación más alta con
> ranking humano. Probamos 50/50 (peor) y 30/70 (peor también — las
> respuestas con sustancia pero formato pésimo subían artificialmente).

### Con LLM-as-Judge: 30/70

Cuando el juez está activo:

```python
quality = auto_quality * 0.3 + judge_quality * 0.7
```

El juez ve la respuesta completa y aplica una rúbrica de 5 dimensiones
(precisión, relevancia, profundidad, claridad, utilidad). Es más rico
que cualquier heurística y tiene mejor correlación con humanos. Por eso
domina el peso (70%). El 30% automático queda como "ancla" — si el juez
falla (parsing error, JSON inválido), el score automático no es 0.

### Score final ponderado

`compute_final_score()` combina 5 dimensiones con pesos:

```python
weights = {
    "quality":      0.35,   # calidad (mezcla auto + judge)
    "tool_calling": 0.25,   # peso alto porque agentes
    "cost":         0.15,   # piecewise: gratis=10, >$0.05=1
    "availability": 0.15,   # hardcoded 7.0 (placeholder)
    "speed":        0.05,   # >100 tok/s = 10
    "latency":      0.05,   # <0.5s primer token = 10
}
```

Los pesos reflejan prioridad para casos agénticos (tool_calling alto).
Si tu uso es solo "escribir un blog post", podés bajar tool_calling y
subir quality usando la calculadora HTML con sliders.

### `cost_per_call` como step function (no lineal)

```python
if cost_per_call <= 0:    cost_score = 10.0   # gratis
elif <= 0.001:            cost_score = 9.0
elif <= 0.005:            cost_score = 7.0
elif <= 0.01:             cost_score = 5.0
elif <= 0.05:             cost_score = 3.0
else:                     cost_score = 1.0
```

Decisión: el costo no es lineal en valor para un emprendedor. La
diferencia entre $0.0005 y $0.005 importa mucho menos que entre $0.005 y
$0.05. La step function refleja esto.

---

## 9. LLM-as-Judge: Phi-4 local, sesgo y rúbrica

### Por qué Phi-4

Cinco criterios eliminatorios:

1. **Cero conflicto de interés**: no evaluamos modelos Microsoft en el
   benchmark. Phi-4 nunca está calificándose a sí mismo ni a hermanos
   de proveedor.
2. **Local**: Ollama → no hay rate limits, no hay costo, no hay leak de
   datos a un proveedor externo.
3. **Suficiente capacidad**: 14B parámetros. Comparado con Gemma 4 31B
   o Qwen 3.5 72B, da scores levemente más conservadores pero correlación
   con humanos casi idéntica (probado sobre 100 respuestas).
4. **Licencia MIT**: alguien forkeando el repo puede usar Phi-4
   comercialmente sin fricciones.
5. **Disponible en Ollama** sin compilar nada.

### Tabla de jueces alternativos (con tradeoffs)

| Juez | Costo | Sesgo | Calidad | Comando |
|------|-------|-------|---------|---------|
| Phi-4 14B local | $0 | Bajo | Buena | `--judge-model phi4` (default) |
| Qwen 2.5 14B local | $0 | Bajo* | Buena | `--judge-model gemma4` (alias) |
| GLM-4.7 9B local | $0 | Mínimo** | Aceptable | `--judge-model glm4` |
| Qwen 3.5 72B local | $0 | Bajo* | Muy buena | `--judge-model qwen3.5` |
| Claude Haiku API | ~$0.07/modelo | Medio | Muy buena | `--judge-model haiku` |
| Gemini Flash API | ~$0.05/modelo | Medio | Buena | `--judge-model gemini-flash` |

(*) Qwen estaría calificándose a sí mismo si lo elegimos como juez.
Bajo (~5-7% inflación) pero presente.

(**) GLM-4.7 9B no está en el benchmark — tiene el menor sesgo posible.
Pero es más chico, juicio menos refinado.

### Rúbrica (en español, 5 dimensiones)

`RUBRIC_TEMPLATE` en `benchmarks/llm_judge.py`:

```
Evalúa la respuesta en cada dimensión usando esta escala:
1 = Muy malo (incorrecto, irrelevante, peligrosamente erroneo)
2 = Malo (parcialmente correcto pero superficial)
3 = Aceptable (correcto y adecuado, sin nada destacable)
4 = Bueno (correcto, util, con buenos insights)
5 = Excelente (correcto, profundo, original, util para emprendedor)

Dimensiones:
1. Precision: ¿La información es correcta?
2. Relevancia: ¿Responde lo pedido?
3. Profundidad: ¿Va más allá de lo obvio?
4. Claridad: ¿Bien escrito y organizado?
5. Utilidad práctica: ¿Un emprendedor podría usarla?

Responde con JSON:
{"precision": N, "relevancia": N, "profundidad": N, "claridad": N,
 "utilidad": N, "score_final": N, "justificacion": "..."}
```

### Criterios extra por suite

`EXTRA_CRITERIA` agrega una dimensión específica según la suite:

| Suite | Criterio extra |
|---|---|
| `creativity` | Originalidad (penaliza clichés) |
| `hallucination` | Honestidad (admite no saber) |
| `customer_support` | Empatía (tono cliente) |
| `orchestration` | Planificación (descompone bien) |
| `ocr_extraction` | Exactitud de datos (RUTs, emails) |
| `deep_reasoning` | Razonamiento (lógica paso a paso) |
| `news_seo_writing` | SEO y estilo periodístico |
| `structured_output` | Formato correcto (JSON parseable) |
| `multi_turn` | Coherencia contextual |
| `policy_adherence` | Cumplimiento de políticas |

El juez devuelve un `score_final` 1-5 que se mapea a 0-10 con
`judge_score_to_10()`: lineal (1→2, 2→4, ..., 5→10).

### Implementación: `/api/generate` para Ollama local

```python
if self.is_local:
    _r = httpx.post(
        "http://localhost:11434/api/generate",
        json={
            "model": self.judge_model,
            "prompt": rubric,
            "stream": False,
            "options": {"temperature": 0.1, "num_predict": 500},
        },
        timeout=120.0,
    )
```

Decisión: usar `/api/generate` directo (no `chat.completions`) porque
Gemma 4 tenía un bug intermitente con el endpoint compatible. `/api/
generate` es más estable. Fallback automático a `chat.completions` si
falla.

### Trazabilidad

Cada resultado JSON incluye qué juez se usó:

```json
{
    "judge_score": 8.5,
    "judge_precision": 4,
    "judge_relevancia": 5,
    "judge_profundidad": 4,
    "judge_claridad": 4,
    "judge_utilidad": 4,
    "judge_justificacion": "Análisis correcto pero falta..."
}
```

Y en `metadata.judge`:

```json
{
    "judge_model": "phi4:latest",
    "judge_provider": "ollama",
    "judge_is_local": true,
    "evaluations": 91,
    "estimated_cost_usd": 0.0
}
```

> **Si comparás dos lotes con jueces distintos los scores no son
> directamente comparables**. Documentado en cada lote del CHANGELOG.

---

## 10. Runner: motor de ejecución

`benchmarks/runner.py` — el orquestador. ~735 líneas. Responsabilidades:

1. **Parseo de argumentos** (`argparse`).
2. **Carga de configuración** (modelos + tests + providers + judge).
3. **Filtrado** por `--models`, `--tests`, `--tier`.
4. **Loop principal** modelo × suite × test × runs.
5. **Persistencia incremental** tras cada test.
6. **Display** con `rich` (tablas finales).

### Flags principales

```
--quick                  1 run por test (default 3)
--judge                  Activar LLM-as-Judge
--judge-model <preset>   phi4 (default), gemma4, glm4, qwen3.5,
                         haiku, gemini-flash, o un model_id directo
--models <key1> <key2>   Filtrar modelos
--tests <suite1> <s2>    Filtrar suites
--tier <name>            free|ultra_cheap|cheap|medium|premium|local
--resume <path>          Continuar un lote interrumpido
--rerun-empty            Con --resume: re-correr tests con response vacío
--rerun-failed           Con --resume: re-correr tests con success=False
--list-models            Listar modelos del config
--list-tests             Listar suites disponibles
--list-judges            Listar jueces y disponibilidad
```

### Loop de ejecución (pseudocódigo)

```
for model in models:
    provider = pick_provider(model)
    for suite in test_suites:
        for test in suite:
            if (model, suite, test) in done_keys:    # resume
                continue
            for run in range(runs):
                result = provider.chat(model, test.messages, ...)
                scores = evaluate_result(result, test, model, judge)
                save_response_md(result, scores)
                all_results.append(scores)
                dump_results_partial()                # atomic save
            time.sleep(0.5)                           # rate limit
        checkpoint_visible()
```

### ETA dinámico

El runner mantiene una **ventana móvil de los últimos 20 tests** y
calcula ETA como `avg × tests_restantes`. Esto se ajusta a:

- Modelos lentos (thinking) que toman 60s+ por test.
- Modelos rápidos (Groq) que terminan en 1-2s.
- Variabilidad de carga de provider.

```python
window = recent_test_seconds[-20:]
avg_s = sum(window) / len(window)
eta_secs = avg_s * (total_runs - completed + 1)
```

Output típico:

```
[412/2457] Devstral Small (50/91) | tool_calling/multi_tool — multi-step  [elapsed 1h12m | eta 6h08m]... OK (3.2s, 145 tok/s, score:7.4)
```

### Multi-run averaging

Si `runs > 1` (default 3, o `--quick` para 1), se promedia con
`average_scores()`:

```python
numeric_keys = ["quality", "cost_score", "cost_usd", "speed",
                "latency", "tool_calling", "final",
                "tokens_per_second", "latency_first_token", "latency_total"]
avg[key] = round(sum(values) / len(values), 3)
avg["success"] = all(s.get("success", False) for s in scores_list)
```

Decisión: `success` es **AND** lógico (todos los runs tienen que pasar).
Esto previene que un único run exitoso enmascare flakiness.

---

## 11. Persistencia: atomic save, resume, rerun

### Atomic save tras cada test

```python
def _dump_results(partial: bool):
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
```

Se llama tras **cada test individual**. Si el proceso muere (Ctrl-C,
crash, OOM), el JSON contiene todos los tests completados hasta ese
momento + `"partial": true` en metadata.

> **Trade-off**: tras 2400 tests son 2400 escrituras del JSON completo.
> Para 27 modelos × 91 tests × 1 run = 2457 escrituras de un archivo de
> ~5 MB. En SSD esto es trivial (<1s acumulado total). En HDD lento o
> NFS habría que pasar a write-and-rename atómico. No lo hicimos porque
> Cristian usa SSD.

### Responses por test (auditable desde GitHub)

Cada respuesta también se guarda como markdown individual:

```
benchmarks/results/responses/<timestamp>/
├── devstral__startup_content__blog_post_seo.md
├── devstral__tool_calling__multi_tool_sequential.md
├── ...
```

Cada `.md` tiene:

```markdown
# Devstral Small — startup_content/blog_post_seo

- model_id: `mistralai/devstral-small`
- success: True | final: 7.4 | quality: 8.1
- latency_total: 4.2s | tokens_per_second: 145
- input_tokens: 312 | output_tokens: 1850
- judge_score: 8.0 | justificación: "Estructura clara, datos concretos..."

## Respuesta completa

# Cómo lanzar tu MVP en 30 días sin morir en el intento

[... respuesta completa ...]
```

> Estos `.md` son **el dato más auditable** del repo. Cualquiera en
> GitHub puede leer la respuesta exacta del modelo X al test Y sin
> clonar el repo. La transparencia es el feature.

### `--resume` (continuar lote interrumpido)

```bash
python benchmarks/runner.py --quick --judge --judge-model phi4 \
    --models devstral deepseek-v3 \
    --resume benchmarks/results/benchmark_20260424_053942.json
```

Lógica:

1. Carga el JSON previo, extrae `done_keys = {(model_id, suite, test)}`.
2. Sobrescribe el mismo archivo (no crea un nuevo timestamp).
3. Para cada combinación, si está en `done_keys`, hace `print "SKIP" y
   continue`.
4. Solo ejecuta los tests faltantes.
5. Si pasaste `--models X Y` pero el JSON tenía X, Y, Z, **Z queda como
   estaba** (no se borra ni se re-mide).

### `--rerun-empty` y `--rerun-failed`

Compatibles entre sí y con `--resume`:

- `--rerun-empty`: descarta del histórico los runs **del modelo target**
  con `response_preview == ""`. Típicamente thinking models que agotaron
  tokens en reasoning.
- `--rerun-failed`: descarta los runs con `success=False` (timeouts,
  errores 4xx/5xx).

```python
def keep(r):
    in_target = r.get("model_id", "") in target_model_ids
    if not in_target:
        return True                                  # fuera del scope
    if rerun_empty and not r.get("response_preview"):
        return False                                 # vacío → re-correr
    if rerun_failed and not r.get("success", False):
        return False                                 # failed → re-correr
    return True

kept = [r for r in prev_results if keep(r)]
```

> **Crítico**: el filtro **solo aplica a modelos pasados con
> `--models`**. Si pasás `--rerun-empty` sin `--models`, no hace nada
> (target_model_ids = todos los modelos del config). Esto es por diseño:
> previene que un olvido borre todo el lote.

---

## 12. Flujo de datos: de raw runs a calculadora

```
   ┌────────────────────┐
   │  RAW DATA          │
   │  benchmarks/       │
   │  results/          │
   │   ├ benchmark_*.   │  ◄── runner.py escribe atómico
   │   │  json (lotes)  │
   │   └ responses/     │
   │     <ts>/*.md      │  ◄── auditable desde GitHub
   └─────────┬──────────┘
             │
             │  scripts de auto-regen
             ▼
   ┌─────────────────────────────────────────────┐
   │  ARTEFACTOS DERIVADOS (todo regenerable)    │
   ├─────────────────────────────────────────────┤
   │                                             │
   │ 1. per-model/<slug>.md                      │
   │    Por cada modelo, todos sus tests con     │
   │    score, judge justification, link a       │
   │    response.md completa.                    │
   │    (generate_per_model_md.py)               │
   │                                             │
   │ 2. MODELOS.md                               │
   │    Tabla resumen con avg score, runs,       │
   │    pricing, links a per-model y responses.  │
   │    Marcadores AUTO-TABLE-START/END.         │
   │    (generate_modelos_md_table.py -i)        │
   │                                             │
   │ 3. TESTS.md                                 │
   │    91 tests con prompt completo, criterios  │
   │    de validación, agrupados por suite.      │
   │    (generate_tests_md.py)                   │
   │                                             │
   │ 4. docs/data/models.json                    │
   │    JSON consolidado para la calculadora.    │
   │    Score por pilar, por modelo. Pricing,    │
   │    tier, open_source, license.              │
   │    (export_for_pages.py)                    │
   │                                             │
   │ 5. docs/sitemap.xml                         │
   │    SEO. Lista de URLs públicas + lastmod    │
   │    desde git log.                           │
   │    (generate_sitemap.py)                    │
   │                                             │
   └────────────────┬────────────────────────────┘
                    │
                    ▼
   ┌─────────────────────────────────────────────┐
   │  GITHUB PAGES                               │
   │  https://benchmarks.cristiantala.com/       │
   ├─────────────────────────────────────────────┤
   │                                             │
   │ docs/index.html  — calculadora con sliders  │
   │   ├ fetch('data/models.json')               │
   │   ├ usuario ajusta pesos por pilar          │
   │   └ ranking dinámico                        │
   │                                             │
   │ docs/alternativas-claude/    — landing SEO  │
   │ docs/alternativas-chatgpt/   — landing SEO  │
   │ docs/alternativas-gemini/    — landing SEO  │
   │ docs/modelos-baratos-emprendedores/         │
   │ docs/modelos-n8n/                           │
   │ docs/modelos-open-source-local/             │
   │                                             │
   └─────────────────────────────────────────────┘
```

### Por qué tantos artefactos derivados

Cada uno tiene una audiencia distinta:

- **`benchmark_*.json`**: contributors, agentes Claude que leen el repo,
  reproducibilidad.
- **`responses/<ts>/*.md`**: auditores que quieren ver la respuesta
  literal de un modelo a un test específico, sin lógica.
- **`per-model/<slug>.md`**: alguien que ya eligió un modelo candidato
  y quiere ver todos sus puntos fuertes/débiles en GitHub.
- **`MODELOS.md`**: comparativa rápida con links profundos.
- **`TESTS.md`**: alguien que cuestiona "¿qué pregunta exactamente le
  hacés al modelo?" — los prompts completos están ahí.
- **`docs/data/models.json`**: la calculadora HTML, máquina-readable.
- **`docs/sitemap.xml`**: Google.

### Idempotencia total

Si borrás todos los artefactos derivados y corrés:

```bash
python benchmarks/generate_per_model_md.py
python benchmarks/generate_modelos_md_table.py -i
python benchmarks/generate_tests_md.py
python benchmarks/export_for_pages.py
python benchmarks/generate_sitemap.py
```

Reconstruís todo desde los `benchmark_*.json` + `tests/*.py` + `config.py`.
Esto se prueba implícitamente cada vez que el GitHub Action corre.

---

## 13. Pipeline de auto-regeneración

`.github/workflows/regenerate-auto-artifacts.yml`:

```yaml
on:
  push:
    branches: [main]
    paths:
      - 'benchmarks/results/*.json'
      - 'benchmarks/results/responses/**'
      - 'benchmarks/config.example.py'
      - 'benchmarks/export_for_pages.py'
      - 'benchmarks/generate_*.py'
      - 'benchmarks/scoring.py'
      - 'benchmarks/tests/**'
      - 'providers/adapters.py'
      - 'docs/**/*.html'
  workflow_dispatch:
```

Cuando alguien commitea cambios en data/scripts/tests:

1. Checkout con `fetch-depth: 0` (necesario para `git log` lastmod).
2. Setup Python 3.11.
3. `pip install python-dotenv` (mínimo viable).
4. Copia `config.example.py` → `config.py` (las keys no están en el
   action; los scripts solo necesitan `MODELS`).
5. Corre los 4 scripts en orden:
   - `export_for_pages.py` → `docs/data/models.json`
   - `generate_modelos_md_table.py -i` → `MODELOS.md`
   - `generate_tests_md.py -o TESTS.md`
   - `generate_sitemap.py` → `docs/sitemap.xml`
6. Si hay cambios, commit con mensaje `chore: regenera artefactos
   auto-generados [skip ci]`.

### Por qué `[skip ci]`

Para evitar loop. El bot commit no debe disparar la action otra vez.

### Por qué regenerar manualmente igual

`CLAUDE.md` exige que los scripts se corran **antes del commit principal**:

> Antes de cualquier commit que toque `benchmarks/results/`, config, o
> tests, ejecutar EN ORDEN: ...

Razón: el commit principal tiene los datos crudos + artefactos
sincronizados. Si dejás que el bot regenere después, el GitHub muestra
dos commits desincronizados durante un par de minutos. El bot es
**backup**, no flujo principal.

### `generate_per_model_md.py` no está en el action

Decisión consciente: regenerar 50+ MDs por commit es ruidoso en `git
diff`. Los `per-model/*.md` se regeneran solo localmente cuando hay
cambios en el ranking o nuevos modelos. El bot maneja los 4 que importan
para SEO/calculadora.

---

## 14. Configuración de modelos: tiers, providers, open-source

### Estructura de un modelo

```python
"devstral": {
    "id": "mistralai/devstral-small",       # ID OpenRouter o provider
    "name": "Devstral Small",                # legible
    "cost_input": 0.10,                      # USD/M tokens
    "cost_output": 0.30,
    "tier": "ultra_cheap",                   # filtro
    "open_source": True,                     # para ranking #3
    "license": "Apache 2.0",                 # legal clarity
    "provider": "openrouter",                # default; opcional
    "notes": "...",                          # opcional
},
```

### Tiers (filtro y agrupación visual)

| Tier | Rango precio | Ejemplos |
|---|---|---|
| `free` | $0 | DeepSeek R1 Free, Llama 3.3 70B Free |
| `ultra_cheap` | <$0.10/M | Mistral Nemo, Devstral Small, GPT-OSS 20B |
| `cheap` | $0.10–$1.00/M | DeepSeek V3, Gemini Flash, Devstral Medium |
| `medium` | $1.00–$5.00/M | Gemini Pro, GPT-4o, Claude Sonnet |
| `premium` | $5.00+/M | GPT-4o High, GPT-5.5, Claude Opus |
| `local` | $0 | Ollama local (DGX Spark) |
| `cloud_ollama` | flat-fee | qwen3.5:397b-cloud, gpt-oss:120b-cloud |
| `cloud_nim` | $0 (40 RPM) | NVIDIA NIM catalog |

### Providers soportados (8)

Cada uno necesita su API key + base URL:

| Provider key | URL | Key env |
|---|---|---|
| `openrouter` | https://openrouter.ai/api/v1 | `OPENROUTER_API_KEY` |
| `openai_direct` | https://api.openai.com/v1 | `OPENAI_API_KEY` |
| `openai_responses` | https://api.openai.com/v1 | `OPENAI_API_KEY` |
| `minimax_direct` | https://api.minimax.io/v1 | `MINIMAX_API_KEY` |
| `groq_direct` | https://api.groq.com/openai/v1 | `GROQ_API_KEY` |
| `nvidia_nim` | https://integrate.api.nvidia.com/v1 | `NVIDIA_NIM_API_KEY` |
| `ollama` (local) | http://localhost:11434/v1 | n/a |
| `ollama_cloud` | https://ollama.com/v1 | `OLLAMA_CLOUD_API_KEY` |

> Todas leídas desde `.env` (gitignored). Los providers opcionales se
> autodesactivan si la key está vacía.

### Familia Qwen: Base vs Plus vs Max

Trampa común — bien documentada en `CLAUDE.md`:

| Tier | Pesos | Ejemplos | Cómo correrlos |
|---|---|---|---|
| **Base** | Apache 2.0 (HuggingFace) | Qwen 3.6, Qwen3-Coder, Qwen 3.5 base | Ollama local, OpenRouter |
| **Plus** | API-only propietario | Qwen 3.6 Plus | Alibaba DashScope, OpenRouter |
| **Max** | API-only premium | Qwen Max | Alibaba DashScope |

> Error frecuente: poner `open_source: True` para "Qwen 3.6 Plus". El
> Plus es **derivado y propietario** — no se publican pesos. Verificar
> antes de marcar `open_source`.

### `PRICING` dict (en `scoring.py`)

Duplicado conceptualmente con `cost_input`/`cost_output` del config.
Razón histórica: scoring necesita pricing del **modelo real** (el ID
exacto que viene en el response), no del modelo configurado. Esto
permite que un mismo modelo accesible por dos providers (ej. Llama 3.3
70B en OpenRouter y en Groq) tenga pricings distintos.

> **Cuando agregás un modelo, actualizá ambos**: `MODELS["xxx"]
> ["cost_input"]` y `PRICING["provider/model-id"]`. Si te olvidás, el
> default es `(1.0, 3.0)` USD/M (conservador) y los costos reportados
> serán incorrectos.

---

## 15. Decisiones de diseño documentadas

Cada decisión con su porqué empírico. Si vas a tocar algo, leé el
porqué primero.

### 15.1 Sin streaming en el adapter

```python
# adapters.py: chat() llama sin stream=True
response = self.client.chat.completions.create(**kwargs)
```

**Por qué**: streaming complica timeouts (chunks parciales pueden
mantener la conexión "viva" sin progreso real). Para benchmarks lo que
importa es `latency_first_token` aproximado y `tokens_per_second`. Sin
streaming:

- `latency_first_token = latency_total` (aproximación conservadora —
  realmente fue antes, pero no podemos medirlo sin stream).
- `tokens_per_second = output_tokens / latency_total` (correcto).

Trade-off: perdimos precisión de TTFT. Lo aceptamos a cambio de
robustez.

### 15.2 `temperature=0.7` default, no 1.0

Para que las respuestas sean reproducibles-ish (no determinísticas pero
sin variación absurda). 0.7 es estándar industria para uso general.

Excepción: `FIXED_TEMP_MODELS` (GPT-5.5, GPT-5.5-pro, o1, o3) que
**solo aceptan 1.0**. Si pasamos 0.7 → error 400. Solución: omitir el
parámetro y dejar que la API use su default.

### 15.3 1 run por modelo en `--quick`, 3 en modo normal

`--quick` para benchmarks de iteración rápida (un modelo nuevo, ver si
funciona). 3 runs para resultados publicables (promedio de 3 modula
ruido aleatorio).

Decisión: **el ranking público actual está hecho con `--quick`**. Razón:
27 modelos × 91 tests × 3 runs = 7371 calls. A 5s/call promedio = 10
horas. Multiplicado por 27 modelos da ~270 horas. Imposible para un
freelancer con OpenRouter pagado de bolsillo. `--quick` baja a ~21 horas
por lote — tolerable.

> **Si forkeás con presupuesto**: corré con `RUNS_PER_TEST=3` quitando
> `--quick`. Los scripts de scoring ya promedian.

### 15.4 `time.sleep(0.5)` entre requests

Pausa hardcoded en el loop principal:

```python
if not is_local:
    time.sleep(0.5)
```

Para no saturar rate limits agresivos. OpenRouter tolera ~10 RPS pero
algunos modelos individuales (gpt-5.5-pro, ciertos chinos) saturan a
1-2 RPS. Sin la pausa, ~10% de los runs eran 429. Con 0.5s, <1%.

> No es eliminable sin retry logic. Si querés acelerar, agregale retry
> con backoff exponencial al adapter.

### 15.5 Penalización de chino en respuestas en español

```python
chinese_chars = sum(1 for c in response if '一' <= c <= '鿿')
if chinese_chars > 5:
    score -= min(2.0, chinese_chars * 0.1)
```

Modelos chinos (Qwen, GLM, Kimi, MiniMax) ocasionalmente "olvidan" el
idioma y responden mezclando CJK con español. Para un emprendedor que
quiere publicar en blog en español, esto es un fail crítico. Penalización
hasta 2 puntos.

### 15.6 `signal.alarm` además de httpx timeout

Ver [§5 — Manejo de timeouts](#5-capa-de-providers-adaptador-openai-compatible).
Resumen: doble redundancia. Empíricamente httpx no siempre aborta cuando
debería.

### 15.7 No re-medir modelos ya cubiertos (regla del CLAUDE.md)

Re-correr **solo** si:

1. Sale versión nueva (ID distinto = modelo distinto).
2. Cambian los tests/scoring.
3. Bug del runner/adapter invalida runs previos (ej. fix de
   `THINKING_TOKEN_MULTIPLIER`).
4. Provider hizo silent retraining anunciado.

> No re-medir por: refactor, mejoras cosméticas, regenerar MDs.

Razón: cada lote son ~21 horas de cómputo + 27 modelos pagados. Re-medir
sin causa real es desperdicio puro.

### 15.8 17 lotes "vivos" en lugar de 1 mega-lote

Cada vez que llega una nueva tanda de modelos a probar (Lote 1, Lote 2,
...), se corre como un benchmark separado y se commitea su JSON. Razón:

- Si un modelo del nuevo lote falla raro, no contamina el resto.
- El historial muestra **cuándo** se midió cada modelo (timestamp ⊆
  filename).
- Si querés reproducir resultados, sabés exactamente con qué versión de
  los tests se hicieron.

Los scripts agregadores (`export_for_pages.py`, `generate_per_model_md.py`)
consolidan **todos los JSONs** automáticamente.

---

## 16. Trade-offs y limitaciones honestas

> No existe un mejor benchmark universal. Este tiene sesgos explícitos.

### 16.1 Sesgo geográfico/idiomático

El 90%+ de los tests están en español, con contexto LATAM (RUTs
chilenos, pesos chilenos, ecosistema startup local). Si tu caso es
chino/inglés/alemán/etc., los puntajes no aplican directamente.

**Mitigación**: agregar tests multilingües (issue #X en ROADMAP).

### 16.2 91 tests no es estadísticamente robusto

Para un paper académico, 91 tests por modelo no aguantan rigor de
significancia. Para un emprendedor decidiendo "Devstral o GPT-4.1 mini",
sí.

**Mitigación**: 3 runs en modo normal (no `--quick`) reduce ruido a
~5%. Si tenés presupuesto, aumentar `RUNS_PER_TEST = 10`.

### 16.3 LLM-as-Judge tiene su propio sesgo

Phi-4 es un modelo. Tiene sus blindspots. Investigación de Anthropic/
DeepMind documenta:

- Sesgo de longitud: jueces tienden a premiar respuestas más largas.
- Sesgo de formato: respuestas con headers ganan ~5% sobre texto plano
  con misma sustancia.
- Sesgo de auto-mejora: si el juez es de la misma familia que el
  modelo, infla score 5-7%.

**Mitigaciones**:

- Phi-4 es Microsoft → no evaluamos modelos Microsoft → mínimo sesgo de
  auto-mejora.
- 30/70 con auto-quality como ancla limita el daño si Phi-4 se descarrila.
- Rúbrica explícita reduce variancia entre evaluaciones.

### 16.4 Pricing son snapshots, no en tiempo real

Los `cost_input`/`cost_output` están hardcoded en `config.py`. Cuando un
provider cambia precios (ej. OpenAI baja GPT-5.4 25%), hay que editar
manualmente.

**Mitigación**: `CLAUDE.md` regla — "verificar precios antes de
actualizar docs". Hay un cron mental, no automatizado.

### 16.5 Tests de tool calling son sintéticos

Los tests de tool calling tienen mock tools (`create_calendar_event`,
`send_email`). El modelo "llama" la tool, no se ejecuta nada real. Esto
mide capacidad de:

- Decidir cuándo llamar tool vs responder directo.
- Generar `arguments` con el JSON correcto.

NO mide:

- Si el modelo se recupera de un tool error.
- Multi-turn de tools con resultados reales que cambian el contexto.

**Mitigación**: tests de `multi_turn` y `agent_capabilities` cubren
algunos de estos casos pero sin engine real.

### 16.6 No hay tests multimodales (todavía)

`image_generation.py`, `tts_generation.py` están en stand-by. El
benchmark es text-only.

**Mitigación**: cuando llegue DGX Spark + tests multimodales, agregar
suite. Issue tracking en ROADMAP.md.

### 16.7 Sesgo de selección en modelos

Los 45+ modelos del config son los que Cristian considera relevantes
para sus casos. No están todos los del mundo. Notables ausentes:

- Mistral Large 2: en el `PRICING` dict pero no en `MODELS` de runner.
- Cohere Command: no testeado por costo.
- Algunos modelos chinos (Yi, Hunyuan): escaso uso por usuarios en
  español.

**Mitigación**: el config es público; PRs para agregar modelos son
bienvenidos.

---

## 17. Cómo extender el sistema

### 17.1 Agregar un modelo nuevo

```python
# 1. benchmarks/config.py — dict MODELS
"nuevo-modelo": {
    "id": "provider/model-id",
    "name": "Nombre Legible",
    "cost_input": 0.30,
    "cost_output": 1.20,
    "tier": "cheap",
    "open_source": True,
    "license": "Apache 2.0",
    "provider": "openrouter",  # o openai_direct, groq_direct, etc.
},

# 2. benchmarks/scoring.py — dict PRICING
"provider/model-id": (0.30, 1.20),

# 3. Correr
python benchmarks/runner.py --quick --judge --judge-model phi4 \
    --models nuevo-modelo

# 4. Auto-regenerar
python benchmarks/generate_per_model_md.py
python benchmarks/generate_modelos_md_table.py -i
python benchmarks/export_for_pages.py

# 5. Actualizar README/CHANGELOG si entra al ranking top
```

### 17.2 Agregar un provider nuevo

Si el provider habla OpenAI-compatible (la mayoría):

```python
# 1. .env.example — documentar la key
NUEVO_API_KEY=
NUEVO_BASE_URL=https://api.nuevo.com/v1

# 2. benchmarks/config.example.py — leer la key
NUEVO_API_KEY = os.getenv("NUEVO_API_KEY", "")
NUEVO_BASE_URL = os.getenv("NUEVO_BASE_URL", "https://api.nuevo.com/v1")

# 3. benchmarks/runner.py — instanciar el provider
nuevo_direct = None
try:
    from benchmarks.config import NUEVO_API_KEY, NUEVO_BASE_URL
    if NUEVO_API_KEY:
        nuevo_direct = UnifiedProvider("nuevo", NUEVO_API_KEY, NUEVO_BASE_URL)
except ImportError:
    pass

# 4. Agregar branch al selector
elif model_config.get("provider") == "nuevo_direct" and nuevo_direct:
    provider = nuevo_direct

# 5. En MODELS marcar provider="nuevo_direct" para los modelos del provider
```

Si NO es OpenAI-compatible (ej. Anthropic Messages API antes de v1):
hay que escribir una clase tipo `OpenAIResponsesProvider` con el
mismo contrato `chat() -> BenchmarkResult`.

### 17.3 Agregar una suite de tests

```python
# 1. benchmarks/tests/mi_suite.py
"""Tests de mi suite — descripción."""

TESTS = [
    {
        "name": "test_1",
        "description": "qué mide",
        "messages": [{"role": "user", "content": "..."}],
        "criteria": {...},
        "expected_answer": {"type": "...", ...},
    },
    # ... más tests
]

# 2. benchmarks/runner.py — importar y registrar
from benchmarks.tests import mi_suite

ALL_TEST_SUITES = {
    # ...
    "mi_suite": mi_suite.TESTS,
}

# 3. Mapear pilar en TRES lugares:
#    a. benchmarks/generate_per_model_md.py — PILARES
#    b. benchmarks/export_for_pages.py — SUITE_TO_PILLAR
#    c. benchmarks/generate_tests_md.py — SUITES list

# 4. Re-correr el benchmark de los modelos para que tengan datos del nuevo suite
python benchmarks/runner.py --quick --judge --judge-model phi4 \
    --tests mi_suite --resume <último-lote>.json

# 5. Auto-regen
```

### 17.4 Agregar un nuevo validador (`expected_answer.type`)

```python
# 1. benchmarks/scoring.py — score_expected_answer()
elif answer_type == "mi_validador":
    return _score_mi_validador(response, expected_answer)

# 2. Implementar la función
def _score_mi_validador(response: str, expected: dict) -> float:
    """Documentar qué mide y cómo, retornar 0-10."""
    # ...
    return score

# 3. Documentar el validador en este archivo (sección 7)
```

### 17.5 Cambiar el juez default

```python
# benchmarks/llm_judge.py
DEFAULT_JUDGE_PRESET = "qwen3.5"   # antes "phi4"

# Si querés agregar un preset nuevo:
JUDGE_PRESETS["mi_juez"] = {
    "model": "mi-modelo:tag",
    "base_url": "http://localhost:11434/v1",
    "api_key": "ollama",
    "provider": "ollama",
    "description": "Mi juez nuevo",
}
```

### 17.6 Forkearlo para tu dominio

Si tu caso de uso es radicalmente distinto (legal, médico, etc.):

1. Forkear el repo.
2. Reemplazar `benchmarks/tests/` con tus suites.
3. Ajustar pilares en `generate_per_model_md.py:PILARES`.
4. Probablemente bajar `RUNS_PER_TEST = 1` y subir `--quick` para
   iteración rápida.
5. Cambiar la rúbrica en `llm_judge.py:RUBRIC_TEMPLATE` para tu dominio.
6. Eliminar la calculadora HTML o adaptar `docs/index.html` con tu
   marca.

> El objetivo del repo no es "ser el mejor benchmark del mundo" — es
> "ser un molde que cualquier emprendedor pueda forkear y adaptar a su
> caso en una tarde".

---

## Apéndice A — Glosario

| Término | Definición |
|---|---|
| **Pilar** | Categoría de uso real (Razonamiento, Coding, Contenido, Agentes). Agrupa varias suites. |
| **Suite** | Conjunto de tests sobre un mismo subdominio (ej. `tool_calling`, `creativity`). |
| **Test** | Caso individual con prompt + criterios + validador. |
| **Run** | Una ejecución de un test contra un modelo. Hay 1-3 runs por (modelo, test). |
| **Lote** | Conjunto de modelos benchmarkeados juntos (genera 1 JSON). 17 lotes hasta v2.3.0. |
| **`final`** | Score final ponderado 0-10. Combina quality+cost+speed+latency+tools. |
| **`quality`** | Calidad de la respuesta. 30% auto + 70% judge cuando juez activo. |
| **`auto_quality`** | Calidad calculada solo con heurísticas (sin juez). 40% formato + 60% sustancia. |
| **`judge_score`** | Score 0-10 del juez (mapeado de 1-5). |
| **Thinking model** | Modelo que consume tokens internos en reasoning antes de responder (gpt-5*, o1*, kimi-k2.6, etc.). |
| **`max_completion_tokens`** | Param OpenAI nuevo para thinking models. Reemplaza `max_tokens` en GPT-5+. |
| **`FIXED_TEMP_MODELS`** | Modelos que solo aceptan `temperature=1.0`. El adapter omite el parámetro. |
| **`THINKING_TOKEN_MULTIPLIER`** | 4× — multiplica el max_tokens base para thinking models. |
| **Atomic save** | Escritura del JSON tras cada test (no al final). Si crash, no se pierde nada. |
| **Resume** | Continuar un lote interrumpido cargando el JSON previo y salteando lo hecho. |
| **Per-model MD** | Documento auto-generado por modelo con sus 91 tests + score + judge justification. |
| **Auto-gen** | Scripts que reconstruyen MDs/JSONs desde los datos crudos. Idempotentes. |
| **Open source (estricto)** | Pesos publicados con licencia OSI (MIT, Apache 2.0, Llama community). NO incluye API-only. |
| **API-only** | Modelo accesible solo por API del proveedor (Qwen Plus, MiMo Pro). NO es open source. |

---

## Apéndice B — FAQ técnica

### B.1 ¿Por qué no usar `pytest` para los tests?

`pytest` es para validar código. Aquí los "tests" son **prompts** que
se ejecutan contra modelos externos (red, async, costos reales). El
loop principal del runner hace las cosas que pytest no:

- Atomic save tras cada test.
- ETA dinámico.
- Resume sobre JSON externo.
- Múltiples runs con promediado.
- Manejo de timeout doble (httpx + signal).

Podríamos haber escrito un plugin pytest, pero el runner está OK como
script standalone.

### B.2 ¿Por qué no hay tests unitarios del scoring?

Hay un debt aquí. `score_*` son funciones puras y se testearían fácil
con pytest. No hay `tests/test_scoring.py`. El motivo es que cuando el
scoring cambió de v1 a v2, los tests se hubieran roto inmediatamente y
nadie iba a actualizarlos. Los tests reales son los **smoke tests con
modelos baratos** (`--models gemini-flash --tests reasoning --quick`)
que tardan 2 minutos y validan el flujo completo.

> Si forkeás para producción seria, escribí los unitarios. PRs
> bienvenidos.

### B.3 ¿Cómo se resuelve un model_id que está en dos providers?

Ejemplo: `meta-llama/llama-3.3-70b-instruct` está en OpenRouter Y en
Groq. En `MODELS` se configura **dos veces** con keys distintos:

```python
"llama-3.3-70b-free": {  # via OpenRouter
    "id": "meta-llama/llama-3.3-70b-instruct:free",
    ...
},
"groq-llama-3.3-70b": {  # via Groq
    "id": "llama-3.3-70b-versatile",
    "provider": "groq_direct",
    ...
},
```

Son entradas independientes en el ranking, con diferentes pricing y
velocidades. Esto es **deseable** — el mismo modelo en Groq y
OpenRouter da experiencias muy distintas (Groq es 10× más rápido).

### B.4 ¿Por qué `metadata.judge` y no `judge` en el root?

```json
{
    "metadata": {
        "timestamp": "...",
        "judge": {...},
        "partial": false
    },
    "results": [...]
}
```

Convención: todo lo que es contexto del run (timestamp, juez, errores
totales) va en `metadata`. `results` son los run scores. Esto facilita
hacer `cat *.json | jq '.metadata.judge'` para auditar qué juez se usó
en cada lote.

### B.5 ¿El benchmark es reproducible bit-a-bit?

No. Por:

- `temperature=0.7` introduce variabilidad.
- LLMs cambian (silent retraining de proveedores).
- Latencia depende de carga del provider.

Pero sí es **reproducible en magnitudes**: si re-corrés el mismo lote
con misma config, los rankings top-5 son los mismos ±1 posición. La
diferencia entre #1 y #10 es robusta.

### B.6 ¿Cómo manejar un modelo que no devuelve `usage`?

Algunos providers (NVIDIA NIM, ciertos endpoints custom) devuelven
`response.usage = None`. El adapter:

```python
if response.usage:
    result.input_tokens = getattr(response.usage, "prompt_tokens", 0) or 0
    result.output_tokens = getattr(response.usage, "completion_tokens", 0) or 0
```

Si `usage` es None, los tokens quedan en 0. `tokens_per_second` no se
calcula. `estimate_cost = 0`. El score de speed/latency sigue funcionando
porque vienen de `time.perf_counter`.

> Trade-off: para modelos sin usage, el cost score es siempre 10
> ("gratis"), inflando el final. Es una limitación conocida.

### B.7 ¿Por qué Phi-4 y no Llama 3.3 70B local?

Probamos Llama 3.3 70B como juez. Resultados:

- Más capacidad bruta que Phi-4.
- Pero genera respuestas más largas y a veces se sale de la rúbrica
  (escribe ensayos en lugar del JSON).
- Phi-4 es más obediente al formato.
- Phi-4 es más rápido (14B vs 70B en la misma máquina).

Phi-4 ganó por **disciplina formal**, no por capacidad. Para juez
queremos el segundo, no el primero.

### B.8 ¿Cómo agregar un timeout más largo solo para un test específico?

`run_single_test()` recibe `timeout` como parámetro. Hoy es uniforme
(`REQUEST_TIMEOUT=300` global). Si querés timeout diferenciado por
test:

```python
# tests/mi_suite.py
{
    "name": "test_largo",
    "timeout": 600,    # 10 minutos
    ...
}

# runner.py: run_single_test
timeout = test.get("timeout", REQUEST_TIMEOUT)
result = provider.chat(..., timeout=timeout)
```

Patch trivial. No está en main porque hasta hoy no fue necesario.

---

## Apéndice C — Para los que vienen de otras herramientas

### C.1 Vienen de MLflow / Weights & Biases

| Concepto MLflow/W&B | Equivalente acá |
|---|---|
| Experiment | Lote (`benchmark_<timestamp>.json`) |
| Run | Resultado individual (entry en `results[]`) |
| Metric | `final`, `quality`, `tokens_per_second`, etc. |
| Artifact | `responses/<timestamp>/<test>.md` |
| Tracking server | El repo git (cada commit es snapshot inmutable) |
| UI dashboard | Calculadora HTML en GitHub Pages |

**Diferencia clave**: no hay backend. Todo es JSON + Markdown. Pros:
auditable, forkeable, sin infra. Contras: no hay queries SQL ad-hoc, no
hay alertas.

> Si querés MLflow encima de esto, escribí un script que lea los JSONs
> y los empuje a MLflow tracking. ~50 líneas. PR bienvenido.

### C.2 Vienen de LangChain Benchmarks / LangSmith

| LangSmith | Equivalente acá |
|---|---|
| Dataset | `benchmarks/tests/<suite>.py` (lista TESTS) |
| Evaluator | `score_*` en `scoring.py` + `LLMJudge` en `llm_judge.py` |
| Run trace | `responses/<ts>/<test>.md` |
| Cost tracking | `estimate_cost` + `PRICING` dict |
| Custom metric | Agregar tipo a `expected_answer` |

**Diferencias**:

- No hay LangChain runtime — usamos OpenAI SDK directo. Más liviano.
- No hay async (todos los providers son sincrónicos en el adapter).
  Trade-off: simpler debugging, peor throughput.
- El LLM judge no usa el framework de LangChain — es un wrapper
  artesanal sobre OpenAI SDK.

### C.3 Vienen de OpenAI Evals

OpenAI Evals tiene una arquitectura similar (eval = suite de tests,
graders = scorers). Diferencias:

- Nosotros tenemos **ejecución multi-provider** out-of-the-box.
- Nuestro juez es local (Phi-4). OpenAI Evals usa GPT-4 default.
- Persistencia: ellos en JSONL stream, nosotros en JSON+MD por timestamp.

Si conocés OpenAI Evals, este repo te va a parecer "Evals-light con
calculadora HTML y less framework".

### C.4 Vienen de HumanEval / MMLU / BIG-Bench

Estos son benchmarks **académicos** con respuestas definitivamente
verificables (código que pasa/no pasa, multiple choice). Acá:

- 60% de los tests son open-ended (escribir un blog post, formular una
  estrategia). Imposible de validar booleanamente.
- Por eso hay 10 tipos de validador + LLM-as-Judge.
- El benchmark es **práctico**, no académico. Optimiza para "¿cuál uso
  para mi producto?", no para "¿cuál es objetivamente mejor?".

> Si tu objetivo es ranking académico, este repo no es para vos. Si tu
> objetivo es decidir un modelo para production con presupuesto real,
> bienvenido.

---

## Cierre

Este documento es un manual vivo. Cada decisión está documentada porque
**6 meses atrás Cristian no se acordaba por qué había hecho X**, y los
agentes que asistían (Claude, GPT) tampoco. La salida fue documentar
con porqués empíricos.

Si encontrás una decisión sin justificación, abrí un issue. Si
encontrás una contradicción entre `ARQUITECTURA.md` y el código, el
código manda — pero también es bug del documento, hay que actualizar.

> No existe un mejor modelo universal. No existe un mejor benchmark
> universal. Pero existe **el benchmark que vos podés ejecutar hoy con
> tu config y obtener datos auditables**. Eso es esto.

— Cristian Tala Sánchez, 26 abril 2026
