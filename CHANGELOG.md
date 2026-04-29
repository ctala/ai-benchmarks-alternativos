# Changelog

> **Regla de flujo**: todo lo que se marca como completado en ROADMAP.md se migra aquí con el commit correspondiente. El ROADMAP mira hacia adelante, el CHANGELOG deja traza de lo que pasó.

## [v2.4.0] - 2026-04-29 — Lote 9 NIM + DGX Spark Lote 1

### Cobertura
- **68 modelos con ≥50 runs** (antes 61), **7,725 runs** ejecutados (antes 7,223), 99 modelos en config (antes 88).
- **Lote 9 NIM** completado: 1,358 runs, 117 errores. Top 3 NIM: 🥇 Gemma 4 31B (NIM) 7.20 — 🥈 Nemotron Nano 9B v2 (NIM) 6.91 — 🥉 GLM 5.1 (NIM) 6.79.
- **DGX Spark Lote 1** completado: Gemma 4 31B Q4_K_M (89/91 = 6.84) + Nemotron 3 Super 120B Q4_K_M (90/91 = 6.74). 9-18 tok/s sostenido en hardware propio.
- **Hallazgo Gemma 4 31B**: NIM 7.20 vs DGX Q4_K_M 6.84 = -0.36 puntos por cuantización. Sigue siendo competitivo para correrlo local sin pagar.
- **Magistral Small (NIM) descartado**: error 400 instant en 91/91 — modelo rechaza algún parámetro en el adapter.
- **DeepSeek V4 Pro (NIM) descartado**: 502/504 timeouts en NIM gateway con prompts largos. Funciona bien via Ollama Cloud (smoke test confirmado).

### Sincronización de docs (#desync)
- **`benchmarks/sync_doc_counts.py`** (nuevo) — script preventivo que lee `docs/data/models.json` (single source of truth) y reescribe counts (X modelos, X+ tests, X lotes) en README, AGENTS, INSIGHTS, ARQUITECTURA, MODELOS, agentes y landing pages SEO. Excluye blogs y CHANGELOG (históricos dated).
- **Agregado a la regla de auto-generación** en `CLAUDE.md` como paso 6.
- **30+ referencias desactualizadas** corregidas en una sola pasada (53→68, 5K→7K tests, 7→16 lotes, 45 modelos × 91 → recalculado).

### Refactor export
- `export_for_pages.py` ahora hace merge de `MODELS` (cloud) + `OLLAMA_MODELS` (locales DGX/Mac) → los DGX models aparecen en la calculadora.
- Total catálogo: 99 modelos (antes 88).

### Capability flags
- `_infer_capabilities()` en `export_for_pages.py` infiere `tool_calling`, `thinking`, `multimodal` por modelo desde patterns conocidos. Permite override manual en config.
- Calculator UX: filtros por capability con guía colapsable de 6 categorías + cards semánticos.

### Calidad calculadora (UX)
- Sub-categorías cascade: 4 pilares × 23 suites con dropdown que se expande al elegir tarea.
- Presets: Personal/Solopreneur/Pyme/Producción con preset de defaults razonable.
- Costo-Beneficio columna con badges semánticos (Excelente/Bueno/Aceptable/Caro/Gratis-contextual).
- Free labels específicos por provider: ★ NIM 40rpm / ★ Sub Ollama / ★ Sub Xiaomi / ★ Local / ★ Sin pago.
- Default budget=500, calidad=6.5, sin límite de resultados.
- WCAG AA touch targets, cache busting via `?v=YYYYMMDDx`.

## [Unreleased] - 2026-04-25 (continúa)

### NVIDIA NIM provider (#19)
- Provider `nvidia_nim` agregado al runner. Base URL `https://integrate.api.nvidia.com/v1` (OpenAI-compatible).
- Free tier 40 RPM = perfecto para benchmarks secuenciales (cada test ~5-30s, no excede el límite).
- `NVIDIA_NIM_API_KEY` en `.env`, smoke test OK con Nemotron Super 49B v1.5 (8.3s para "hola").
- 135+ modelos en el catálogo. 8 agregados al config (claves `nim-*`):
  - `nim-nemotron-super-1.5` (versión v1.5 del Nemotron Super que ya medimos)
  - `nim-nemotron-ultra-253b` (más grande de la familia)
  - `nim-qwen3-next-instruct` y `nim-qwen3-next-thinking` (Qwen 3-Next 80B, próxima gen)
  - `nim-mistral-nemotron` (colab Mistral × NVIDIA)
  - `nim-kimi-k2-thinking` (variante thinking del K2 — comparar con K2.6)
  - `nim-deepseek-v4-flash` (mismo modelo que OpenRouter, comparar latencia/calidad)
  - `nim-qwen3.5-397b` (mismo Cristian usa en producción via Ollama Cloud — comparar)
- 8 nuevos modelos = potencial de 8 × 91 = 728 tests gratis en próximo Lote 6.

### Agregado
- **`OpenAIResponsesProvider`** en `providers/adapters.py` — soporta el endpoint `/v1/responses` de OpenAI requerido por `gpt-5.5-pro` y `o1-pro`. Estos modelos NO funcionan en `/v1/chat/completions` (404 en 58/58 tests del Lote 4).
- Mapping de `messages` → `instructions` (system) + `input` (user concatenado).
- Captura `reasoning_tokens` separados en `result.metadata` cuando el SDK los expone (`usage.output_tokens_details.reasoning_tokens`).
- Smoke test con `gpt-5.5-pro` "Di solo hola": 15 input + 46 output + **39 reasoning** tokens. Confirma cuantitativamente que el reasoning interno de pro models es ~85% del costo facturado.
- Provider key `"openai_responses"` en config para rutear modelos a este endpoint.
- `gpt-5.5-pro` ya no está bloqueado para correr en lotes futuros.

### Documentación de costos honesta (`Lo que te ahorras` en README)
- `PRICING` dict en `scoring.py` ampliado: agregados Anthropic (Claude Opus/Sonnet/Haiku 4.x), Kimi K2/K2.5/K2.6, Mistral Large, Llama 4 family, Qwen 3.6 Plus, MiniMax, DeepSeek V4 Flash/Pro, DeepSeek R1, gpt-oss 20/120B. Corregidos GPT-5.4/5.4-mini/5.5 con tarifas reales.
- Recálculo: $14 → $48 sobre runs preservados (antes Claude/Kimi caían en fallback `(1.0, 3.0)`).
- Documentadas 4 categorías de costo invisible: iteración de metodología, vacíos facturados, timeouts cobrados, retries.
- Dashboard real OpenRouter: $100+ acumulado al cierre de v2.2.1 (vs los $48 calculados — diferencia es la iteración pre-tracking no preservada en JSONs).

### Reglas y estándares
- **Corte "Solo Alternativas"** ahora excluye también modelos Google propietarios (Gemini Flash/Flash-Lite/Pro). Sí permite open-source de Google (Gemma). Tabla del README reducida de 20 a 17 modelos. Documentado en `CLAUDE.md` y `ROADMAP.md`.
- **Estándar de no re-medir** en `CLAUDE.md`: re-correr SÓLO si versión nueva del modelo, suites/tests cambiados, bug del runner, o cambio visible del proveedor. NO por refactors/cosméticos.

### Inventario y documentación pública
- **`MODELOS.md`** (nuevo) — inventario único de cobertura: 28 probados + 20 en config sin probar + ~10 mercado por agregar. Plan Lote 6 priorizado.
- **`TESTS.md`** (nuevo, auto-generado) — 91 tests en 23 suites con prompt + criterios visibles. Script `benchmarks/generate_tests_md.py` para regenerar tras agregar/cambiar tests.
- **`benchmarks/calculate_costs.py`** (nuevo) — calcula costos reales sumando todos los JSONs y recalculando con `PRICING` actual. Comando `--markdown` para tabla pegable.

### DeepSeek V4
- Agregados al config: `deepseek-v4-flash` (0.14/0.28, 284B params, 1M context) y `deepseek-v4-pro` (1.74/3.48, 1.6T params, 1M context). IDs verificados via OpenRouter.

### Recovery 402 (post-saldo bajo OpenRouter)
- Detectado: thinking models con `max_completion_tokens=8192` requieren reserva worst-case ~$74/request. Con saldo bajo, OpenRouter rechazó con 402 todos los Kimi K2.6 (47 + 9 = 56 tests + 1 GLM-5.1).
- Tras recarga del usuario: `--rerun-failed` recupera los runs sin afectar los exitosos. Recovery 1 (GLM-5.1, 1 test) y Recovery 2 (Kimi K2.6 Lote 3, 9 tests) completados. Recovery 3 (Kimi vs Opus, 47 tests) en curso.

## [2.2.1] - 2026-04-25 (post-Lote 3 / Lote 4 GPT-5.5)

### Por que v2.2.1
- Auditoria sistematica de empty responses revelo 165+ runs con `success=True` y `content=""` distribuidos en 4 lotes. Detectada raiz: thinking models agotando max_tokens en reasoning interno.
- 6 timeouts de GPT-5.5 a 181s causados por httpx read_timeout=60s × 3 retries.
- GPT-5.5 Pro inservible en chat/completions (404), requiere endpoint Responses.

### Mejorado (`providers/adapters.py`)
- **Constantes a nivel de modulo** para que el estandar este visible y editable sin tocar la logica:
  - `THINKING_MODELS`: tupla de prefijos (gpt-5*, o1*, o3*, glm-5*, kimi-k2.6, nemotron*)
  - `FIXED_TEMP_MODELS`: tupla de modelos que solo aceptan temperature=1.0
  - `THINKING_TOKEN_MULTIPLIER = 4` (era hardcoded)
  - `THINKING_MIN_TOKENS = 8192` (piso absoluto para thinking)
  - `HTTP_READ_TIMEOUT_S = 240.0` (era 60.0)
- Adapter omite `temperature` para FIXED_TEMP_MODELS para evitar HTTP 400.
- Adapter usa `max_completion_tokens` en thinking models y aplica el multiplicador automaticamente.

### Resultados Lote 4 (GPT-5.5)
- GPT-5.5 score final: **6.42** (era 5.76 antes del fix de max_tokens, antes de eso quedaba `content=""` por agotar budget razonando).
- 6 tests strategy/workshop/creativity recuperados con scores 6.3-6.7 tras subir HTTP_READ_TIMEOUT a 240s.
- 10 tests tool_calling/customer_support/orchestration/agent siguen empty: bug cosmetico #23 (content=None cuando hay tool_calls), no afecta el scoring.
- GPT-5.5 Pro: 58/58 tests fallaron con 404. Requiere endpoint Responses API. Excluido del benchmark hasta task #21.

### Documentado (este commit)
- README.md: tabla de "Estandar del benchmark para thinking models" con las 7 constantes, sus valores y razones (nivel etiqueta).
- CLAUDE.md: misma tabla mas explicacion de cuando editar cada constante.
- DESCUBRIMIENTOS.md: seccion "Lote 4 + Hallazgos tecnicos" con
  - Cost multiplier de thinking models (3-4× facturacion real)
  - Audit de 165+ runs vacios por agotar max_tokens
  - Patron 8-empty = bug cosmetico de tool_calling
  - HTTP read_timeout 60s vs 240s
  - FIXED_TEMP_MODELS rechazo de temperature distinta de 1.0
  - GPT-5.5 Pro endpoint Responses (404 en chat/completions)
  - Atomic incremental save: 10.5h perdidos en Lote 1 sin checkpoint
  - Qwen 3.6 Plus marcado proprietary (no open-source)

## [2.2.0] - 2026-04-25

### Por que v2.2 (Lote 3 + 10 modelos nuevos)
- Lote 3 con juez Phi-4 (10 modelos × 91 tests = 910 runs). Total acumulado: **27 modelos × 91 tests = 2457 runs evaluados**. Ranking global re-calculado.
- 3 cortes en README: global, sin Anthropic/OpenAI, **solo open-source** (nuevo).

### Resultados destacados Lote 3
- **Devstral Small mantiene #1 (7.35)** tras agregar 10 modelos.
- **Devstral 2 (dic 2025) entra #5** pero NO supera al Small original.
- **Gemma 4 26B sorprende #10** — open-source pequeño compitiendo con Claude Opus.
- **MiMo-V2-Pro decepciona #20** — el flagship Xiaomi rinde MENOS que MiMo-V2-Flash (#6).
- **GPT-5.4 #14 vs GPT-5.4 Mini #2** — el Mini supera al grande.
- **Gemini 2.5 Pro #25** — el flagship Google rinde peor que su propio Flash Lite.
- **Kimi K2.6 ÚLTIMO #27 (5.76)** — peor que K2 original.
- **Mistral Nemo aceptable #21 ($0.02/$0.02)** — baseline ultra económico.

### Tiempo invertido (todos los lotes desde abril 11)
| Concepto | Wall-clock |
|---|---|
| Pre-v2.1 (16 sesiones abril 11-15) | ~12 h |
| Kimi K2.6 vs Claude (abril 22) | 2.9 h |
| Agent capabilities 13 modelos (abril 22) | 0.5 h |
| Lote 1 PERDIDO sin checkpoint (704/728) | 10.5 h |
| Lote 1 v2.1 oficial (728 runs) | 7.0 h |
| Lote 2 v2.1 (819 runs) | 14.0 h |
| Lote 3 v2.2 (910 runs) | 17.7 h |
| **Total** | **≈ 65 h wall-clock** |

3515 runs ejecutados (2811 guardados, 704 perdidos en Lote 1 sin checkpoint), equivalentes a 8 jornadas laborales o 2.7 días de cómputo continuo. No incluye refactors del runner, investigación, ni documentación.

### Documentado
- README v2.2 con 3 cortes de ranking + tabla por categoría con 27 modelos
- Mejor por categoría re-calculado con los 10 nuevos
- Recomendaciones por caso de uso actualizadas

## [2.1.1] - 2026-04-23 / 2026-04-24

### Agregado
- **MDs navegables por modelo** en `benchmarks/results/per-model/` (17 archivos + index README). Cada MD tiene resumen global, tabla por pilar/suite, tests expandibles con judge score y preview de respuesta. Directamente auditable desde GitHub, sin infra.
- **Script `benchmarks/generate_per_model_md.py`**: regenera los MDs desde los JSON sin re-correr tests. Acepta `--inputs` para consolidar varios lotes.
- **Log del runner mejorado**: cada línea muestra progreso global + nombre corto del modelo + progreso local por modelo (N/91) + suite/test + descripción corta del test + elapsed total + ETA basado en promedio móvil de últimos 20 tests.
- **Devstral Medium** (`mistralai/devstral-medium`, $0.40/$2.00, Apache 2.0) y **Devstral 2** (`mistralai/devstral-2512`, $0.40/$2.00, Apache 2.0) agregados al config. Pendiente: correr benchmark en Lote 3.
- **Provider Ollama Cloud**: nuevo `UnifiedProvider("ollama_cloud", ..., "https://ollama.com/v1")` en runner. Activar con `OLLAMA_CLOUD_API_KEY` en config.py (crear key en https://ollama.com/settings/keys). Modelos con `"provider": "ollama_cloud"` rutean al endpoint cloud. `config.example.py` incluye ejemplos: `qwen3.5:397b-cloud` (el que Cristian usa en prod para ecosistemastartup.com), `qwen3.5:cloud`, `gpt-oss:120b-cloud`.
- **Lote 3 en curso** (arrancado 2026-04-24): 10 modelos × 91 tests = 910 runs. Modelos: devstral-medium, devstral-2, gpt-5.4, mimo-v2-pro, gemini-flash, gemini-pro, kimi-k2.6, claude-opus-4.6, gemma-4-26b, mistral-nemo.
- **Migración a `.env`**: todas las API keys (OPENROUTER, OPENAI, MINIMAX, OLLAMA_CLOUD) ahora viven en `.env` gitignored en lugar de hardcoded en `config.py`. Usa `python-dotenv`. `.env.example` committed como template. `config.py` y `config.example.py` sólo definen dicts (MODELS, OLLAMA_MODELS) y leen keys via `os.getenv()`.
- **Regla de 3 cortes en README**: al actualizar rankings mantener siempre (1) global, (2) sin Anthropic/OpenAI, y (3) solo open-source. Documentado en CLAUDE.md y ROADMAP.md.

### Documentado
- **ROADMAP.md** re-escrito desde cero: estado real v2.1, queue inmediato (modelos nuevos identificados), skills propuestos (`/add-model`, `/run-benchmark`), plan para DGX Spark y Ollama Cloud.
- **CLAUDE.md** actualizado: archivos clave nuevos, workflow con regeneración de MDs, regla de flujo ROADMAP↔CHANGELOG.

## [2.1.0] - 2026-04-23

### Por que v2.1 (first full Phi-4 run)
- **1512 corridas** evaluadas con Phi-4 judge: 17 modelos × 91 tests. Primer run completo del benchmark v2 con juez local.
- Ranking v1 (sin juez) queda obsoleto. v2.1 es la primera "verdad" con scoring completo.

### Agregado
- **Guardado incremental atomico en runner.py**: dump a JSON tras cada test, no al final. Si se corta no se pierde nada.
- **Flag `--resume <archivo.json>`**: retoma desde un benchmark parcial, saltea tests ya completados.
- **Guardado de respuesta completa por test**: cada request genera un `.md` auditable en `benchmarks/results/responses/<timestamp>/<modelo>__<suite>__<test>.md`. El JSON lleva `response_file` con path relativo.

### Resultados destacados (Phi-4 judge, 91 tests/modelo)
- **Top 5**: 1) Devstral Small 7.35, 2) GPT-5.4 Mini 7.32, 3) GPT-4.1 7.29, 4) Gemini 2.5 Flash Lite 7.22, 5) MiMo-V2-Flash 7.20
- **Devstral Small domina** como #1 overall y top en creatividad (7.70), string precision (7.66), traducción (7.87)
- **MiMo-V2-Flash sorprende**: #1 en razonamiento (7.58), contenido ES (7.51), code (7.74), strategy (7.78), productividad (7.66) — a $0.09/$0.29 per M (MIT)
- **GPT-5.4 Mini sube del #8 (v1) al #2**: el juez revaloriza su equilibrio calidad/velocidad (117 tok/s)
- **Llama 4 Maverick top en agentes (7.32)** pero 17 tests fallan por falta de tool calling nativo en OpenRouter
- **Kimi K2 17 errores 429** por rate limits sostenidos del provider
- **GLM-5.1 último (6.25)**: muy flojo en code/reasoning/contenido a pesar del branding agentic
- **Modelos chinos (MiniMax, Qwen, GLM) y Nemotron** agrupados al final del ranking

### Modelos nuevos evaluados en este run
- GPT-4.1 (directo, no Mini), GPT-5.4 Mini, Claude Opus 4.7, Kimi K2, Qwen 3.6 Plus, Qwen3 Coder, Mistral Large, Nemotron 3 Super, GLM-5.1

### Documentado
- README.md actualizado con ranking real de 17 modelos × 91 tests
- Mejor por categoría expandido a 12 categorías con Phi-4 judge
- Recomendaciones por caso de uso re-escritas con los nuevos datos

## [2.0.0] - 2026-04-22

### Por que v2.0 (breaking changes)
- Scoring v2 + LLM-as-Judge cambia todos los scores. Rankings anteriores no son comparables.
- Tests reorganizados en 4 pilares del emprendedor (razonamiento, coding, contenido, agentes)
- Juez cambiado de Gemma 4 a Phi-4 (Microsoft) por cero conflicto de interes
- Claude Code removido de suscripcion Pro $20 (21 abril 2026) - contexto actualizado

### Agregado
- **4 suites nuevas**: strategy (3 tests), sales_outreach (3 tests), translation (3 tests), agent_capabilities (5 tests)
- **Phi-4 como juez local**: Microsoft no tiene modelos en el benchmark = cero sesgo. MIT license, 14B, 3-9s/eval, $0.
- **6 modelos nuevos**: GLM-5.1 (#1 SWE-Bench Pro), Kimi K2.6, MiMo-V2-Flash/Pro, Nemotron 3 Super, Claude Opus 4.7
- **CASOS_DE_USO.md**: 50+ casos reales de IA para emprendedores organizados en 8 categorias
- **Compatibilidad con coding tools**: Info sobre que modelos funcionan con Claude Code, Roo Code, Cursor, etc.
- Total: **91 tests en 23 suites**, 30+ modelos configurados

### Mejorado
- Tests organizados en 4 pilares: Razonamiento, Coding, Contenido/Marketing, Agentes/Operaciones
- Adapter soporta thinking models (max_completion_tokens) para GLM-5.1, Kimi K2.6, Nemotron, GPT-5.4
- Judge usa /api/generate nativo para Ollama (fix: gemma4 devuelve vacio en /api/chat)
- Timeout subido a 300s para articulos largos
- Contexto actualizado: Claude Code ya no en suscripcion Pro $20

### Documentado
- Por que Phi-4 como juez (cero conflicto, MIT, replicable)
- Sesgo de LLM-as-Judge con referencias a papers (NeurIPS 2024, self-enhancement bias 5-7%)
- DESCUBRIMIENTOS.md actualizado con hallazgos de string precision y news SEO

## [1.3.0] - 2026-04-16

### Agregado
- **4 modelos Xiaomi MiMo**: MiMo-V2-Pro ($1/$3, 1T params), MiMo-V2-Flash ($0.09/$0.29, MIT), MiMo-V2-Flash free, MiMo-V2-Omni ($0.40/$2, multimodal)
- **Suite ocr_extraction** (5 tests): Facturas, tarjetas de presentacion, recibos con verificacion matematica, tablas de dashboard, notas manuscritas con OCR errors
- **Suite orchestration** (5 tests): Planificacion multi-paso, recuperacion de errores, descomposicion de workflows, seleccion precisa de herramientas, juicio paralelo vs secuencial
- **Suite multi_turn** (4 tests): Iteracion de contenido con feedback, soporte que escala, cambio de requisitos a mitad de camino, debugging iterativo
- **Suite policy_adherence** (4 tests): Politicas de reembolso bajo presion, proteccion de datos ante ingenieria social, reglas de idioma/tono, limites de alcance de servicio
- **LLM-as-Judge** (`--judge`): Sistema de evaluacion con auto-deteccion de juez. Prioridad: 1) Gemma 4 31B local via Ollama ($0, bajo sesgo), 2) Claude Haiku via OpenRouter (~$0.07/modelo). Evalua 5 dimensiones (precision, relevancia, profundidad, claridad, utilidad) + criterios extra por suite (originalidad, empatia, planificacion, coherencia contextual, cumplimiento de politicas). Combina 30% score automatico + 70% juez. Presets: gemma4, glm4, qwen3.5, haiku, gemini-flash. Tambien acepta model IDs directos.
- **Documentacion de sesgo del juez**: El modelo juez introduce sesgo (~5-7% de inflacion para modelos del mismo proveedor). Documentado en README, llm_judge.py, y CHANGELOG con tabla de tradeoffs por juez. Resultados JSON registran que juez se uso.
- **9 modelos nuevos de Abril 2026**: Nemotron 3 Nano ($0.05/$0.20), Nemotron 3 Super ($0.10/$0.50), Mistral Small 4 ($0.15/$0.60, Apache), Grok 4.1 Fast ($0.20/$0.50), Gemini 3.1 Flash Lite ($0.25/$1.50), Devstral 2 ($0.40/$2.00, MIT), GLM-5.1 ($0.95/$3.15, MIT, #1 SWE-Bench Pro), Gemini 3.1 Pro ($2.00/$12.00), Grok 4.20 ($2.00/$6.00)
- **Seccion "Como Replicar el Benchmark"** en README: guia paso a paso desde cero, costos estimados, como agregar modelos
- Total: 77 tests en 19 suites (antes: 59 tests en 15 suites)
- 3 proveedores nuevos: Xiaomi (MiMo), NVIDIA (Nemotron), xAI (Grok) en PROVEEDORES.md y COMPARATIVA.md

### Mejorado (Scoring v2 - correccion de sesgo)
- **Formato reducido de 3 a 2 puntos** en score_content_quality (era 30% del score de calidad, ahora 20%)
- **Secciones requeridas subidas de 3 a 4 puntos** para priorizar contenido sobre formato
- **Busqueda de secciones ahora ignora acentos** ("titulo" encuentra "título") via normalizacion Unicode
- **Penalizacion de caracteres chinos** en respuestas en espanol (hasta -2 pts). Mitiga problema de MiniMax y Qwen.
- **Nuevo score_expected_answer()** que valida respuestas contra criterios especificos:
  - `reasoning`: verifica que key_insights esten presentes (60% de palabras clave)
  - `hallucination_check`: evalua si el modelo dice "no se" en preguntas trampa
  - `creativity_check`: penaliza cliches (-1.5 a -5 puntos segun cantidad)
  - `depth_check`: penaliza frases genericas, premia datos concretos y riesgos
  - `honesty_check`: evalua transparencia sobre incertidumbre
  - `numeric`, `sequence`, `range`: validacion de respuestas factuales
- **Sin juez**: tests con expected_answer usan 40% formato + 60% sustancia
- **Con juez** (`--judge`): usa 30% automatico + 70% LLM-as-Judge

### Por que estos cambios (contexto)
- El scoring anterior daba 30% de los puntos de calidad por formato markdown (headers, bold, listas)
- Tests como deep_reasoning, creativity, hallucination tenian `expected_answer` definido pero NUNCA se validaba
- La lista de cliches en creativity.py existia pero no se usaba en el scoring
- Esto hacia que modelos rapidos y baratos que formateaban bien (Devstral) dominaran sobre modelos con mejor razonamiento
- El nuevo scoring valida sustancia: insights correctos, honestidad, creatividad real, datos precisos
- Los tests multi-turno y policy_adherence miden capacidades criticas para agentes reales que los tests single-turn no capturan
- LLM-as-Judge agrega evaluacion semantica que el scoring regex no puede hacer (calidad de analogias, empatia, utilidad practica)
- Benchmarks de referencia: HELM (Stanford), tau-Bench (Sierra), BFCL (Berkeley), LMSYS Arena

## [0.8.0] - 2026-04-12

### Agregado
- 6 modelos nuevos: Devstral Small, GPT-4.1, GPT-4.1 Mini, Mistral Large, Kimi K2, Kimi K2.5
- Claude Opus 4.6 (el #1 del mundo en Arena)
- 21 modelos en ranking global total
- Nota sobre limitaciones del scoring automatico

### Resultados Destacados
- Devstral Small es #1 (7.40) - open-source Apache 2.0, 171 tok/s, ultra barato
- GPT-4.1 es #2 (7.28) - supera a GPT-5.4 (#19), confirma hallazgo previo
- Claude Opus 4.6 es #13 (6.59) - scoring no captura calidad de razonamiento
- Kimi K2 es #16 (6.49) - decente pero no tan bueno como en benchmark manual previo

### Descubierto
- Scoring automatico favorece formato sobre sustancia
- GPT-4.1 consistentemente supera GPT-5.4 en tests estructurados
- Devstral Small de Mistral es una joya oculta

## [1.1.0] - 2026-04-12

### Agregado
- Suite hallucination: 3 tests (trampas factuales, fidelidad al contexto, citas falsas)
- Suite creativity: 4 tests (hooks sin cliches, analogias, profundidad, storytelling)
- DESCUBRIMIENTOS.md con observaciones no obvias
- Ranking global actualizado con 48 tests por modelo, 951 runs totales
- Recomendaciones expandidas: 11 casos de uso con modelo recomendado
- CheatSheet PDF actualizado a 9 paginas con alucinaciones y creatividad

### Resultados
- Alucinaciones: Claude Sonnet #1 (7.62), Anthropic = mas honesto
- Creatividad: Devstral #1 (6.93), MiniMax ultimo (5.19)
- Claude Opus sube a #9 global (desde #13) con los tests de calidad
- Claude Sonnet sube a #7 global (desde #12)

### Hallazgos
- Claude es el modelo mas honesto pero no el mas creativo
- MiniMax M2.7 es generico y con cliches en contenido
- MiniMax y Qwen a veces responden con caracteres chinos

## [0.7.0] - 2026-04-12

### Agregado
- Llama 4 Maverick via OpenRouter - #6 global, empata con Claude, open-source
- Qwen3 Coder via OpenRouter - #8 global, bueno para coding
- Gemma 4 31B y 26B MoE via OpenRouter - lentos pero funcionales
- Ranking actualizado con 12 modelos (14 contando variantes)
- Tabla solo alternativas (sin Anthropic/OpenAI) con 8 modelos

### Resultados
- Llama 4 Maverick (6.70): Sorpresa, empata con Claude Sonnet 4.6 y es open-source
- Qwen3 Coder (6.62): Solido para coding
- Gemma 4 26B MoE (6.53): Decente pero lento via OpenRouter (19 tok/s)
- Gemma 4 31B (6.42): Mas lento aun (11 tok/s), rate limits frecuentes

## [0.6.0] - 2026-04-11

### Agregado
- GPT-5.4 y GPT-5.4-mini via API directa de OpenAI
- Ranking global con 9 modelos medidos (10 contando duplicados de MiniMax por provider)
- Tabla separada "Solo Alternativas" (sin Anthropic/OpenAI)
- Tabla "Mejor por Categoria" con top 3
- Tabla "Recomendacion para Agentes N8N/OpenClaw"
- Soporte max_completion_tokens para GPT-5.4+

### Resultados
- GPT-5.4 Mini: Sorpresa, gana al GPT-5.4 en todas las categorias
- GPT-5.4 Mini: #1 en tool calling (7.5), ideal para agentes
- DeepSeek V3.2 se mantiene #1 global (7.09)
- Gemini 2.5 Flash Lite: 212 tok/s, el mas rapido por lejos

## [0.5.0] - 2026-04-11

### Agregado
- CLAUDE.md para continuidad entre sesiones de agentes
- Tests de generacion de imagenes MiniMax Image-01 (5/5 exitosos)
- Tests de TTS MiniMax (requiere plan Agent, no funciona con Coding Plan)
- Modelos nuevos: Gemma 4 31B, Gemma 4 26B MoE, Claude Sonnet 4.6, Gemini 2.5 Flash Lite, Qwen3 Coder 480B
- PROVEEDORES.md actualizado
- Image generation results en benchmarks/results/images/

### Descubierto
- MiniMax Coding Plan no incluye TTS (speech-02). Requiere plan Agent ($19/$69)
- MiniMax Image-01 funciona con Coding Plan token key
- Gemma 4 via OpenRouter es lento (~8 tok/s) - mejor correr local en DGX Spark

## [0.4.0] - 2026-04-11

### Agregado
- PROVEEDORES.md: Guia de contexto de cada proveedor (fundacion, foco, fortalezas, open-source)
- Resultados de benchmark en README.md
- Soporte API directa de MiniMax (M2.7 y M2.7 Highspeed)
- Tests de startup_content: blog ecosistemastartup.com, cursos, workshops, newsletters
- Repo privado en GitHub: ctala/ai-benchmarks-alternativos

### Resultados
- Benchmark general: DeepSeek V3.2 (7.05) > MiniMax M2.7 (6.40) > Qwen 3.6 Plus (6.08)
- MiniMax M2.7 vs Highspeed: diferencia marginal (~1%), practicamente iguales
- DeepSeek gana en 6/7 categorias, MiniMax gana en tool calling

### Corregido
- Runner: timeout robusto con signal alarm, output en texto plano
- Model IDs: Qwen 3.6 Plus free deprecado, MiniMax highspeed solo via API directa

## [0.3.0] - 2026-04-11

### Agregado
- PACKS.md: Guia de packs por suscripcion (MiniMax, Qwen, OpenAI, Google, Ollama, OpenRouter, xAI)
- Estrategia de optimizacion local + nube para DGX Spark
- Rankings completos por categoria (6 categorias con top 8-10 modelos cada una)
- Diagrama de routing: que modelo usar para que tarea
- Fecha de ultima actualizacion en todos los documentos

### Modificado
- COMPARATIVA.md: Rankings expandidos con listas completas en vez de solo el lider
- README.md: Version 0.3.0, referencia a PACKS.md

## [0.2.0] - 2026-04-11

### Agregado
- Modelos nuevos: Gemma 4 (31B, 26B MoE), Llama 4 Maverick, MiniMax M2.7 Highspeed
- Columna "Open Source" en todas las comparativas
- Seccion de modelos locales para NVIDIA DGX Spark (128GB)
- Suscripciones de MiniMax (Coding Plan $10-$150, Agent $19/$69)
- Suscripciones de Alibaba/Qwen (Coding Pro $50/mes)
- Ollama Cloud ($0/$20/$100)
- CHANGELOG.md para versionamiento

### Modificado
- Correccion: Anthropic SI funciona con OpenClaw/N8N via API key, la suscripcion Pro/Team NO da acceso API
- Modelos locales expandidos para aprovechar los 128GB del DGX Spark
- Config actualizado con modelos open-source marcados con licencia

## [0.1.0] - 2026-04-11

### Agregado
- Estructura inicial del proyecto
- COMPARATIVA.md con 30+ modelos organizados por tier de costo
- SUSCRIPCIONES.md con todas las suscripciones fijas ($0-$300/mes)
- 7 suites de benchmark con 18 tests totales
- Motor de benchmark (runner.py) con soporte OpenRouter
- Sistema de scoring multi-criterio (calidad, velocidad, costo, tool calling)
- Adaptador unificado para APIs compatibles OpenAI
- Soporte para Ollama local y Ollama Cloud
