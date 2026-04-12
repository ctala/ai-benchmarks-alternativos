# Guia de Proveedores y Modelos

> Ultima actualizacion: 11 de Abril de 2026

Contexto sobre cada proveedor, quien lo creo, su foco y modelos principales.

---

## Proveedores Propietarios (Closed-Source)

### OpenAI (USA)
- **Fundada**: 2015, San Francisco
- **Fundadores**: Sam Altman, Elon Musk (salio), Greg Brockman, Ilya Sutskever (salio)
- **Foco**: Modelos frontier de proposito general, lider en tool calling
- **Modelos**: GPT-4o, GPT-5.2, o3, o1 (razonamiento), DALL-E (imagenes)
- **Fortalezas**: Mejor tool calling del mercado, ecosistema maduro, ChatGPT masivo
- **Debilidades**: Caro, no open-source, dependencia de un vendor
- **API**: api.openai.com | Suscripcion: ChatGPT Plus $20/mes, Pro $200/mes

### Google DeepMind (USA/UK)
- **Fundada**: 2023 (fusion de Google Brain + DeepMind, ambas ~2010)
- **Foco**: Multimodal, velocidad, integracion con Google Workspace
- **Modelos**: Gemini 2.5 Pro/Flash, Gemini 3.1 Pro, **Gemma 4** (open-source)
- **Fortalezas**: Velocidad (Flash es muy rapido), contexto largo (1M+), tier gratuito generoso
- **Debilidades**: Gemini Pro es caro en output ($10/M)
- **API**: generativelanguage.googleapis.com | Suscripcion: AI Pro $19.99/mes
- **Open-source**: Gemma 4 (Apache 2.0) - 4 tamanos: E2B, E4B, 26B MoE, 31B Dense

### Anthropic (USA)
- **Fundada**: 2021, San Francisco, por ex-OpenAI (Dario y Daniela Amodei)
- **Foco**: Safety, razonamiento, coding
- **Modelos**: Claude Opus 4.6, Claude Sonnet 4.5, Claude Haiku
- **Fortalezas**: #1 en Arena, mejor coding del mercado, excelente razonamiento
- **Debilidades**: Muy caro (Opus $15/$75 per M), **suscripcion no da API para agentes**
- **API**: api.anthropic.com | Suscripcion: Pro $20/mes (solo chat web)

### xAI (USA)
- **Fundada**: 2023, por Elon Musk
- **Foco**: Razonamiento, integracion con X/Twitter
- **Modelos**: Grok 4.20, Grok 4
- **Fortalezas**: #4 en Arena, RPM mas alto del mercado (1200), acceso a datos de X
- **Debilidades**: Ecosistema joven, SuperGrok Heavy es carisimo ($300/mes)
- **API**: api.x.ai | Suscripcion: SuperGrok $30/mes

---

## Proveedores Open-Source

### MiniMax (China, Beijing)
- **Fundada**: 2021, por Yan Junjie (ex-SenseTime)
- **Foco**: Modelos agenticos, coding, multimodal (texto, imagen, audio, video)
- **Modelos**: M2.7 (flagship), M2.5 (open-source, MIT), M2.1 (coding plan)
- **Fortalezas**: SOTA en tareas agenticas, tool calling excelente, genera imagenes y audio
- **Debilidades**: Empresa china (posibles restricciones), M2.7 no es full open-source
- **API**: api.minimax.io | Suscripcion: Coding Plan $10-$150/mes, Agent Pro $19/$69
- **Open-source**: M2.5 (MIT license, 80.2% SWE-Bench)
- **Especial**: Image generation + text-to-speech integrados

### DeepSeek (China, Hangzhou)
- **Fundada**: 2023, spin-off del fondo de inversion High-Flyer
- **Foco**: Razonamiento, eficiencia, costo ultra-bajo
- **Modelos**: DeepSeek V3.2, V4, R1 (razonamiento), Coder
- **Fortalezas**: **Mejor relacion calidad/precio del mercado** ($0.14/$0.28), open-source MIT
- **Debilidades**: Latencia variable (alta demanda), empresa china
- **API**: api.deepseek.com | Sin suscripcion, solo pay-as-you-go
- **Open-source**: Todo es MIT license

### Alibaba Cloud / Qwen (China, Hangzhou)
- **Fundada**: Qwen team dentro de Alibaba Cloud (~2023)
- **Foco**: Multiidioma, contexto largo (1M tokens), coding
- **Modelos**: Qwen 3.6 Plus, Qwen 3.5 Plus, Qwen-Coder-Max
- **Fortalezas**: 1M de contexto, excelente en espanol y chino, Apache 2.0, limites muy generosos (15K RPM)
- **Debilidades**: Latencia alta desde Latam, Coding Plan Lite fue descontinuado
- **API**: Alibaba Cloud Model Studio | Suscripcion: Coding Pro $50/mes
- **Open-source**: Apache 2.0

### Meta AI (USA)
- **Fundada**: Equipo FAIR de Meta/Facebook
- **Foco**: Modelos open-source de proposito general
- **Modelos**: Llama 4 Maverick, Llama 3.3, Code Llama
- **Fortalezas**: Open-source confiable, comunidad enorme, multimodal (Llama 4)
- **Debilidades**: Licencia restrictiva (Llama Community, no Apache), necesita fine-tuning
- **Open-source**: Llama Community License (uso comercial permitido con restricciones)

### Mistral AI (Francia, Paris)
- **Fundada**: 2023, por ex-Google DeepMind y ex-Meta (Arthur Mensch, Guillaume Lample, Timothee Lacroix)
- **Foco**: Eficiencia, multiidioma europeo, modelos compactos
- **Modelos**: Mistral Large, Medium 3, Nemo (12B), Mixtral
- **Fortalezas**: Nemo es el mas barato del mercado ($0.02/M), excelente en idiomas europeos, Apache 2.0
- **Debilidades**: No esta en el top 5 global
- **API**: api.mistral.ai | Suscripcion: Le Chat ~$15/mes
- **Open-source**: Apache 2.0 (Nemo, Mixtral)

### Microsoft (USA)
- **Foco**: Modelos compactos de alta calidad
- **Modelos**: Phi-4 (14B)
- **Fortalezas**: Calidad sorprendente para su tamano, MIT license
- **Open-source**: MIT license

### Zhipu AI / GLM (China, Beijing)
- **Fundada**: 2019, spin-off de Tsinghua University
- **Foco**: Modelos agenticos, tool calling
- **Modelos**: GLM-4.7, GLM-4.7 Thinking
- **Fortalezas**: 90%+ accuracy en tool calling, excelente para agentes locales
- **Open-source**: Apache 2.0

---

## Proveedores de Infraestructura (No crean modelos, los sirven)

### OpenRouter (USA)
- **Que es**: Agregador de APIs - una sola API key para 290+ modelos
- **Pricing**: Sin markup sobre el precio del proveedor original
- **Ventaja**: Fallback automatico, modelos gratis subsidiados, 1 key para todo
- **Modelos gratis**: DeepSeek R1, Llama 3.3 70B, Qwen 3.6 Plus (preview)
- **Ideal para**: Probar muchos modelos sin crear multiples cuentas

### Ollama (USA)
- **Que es**: Runtime local para modelos open-source
- **Cloud**: $0/$20/$100 por mes
- **Ventaja**: Correr cualquier modelo open-source localmente, sin internet
- **Ideal para**: NVIDIA DGX Spark, privacidad, sin dependencia de APIs

### Groq (USA)
- **Que es**: Hardware propio (LPU) para inferencia ultra-rapida
- **Velocidad**: ~544 tok/s en Llama 70B
- **Debilidad**: Rate limits diarios (TPD), seleccion limitada de modelos

### Cerebras (USA)
- **Que es**: Hardware propio (CS-3) para inferencia
- **Velocidad**: Record: 1800 tok/s en Llama 8B, 969 tok/s en 405B
- **Ideal para**: Cuando la velocidad es critica

### SambaNova (USA)
- **Que es**: Hardware propio (SN50) para inferencia
- **Velocidad**: ~580 tok/s en Llama 70B
- **Ventaja**: 5x mas rapido que GPUs segun sus claims

---

## Tabla Resumen: Que es Open-Source y Que No

| Proveedor | Modelo | Open Source | Licencia | Correr en DGX Spark |
|-----------|--------|-------------|----------|---------------------|
| Google | Gemma 4 31B | **Si** | Apache 2.0 | Si (20 GB) |
| Google | Gemma 4 26B MoE | **Si** | Apache 2.0 | Si (16 GB) |
| Google | Gemini 2.5 Pro | No | Propietario | No |
| DeepSeek | V3.2, V4, R1 | **Si** | MIT | Si (120 GB Q4) |
| MiniMax | M2.5 | **Si** | MIT | Si (90 GB) |
| MiniMax | M2.7 | Parcial | Propietario | No |
| Alibaba | Qwen 3.5/3.6 | **Si** | Apache 2.0 | Si (16-42 GB) |
| Meta | Llama 3.3/4 | **Si** | Llama Community | Si (40-60 GB) |
| Mistral | Nemo, Mixtral | **Si** | Apache 2.0 | Si (8-30 GB) |
| Microsoft | Phi-4 | **Si** | MIT | Si (10 GB) |
| Zhipu | GLM-4.7 | **Si** | Apache 2.0 | Si (7 GB) |
| OpenAI | GPT-4o, o3 | No | Propietario | No |
| Anthropic | Claude | No | Propietario | No |
| xAI | Grok | No | Propietario | No |
