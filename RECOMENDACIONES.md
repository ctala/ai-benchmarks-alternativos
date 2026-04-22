# Recomendaciones por Caso de Uso

> Basado en 91 tests, 23 suites, 30+ modelos evaluados con juez Phi-4 (Microsoft).
> Ultima actualizacion: 22 de Abril de 2026

---

## Por Plataforma de Agentes

### OpenClaw

El agente open-source mas popular de 2026. Corre localmente, conecta LLMs a software real.

| Caso de Uso en OpenClaw | Modelo Recomendado | Por que | Alternativa Barata |
|------------------------|-------------------|---------|-------------------|
| Cerebro principal del agente | Claude Opus 4.7 | #1 en razonamiento y agentes | GPT-4.1 Mini |
| Sub-agentes especializados | DeepSeek V3.2 | Barato ($0.14/M), buena calidad | MiMo-V2-Flash ($0.09/M) |
| Automatizacion de redes sociales | Devstral Small | #1 global, rapido, open-source | DeepSeek V3.2 |
| Newsletter semanal automatica | DeepSeek V3.2 | #1 en news_seo_writing | Gemini Flash Lite |
| Daily briefing (email/Telegram) | Gemini Flash Lite | 195 tok/s, 4s latencia | Devstral Small |
| Monitoreo de competencia | GPT-4.1 | Bueno en analisis, rapido | DeepSeek V3.2 |
| Multi-agent teams | Claude Opus 4.7 | Mejor orquestador | GPT-4.1 |

**Setup recomendado OpenClaw**:
- Modelo principal: Claude Opus 4.7 o GPT-4.1 (via API key)
- Modelo para tareas rapidas: Gemini Flash Lite o Devstral
- Cron jobs: DeepSeek V3.2 (barato para tareas repetitivas)
- Costo estimado: $30-80/mes segun uso

### Hermes

Agente open-source auto-mejorante (Nous Research). 104K+ stars en GitHub. Se conecta a Telegram, WhatsApp, Slack.

| Caso de Uso en Hermes | Modelo Recomendado | Por que | Alternativa |
|-----------------------|-------------------|---------|------------|
| Asistente personal 24/7 | GPT-4.1 Mini | Rapido, buen tool calling, barato | MiniMax M2.7 |
| Multi-agent orchestration | Claude Opus 4.7 | Mejor delegacion y coordinacion | GPT-4.1 |
| Self-improving skills | DeepSeek V3.2 | Barato para iteraciones frecuentes | Devstral |
| Gateway multi-plataforma | Gemini Flash Lite | Ultra rapido para mensajes cortos | Mistral Nemo |

**Setup recomendado Hermes**:
- Modelo principal: GPT-4.1 Mini (balance precio/calidad/velocidad)
- Modelo para learning loop: DeepSeek V3.2 (barato, muchas iteraciones)
- Costo estimado: $15-40/mes

### N8N

Plataforma de automatizacion con 8,300+ templates. 75% de templates nuevos usan AI/LLM.

| Caso de Uso en N8N | Modelo para AI Agent Node | Por que | Template Base |
|--------------------|--------------------------|---------|--------------|
| Chatbot con knowledge base (RAG) | Claude Sonnet 4.6 | Honesto (#1 alucinaciones), no inventa | AI Agent + Vector Store |
| Email auto-responder | GPT-4.1 Mini | Rapido, buen tono, tool calling | Gmail Trigger + AI Agent |
| Clasificacion de tickets | Gemini Flash Lite | Ultra rapido (195 tok/s), barato | Webhook + AI Agent + Zendesk |
| Generacion de contenido SEO | DeepSeek V3.2 | #1 en news_seo_writing (7.67) | Schedule + AI Agent + WordPress |
| SQL desde lenguaje natural | Devstral Small | #1 en coding, rapido | AI Agent + Postgres |
| Calificacion de leads | GPT-4.1 | Buen razonamiento, tool calling | CRM Trigger + AI Agent |
| Generacion de workflows N8N | Claude Opus 4.7 / GPT-4.1 | Mejor para flujos complejos | (manual) |
| Debugging de workflows | Claude Sonnet 4.6 | Honesto sobre errores | (manual) |

**Setup recomendado N8N**:
- AI Agent node: GPT-4.1 Mini via OpenRouter (una API key para todo)
- Para contenido largo: DeepSeek V3.2 (barato, buena calidad)
- Para clasificacion rapida: Gemini Flash Lite
- Fallback: configurar OpenRouter con auto-fallback entre modelos
- Costo estimado: $10-30/mes (pay-as-you-go via OpenRouter)

### Claude Code (alternativas desde abril 2026)

Claude Code ya no viene en la suscripcion Pro de $20/mes. Alternativas:

| Setup | Costo/mes | Modelo | Herramienta | Calidad vs Opus |
|-------|-----------|--------|-------------|-----------------|
| **MiniMax M2.7-HS** | $40 | M2.7 Highspeed | Claude Code wrapper / Roo Code | ~80-85% |
| **Gemini CLI** | $0 | Gemini Flash | Gemini CLI nativo | ~75% |
| **DeepSeek + Roo Code** | ~$5-15 | DeepSeek V3.2 | Roo Code | ~80% |
| **Devstral + Roo Code** | ~$5-15 | Devstral Small | Roo Code / OpenCode | ~85% |
| **GLM Coding Plan** | $3/mes | GLM-5.1 | Claude Code wrapper | ~80% |
| **Combo optimo** | ~$50 | MiniMax + DeepSeek + Gemini | Roo Code | ~90% |

---

## Por Tarea de Negocio

### Soporte al Cliente

| Nivel | Modelo | Config | Costo |
|-------|--------|--------|-------|
| L1 (FAQ automatico) | Gemini Flash Lite | RAG + knowledge base en N8N | ~$5/mes |
| L2 (problemas complejos) | Claude Sonnet 4.6 | Con tools (buscar pedido, crear ticket) | ~$15/mes |
| L3 (escalamiento) | Claude Opus 4.7 | Detecta cuando escalar a humano | ~$5/mes (poco volumen) |
| **Combo** | Flash Lite -> Sonnet -> Opus | Pipeline en N8N con clasificacion | **~$20/mes** |

**Por que Claude para soporte**: #1 en honestidad (no inventa), #3 en agentes, mejor empatia. No quieres que tu bot le mienta al cliente.

### Generacion de Contenido SEO (ecosistemastartup.com)

| Paso | Modelo | Tarea | Costo/articulo |
|------|--------|-------|---------------|
| Research | Perplexity API | Buscar info actualizada | ~$0.01 |
| Redaccion | DeepSeek V3.2 | Escribir articulo 1500 palabras | ~$0.002 |
| Feature image | MiniMax Image-01 | Generar imagen 16:9 | ~$0.02 |
| SEO metadata | Gemini Flash Lite | Titulo, meta desc, slug | ~$0.001 |
| Publicacion | N8N workflow | WordPress API | $0 |
| **Total** | | | **~$0.03/articulo** |

**Pipeline N8N**: Schedule Trigger -> Perplexity -> DeepSeek (redaccion) -> MiniMax (imagen) -> Gemini (SEO) -> WordPress

### Campanas de Marketing

| Tarea | Modelo | Por que |
|-------|--------|---------|
| Copy de anuncios (Google Ads, Meta) | GPT-4.1 Mini | Bueno en contenido corto y persuasivo |
| Analisis de metricas (CTR, CPA) | DeepSeek V3.2 | #1 en razonamiento con numeros |
| A/B test de copy | Gemini Flash Lite | Generar 10 variantes rapido (195 tok/s) |
| Emails de nurture/follow-up | Claude Sonnet 4.6 | Tono empatico, no generico |
| Cold outreach personalizado | GPT-4.1 | Bueno en personalizacion sin cliches |
| Reportes semanales | DeepSeek V3.2 | Barato, bueno con datos |

### Calificacion de Leads

**Workflow N8N recomendado**:
1. Trigger: Webhook desde formulario/CRM
2. Enrichment: Perplexity busca info de la empresa
3. Scoring: GPT-4.1 Mini evalua BANT (Budget, Authority, Need, Timeline)
4. Routing: Score alto -> Slack a ventas | Score bajo -> email nurture
5. CRM update: Actualizar HubSpot/Pipedrive con score

**Modelo**: GPT-4.1 Mini ($0.40/$1.60 per M) - buen balance entre calidad de juicio y costo.

### Generacion y Debugging de Workflows N8N

| Tarea | Modelo | Notas |
|-------|--------|-------|
| Generar workflow simple | Devstral / DeepSeek V3.2 | Bueno generando JSON de N8N |
| Generar workflow complejo | Claude Opus 4.7 / GPT-4.1 | Mejor para flujos multi-nodo con logica |
| Debugear workflow roto | Claude Sonnet 4.6 | Honesto sobre el error, no inventa fix |
| Documentar workflow | DeepSeek V3.2 | Barato, buena redaccion |

---

## Por Presupuesto

### $0/mes - Solo Local (Ollama + DGX Spark)

```
Modelos a instalar:
- Gemma 4 26B MoE (16 GB) - tareas rapidas, solo 3.8B activos
- Qwen 3.5 72B (42 GB) - calidad alta para coding y razonamiento
- MiniMax M2.5 (90 GB) - 80.2% SWE-Bench, MIT license
- Phi-4 14B (9 GB) - juez local

Para que sirve:
- Coding y debugging (Qwen 3.5 72B o MiniMax M2.5)
- Contenido y redaccion (Qwen 3.5 72B)
- Tareas rapidas y clasificacion (Gemma 4 26B MoE)
- Privacidad total, sin dependencia de internet

Limitaciones:
- Sin tool calling avanzado (modelos locales son peores)
- Sin acceso a datos en tiempo real
- 1-2 modelos activos a la vez en DGX Spark
```

### $20/mes - Una Suscripcion

| Opcion | Que obtienes | Mejor para |
|--------|-------------|-----------|
| **Google AI Pro ($19.99)** | Gemini 2.5 Pro + workspace integration | Todo-en-uno si usas Google |
| **MiniMax Coding Plus ($20)** | M2.1 para coding, 300 prompts/5h | Coding con costo fijo |
| **MiniMax Agent Pro ($19)** | M2.7 para agentes + imagenes | Agentes N8N/OpenClaw |
| **OpenRouter pay-as-you-go** | 290+ modelos, ~$20 de credito | Flexibilidad maxima |

**Recomendacion**: OpenRouter por la flexibilidad. Una API key para todo, fallback automatico.

### $50/mes - Combo Optimo

```
OpenRouter pay-as-you-go: ~$15-20 (DeepSeek + Gemini Flash + Devstral)
MiniMax Agent Pro: $19 (M2.7 para agentes con suscripcion fija)
Gemini CLI: $0 (prototipos rapidos)
Total: ~$35-40

O alternativamente:
OpenRouter: ~$20
Qwen Coding Pro: $50 (Qwen-Coder-Max, 90K req/mes)
Total: $70 (pero coding ilimitado)
```

### $100+/mes - Setup Enterprise

```
Claude Max ($100-200): Opus 4.7 para tareas criticas + Claude Code
OpenRouter ($20): DeepSeek + Devstral para volumen
MiniMax Agent ($19): M2.7 para agentes N8N con costo fijo
DGX Spark (local, $0): Modelos open-source para privacidad
Total: ~$140-240

Routing inteligente:
- Tareas criticas (soporte, contratos) -> Claude Opus 4.7
- Volumen alto (contenido, clasificacion) -> DeepSeek o Gemini Flash
- Agentes 24/7 -> MiniMax M2.7 (suscripcion, no se acaba)
- Privacidad/offline -> Modelos locales en DGX Spark
```

---

## Stack Completo del Solopreneur 2026

Para un emprendedor solo que quiere reemplazar un equipo de 5-10 personas:

| Funcion | Herramienta | Modelo AI | Costo/mes |
|---------|-------------|-----------|-----------|
| **Coding** | Roo Code / Cursor | Devstral o DeepSeek V3.2 | ~$10 |
| **Agente personal** | OpenClaw o Hermes | GPT-4.1 Mini | ~$10 |
| **Automatizacion** | N8N (self-hosted) | Varios via OpenRouter | ~$15 |
| **Contenido/Blog** | N8N + WordPress | DeepSeek V3.2 | ~$2 |
| **Soporte L1** | N8N + chatbot | Gemini Flash Lite | ~$5 |
| **Email marketing** | N8N + SendGrid | GPT-4.1 Mini | ~$3 |
| **Imagenes** | MiniMax Image-01 | Image-01 | ~$5 |
| **Presentaciones** | Manual + AI | Claude Sonnet 4.6 | ~$5 |
| **Total** | | | **~$55/mes** |

> Comparacion: contratar las mismas funciones costaria $15,000-25,000/mes en salarios.
> ROI: 270-450x en el primer mes.

---

## Matriz de Decision Rapida

**Necesito lo mas barato posible** -> DeepSeek V3.2 ($0.14/$0.28 per M)

**Necesito lo mas rapido** -> Gemini 2.5 Flash Lite (195 tok/s, 4s)

**Necesito que no mienta** -> Claude Sonnet 4.6 (#1 honestidad)

**Necesito un agente 24/7** -> MiniMax M2.7 ($20/mes fijo, no se acaba)

**Necesito generar codigo** -> Devstral Small (#1 coding, open-source)

**Necesito analizar datos** -> DeepSeek V3.2 o GPT-4.1 (razonamiento)

**Necesito escribir contenido** -> DeepSeek V3.2 (#1 SEO) o GPT-4.1 (creatividad)

**Necesito soporte al cliente** -> Claude Sonnet/Opus (empatia + honestidad)

**No quiero depender de APIs** -> Ollama + DGX Spark ($0/mes)

**Quiero todo por $50/mes** -> OpenRouter ($20) + MiniMax Agent ($19) + Gemini CLI ($0)
