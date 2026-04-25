# Descubrimientos y Observaciones

> Hallazgos no obvios descubiertos durante los benchmarks. Actualizado cada edicion.

## Abril 2026 (Lote 4 + Hallazgos tecnicos)

### Thinking models facturan 3-4x mas tokens de lo que parece

Los modelos con razonamiento interno (gpt-5.5, gpt-5.4, kimi-k2.6, glm-5.1, nemotron-3-super, o1, o3) consumen tokens en su "thinking" antes de generar la respuesta visible. Esos tokens se facturan como `completion_tokens` aunque no aparezcan en la API.

**Impacto descubierto al medir 4 lotes**:

| Modelo | Tipo | output_tokens promedio | output visible | factor real |
|---|---|---|---|---|
| Devstral Small | normal | ~600 | ~600 | 1.0× |
| GPT-4.1 | normal | ~700 | ~700 | 1.0× |
| Kimi K2.6 | thinking | ~3500 | ~700 | 5.0× |
| GLM-5.1 | thinking | ~2800 | ~600 | 4.7× |
| GPT-5.5 | thinking | ~2400 | ~500 | 4.8× |
| Nemotron-3 Super | thinking | ~2200 | ~600 | 3.7× |

**Implicaciones**:
1. Suscripciones flat-rate (ChatGPT Pro, Anthropic Pro Max, Kimi $7/sem) se agotan 3-4× mas rapido con thinking models que con modelos normales.
2. Tarifa por token en OpenRouter para thinking model = (tarifa publicada) × ~4 en gasto real.
3. Si tu prompt no requiere razonamiento profundo, prefiere un modelo normal: mismo resultado, 4× mas barato.

### Bug: thinking models devolvian content="" con max_tokens=2048

Detectado al revisar JSONs de Lote 1-3: 165 runs con `success=True` pero `content=""` y `output_tokens=2048` (justo el limite).

**Causa**: el modelo agotaba todo el budget razonando antes de empezar a escribir la respuesta visible. La API responde 200 OK con string vacio.

| Lote | Modelo | empty/91 |
|---|---|---|
| Lote 1 (Kimi vs Opus) | kimi-k2.6 | 47 |
| Lote 3 | kimi-k2.6 | 35 |
| Lote 3 | gemini-2.5-pro | 27 |
| Lote 2 | glm-5.1 | 20 |
| Lote 2 | nemotron-3-super | 18 |
| Lote 4 | gpt-5.5 | 10 |
| Lote 3 | gpt-5.4 | 7 |
| Lote 2 | gpt-5.4-mini | 4 |

**Fix** (en `providers/adapters.py`, abril 25 2026):
- `THINKING_TOKEN_MULTIPLIER = 4` (max_tokens × 4 para thinking)
- `THINKING_MIN_TOKENS = 8192` (piso absoluto)
- Detection por prefijo: `gpt-5*`, `o1*`, `o3*`, `glm-5*`, `kimi-k2.6`, `nemotron*`

**Resultado tras fix** (GPT-5.5 Lote 4): 6 timeouts recuperados con scores 6.3-6.7. Score final del modelo subio de 5.76 (Lote 1) a 6.42.

### Patron: 8 empty tests = bug cosmetico de tool_calling

Detectado al auditar empty responses: muchos modelos NO-thinking tenian exactamente 8 empty tests. Coincide con la cantidad de tests en suite `tool_calling`.

**Modelos afectados** (8 empty cada uno): gpt-4.1, gpt-4.1-mini, mistral-large, devstral-2, mimo-v2-pro, mimo-v2-flash, qwen3-coder, minimax-m2.7, deepseek-chat.

**Causa**: cuando el modelo invoca tools, la API devuelve `message.tool_calls=[...]` y `message.content=None`. El adapter actual guarda solo `content` en `response_preview`. El score sigue funcionando porque mide `tool_calls_made` y `tool_calls_correct`, pero el preview queda vacio.

**Status**: cosmetico, no afecta scoring. Pendiente fix en task #23: serializar `tool_calls` cuando `content=None`.

### HTTP read_timeout 60s causaba timeouts falsos en thinking models

GPT-5.5 daba `httpx.ReadTimeout` a los ~181s. Diagnostico: cliente OpenAI hace 3 retries × 60s = 180s antes de fallar definitivamente. Algunos thinking models con razonamiento extenso (workshop_outline, business_validation) tardan 90-110s legitimos.

**Fix**: `HTTP_READ_TIMEOUT_S = 240.0` en `providers/adapters.py`. Tras el fix, los 6 tests timeout de GPT-5.5 completaron en 50-106s con scores normales (6.3-6.7).

**Diferencia critica**: timeout cliente (httpx) ≠ timeout signal alarm. El primero corta la respuesta de la API, el segundo el tiempo total del test desde Python. Hay que subir ambos para thinking heavy.

### GPT-5.5 / o1 / o3 / gpt-5-pro rechazan temperature distinto de 1.0

Error 400 al enviar `temperature=0.7` con estos modelos. Documentado en OpenAI API: estos modelos solo aceptan default (1.0).

**Fix**: `FIXED_TEMP_MODELS = ("gpt-5.5", "gpt-5-pro", "gpt-5.5-pro", "o1", "o3")` en adapter; el parametro se omite del request.

### GPT-5.5 Pro requiere endpoint Responses API, no chat/completions

Lote 4 mostro 58/58 tests fallidos con 404 para `gpt-5.5-pro`. El modelo **no esta disponible** en el endpoint estandar `/v1/chat/completions`; requiere `/v1/responses`. Mismo patron para `o1-pro`.

**Status**: pendiente integrar en adapter (task #21). Por ahora, gpt-5.5-pro queda excluido del benchmark.

### Atomic incremental save: -10.5h de computo perdidos sin checkpoint

Lote 1 original (abril 22) se corto en 704/728 sin guardar nada. **Costo**: ~10.5h de computo + costo en API. Causa: el runner solo hacia `json.dump` al final del proceso.

**Fix** (abril 23): cada test ahora dispara `_dump_results(partial=True)` inmediatamente despues de evaluar el score. Si el proceso muere por SIGINT, OOM, crash de Python, kernel panic, etc., los runs anteriores ya estan en el JSON.

**Bonus**: `--resume <archivo.json>` permite retomar un benchmark parcial salteando los tests ya completados. `--rerun-empty` y `--rerun-failed` permiten re-correr solo los que fallaron, sin tocar los exitosos.

### Qwen 3.6 Plus es proprietary, no open-source

`Qwen 3.6` (base) es Apache 2.0. `Qwen 3.6 Plus` es un producto comercial de Alibaba **sin pesos publicos**. La confusion venia del prefijo "Qwen" asociado historicamente a open-source.

**Fix**: en `config.py`, `qwen-3.6-plus` marcado `open_source: False, license: "Proprietary"`. Auditoria pendiente para otros "Plus/Max/Pro" (task #24).



### Cambios en el Ecosistema

- **Claude Code removido de suscripcion Pro $20/mes (21 abril 2026)**: Ahora requiere Max $100-200/mes. Alternativas viables: MiniMax M2.7-HS ($40/mes), Gemini CLI (gratis), DeepSeek + Roo Code. Setup de ~$50/mes reemplaza lo que costaba $20.

- **Gemma 4 tiene bug en Ollama**: Tanto el 8B como el 26B devuelven respuestas vacias en `/api/chat` y `/api/generate` con prompts largos. No sirve como juez local. Alternativa: Phi-4 o Qwen 2.5 14B.

- **Coding Plans (nuevos)**: GLM $3/mes, MiniMax $10-150/mes, Kimi ~$7/semana, Qwen $10-50/mes. Todos compatibles con Claude Code como wrapper.

### Comportamiento de Modelos

- **MiniMax y Qwen a veces responden en chino**: Tanto MiniMax M2.7 como Qwen 3.6 Plus ocasionalmente incluyen caracteres chinos en sus respuestas en espanol. Esto ocurre mas frecuentemente en tareas de razonamiento y menos en content generation.

- **GPT-4.1 supera consistentemente a GPT-5.4**: En TODAS las categorias de nuestros tests, GPT-4.1 (varias generaciones atras) rinde mejor que GPT-5.4. Esto podria deberse a que GPT-5.4 esta optimizado para tareas de agente de larga duracion y no para respuestas puntuales como nuestros tests.

- **GPT-5.4 Mini gana a GPT-5.4**: El modelo "mini" supera al modelo completo en todas las categorias. OpenAI parece haber optimizado el mini para respuestas mas directas.

- **Claude Opus es #9 global y #3 en Agentes**: Con los tests de alucinaciones y creatividad, Opus sube de #13 a #9. Sonnet sube a #7 gracias a ser #1 en honestidad (7.62). Donde Claude realmente brilla es en tareas que requieren empatia, protocolos de seguridad y juicio situacional.

- **Devstral Small es la sorpresa del benchmark**: Un modelo de Mistral que cuesta $0.10/$0.30 per M tokens y es open-source (Apache 2.0) lidera en 5 de 6 categorias agrupadas. Su debilidad: customer support (#1 pero otros le pisan los talones).

### Problemas Tecnicos

- **Gemma 4 via OpenRouter es muy lento**: 11-19 tok/s con rate limits frecuentes (429). Mejor correrlo local en DGX Spark.

- **MiniMax Coding Plan no incluye TTS**: El Token Plan (Coding) no da acceso a Speech-02. Se necesita el plan Agent ($19/$69) para TTS.

- **GPT-5.4 usa max_completion_tokens**: No acepta el parametro standard max_tokens. Requiere max_completion_tokens.

- **Qwen 3.6 Plus :free fue deprecado**: La version gratuita en OpenRouter fue removida. Solo la version pagada funciona.

- **Ningun modelo copia strings perfectamente**: En el test de string_precision, ningun modelo logro 10/10 en ningun test. Devstral fue el mejor (8.58) y Claude Opus el peor (7.47). Claude falla especificamente en write_config_file (escribir credenciales en archivos .env).

- **Kimi K2 y Mistral Large no sirven para articulos largos**: 100% timeout en news_seo_writing. No pueden generar articulos de 1500+ palabras sin cortarse.

- **DeepSeek V3.2 es el mejor para noticias SEO**: #1 en news_seo_writing (7.67), ideal para el workflow de ecosistemastartup.com que actualmente usa Claude Sonnet.

### Sobre el Scoring

- **[CORREGIDO en v1.3.0] El scoring favorecia formato sobre sustancia**: Modelos que producen respuestas bien estructuradas (headers, listas, longitud adecuada) obtenian scores altos aunque el contenido sea generico. Formato valia 3/10 puntos (30% de calidad). Ahora vale 2/10 (20%) y se valida contenido real con score_expected_answer (60% del score de calidad cuando hay expected_answer). Ver CHANGELOG para detalles.

- **La latencia desde Chile penaliza a modelos lentos**: Qwen 3.6 Plus tiene 83s de latencia promedio, lo que baja su score significativamente vs Gemini Flash Lite con 4.7s.

- **El costo impacta el ranking**: Con 15% de peso, modelos caros como Claude Opus ($0.00417/call) bajan vs modelos baratos como DeepSeek ($0.00024/call).

### Recomendaciones Basadas en Descubrimientos

1. **Para espanol puro sin caracteres chinos**: Usa GPT-4.1, Claude, o Devstral. Evita MiniMax y Qwen para contenido editorial en espanol.

2. **Para agentes N8N que necesitan funcionar 24/7**: DeepSeek V3.2 o Devstral por costo y disponibilidad. MiniMax con suscripcion fija si prefieres predecibilidad.

3. **Para tareas que requieren juicio y empatia**: Claude Opus o Sonnet. Paga el premium por la calidad en customer support.

4. **Para volumen alto y velocidad**: Gemini 2.5 Flash Lite (212 tok/s) o Devstral (171 tok/s).
