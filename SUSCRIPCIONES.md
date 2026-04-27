# Comparacion de Suscripciones Mensuales Fijas

> Ultima actualizacion: 22 de Abril de 2026
> Los precios y planes pueden cambiar. Verifica datos actuales antes de suscribirte.
> **Objetivo**: Encontrar la mejor suscripcion fija para usar con agentes (OpenClaw, N8N) sin sorpresas de costo.

## Suscripciones con Precio Fijo Mensual

### Tier Gratuito

| Servicio | Precio | Modelos | Limites | Compatible N8N/OpenClaw | Notas |
|----------|--------|---------|---------|------------------------|-------|
| Ollama Local | $0 | Llama, Qwen, Mistral, etc. | Sin limites | Si (nativo) | Requiere hardware propio |
| Ollama Cloud Free | $0 | Limitados | Muy restrictivos | Si | Para probar |
| OpenRouter Free | $0 | 27 modelos gratis | 20 req/min, 200/dia | Si | DeepSeek R1, Llama 3.3 gratis |
| Google AI Studio | $0 | Gemini Flash | 15 req/min | Si | Tier gratuito generoso |
| Groq Free | $0 | Llama, Mixtral | 30 req/min, TPD | Si | Ultra rapido pero limites diarios |

### Tier $10/mes

| Servicio | Precio | Mejor Modelo | Limites | Compatible N8N/OpenClaw | Para Agentes |
|----------|--------|-------------|---------|------------------------|-------------|
| **MiniMax Coding Starter** | $10/mes | MiniMax M2.1 | 100 prompts/5h | Si (API) | Basico para probar |

### Tier $20/mes (Estandar de la industria)

| Servicio | Precio | Mejor Modelo | Limites | Compatible N8N/OpenClaw | Para Agentes |
|----------|--------|-------------|---------|------------------------|-------------|
| **ChatGPT Plus** | $20/mes | GPT-4o, o3-mini | ~80 msg/3h (GPT-4o) | Si (API separada) | Bueno - lider en tool calling |
| **MiniMax Coding Plus** | $20/mes | MiniMax M2.1 | 300 prompts/5h | Si (API) | Bueno - rapido y agentico |
| **Google AI Pro** | $19.99/mes | Gemini 2.5 Pro | Generosos | Si | Muy bueno - rapido y capaz |
| **MiniMax Agent Pro** | $19/mes | MiniMax M2.7 | Generosos | Si | Excelente para agentes |
| **Ollama Cloud Pro** | $20/mes | Todos los open-source | Session limits (reset 5h) | Si | Bueno - costo predecible |
| **Claude Pro** | $20/mes | Claude Sonnet 4.5 | ~100 msg/dia | NO (sin API, sin Claude Code desde 21/04) | Solo chat web |
| **Perplexity Pro** | $20/mes | Sonar, GPT-4o | 600+ queries/dia | No (orientado a busqueda) | No es para agentes |
| **Mistral Le Chat** | ~$15/mes | Mistral Large | Generosos | Parcial | Bueno para texto |

### Tier $30/mes

| Servicio | Precio | Mejor Modelo | Limites | Compatible N8N/OpenClaw | Para Agentes |
|----------|--------|-------------|---------|------------------------|-------------|
| **SuperGrok** | $30/mes | Grok 4.20 | Generosos | Si (API compatible) | Bueno - #4 global |
| **Claude Team** | $30/usuario | Claude Opus | Mas que Pro | NO (suscripcion no da API) | Solo chat web |

### Tier $50/mes

| Servicio | Precio | Mejor Modelo | Limites | Compatible N8N/OpenClaw | Para Agentes |
|----------|--------|-------------|---------|------------------------|-------------|
| **MiniMax Coding Max** | $50/mes | MiniMax M2.1 | 1000 prompts/5h | Si (API) | Muy bueno - alto volumen |
| **Qwen Coding Pro** | $50/mes | Qwen-Coder-Max | 90K req/mes, 10x tokens | Si (API) | Excelente para coding |
| **MiniMax Agent Pro+** | $69/mes | MiniMax M2.7 | Muy generosos | Si | Excelente para agentes |

### Tier Premium ($100+/mes)

| Servicio | Precio | Mejor Modelo | Limites | Compatible N8N/OpenClaw | Para Agentes |
|----------|--------|-------------|---------|------------------------|-------------|
| **Ollama Cloud Max** | $100/mes | Todos open-source | Generosos | Si | Bueno - sin sorpresas |
| **MiniMax Coding Ultra** | $150/mes | MiniMax (ultra-speed) | 1000 prompts/5h, max speed | Si | Para uso intensivo |
| **ChatGPT Pro** | $200/mes | GPT-5.2, o3 | Muy generosos | Si (API separada) | Excelente |
| **Google AI Ultra** | $249.99/mes | Gemini 3.1 Pro | Ilimitado* | Si | Excelente |
| **SuperGrok Heavy** | $300/mes | Grok 4 | Generosos | Si | Top tier |

### Xiaomi MiMo Token Plan (NUEVO, abril 2026 — pendiente testear V2.5)

Lanzado 22 abril 2026. **Una suscripción = 8 modelos** (V2.5 series + V2 series + TTS). Compatible con OpenClaw, Claude Code, OpenCode, KiloCode. API: `platform.xiaomimimo.com`.

| Plan | Mensual (first) | Mensual normal | Anual | Credits/mes | Multiplicador Lite |
|------|-----------------|----------------|-------|-------------|---------------------|
| **Lite** | $5.28 | $6 | save 12% | 60M | 1x (baseline) |
| **Standard** | $14.08 | $16 | save 12% | 200M | 3.3x |
| **Pro** | $44.00 | $50 | save 12% | 700M | 11.7x |
| **Max** | $88.00 | $100 | save 12% | 1,600M | 26.7x |

**Cómo se calculan los credits**:
- 1 token = 1 credit en MiMo-V2.5 (multimodal base)
- 1 token = 2 credits en MiMo-V2.5-Pro (flagship reasoning)
- **Off-peak** (16:00-24:00 UTC, perfecto para LATAM que cae 13:00-21:00 hora local) = 0.8x consumption (20% descuento)

**Modelos accesibles** (todos los planes tienen acceso a los 8):
- MiMo-V2.5-Pro: flagship reasoning (1M context)
- MiMo-V2.5: all-in-one multimodal nativo
- MiMo-V2.5-TTS / VoiceClone / VoiceDesign: text-to-speech (gratis por tiempo limitado)
- MiMo-V2-Pro, V2-Omni, V2-TTS: serie anterior

**Descuentos disponibles**:
- 12% off primera compra (incluido en precios "first" arriba)
- 23% off primera renovación auto (nuevo usuario) → $33.88 Pro tras renovar
- 30% off primera renovación auto (existing user)
- Annual save 12% adicional vs mensual auto-renewal

**Recomendación por volumen** (asume 1800 tokens promedio per call: 300 input + 1500 output):

| Volumen mensual | Plan recomendado | Razón |
|---|---|---|
| <30K calls (~54M credits con V2.5) | **Lite $5.28-6** | Cabe holgado |
| 30K-110K calls (~200M credits) | **Standard $14-16** ⭐ | Balance ideal para emprendedor con varios agentes |
| 110K-380K calls | Pro $44-50 | Si tenés 5+ workflows N8N en producción |
| 380K+ calls | Max $88-100 | Volumen industrial |

**Para benchmarkear V2.5 + V2.5-Pro**: requiere **Standard mínimo** (~110M credits para 91 tests × 2 modelos). Lite no alcanza.

⚠️ **Pendiente del benchmark**: testear MiMo-V2.5 y V2.5-Pro en los 91 tests para validar si justifica la suscripción vs alternativas. Estado actual: solo V2 series (MiMo-V2-Flash, V2-Pro, V2-Omni) están en `docs/data/models.json`.

---

## Opcion Pay-as-you-go (Sin Suscripcion)

Para quien prefiere pagar solo lo que usa:

| Proveedor | Modelo Recomendado | Costo Estimado/mes* | Setup | Notas |
|-----------|-------------------|---------------------|-------|-------|
| **OpenRouter** | DeepSeek V3.2 | $2-10 | 1 API key para todo | **RECOMENDADO** - 290+ modelos, sin markup |
| **DeepSeek API** | DeepSeek V4 | $3-15 | API directa | Cache a $0.03/M, muy economico |
| **Google AI** | Gemini 2.5 Flash | $2-8 | API directa | Tier gratuito + pay-as-you-go |
| **Groq** | Llama 3.3 70B | $1-5 | API directa | Ultra rapido, pero rate limits |
| **Together AI** | Varios | $3-12 | API directa | Limites dinamicos que crecen |
| **OpenAI API** | GPT-4o-mini | $5-20 | API directa | Mas caro pero confiable |
| **Fireworks AI** | Varios | $2-10 | API directa | Buen balance precio/velocidad |
| **MiniMax API** | MiniMax M2.7 | $3-15 | API directa | SOTA en agentes, $0.30/$1.20 per M |
| **Qwen API** | Qwen 3.6 Plus | $2-8 | Alibaba Cloud | 1M contexto, muy economico |

> *Estimado para uso moderado de agente: ~500K-2M tokens/dia

---

## Recomendaciones por Caso de Uso

### Para agente 24/7 con bajo presupuesto
1. **Ollama Local** (gratis) + **OpenRouter free tier** como backup
2. **Ollama Cloud Pro** ($20/mes) si no tienes hardware
3. **OpenRouter pay-as-you-go** con DeepSeek V3.2 (~$5-10/mes)

### Para agente de alta calidad
1. **MiniMax Agent Pro** ($19/mes) - M2.7 es SOTA en tareas agenticas
2. **Google AI Pro** ($19.99/mes) - Gemini 2.5 Pro es top 3 global
3. **ChatGPT Plus** ($20/mes) + API - GPT-4o lider en tool calling
4. **SuperGrok** ($30/mes) - Grok 4.20 es #4 global

### Para nunca quedarse sin servicio
1. **Ollama Local** - literalmente imposible quedarse sin servicio
2. **OpenRouter** con fallback automatico entre modelos
3. **Qwen API** - 15K RPM, 10M TPM (limites mas generosos)

### Para mejor relacion calidad/precio
1. **DeepSeek V3.2** via OpenRouter ($0.14/$0.28 per M) - 90%+ de calidad de GPT-4o al 5% del precio
2. **MiniMax M2.7** ($0.30/$1.20 per M) - SOTA en agentes, excelente precio
3. **Qwen 3.6 Plus** (GRATIS en preview / $0.33 per M) - 1M contexto
4. **Gemini 2.5 Flash** ($0.30/$2.50 per M) - Rapido y capaz

---

## Suscripciones que DEBES Probar (Orden de Prioridad)

### Ya probadas (segun contexto)
- [x] Anthropic Claude (suscripcion no da API para agentes, API pay-as-you-go si funciona)
- [x] MiniMax M2.7 (funcionando bien)
- [x] Qwen 3.5 25B via Ollama (funcionando bien)
- [x] Qwen 3.6 Plus (funcionando bien)

### Por probar - Alta prioridad
- [ ] **OpenRouter pay-as-you-go** - Una API key, 290+ modelos, fallback automatico
- [ ] **MiniMax Agent Pro** ($19/mes) - SOTA en agentes, suscripcion fija
- [ ] **MiniMax Coding Plus** ($20/mes) - Para coding con costo predecible
- [ ] **Google AI Pro** ($19.99/mes) - Gemini es top 3 y muy rapido
- [ ] **DeepSeek API** (pay-as-you-go) - El mas economico con buena calidad
- [ ] **Qwen Coding Pro** ($50/mes) - Qwen-Coder-Max, 90K req/mes

### Por probar - Media prioridad
- [ ] **ChatGPT Plus** ($20/mes) + API - Mejor tool calling
- [ ] **Ollama Cloud Pro** ($20/mes) - Costo fijo predecible
- [ ] **SuperGrok** ($30/mes) - #4 en Arena, API compatible OpenAI
- [ ] **Groq** (free/pay-as-you-go) - Velocidad extrema

### Por probar - Baja prioridad
- [ ] **Mistral Le Chat** (~$15/mes) - Bueno pero no destaca para agentes
- [ ] **Perplexity Pro** ($20/mes) - Solo si necesitas busqueda web integrada
- [ ] **Together AI** (pay-as-you-go) - Alternativa a OpenRouter
- [ ] **Cerebras** (pay-as-you-go) - Si la velocidad es critica
- [ ] **Fireworks AI** (pay-as-you-go) - Buen balance general

---

## Análisis de Break-Even por Perfil de Uso

> Generado por `python benchmarks/calculate_breakeven.py --markdown`. Re-correr cuando cambien precios o se agreguen suscripciones.

Asumimos **300 input + 1500 output tokens por call** (escenario realista de agente con prompt detallado y respuesta sustantiva).

### Perfiles de usuario

| Perfil | Calls/mes | Escenario típico |
|---|---:|---|
| Light (test/dev) | 100 | Probar 1-2 modelos, debuggear flujos |
| Casual (agente ocasional) | 500 | 1 flow N8N corriendo cada hora laboral |
| Active (agente diario) | 2,000 | 3-5 agentes activos, equipo pequeño |
| Heavy (N8N 24/7) | 10,000 | Workflows constantes, múltiples agentes |
| Power (multi-agente prod) | 30,000 | SaaS con agentes en producción |

### Costo mensual pay-per-use por perfil

| Modelo | Light | Casual | Active | Heavy | Power |
|---|---:|---:|---:|---:|---:|
| **Devstral Small** (#1 ranking, open) | $0.05 | $0.24 | $0.96 | $4.80 | $14.40 |
| **DeepSeek V3.2** (#7, open MIT) | $0.06 | $0.32 | $1.29 | $6.43 | $19.28 |
| **DeepSeek V4 Flash** (open MIT) | $0.05 | $0.23 | $0.92 | $4.62 | $13.86 |
| **Nemotron 3 Super** (NIM gratis 40 RPM) | $0 | $0 | $0 | $0 | $0 |
| **Gemini 2.5 Flash Lite** | $0.05 | $0.24 | $0.94 | $4.72 | $14.18 |
| **MiniMax M2.7** (SOTA agentes) | $0.19 | $0.94 | $3.78 | $18.90 | $56.70 |
| **Qwen3 Coder** (open Apache) | $0.09 | $0.47 | $1.89 | $9.45 | $28.35 |
| **GPT-4.1 Mini** | $0.25 | $1.26 | $5.04 | $25.20 | $75.60 |
| **GPT-4.1** | $1.26 | $6.30 | $25.20 | **$126** | **$378** |
| **GPT-5.5** (thinking, 4× output real) | $6.99 | $34.95 | **$140** | **$699** | **$2,097** |
| **Claude Sonnet 4.6** | $2.34 | $11.70 | **$46.80** | **$234** | **$702** |
| **Claude Opus 4.7** | $11.70 | $58.50 | **$234** | **$1,170** | **$3,510** |
| **Kimi K2.6 thinking** (4× output real) | $1.39 | $6.97 | $27.90 | $139.50 | $418.50 |

### Break-even por suscripción

Calls/mes en que la suscripción cuesta lo mismo que pagar API. Por encima → la suscripción es más barata.

| Suscripción | Modelo equivalente | Break-even | Perfil |
|---|---|---:|---|
| **$10 MiniMax Coding Starter** | MiniMax M2.7 | 5,291 | Active → Heavy |
| **$19 MiniMax Agent Pro** | MiniMax M2.7 | 10,052 | Heavy → Power |
| **$20 MiniMax Coding Plus** | MiniMax M2.7 | 10,582 | Heavy → Power |
| **$20 Ollama Cloud Pro** | Devstral Small | 41,666 | Power+ (no conviene si solo Devstral) |
| **$20 Google AI Pro** | Gemini Flash Lite | 42,328 | Power+ |
| **$30 SuperGrok** | ≈ GPT-4.1 | 2,380 | Active → Heavy |
| **$50 MiniMax Coding Max** | MiniMax M2.7 | 26,455 | Heavy → Power |
| **$50 Qwen Coding Pro** | Qwen3 Coder | 52,910 | Power+ |
| **$69 MiniMax Agent Pro+** | MiniMax M2.7 | 36,507 | Power+ |
| **$100 Ollama Cloud Max** | Devstral Small | 208,333 | Power+ |
| **$150 MiniMax Coding Ultra** | MiniMax M2.7 | 79,365 | Power+ |
| **$200 ChatGPT Pro** | GPT-5.5 (thinking) | 2,861 | Active → Heavy |

### Recomendación por perfil

| Perfil | Mejor opción | Por qué |
|---|---|---|
| **Light** (100 calls) | Pay-per-use OpenRouter + Devstral / DeepSeek V3.2 (~$0.05-0.30/mes) o NVIDIA NIM gratis | Suscripción es overkill — pagás $20 para usar $0.30 |
| **Casual** (500 calls) | Pay-per-use con Devstral o DeepSeek (~$0.24/mes) **o** $20 Ollama Cloud Pro si querés más calidad fija | Por debajo de 1K calls cualquier sub es derroche |
| **Active** (2K calls) | **MiniMax Agent Pro $19** *o* **Google AI Pro $19.99** | A 2K calls Claude Sonnet API ya cuesta $46.80, GPT-5.5 thinking $140. Sub gana fácil |
| **Heavy** (10K calls) | **MiniMax Coding Max $50** *o* **Qwen Coding Pro $50** | Claude Sonnet API = $234, GPT-4.1 = $126. Sub a $50 = ahorro ~70% |
| **Power** (30K calls) | Stack mixto: **ChatGPT Pro $200** (razonamiento) + **MiniMax Coding Ultra $150** (volumen) + **Ollama Cloud Max $100** (open fallback) | Combinar suscripciones específicas vs pagar $702/mes Claude API |

### Hallazgos cualitativos

1. **ChatGPT Plus ($20) y Claude Pro ($20) son chat web only — NO dan API**. Inservibles para agentes (OpenClaw, N8N, Hermes). El equivalente "premium con API" es ChatGPT Pro ($200) o Anthropic API directa pay-per-use.

2. **Modelos open-source ultra baratos hacen suscripciones casi nunca rentables hasta nivel Heavy**: Devstral, DeepSeek V3.2/V4, Gemini Flash Lite — todos rondan $5-20/mes incluso en Heavy. Pagás API directa con tranquilidad.

3. **NVIDIA NIM gratis (40 RPM)** cubre perfectamente el perfil Light/Casual sin pagar nada. Limita el volumen pero da acceso a Nemotron Ultra 253B, Qwen 3-Next 80B, Kimi K2 thinking.

4. **GPT-5.5 thinking infla 4× el costo** por reasoning interno facturado: en Active (2K calls) cuesta $140/mes vs $25 que cuesta GPT-4.1. Si no necesitás razonamiento, NO uses thinking models.

5. **MiniMax es la suscripción con mejor break-even** por su precio bajo de tokens base ($0.30/$1.20). Active→Heavy ya gana vs API.

6. **Suscripciones con cap por hora** (300 prompts/5h, 1000 prompts/5h, etc.) imponen un techo real: en Power profile (30K/mes = ~1000/día), incluso $50 MiniMax Max puede llenarse.
