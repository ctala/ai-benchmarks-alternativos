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

## Scoring v2 + LLM-as-Judge

- `score_content_quality` — formato 2/10, secciones 4/10, idioma 2/10, penaliza chino en español
- `score_expected_answer` — valida sustancia (reasoning, hallucination, creativity, honesty, datos)
- Sin juez: 40% formato + 60% sustancia
- Con juez (`--judge`): 30% automático + 70% evaluación del juez
- **Juez default**: Phi-4 (Microsoft, 14B, MIT) via Ollama local — cero conflicto de interés
- Tests organizados en 4 pilares: Razonamiento, Coding, Contenido/Marketing, Agentes/Operaciones

## Providers configurados

- **OpenRouter** (`OPENROUTER_API_KEY`) — acceso a 290+ modelos
- **OpenAI directo** (`OPENAI_API_KEY`) — GPT-4.1, GPT-5.4, GPT-5.5 (usa `max_completion_tokens` para thinking models)
- **MiniMax directo** (`MINIMAX_API_KEY`) — M2.7-highspeed
- **Xiaomi MiMo** — via OpenRouter (`xiaomi/mimo-v2-pro|flash|omni`)
- **Ollama local** — `localhost:11434`, activar con `INCLUDE_OLLAMA = True`
- **Ollama Cloud** — pendiente implementar (el usuario tiene suscripción activa)

## Reglas del proyecto

- **Guardado atómico**: el runner vuelca JSON tras cada test, no esperar al final
- **Versionar resultados JSON** siempre en git
- **Flujo ROADMAP↔CHANGELOG**: todo lo que se marca completo en ROADMAP.md migra a CHANGELOG.md con el commit
- **3 cortes de ranking en README**: global, solo alternativas (sin Anthropic/OpenAI), y solo open-source — siempre los 3 al actualizar resultados
- **API keys**: las 4 keys (OPENROUTER, OPENAI, MINIMAX, OLLAMA_CLOUD) viven en `.env` (gitignored). Nunca hardcodear en config.py ni imprimir en chat. Usar `len()` para validar presencia.
- **Regenerar MDs** tras cada lote: `python benchmarks/generate_per_model_md.py`
- **README.md + CHANGELOG.md** se actualizan cuando cambia el ranking o se agrega un modelo
- **No re-medir** modelos ya medidos en tests existentes (solo en tests nuevos)
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
