# CLAUDE.md - Guia para Agentes

## Que es este proyecto
Benchmark de modelos AI alternativos para uso con agentes (OpenClaw, N8N). Compara precios, calidad, velocidad, tool calling y disponibilidad. Incluye tests ejecutables y documentacion comparativa.

## Como correr benchmarks

```bash
source .venv/bin/activate
# Todos los modelos, modo rapido
python benchmarks/runner.py --quick
# Con LLM-as-Judge (auto: Gemma 4 local si Ollama, sino Haiku API)
python benchmarks/runner.py --quick --judge
# Con juez local especifico (requiere Ollama)
python benchmarks/runner.py --quick --judge --judge-model gemma4
python benchmarks/runner.py --quick --judge --judge-model glm4   # minimo sesgo
# Con juez API
python benchmarks/runner.py --quick --judge --judge-model haiku
python benchmarks/runner.py --quick --judge --judge-model google/gemini-2.5-flash
# Listar jueces disponibles
python benchmarks/runner.py --list-judges
# Modelos especificos
python benchmarks/runner.py --quick --models deepseek-v3 minimax-m2.7 mimo-v2-flash
# Solo un suite de tests
python benchmarks/runner.py --quick --tests startup_content
# Solo un tier
python benchmarks/runner.py --tier cheap --quick
# Listar modelos y tests disponibles
python benchmarks/runner.py --list-models
python benchmarks/runner.py --list-tests
```

## Como agregar un modelo nuevo

1. Agregar la config en `benchmarks/config.py` en el dict `MODELS`:
```python
"nuevo-modelo": {
    "id": "provider/model-id",  # ID de OpenRouter o del provider directo
    "name": "Nombre Legible",
    "cost_input": 0.30,  # USD por millon de tokens input
    "cost_output": 1.20,  # USD por millon de tokens output
    "tier": "cheap",  # free|ultra_cheap|cheap|medium|premium|local
    "open_source": True,  # opcional
    "license": "Apache 2.0",  # opcional
    "provider": "minimax_direct",  # opcional, si no usa OpenRouter
},
```

2. Agregar pricing en `benchmarks/scoring.py` en el dict `PRICING`
3. Correr: `python benchmarks/runner.py --quick --models nuevo-modelo`
4. Actualizar COMPARATIVA.md, PROVEEDORES.md, y README.md con resultados
5. Commit y push

## Como agregar un test nuevo

1. Crear o editar archivo en `benchmarks/tests/`
2. Formato: lista `TESTS` con dicts que tienen `name`, `description`, `messages`, y `criteria` o `expected_tools`
3. Si es nuevo archivo, importar en `benchmarks/runner.py` y agregar a `ALL_TEST_SUITES`

## Archivos clave

- `benchmarks/config.py` - API keys y modelos (gitignored, copiar de config.example.py)
- `benchmarks/runner.py` - Motor principal
- `benchmarks/scoring.py` - Sistema de puntuacion y precios
- `benchmarks/llm_judge.py` - LLM-as-Judge con rubrica en espanol
- `providers/adapters.py` - Adaptador unificado OpenAI-compatible con timeout
- `benchmarks/results/*.json` - Resultados historicos (versionados en git)

## Scoring v2 + LLM-as-Judge (Abril 2026)

- `score_content_quality`: formato 2/10, secciones 4/10, idioma 2/10, penaliza chino en espanol
- `score_expected_answer`: valida sustancia (reasoning, hallucination, creativity, depth, honesty, etc.)
- Sin juez: 40% formato + 60% sustancia
- Con juez (`--judge`): 30% automatico + 70% evaluacion del juez
- **Juez default**: Phi-4 (Microsoft, 14B, MIT) via Ollama local - cero conflicto de interes
- Tests organizados en 4 pilares: Razonamiento, Coding, Contenido/Marketing, Agentes/Operaciones

## Providers configurados

- **OpenRouter**: API key en `OPENROUTER_API_KEY` - acceso a 290+ modelos
- **OpenAI directo**: API key en `OPENAI_API_KEY` - para GPT-4.1, GPT-5.4 (usa max_completion_tokens)
- **MiniMax directo**: API key en `MINIMAX_API_KEY` - para M2.7-highspeed, imagenes
- **Xiaomi MiMo**: Via OpenRouter (`xiaomi/mimo-v2-pro`, `xiaomi/mimo-v2-flash`, `xiaomi/mimo-v2-omni`)
- **Ollama**: Local en localhost:11434 - activar con `INCLUDE_OLLAMA = True`

## Reglas del proyecto

- Siempre versionar resultados JSON en git
- Actualizar README.md con resultados cada vez que se corra un benchmark nuevo
- Actualizar CHANGELOG.md con cada version
- No re-medir modelos ya medidos en tests existentes (solo en tests nuevos)
- Actualizar TODOS los archivos cuando cambien datos (README, CHANGELOG, CheatSheet, DESCUBRIMIENTOS)
- Verificar que numeros de tests/suites/modelos esten actualizados en todos los documentos
- Hacer commit y push despues de cada sesion de benchmarks
- Los precios cambian frecuentemente - verificar antes de actualizar docs

## Contexto del usuario

- Cristian usa OpenClaw y N8N para agentes AI
- Genera contenido para ecosistemastartup.com (blog actualidad startups)
- Crea cursos para emprendedores (repo privado ctala/cursos)
- Da workshops de emprendimiento y tecnologia
- Tiene NVIDIA DGX Spark (128GB RAM) para modelos locales
- Ubicado en Chile (latencia a servidores USA)
- Suscripciones activas: OpenRouter, MiniMax (highspeed), Anthropic (API)
- Claude Code ya no viene en suscripcion Pro $20 (desde 21 abril 2026)
- DGX Spark llega la proxima semana (comprado, en camino)

## Estado actual (23 Abril 2026)

### YA COMPLETADO (no re-hacer)
- **Lote 1 con juez Phi-4**: 8 modelos × 91 tests = 728 runs -> `benchmark_20260422_204025.json` (partial=false, 17 errores en Llama 4 Maverick por tools 404 en OpenRouter)
- **Lote 2 con juez Phi-4**: 9 modelos × 91 tests = 819 runs -> `benchmark_20260423_051248.json` (partial=false, 18 errores 429 en Kimi K2 por rate limits)
- **Ranking consolidado**: 17 modelos en README.md v2.1.0 con tabla global, solo alternativas, mejor por categoría (12), recomendaciones por caso de uso
- Kimi K2.6 vs Claude Opus 4.7/4.6 (otro lote): `benchmark_20260422_082319.json`
- Agent capabilities: 13 modelos x 5 tests -> `benchmark_20260422_062137.json`

### MEJORAS AL RUNNER (aplicar para futuros lotes)
- **Guardado incremental atomico**: `_dump_results(partial=True)` tras cada test
- **`--resume <archivo.json>`**: retoma desde un benchmark parcial, saltea tests ya completados (match por model_id + suite + test_name)
- **Respuestas completas auditables**: cada test escribe un `.md` en `benchmarks/results/responses/<timestamp>/<modelo>__<suite>__<test>.md` con el output completo. El JSON lleva `response_file` con path relativo. **Solo aplica a corridas nuevas** — los Lotes 1 y 2 sólo tienen `response_preview[:300]`.

### Ranking actual (top 5)
1. Devstral Small 7.35 (Apache 2.0)
2. GPT-5.4 Mini 7.32
3. GPT-4.1 7.29
4. Gemini 2.5 Flash Lite 7.22 (165 tok/s — el más rápido)
5. MiMo-V2-Flash 7.20 (MIT, $0.09/$0.29, el más barato del top)

### PENDIENTE (proximas sesiones)
- **#8 MD por modelo** en `benchmarks/results/per-model/<modelo>.md` con tabla por suite + link a `response_file` (estilo GitHub, navegable sin infra)
- **#9 HTML con sliders** (calculadora personalizable) — publicable en GitHub Pages
- **#10 Devstral 2 (dic 2025) + Devstral Medium** — nuevas versiones post-Small 1.1
- **#11 Candidatos Ollama**: Qwen 3-Next 80B, Qwen3-Coder-Next, Ministral-3, LFM2 24B, GLM-OCR
- **#12 Ollama Cloud provider**: Cristian tiene suscripción → testear `qwen3.5:397b-cloud` (el que usa en prod para ecosistemastartup.com)
- **#7 Providers directos (Groq/Fireworks/Together)**: desbloquea Llama 4 Maverick + tools (hoy falla con 404 en OpenRouter)
- **#5 Log mejorado**: incluir modelo en cada línea + elapsed + ETA basado en seg/test recientes
- **Llegada DGX Spark**: correr todos los Ollama locales que quepan (~110B Q4, 70B FP16)
- Ver ROADMAP.md para pipeline completo

### COMO CONTINUAR
```bash
# Ver último resultado
ls -lt benchmarks/results/benchmark_*.json | head -3

# Correr modelos nuevos (ejemplo Devstral 2)
source .venv/bin/activate
python benchmarks/runner.py --quick --judge --judge-model phi4 --models devstral-2

# Si se corta, resume desde archivo parcial
python benchmarks/runner.py --quick --judge --judge-model phi4 --models <modelos> --resume benchmarks/results/benchmark_YYYYMMDD_HHMMSS.json
```
