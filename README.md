# Benchmark de Modelos AI Alternativos

**Version 1.3.0** | Ultima actualizacion: 16 de Abril de 2026

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
python benchmarks/runner.py --quick --judge                  # Con LLM-as-Judge (Claude Haiku)
python benchmarks/runner.py --models minimax-m2.7 deepseek-v3  # Modelos especificos
python benchmarks/runner.py --tier cheap                     # Solo tier economico
python benchmarks/runner.py --list-models                    # Ver modelos disponibles
python benchmarks/runner.py --list-tests                     # Ver tests disponibles
```

## Modelos Incluidos (via OpenRouter)

### Gratuitos
- DeepSeek R1, Llama 3.3 70B, Qwen 3.6 Plus (preview), **MiMo-V2-Flash (free)**

### Economicos ($0.02 - $1.20/M tokens)
- Mistral Nemo, **MiMo-V2-Flash**, DeepSeek V3.2, Gemma 4 (26B MoE, 31B), MiniMax M2.7, MiniMax M2.7 Highspeed, Gemini 2.5 Flash, Qwen 3.6 Plus, **MiMo-V2-Omni**, Llama 4 Maverick, Qwen 3.5 Plus

### Medio ($1.00 - $15/M tokens)
- **MiMo-V2-Pro**, Gemini 2.5 Pro, GPT-4o, Claude Sonnet 4

### Open Source para NVIDIA DGX Spark (128GB)
- Gemma 4 26B MoE, Gemma 4 31B, Qwen 3.5 25B/72B, Llama 3.3/4 70B, MiniMax M2.5, DeepSeek V3.2

## Benchmark Suites (77 tests en 19 suites)

| Suite | Tests | Que Evalua |
|-------|-------|-----------|
| **deep_reasoning** | 6 | Matematica, logica, causal, code bugs, Fermi, etica |
| **hallucination** | 3 | Trampas factuales, fidelidad al contexto, citas falsas |
| **creativity** | 4 | Hooks sin cliches, analogias, profundidad, storytelling |
| **customer_support** | 4 | Empatia, clasificacion, multi-issue, ingenieria social |
| **structured_output** | 4 | JSON simple, arrays, anidado, estricto |
| tool_calling | 4 | Single/multi tool, razonamiento, no-tool |
| content_generation | 4 | Blog, email, social media, product descriptions |
| startup_content | 5 | Blog ecosistemastartup.com, cursos, workshops, newsletters |
| code_generation | 4 | API integration, N8N workflows, SQL, debugging |
| reasoning | 3 | Analisis de negocio, logica, decisiones |
| task_management | 3 | Action items, planning, project breakdown |
| summarization | 2 | Resumen ejecutivo, extraccion datos |
| **string_precision** | 6 | Copia exacta de hex, API keys, JWT, config files |
| **news_seo_writing** | 5 | Articulos SEO, JSON N8N, solo espanol, anti-alucinacion, Perplexity |
| **ocr_extraction** | 5 | Facturas, tarjetas, recibos con verificacion, dashboards, notas manuscritas |
| **orchestration** | 5 | Planificacion multi-paso, error recovery, tool selection, paralelizacion |
| **multi_turn** | 4 | Iteracion de contenido, soporte escalado, cambio de requisitos, debugging |
| **policy_adherence** | 4 | Politicas de reembolso, privacidad de datos, reglas de idioma, limites de alcance |
| presentation | 2 | Slide outline, reportes de datos |

Scripts adicionales (no incluidos en el scoring global):
- `image_generation.py` - Feature images con MiniMax Image-01
- `tts_generation.py` - Text-to-speech con MiniMax Speech-02

## Resultados (12 Abril 2026)

### Ranking Global - 48 tests x modelo, 951 runs, desde Chile

| # | Modelo | Score | tok/s | Latencia | Costo/call | Open Source | Tests |
|---|--------|-------|-------|----------|------------|-------------|-------|
| 1 | **Devstral Small** | **7.38** | **161** | **3.2s** | $0.00194 | Si (Apache) | 48 |
| 2 | **GPT-4.1** | **7.14** | 110 | 5.4s | $0.00203 | No | 48 |
| 3 | **GPT-4.1 Mini** | **7.08** | 98 | 5.8s | $0.00206 | No | 48 |
| 4 | DeepSeek V3.2 | 7.01 | 34 | 16.9s | $0.00022 | Si (MIT) | 48 |
| 5 | Gemini 2.5 Flash Lite | 6.88 | 195 | 4.1s | $0.00311 | No | 48 |
| 6 | Mistral Large | 6.86 | 52 | 16.5s | $0.00296 | Si (Apache) | 48 |
| 7 | Claude Sonnet 4.6 | 6.83 | 59 | 17.6s | $0.00346 | No | 48 |
| 8 | GPT-5.4 Mini | 6.78 | 131 | 5.5s | $0.00265 | No | 48 |
| 9 | Claude Opus 4.6 | 6.77 | 49 | 20.7s | $0.00345 | No | 48 |
| 10 | Kimi K2 | 6.67 | 30 | 22.7s | $0.00248 | No | 48 |
| 11 | Llama 4 Maverick | 6.65 | 53 | 13.0s | $0.00195 | Si (Llama) | 48 |
| 12 | Qwen3 Coder | 6.61 | 60 | 20.1s | $0.00244 | Si (Apache) | 48 |
| 13 | GPT-5.4 | 6.33 | 58 | 14.0s | $0.00278 | No | 48 |
| 14 | MiniMax M2.7 | 6.27 | 45 | 29.4s | $0.00397 | Parcial | 48 |
| 15 | Qwen 3.6 Plus | 6.19 | 46 | 87.7s | $0.01033 | Si (Apache) | 48 |
| 16 | Kimi K2.5 | 5.78 | 45 | 47.1s | $0.00529 | No | 27 |

### Ranking Solo Alternativas (sin Anthropic/OpenAI)

| # | Modelo | Score | tok/s | Costo/call | Open Source | Suscripcion |
|---|--------|-------|-------|------------|-------------|-------------|
| 1 | **Devstral Small** | **7.38** | 161 | $0.00194 | Si (Apache) | Pay-as-you-go |
| 2 | DeepSeek V3.2 | 7.01 | 34 | $0.00022 | Si (MIT) | Pay-as-you-go |
| 3 | Gemini 2.5 Flash Lite | 6.88 | 195 | $0.00311 | No | Google AI Pro $20/mes |
| 4 | Mistral Large | 6.86 | 52 | $0.00296 | Si (Apache) | Le Chat ~$15/mes |
| 5 | Kimi K2 | 6.67 | 30 | $0.00248 | No | Pay-as-you-go |
| 6 | Llama 4 Maverick | 6.65 | 53 | $0.00195 | Si (Llama) | Pay-as-you-go |
| 7 | Qwen3 Coder | 6.61 | 60 | $0.00244 | Si (Apache) | Pay-as-you-go |
| 8 | MiniMax M2.7 | 6.27 | 45 | $0.00397 | Parcial | MiniMax $20-$69/mes |
| 9 | Qwen 3.6 Plus | 6.19 | 46 | $0.01033 | Si (Apache) | Qwen $50/mes |

### Mejor por Categoria

| Categoria | 1ro | 2do | 3ro |
|-----------|-----|-----|-----|
| **Razonamiento** | DeepSeek V3.2 (7.65) | Devstral (7.64) | GPT-4.1 (7.45) |
| **Agentes (tool+soporte)** | Devstral (7.21) | GPT-5.4 Mini (7.13) | Claude Opus 4.6 (7.02) |
| **Contenido** | Devstral (7.37) | GPT-4.1 Mini (7.21) | GPT-4.1 (7.14) |
| **Codigo** | Devstral (7.65) | GPT-4.1 (7.37) | DeepSeek V3.2 (7.34) |
| **Productividad** | Devstral (7.39) | GPT-4.1 (7.26) | Gemini Flash Lite (7.13) |
| **JSON/Datos** | Devstral (7.33) | Gemini Flash Lite (7.33) | GPT-4.1 (7.22) |
| **Alucinaciones** | Claude Sonnet 4.6 (7.62) | Mistral Large (7.52) | Gemini Flash Lite (7.47) |
| **Creatividad** | Devstral (6.93) | Gemini Flash (6.85) | DeepSeek V3.2 (6.75) |
| **String Precision** | Devstral (8.58) | Gemini Flash Lite (8.43) | GPT-5.4 Mini (8.38) |
| **Noticias SEO** | DeepSeek V3.2 (7.67) | Gemini Flash Lite (7.38) | Gemini Flash (7.35) |

### Hallazgos Clave

- **#1 Devstral Small**: Open-source (Apache 2.0), 161 tok/s, $0.10/$0.30 per M. Sorpresa total.
- **GPT-4.1 > GPT-5.4**: GPT-4.1 (#2) supera consistentemente a GPT-5.4 (#13) en todos los tests
- **Claude sube con tests de calidad**: Sonnet #7 y Opus #9 gracias a honestidad y soporte al cliente
- **Mas honesto**: Claude Sonnet 4.6 - #1 en alucinaciones (7.62)
- **Menos creativo**: MiniMax M2.7 ultimo en creatividad (5.19) - respuestas genericas
- **Mas rapido**: Gemini Flash Lite (195 tok/s) y Devstral (161 tok/s)
- **Mas barato**: DeepSeek V3.2 - $0.00022/call, #4 global
- **Modelos chinos**: MiniMax y Qwen a veces responden con caracteres chinos en espanol
- **LLM-as-Judge (Abril 16)**: Nuevo modo `--judge` que usa Claude Haiku como evaluador. Califica precision, relevancia, profundidad, claridad y utilidad practica en escala 1-5. Combina 30% score automatico + 70% juez. Costo ~$0.07 por modelo.
- **Scoring v2 (Abril 16)**: Corregido sesgo de formato. Ahora valida sustancia (razonamiento, honestidad, creatividad real, datos correctos). Los rankings pueden cambiar al re-correr benchmarks. Ver [CHANGELOG.md](CHANGELOG.md) para detalles.
- **Nuevos tests (18 nuevos)**: OCR/extraccion, orquestacion, multi-turno, y adherencia a politicas. Total: 77 tests en 19 suites.
- **Xiaomi MiMo**: 4 modelos nuevos incluyendo MiMo-V2-Flash (MIT, $0.09/$0.29, 73.4% SWE-Bench) - candidato serio a top 5

### Recomendacion por Caso de Uso

| Uso | Modelo Recomendado | Por que |
|-----|-------------------|---------|
| Agente general | Devstral Small | #1 global, rapido, open-source |
| Agente con tool calling | GPT-4.1 Mini | Top en tool calling, rapido |
| Agente economico | DeepSeek V3.2 | #4 global, el mas barato |
| Agente ultra rapido | Gemini 2.5 Flash Lite | 195 tok/s, 4.1s latencia |
| Agente con suscripcion fija | MiniMax M2.7 | $20-69/mes, sin sorpresas |
| Soporte al cliente | Claude Opus 4.6 | #3 en agentes, empatia superior |
| Contenido sin alucinaciones | Claude Sonnet 4.6 | #1 en honestidad (7.62) |
| Contenido creativo | Devstral Small o Gemini Flash | Top en creatividad |
| Coding/automatizaciones | Devstral o DeepSeek V3.2 | Top en coding |
| JSON/datos estructurados | Devstral o Gemini Flash Lite | Empatan #1 (7.33) |
| Open-source para DGX Spark | Llama 4 Maverick | #11, open-source, barato |

> Los resultados JSON completos estan en `benchmarks/results/`
> Ver tambien: [DESCUBRIMIENTOS.md](DESCUBRIMIENTOS.md) | [PACKS.md](PACKS.md) | [PROVEEDORES.md](PROVEEDORES.md)

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
│   ├── tests/                       # 19 suites de tests
│   └── results/                     # Resultados JSON
├── providers/
│   └── adapters.py                  # Adaptador unificado OpenAI-compatible
└── requirements.txt
```
