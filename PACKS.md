# Packs por Suscripcion: Que Obtienes y Como Usarlo

> Ultima actualizacion: 11 de Abril de 2026

Guia practica de que modelos usar y para que con cada suscripcion. Incluye estrategia de optimizacion local + nube.

---

## Pack 1: MiniMax ($10 - $150/mes)

### Opciones de suscripcion

| Plan | Precio | Modelo | Limites | Mejor para |
|------|--------|--------|---------|-----------|
| Coding Starter | $10/mes | M2.1 | 100 prompts/5h | Probar, uso ligero |
| Agent Pro | $19/mes | M2.7 | Generosos | **Agentes N8N/OpenClaw** |
| Coding Plus | $20/mes | M2.1 | 300 prompts/5h | Coding diario |
| Coding Plus HS | $40/mes | M2.1 (highspeed) | 300 prompts/5h | Coding rapido |
| Coding Max | $50/mes | M2.1 | 1000 prompts/5h | Coding intensivo |
| Agent Pro+ | $69/mes | M2.7 | Muy generosos | Agentes 24/7 |
| Coding Max HS | $80/mes | M2.1 (highspeed) | 1000 prompts/5h | Dev profesional |
| Coding Ultra HS | $150/mes | M2.1 (ultra-speed) | 1000 prompts/5h | Equipos/uso intenso |

### Que modelos usar y para que

| Tarea | Modelo | Via | Notas |
|-------|--------|-----|-------|
| Agente en N8N/OpenClaw | **M2.7** | API / OpenRouter | SOTA en tool calling |
| Agente rapido | **M2.7 Highspeed** | API / OpenRouter | Misma calidad, menor latencia |
| Coding / debug | **M2.1** (via Coding Plan) | Cursor/VSCode | Integra con IDEs |
| Tareas locales pesadas | **M2.5** (open-source) | Ollama local | MIT license, 80.2% SWE-Bench |
| Contenido / redaccion | **M2.7** | API | Sorprendente calidad |

### Recomendacion MiniMax
- **Mejor combo**: Agent Pro ($19/mes) + M2.5 local en DGX Spark = agente 24/7 sin limites con fallback a la nube
- **Para devs**: Coding Plus ($20/mes) + M2.5 local para coding pesado

---

## Pack 2: Alibaba / Qwen ($0 - $50/mes)

### Opciones de suscripcion

| Plan | Precio | Modelo | Limites | Mejor para |
|------|--------|--------|---------|-----------|
| API Free tier | $0 | Qwen 3.6 Plus | Basicos | Probar |
| OpenRouter preview | $0 | Qwen 3.6 Plus | Preview | Gratis ahora, aprovecha |
| Coding Pro | $50/mes | Qwen-Coder-Max | 90K req/mes, 10x tokens | Coding profesional |

### Que modelos usar y para que

| Tarea | Modelo | Via | Notas |
|-------|--------|-----|-------|
| Agente en N8N/OpenClaw | **Qwen 3.6 Plus** | OpenRouter / API | 1M contexto, muy capaz |
| Coding / debug | **Qwen-Coder-Max** | Coding Pro plan | Especializado en codigo |
| Razonamiento largo | **Qwen 3.6 Plus** | API | 1M tokens de contexto |
| Tareas locales (ligeras) | **Qwen 3.5 25B** | Ollama local | Ya probado, funciona bien |
| Tareas locales (pesadas) | **Qwen 3.5 72B** | Ollama en DGX Spark | Excelente calidad |
| Multiidioma | **Qwen 3.6 Plus** | API | Fuerte en espanol y chino |

### Recomendacion Qwen/Alibaba
- **Mejor combo gratis**: Qwen 3.6 Plus (preview gratis) + Qwen 3.5 25B local = $0/mes
- **Para devs**: Coding Pro ($50/mes) + Qwen 3.5 72B local

---

## Pack 3: OpenAI ($0 - $200/mes)

### Opciones de suscripcion

| Plan | Precio | Modelos | Limites | Mejor para |
|------|--------|---------|---------|-----------|
| API Free tier | $0 | GPT-4o-mini | Muy limitados | Probar |
| API Pay-as-you-go | Variable | Todos | Pay per use | Uso moderado |
| ChatGPT Plus | $20/mes | GPT-4o, o3-mini | ~80 msg/3h | Chat personal |
| ChatGPT Pro | $200/mes | GPT-5.2, o3, GPT-4o | Muy generosos | Uso intensivo |

### Que modelos usar y para que

| Tarea | Modelo | Via | Notas |
|-------|--------|-----|-------|
| Agente en N8N/OpenClaw | **GPT-4o** | API key | #1 en tool calling precio/calidad |
| Agente premium | **GPT-5.2** | API key | Mejor tool calling absoluto |
| Razonamiento complejo | **o3** | API key | Razonamiento step-by-step |
| Tareas rapidas/baratas | **GPT-4o-mini** | API key | $0.15/$0.60 per M |
| Chat personal | **GPT-4o** | ChatGPT Plus | Interfaz web |
| Imagenes | **DALL-E 3** | API / Plus | Incluido en Plus |

### Recomendacion OpenAI
- **Mejor combo**: API pay-as-you-go con GPT-4o para agentes (~$10-20/mes uso moderado)
- **Si solo chateas**: ChatGPT Plus ($20/mes)
- **NO recomendado**: ChatGPT Plus NO te da API key para agentes, son productos separados

---

## Pack 4: Google / Gemini ($0 - $249/mes)

### Opciones de suscripcion

| Plan | Precio | Modelos | Limites | Mejor para |
|------|--------|---------|---------|-----------|
| AI Studio Free | $0 | Gemini Flash | 15 req/min | Probar, prototipo |
| API Pay-as-you-go | Variable | Todos | Generosos | Uso moderado |
| AI Pro | $19.99/mes | Gemini 2.5 Pro | Generosos | **Mejor valor $20** |
| AI Ultra | $249.99/mes | Gemini 3.1 Pro | Ilimitado* | Uso enterprise |

### Que modelos usar y para que

| Tarea | Modelo | Via | Notas |
|-------|--------|-----|-------|
| Agente en N8N/OpenClaw | **Gemini 2.5 Flash** | API key | Ultra rapido y barato |
| Agente de calidad | **Gemini 2.5 Pro** | API / AI Pro | Top 3 global |
| Tareas rapidas | **Gemini 2.5 Flash-Lite** | API | $0.10/M, rapidisimo |
| Google Workspace | **Gemini** | AI Pro | Integrado en Gmail, Docs, etc. |
| Modelos locales | **Gemma 4 31B** | Ollama en DGX Spark | Open-source Apache 2.0 |
| Modelo local ligero | **Gemma 4 26B MoE** | Ollama | Solo 3.8B activos, super rapido |

### Recomendacion Google
- **Mejor combo**: AI Pro ($19.99) para Gemini Pro + Gemma 4 31B local en DGX Spark
- **Para presupuesto cero**: Gemma 4 26B MoE local (gratis, rapido, 3.8B activos)

---

## Pack 5: Ollama Cloud ($0 - $100/mes)

### Opciones de suscripcion

| Plan | Precio | Modelos | Limites | Mejor para |
|------|--------|---------|---------|-----------|
| Local (gratis) | $0 | Todos open-source | Sin limite | Hardware propio |
| Cloud Free | $0 | Limitados | Muy restrictivos | Probar |
| Cloud Pro | $20/mes | Todos open-source | Session limits (reset 5h) | Uso moderado |
| Cloud Max | $100/mes | Todos open-source | Generosos | Uso intensivo |

### Que modelos usar y para que

| Tarea | Modelo | Via | Notas |
|-------|--------|-----|-------|
| Agente en N8N/OpenClaw | **Qwen 3.5 72B** | Cloud/Local | Excelente para agentes |
| Coding | **MiniMax M2.5** | Local (DGX Spark) | 80.2% SWE-Bench |
| Tareas rapidas | **Gemma 4 26B MoE** | Local | Solo 3.8B activos |
| RAG / contexto largo | **Qwen 3.6 Plus** | Cloud | 1M contexto |
| Privacidad total | **Cualquiera** | Local | Nada sale de tu red |

### Recomendacion Ollama
- **Mejor combo**: DGX Spark local ($0/mes) + Cloud Pro ($20/mes) como backup
- **Sin hardware**: Cloud Pro ($20/mes) para acceso a todos los modelos open-source

---

## Pack 6: OpenRouter ($0 - pay-as-you-go)

### Opciones

| Plan | Precio | Modelos | Limites | Mejor para |
|------|--------|---------|---------|-----------|
| Free tier | $0 | 27 modelos gratis | 20 req/min, 200/dia | Probar todo |
| Pay-as-you-go | Variable | 290+ modelos | Sin limite fijo | **Flexibilidad maxima** |

### Que modelos usar y para que

| Tarea | Modelo | Costo/M | Notas |
|-------|--------|---------|-------|
| Agente economico | **DeepSeek V3.2** | $0.14/$0.28 | Mejor valor |
| Agente inteligente | **MiniMax M2.7** | $0.30/$1.20 | SOTA agentico |
| Agente rapido | **MiniMax M2.7 HS** | $0.30/$1.20 | Menor latencia |
| Razonamiento largo | **Qwen 3.6 Plus** | GRATIS (preview) | 1M contexto |
| Coding | **Gemma 4 31B** | $0.30/$0.60 | Open-source top |
| Contenido | **GPT-4o** | $2.50/$10 | Lider en redaccion |
| Ultra barato | **Mistral Nemo** | $0.02/$0.02 | Para volumen alto |
| Fallback gratis | **Llama 3.3 70B** | GRATIS | Subsidiado |

### Recomendacion OpenRouter
- **Mejor combo**: Una sola API key, configurar fallback automatico: MiniMax M2.7 -> DeepSeek V3.2 -> Llama 3.3 70B (gratis)
- **Costo estimado**: $5-15/mes para uso moderado de agente

---

## Pack 7: xAI / Grok ($30 - $300/mes)

### Opciones

| Plan | Precio | Modelo | Limites | Mejor para |
|------|--------|--------|---------|-----------|
| SuperGrok | $30/mes | Grok 4.20 | Generosos | Chat + API |
| SuperGrok Heavy | $300/mes | Grok 4 | Muy generosos | Uso enterprise |
| API Pay-as-you-go | Variable | Grok 2 | 1200 RPM base | Agentes |

### Recomendacion xAI
- **Solo si**: Necesitas el ecosistema X/Twitter integrado o quieres un modelo top-5 global
- **RPM mas alto**: 1200 RPM base es el mas generoso del mercado

---

# Estrategia de Optimizacion: Local + Nube

> Como combinar tu DGX Spark (128GB) con servicios cloud para maximizar calidad y minimizar costo.

## Principio: Local primero, nube para lo que no cabe o cuando necesitas velocidad

```
┌─────────────────────────────────────────────────────────┐
│                    Tu DGX Spark (128GB)                  │
│                                                         │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────┐  │
│  │ Gemma 4 26B │  │ Qwen 3.5 25B │  │ Gemma 4 31B   │  │
│  │ MoE (16GB)  │  │   (16GB)     │  │   (20GB)      │  │
│  │ RAPIDO      │  │ YA PROBADO   │  │ ALTA CALIDAD  │  │
│  └─────────────┘  └──────────────┘  └───────────────┘  │
│                                                         │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────────┐  │
│  │ Qwen 3.5 72B│  │ MiniMax M2.5 │  │ DeepSeek V3.2 │  │
│  │   (42GB)    │  │   (90GB)     │  │  (120GB Q4)   │  │
│  │ CODING PRO  │  │ CODING SOTA  │  │  FRONTIER     │  │
│  └──────────────┘  └──────────────┘  └───────────────┘  │
│                                                         │
│  Nota: Solo 1-2 modelos grandes a la vez               │
└─────────────────────────────────────────────────────────┘
                          │
                    Cuando necesitas:
                    - Mas velocidad
                    - Tool calling SOTA
                    - Modelo que no cabe
                    - Backup si local falla
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                   Nube (OpenRouter)                      │
│                                                         │
│  MiniMax M2.7 HS ──── Agentes rapidos ($0.30/$1.20)     │
│  DeepSeek V3.2 ────── Backup barato ($0.14/$0.28)       │
│  Gemini 2.5 Flash ─── Ultra rapido ($0.30/$2.50)        │
│  GPT-4o ───────────── Tool calling pro ($2.50/$10)      │
│  Qwen 3.6 Plus ────── 1M contexto (GRATIS preview)     │
└─────────────────────────────────────────────────────────┘
```

## Configuracion Recomendada por Escenario

### Escenario 1: Agente 24/7 con costo minimo ($0/mes)
```
Local:  Gemma 4 26B MoE (rapido, 16GB) para tareas simples
        Qwen 3.5 72B (42GB) para tareas complejas
Nube:   Qwen 3.6 Plus preview (GRATIS) como fallback
Costo:  $0/mes (solo electricidad del DGX Spark)
```

### Escenario 2: Agente de alta calidad ($19-20/mes)
```
Local:  MiniMax M2.5 (90GB) para coding y tareas pesadas
        Gemma 4 31B (20GB) para tareas generales
Nube:   MiniMax M2.7 via Agent Pro ($19/mes) para tool calling
        o Google AI Pro ($19.99/mes) para Gemini 2.5 Pro
Costo:  $19-20/mes
```

### Escenario 3: Maximo rendimiento ($50/mes)
```
Local:  MiniMax M2.5 (90GB) para coding offline
        Qwen 3.5 72B (42GB) para tareas generales
Nube:   OpenRouter pay-as-you-go (~$15/mes)
        + Qwen Coding Pro ($50/mes) para coding en IDE
Routing: Agente -> MiniMax M2.7 HS -> DeepSeek V3.2 -> Local
Costo:  ~$65/mes
```

### Escenario 4: Solo local, independencia total ($0/mes)
```
Local:  Gemma 4 26B MoE ─── Tareas rapidas (3.8B activos)
        Gemma 4 31B ──────── Calidad general (#3 open)
        Qwen 3.5 72B ────── Coding y razonamiento
        MiniMax M2.5 ────── Coding SOTA (80.2% SWE)
Nota:   Solo puedes cargar 1-2 modelos grandes simultaneamente
        Swap entre modelos segun la tarea
Costo:  $0/mes
```

## Regla de Oro para el Routing

```
SI la tarea necesita tool calling rapido:
  -> MiniMax M2.7 HS (nube) o GLM-4.7 (local)

SI la tarea necesita mucho contexto (>128K tokens):
  -> Qwen 3.6 Plus (nube, 1M ctx)

SI la tarea es coding/debug:
  -> MiniMax M2.5 (local) o Qwen 3.5 72B (local)

SI la tarea es generacion de contenido:
  -> Gemma 4 31B (local) o Qwen 3.6 Plus (nube)

SI necesitas velocidad maxima:
  -> Gemma 4 26B MoE (local, solo 3.8B activos) o Groq (nube)

SI no importa el costo y quieres lo mejor:
  -> GPT-4o (tool calling) / Gemini 2.5 Pro (general)

FALLBACK siempre:
  -> DeepSeek V3.2 (nube, $0.14/M) o Llama 3.3 70B (gratis)
```
