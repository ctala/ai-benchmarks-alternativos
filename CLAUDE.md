# CLAUDE.md - Guia para Agentes

> **Relación con `AGENTS.md`**: `AGENTS.md` es la guía canónica de **recomendación de modelos** —filosofía, schema de `docs/data/models.json`, reglas por caso de uso y anti-patrones. `CLAUDE.md` es la guía técnica del **proyecto y pipeline**. Antes de recomendar un modelo, leer `AGENTS.md`; antes de modificar código, tests o docs, leer esta guía.

## Que es este proyecto
Benchmark de modelos AI alternativos para uso con agentes (N8N, Hermes). Compara precios, calidad, velocidad, tool calling y disponibilidad. Incluye tests ejecutables, LLM-as-Judge local (Phi-4) y documentación comparativa.

## Setup inicial

```bash
# Entorno virtual (recomendado)
python3 -m venv .venv
source .venv/bin/activate

# Deps
pip install -r requirements.txt  # incluye python-dotenv

# API keys: crear .env a partir del template (gitignored)
cp .env.example .env
# Editar .env con tus keys reales (OPENROUTER, OPENAI, MINIMAX, OLLAMA_CLOUD, XIAOMI_API_KEY, etc.)

# Config de modelos: primera vez
# benchmarks/config.py y benchmarks/models.py YA están en el repo.
# Solo necesitas .env con tus API keys.
```

>  🚨 **ANTES de correr un lote de medición o un backfill: leé [`RUNBOOK-MEDICION.md`](RUNBOOK-MEDICION.md).**
>  Tiene el patrón correcto a la primera (paralelizar N runners para modelos cloud — el runner
>  va secuencial y eso es 10× más lento —, resume de nombre fijo idempotente contra los kills del
>  entorno, costo calculado antes, y dónde va / dónde NO va el filtro de procedencia). Existe porque
>  esas lecciones se redescubrieron y re-rompieron varias veces; el runbook es para que no vuelva a pasar.

## Como correr benchmarks

```bash
source .venv/bin/activate
# Todos los modelos, modo rapido
.venv/bin/python benchmarks/runner.py --quick
# Con juez local Phi-4 (default)
.venv/bin/python benchmarks/runner.py --quick --judge --judge-model phi4
# Otros jueces
.venv/bin/python benchmarks/runner.py --quick --judge --judge-model gemma4   # local, alt
.venv/bin/python benchmarks/runner.py --quick --judge --judge-model haiku    # API
.venv/bin/python benchmarks/runner.py --list-judges
# Modelos especificos (keys de benchmarks/models.py)
.venv/bin/python benchmarks/runner.py --quick --judge --judge-model phi4 --models devstral-small deepseek-v4-flash
# Un solo test suite
.venv/bin/python benchmarks/runner.py --quick --tests startup_content
# Solo un tier
.venv/bin/python benchmarks/runner.py --tier cheap --quick
# Listar
.venv/bin/python benchmarks/runner.py --list-models
.venv/bin/python benchmarks/runner.py --list-tests
# Resumir benchmark parcial (si se cortó)
.venv/bin/python benchmarks/runner.py --quick --judge --judge-model phi4 --models <modelos> \
    --resume benchmarks/results/benchmark_YYYYMMDD_HHMMSS.json
```

El runner **guarda incrementalmente** tras cada test y puede continuar desde cualquier punto. También guarda la respuesta completa por test en `benchmarks/results/responses/<timestamp>/<modelo>__<suite>__<test>.md` (auditable desde GitHub).

## Como agregar un modelo nuevo

1. **`benchmarks/models.py`** — agregar al dict `MODELS` (publico, en git) con `cost_input`/`cost_output` en USD por millón de tokens:
```python
"nuevo-modelo": {
    "id": "provider/model-id",       # ID de OpenRouter o del provider directo
    "name": "Nombre Legible",
    "cost_input": 0.30,              # USD por millon de tokens input
    "cost_output": 1.20,             # USD por millon de tokens output
    "tier": "cheap",                 # free|ultra_cheap|cheap|medium|premium|local|cloud_*
    "open_source": True,             # opcional
    "license": "Apache 2.0",         # opcional
    "provider": "openai_direct",     # opcional si no es OpenRouter
    "context_window": 131072,        # opcional
},
```
2. (Opcional) **`benchmarks/scoring.py`** — agregar al dict `PRICING` solo como fallback si el runner no recibe costos del config.
3. Correr: `.venv/bin/python benchmarks/runner.py --quick --judge --judge-model phi4 --models nuevo-modelo`
4. **Regenerar todos los artefactos**: `.venv/bin/python benchmarks/regenerate_all.py`
5. Actualizar README.md (ranking, recomendaciones) y CHANGELOG.md si cambia el ranking.
6. Commit + push

## Como agregar un test nuevo

1. Crear/editar archivo en `benchmarks/tests/`
2. Formato: lista `TESTS` con dicts `{name, description, messages, criteria|expected_tools, expected_answer}`
3. Si es archivo nuevo, importarlo en `benchmarks/runner.py` y agregar a `ALL_TEST_SUITES`

## Archivos clave

- `benchmarks/models.py` — Catálogo público de modelos: `MODELS` + `OLLAMA_MODELS` (en git, fuente única)
- `benchmarks/config.py` — Lee env vars de `.env`, importa MODELS de models.py
- `benchmarks/runner.py` — Motor principal, acepta `--resume`, `--rerun-empty`, `--rerun-failed`
- `benchmarks/scoring.py` — Sistema de puntuación, pesos (referencia congelada v4.0) y dict `PRICING` (fallback)
- `benchmarks/llm_judge.py` — LLM-as-Judge con rúbrica en español (presets phi4/phi4-spark/phi4-vllm)
- `benchmarks/export_for_pages.py` — Genera `docs/data/models.json` (single source of truth)
- `benchmarks/regenerate_all.py` — Pipeline maestro que regenera todos los artefactos derivados
- `benchmarks/generate_per_model_md.py` — Regenera MDs navegables desde JSON
- `providers/adapters.py` — Adaptador unificado OpenAI-compatible con timeout y manejo de thinking models
- `benchmarks/results/*.json` — Resultados históricos versionados en git
- `benchmarks/results/responses/<timestamp>/` — Respuestas completas por test (nuevas corridas)
- `benchmarks/results/per-model/` — MDs navegables por modelo con ranking + link a responses

## Estándar del benchmark para thinking models

Constantes en `providers/adapters.py` (cima del archivo) — **este es el estándar oficial** que aplica a todos los lotes. Editar si tu hardware/budget difiere.

| Constante | Valor | Razón |
|---|---|---|
| `THINKING_MODELS` | `gpt-5*`, `o1*`, `o3*`, `glm-5*`, `kimi-k2.6`, `kimi-k2.7`, `nemotron*`, `gemini-2.5-pro`, `gemini-3-pro`, `gemini-3.1-pro`, `deepseek-v4`, `deepseek-r`, `gemma4`, `gemma-4`, `minimax-m3`, `qwen3.7-max`, `qwen3.7-plus` | Modelos que consumen tokens internos de reasoning facturados como output |
| `FIXED_TEMP_MODELS` | `gpt-5.5`, `gpt-5-pro`, `gpt-5.5-pro`, `o1`, `o3` | Modelos que rechazan `temperature` ≠ 1.0 (error 400). El adapter omite el parámetro |
| `THINKING_TOKEN_MULTIPLIER` | `4` | max_tokens × 4 para thinking. Sin esto agotan el budget razonando y retornan `content=""` |
| `THINKING_MIN_TOKENS` | `8192` | Piso absoluto de output para thinking. Para que respuestas largas (blog, workshop) no queden cortadas |
| `HTTP_READ_TIMEOUT_S` | `360.0` | httpx read_timeout. Subido de 60s → 240s → 360s. Última subida abril 27 tras 2 timeouts residuales en DeepSeek V4 Pro con prompts largos (workshop_outline, perplexity_research razonan >240s). |
| `REQUEST_TIMEOUT` (en `config.py`) | `300` | signal alarm timeout total — backup si httpx no aborta |
| `max_tokens` default (en `runner.py`) | `2048` | Output estándar para non-thinking. Multiplicado por 4 = 8192 para thinking |
| `temperature` default | `0.7` | Para todos los no-FIXED_TEMP_MODELS |

**Cómo modificar**: editar las constantes en `providers/adapters.py` (todas con sus razones explicadas inline). Cambios típicos:
- Bajar `max_tokens` a 1024 → ahorra costo, respuestas más cortas
- Subir `max_tokens` a 4096 → respuestas más largas (cuidado: thinking models facturarán 16384)
- Agregar nuevo modelo a `THINKING_MODELS` cuando lance otro proveedor un thinking model
- Subir `HTTP_READ_TIMEOUT_S` si tu modelo razona >240s (raro)

**Origen del estándar**: detectado abril 25 2026 — 165 runs vacíos de thinking models con `max_tokens=2048` original + 6 timeouts de GPT-5.5 con `read=60s`. Tras el fix, GPT-5.5 subió de 5.76 a 6.41+ (sigue subiendo con la re-corrida de timeouts).

## Scoring v4.0 (z-score congelado) + LLM-as-Judge

El `score_global` es una **función ponderada y z-scoreada** de 4 componentes (ver `benchmarks/scoring.py`). **Desde v4.0 la referencia del z-score (mean/std por dimensión) está CONGELADA por versión** en `scoring_reference.json` (`score_method: zscore_frozen_v4`): agregar un modelo nuevo NO recalcula el score de los demás. La referencia solo se recalcula con `export_for_pages.py --recalibrate --scoring-version vX.Y` (evento de versión deliberado). Los pesos default siguen siendo 70/15/7.5/7.5:

| Componente | Peso default | Qué mide |
|---|---|---|
| Quality | **70%** | Phi-4 judge + criterios automáticos (formato + sustancia) |
| Cost | **15%** | Curva log inversa; todos los modelos tienen un costo mínimo de **$0.001/call** para comparabilidad |
| Speed | **7.5%** | Tokens/s promedio |
| Latency | **7.5%** | Latencia **total** de respuesta — se promedia `latency_total` (ver `export_for_pages.py`), NO time-to-first-token. Decirle TTFT en los docs es un claim que la data no sostiene |

- Cada dimensión se estandariza (z-score) antes de ponderar → el peso nominal = influencia real.
- Tool calling y seguridad son **badges/dimensiones separadas**, no entran en el compuesto.
- Sin juez: 40% formato + 60% sustancia
- Con juez (`--judge`): 30% automático + 70% evaluación del juez
- **Juez default**: Phi-4 (Microsoft, 14B, MIT) via Ollama local — cero conflicto de interés. También disponibles presets `phi4-spark` (DGX Spark LAN) y `phi4-vllm` (FP16 continuous batching en Spark).
- Tests organizados en 4 pilares prácticos: Razonamiento, Coding, Contenido/Marketing, Agentes/Operaciones. Long-context (`niah_es`) y seguridad (`prompt_injection_es`) se reportan como dimensiones aparte.

## Providers configurados

- **OpenRouter** (`OPENROUTER_API_KEY`) — acceso a 290+ modelos
- **OpenAI directo** (`OPENAI_API_KEY`) — `/v1/chat/completions` para GPT-4.1, GPT-5.4, GPT-5.5 (usa `max_completion_tokens` para thinking)
- **OpenAI Responses** (`OPENAI_API_KEY`) — `/v1/responses` para gpt-5.5-pro / o1-pro (no funcionan en chat/completions). Provider key: `openai_responses`. Captura `reasoning_tokens` aparte en `metadata`.
- **Claude Code subscription** (`ANTHROPIC_API_KEY` + login de suscripción) — Opus 4.6/4.7/4.8, Sonnet 4.6, Haiku 4.5, Fable 5. Provider key: `claude_code`. Accede por CLI de Anthropic; costo real $0/call para benchmarks, pero se normaliza al precio OpenRouter equivalente en el score global.
- **MiniMax directo** (`MINIMAX_API_KEY`) — M2.7, M2.7-highspeed, M3.
- **Kimi / MoonshotAI** (`MOONSHOT_API_KEY` o `KIMI_API_KEY`) — Kimi K2 / K2.5 / K2.6 / K2.7 Code.
- **Groq directo** (`GROQ_API_KEY`) — Llama 3.3 70B, GPT-OSS 120/20B (LPU latencia ultra baja).
- **NVIDIA NIM** (`NVIDIA_NIM_API_KEY`) — catálogo de modelos GRATIS con 40 RPM. Provider key: `nvidia_nim`. Incluye Nemotron, Qwen 3-Next, Mistral-Nemotron, Kimi K2 thinking, DeepSeek V4.
- **Ollama local** — `localhost:11434`, activar con `INCLUDE_OLLAMA = True` en `config.py`.
- **Ollama Cloud** (`OLLAMA_CLOUD_API_KEY`) — modelos cloud de Ollama, incluyendo Qwen 3.5 397B Cloud.
- **Xiaomi MiMo** (`XIAOMI_API_KEY`) — suscripción mensual con créditos; modelos V2.5 family. Provider key: `xiaomi_direct`.
- **NVIDIA NIM Local** (`NIM_LOCAL_BASE_URL`) — containers NIM en DGX Spark u otro hardware NVIDIA propio. Provider key: `nim_local`.
- **Diffusion CLI** (`diffusion_cli`) — adapter para DiffusionGemma vía `llama-diffusion-cli` en DGX Spark. No requiere API key; corre local.

## Familia Qwen: Base (open) vs Plus/Max (closed)

Tres tiers en la oferta Alibaba — distinción importante para el ranking "open source":

| Tier | Pesos | Ejemplos | Cómo usar |
|---|---|---|---|
| **Base** | ✅ Apache 2.0 (HuggingFace) | Qwen 3.6, Qwen3-Coder, Qwen 3.5 base | Ollama local, OpenRouter |
| **Plus** | ❌ API-only propietario | Qwen 3.6 Plus, Qwen 3.5 Plus | Alibaba DashScope, OpenRouter |
| **Max** | ❌ API-only premium | Qwen Max | Alibaba DashScope |

⚠️ Error común en los configs: poner `open_source: True` para "Qwen 3.6 Plus" porque el nombre dice "Qwen 3.6". El Plus es **derivado y propietario** — no se publican pesos. Verificar siempre antes de marcar open_source.

## Agentes disponibles (`.claude/agents/`)

11 agentes pre-hechos descargados de [wshobson/agents](https://github.com/wshobson/agents). Detalles + estrategia por fase en [.claude/agents/README.md](.claude/agents/README.md).

**SEO + Marketing (7)**:
- `seo-content-writer`, `seo-content-auditor`, `seo-keyword-strategist`, `seo-structure-architect`, `seo-meta-optimizer`, `content-marketer`, `search-specialist`

**Análisis y Documentación (4 — abril 26)**:
- `data-scientist` — análisis cuantitativo de benchmark JSONs → `INSIGHTS.md` (Fase 1)
- `business-analyst` — traduce insights a decisiones de negocio
- `docs-architect` — `ARQUITECTURA.md` con depth técnica del repo (Fase 2)
- `tutorial-engineer` — `tutoriales/` con 5 guías paso a paso

**Workaround actual**: los `.md` locales en `.claude/agents/` no se registran como `subagent_type` invocable hasta reload de Claude Code. Mientras tanto se invocan via `general-purpose` pasando el contenido del agente como contexto. Todos tienen `Use PROACTIVELY` para auto-invocación post-reload.

**Outputs auto-generados por agentes** (NO editar a mano):
- `INSIGHTS.md` — regenerado post-cada-lote por data-scientist
- `ARQUITECTURA.md` — regenerado cuando cambia arquitectura del runner/scoring
- `tutoriales/*.md` — actualizar al cambiar API del runner o agregar features

## Reglas del proyecto

- **Guardado atómico**: el runner vuelca JSON tras cada test, no esperar al final
- **Versionar resultados JSON** siempre en git
- **Flujo ROADMAP↔CHANGELOG**: todo lo que se marca completo en ROADMAP.md migra a CHANGELOG.md con el commit
- **3 cortes de ranking en README**: (1) **global** = todos los modelos. (2) **solo alternativas** = sin Anthropic + sin OpenAI + sin Google propietarios (Gemini Flash / Flash Lite / Pro). Sí se permiten modelos Google open-source (Gemma). (3) **solo open-source** = todos los modelos con `open_source: True`. Siempre los 3 al actualizar resultados.
- **No modificar prompts de tests**. Los prompts y criterios de `benchmarks/tests/` son la línea base de comparabilidad del benchmark. Cambios de stack de producción (p. ej. OpenClaw → Hermes) se reflejan en `README.md`, `CLAUDE.md` y generadores pSEO, **nunca en los tests**. Si hay que medir algo nuevo, se agrega como suite/test adicional; no se reescribe uno existente.
- **API keys**: las 4 keys (OPENROUTER, OPENAI, MINIMAX, OLLAMA_CLOUD) viven en `.env` (gitignored). Nunca hardcodear en config.py ni imprimir en chat. Usar `len()` para validar presencia.
- **Regla de auto-generación**: antes de cualquier commit que toque benchmarks/results/, config, tests o docs/, ejecutar el pipeline maestro:
  ```bash
  .venv/bin/python benchmarks/regenerate_all.py
  ```
  El pipeline regenera en orden: `docs/data/models.json`, `MODELOS.md`, `TESTS.md`, MDs por modelo, rankings/comparaciones pSEO, `sitemap.xml`, `llms.txt`, `og-benchmark.png` y sincroniza counts en README/ROADMAP/landings via `sync_doc_counts.py`. Usar `--skip-og-image` si PIL no está disponible.
  - **Páginas pSEO programáticas** (rankings y comparaciones) filtran modelos con cobertura sólida y usan `docs/data/models.json` como fuente única. Para agregar una página nueva se edita la config de `generate_rankings.py` / `generate_comparison.py`; no se escribe HTML a mano. **Cada vez que se agreguen modelos nuevos o cambien scores, regenerar estas páginas para que los rankings por dimensión individual sigan actualizados.**
- **GitHub Action de seguridad** (`.github/workflows/regenerate-auto-artifacts.yml`): si olvidás los pasos manualmente, el bot regenera los artefactos al hacer push. Pero hacelo manual primero para que el commit principal lleve los cambios sincronizados (mejor experiencia de revisión). **Pendiente:** agregar los generadores pSEO (paso 7) a esta Action para que las páginas se actualicen solas con cada lote.
- **README.md + CHANGELOG.md** se actualizan cuando cambia el ranking o se agrega un modelo
- **No re-medir modelos ya cubiertos**. Re-correr SÓLO si:
  1. Sale **versión nueva** del modelo (ej. Kimi K2.7, Devstral 3) — distinto ID = distinto modelo, se mide.
  2. Cambian las **suites/tests** del benchmark (suite nueva, criterios de scoring diferentes).
  3. Se detecta un **bug del runner/adapter** que invalida runs previos (ej. fix de max_tokens para thinking, abril 2026 → re-run sólo de los empties con `--rerun-empty`).
  4. El modelo tuvo cambios visibles del proveedor (silent retraining anunciado, cambio de pricing radical, etc).
  No re-medir por: refactor del runner, mejoras cosméticas, formato de output, regeneración de MDs por modelo.
- **Endpoints caducos: chequear ANTES de un lote grande.**
  ```bash
  .venv/bin/python benchmarks/check_endpoints.py --ranked        # solo reporta
  .venv/bin/python benchmarks/check_endpoints.py --ranked --fix  # marca retired: True
  ```
  Manda un ping de 1 token a cada modelo y clasifica: **MUERTO** (deprecated / no
  endpoints / invalid model → se retira) · **INTERMITENTE** (429, 5xx, timeout → NO se
  toca, el modelo existe) · **SIN CREDENCIAL** (falta la key del provider, no es culpa
  del modelo). La distinción importa: marcar como muerto a uno que solo tuvo un timeout
  sería tan malo como lo contrario.

  **Por qué existe:** el 13-jul-2026, a mitad de un backfill de ~$44, se descubrió que
  **4 modelos del ranking ya no existían**. Uno era **Devstral Small, #5** — alguien
  podía leerlo, integrarlo y estrellarse. Nos enteramos tarde y caro, porque el lote se
  estrelló contra ellos. Este chequeo cuesta centavos y lo detecta antes.

  **Y el error inverso, que casi cometo:** marqué como muerto a Llama 3.1 8B (Groq), que
  estaba **perfectamente vivo**. Lo que faltaba era `GROQ_API_KEY`. Sin la key, el runner
  caía **en silencio** a OpenRouter — que no conoce el id de Groq
  (`llama-3.3-70b-versatile`; ahí se llama `meta-llama/llama-3.3-70b-instruct`) — y
  respondía *"not a valid model ID"*, un error **idéntico** al de un modelo retirado.
  Hoy `providers/registry.py` levanta `MissingCredential` en vez de caer a OpenRouter, y
  esos modelos quedan `unavailable` (**siguen rankeados** con sus runs históricos; solo no
  reciben runs nuevos). Una credencial que falta no es un modelo que murió.

  Un modelo `retired: True` queda **fuera del ranking y de las recomendaciones** (un
  modelo que no puedes usar no es un candidato), pero **sigue en los datos**: sus runs
  son reales y alimentan el análisis histórico. Se muestra en la sección *Retirados* de
  MODELOS.md. El runner también los omite (`--include-retired` para forzarlos).

- **Verificar consistencia** entre docs: conteos de modelos/tests/suites deben coincidir.
  ```bash
  .venv/bin/python benchmarks/check_consistency.py   # exit 1 si un doc vivo cita un score obsoleto
  ```
  **Correrlo antes de cada push** (y antes de publicar contenido que cite cifras). Compara los
  scores citados en los docs **vivos** (README, MODELOS, CLAUDE, AGENTS, RECOMENDACIONES,
  COMPARATIVA) contra `models.json`. Ignora a propósito los **snapshots con fecha** (CHANGELOG,
  DATASHEET_*, INSIGHTS): esos DEBEN conservar el valor del momento — reescribir la historia
  sería el bug, no el fix.
- **Nunca escribir un score a mano en un doc vivo.** El z-score se recalcula con cada modelo
  nuevo, así que toda cifra hardcodeada caduca sola. Si necesitás citar una, que salga de un
  generador; si es narrativa (un párrafo), el `check_consistency.py` te avisa cuando caduca.
- **Nunca $0 como precio de un modelo del ranking.** Un modelo "gratis" (tier `:free` de
  OpenRouter, NIM 40 RPM) gana el eje costo artificialmente y engaña la decisión — que es
  exactamente lo que la calculadora existe para evitar. Usar el precio real: el de OpenRouter
  si existe versión paga, o el del proveedor de origen (ej. NIM pago de NVIDIA) si OpenRouter
  solo lista `:free`. Si hay que ESTIMAR un precio, se estima con disclaimer en `notes` — pero
  $0 nunca. Fallo real (14-jul-2026): 2 Nemotron a $0 se colaron al top 10; con precio real de
  NVIDIA cayeron a #13 y #31.
- **First-party = misma calidad por OpenRouter; NO duplicar.** Si un modelo se midió por la
  API directa de su creador (OpenAI, Moonshot, MiniMax midiendo SU propio modelo), esa medición
  cuenta en el ranking: OpenRouter es un intermediario y la calidad es la misma. NO crear una
  fila `or-<modelo>` vacía "para medirlo en el plano común" — queda un duplicado con 0 runs que
  confunde. Esto SOLO vale para first-party: en Groq/NIM/Ollama Cloud la calidad SÍ cambia por
  serving (cuantización/config — caso Qwen 3.5 397B: 7.96 en NIM vs 5.46 en Ollama Cloud) y la
  variante se mide aparte como `provider_variant`.
- **Un (id, name) = UNA config en MODELS.** El export asigna los runs por `(model_id, name)`:
  dos configs con el mismo par reciben LOS MISMOS runs y el modelo aparece duplicado con todo
  contado dos veces (pasó con Kimi K2.5 y Gemma 4 31B, dedup 14-jul-2026). Antes de agregar un
  modelo, `grep` su id en `models.py`.
- **Al analizar models.json, indexar SIEMPRE por `key`, nunca por `name`.** Un dict
  `{x['name']: x}` colapsa silenciosamente las entradas que comparten nombre (directa + `or-`,
  variantes) y te deja leyendo la que quedó última — que puede ser la vacía. Fallo real
  (14-jul-2026): "GPT-4.1 no está medido (Q=None)" cuando la entrada real tenía 169 runs; el
  análisis leyó el twin `or-gpt-4.1` con 0 runs y una conclusión falsa llegó a borrar una
  sección correcta del pilar del blog.
- **Actualizar el pilar del blog cuando el ranking cambie materialmente.** El post vivo
  `benchmark-de-modelos-de-ia-2026-...` en el repo hermano `~/Playground/sitios/cristiantala-blog/`
  es un cornerstone SEO (top-3 Google) que cita cifras de `models.json` en prosa, tablas y FAQ. Un
  rescoring las caduca TODAS (y puede dejar modelos citados sin data o una recomendación de seguridad
  peligrosa). Tras `regenerate_all.py`, si el top 10 / la tesis / la seguridad se movieron:
  verificar CADA cifra del `.md` contra `models.json` (guardrail estilo `check_consistency`), bumpear
  `updatedDate` **solo con cambio real** (de ahí salen `dateModified`/FAQPage/sitemap `<lastmod>` —
  frescura automática), y NO crear un post mensual paralelo (canibaliza). Procedimiento completo:
  paso 9 del skill `linkedin-benchmark-carousel`. Fallo que lo motivó: 14-jul-2026.
- **Commit y push** después de cada sesión
- **Precios cambian** — verificar antes de actualizar docs
- **Plan antes de push** — operaciones destructivas o públicas requieren confirmación

## Contexto del usuario

- Cristian usa **N8N y Hermes** para agentes AI
- Genera contenido para **ecosistemastartup.com** (blog de actualidad startups)
- Usa **Claude Code** como IDE/coding agent con varios modelos, incluyendo **MiniMax M3** y familias Claude/Opus
- En producción evalúa Qwen 3.5 397B Cloud, MiniMax M2.7/M3 y Kimi K2.7 Code para el blog
- Crea cursos para emprendedores (repo privado `ctala/cursos`)
- Da workshops de emprendimiento y tecnología
- Tiene NVIDIA **DGX Spark (128GB RAM)** para modelos locales — operativo
- Ubicado en Chile (latencia a servidores USA)
- Suscripciones activas: OpenRouter, MiniMax (Agent Pro / highspeed), Anthropic (Claude Code), Kimi / MoonshotAI, Ollama Cloud, Xiaomi MiMo, xAI SuperGrok

## Estado actual (v4.0.0, 17 Julio 2026) — ver ROADMAP.md para plan completo

### Ranking actual — NO se copia acá, se lee de la fuente

**El ranking vivo está en el README** (bloque `<!-- AUTO-RANKING -->`, auto-generado) y en
`docs/data/models.json`. **Este archivo ya no lo duplica, a propósito.**

Por qué: el `score_global` es un **z-score**. **Desde v4.0 la referencia (mean/std por
dimensión) está CONGELADA por versión** en `scoring_reference.json` (`score_method:
zscore_frozen_v4`): agregar/medir un modelo nuevo ya **NO recalcula el score de los demás** —
se puntúa contra la referencia fija. Los scores solo se reajustan al publicar una versión nueva
(`export_for_pages.py --recalibrate --scoring-version vX.Y`, evento deliberado). **Aun así, no
hardcodees un score en un doc vivo**: entre versiones cambian, y un ranking copiado a mano queda
obsoleto (pasó en julio 2026: el README publicaba Grok 4.5 = 6.99 mientras el sitio mostraba 5.84).

Para ver el ranking al día:
```bash
.venv/bin/python -c "import json;d=json.load(open('docs/data/models.json'));\
r=sorted([m for m in d['models'] if m['ranked']],key=lambda x:-x['score_global'])[:10];\
[print(f\"{i}. {m['name']} — {m['score_global']} ({m['runs']} runs)\") for i,m in enumerate(r,1)]"
```

**Dos umbrales, no uno** (definidos en `export_for_pages.py`, todo el pipeline los importa):
- `MIN_RUNS_TESTED = 20` → cobertura suficiente para **reportar** el modelo (`tested`).
- `MIN_RUNS_RANKED = 50` → muestra suficiente para **rankearlo** (`ranked`). Con 3-12 runs un
  modelo puede liderar por azar. Los que no llegan se publican en *En evaluación* (MODELOS.md)
  con el score marcado como indicativo.

### Infraestructura actual
- **DGX Spark (GB10, 128GB)** operativo en LAN — corre Ollama + vLLM Phi-4 judge + modelos locales Q4/Q8.
- **vLLM Phi-4 FP16** (:8001) como juez principal para sweeps paralelos. Ollama local sigue disponible como backup.
- **Pipeline maestro**: `benchmarks/regenerate_all.py` regenera todos los artefactos desde `docs/data/models.json`.
- **Calculadora web**: https://benchmarks.cristiantala.com/ — sirve `docs/data/models.json` desde GitHub Pages.

### Próximo trabajo inmediato (ver ROADMAP.md)
- **Release julio 2026**: DATASHEET_2026-07.md, CheatSheet PDF mensual julio, tag semver.
- **Tier 1 pendientes**: Nemotron 3 Ultra 550B, Qwen 3.7 Plus, Cohere North Mini Code, Poolside Laguna, Claude Opus 4.8 Fast, Grok 4.3.
- **Tech debt**:TESTS_FALTANTES.md auto-regen, drift de ids (devstral-small, grok-4.1-fast), suite multimodal/visión.

### Contexto del usuario (actualizado)
- Cristian usa **N8N y Hermes** para agentes AI; genera contenido para **ecosistemastartup.com**.
- Usa **Claude Code** como coding agent/IDE con varios modelos, incluyendo **MiniMax M3**, Claude Sonnet/Opus y Kimi K2.7 Code.
- **DGX Spark operativo** para modelos locales y juicio Phi-4 vLLM.
- Suscripciones activas: OpenRouter, MiniMax (Agent Pro / highspeed), Anthropic (Claude Code), Kimi / MoonshotAI, Ollama Cloud, Xiaomi MiMo, xAI SuperGrok.
- Producción actual para blog: evaluando alternativas entre MiniMax M2.7/M3, Qwen 3.5 397B Cloud y Kimi K2.7 Code.
