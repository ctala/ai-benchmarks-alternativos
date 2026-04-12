# CLAUDE.md - Guia para Agentes

## Que es este proyecto
Benchmark de modelos AI alternativos para uso con agentes (OpenClaw, N8N). Compara precios, calidad, velocidad, tool calling y disponibilidad. Incluye tests ejecutables y documentacion comparativa.

## Como correr benchmarks

```bash
source .venv/bin/activate
# Todos los modelos, modo rapido
python benchmarks/runner.py --quick
# Modelos especificos
python benchmarks/runner.py --quick --models deepseek-v3 minimax-m2.7 gemma-4-31b
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
- `providers/adapters.py` - Adaptador unificado OpenAI-compatible con timeout
- `benchmarks/results/*.json` - Resultados historicos (versionados en git)

## Providers configurados

- **OpenRouter**: API key en `OPENROUTER_API_KEY` - acceso a 290+ modelos
- **OpenAI directo**: API key en `OPENAI_API_KEY` - para GPT-4.1, GPT-5.4 (usa max_completion_tokens)
- **MiniMax directo**: API key en `MINIMAX_API_KEY` - para M2.7-highspeed, imagenes
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
