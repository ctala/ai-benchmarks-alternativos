# Benchmark de Modelos AI Alternativos

**Version 0.3.0** | Ultima actualizacion: 11 de Abril de 2026

Proyecto para evaluar y comparar modelos de IA para uso con agentes (OpenClaw, N8N) y asistentes personales. Incluye benchmarks propios ejecutables, comparativas de precios, y guia de modelos open-source para hardware local (NVIDIA DGX Spark).

> **Contexto**: La suscripcion de Anthropic no provee API key para agentes. Buscamos alternativas priorizando costo, calidad, velocidad, tool calling y disponibilidad continua.

## Documentos Principales

| Documento | Contenido |
|-----------|-----------|
| [COMPARATIVA.md](COMPARATIVA.md) | 35+ modelos con precios, open-source/propietario, licencias, rankings por categoria |
| [SUSCRIPCIONES.md](SUSCRIPCIONES.md) | Todas las suscripciones fijas ($0-$300/mes) + checklist de que probar |
| [PACKS.md](PACKS.md) | Packs por suscripcion (MiniMax, Qwen, OpenAI, Google, Ollama, OpenRouter, xAI) + estrategia local+nube |
| [CHANGELOG.md](CHANGELOG.md) | Historial de cambios del proyecto |

## Criterios de Evaluacion

| Criterio | Peso | Descripcion |
|----------|------|-------------|
| Costo | 25% | Precio por millon de tokens o suscripcion mensual fija |
| Calidad | 25% | Precision, coherencia, seguimiento de instrucciones |
| Velocidad | 20% | Tokens/segundo y latencia de primera respuesta |
| Tool Calling | 20% | Capacidad de function calling para agentes |
| Disponibilidad | 10% | Rate limits, cuotas, que no se quede sin servicio |

## Quick Start

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp benchmarks/config.example.py benchmarks/config.py
# Editar config.py con tu OPENROUTER_API_KEY
python benchmarks/runner.py --quick                          # Todos los modelos, 1 run
python benchmarks/runner.py --models minimax-m2.7 deepseek-v3  # Modelos especificos
python benchmarks/runner.py --tier cheap                     # Solo tier economico
python benchmarks/runner.py --list-models                    # Ver modelos disponibles
python benchmarks/runner.py --list-tests                     # Ver tests disponibles
```

## Modelos Incluidos (via OpenRouter)

### Gratuitos
- DeepSeek R1, Llama 3.3 70B, Qwen 3.6 Plus (preview)

### Economicos ($0.02 - $1.20/M tokens)
- Mistral Nemo, DeepSeek V3.2, Gemma 4 (26B MoE, 31B), MiniMax M2.7, MiniMax M2.7 Highspeed, Gemini 2.5 Flash, Qwen 3.6 Plus, Llama 4 Maverick, Qwen 3.5 Plus

### Medio ($1.25 - $15/M tokens)
- Gemini 2.5 Pro, GPT-4o, Claude Sonnet 4

### Open Source para NVIDIA DGX Spark (128GB)
- Gemma 4 26B MoE, Gemma 4 31B, Qwen 3.5 25B/72B, Llama 3.3/4 70B, MiniMax M2.5, DeepSeek V3.2

## Benchmark Suites (18 tests)

| Suite | Tests | Que Evalua |
|-------|-------|-----------|
| content_generation | 4 | Blog, email, social media, product descriptions |
| tool_calling | 4 | Single/multi tool, razonamiento, no-tool |
| task_management | 3 | Action items, planning, project breakdown |
| code_generation | 4 | API integration, N8N workflows, SQL, debugging |
| reasoning | 3 | Analisis de negocio, logica, decisiones |
| summarization | 2 | Resumen ejecutivo, extraccion JSON |
| presentation | 2 | Slide outline, reportes de datos |
| startup_content | 5 | Blog ecosistemastartup.com, cursos, workshops, newsletters, research |

## Estructura

```
├── README.md                        # Este archivo
├── COMPARATIVA.md                   # Comparativa completa de modelos
├── SUSCRIPCIONES.md                 # Suscripciones mensuales
├── CHANGELOG.md                     # Historial de cambios
├── benchmarks/
│   ├── config.example.py            # Configuracion ejemplo
│   ├── config.py                    # Tu configuracion (gitignored)
│   ├── runner.py                    # Motor de benchmarks
│   ├── scoring.py                   # Sistema de puntuacion
│   ├── tests/                       # 7 suites de tests
│   └── results/                     # Resultados JSON
├── providers/
│   └── adapters.py                  # Adaptador unificado OpenAI-compatible
└── requirements.txt
```
