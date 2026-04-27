# CLAUDE.md - Guia para Agentes

## Que es este proyecto
Benchmark de modelos AI alternativos para uso con agentes (OpenClaw, N8N). Compara precios, calidad, velocidad, tool calling y disponibilidad. Incluye tests ejecutables, LLM-as-Judge local (Phi-4) y documentación comparativa.

## Setup inicial

```bash
# Deps
pip install -r requirements.txt  # incluye python-dotenv

# API keys: crear .env a partir del template (gitignored)
cp .env.example .env
# Editar .env con tus keys reales (OPENROUTER, OPENAI, MINIMAX, OLLAMA_CLOUD)

# Config de modelos: primera vez
cp benchmarks/config.example.py benchmarks/config.py
```

## Como correr benchmarks

```bash
source .venv/bin/activate
# Todos los modelos, modo rapido
python benchmarks/runner.py --quick
# Con juez local Phi-4 (default)
python benchmarks/runner.py --quick --judge --judge-model phi4
# Otros jueces
python benchmarks/runner.py --quick --judge --judge-model gemma4   # local, alt
python benchmarks/runner.py --quick --judge --judge-model haiku    # API
python benchmarks/runner.py --list-judges
# Modelos especificos
python benchmarks/runner.py --quick --judge --judge-model phi4 --models devstral deepseek-v3
# Un solo test suite
python benchmarks/runner.py --quick --tests startup_content
# Solo un tier
python benchmarks/runner.py --tier cheap --quick
# Listar
python benchmarks/runner.py --list-models
python benchmarks/runner.py --list-tests
# Resumir benchmark parcial (si se cortó)
python benchmarks/runner.py --quick --judge --judge-model phi4 --models <modelos> \
    --resume benchmarks/results/benchmark_YYYYMMDD_HHMMSS.json
```

El runner **guarda incrementalmente** tras cada test y puede continuar desde cualquier punto. También guarda la respuesta completa por test en `benchmarks/results/responses/<timestamp>/<modelo>__<suite>__<test>.md` (auditable desde GitHub).

## Como agregar un modelo nuevo

1. **`benchmarks/config.py`** — agregar al dict `MODELS`:
```python
"nuevo-modelo": {
    "id": "provider/model-id",       # ID de OpenRouter o del provider directo
    "name": "Nombre Legible",
    "cost_input": 0.30,              # USD por millon de tokens input
    "cost_output": 1.20,             # USD por millon de tokens output
    "tier": "cheap",                 # free|ultra_cheap|cheap|medium|premium|local|cloud_ollama
    "open_source": True,             # opcional
    "license": "Apache 2.0",         # opcional
    "provider": "openai_direct",     # opcional si no es OpenRouter
},
```
2. **`benchmarks/scoring.py`** — agregar pricing al dict `PRICING`
3. Correr: `python benchmarks/runner.py --quick --judge --judge-model phi4 --models nuevo-modelo`
4. **Regenerar MDs por modelo**: `python benchmarks/generate_per_model_md.py`
5. Actualizar README.md (ranking, recomendaciones) y CHANGELOG.md
6. Commit + push

## Como agregar un test nuevo

1. Crear/editar archivo en `benchmarks/tests/`
2. Formato: lista `TESTS` con dicts `{name, description, messages, criteria|expected_tools, expected_answer}`
3. Si es archivo nuevo, importarlo en `benchmarks/runner.py` y agregar a `ALL_TEST_SUITES`

## Archivos clave

- `benchmarks/config.py` — API keys y dict `MODELS` (gitignored, copiar de `config.example.py`)
- `benchmarks/runner.py` — Motor principal, acepta `--resume`
- `benchmarks/scoring.py` — Sistema de puntuación y dict `PRICING`
- `benchmarks/llm_judge.py` — LLM-as-Judge con rúbrica en español
- `benchmarks/generate_per_model_md.py` — Regenera MDs navegables desde JSON
- `providers/adapters.py` — Adaptador unificado OpenAI-compatible con timeout
- `benchmarks/results/*.json` — Resultados históricos versionados en git
- `benchmarks/results/responses/<timestamp>/` — Respuestas completas por test (nuevas corridas)
- `benchmarks/results/per-model/` — MDs navegables por modelo con ranking + link a responses

## Estándar del benchmark para thinking models

Constantes en `providers/adapters.py` (cima del archivo) — **este es el estándar oficial** que aplica a todos los lotes. Editar si tu hardware/budget difiere.

| Constante | Valor | Razón |
|---|---|---|
| `THINKING_MODELS` | `gpt-5*`, `o1*`, `o3*`, `glm-5*`, `kimi-k2.6`, `nemotron*`, `gemini-2.5-pro`, `gemini-3-pro`, `deepseek-v4`, `deepseek-r` | Modelos que consumen tokens internos de reasoning facturados como output |
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

## Scoring v2 + LLM-as-Judge

- `score_content_quality` — formato 2/10, secciones 4/10, idioma 2/10, penaliza chino en español
- `score_expected_answer` — valida sustancia (reasoning, hallucination, creativity, honesty, datos)
- Sin juez: 40% formato + 60% sustancia
- Con juez (`--judge`): 30% automático + 70% evaluación del juez
- **Juez default**: Phi-4 (Microsoft, 14B, MIT) via Ollama local — cero conflicto de interés
- Tests organizados en 4 pilares: Razonamiento, Coding, Contenido/Marketing, Agentes/Operaciones

## Providers configurados

- **OpenRouter** (`OPENROUTER_API_KEY`) — acceso a 290+ modelos
- **OpenAI directo** (`OPENAI_API_KEY`) — `/v1/chat/completions` para GPT-4.1, GPT-5.4, GPT-5.5 (usa `max_completion_tokens` para thinking)
- **OpenAI Responses** (`OPENAI_API_KEY`) — `/v1/responses` para gpt-5.5-pro / o1-pro (no funcionan en chat/completions). Provider key: `openai_responses`. Captura `reasoning_tokens` aparte en `metadata`.
- **MiniMax directo** (`MINIMAX_API_KEY`) — M2.7-highspeed
- **Groq directo** (`GROQ_API_KEY`) — Llama 3.3 70B, GPT-OSS 120/20B (LPU latencia ultra baja)
- **NVIDIA NIM** (`NVIDIA_NIM_API_KEY`) — catálogo de 135+ modelos GRATIS con 40 RPM (suficiente para benchmarks secuenciales). Provider key: `nvidia_nim`. Joyas no disponibles en otros providers: Nemotron Ultra 253B, Qwen 3-Next 80B (instruct + thinking), Mistral-Nemotron, Kimi K2 thinking, DeepSeek V4. Catálogo en build.nvidia.com.
- **Ollama local** — `localhost:11434`, activar con `INCLUDE_OLLAMA = True`
- **Ollama Cloud** (`OLLAMA_CLOUD_API_KEY`) — qwen3.5:397b-cloud (Cristian usa este en producción)
- **Xiaomi MiMo** (`XIAOMI_API_KEY`) — suscripción mensual con 8 modelos (V2.5-Pro, V2.5, V2-Pro, V2-Omni, V2.5-TTS family). Provider key: `xiaomi_direct`. Base URL: `https://token-plan-sgp.xiaomimimo.com/v1`. Off-peak 16-24 UTC = 0.8x consumption.

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
- **API keys**: las 4 keys (OPENROUTER, OPENAI, MINIMAX, OLLAMA_CLOUD) viven en `.env` (gitignored). Nunca hardcodear en config.py ni imprimir en chat. Usar `len()` para validar presencia.
- **Regla de auto-generación**: antes de cualquier commit que toque benchmarks/results/, config, tests o docs/, ejecutar EN ORDEN:
  1. `python benchmarks/generate_per_model_md.py` — regenera MDs por modelo
  2. `python benchmarks/generate_modelos_md_table.py -i` — regenera tabla de MODELOS.md con links
  3. `python benchmarks/generate_tests_md.py` — regenera TESTS.md con prompts completos
  4. `python benchmarks/export_for_pages.py` — regenera docs/data/models.json para la calculadora
  5. `python benchmarks/generate_sitemap.py` — regenera docs/sitemap.xml (lee lastmod desde git, descubre landing pages auto)
- **GitHub Action de seguridad** (`.github/workflows/regenerate-auto-artifacts.yml`): si olvidás los pasos manualmente, el bot regenera los artefactos al hacer push. Pero hacelo manual primero para que el commit principal lleve los cambios sincronizados (mejor experiencia de revisión).
- **README.md + CHANGELOG.md** se actualizan cuando cambia el ranking o se agrega un modelo
- **No re-medir modelos ya cubiertos**. Re-correr SÓLO si:
  1. Sale **versión nueva** del modelo (ej. Kimi K2.7, Devstral 3) — distinto ID = distinto modelo, se mide.
  2. Cambian las **suites/tests** del benchmark (suite nueva, criterios de scoring diferentes).
  3. Se detecta un **bug del runner/adapter** que invalida runs previos (ej. fix de max_tokens para thinking, abril 2026 → re-run sólo de los empties con `--rerun-empty`).
  4. El modelo tuvo cambios visibles del proveedor (silent retraining anunciado, cambio de pricing radical, etc).
  No re-medir por: refactor del runner, mejoras cosméticas, formato de output, regeneración de MDs por modelo.
- **Verificar consistencia** entre docs: conteos de modelos/tests/suites deben coincidir
- **Commit y push** después de cada sesión
- **Precios cambian** — verificar antes de actualizar docs
- **Plan antes de push** — operaciones destructivas o públicas requieren confirmación

## Contexto del usuario

- Cristian usa OpenClaw y N8N para agentes AI
- Genera contenido para **ecosistemastartup.com** (blog de actualidad startups)
- En producción usa **`qwen3.5:397b-cloud`** via Ollama Cloud para ese blog
- Crea cursos para emprendedores (repo privado `ctala/cursos`)
- Da workshops de emprendimiento y tecnología
- Tiene NVIDIA **DGX Spark (128GB RAM)** para modelos locales — llega ~próxima semana
- Ubicado en Chile (latencia a servidores USA)
- Suscripciones: OpenRouter, MiniMax (highspeed), Anthropic API, **Ollama Cloud**
- Claude Code ya no viene en suscripción Pro $20 (desde 21 abril 2026)

## Estado actual (25 Abril 2026) — ver ROADMAP.md para plan completo

### Ranking v2.2 top 5 (27 modelos × 91 tests, Phi-4 judge)
1. **Devstral Small** 7.35 (Apache 2.0, $0.10/$0.30, 146 tok/s)
2. **GPT-5.4 Mini** 7.32 (117 tok/s)
3. **GPT-4.1** 7.29 (80 tok/s)
4. **Gemini 2.5 Flash Lite** 7.22 (165 tok/s — el más rápido)
5. **Devstral 2 (Dic 2025)** 7.22 (Apache 2.0, $0.40/$2.00) — empate técnico con Flash Lite

### JSON de resultados v2.2
- `benchmark_20260422_204025.json` — Lote 1 (8 modelos × 91)
- `benchmark_20260423_051248.json` — Lote 2 (9 modelos × 91)
- `benchmark_20260424_053942.json` — Lote 3 (10 modelos × 91)
- `benchmark_20260424_071523.json` — Smoke test Ollama Cloud (qwen3.5:397b-cloud, 3 tests)
- Otros: `benchmark_20260422_082319.json` (Kimi K2.6 vs Claude), `benchmark_20260422_062137.json` (agent_capabilities)

### Próximo trabajo inmediato (queue)

1. **#15 DeepSeek V4** — lanzado 24 abril, verificar ID OpenRouter y agregar
2. **MiMo V2.5 + V2.5-Pro** (Xiaomi) — multimodal nuevo abril 2026, agregar al config
3. **Modelos pendientes sin testear**: GPT-OSS 120B/20B, GPT-5.5 (cuando aparezca), Grok 4.1 Fast, Hermes 4, Gemini 3.1 Flash Lite, Muse Spark, Step 3.5 Flash
4. **#7 Providers directos** (Groq/Fireworks/Together) → desbloquea Llama 4 Maverick + tools
5. **Lote 4** con todos los nuevos (~12-15 modelos)
6. **#16 Investigación de suscripciones** — comparar costo-eficiencia con ranking v2.2
7. **#9 HTML con sliders** (calculadora personalizable)
8. **DGX Spark cuando llegue** — barrido modelos Ollama locales

### Modelos cloud_ollama configurados (Ollama Cloud)
- `qwen3.5-397b-cloud` (qwen3.5:397b-cloud) — usado por Cristian en producción
- `qwen3.5-cloud` (qwen3.5:cloud)
- `gpt-oss-120b-cloud` (gpt-oss:120b-cloud)
Smoke test confirmó endpoint funcional.
