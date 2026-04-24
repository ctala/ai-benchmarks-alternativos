# Benchmark de Modelos AI Alternativos

**Version 2.1.0** | Ultima actualizacion: 23 de Abril de 2026

Benchmark de modelos AI para emprendedores y equipos que usan agentes (OpenClaw, N8N, Hermes). Evalua modelos en los 4 pilares del emprendedor: **Razonamiento, Coding, Contenido/Marketing, y Agentes/Operaciones**. Incluye LLM-as-Judge local con Phi-4 (Microsoft, cero conflicto de interes).

> **Contexto**: Desde el 21 de abril 2026, Claude Code ya no viene en la suscripcion Pro de $20/mes. Este benchmark ayuda a encontrar las mejores alternativas por caso de uso y presupuesto.

## Documentos Principales

| Documento | Contenido |
|-----------|-----------|
| [COMPARATIVA.md](COMPARATIVA.md) | 35+ modelos con precios, open-source/propietario, licencias |
| [SUSCRIPCIONES.md](SUSCRIPCIONES.md) | Suscripciones fijas ($0-$300/mes) + coding plans |
| [PACKS.md](PACKS.md) | Packs por suscripcion + estrategia local+nube |
| [PROVEEDORES.md](PROVEEDORES.md) | Proveedores: fundacion, foco, contexto, open-source |
| [RECOMENDACIONES.md](RECOMENDACIONES.md) | Que modelo usar por plataforma (OpenClaw, N8N, Hermes), tarea y presupuesto |
| [CASOS_DE_USO.md](CASOS_DE_USO.md) | 50+ casos de uso reales de IA para emprendedores |
| [DESCUBRIMIENTOS.md](DESCUBRIMIENTOS.md) | Hallazgos no obvios y bugs de modelos |
| [ROADMAP.md](ROADMAP.md) | Roadmap y pipeline de mejoras futuras |
| [CHANGELOG.md](CHANGELOG.md) | Historial de cambios |

## Criterios de Evaluacion

| Criterio | Peso | Descripcion |
|----------|------|-------------|
| Costo | 25% | Precio por millon de tokens o suscripcion mensual fija |
| Calidad | 25% | Precision, coherencia, seguimiento de instrucciones |
| Velocidad | 20% | Tokens/segundo y latencia de primera respuesta |
| Tool Calling | 20% | Capacidad de function calling para agentes |
| Disponibilidad | 10% | Rate limits, cuotas, que no se quede sin servicio |

## Metodologia

```mermaid
flowchart TD
    subgraph INPUT["Entrada"]
        T["91 Tests en 23 Suites"]
        M["30+ Modelos via OpenRouter"]
    end

    subgraph EXEC["Ejecucion"]
        R["runner.py envia test al modelo"]
        RESP["Modelo genera respuesta"]
        R --> RESP
    end

    subgraph SCORING["Scoring (3 capas)"]
        direction TB
        S1["<b>Capa 1: Automatico</b>
        Longitud, secciones, idioma, formato
        Penalizacion: chino en espanol
        Busqueda Unicode-aware"]

        S2["<b>Capa 2: Expected Answer</b>
        Razonamiento, alucinaciones,
        creatividad, honestidad,
        datos numericos, precision"]

        S3["<b>Capa 3: LLM-as-Judge</b>
        Gemma 4 31B local o API
        precision, relevancia,
        profundidad, claridad,
        utilidad practica"]

        S1 --> COMBINE
        S2 --> COMBINE
        S3 -->|"--judge"| COMBINE
    end

    subgraph COMBINE["Combinacion"]
        direction TB
        NOJUDGE["Sin juez: 40% formato + 60% sustancia"]
        WITHJUDGE["Con juez: 30% auto + 70% juez"]
    end

    subgraph METRICS["Score Final Ponderado"]
        direction LR
        Q["Calidad 35%"]
        TC["Tool Calling 25%"]
        CO["Costo 15%"]
        AV["Disponibilidad 15%"]
        SP["Velocidad 5%"]
        LA["Latencia 5%"]
    end

    subgraph OUTPUT["Salida"]
        JSON["results/*.json"]
        RANK["Ranking Global"]
        CAT["Mejor por Categoria"]
    end

    T --> R
    M --> R
    RESP --> S1
    RESP --> S2
    RESP --> S3
    COMBINE --> METRICS
    METRICS --> JSON
    JSON --> RANK
    JSON --> CAT

    style INPUT fill:#1a1a2e,stroke:#e94560,color:#fff
    style EXEC fill:#16213e,stroke:#0f3460,color:#fff
    style SCORING fill:#0f3460,stroke:#533483,color:#fff
    style COMBINE fill:#533483,stroke:#e94560,color:#fff
    style METRICS fill:#1a1a2e,stroke:#e94560,color:#fff
    style OUTPUT fill:#16213e,stroke:#0f3460,color:#fff
```

### Flujo detallado

1. **Entrada**: Cada test (prompt + criterios + expected_answer) se envia a cada modelo via OpenRouter
2. **Scoring automatico** (Capa 1): Regex verifica longitud, secciones, idioma, formato. Penaliza caracteres chinos en espanol.
3. **Expected answer** (Capa 2): Valida que la respuesta contenga los insights correctos, no alucine, sea creativa sin cliches, y tenga datos precisos.
4. **LLM-as-Judge** (Capa 3, opcional con `--judge`): Un modelo juez lee la respuesta y la evalua con rubrica en 5 dimensiones + criterios extras por suite.
5. **Combinacion**: Sin juez usa 40% formato + 60% sustancia. Con juez usa 30% automatico + 70% evaluacion del juez.
6. **Score final**: Pondera calidad (35%), tool calling (25%), costo (15%), disponibilidad (15%), velocidad (5%), latencia (5%).

### Eleccion del modelo juez y sesgo

El modelo juez introduce sesgo: un LLM tiende a puntuar mejor respuestas de su propio proveedor (~5-7% de inflacion documentada). Por eso la eleccion importa:

| Juez | Costo | Sesgo | Recomendacion |
|------|-------|-------|---------------|
| **Gemma 4 31B (local)** | **$0** | **Bajo** | **Default - buena calidad, gratis, Apache 2.0** |
| GLM-4.7 9B (local) | $0 | Minimo | No esta en benchmark = 0 conflicto de interes |
| Qwen 3.5 72B (local) | $0 | Bajo | Maxima calidad si tienes 42GB+ RAM |
| Claude Haiku (API) | ~$0.07/modelo | Medio | Rapido pero sesga modelos Anthropic |
| Gemini Flash (API) | ~$0.05/modelo | Medio | Rapido pero sesga modelos Google |

El default es **Phi-4 (Microsoft, 14B, MIT)** via Ollama. Phi-4 fue elegido porque:
- Microsoft **no tiene modelos en nuestro benchmark** = cero conflicto de interes
- 14B parametros = buena calidad de evaluacion
- MIT license = cualquiera puede replicar
- ~9 GB, cabe en hardware modesto
- 3-9 segundos por evaluacion

```bash
python benchmarks/runner.py --list-judges                      # Ver jueces disponibles
python benchmarks/runner.py --quick --judge                    # Auto: Phi-4 local
python benchmarks/runner.py --quick --judge --judge-model phi4 # Phi-4 explicito
python benchmarks/runner.py --quick --judge --judge-model haiku # Claude Haiku via API (backup)
```

## Quick Start

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp benchmarks/config.example.py benchmarks/config.py
# Editar config.py con tu OPENROUTER_API_KEY
python benchmarks/runner.py --quick                          # Todos los modelos, 1 run
python benchmarks/runner.py --quick --judge                  # Con LLM-as-Judge (Phi-4 local)
python benchmarks/runner.py --models minimax-m2.7 deepseek-v3  # Modelos especificos
python benchmarks/runner.py --tier cheap                     # Solo tier economico
python benchmarks/runner.py --list-models                    # Ver modelos disponibles
python benchmarks/runner.py --list-tests                     # Ver tests disponibles
```

## Como Replicar el Benchmark

Guia paso a paso para correr el benchmark completo desde cero.

### Requisitos
- Python 3.11+
- API key de [OpenRouter](https://openrouter.ai/) (unica key necesaria, da acceso a 290+ modelos)
- (Opcional) [Ollama](https://ollama.ai/) para modelos locales y LLM-as-Judge local

### Paso 1: Setup

```bash
git clone https://github.com/ctala/ai-benchmarks-alternativos.git
cd ai-benchmarks-alternativos
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp benchmarks/config.example.py benchmarks/config.py
```

Edita `benchmarks/config.py` y agrega tu `OPENROUTER_API_KEY`.

### Paso 2: Elegir modelos

En `config.py`, comenta/descomenta los modelos que quieras evaluar. Para una prueba rapida:

```bash
# Solo 2 modelos baratos, 1 run por test
python benchmarks/runner.py --quick --models deepseek-v3 mimo-v2-flash
```

### Paso 3: Correr benchmark

```bash
# Rapido sin juez (~5 min por modelo)
python benchmarks/runner.py --quick

# Con LLM-as-Judge para resultados confiables (~8 min por modelo)
python benchmarks/runner.py --quick --judge

# Con juez local via Ollama ($0, requiere Ollama + modelo descargado)
ollama pull gemma4:31b
python benchmarks/runner.py --quick --judge --judge-model gemma4

# Benchmark completo (3 runs por test, mas preciso, ~15 min por modelo)
python benchmarks/runner.py --judge
```

### Paso 4: Resultados

Los resultados se guardan en `benchmarks/results/benchmark_YYYYMMDD_HHMMSS.json` con:
- Scores por test y modelo (calidad, tool calling, velocidad, costo)
- Metadata del juez usado (modelo, proveedor, local/API) para trazabilidad
- Rankings global y por categoria en la consola

### Paso 5: Agregar un modelo nuevo

```bash
# 1. Agregar en config.py (ver config.example.py para formato)
# 2. Agregar pricing en scoring.py dict PRICING
# 3. Correr
python benchmarks/runner.py --quick --judge --models mi-nuevo-modelo
# 4. Actualizar docs con resultados
```

### Costo estimado por run completo

| Componente | Costo |
|------------|-------|
| 1 modelo, 91 tests, modo --quick | ~$0.01-0.05 (depende del modelo) |
| LLM-as-Judge (Haiku, 77 evals) | ~$0.07 |
| LLM-as-Judge (local Ollama) | $0.00 |
| Run completo 10 modelos con juez | ~$0.50-1.00 |
| Run completo 10 modelos, 3 runs, con juez | ~$1.50-3.00 |

## Modelos Incluidos (via OpenRouter)

### Gratuitos
- DeepSeek R1, Llama 3.3 70B, MiMo-V2-Flash (free)

### Ultra Economicos (<$0.10/M tokens)
- Mistral Nemo, **Nemotron 3 Nano**, MiMo-V2-Flash

### Economicos ($0.10 - $1.20/M tokens)
- Nemotron 3 Super, DeepSeek V3.2, Mistral Small 4, Grok 4.1 Fast, Gemini 3.1 Flash Lite, MiniMax M2.7, Gemini 2.5 Flash, Qwen 3.6 Plus, Devstral 2, MiMo-V2-Omni, **GLM-5.1**, **Kimi K2.6**, Qwen 3.5 Plus, Llama 4 Maverick, Qwen3 Coder

### Medio y Premium ($1.00+/M tokens)
- MiMo-V2-Pro, Gemini 2.5 Pro, Gemini 3.1 Pro, Grok 4.20, GPT-4o, GPT-4.1, Claude Sonnet 4.6, **Claude Opus 4.7**, GPT-5.4/Mini

### Open Source para NVIDIA DGX Spark (128GB)
- **Nemotron 3 Super** (16 GB), **Nemotron 3 Nano** (4 GB), Gemma 4 26B MoE, Gemma 4 31B, Qwen 3.5 25B/72B, Llama 3.3/4 70B, MiniMax M2.5, DeepSeek V3.2

## Benchmark Suites (91 tests en 23 suites)

Organizadas en los 4 pilares del emprendedor:

### Pilar 1: Razonamiento y Estrategia
| Suite | Tests | Que Evalua |
|-------|-------|-----------|
| deep_reasoning | 6 | Matematica, logica, causal, code bugs, Fermi, etica |
| reasoning | 3 | Analisis de negocio, logica, decisiones |
| hallucination | 3 | Trampas factuales, fidelidad al contexto, citas falsas |
| **strategy** | 3 | Competitor analysis, pricing, business model validation |

### Pilar 2: Coding y Datos
| Suite | Tests | Que Evalua |
|-------|-------|-----------|
| code_generation | 4 | API integration, N8N workflows, SQL, debugging |
| structured_output | 4 | JSON simple, arrays, anidado, estricto |
| string_precision | 6 | Copia exacta de hex, API keys, JWT, config files |
| ocr_extraction | 5 | Facturas, tarjetas, recibos, dashboards, notas manuscritas |

### Pilar 3: Contenido y Marketing
| Suite | Tests | Que Evalua |
|-------|-------|-----------|
| content_generation | 4 | Blog, email, social media, product descriptions |
| startup_content | 5 | Blog ecosistemastartup.com, cursos, workshops, newsletters |
| news_seo_writing | 5 | Articulos SEO, JSON N8N, solo espanol, Perplexity |
| creativity | 4 | Hooks sin cliches, analogias, profundidad, storytelling |
| **sales_outreach** | 3 | Cold email, lead qualification, campaign optimization |
| **translation** | 3 | Marketing es-en, tecnica en-es, deteccion de problemas idioma |
| presentation | 2 | Slide outline, reportes de datos |

### Pilar 4: Agentes y Operaciones
| Suite | Tests | Que Evalua |
|-------|-------|-----------|
| tool_calling | 4 | Single/multi tool, razonamiento, no-tool |
| customer_support | 4 | Empatia, clasificacion, multi-issue, ingenieria social |
| orchestration | 5 | Planificacion multi-paso, error recovery, tool selection |
| multi_turn | 4 | Iteracion, soporte escalado, cambio de requisitos |
| policy_adherence | 4 | Reembolsos, privacidad, reglas de idioma, limites |
| **agent_capabilities** | 5 | Skills, delegacion sub-agentes, agent teams, routing |
| task_management | 3 | Action items, planning, project breakdown |
| summarization | 2 | Resumen ejecutivo, extraccion datos |

## Resultados (Abril 2026) — Scoring v2 + Phi-4 Judge

> Ranking completo con **17 modelos × 91 tests cada uno = 1512 corridas** evaluadas por Phi-4 (Microsoft, 14B, MIT) corriendo local via Ollama. Juez local sin conflicto de interes. Resultados JSON: `benchmarks/results/benchmark_20260422_204025.json` (Lote 1) + `benchmark_20260423_051248.json` (Lote 2).

### Ranking Global (Phi-4 judge, 91 tests)

| # | Modelo | Final | Calidad | tok/s | Open Source | OK/Total |
|---|--------|-------|---------|-------|-------------|----------|
| 1 | **Devstral Small** | **7.35** | 7.91 | 146 | Si (Apache 2.0) | 91/91 |
| 2 | **GPT-5.4 Mini** | **7.32** | 7.88 | 117 | No | 91/91 |
| 3 | **GPT-4.1** | **7.29** | 7.73 | 80 | No | 91/91 |
| 4 | Gemini 2.5 Flash Lite | 7.22 | 7.87 | **165** | No | 91/91 |
| 5 | MiMo-V2-Flash | 7.20 | 7.60 | 52 | Si (MIT) | 91/91 |
| 6 | Llama 4 Maverick* | 7.20 | **8.13** | 46 | Si (Llama) | 74/91 |
| 7 | Claude Opus 4.7 | 7.17 | 8.09 | 63 | No | 91/91 |
| 8 | Claude Sonnet 4.6 | 7.15 | 7.98 | 54 | No | 91/91 |
| 9 | GPT-4.1 Mini | 7.11 | 7.53 | 59 | No | 91/91 |
| 10 | DeepSeek V3.2 | 7.11 | 7.69 | 22 | Si (MIT) | 91/91 |
| 11 | Kimi K2* | 7.05 | 7.86 | 28 | No | 74/91 |
| 12 | Qwen3 Coder | 7.04 | 7.73 | 52 | Si (Apache) | 91/91 |
| 13 | Mistral Large | 7.03 | 7.70 | 50 | Si (Apache) | 91/91 |
| 14 | MiniMax M2.7 | 6.71 | 7.38 | 35 | Parcial | 91/91 |
| 15 | Nemotron 3 Super | 6.63 | 6.76 | 32 | Si (NVIDIA) | 91/91 |
| 16 | Qwen 3.6 Plus | 6.57 | 7.41 | 50 | Si (Apache) | 90/91 |
| 17 | GLM-5.1 | 6.25 | 6.28 | 38 | Si (MIT) | 91/91 |

*Llama 4 Maverick: 17 errores 404 en suites con tools (OpenRouter no tiene endpoint con function calling nativo). Kimi K2: 17 errores 429 por rate limits del provider. No afecta los scores de los tests que sí se ejecutaron.

### Ranking Solo Alternativas (sin Anthropic/OpenAI)

| # | Modelo | Final | tok/s | Open Source | Suscripcion |
|---|--------|-------|-------|-------------|-------------|
| 1 | **Devstral Small** | **7.35** | 146 | Si (Apache 2.0) | Pay-as-you-go |
| 2 | Gemini 2.5 Flash Lite | 7.22 | 165 | No | Google AI Pro $20/mes |
| 3 | MiMo-V2-Flash | 7.20 | 52 | Si (MIT) | Pay-as-you-go |
| 4 | Llama 4 Maverick | 7.20 | 46 | Si (Llama) | Pay-as-you-go |
| 5 | DeepSeek V3.2 | 7.11 | 22 | Si (MIT) | Pay-as-you-go |
| 6 | Kimi K2 | 7.05 | 28 | No | Pay-as-you-go |
| 7 | Qwen3 Coder | 7.04 | 52 | Si (Apache) | Pay-as-you-go |
| 8 | Mistral Large | 7.03 | 50 | Si (Apache) | Le Chat ~$15/mes |
| 9 | MiniMax M2.7 | 6.71 | 35 | Parcial | MiniMax $20-$69/mes |
| 10 | Nemotron 3 Super | 6.63 | 32 | Si (NVIDIA) | Pay-as-you-go |
| 11 | Qwen 3.6 Plus | 6.57 | 50 | Si (Apache) | Qwen $50/mes |
| 12 | GLM-5.1 | 6.25 | 38 | Si (MIT) | Pay-as-you-go |

### Mejor por Categoria (Phi-4 judge)

| Categoria | 1ro | 2do | 3ro |
|-----------|-----|-----|-----|
| **Razonamiento** | MiMo-V2-Flash (7.58) | Devstral (7.36) | GPT-5.4 Mini (7.32) |
| **Agentes (tool+orch+agent)** | Llama 4 Maverick (7.32) | Claude Opus 4.7 (7.09) | Claude Sonnet 4.6 (7.02) |
| **Contenido ES** | MiMo-V2-Flash (7.51) | DeepSeek V3.2 (7.40) | Devstral (7.39) |
| **Codigo** | MiMo-V2-Flash (7.74) | Qwen3 Coder (7.72) | Devstral (7.65) |
| **Customer/Policy/Multi-turn** | GPT-5.4 Mini (7.32) | Kimi K2 (7.27) | Devstral (7.22) |
| **Creatividad** | Devstral (7.70) | Gemini Flash Lite (7.63) | MiMo-V2-Flash (7.58) |
| **Estructurado/Hallucination** | Devstral (7.63) | Gemini Flash Lite (7.63) | GPT-4.1 (7.57) |
| **Strategy/Sales** | MiMo-V2-Flash (7.78) | GPT-4.1 (7.59) | GPT-4.1 Mini (7.57) |
| **Traduccion** | Devstral (7.87) | Gemini Flash Lite (7.84) | MiMo-V2-Flash (7.67) |
| **OCR** | GPT-4.1 (7.28) | MiMo-V2-Flash (7.21) | Gemini Flash Lite (7.18) |
| **String Precision** | Devstral (7.66) | GPT-5.4 Mini (7.58) | GPT-4.1 (7.53) |
| **Productividad (resumen/planning)** | MiMo-V2-Flash (7.66) | Devstral (7.47) | GPT-5.4 Mini (7.45) |

### Hallazgos Clave

- **#1 Devstral Small**: Open-source Apache 2.0, 146 tok/s, $0.10/$0.30 per M. Campeón en creatividad, string precision y traducción. Increíble para un 24B.
- **#2 GPT-5.4 Mini sorprende**: sube del #8 (v1 sin juez) al #2 con el juez Phi-4. Muy equilibrado, rapido (117 tok/s) y bueno en customer/policy.
- **#3 GPT-4.1 mantiene fortaleza**: especialmente en OCR (líder) y strategy/sales.
- **MiMo-V2-Flash dispara en 4 categorias**: reasoning (7.58), contenido ES (7.51), code (7.74), strategy (7.78). Precio minúsculo ($0.09/$0.29 per M, MIT).
- **Llama 4 Maverick top en agentes (7.32)** pero 17 tests fallan: OpenRouter no soporta tool calling nativo en ese endpoint. Para usarlo con tools: pasar por provider directo (Fireworks, Together, Groq).
- **Claude Opus 4.7 y Sonnet 4.6 parejos**: calidad raw muy alta (8.09, 7.98) pero penalizan en sales/strategy y customer_support genérico.
- **Kimi K2 bajó por rate limits**: 17 errores 429 sostenidos del provider en OpenRouter — no es problema del modelo.
- **GLM-5.1 último (6.25)**: flojo en casi todas las suites salvo agents. Bajo agente coding a pesar del branding.
- **Modelos chinos (MiniMax, Qwen, GLM)**: tienden a bajar por traducción y honestidad. MiniMax sigue último en creatividad (7.00 vs 7.70 de Devstral).
- **Juez Phi-4 local**: cero conflicto de interés (Microsoft, 14B, MIT). Ollama en localhost, gratis. Scoring: 30% auto + 70% juez. 1512 evaluaciones sin costo de API.

### Recomendacion por Caso de Uso (Phi-4 judge)

| Uso | Modelo Recomendado | Por que |
|-----|-------------------|---------|
| Agente general | Devstral Small | #1 global, 146 tok/s, Apache 2.0 |
| Agente con tool calling | Llama 4 Maverick (via Fireworks/Together/Groq) | Top en agentes (7.32) — evitar OpenRouter |
| Agente economico (API) | DeepSeek V3.2 o MiMo-V2-Flash | #10 a $0.14/M, #5 a $0.09/M |
| Agente ultra rapido | Gemini 2.5 Flash Lite | 165 tok/s, #4 global |
| Agente con suscripcion fija | MiniMax M2.7 | $20-69/mes, sin sorpresas |
| Soporte al cliente | GPT-5.4 Mini o Kimi K2 | Top 2 en customer (7.32, 7.27) |
| Contenido sin alucinaciones | Claude Opus 4.7 | #3 en estructurado/hallucination, calidad raw 8.09 |
| Contenido en español | MiMo-V2-Flash | #1 en contenido ES (7.51) — y el más barato |
| Coding/automatizaciones | MiMo-V2-Flash o Qwen3 Coder | Empatan top en code (7.74, 7.72) |
| OCR/extracción documentos | GPT-4.1 | Líder en OCR (7.28) |
| Traducción es↔en | Devstral Small | #1 en traducción (7.87) |
| Razonamiento profundo | MiMo-V2-Flash | #1 en reasoning (7.58), precio minúsculo |
| Creatividad/storytelling | Devstral Small | #1 en creatividad (7.70) |
| String precision (API keys, JWT) | Devstral Small | #1 en string precision (7.66) |
| Open-source para DGX Spark | MiMo-V2-Flash o Devstral | Ambos top, MIT/Apache |

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
│   ├── llm_judge.py                 # LLM-as-Judge (Phi-4 local, cero sesgo)
│   ├── tests/                       # 23 suites de tests
│   └── results/                     # Resultados JSON
├── providers/
│   └── adapters.py                  # Adaptador unificado OpenAI-compatible
└── requirements.txt
```
