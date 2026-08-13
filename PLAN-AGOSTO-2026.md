<!-- doc: vigente | verificado: 2026-08-12 -->
# Plan release Agosto 2026 — terminar de aplicar la doctrina del verificador

## 📍 ESTADO AL 11-AGO-2026 16:30 (leer primero)

**El punto 2 del plan (sync de precios) está CERRADO y commiteado como `v4.0.1`.** Ver el
CHANGELOG para el delta completo. Resumen:

- ✅ `sync_prices.py` — nuevo, idempotente, nunca escribe $0, respeta `free_runtime`, ancla por
  `key` (no por `id`). **34 precios corregidos** en `models.py` (diff 52/52, nada fuera de
  `cost_input`/`cost_output`).
- ✅ **`PRICING` derivado de `MODELS`** — se acabó la segunda fuente escrita a mano. Los 19 ids
  huérfanos se borraron tras verificar que no tenían ningún run. Import muerto de `PRICING`
  quitado de `export_for_pages.py`.
- ✅ `rescore_costs.py` aplicado (12.020 runs, solo `cost_usd`/`cost_score`/`final`).
- ✅ `export_for_pages.py` **sin `--recalibrate`** + `regenerate_all.py`. `validate.py` y
  `check_consistency.py` en verde. Ranking: 70 antes y después, nadie entra ni sale, un solo
  movimiento >0,30 (Luna, +0,46, el sobrecosto de 10× corregido).

**Lo que sigue pendiente del plan:** P0 guardrail de tipos huérfanos · P1 suite `produccion_real`
· P0-c los 3 scorers (**septiembre, con protocolo propio**) · P3 DATASHEET + CheatSheet + tag.

### 📏 PENDIENTE para la próxima tanda: `RUNS_PER_TEST` en las suites con herramientas

**Medido el 12-ago-2026, no estimado.** Se re-midieron las 4 suites con herramientas
(`tool_calling`, `customer_support`, `orchestration`, `agent_capabilities`) en 15 modelos,
con el ruteo ya corregido. Comparando contra la medición anterior de los MISMOS modelos:

```
Δ quality   media +0,11  ·  desviación ±0,58  ·  subieron 10, bajaron 5
Δ %toolcall media −1,8pp ·  subieron 3,  bajaron 7
```

**El delta es simétrico**, o sea que las dos mediciones difieren por azar, no por el fix.
Eso convierte el ±0,58 en una medición directa del **ruido del instrumento con
`--quick` (1 run por test)**.

**Y explica algo que llevaba meses sin explicación.** En v3.x se sacó `tool_calling` del
score con el argumento de que "no discriminaba: todos entre 5,3 y 7,2". Con un rango útil
de 1,9 puntos y un ruido de ±0,58, **más de la mitad del rango es ruido**. El problema
nunca fue que la suite midiera lo que no importa: es que **no tiene resolución** con n=1.

Ojo con la conclusión fácil: esto también dice que el *par de validación* de Flip
(gpt-oss-20b 6,91 vs llama-3.3 7,18) está **dentro del ruido** — esa diferencia de 0,27 no
significa nada. El contraste con producción sigue siendo válido; el número que lo
"confirmaba" no lo confirmaba.

**Qué hacer (decidido: va en la próxima tanda, no ahora):** subir `RUNS_PER_TEST` para
estas suites. Triplica el costo de esa parte y por eso no se hace a mitad del lote de
agosto. Antes de subirlo, calcular cuántos runs hacen falta para bajar el ruido bajo 0,2 —
con n=3 el error estándar cae ~1,7×, que probablemente no alcance.

### 🔴 Deuda nueva encontrada el 11-ago (dos guardrails que fallan EN VERDE)

1. **`check_endpoints.py` corre ciego.** Solo `benchmarks/config.py` carga el `.env`, y ese script
   nunca lo importa → cuando lo dispara `regenerate_all.py` da **SIN CREDENCIAL en los 70** y
   **nunca puede reportar un muerto**. Es exactamente el chequeo que existe porque Devstral Small
   estuvo #5 con el endpoint apagado. Fix: una línea (`import benchmarks.config`).
2. **La `OPENROUTER_API_KEY` del `.env` devuelve 401.** Hay que rotarla (Infisical) antes del
   próximo lote. El sync de precios no la necesita: ese endpoint es público.
3. **`check_consistency.py` no ve los bloques auto-generados** (solo caza `score <n>` en prosa).
   Dio verde con el README en 8.34 y `models.json` en 8.80. La red es correr `regenerate_all.py`
   antes de commitear; conviene que el propio chequeo lo cubra.

---

> Semana del **martes 11-ago-2026**. Estado verificado: rama `agentic-backfill` **al día con `origin/main`** (HEAD `c37b7d9d`, Kimi K3, 27-jul). Último tag: v4.0.0.
> **Tesis del mes: el fix del juez del 13-jul fue correcto y quedó a medio aplicar. Dos suites publican 5,00 fijo porque su verificador no existe, y el 37% del catálogo tiene el precio equivocado.**

---

## 0. Punto de partida: lo que YA está resuelto (y no hay que rehacer)

El commit **`6e1075e3` (13-jul-2026, en v4.0.0) — "el LLM verifica hechos, no opina sobre calidad"** ya cerró el problema del juez. Para que no se re-litigue:

- **El bakeoff se corrió**: seis jueces sin conflicto de interés, de 14B a 671B (phi-4, Hunyuan 3, Solar Pro 3, Ling 1T, Nova Pro, Cogito 671B). **Todos saturan.** phi-4: 100% de techo, correlación 0,00 con la verdad objetiva. Cogito 671B: idéntico. **No es problema de tamaño del juez** — y por lo tanto tampoco de temperatura. Cambiar el juez no está en la mesa.
- **El diagnóstico correcto ya está escrito:** el error no era el LLM, era la pregunta. *"¿Está bien hecha esta auditoría?"* → subjetiva → 5/5 siempre. *"¿El texto afirma que los costos suman 9.150 y no 7.400?"* → verificable → sí/no. *"Es lectura comprensiva, no crítica literaria."*
- **La solución ya está implementada:** `verifier.py` (LLM-as-checker), `reasoning` puntúa con el verificador y **levanta excepción** si falta, y los tests con `expected_answer` ya no pasan por el juez.
- **Ya te corregiste sobre `business_audit`**: el spread de 6,00 que parecía discriminación era **ruido de sinónimos** (correlación −0,29 con `string_precision`) — se ordenaban modelos por parecido con el diccionario. Lo que separa de verdad son las trampas duras: **`numeric` (spread 3,62)** y **`honesty_check` (3,53)**.
- **Y dejaste escrito el próximo trabajo:** *"Los 'key insights' los caza cualquier modelo decente — el verificador los pone en 9,25/10 de media. Ese es el próximo trabajo: **más trampas, menos listas de conceptos**."*

**Este plan es ese próximo trabajo.** Todo lo de abajo lo continúa; nada lo repite.

---

## 1. Los tres hallazgos de esta semana

### Hallazgo 1 — La doctrina "fallar ruidoso" no se aplicó al fallback 🔴

`scoring.py:132` cierra el dispatcher así:

```python
else:
    return 5.0  # tipo desconocido, score neutral
```

El mismo commit que puso `raise RuntimeError` en `reasoning` y `must_not_assert` —*"caer al matcher de keywords en silencio daría un número plausible y falso, que es peor que ninguno"*— **dejó intacto el catch-all silencioso**. Y hay tipos que caen ahí.

Barrido de los `expected_answer.type` reales usados en las suites contra los 14 tipos con scorer (descartados los falsos positivos: `string`/`object`/`function`/`integer`/`array` son JSON Schema de definiciones de tools, no verificadores):

| Tipo huérfano | Usos | Suites afectadas |
|---|---|---|
| `json_valid` | 4 | `structured_output`, `news_seo_writing` |
| `json_exact` | 1 | `structured_output` |
| `language_check` | 1 | `news_seo_writing` |

**Consecuencia medida: `structured_output` da exactamente 5,00 en los 117 modelos.** Un solo valor, cero varianza — todos sus tests son `json_valid`/`json_exact`.

**Y es una regresión, no un defecto viejo.** Antes del 13-jul la nota era 30% automática + 70% juez: el 5,0 fijo del auto se diluía y el juez aportaba varianza. El CHANGELOG v2.9.1 lo registra funcionando (*"Fable pierde en tareas cortas de formato: …structured_output −0,98"*). Al sacar del juez los tests con `expected_answer`, la suite quedó **100% dependiente de un scorer que no existe**.

`news_seo_writing` está a medias por lo mismo: 2 de sus tests clavados en 5,0 y solo `hallucination_check` discriminando.

**Lo que lo vuelve prioridad y no una curiosidad:** `json_valid` es *literalmente* el modo de fallo que descartó candidatos en Eco — `null` inconsistente, `Bad request` con output largo, HTML sucio. **El test existe, la suite existe, y devuelve 5,0 para todos.** Es la verdad objetiva más barata del repo (parsea o no parsea) tirada a la basura.

### Hallazgo 2 — 37% del catálogo tiene el precio equivocado 🔴

Cruce del config contra la API pública de OpenRouter, 11-ago: **32 de 87 modelos parseables con drift.** Costo pesa **15% del score** y, a diferencia de una suite constante, **esto sí cambia el orden**.

| Modelo | Config | OpenRouter real | Error |
|---|---|---|---|
| **GPT-5.6 Luna** | $1,00 / $6,00 | **$0,10 / $0,60** | **sobre-costeado 10×** |
| MiMo-V2.5 (omnimodal) | $0,40 / $2,00 | $0,14 / $0,28 | 7,1× |
| MiMo-V2.5 Pro | $1,00 / $3,00 | $0,43 / $0,87 | 3,4× |
| **GPT-5.6 Terra** | $2,50 / $15,00 | **$1,00 / $6,00** | 2,5× |
| GLM 5.2 | $0,95 / $3,00 | $0,49 / $1,54 | 2,0× |
| **DeepSeek V3.2** | $0,14 / $0,28 | **$0,26 / $1,03** | **sub-costeado 3,7×** |
| Kimi K2 | $0,20 / $0,80 | $0,57 / $2,30 | sub 2,9× |

**Luna es #1 hoy (8,34) mientras se le cobra 10× de más en costo** — con el precio real sube. Y publicas que DeepSeek V3.2, tu modelo de producción, es 3,7× más barato de lo que cuesta.

Esto también explica lo de Terra: **no está mal el badge, está mal el precio.** A $2,50/$15 cayó en `tier: medium`; a su precio real ($1/$6, contexto 1,05M) la lectura correcta es *flagship de OpenAI a precio de workhorse*. `terra-pro` y `sol-pro` existen en OpenRouter y no están en config.

Como los precios cambian cada mes o cada semana, **el fix no es actualizarlos: es que dejen de escribirse a mano.** Ya pasó en junio con V4 Flash, se corrigió uno, volvió en 32.

### Hallazgo 3 — Ninguna suite pone al modelo en la situación que rompe producción

Estado vigente de Eco: **`deepseek/deepseek-v3.2@0.2` en producción y funcionando**; el que alucinó fue **V4 Flash**. Contra lo que dice el benchmark:

| Modelo | En producción | `quality_avg` | `content_verificable` |
|---|---|---|---|
| **DeepSeek V3.2** | ✅ en producción, 0 inventos | 8,14 | **7,33** |
| DeepSeek V4 Flash | ❌ alucinó | 8,02 | **10,00** |

La suite que parecía la buena le dio **10,00 al que falló**. Y la causa raíz ya la habías medido en Eco: *"con artículos de 150-200 palabras casi ningún modelo inventó; la invención aparece cuando el texto se alarga… el problema nunca fue que el modelo alucine, era **pedirle 900-1.300 palabras con material para 400**"*.

La alucinación es función de la **razón material/extensión pedida**, y ninguna suite varía esa razón: todas dan material suficiente. El instrumento nunca puso al modelo en la condición que rompe.

---

## 2. Plan de la semana

### ⚠️ Antes de nada: por qué este plan NO arranca por el fix del scoring

El post-mortem del 16-17 jul documenta 11 errores de proceso y 7 bugs, y el #2 es literal: *"el 'definitivo' que colapsó el ranking — se metió `_misma_formula` en `aggregate_metrics` → ranking a 6 modelos, GPT-4.1 falso #1"*.

**Implementar los 3 scorers huérfanos es exactamente ese tipo de cambio**: toca la agregación de `quality_avg` de los 117 modelos a la vez. Es el arreglo correcto, pero **es el más riesgoso del plan y va último, no primero**. Regla dura #4 del proyecto: un solo cambio a la vez, validar antes de seguir.

**Orden por riesgo, no por importancia:**

| | Trabajo | Qué toca | Riesgo | Cuándo |
|---|---|---|---|---|
| 1 | Guardrail que detecta tipos huérfanos | nada — solo detecta | **nulo** | martes |
| 2 | Sync de precios | solo `cost_score` (`rescore_costs.py` es idempotente y tiene `--dry-run`) | **bajo** | martes |
| 3 | Suite `produccion_real` | nada existente — suite nueva es el camino permitido | **bajo** | mié-jue |
| 4 | Los 3 scorers + `raise` en el `else` | `quality_avg` de **todos** | **alto** | viernes o septiembre |

**Protocolo obligatorio para el punto 4** (y para cualquier cambio de scoring futuro):

1. **Snapshot del baseline primero.** Guardar el ranking completo actual (`key`, `quality_avg`, `score_global`, posición) a un JSON versionado. Sin baseline no hay forma de saber qué se rompió.
2. **Rama aparte.** Nunca sobre `main`.
3. **UN scorer a la vez**, no los tres. `json_valid` primero (4 usos, el de mayor impacto), medir, después los otros.
4. **`audit_anomalies.py` como gate** — el post-mortem lo dejó como obligatorio antes de recalibrar, y el error #8 fue justamente arreglar por síntoma en vez de barrer.
5. **Diff contra el baseline**, modelo por modelo. Todo movimiento >0,3 en `score_global` se explica o se revierte. Si el ranking se acorta o aparece un #1 nuevo inesperado, es el error #2 otra vez.
6. **`validate.py`** — el portero: si algo no cuadra, no se publica.
7. Recién ahí, commit.

**Y hay tres salvaguardas que ya existen** (buena noticia, no hay que construirlas):
- `rescore_all.py` **archiva los originales antes de tocar** (`results/_archive-pre-verificador/`) y tiene `--dry-run`.
- El fix del 13-jul **guarda los componentes** (`content_score`, `answer_score`) por separado: *"re-pesar ahora es gratis"*. El re-scoring es reversible sin re-correr modelos.
- La referencia z-score congelada aísla del efecto "agregar un modelo mueve a todos".

**Opción conservadora, perfectamente válida:** hacer 1-2-3 esta semana y **solo reportar** el bug de los scorers huérfanos en el DATASHEET, dejando el fix para un evento de versión deliberado. El hallazgo publicado ya vale como contenido; el ranking no miente más por esperar dos semanas —`structured_output` suma lo mismo a todos, así que no altera el orden— y evita repetir julio. **Recomendado si la semana viene apretada.**

### P0 · Martes — El guardrail (30 min, riesgo nulo)

Un test que falle si algún `expected_answer.type` usado en `tests/` no tiene scorer en el dispatcher. **No cambia ningún número**: solo impide que el próximo tipo nuevo entre en silencio.

Es la lección que ya pagaste dos veces el 13-jul: cazaste `must_not_assert` pasado a `hallucination_check` (*"lo ignoró en silencio y puntuó cualquier cosa"*) y lo arreglaste **para ese tipo**, sin barrer el resto. Por eso quedaron `json_valid`, `json_exact` y `language_check`. El guardrail convierte un hallazgo puntual en una defensa permanente.

### P0-c · Viernes o septiembre — Los 3 verificadores (riesgo alto, con el protocolo de arriba)

1. **Implementar los scorers**, uno por vez. Los tres son verdad objetiva barata, sin LLM:
   - `json_valid` → ¿parsea? ¿tiene las claves exigidas? Binario.
   - `json_exact` → ¿coincide con el objeto esperado?
   - `language_check` → ¿está en el idioma pedido? (de paso caza la fuga de CJK que te mordió con Qwen en Eco)
2. **El `else: return 5.0` → `raise` es el cambio más peligroso y va SEPARADO**, en su propio commit y después de los scorers. Con `raise`, cualquier tipo huérfano que no haya visto tumba el rescore de 10.245 runs históricos completo. Mitigación: **modo estricto en el runner** (falla temprano, sobre datos nuevos) y **modo ruidoso+contador en el rescore histórico** (registra y sigue). No son la misma decisión.
3. `rescore_all.py --dry-run` → revisar → aplicar. Los originales quedan archivados solos.
4. Reportar el delta en el CHANGELOG como corrección, no como mejora silenciosa.

### P0-b · Martes — Sincronizar precios y automatizarlo (1-2 h)

> ⚠️ **La mitad ya está construida: NO reimplementar.** `rescore_costs.py` ya recalcula `cost_usd`/`cost_score`/`final` de los runs históricos desde el precio por-proveedor del config, sin re-correr nada, idempotente y con `--dry-run`. Lo que falta es el paso **anterior**: nadie actualiza `models.py` contra la realidad. El script nuevo es solo fetch + diff + apply, y encadena con el que ya existe y está probado.

1. `sync_prices.py`: lee `https://openrouter.ai/api/v1/models` (pública, sin auth), compara contra el config y **falla ruidoso** listando el drift; `--apply` para escribir sobre `models.py`.
2. Correr, revisar el diff de 32, aplicar.
3. **Encadenar `rescore_costs.py --dry-run`** para ver el impacto, luego aplicar. No tocar `rescore_all.py` (ese re-puntúa calidad, es otro trabajo).
4. **El chequeo entra en `check_consistency.py`** y corre en cada release. Un precio a mano caduca solo, igual que los scores hardcodeados de v3.1.2.
5. Reportar el delta de ranking. Si Luna se mueve, se dice.

> 📌 **Riesgo de drift interno, a resolver de paso:** hay **dos fuentes de precio** en el repo. `rescore_costs.py` usa el config por-proveedor de `models.py` (fuente única declarada); `calculate_costs.py` usa un dict global `PRICING` con fallback `(1.0, 3.0)` para lo que falte — el mismo dict que su propio docstring describe como del "runner viejo" y "ambiguo cuando el mismo id corre en varios proveedores". Sincronizar solo una de las dos deja la otra mintiendo. Verificar si `PRICING` sigue vivo o es legacy que se puede borrar.

### P1 · Miércoles-jueves — Suite `produccion_real`: más trampas duras (6-8 h)

Siguiendo tu propia conclusión —**más trampas, menos listas de conceptos**— todos los tests son `numeric`, `honesty_check`, `json_valid` o `constraint_check`. **Cero `reasoning`**: el verificador ya los pone en 9,25/10 de media, no separan.

| Test | Tipo | Deriva de | Trampa (verdad objetiva) |
|---|---|---|---|
| `material_insuficiente` ⭐ | `honesty_check` | Eco, la causa raíz real | Pedir 900-1.300 palabras con material para 400. **Correcto:** entregar menos y decirlo. **Falla:** rellenar inventando. Con **par de control** de material rico: el hallazgo no es "inventa", es "inventa cuando falta material y no cuando sobra" |
| `fuentes_no_inventadas` | `constraint_check` | Eco | Toda URL/medio citado debe existir en el input. Binario |
| `catalogo_sin_sustituir` | `honesty_check` | Flip / Flipper | Se pide algo que **no está en el catálogo**. **Correcto:** admitirlo y pedir datos. **Falla:** ofrecer el más parecido (le ofreció un pacto de accionistas a quien pidió una asociación) |
| `version_especifica_n8n` | `json_valid` | n8n + MCP | Flujo para **una versión concreta**; trampa: un parámetro que solo existe en la nueva. Verificable: importa o no |
| `html_largo_limpio` | `json_valid` + parser | Eco | HTML de artículo completo con reglas explícitas. ¿`style=` inline? ¿error con output largo? ¿`null`? |
| `presupuesto_de_tarea` | `numeric` | Hermes → Terra → Mercado Libre | Tarea agéntica con tope declarado. **¿resolvió, y a qué costo?** |
| `tool_call_sintaxis` ⭐ | `json_valid` | Flip / Flipper (Groq) | ¿La tool call sale **sintácticamente válida**? Tres niveles, no dos (abajo). El veredicto no lo pone un juez: lo pone la API, que valida antes de devolver |

#### `tool_call_sintaxis` — el test que tu ranking contradice hoy

Verificado en `flip-legal-web/functions/api/chat.ts` (11-ago). **Flipper corre `llama-3.3-70b-versatile` en Groq** (temp 0.3, `tools` + `tool_choice: auto`, timeout 12s, override sin deploy vía `GROQ_MODEL`). Antes corría **`openai/gpt-oss-20b`** y se sacó por esto, escrito en el propio código:

> *"⚠️ NO usar `openai/gpt-oss-20b` con herramientas. Ese modelo contamina el nombre de la función con sus tokens internos de canal y Groq rechaza la generación entera: `attempted to call tool 'responder<|channel|>commentary' which was not in request.tools`. El error llega como 400 —valida antes de devolver—, así que no hay forma de sanearlo de este lado. Costó dos referencias de error encontrarlo: **FL-E-PV3N** y **FL-E-5KHK**."*

Lo que dice el benchmark de esos dos modelos:

| Modelo | `tool_calling_score` | suite `tool_calling` | En producción |
|---|---|---|---|
| GPT-OSS 20B (Groq) | 6,91 | **5,91** | ❌ inusable con tools |
| Llama 3.3 70B (Groq) | 7,18 | **5,33** | ✅ el que corre hoy |

**La suite puntúa mejor al que no puede emitir una tool call válida.** Y explica por qué `tool_calling` salió del score en v3.x por "no discriminar": todos entre 5,3 y 7,2, incluido uno que ni arranca. La suite mide *"¿elige la herramienta correcta?"*; lo que rompe producción es *"¿el nombre sale sintácticamente válido?"*.

**Y no son dos estados, son tres** — el código de Flip documenta los dos fallos reales:

| Nivel | Conducta | Caso real |
|---|---|---|
| ✅ | tool call válida | — |
| ⚠️ | mal envuelta pero **recuperable** desde `failed_generation` | `<function=responder{"texto":"De nada"}</function>` — **llama-3.3, el que usan hoy** |
| ❌ | nombre contaminado, **irrecuperable** | `responder<|channel|>commentary` — gpt-oss-20b |

Un score binario perdería la distinción que decide: llama-3.3 **también** falla el formato, solo que su fallo se rescata. Escala 10 / 5 / 0.

> 📌 **Hallazgo lateral, para Flip, no para el benchmark:** el fallo de llama-3.3 **no tiene referencia de error** porque se rescata — sale por `console.warn`, no por `registrarError()`. Y los logs de Cloudflare *"duran minutos"*. Así que **no se sabe con qué frecuencia el modelo en producción falla el formato**. Es el mismo patrón que ya pagaste en Eco (*"sin instrumentación no había nada que medir"*, resuelto con la columna `modelo_generacion`): contar los rescates en la tabla `errores` —o una columna aparte— convierte un ruido invisible en una métrica. Sin eso, el día que se cambie de modelo tampoco se va a poder saber si mejoró.

Tres reglas de diseño, todas ya pagadas:

- **No inducir el resultado.** *"El primer A/B usó un prompt que decía 'si la fuente da para poco, escribí poco'. Los modelos obedecieron y el juez las castigó parejo. Un test que induce el resultado no mide nada."* La instrucción es idéntica para todos; **lo único que varía es el material**.
- **`presupuesto_de_tarea` estrena costo por tarea *resuelta*** — hoy mides costo por llamada, y el caso Terra prueba que no basta: quemar una semana de cuota en un día sin converger es más caro que un modelo caro que resuelve en 30 min. Va como **eje aparte**, no al score global.
- **No tocar prompts de suites existentes.** Línea base de comparabilidad.

### P2 · Jueves — Medición (2 h de reloj, ~US$35 + nuevos)

Suite nueva sobre ~20 candidatos reales, no sobre los 171. Del runbook: resume de nombre fijo, 10 concurrentes solo para verificables simples, **2 workers** para `presupuesto_de_tarea` y todo lo que lleve tools o multi-turno.

**Cola de modelos, por criterio ICP** (emprendedores de startups y pymes). 405 en OpenRouter vs ~104 en config: la brecha no se cierra, se prioriza.

> 🎯 **Criterio de entrada al catálogo (Cristian, 11-ago-2026): el filtro es la utilidad para un
> emprendedor, no la novedad ni la cobertura.** Medir cuesta dinero y tiempo, y cada modelo que
> entra al ranking es un modelo que alguien puede leer, integrar y estrellarse. Un modelo entra
> solo si un emprendedor podría **elegirlo de verdad**: precio que un pyme puede pagar, acceso
> real (no waitlist ni región), y un caso de uso del ICP (contenido, agentes/n8n, código, atención).
> Muchos de los 405 no cumplen eso — y para esos la respuesta correcta es **no medirlos y decirlo**
> (el Grupo D del plan). Amplitud sin criterio no es un mejor benchmark: es un catálogo más caro
> y menos útil. Ver `AGENTS.md` (filosofía de recomendación) y el agente `model-curator`.

- **Grupo A — ausencias injustificables:** **`anthropic/claude-opus-5`** y **`anthropic/claude-sonnet-5`** no están en config. Sonnet 5 ($2/$10, ctx 1M) es referencia obligada; y `opus-5-fast` **ya redacta en producción en el copiloto de CAR** — medirías lo que ya usas. Más `gpt-5.6-terra-pro` y `sol-pro`.
- **Grupo B — donde un pyme decide de verdad** (out ≤$0,40/M, todos ausentes): `qwen/qwen3.7-flash` ($0,03/$0,13, ctx 1M) · `z-ai/glm-4.7-flash` · `openai/gpt-5-nano` · `inclusionai/ling-3.0-flash` · `qwen/qwen3.5-9b` · `mistralai/ministral-8b-2512` · `amazon/nova-lite-v1`. **El grupo que más le sirve al lector y el más barato de medir.**
- **Grupo C — los que ya pagas o corres:** Kimi K2.5 / K2.6 thinking · variantes thinking de Gemini 3.1.
- **Grupo D — fuera, y dicho en el DATASHEET:** o1/o3/gpt-4/Opus 4.x anteriores · variantes image/audio · `:free` (flaky) · los `-pro` sobre $100/M salida.

> ✅ **Resuelto (11-ago):** Flipper corre **`llama-3.3-70b-versatile` en Groq**. El que se sacó por tools fue **`gpt-oss-20b`**, no el 120B. Ambos ya están medidos y con muestra suficiente (140 y 141 runs) — **no hay que medirlos de nuevo: hay que re-medirlos con `tool_call_sintaxis`**, que es donde el ranking actual dice lo contrario de lo que pasó. Son el par de validación natural del test nuevo: se conoce el resultado de producción de antemano, así que si el test no los separa, el test está mal.

### P3 · Viernes — Release (3-4 h)

- **Si se tomó la vía conservadora** (sin tocar scorers): el release es **v4.0.1** — precios corregidos + suite nueva + hallazgos reportados. **Sin recalibrar**: no cambió la fórmula de calidad, y recalibrar sin necesidad es exponerse gratis.
- **Si se aplicaron los scorers**: recalibrar al final, sobre el dataset completo, con `audit_anomalies.py` y `validate.py` en verde: `export_for_pages.py --recalibrate --scoring-version v4.1`.
- `DATASHEET_2026-08.md` + CheatSheet + tag + `check_consistency.py` antes de publicar.
- **El contenido del mes ya está escrito por los hechos:** *"arreglé el juez en julio y dejé dos suites publicando 5,00 fijo; corregí el precio de 32 modelos; y mi benchmark le puso 10/10 al modelo que me alucinó en producción."* Cágala-Aprende-Repite literal, y nadie más lo puede publicar porque casi nadie corre su propio benchmark contra sus propias decisiones.

---

## 3. Lo que queda instalado

1. **Ningún tipo sin scorer puede puntuar en silencio.** El `else: return 5.0` es el último resto de la doctrina vieja; se cierra y se cubre con un test.
2. **Los precios se sincronizan, no se escriben.** Con guardrail en `check_consistency.py`.
3. **Criterio de suite viva:** cada suite reporta valores distintos y rango. Varianza cero → fuera del score + aviso. Este bug vivió semanas publicando 5,00 sin que nada chillara.
4. **La regla de oro, invertida.** Ya tienes *"diferencia demasiado grande = sospechar de la medición propia"*. Falta la gemela: **"empate perfecto = sospechar de la medición propia"**. Vale para el 5,00 de `structured_output` y para el 5/5 de los seis jueces. Al CLAUDE.md del repo.
5. **Puente producción→benchmark.** Cada modelo descartado en un flujo real es un test candidato. Los casos de este plan vivieron meses en docs de operación sin llegar al instrumento que existe para eso.
6. **Los docs de operación caducan.** `noticias-rss-optimizacion.md` decía lo contrario de lo vigente (que está en `14-alucinacion-causas-y-fixes.md`) y mandó la primera versión de este plan a atribuir al revés. Fecha de verificación obligatoria: con más de un mes, es rumor.
