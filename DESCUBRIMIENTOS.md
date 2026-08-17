<!-- doc: vigente | verificado: 2026-08-16 -->
# Descubrimientos y Observaciones

> Hallazgos no obvios descubiertos durante los benchmarks. Actualizado cada edicion.

## Agosto 2026 (v4.2 – v4.4.2)

### El pilar «Agentes» correlaciona NEGATIVO con hacer trabajo agéntico

Lo más incómodo del mes. Contra la única verdad objetiva que tenemos —el reward de las
tareas Harbor, verificadas por pytest sobre artefactos, no por un juez— sobre 75 modelos:

    pilar Agentes                    −0,20   ← negativa
    compuesto 65% pilar + 35% tools  +0,44
    tool_calling solo                +0,58

Las nueve suites que se llaman «Agentes» miden **prosa sobre agentes**, no ejecución:
`agent_long_horizon` mide sostener el hilo **sin** herramientas y `tool_calling_adversarial`
mide **abstenerse**. Ninguna mide llamar una función y que el flujo siga.

Y el orden de los descubrimientos importa: primero metimos esas dos suites al pilar
creyendo que lo mejoraban (v4.4) y la correlación **empeoró** de −0,14 a −0,20. El nombre
de una suite no dice qué mide.

### Un modelo puede ser #3 en una cosa y #76 en el promedio

Gemini 3.6 Flash: **#3 de 80 en calidad agéntica y #76 de 80 en el índice general**. El
promedio de 29 ejes lo entierra. Salió de que Cristian dijera *"lo estoy usando en Hermes
y funciona muy bien"* contra un número que decía lo contrario — y terminó justificando
publicar cortes por eje individual.

### Calidad alta y cero dentro de un agente no son contradictorios

**Hermes 4 405B tiene calidad 8,20 (top 10 abierto) y saca 0,00 en tareas agénticas**: no
existe endpoint que le dé herramientas. **Llama 3.1 8B Instant sale #4 en «tareas largas»
y también saca 0,00** — esa suite mide sostener el hilo sin herramientas, así que lucirse
ahí y romper el bucle es perfectamente compatible.

Corolario para quien elige: una nota de calidad no dice si el modelo **sirve para tu caso**.

### El z-score inflaba las diferencias seis veces

Toda la población entra en **1,43 puntos** de calidad real. El z-score los repartía sobre
una escala de 0 a 10. La diferencia de serving de Qwen 3.5 397B (NIM vs Ollama Cloud) se
publicó como **2,50 puntos** y el efecto real es **0,34**. Estuvo meses en el pilar del
blog como argumento.

Sigue siendo un efecto grande —0,34 sobre 1,43 mueve muchas posiciones— pero el tamaño
que publicábamos era del método, no del mundo.

### Una regla que no llegó a todas las superficies es una regla que no existe

Medido: **76 condicionales de filtrado en 25 archivos** decidiendo a mano si un modelo se
puede recomendar. Cada campo nació de un fallo distinto y se aplicó **donde dolía ese
día**: `retired` el 13-jul (Devstral Small llevaba meses #5 con el endpoint apagado),
`sirve_para_agentes` el 14-ago (Hermes 4). Lo escrito antes no los tenía; lo escrito
después los copiaba del vecino.

Consecuencia concreta: la página `/mejor-llm-para-agentes/` filtraba a los no-aptos y **la
calculadora no** — ponía a Hermes 4 405B #3 del pilar Agentes.

### Una herramienta puede reportar éxito sin haber hecho nada

`completar_examen --correr` imprimió **«✅ exámenes completados» sin ejecutar un solo
test**, dos veces seguidas, por dos bugs distintos:

1. El resume consolidaba runs **fallidos**. `--resume` saltea por `(modelo, suite, test)`
   sin mirar si el run sirvió; el export solo cuenta `success=True`. Un test que falló las
   cuatro veces quedaba *incompleto para el export y completo para el resume*.
2. El runner escribe sobre el archivo de resume, que vivía en un subdirectorio que
   `load_all_results()` no lee. Aunque corriera perfecto, el resultado se tiraba.

Siete modelos llevaban días fuera del ranking por eso. Al arreglarlo, 11 tests corrieron y
los 11 pasaron — incluido `social_engineering_attempt`, que llevaba 4 fallos y estaba
tapado.

### Preguntar «¿sobra algo?» encuentra lo que «¿falta algo?» no ve

Los detectores del repo cazan **ausencia**: un dato que falta, un score viejo, una página
sin generar. Ninguno cazaba lo contrario: **3 páginas publicadas que ningún generador
regeneraba** desde junio, sirviendo datos congelados. No fallan — cargan, se ven bien y
mienten despacio. Una de ellas declaraba «última actualización» del día.


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

### Benchmark single-turn subestima modelos diseñados para workflow con tools

Ejemplo concreto detectado en Lote 6: **Qwen 3.5 397B Cloud** scoreó:
- 7.7-8.5 en contenido, customer_support, code, agentes
- **4.8-5.8 en `news_seo_writing` suite (5 tests)**

Pero el caso real de Cristian (https://ecosistemastartup.com/apple-pay-y-google-pay-80-menos-fraude-que-tarjetas-fisicas/) usa exactamente Qwen 3.5 397B y los artículos salen excelentes. ¿Por qué la discrepancia?

**El benchmark mide "Qwen solo, sin tools"** — un test single-turn con extracto + system prompt. La cadena real de producción tiene 3 capas:

1. **Perplexity tool** que enriquece runtime con datos verificados (cifras, fuentes, contexto reciente)
2. **Workflow N8N** que preprocesa el input y postprocesa el output
3. **Qwen 3.5 397B** que sólo tiene que **integrar** los datos provistos, no inventarlos

Tests específicos que castigan al modelo bien-comportado:
- `news_no_hallucination_sources`: system prompt dice "NO inventes datos". Si el modelo expande contexto natural → score bajo. En producción **esa expansión sí está respaldada por la tool**.
- `news_seo_article_full`: pide 1500-2500 palabras desde extracto corto. Sin tool, debe rellenar con conocimiento estático (penalizado) o quedarse corto (penalizado). Con tool, tiene fuentes para 1500+ palabras.
- `news_perplexity_enrichment`: datos hardcodeados en prompt en lugar de tool real. El modelo a veces los "embellece" inventando — penalizado por anti-hallucination.

**Implicación**: el ranking global del benchmark refleja "modelo solo". Para uso con workflow + tools, **el ranking puede invertirse**. Modelos como Qwen 3.5 397B (diseñados para integrarse con tools en producción) aparecen "regulares" en el benchmark pero son excelentes en su entorno real.

**Mitigación pendiente**: Lote 7 podría incluir tests con tool calls reales (Perplexity, web search) para diferenciar capacidad-bruta vs capacidad-con-tools. Por ahora, el ranking sirve como baseline pero **no debería ser la única señal** para decidir uso en producción.

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
