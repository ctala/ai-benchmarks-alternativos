# Comparativa Completa de Proveedores y Modelos

> Ultima actualizacion: 23 de Abril de 2026
> Los precios, benchmarks y rankings pueden cambiar. Verifica datos actuales antes de tomar decisiones de compra.
> **Ranking propio v2.1** (17 modelos × 91 tests con juez Phi-4) en [README.md](README.md#resultados-abril-2026--scoring-v2--phi-4-judge). Los "Benchmarks Publicos" de la sección 4 son de terceros (Arena, BFCL, SWE-Bench).

## 1. Ranking por Costo (Pay-as-you-go)

### Tier Ultra-Economico (< $0.10/M tokens)

| Modelo | Input/M | Output/M | Tool Calling | Open Source | Licencia | Proveedor | Notas |
|--------|---------|----------|--------------|-------------|----------|-----------|-------|
| Mistral Nemo | $0.02 | $0.02 | Si | **Si** | Apache 2.0 | Mistral / OpenRouter | El mas barato, correr local |
| Nemotron 3 Nano | $0.05 | $0.20 | Si | **Si** | NVIDIA Open | NVIDIA / OpenRouter | 30B MoE, 3B activos, ultra barato |
| MiMo-V2-Flash | $0.09 | $0.29 | Si | **Si** | MIT | Xiaomi / OpenRouter | 309B MoE, 15B activos, 73.4% SWE-Bench |
| Gemini 2.5 Flash-Lite | $0.10 | $0.40 | Si | No | Propietario | Google | Muy rapido, buena calidad |
| DeepSeek V3.2 | $0.14 | $0.28 | Si | **Si** | MIT | DeepSeek / OpenRouter | Excelente calidad/precio, correr local |
| Gemma 4 26B MoE | $0.15 | $0.30 | Si | **Si** | Apache 2.0 | Google / OpenRouter | Solo 3.8B activos, ideal DGX Spark |
| Llama 3.3 70B | GRATIS | GRATIS | Si | **Si** | Llama Community | OpenRouter (subsidiado) | Rate limits: 20 req/min |
| DeepSeek R1 | GRATIS | GRATIS | Limitado | **Si** | MIT | OpenRouter (subsidiado) | Rate limits: 20 req/min |
| Qwen 3.6 Plus | GRATIS | GRATIS | Si | **Si** | Apache 2.0 | OpenRouter (preview) | 1M ctx, gratis en preview |

### Tier Economico ($0.10 - $1.00/M tokens)

| Modelo | Input/M | Output/M | Tool Calling | Open Source | Licencia | Proveedor | Notas |
|--------|---------|----------|--------------|-------------|----------|-----------|-------|
| Gemma 4 31B | $0.30 | $0.60 | Si | **Si** | Apache 2.0 | Google / OpenRouter | #3 open en Arena, 256K ctx |
| MiniMax M2.7 | $0.30 | $1.20 | Si (SOTA) | Parcial | MIT (M2.5) | MiniMax / OpenRouter | Lider agentic, 205K ctx |
| MiniMax M2.7 HS | $0.30 | $1.20 | Si (SOTA) | Parcial | MIT (M2.5) | MiniMax / OpenRouter | Version highspeed |
| Nemotron 3 Super | $0.10 | $0.50 | Si | **Si** | NVIDIA Open | NVIDIA / OpenRouter | 120B MoE, 12B activos, 1M ctx, mejor open agentic |
| Mistral Small 4 | $0.15 | $0.60 | Si | **Si** | Apache 2.0 | Mistral / OpenRouter | 119B MoE, vision+coding+reasoning unificado |
| Grok 4.1 Fast | $0.20 | $0.50 | Si | No | Propietario | xAI / OpenRouter | Mejor tool calling de xAI, 2M ctx |
| Gemini 3.1 Flash Lite | $0.25 | $1.50 | Si | No | Propietario | Google | Sucesor Flash Lite, niveles de pensamiento |
| DeepSeek V4 | $0.30 | $0.50 | Si | **Si** | MIT | DeepSeek | Cache: $0.03/M input |
| Gemini 2.5 Flash | $0.30 | $2.50 | Si | No | Propietario | Google | Muy rapido |
| Qwen 3.6 Plus | $0.33 | ~$0.65 | Si | **Si** | Apache 2.0 | Alibaba / OpenRouter | 1M ctx |
| Devstral 2 | $0.40 | $2.00 | Si | **Si** | MIT | Mistral / OpenRouter | 123B, 72.2% SWE-bench, upgrade de Devstral Small |
| Mistral Medium 3 | $0.40 | $2.00 | Si | **Si** | Apache 2.0 | Mistral | Near-proprietary quality |
| MiMo-V2-Omni | $0.40 | $2.00 | Si | No | Propietario | Xiaomi / OpenRouter | Multimodal: imagen, video, audio, 260K ctx |
| GLM-5.1 | $0.95 | $3.15 | Si | **Si** | MIT | Zhipu / OpenRouter | 754B MoE, #1 SWE-Bench Pro, sesiones 8h |
| Llama 4 Maverick | $0.50 | $1.00 | Si | **Si** | Llama Community | Meta / OpenRouter | 128K ctx, multimodal |
| Qwen 3.5 Plus | $1.20 | ~$2.00 | Si | **Si** | Apache 2.0 | Alibaba Cloud | Muy bueno para agentes |

### Tier Medio ($1.00 - $5.00/M tokens)

| Modelo | Input/M | Output/M | Tool Calling | Open Source | Licencia | Proveedor | Notas |
|--------|---------|----------|--------------|-------------|----------|-----------|-------|
| MiMo-V2-Pro | $1.00 | $3.00 | Si | No | Propietario | Xiaomi / OpenRouter | 1T MoE, 42B activos, ~Opus 4.6 en ClawEval |
| Gemini 2.5 Pro | $1.25 | $10.00 | Si | No | Propietario | Google | Top 3 global |
| Gemini 3.1 Pro | $2.00 | $12.00 | Si | No | Propietario | Google | 78.8% SWE-bench, upgrade Gemini 2.5 Pro |
| Grok 4.20 | $2.00 | $6.00 | Si | No | Propietario | xAI | Multi-agent interno (4 agentes), baja alucinacion |
| GPT-4o | ~$2.50 | ~$10.00 | Si | No | Propietario | OpenAI | Lider en tool calling |
| Claude Sonnet 4.5 | $3.00 | $15.00 | Si | No | Propietario | Anthropic | API key (no suscripcion) |

### Tier Premium ($5.00+/M tokens)

| Modelo | Input/M | Output/M | Tool Calling | Open Source | Licencia | Proveedor | Notas |
|--------|---------|----------|--------------|-------------|----------|-----------|-------|
| GPT-5.2 | ~$5.00 | ~$15.00 | Si | No | Propietario | OpenAI | Lider benchmarks agenticos |
| GPT-o3 | ~$10.00 | ~$40.00 | Si | No | Propietario | OpenAI | Razonamiento avanzado |
| Claude Opus 4.6 | ~$15.00 | ~$75.00 | Si | No | Propietario | Anthropic | #1 Arena |

---

## 2. Modelos Open Source para Uso Local (Ollama - GRATIS)

Todos estos modelos se pueden correr localmente con Ollama. Organizados por tamano de RAM requerida.

### Para cualquier hardware (< 16 GB RAM)

| Modelo | RAM | Licencia | Tool Calling | Calidad | Contexto |
|--------|-----|----------|--------------|---------|----------|
| Gemma 4 E2B | 2 GB | Apache 2.0 | Si | Basica | 128K |
| Gemma 4 E4B | 4 GB | Apache 2.0 | Si | Buena | 128K |
| Llama 3.3 8B | 6 GB | Llama Community | Si | Buena | 128K |
| Qwen 3.5 7B | 6 GB | Apache 2.0 | Si | Buena | 128K |
| GLM-4.7 9B | 7 GB | Apache 2.0 | Si (90%+) | Excelente (agentes) | 128K |
| Mistral Nemo 12B | 8 GB | Apache 2.0 | Si | Buena | 128K |
| Phi-4 14B | 10 GB | MIT | Si | Buena | 16K |

### Para NVIDIA DGX Spark (128 GB RAM unificada)

| Modelo | RAM | Licencia | Tool Calling | Calidad | Contexto | Notas |
|--------|-----|----------|--------------|---------|----------|-------|
| Gemma 4 26B MoE | 16 GB | Apache 2.0 | Si | Muy buena | 256K | Solo 3.8B activos, muy rapido |
| Qwen 3.5 25B | 16 GB | Apache 2.0 | Si | Muy buena | 128K | **Ya probado, funciona bien** |
| Gemma 4 31B | 20 GB | Apache 2.0 | Si | Excelente | 256K | #3 open en Arena |
| Llama 3.3 70B | 40 GB | Llama Community | Si | Muy buena | 128K | Clasico, confiable |
| Qwen 3.5 72B | 42 GB | Apache 2.0 | Si | Excelente | 128K | Top open para coding |
| Llama 4 Maverick | ~60 GB | Llama Community | Si | Excelente | 128K | Nuevo, multimodal |
| MiniMax M2.5 | ~90 GB | MIT | Si (SOTA) | Excelente | 128K | 80.2% SWE-Bench |
| DeepSeek V3.2 | ~120 GB | MIT | Si | Excelente | 128K | Cabe con cuantizacion Q4 |

> **Ventaja Ollama + DGX Spark**: Costo $0 despues del hardware, sin rate limits, sin dependencia de internet, privacidad total, modelos de hasta 200B parametros.
> **Ventaja open-source**: Puedes fine-tunear modelos de hasta 70B en el DGX Spark.

---

## 3. Proveedores de Inferencia Rapida

| Proveedor | Modelo | Tokens/s | Costo | Notas |
|-----------|--------|----------|-------|-------|
| Groq | Llama 3.3 70B | ~544 | Pay-as-you-go barato | Rate limits diarios (TPD) |
| Cerebras | Llama 3.1 8B | ~1800 | Pay-as-you-go | Record de velocidad |
| Cerebras | Llama 3.1 405B | ~969 | Pay-as-you-go | Mas rapido en 405B |
| SambaNova | Llama 3.1 70B | ~580 | Pay-as-you-go | Lider en 70B |
| Fireworks AI | Varios | ~200-400 | Competitivo | Buen balance |
| Together AI | Varios | ~200-300 | Competitivo | Limites dinamicos |

---

## 4. Benchmarks Publicos (Abril 2026)

### LMSYS Chatbot Arena (Top 10)

| Rank | Modelo | Elo | Proveedor |
|------|--------|-----|-----------|
| 1 | Claude Opus 4.6 Thinking | 1504 | Anthropic |
| 2 | Gemini 3.1 Pro Preview | 1493 | Google |
| 3 | GPT-5.4 | ~1491 | OpenAI |
| 4 | Grok 4.20 Beta1 | 1491 | xAI |
| 5 | GPT-5.4 High | 1484 | OpenAI |

### Coding (LMSYS)

| Rank | Modelo | Elo |
|------|--------|-----|
| 1 | Claude Opus 4.6 | 1549 |
| 2 | GPT-5.2 | ~1500 |

### Function Calling / Tool Use (BFCL v4 + IFBench)

| Modelo | BFCL Score | IFBench | Notas |
|--------|-----------|---------|-------|
| GPT-5.2 (xhigh) | ~95% | 95%+ | Lider en tool calling |
| GPT-4o | ~93% | ~93% | Mejor relacion precio/calidad |
| Claude Opus 4.5 | ~92% | ~91% | Multi-tool orchestration |
| GLM-4.7 Thinking | ~90.6% | ~90% | Mejor open-source |
| DeepSeek V3.2 | ~88% | ~87% | Excelente precio |
| Qwen 3.5 | ~87% | ~86% | Mejor open-weight agentico |

### Ranking Completo por Categoria

#### Tool Calling / Function Calling (critico para agentes)

| Rank | Modelo | Score | Open Source | Costo/M (in/out) | Veredicto |
|------|--------|-------|-------------|-------------------|-----------|
| 1 | GPT-5.2 (xhigh) | 95%+ | No | $5/$15 | El mejor, pero caro |
| 2 | GPT-4o | ~93% | No | $2.50/$10 | Mejor relacion calidad/precio propietario |
| 3 | MiniMax M2.7 | ~92% | Parcial | $0.30/$1.20 | **SOTA economico para agentes** |
| 4 | Claude Opus 4.5 | ~92% | No | $15/$75 | Excelente pero muy caro |
| 5 | Gemma 4 31B | ~91% | **Si** | $0.30/$0.60 | Mejor open-source nuevo |
| 6 | GLM-4.7 Thinking | ~90.6% | **Si** | Gratis (local) | Mejor para correr local |
| 7 | Gemini 2.5 Pro | ~90% | No | $1.25/$10 | Buen balance |
| 8 | DeepSeek V3.2 | ~88% | **Si** | $0.14/$0.28 | Ultra barato y bueno |
| 9 | Qwen 3.6 Plus | ~87% | **Si** | $0.33/$0.65 | 1M contexto, gratis preview |
| 10 | Llama 4 Maverick | ~86% | **Si** | $0.50/$1.00 | Multimodal, buen valor |

#### Razonamiento y Analisis

| Rank | Modelo | Arena Elo | Open Source | Costo/M | Veredicto |
|------|--------|-----------|-------------|---------|-----------|
| 1 | Claude Opus 4.6 | 1504 | No | $15/$75 | Imbatible, pero carisimo |
| 2 | Gemini 3.1 Pro | 1493 | No | $1.25/$10 | Excelente precio/calidad |
| 3 | GPT-5.4 | 1491 | No | $5/$15 | Top tier |
| 4 | Grok 4.20 | 1491 | No | $2/$10 | Sorpresa, muy competitivo |
| 5 | DeepSeek V4 | ~1460 | **Si** | $0.30/$0.50 | **Mejor open-source razonamiento** |
| 6 | MiniMax M2.7 | ~1450 | Parcial | $0.30/$1.20 | Muy bueno para el precio |
| 7 | Qwen 3.6 Plus | ~1440 | **Si** | $0.33/$0.65 | Excelente valor |
| 8 | Gemma 4 31B | ~1435 | **Si** | $0.30/$0.60 | #3 open en Arena |
| 9 | Llama 4 Maverick | ~1420 | **Si** | $0.50/$1.00 | Solido |
| 10 | Mistral Medium 3 | ~1400 | **Si** | $0.40/$2.00 | Bueno, multiidioma |

#### Codigo y Programacion

| Rank | Modelo | Coding Elo / SWE-Bench | Open Source | Costo/M | Veredicto |
|------|--------|----------------------|-------------|---------|-----------|
| 1 | Claude Opus 4.6 | 1549 Elo | No | $15/$75 | Imbatible en codigo |
| 2 | GPT-5.2 | ~1500 Elo | No | $5/$15 | Muy cerca |
| 3 | MiniMax M2.5 | 80.2% SWE | **Si** | Gratis (local) | **Mejor open-source coding** |
| 4 | MiniMax M2.7 | ~78% SWE | Parcial | $0.30/$1.20 | Excelente y barato |
| 5 | Gemini 2.5 Pro | ~76% SWE | No | $1.25/$10 | Buen balance |
| 6 | DeepSeek V3.2 | ~74% SWE | **Si** | $0.14/$0.28 | Increible por el precio |
| 7 | Qwen 3.5 72B | ~72% SWE | **Si** | Gratis (local) | Excelente para DGX Spark |
| 8 | Gemma 4 31B | ~70% SWE | **Si** | $0.30/$0.60 | Nuevo, mejorando rapido |
| 9 | Llama 4 Maverick | ~68% SWE | **Si** | $0.50/$1.00 | Solido |
| 10 | GPT-4o | ~65% SWE | No | $2.50/$10 | Bueno pero ya superado |

#### Velocidad (tokens/segundo)

| Rank | Modelo | tok/s | Open Source | Costo/M | Veredicto |
|------|--------|-------|-------------|---------|-----------|
| 1 | Cerebras Llama 8B | ~1800 | **Si** | Barato | Record absoluto |
| 2 | Cerebras Llama 405B | ~969 | **Si** | Medio | Record para modelos grandes |
| 3 | Groq Llama 70B | ~544 | **Si** | Barato | Muy rapido, rate limits |
| 4 | SambaNova Llama 70B | ~580 | **Si** | Medio | Lider en 70B |
| 5 | MiniMax M2.7 HS | ~400 | Parcial | $0.30/$1.20 | Rapido + inteligente |
| 6 | Gemini 2.5 Flash | ~350 | No | $0.30/$2.50 | Rapido y capaz |
| 7 | Gemma 4 26B MoE | ~300 | **Si** | $0.15/$0.30 | Solo 3.8B activos = rapido |
| 8 | Mistral Nemo | ~250 | **Si** | $0.02/$0.02 | Baratisimo y rapido |

#### Mejor Relacion Calidad/Precio (valor por dolar)

| Rank | Modelo | Costo/M (in/out) | Open Source | Calidad Global | Veredicto |
|------|--------|-------------------|-------------|----------------|-----------|
| 1 | DeepSeek V3.2 | $0.14/$0.28 | **Si** | ~88% BFCL | **Mejor valor absoluto** |
| 2 | Qwen 3.6 Plus | GRATIS (preview) | **Si** | ~87% BFCL | Gratis y excelente |
| 3 | MiMo-V2-Flash | $0.09/$0.29 | **Si** | 73.4% SWE | Ultra barato, MIT license |
| 4 | Gemma 4 26B MoE | $0.15/$0.30 | **Si** | Muy buena | Ultra eficiente, rapido |
| 4 | MiniMax M2.7 | $0.30/$1.20 | Parcial | ~92% BFCL | Mejor agente economico |
| 5 | Gemma 4 31B | $0.30/$0.60 | **Si** | Excelente | #3 open en Arena |
| 6 | Gemini 2.5 Flash | $0.30/$2.50 | No | Muy buena | Rapido y confiable |
| 7 | Mistral Nemo | $0.02/$0.02 | **Si** | Buena | Si el presupuesto es cero |
| 8 | Llama 3.3 70B | GRATIS | **Si** | Buena | Gratis en OpenRouter |

#### Contenido y Redaccion

| Rank | Modelo | Open Source | Costo/M | Veredicto |
|------|--------|-------------|---------|-----------|
| 1 | Claude Opus 4.6 | No | $15/$75 | Mejor escritura, pero caro |
| 2 | GPT-4o | No | $2.50/$10 | Versatil, buen tono |
| 3 | Gemini 2.5 Pro | No | $1.25/$10 | Multiidioma excelente |
| 4 | MiniMax M2.7 | Parcial | $0.30/$1.20 | Sorprendente para el precio |
| 5 | Qwen 3.6 Plus | **Si** | $0.33/$0.65 | Muy bueno en espanol |
| 6 | DeepSeek V3.2 | **Si** | $0.14/$0.28 | Bueno, a veces verbose |
| 7 | Llama 4 Maverick | **Si** | $0.50/$1.00 | Solido |
| 8 | Mistral Medium 3 | **Si** | $0.40/$2.00 | Excelente en europeos |

---

## 5. Rate Limits y Disponibilidad

| Proveedor | RPM Base | TPM Base | Limite Diario | Riesgo de Corte |
|-----------|----------|----------|---------------|-----------------|
| OpenAI | 500 | 800K | No | Bajo (pay-as-you-go) |
| Google Gemini | 1000 | 4M | No | Muy bajo |
| DeepSeek | 300 | 500K | No | Medio (alta demanda) |
| Groq | 30 | 100K | Si (TPD) | **Alto** |
| OpenRouter | Varia | Varia | No | Bajo (fallback automatico) |
| Qwen (Alibaba) | 15000 | 10M | No | Muy bajo |
| Together AI | Dinamico | Dinamico | No | Bajo |
| Mistral | 500 | 1M | No | Bajo |
| Ollama (local) | Ilimitado | Ilimitado | No | **Ninguno** |

> **Para evitar que el agente se quede sin servicio**: OpenRouter permite configurar fallback automatico entre modelos. Ollama nunca se queda sin servicio. Qwen tiene los limites mas generosos.

---

## 6. Compatibilidad con OpenClaw y N8N

| Proveedor | OpenClaw | N8N | Via OpenRouter | Notas |
|-----------|----------|-----|----------------|-------|
| OpenAI | Si | Si (nativo) | Si | Soporte completo |
| Google Gemini | Si | Si (nativo) | Si | Buena integracion |
| DeepSeek | Si | Si (custom) | Si | API compatible OpenAI |
| Mistral | Si | Si (custom) | Si | API compatible OpenAI |
| Ollama Local | Si | Si (nativo) | No | Local, sin costo |
| Ollama Cloud | Si | Si (nativo) | No | $0/$20/$100 mes, costo fijo |
| Groq | Si | Si (custom) | Si | Rapido pero rate limits |
| Qwen | Parcial | Si (custom) | Si | Mejor via OpenRouter |
| xAI (Grok) | Parcial | Si (custom) | Si | API compatible OpenAI |
| Anthropic | Si | Si | Si (via OpenRouter) | API key funciona, **suscripcion Pro/Team NO** |

> **Nota importante**: Anthropic funciona con OpenClaw y N8N usando API key con creditos pay-as-you-go. La suscripcion mensual (Pro $20, Team $30) NO da acceso API para estos agentes.
