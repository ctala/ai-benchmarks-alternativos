# Benchmark de Modelos AI Alternativos

**Version 0.8.0** | Ultima actualizacion: 12 de Abril de 2026

Proyecto para evaluar y comparar modelos de IA para uso con agentes (OpenClaw, N8N) y asistentes personales. Incluye benchmarks propios ejecutables, comparativas de precios, y guia de modelos open-source para hardware local (NVIDIA DGX Spark).

> **Contexto**: La suscripcion de Anthropic no provee API key para agentes. Buscamos alternativas priorizando costo, calidad, velocidad, tool calling y disponibilidad continua.

## Documentos Principales

| Documento | Contenido |
|-----------|-----------|
| [COMPARATIVA.md](COMPARATIVA.md) | 35+ modelos con precios, open-source/propietario, licencias, rankings por categoria |
| [SUSCRIPCIONES.md](SUSCRIPCIONES.md) | Todas las suscripciones fijas ($0-$300/mes) + checklist de que probar |
| [PACKS.md](PACKS.md) | Packs por suscripcion (MiniMax, Qwen, OpenAI, Google, Ollama, OpenRouter, xAI) + estrategia local+nube |
| [PROVEEDORES.md](PROVEEDORES.md) | Guia de proveedores: quien los creo, foco, contexto, open-source vs propietario |
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
| image_generation | 5 | Feature images WordPress (MiniMax Image-01) para Discover/SEO |
| tts_generation | 4 | Text-to-speech (MiniMax Speech-02) para newsletters, cursos, podcasts |

## Resultados (11 Abril 2026)

### Ranking Global - 21 Modelos (27 tests x modelo, desde Chile)

| # | Modelo | Score | tok/s | Latencia | Costo/call | Open Source |
|---|--------|-------|-------|----------|------------|-------------|
| 1 | **Devstral Small** | **7.40** | **171** | **3.8s** | $0.00233 | Si (Apache) |
| 2 | **GPT-4.1** | **7.28** | 118 | 6.4s | $0.00233 | No |
| 3 | **GPT-4.1 Mini** | **7.20** | 110 | 6.6s | $0.00247 | No |
| 4 | DeepSeek V3.2 | 7.09 | 36 | 18.8s | $0.00024 | Si (MIT) |
| 5 | Gemini 2.5 Flash Lite | 6.95 | 212 | 4.7s | $0.00362 | No |
| 6 | Mistral Large | 6.80 | 54 | 19.0s | $0.00341 | Si (Apache) |
| 7 | GPT-5.4 Mini | 6.74 | 142 | 6.4s | $0.00316 | No |
| 8 | MiniMax M2.7 Highspeed | 6.74 | 51 | 26.1s | $0.00421 | Parcial |
| 9 | Claude Sonnet 4.6 | 6.70 | 62 | 21.1s | $0.00415 | No |
| 10 | Llama 4 Maverick | 6.70 | 58 | 15.8s | $0.00231 | Si (Llama) |
| 11 | MiniMax M2.7 | 6.68 | 57 | 26.5s | $0.00431 | Parcial |
| 12 | Qwen3 Coder | 6.62 | 52 | 27.0s | $0.00287 | Si (Apache) |
| 13 | Claude Opus 4.6 | 6.59 | 54 | 24.3s | $0.00417 | No |
| 14 | Gemma 4 26B MoE | 6.53 | 19 | 42.2s | $0.00246 | Si (Apache) |
| 15 | Kimi K2 | 6.49 | 31 | 27.5s | $0.00294 | No |
| 16 | GPT-5.4 | 6.25 | 65 | 14.8s | $0.00320 | No |
| 17 | Qwen 3.6 Plus | 6.07 | 47 | 83.1s | $0.00995 | Si (Apache) |
| 18 | Kimi K2.5 | 5.78 | 45 | 47.1s | $0.00529 | No |

### Ranking Solo Alternativas (sin Anthropic/OpenAI)

| # | Modelo | Score | tok/s | Costo/call | Open Source | Suscripcion |
|---|--------|-------|-------|------------|-------------|-------------|
| 1 | **Devstral Small** | **7.40** | 171 | $0.00233 | Si (Apache) | Pay-as-you-go |
| 2 | DeepSeek V3.2 | 7.09 | 36 | $0.00024 | Si (MIT) | Pay-as-you-go |
| 3 | Gemini 2.5 Flash Lite | 6.95 | 212 | $0.00362 | No | Google AI Pro $20/mes |
| 4 | Mistral Large | 6.80 | 54 | $0.00341 | Si (Apache) | Le Chat ~$15/mes |
| 5 | MiniMax M2.7 HS | 6.74 | 51 | $0.00421 | Parcial | MiniMax $20-$69/mes |
| 6 | Llama 4 Maverick | 6.70 | 58 | $0.00231 | Si (Llama) | Pay-as-you-go |
| 7 | MiniMax M2.7 | 6.68 | 57 | $0.00431 | Parcial | MiniMax $20-$69/mes |
| 8 | Qwen3 Coder | 6.62 | 52 | $0.00287 | Si (Apache) | Pay-as-you-go |
| 9 | Kimi K2 | 6.49 | 31 | $0.00294 | No | Pay-as-you-go |
| 10 | Qwen 3.6 Plus | 6.07 | 47 | $0.00995 | Si (Apache) | Qwen $50/mes |

### Mejor por Categoria

| Categoria | 1ro | 2do | 3ro |
|-----------|-----|-----|-----|
| **Tool Calling** | GPT-5.4 Mini (7.5) | GPT-5.4 (7.3) | Claude Sonnet 4.6 (6.9) |
| **Content** | GPT-5.4 Mini (7.2) | Gemini Flash Lite (7.2) | MiniMax M2.7 (6.8) |
| **Coding** | DeepSeek V3.2 (7.3) | Gemini Flash Lite (7.2) | MiniMax M2.7 (7.0) |
| **Reasoning** | DeepSeek V3.2 (7.5) | MiniMax M2.7 HS (6.8) | Claude Sonnet 4.6 (6.7) |
| **Startup Content** | DeepSeek V3.2 (7.3) | Gemini Flash Lite (6.9) | MiniMax M2.7 HS (6.6) |
| **Task Mgmt** | DeepSeek V3.2 (7.2) | Gemini Flash Lite (7.0) | MiniMax M2.7 HS (6.8) |

### Hallazgos Clave

- **#1 Devstral Small**: Open-source (Apache 2.0), 171 tok/s, ultra barato. Sorpresa total.
- **GPT-4.1 > GPT-5.4**: Generaciones anteriores superan a las nuevas en nuestros tests
- **Mas rapido**: Gemini 2.5 Flash Lite (212 tok/s) y Devstral (171 tok/s)
- **Mas barato con calidad**: DeepSeek V3.2 - $0.00024/call, #4 global
- **Claude Opus 4.6 es #13**: El modelo mas caro no rinde en scoring automatico
- **Mejor suscripcion fija**: MiniMax ($20-69/mes) con M2.7
- **Nota sobre scoring**: Evalua formato y estructura, no profundidad de razonamiento. Opus destaca en calidad que no se captura automaticamente

### Recomendacion para Agentes N8N/OpenClaw

| Uso | Modelo Recomendado | Por que |
|-----|-------------------|---------|
| Agente con tool calling | GPT-4.1 Mini o GPT-5.4 Mini | Top en tool calling |
| Agente economico | DeepSeek V3.2 | #4 global, el mas barato |
| Agente ultra rapido | Devstral Small o Gemini Flash Lite | 171-212 tok/s |
| Agente con suscripcion fija | MiniMax M2.7 | $20-69/mes, sin sorpresas |
| Agente open-source | Llama 4 Maverick | Empata con Claude, open-source |
| Coding/automatizaciones | Qwen3 Coder o DeepSeek V3.2 | Top en coding |
| Contenido ecosistemastartup.com | DeepSeek V3.2 | #1 en startup content |
| Feature images WordPress | MiniMax Image-01 | 5/5 exitosos, 16-60s |

> Los resultados JSON completos estan en `benchmarks/results/`

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
