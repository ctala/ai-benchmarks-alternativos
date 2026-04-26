# Benchmark de Modelos AI Alternativos: comparación abierta de 44 LLMs en español para N8N, OpenClaw y emprendedores

**Version 2.3.0** | Ultima actualizacion: 26 de Abril de 2026

> **Encuentra alternativas a Claude, GPT-5 y Gemini** comparadas con 5,000+ tests reales: precio, calidad, velocidad y tool calling. Pensado para emprendedores latinoamericanos que construyen agentes en N8N, OpenClaw o Hermes con presupuestos reales.

> ⚠️ **No existe un "mejor modelo" universal.** "Coding" significa cosas distintas si desarrollás *plugins de WordPress*, *templates de N8N*, *scripts de automatización* o *proyectos grandes*. Lo mismo con contenido (blog técnico ≠ copy de marketing ≠ newsletter), soporte al cliente o agentes. **Este benchmark nació porque, como emprendedor, no encontré tests que me ayudaran a decidir para mis casos reales** — ahora existen y son tuyos.

Benchmark de modelos AI para emprendedores y equipos que usan agentes (OpenClaw, N8N, Hermes). Evalua modelos en los 4 pilares del emprendedor: **Razonamiento, Coding, Contenido/Marketing, y Agentes/Operaciones**. Incluye LLM-as-Judge local con Phi-4 (Microsoft, cero conflicto de interes).

**Cobertura actual**: 44 modelos con ≥50 runs cada uno, 5,000+ tests ejecutados, 7 lotes con juez Phi-4 + Lote 8 en curso.

## Top 10 Global Ranking

| # | Modelo | Score | $ in/$ out per M | Provider | Notas |
|---|---|---:|---|---|---|
| 1 | **Llama 3.3 70B Groq** | **7.64** | $0.59/$0.79 | Groq | 270 tok/s avg ⚡ |
| 2 | **Mistral Small 4** | **7.54** | $0.15/$0.60 | OpenRouter | Apache 2.0, baratísimo |
| 3 | **Gemini 3.1 Flash Lite** | **7.50** | $0.25/$1.50 | OpenRouter | Sucesor del 2.5 Flash Lite |
| 4 | GPT-OSS 120B Cloud | 7.41 | $0/$0 (sub) | Ollama Cloud | Apache 2.0, gratis con sub |
| 5 | Devstral Small | 7.35 | $0.10/$0.30 | OpenRouter | #1 anterior, Apache 2.0 |
| 6 | Hermes 4 70B | 7.24 | $0.13/$0.40 | OpenRouter | Nous Research, hybrid reasoning |
| 7 | GPT-4.1 | 7.23 | $2.00/$8.00 | OpenAI | Premium baseline |
| 8 | Devstral 2 (Dic 2025) | 7.22 | $0.40/$2.00 | OpenRouter | Apache 2.0 |
| 9 | MiMo V2 Flash | 7.20 | $0.09/$0.29 | OpenRouter | MIT |
| 10 | Gemini 2.5 Flash | 7.19 | $0.30/$2.50 | OpenRouter | Velocidad alta |

> 4 de los 10 son **modelos nuevos abril 2026** (Llama Groq #1, Mistral Small 4, Gemini 3.1 Flash Lite, Hermes 4) — el ecosistema cambia rápido.

> **Contexto**: Desde el 21 de abril 2026, Claude Code ya no viene en la suscripcion Pro de $20/mes. Este benchmark ayuda a encontrar las mejores alternativas por caso de uso y presupuesto.

## 🎛️ Calculadora interactiva

**[https://benchmarks.cristiantala.com/](https://benchmarks.cristiantala.com/)** — encuentra el modelo IA perfecto en 30 segundos.

Filtros: presupuesto mensual, calls/mes, calidad mínima, velocidad mínima, tarea (razonamiento / coding / contenido / agentes), open-source, excluir Anthropic+OpenAI+Google propietarios. Ranking por mejor balance calidad/costo. Datos del último benchmark, regenerados automáticamente vía GitHub Actions cuando se agregan tests.

## Lo que te ahorras al usar este benchmark

Para responder *"qué modelo usar para mi agente N8N / qué tan bueno es Kimi K2.6 vs DeepSeek / cuál es el mejor open-source para code"* tendrías que correr esto tú mismo. Acá ya está hecho:

| Recurso invertido | Cantidad |
|---|---|
| Modelos comparados | **30 únicos** |
| Tests por modelo | **91 tests en 23 suites** |
| Runs preservados en JSON | **4,142** (3,873 exitosos) |
| Tokens consumidos (preservados) | 1.26M input + 3.72M output |
| **Costo calculado (`calculate_costs.py`)** | **~$48 USD** sobre runs preservados con PRICING actual |
| **Costo real OpenRouter dashboard** | **$100+ USD** (incluye iteración no preservada) |
| **+ recargas posteriores para retries y nuevos lotes** | **$120+ adicional** abril 25 |
| **Tiempo wall-clock** | **~67h** desde 11 de abril |
| Iteración de metodología | cientos de runs no documentados antes del scoring v2 |

> El número "$200+" no es solo lo medido. Hay 4 categorías de costo que el `cost_usd` calculado **NO captura**:
>
> 1. **Iteración de metodología** (cientos de runs antes de instrumentar `cost_usd`/`output_tokens`): exploración de qué tests, qué scoring, qué juez, cómo medir thinking models.
> 2. **Respuestas vacías facturadas a precio completo**: 165+ corridas de thinking models (Kimi K2.6, GPT-5.5, GLM-5.1, Nemotron) consumieron `max_tokens=2048` razonando y devolvieron `content=""`. **OpenRouter cobra esos tokens igual** — el modelo razonó, los tokens se generaron. Solo que no llegaron como respuesta visible.
> 3. **Timeouts cobrados**: requests que sobrepasaron el timeout cliente fueron abortados desde nuestro lado, pero el provider ya había generado la respuesta y nos la facturó.
> 4. **Retries del usuario y del runner**: cada retry con `--rerun-empty` / `--rerun-failed` es una invocación nueva. Algunos tests se corrieron 3-4 veces hasta llegar a un score válido.
>
> El cálculo automático con `python benchmarks/calculate_costs.py --markdown` ahora da **~$48** sobre los runs preservados (PRICING actualizado abril 25 con Claude Opus/GPT-5.5/Kimi/Mistral Large que faltaban). **El dashboard de OpenRouter reporta $100+** acumulado — la diferencia es la iteración no preservada en JSONs y otros consumos del usuario en OpenRouter.

Regla práctica: **un emprendedor que quiera replicar este benchmark desde cero gastaría ~$100-200 en APIs + ~50h de trabajo + el costo invisible de iterar la metodología**. Acá ya está hecho con todos los hallazgos — abre [RECOMENDACIONES.md](RECOMENDACIONES.md) y elegí por plataforma + tarea + presupuesto.

## Documentos Principales

| Documento | Contenido |
|-----------|-----------|
| [MODELOS.md](MODELOS.md) | Inventario completo: probados, en cola y por agregar al config |
| [TESTS.md](TESTS.md) | 91 tests en 23 suites (auto-generado desde benchmarks/tests/) |
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

### Estandar del benchmark para thinking models

Todas las constantes estan en `providers/adapters.py` (cima del archivo, con razones inline). Este es el estandar oficial aplicado a todos los lotes — editalo si tu hardware/budget difiere.

| Constante | Valor | Aplica a |
|---|---|---|
| `THINKING_MODELS` | `gpt-5*`, `o1*`, `o3*`, `glm-5*`, `kimi-k2.6`, `nemotron*` | Modelos que consumen reasoning interno facturado |
| `THINKING_TOKEN_MULTIPLIER` | `4` | max_tokens × 4 para thinking. Sin esto, agotan budget razonando y devuelven `content=""` |
| `THINKING_MIN_TOKENS` | `8192` | Piso absoluto de output para que blog/workshop largos no queden cortados |
| `HTTP_READ_TIMEOUT_S` | `240.0` | httpx read_timeout. Antes 60s causaba timeouts a 181s (3 retries × 60s) |
| `FIXED_TEMP_MODELS` | `gpt-5.5`, `gpt-5-pro`, `gpt-5.5-pro`, `o1`, `o3` | Sólo aceptan temperature=1.0. El adapter omite el parámetro |
| `max_tokens` default (runner.py) | `2048` | Para non-thinking. Thinking reciben 8192 |
| `temperature` default | `0.7` | Para los no-FIXED_TEMP_MODELS |

**Origen**: detectado abril 25 2026 que 165 runs de thinking models tenían `content=""` (agotaban max_tokens=2048 en reasoning interno) + 6 timeouts en GPT-5.5 strategy/workshop por httpx 60s. Tras el fix, los scores subieron 2-3 puntos. Documentado en CHANGELOG v2.2.1.

> **Implicación para tu billetera**: thinking models facturan ~3-4× más tokens de lo que parece (reasoning tokens cuentan como `completion_tokens`). Una respuesta de 500 tokens visibles en GPT-5.5 puede haber consumido 2000+ tokens facturados. Las suscripciones flat-rate (ChatGPT Pro, Anthropic Pro Max) se consumen 3-4× más rápido con thinking models. Tabla concreta en COMPARATIVA.md.

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

> Ranking completo con **27 modelos × 91 tests = 2457 corridas** evaluadas por Phi-4 (Microsoft, 14B, MIT) local via Ollama. Juez sin conflicto de interés. Total cómputo: **~65h wall-clock** distribuidas en 3 lotes (22-25 abril).
>
> JSON: `benchmark_20260422_204025.json` (Lote 1) + `benchmark_20260423_051248.json` (Lote 2) + `benchmark_20260424_053942.json` (Lote 3). Detalle por modelo navegable en [`results/per-model/`](benchmarks/results/per-model/).

### Ranking Global (Phi-4 judge, 91 tests/modelo)

| # | Modelo | Final | Calidad | tok/s | Open Source | OK/Total |
|---|--------|-------|---------|-------|-------------|----------|
| 1 | **Devstral Small** | **7.35** | 7.91 | 146 | Si (Apache 2.0) | 91/91 |
| 2 | **GPT-5.4 Mini** | **7.32** | 7.88 | 117 | No | 91/91 |
| 3 | **GPT-4.1** | **7.29** | 7.73 | 80 | No | 91/91 |
| 4 | Gemini 2.5 Flash Lite | 7.22 | 7.87 | **165** | No | 91/91 |
| 5 | **Devstral 2 (Dic 2025)** | 7.22 | 7.78 | 65 | Si (Apache 2.0) | 91/91 |
| 6 | MiMo-V2-Flash | 7.20 | 7.60 | 52 | Si (MIT) | 91/91 |
| 7 | Llama 4 Maverick* | 7.20 | **8.13** | 46 | Si (Llama) | 74/91 |
| 8 | **Gemini 2.5 Flash** | 7.20 | 7.80 | 115 | No | 91/91 |
| 9 | Claude Opus 4.7 | 7.17 | 8.09 | 63 | No | 91/91 |
| 10 | **Gemma 4 26B MoE** (3.8B activos) | 7.15 | 7.85 | 48 | Si (Apache 2.0) | 91/91 |
| 11 | Claude Sonnet 4.6 | 7.15 | 7.98 | 54 | No | 91/91 |
| 12 | **Claude Opus 4.6** | 7.11 | **8.16** | 46 | No | 91/91 |
| 13 | GPT-4.1 Mini | 7.11 | 7.53 | 59 | No | 91/91 |
| 14 | **GPT-5.4** | 7.11 | 7.62 | 57 | No | 91/91 |
| 15 | DeepSeek V3.2 | 7.11 | 7.69 | 22 | Si (MIT) | 91/91 |
| 16 | **Devstral Medium** | 7.09 | 7.89 | 60 | Si (Apache 2.0) | 88/91 |
| 17 | Kimi K2* | 7.05 | 7.86 | 28 | No | 74/91 |
| 18 | Qwen3 Coder | 7.04 | 7.73 | 52 | Si (Apache) | 91/91 |
| 19 | Mistral Large | 7.03 | 7.70 | 50 | Si (Apache) | 91/91 |
| 20 | **MiMo-V2-Pro** | 6.88 | 7.52 | 52 | No (Xiaomi) | 91/91 |
| 21 | **Mistral Nemo** | 6.86 | 7.08 | 30 | Si (Apache) | 90/91 |
| 22 | MiniMax M2.7 | 6.71 | 7.38 | 35 | Parcial | 91/91 |
| 23 | Nemotron 3 Super | 6.63 | 6.76 | 32 | Si (NVIDIA) | 91/91 |
| 24 | Qwen 3.6 Plus | 6.57 | 7.41 | 50 | Si (Apache) | 90/91 |
| 25 | **Gemini 2.5 Pro** | 6.45 | 6.52 | 91 | No | 91/91 |
| 26 | GLM-5.1 | 6.25 | 6.28 | 38 | Si (MIT) | 91/91 |
| 27 | **Kimi K2.6** | 5.76 | 5.13 | 34 | No | 91/91 |

*Llama 4 Maverick: 17 errores 404 en suites con tools (OpenRouter sin endpoint con function calling). Kimi K2: 17 errores 429 por rate limits. Devstral Medium: 3 errores 503 puntuales del provider. Mistral Nemo: 1 error 400. Negrita = nuevos modelos del Lote 3 (24-25 abril).

### Ranking Solo Alternativas (sin Anthropic, OpenAI, ni Google propietarios)

> Excluye los 3 proveedores propietarios populares (Anthropic, OpenAI, Gemini Flash/Flash-Lite/Pro). **Gemma sí queda** porque es open-source.

| # | Modelo | Final | tok/s | Open Source |
|---|--------|-------|-------|-------------|
| 1 | **Devstral Small** | **7.35** | 146 | Si (Apache 2.0) |
| 2 | **Devstral 2** | 7.22 | 65 | Si (Apache 2.0) |
| 3 | MiMo-V2-Flash | 7.20 | 52 | Si (MIT) |
| 4 | Llama 4 Maverick | 7.20 | 46 | Si (Llama) |
| 5 | Gemma 4 26B MoE | 7.15 | 48 | Si (Apache 2.0) |
| 6 | DeepSeek V3.2 | 7.11 | 22 | Si (MIT) |
| 7 | Devstral Medium | 7.09 | 60 | Si (Apache 2.0) |
| 8 | Kimi K2 | 7.05 | 28 | No |
| 9 | Qwen3 Coder | 7.04 | 52 | Si (Apache) |
| 10 | Mistral Large | 7.03 | 50 | Si (Apache) |
| 11 | MiMo-V2-Pro | 6.88 | 52 | No |
| 12 | Mistral Nemo | 6.86 | 30 | Si (Apache) |
| 13 | MiniMax M2.7 | 6.71 | 35 | Parcial |
| 14 | Nemotron 3 Super | 6.63 | 32 | Si (NVIDIA) |
| 15 | Qwen 3.6 Plus | 6.57 | 50 | No (proprietary) |
| 16 | GLM-5.1 | 6.25 | 38 | Si (MIT) |
| 17 | Kimi K2.6 | 5.76 | 34 | No |

### Ranking Solo Open-Source

| # | Modelo | Final | tok/s | Licencia |
|---|--------|-------|-------|----------|
| 1 | **Devstral Small** | **7.35** | 146 | Apache 2.0 |
| 2 | **Devstral 2 (Dic 2025)** | 7.22 | 65 | Apache 2.0 |
| 3 | MiMo-V2-Flash | 7.20 | 52 | MIT |
| 4 | Llama 4 Maverick | 7.20 | 46 | Llama Community |
| 5 | **Gemma 4 26B MoE** | 7.15 | 48 | Apache 2.0 |
| 6 | DeepSeek V3.2 | 7.11 | 22 | MIT |
| 7 | Devstral Medium | 7.09 | 60 | Apache 2.0 |
| 8 | Qwen3 Coder | 7.04 | 52 | Apache 2.0 |
| 9 | Mistral Large | 7.03 | 50 | Apache 2.0 |
| 10 | Mistral Nemo | 6.86 | 30 | Apache 2.0 |
| 11 | Nemotron 3 Super | 6.63 | 32 | NVIDIA Open |
| 12 | Qwen 3.6 Plus | 6.57 | 50 | Apache 2.0 |
| 13 | GLM-5.1 | 6.25 | 38 | MIT |

### Mejor por Categoria

| Categoria | 1ro | 2do | 3ro |
|-----------|-----|-----|-----|
| **Razonamiento** | MiMo-V2-Flash (7.58) | Devstral Small (7.36) | GPT-5.4 Mini (7.32) |
| **Contenido ES** | MiMo-V2-Flash (7.51) | DeepSeek V3.2 (7.40) | Devstral Small (7.39) |
| **Code** | MiMo-V2-Flash (7.74) | Qwen3 Coder (7.72) | GPT-4.1 (7.65) |
| **Agentes (tool+orch)** | Llama 4 Maverick (7.32) | Claude Opus 4.7 (7.09) | Claude Sonnet 4.6 (7.02) |
| **Customer/Policy** | GPT-5.4 Mini (7.32) | Kimi K2 (7.27) | Devstral Small (7.22) |
| **Creatividad** | Devstral Small (7.70) | Gemini Flash Lite (7.63) | Devstral Medium (7.59) |
| **Estructurado/Hallucination** | Devstral Small (7.63) | Gemini Flash Lite (7.63) | GPT-4.1 (7.57) |
| **Strategy/Sales** | MiMo-V2-Flash (7.78) | Devstral 2 (7.63) | GPT-4.1 (7.59) |
| **Traduccion** | Devstral Small (7.87) | Gemini Flash Lite (7.84) | Devstral 2 (7.69) |
| **OCR** | GPT-4.1 (7.28) | MiMo-V2-Flash (7.21) | Gemini Flash Lite (7.18) |
| **String Precision** | Devstral Small (7.66) | GPT-5.4 Mini (7.58) | Gemini Flash Lite (7.53) |
| **Productividad** | MiMo-V2-Flash (7.66) | Devstral Small (7.47) | Devstral 2 (7.47) |

### Hallazgos Clave (v2.2)

- **Devstral Small mantiene #1** tras agregar 10 modelos nuevos. Impecable para un 24B Apache 2.0.
- **Devstral 2 (dic 2025) entra #5** pero NO supera al Small original — el Small sigue siendo más eficiente.
- **Gemma 4 26B (3.8B activos) sorprende #10** — modelo open-source pequeño compitiendo con Claude Opus a $0.15/M.
- **MiMo-V2-Pro decepciona #20** ($1.00/$3.00) — el flagship de Xiaomi rinde MENOS que MiMo-V2-Flash (#6, $0.09/$0.29).
- **GPT-5.4 #14 vs Mini #2**: el Mini supera consistentemente al modelo grande.
- **Gemini 2.5 Pro inesperadamente bajo (#25)** — el flagship de Google rinde peor que su propio Flash Lite.
- **Kimi K2.6 ÚLTIMO (#27, 5.76)** — peor que K2 (#17). El modelo nuevo de Moonshot tiene problemas serios.
- **Mistral Nemo top de los baratos (#21, $0.02/$0.02)** — baseline ultra económico aceptable.
- **Llama 4 Maverick top en agentes (7.32)** — pero requiere provider directo para tool calling.
- **Juez Phi-4 local**: 2457 evaluaciones, cero conflicto, $0 costo, replicable con MIT license.

### Recomendacion por Caso de Uso (v2.2)

| Uso | Modelo Recomendado | Por que |
|-----|-------------------|---------|
| Agente general | Devstral Small | #1 global, 146 tok/s, Apache 2.0 |
| Agente con tool calling | Llama 4 Maverick (via Fireworks/Together/Groq) | Top en agentes (7.32), evitar OpenRouter |
| Agente económico API | MiMo-V2-Flash o DeepSeek V3.2 | #6 a $0.09/M, #15 a $0.14/M |
| Agente ultra rápido | Gemini 2.5 Flash Lite | 165 tok/s, #4 global |
| Agente con suscripción fija | MiniMax M2.7 | $20-69/mes |
| Soporte al cliente | GPT-5.4 Mini o Kimi K2 | Top 2 customer (7.32, 7.27) |
| Contenido sin alucinaciones | Claude Opus 4.6 o 4.7 | Calidad raw 8.16 / 8.09 |
| Contenido en español | MiMo-V2-Flash | #1 contenido ES (7.51), el más barato |
| Coding | MiMo-V2-Flash, Qwen3 Coder, GPT-4.1 | Top 3 code (7.74, 7.72, 7.65) |
| OCR/documentos | GPT-4.1 | Líder OCR (7.28) |
| Traducción es↔en | Devstral Small | #1 traducción (7.87) |
| Razonamiento profundo | MiMo-V2-Flash | #1 reasoning (7.58), precio minúsculo |
| Creatividad/storytelling | Devstral Small | #1 creatividad (7.70) |
| String precision | Devstral Small | #1 string precision (7.66) |
| Open-source para DGX Spark | Devstral Small/2, MiMo-V2-Flash, Gemma 4 26B | Top 4 open-source |

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

## Preguntas frecuentes (FAQ)

**¿Cuál es la mejor alternativa a Claude para agentes N8N en 2026?**
Devstral Small (Apache 2.0, $0.10/$0.30 per M tokens), Mistral Small 4 ($0.15/$0.60) y Llama 3.3 70B en Groq (270 tok/s) son las top 3 por relación calidad/precio. El ranking cambia según la tarea — ver [calculadora](https://benchmarks.cristiantala.com/) para filtrar por caso de uso.

**¿Vale la pena pagar GPT-5 o Claude Opus si hay alternativas más baratas?**
Para tareas estándar (contenido, traducción, agentes simples), no — modelos de $0.10-0.60 dan resultados comparables. Para razonamiento profundo, código complejo o tool calling crítico, los premium siguen siendo superiores. El delta real está cuantificado en [DESCUBRIMIENTOS.md](DESCUBRIMIENTOS.md).

**¿Qué modelos open-source recomiendan para correr local?**
Para hardware ≥64GB RAM: Devstral Small (24B), Qwen 3.6 base, Mistral Small 4 (24B) y GPT-OSS 120B. Todos Apache 2.0 o MIT. Ver [RECOMENDACIONES.md](RECOMENDACIONES.md) para guía completa por hardware.

**¿Por qué usar Phi-4 como juez en vez de GPT-4 o Claude?**
Cero conflicto de interés (ningún proveedor del benchmark es también el juez), corre 100% local, gratis, licencia MIT y rúbrica en español. Detalles en sección [Eleccion del modelo juez y sesgo](#eleccion-del-modelo-juez-y-sesgo).

**¿Cómo replico el benchmark en mi propio hardware?**
Ver [Quick Start](#quick-start) y [Como Replicar el Benchmark](#como-replicar-el-benchmark). Necesitás Python 3.10+, Ollama (para Phi-4 judge) y al menos OPENROUTER_API_KEY para empezar.

**¿Puedo usar este benchmark para decidir qué modelo poner en producción?**
Sí — fue diseñado para eso. Pero validá en tu caso específico: replicá 5-10 prompts típicos de tu producto contra los 2-3 finalistas. Ningún benchmark sustituye prompts reales de tu negocio. En la [comunidad Skool](https://www.skool.com/cagala-aprende-repite) compartimos plantillas y workshops para esa validación.

## Para agentes IA consumidores (Claude Code, Cursor, etc.)

Este repo está pensado también para que **agentes IA puedan consumirlo y recomendar modelos basados en datos reales**, no en su entrenamiento (que probablemente está desactualizado).

- **[AGENTS.md](AGENTS.md)** — guía de decisión completa con reglas, anti-patterns y templates de respuesta
- **[docs/data/models.json](https://benchmarks.cristiantala.com/data/models.json)** — JSON con todos los modelos, scores por pilar, costos, licencias
- **[docs/data/agents-decision-guide.json](https://benchmarks.cristiantala.com/data/agents-decision-guide.json)** — schema estructurado de casos de uso → modelos recomendados

Ejemplo mínimo en Python:

```python
import json, urllib.request

GUIDE = json.loads(urllib.request.urlopen(
    'https://benchmarks.cristiantala.com/data/agents-decision-guide.json'
).read())

# Agente recibe pregunta sobre N8N templates
caso = next(uc for uc in GUIDE['use_cases'] if uc['id'] == 'coding_n8n_templates')
print(f"Recomendación: {caso['top_models'][0]['model_id']}")
print(f"Razón: {caso['top_models'][0]['reason']}")
```

Si construís un agente que recomiende modelos, leé AGENTS.md primero — la regla #0 es **"no existe un mejor modelo universal"**.

## Comunidad y soporte

- 💬 **[Cágala, Aprende, Repite (Skool)](https://www.skool.com/cagala-aprende-repite)** — comunidad de emprendedores latinoamericanos usando IA
- 📧 **[Newsletter Cristian Tala](https://cristiantala.com/newsletter/)** — análisis de modelos y casos reales
- 📺 **[YouTube](https://www.youtube.com/@cristiantalasanchez)** — workshops y tutoriales
- 💼 **[LinkedIn](https://linkedin.com/in/ctala)** — ecosistema startup chileno
- 🐛 **[Issues en GitHub](https://github.com/ctala/ai-benchmarks-alternativos/issues)** — bugs, sugerencias, modelos a agregar
