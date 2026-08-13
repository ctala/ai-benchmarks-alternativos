# Plan v4.1 — una sola frontera de comparabilidad

> **Decisión (Cristian, 12-ago-2026): agosto se cierra con v4.1 funcionando.** No se hace
> un release intermedio con lo medido hoy para después rehacerlo. Todo lo que rompe
> comparabilidad entra en ESTE corte, se re-mide una vez, y queda una sola frontera
> documentada en vez de tres archivados sueltos.

## Por qué v4.1 y no v4.0.3

Hoy (12-ago) se encontraron cinco cosas que cambian **cómo se mide**, no solo qué se
publica. Cada una, sola, obliga a archivar y re-medir un pedazo. Juntas, obligan a
re-medir una vez:

| Hallazgo | Qué rompe |
|---|---|
| `max_tokens` 2048 vs 8192 según el modelo | condiciones de examen distintas para el mismo prompt |
| niah rediseñado (needles + grilla + techo) | otra prueba, ya archivados 2.058 runs pre-2-jun |
| Suite `integridad_idioma` nueva | eje que no existía |
| Ruteo sin `require_parameters` | ya corregido y re-medido (19 modelos, 342 runs) |
| Prompts sin persistir | ya corregido: `PROMPTS.md` + `prompt_sha` |

Los dos últimos ya están hechos. Los tres primeros son v4.1.

---

## 0. Lo que dice la investigación (no reinventar la rueda)

Investigado el 12-ago contra las fuentes, no de memoria. **Regla #10 del repo padre.**

| Práctica | Quién | Nosotros |
|---|---|---|
| Prompts publicados | lm-eval-harness: *"publicly available prompts ensures reproducibility and comparability"* · Artificial Analysis | ✅ hecho hoy |
| Ground truth objetivo > juez LLM | LiveBench: *"verifiable, objective ground-truth answers... **without the use of an LLM judge**"* | ✅ desde 13-jul, completado hoy |
| `max_tokens` uniforme | LiveBench: **4096 por defecto**, override explícito | ❌ **v4.1** |
| Recortar la traza de CoT | lm-eval-harness: `think_end_token` | ❌ **v4.1** |
| Model ≠ Endpoint | Artificial Analysis: *"A single model may have multiple endpoints across different providers"* | 🟡 dato crudo desde hoy |
| Costo/velocidad FUERA del ranking | Artificial Analysis: se reportan **aparte** del Intelligence Index | ❌ **a evaluar** |
| Intervalo de confianza publicado | Artificial Analysis: ±1% con evaluaciones repetidas | 🟡 tenemos `quality_ci95`, no se destaca |
| Refresco anti-contaminación | LiveBench: preguntas nuevas cada mes | ⛔ **descartado** (ver abajo) |

### ¿Adoptamos lm-eval-harness?

**No como herramienta; sí como práctica.** Está construido para otra forma: modelos de
HuggingFace, datasets fijos y evaluación por log-likelihood sobre opciones. El nuestro es
API generativa, en español, con suites escritas desde casos reales de emprendedores y
verificadores propios. Migrar sería un rewrite que además tiraría lo único que nos hace
distintos. Lo que **sí** se adopta: prompts publicados (hecho), versionado por hash
(hecho), y `think_end_token` (v4.1).

### Contaminación: descartada, y con argumento

LiveBench rota preguntas cada mes porque publica las suyas. Nosotros acabamos de publicar
206 prompts que llevan desde abril en un repo público. **Decisión de Cristian: no aplica.**
No somos un benchmark que los laboratorios miren para entrenar; somos una herramienta
chica para una comunidad concreta. El costo de rotar prompts (perder toda la serie
histórica cada mes) es enorme y el riesgo es hipotético. Queda anotado como riesgo
conocido y aceptado, no como olvido.

---

## 1. El español necesita 1,62× más tokens — medido, no estimado

Sobre **3.410 respuestas reales** del propio benchmark:

```
2,47 caracteres por token (español)   vs   4,00 de la heurística inglesa
→ el español necesita 1,62× más tokens para el MISMO texto
```

Qué significa en la práctica:

| `max_tokens` | Texto que entra en español | Tests que piden hasta 1.300 palabras |
|---|---|---|
| 2048 (actual, no-thinking) | ~920 palabras | ❌ **no caben** |
| **4096 (propuesto)** | ~1.840 palabras | ✅ con margen |
| 8192 (actual, thinking) | ~3.680 palabras | ✅ sobra |

**Esto explica el 31,3% de respuestas truncadas** en modelos no-thinking: no era que
escribieran de más, era que 2048 tokens en español no alcanzan para lo que el test pide.
El 4096 de LiveBench nos sirve por una razón que ellos no tenían — en español rinde la
mitad.

---

## 2. Los tres cambios de v4.1

### 2.1 `max_tokens` uniforme en 4096

**Un solo presupuesto visible para todos.** Se acabó el 2048/8192 según el modelo.

- Elimina la asimetría: mismo prompt, mismas condiciones.
- Elimina el truncamiento del 31% en no-thinking.
- Cuesta poco: se paga por token generado, no por presupuesto. Solo sube el gasto de los
  que hoy se cortaban.

### 2.2 El razonamiento se recorta, no se presupuesta

El multiplicador ×4 nació de un problema real (los thinking agotaban el budget razonando y
devolvían `content=""`) pero confundió dos presupuestos: los tokens de razonamiento
interno y los de la respuesta que se juzga.

Lo correcto, y es lo que hace lm-eval-harness: **separar la traza del razonamiento de la
respuesta**, juzgar solo la respuesta, y dar a todos el mismo presupuesto visible.

Verificado el 12-ago sobre 10 modelos: `reasoning: {enabled: false}` funciona en 7 de 10
por OpenRouter (GLM 5.2, Kimi K2.6, Qwen 3.7 Flash, Nemotron 3.5 Lightning, DeepSeek V3.2,
MiniMax M3, Ling 3.0 Flash). Fallan con 400 los *always-reasoning*: DeepSeek R1, Muse
Glimmer, Gemini 3.1 Pro.

⚠️ **Apagar el thinking NO es neutral**: en la prueba, Nemotron Lightning respondió 41,98%
y MiniMax M3 respondió 10,93% a un cálculo cuya respuesta es 19,13%. Con razonamiento
acertaban. Por eso **no se apaga el thinking**: se recorta la traza al puntuar y se deja
que cada modelo use su modo nativo. Las variantes `(thinking)` explícitas del catálogo (14
hoy) siguen como comparación aparte.

### 2.3 niah: un prompt canónico por (tipo, tamaño)

| | Hoy | v4.1 |
|---|---|---|
| Combinatoria | 5 tipos × 3 posiciones × 6 tamaños | **5 tipos × 6 tamaños** |
| Tests | 59 | **30** |
| Posición | dimensión propia | **fija por tipo, rotando** — cada tamaño cubre 25/50/75 con tipos distintos |
| Costo estimado | — | **−40%** (~$243 de input sobre 47 modelos con ventana declarada) |

Conserva la señal de *lost in the middle* sin multiplicar tests, y deja un prompt canónico
por celda. **No se materializa el texto**: serían ~35 MB contra 1,1 MB de corpus
commiteado. El prompt "ya existe" como corpus + receta determinista, y `PROMPTS.md`
registra la receta con su hash.

El gate de capacidad ya está corregido (12-ago): reserva el presupuesto de salida antes de
decidir si un tramo entra. Eso solo ya evitaba 378 fallos históricos falsos en 23 modelos.

---

### 2.4 Las suites agénticas: medir orquestar, no narrar

**La evidencia, sobre 719 runs de 125 modelos en la suite `orchestration`:**

```
correlación  tool_calling ↔ quality   :  −0,07   ← CERO
correlación  content_score ↔ quality  :  +0,55
```

**La suite no mide orquestación.** Su nota está desacoplada de elegir bien la herramienta y
la manda la prosa. Es un test de *explicar un plan* con nombre de orquestación.

El caso que lo destapó: Nemotron 3.5 Lightning sacó **10,0 eligiendo la herramienta
correcta y 2,5 de nota** en `tool_selection_precision`. Emitió la tool call y no explicó —
que es lo que hace un agente en un loop real. Qwen 3.6 35B sacó **0,0 en tool calling y
7,5 de nota** en el mismo test: escribió bien y no llamó a nada. **El que orquestó bien
perdió; el que narró bien ganó.**

Y se confirma por el otro lado: en `agent_long_horizon`, la **única** suite multi-turno,
el orden se invierte — Lightning **8,92** vs Qwen **7,06**.

**Los tres problemas de diseño:**

1. **Un número para dos capacidades.** Elegir herramienta y explicar el plan se colapsan en
   `quality`, y gana la que no da nombre a la suite.
2. **Un solo turno para medir algo multi-turno.** Un agente real actúa, observa el
   resultado y después explica. El test pide todo junto y puntúa la explicación, penalizando
   el patrón *act-first* — que es el más eficiente en producción.
3. **Duplica una señal que ya existe.** `tool_calling` se mide aparte y bien; la nota de la
   suite lo ignora.

**Qué se hace (decisión de Cristian, 12-ago): se cambian los prompts.** Un test que no mide
lo que dice medir no se conserva por comparabilidad — la comparabilidad de un número
equivocado no vale nada. Por eso esto es v4.1 y no un parche.

| | Hoy | v4.1 |
|---|---|---|
| Tipo | `single` en 4 de 5 suites agénticas | **`multi_turn_script`** — la maquinaria ya existe |
| Ciclo | pedir plan + ejecución en un turno | **actuar → observar resultado → continuar** |
| Nota | una, dominada por la prosa | **dos señales separadas**: selección de herramienta y convergencia |
| Estilo | premia narrar antes de actuar | **no induce estilo**: se mide qué logró, no cómo lo contó |

**Costo:** ~$79 de re-medición sobre los 68 rankeados (multi-turno, ~5 llamadas por test;
el input acumula historial así que el real es algo mayor). **2.939 runs** quedan fuera de
comparación, incluidos los 342 que re-medimos hoy — asumido: se re-mide una vez, no tres.

**Conexión con `presupuesto_de_tarea`** (del plan de agosto): el rediseño multi-turno es el
mismo motor que necesita el test del caso Terra. Se construyen juntos.

### 2.5 Cómo miden los que ya lo resolvieron (BFCL y τ-bench)

Investigado el 12-ago contra las fuentes. **No inventamos el test de orquestación: adoptamos
el diseño de BFCL y le sumamos lo nuestro.**

**Berkeley Function Calling Leaderboard** — el estándar de facto en tool calling:

| Práctica de BFCL | Qué resuelve de lo nuestro |
|---|---|
| **Objective checks, NO juez LLM.** *"Expert human labelers manually review all data points and label the ground truth"*, unit tests y `mypy` | Nuestras 4 suites agénticas las decide el juez (+0,99 en `tool_calling`), y ese juez satura |
| **State-based evaluation**: comparar *"the backend system's state after all function calls are executed"* | Mide si LOGRÓ la tarea, no si la contó bien. Mata el problema de la prosa |
| **Response-based con subset matching**: el camino ejecutado *"contains the ground truth as a subset, even if it contains additional function calls"*, para admitir *"different, equally valid trajectories"* y recuperación de errores | **Resuelve exactamente el caso Lightning vs Qwen**: uno actúa primero y el otro narra primero. Con subset matching, los dos pasan si llegan |
| **Multi-turn con límite de pasos**: termina cuando *"the model doesn't output any valid function calls"* o a los 20 pasos. Se evalúa al final de CADA turno y solo aprueba quien *"passes both checks in all turns"* | Nuestras suites son single-turn y penalizan al que actúa sin narrar |
| **Categoría dedicada a alucinación**: 240+ entradas, detecta llamadas innecesarias (ej. autenticar cuando ya estaba autenticado) | No medimos la herramienta llamada de más, solo la que falta |

**τ-bench (Sierra)** aporta la pieza que nos falta por otro lado: **`pass^k`** — correr la misma
tarea k veces y reportar con qué fiabilidad la resuelve. Es la respuesta directa a nuestro
**±0,58 de ruido con n=1**: en vez de subir `RUNS_PER_TEST` para achicar el error de una
media, se mide y se publica la **consistencia**, que para un agente que corre 24/7 es más
útil que el promedio.

**El diseño de la suite nueva, entonces:**

1. **Estado verificable al final**, no prosa. La tarea se logró o no.
2. **Subset matching** sobre la trayectoria: distintos caminos válidos aprueban igual.
3. **Multi-turn con tope de pasos** — la maquinaria de `multi_turn_script` ya existe.
4. **Sin juez.** Verificador determinista, como manda la doctrina del 13-jul.
5. **Llamadas de más también cuentan**: la categoría de alucinación de BFCL.
6. **`pass^k`** en vez de una media: qué tan seguido lo logra, no cuán lindo lo cuenta.

### 2.6 Los tres ejes publicados que hay que arreglar antes de re-medir

Detectado por `audit_suites.py` el 12-ago:

| Eje | Problema | Qué hacer |
|---|---|---|
| **`agentic_score`** | sale SOLO de `agent_long_horizon` (multi-turno sin herramientas) y correlaciona **−0,26** con el tool calling real. **Es el que alimenta la página "mejor LLM para agentes"** | Recomponerlo: multi-turno **+ tool calling real**. O renombrarlo a lo que mide |
| **`niah_score_avg`** | **poblado en 0 de 68** rankeados. Medimos 2.932 runs de long-context y el eje publicado no los usa | Computarlo desde los runs que ya existen |
| **La página de agentes** | usa `agentic_score`; el dato bueno (`tool_calling_score_avg`) **está poblado en los 68** y no se usa | Componer la recomendación con ambos |

**Re-medir antes de arreglar estos ejes sería pagar dos veces**: los runs nuevos alimentarían
un eje mal compuesto.

### 2.7 Punto ciego conocido del propio detector

`audit_suites.py` infiere la señal esperada de los tests. En suites con rúbrica determinista
—`agent_long_horizon`— no hay `content_score` ni `answer_score` que correlacionar y devuelve
`—` en vez de fallar ruidoso. **Queda anotado**: el detector no cubre las suites con rúbrica
propia, que hay que auditar a mano hasta que se le agregue el caso.

## 3. DECIDIDO (Cristian, 13-ago-2026): dos ejes publicados, no uno

> **Esta decisión está tomada. No volver a discutirla** — si aparece la duda otra vez,
> la respuesta y su evidencia están acá abajo.

**Qué se publica desde v4.1:**

| | Qué es | Rol |
|---|---|---|
| **Índice de calidad** | solo `quality_avg`, z-scoreado | **el titular**. Responde "¿qué modelo es mejor?" |
| **Frontera de Pareto** | los no dominados en calidad + precio + latencia | responde "¿cuáles vale la pena considerar?". **13 de 82** |
| **Calidad por dólar** | ratio `score_calidad ÷ $/1k` | responde "con el presupuesto como límite, ¿qué rinde más?" |
| Calculadora | sliders de peso + filtros, ya existe | la capa de personalización. **No se toca** |

Costo, velocidad y latencia se reportan **como columnas al lado del índice de calidad**,
nunca dentro de él.

### ⚠️ Corrección del 13-ago: NO se publica una segunda tabla de "mejor valor"

La primera versión de esta decisión ponía el compuesto 70/15/7,5/7,5 como segunda tabla.
**Cristian preguntó si no eran dos scores con el mismo resultado. Lo eran.** Medido:

| segundo eje candidato | r con el índice de calidad | ¿aporta? |
|---|---|---|
| compuesto 70/15/7,5/7,5 | **0,943** (r²=0,889) | no — 6 de 10 del top compartido, 2 modelos sin moverse |
| compuesto v2.9 60/20/10/10 | **0,882** | no |
| **frontera de Pareto** | deja fuera a **69 de 82** | **sí** |
| **calidad por dólar** (ratio) | **0,052** | **sí**, casi ortogonal |

**Todos los compuestos terminan igual, y la razón es estructural:** el costo z-scoreado
aporta ±0,30 al compuesto contra ±1,3 de la calidad. El precio no mueve el orden lo
suficiente como para contar otra cosa. Cualquier tabla que sea "calidad con un poco de
precio" es el ranking de calidad con otro título.

Lo que sí informa son las métricas que **no** son un promedio ponderado: un **descarte**
(la frontera) y un **ratio** (calidad/$). Por eso `build_quality_table` y el ranking de
pesos v2.9 salieron del output de MODELOS.md.

**Calidad por dólar va en el README, no solo en MODELOS.md** (Cristian, 13-ago: *"puede
ser de los que más sirvan a emprendedores"*). Es la pregunta que se hace alguien con el
presupuesto como límite duro — no "cuál es el mejor" sino "cuánto me rinde cada peso" — y
además destapa cosas que el ranking esconde: **Qwen 3.7 Flash sale #3 con calidad 8,89**,
o sea rinde por bueno *y* barato, mientras el resto del top rinde solo por barato.

`score_global` **se queda en el JSON** —es el peso por defecto de la calculadora, ahí sí
tiene sentido— pero **deja de publicarse como ranking**.

### La evidencia que cerró la discusión

Medido el 13-ago sobre los 82 rankeados:

1. **El compuesto ya es calidad en ~80%.** Descomponiendo la contribución (w·z) de cada
   dimensión: Luna 1,11 de 1,38 · Opus 5 −1,04 de −1,40. Costo aporta como máximo ±0,30.
   Si el ranking fuera **solo** calidad, la posición media se movería **6,8 puestos de 82**.
2. **Pero el 20% restante desplaza sistemáticamente**, y ahí está el engaño:

   | | calidad | publicado | Δ | precio |
   |---|---|---|---|---|
   | Claude Opus 4.6 | **#5** | #18 | −13 | $39,00/1k |
   | Kimi K3 | #44 | #67 | −23 | $23,40/1k |
   | Poolside Laguna XS 2.1 | #29 | **#7** | +22 | $0,20/1k |
   | Gemini 3.1 Flash Lite | #41 | #22 | +19 | $2,33/1k |

   Castiga caro, premia barato. **Las dos frases son verdad con etiqueta; ninguna lo es
   bajo un rótulo que dice `score_global`.**
3. En el top 10 las dos listas **comparten 7 modelos**. La diferencia son justo los caros
   — que es exactamente la información útil, no ruido.

### Por qué así y no de otra forma

- **Artificial Analysis** reporta costo y velocidad **aparte** del Intelligence Index. El
  CLAUDE.md ya dice que cuando nuestro motor difiere del estándar, la hipótesis por defecto
  es que nos equivocamos nosotros. Acá diferíamos.
- **No cuesta re-medir nada**: es agregación sobre el mismo dato. Y v4.1 ya es una frontera
  de comparabilidad declarada — el momento más barato, mismo argumento que el de no hacer
  un release intermedio.
- El post-mortem de julio ya había descrito el síntoma sin saber que tenía solución
  conocida: *"con la calidad apelotonada, el compuesto queda decidido por costo/velocidad →
  Opus 4.8 con calidad 8.28 cae a 6.86."*

### Lo que se descartó, y por qué

- **Más ejes** (calidad+velocidad, calidad sin latencia, etc.): fuera del sitio estático.
  Cinco tablas no las lee nadie y cada una es otra superficie donde caducan cifras. Ese
  caso ya lo resuelve la calculadora.
- **Multiplicar los 3 cortes × 2 ejes = 6 tablas**: no. Los 3 cortes (global /
  alternativas / open-source) son **filtros**; esto es un **eje**. Son ortogonales. Los 3
  cortes van sobre el índice de calidad, y **una sola** tabla de mejor valor.

### Advertencias que NO desaparecen con este cambio

- **No rescata a los Claude Opus.** Opus 5 es **#76 de 82 en calidad pura** (7,70).
  Verificado: no es el compuesto, no es el juez (4,26 contra una media de 4,38, dentro de
  rango), no es una suite rota — pierde repartido y gana en cuatro. El cambio de eje mejora
  la honestidad del titular, no ese resultado.
- **El juez casi no discrimina**: puntúa a los 82 rankeados entre **3,88 y 4,70** — 0,82
  puntos de rango en una escala de 10. O sea que `quality_avg` la está decidiendo el
  criterio automático, no el juez. Es un hallazgo aparte y merece su propia revisión.

### ⚠️ Secuencia obligatoria — recalibrar DESPUÉS, no antes

La referencia congelada guarda `mean`/`std` **de las dimensiones que componen el score**.
Si se recalibra ahora (§3.bis) y después se cambia la composición, hay que recalibrar dos
veces y la primera frontera no sirve para nada. **Orden correcto:**

1. Implementar los dos ejes en `export_for_pages.py` + generadores.
2. Recalibrar **una vez**, ya contra la definición nueva (`--recalibrate --scoring-version v4.1`).
3. Regenerar todo, auditar, taggear.

---

## 3.bis — BLOQUEANTE: el rescore dejó la referencia congelada obsoleta

**Estado: el rescore está hecho (10.503 runs, 13-ago 01:30) y NO se publicó a propósito.**
`docs/data/models.json` sigue siendo el de las 07:15. Decisión pendiente de Cristian.

### Qué pasó

Los 3 scorers huérfanos hacen lo que debían: donde antes había un `5.0` de relleno, ahora
hay una nota real. Efecto medido sobre **los mismos 68 modelos**:

| | media `quality_avg` | sd |
|---|---|---|
| referencia congelada v4.0 | 7,9246 | 0,2932 |
| los 68 antes del rescore | 7,926 | 0,296 |
| **los 68 después** | **8,114** | 0,283 |

**+0,187 de media = +0,64 desviaciones.** Como `score = 5,5 + 3,3·z` y calidad pesa 70%,
eso son **+1,48 puntos de inflación** para el modelo promedio. Observado: **65 de 68 se
movieron ≥0,3, y 64 hacia arriba** (de +0,38 a +2,17). GPT-5.6 Luna pasaría de 8,80 a
**9,77**.

No es que el ranking cambió: **la vara quedó corta**. La referencia v4.0 está calibrada
contra la escala vieja, en la que un tercio de los tests devolvía 5,0 fijo.

### Por qué no se arregla solo

Recalibrar es un **evento de versión deliberado** (`export_for_pages.py --recalibrate
--scoring-version vX.Y`) y estaba explícitamente fuera de alcance. Simulado sin escribir:
baja todo ~1 punto y **el orden se mantiene casi intacto** — confirma que la inflación es
uniforme, no un reordenamiento. Top 3 recalibrado: Luna 8,77 · Tencent Hy3 8,48 · Qwen 3.7
Flash 8,30.

### Las tres salidas

**→ ELEGIDA la 1 (Cristian, 13-ago). Con una condición de orden: se recalibra DESPUÉS de
implementar los dos ejes de §3, nunca antes — la referencia guarda mean/std de las
dimensiones que componen el score, así que recalibrar contra la composición vieja es
trabajo que se tira.**

1. **Recalibrar como parte de v4.1** (recomendada). La escala de calidad cambió de verdad,
   así que la referencia tiene que cambiar con ella. v4.1 ya es una frontera de
   comparabilidad declarada — meter esto ahí no agrega una ruptura, usa la que ya hay.
2. **Recalibrar ya como v4.0.1.** Publica antes, pero abre una frontera extra para
   cerrarla en semanas. Contradice la decisión de "una sola frontera".
3. **Publicar sin recalibrar.** Descartada: todo número absoluto quedaría inflado ~1,5
   puntos y el `check_consistency` empezaría a marcar los docs vivos.

### Ojo aparte: los Claude Opus quedan al fondo y NO es un bug

Opus 5 daría **#77 de 82** (2,19 recalibrado). Verificado suite por suite contra Luna y
Sonnet 5: pierde repartido en muchas suites y **gana en varias** (`sales_outreach` +2,22,
`prompt_injection_es` +1,80, `summarization` +1,37, `policy_adherence` +1,00). No hay una
suite rota. Lo que lo hunde es el compuesto: calidad 7,70 **bajo la media de 8,13**, coste
3,35 (de los más caros) y latencia 1,42 (35s). Tres de cuatro dimensiones en contra.

Es lo que el benchmark mide a propósito — valor para un emprendedor, no capacidad
absoluta — pero publicar «el insignia de Anthropic es penúltimo» **exige decirlo con esa
salvedad al lado**, o el titular miente por omisión. Al redactar el release: nombrar que
pierde por precio y latencia, no por incapacidad.

⚠️ La sensibilidad del compuesto es alta por construcción: la sd de calidad entre modelos
es **0,289** sobre una media de 8,13. Una diferencia de 0,4 en calidad = 1,4 sd = varios
puntos de score. Vale revisarlo en §3 junto con sacar costo/velocidad del índice.

---

## 3.ter — CANDIDATO v4.2: benchmarks de terceros como columnas complementarias

Idea de Cristian (13-ago): mostrar resultados de otros benchmarks —SWE-Bench Verified,
GPQA Diamond, HLE— para que se pueda comparar **en ejes que nosotros no medimos**.

**A favor:** es exactamente la doctrina del repo (*"no reinventamos la rueda; nuestro valor
está en QUÉ medimos"*). Coding agéntico y STEM complementan lo nuestro en vez de competir,
y refuerzan el diferenciador: nadie más mide en español contra casos de un emprendedor.

**Por qué NO en v4.1 — la trampa está en la fuente.** El disparador fue una tarjeta de
lanzamiento que decía *"HLE con Tools — Supera DeepSeek V4 Pro"*. Eso no es un resultado,
es **marketing del proveedor**: elige el scaffold, el subset y el best-of-n. Copiar esas
cifras a mano nos devuelve el problema que llevamos meses corrigiendo — números
hardcodeados que caducan solos y que nadie puede auditar.

**Diseño que sí funciona (a resolver antes de construir):**

1. **Solo de fuente consultable.** SWE-Bench y GPQA tienen leaderboards públicos; Artificial
   Analysis y Epoch publican datasets. Si se puede *fetchear*, se regenera y `check_consistency`
   lo protege. **Si hay que copiarlo a mano de una landing, no entra.**
2. **Sección aparte con etiqueta de origen**: "medido por nosotros" vs "reportado por
   terceros". Nunca en la misma columna, nunca sin fecha ni link a la fuente.
3. **Jamás dentro de `score_calidad`.** Mismo principio que aplicamos al costo el 13-ago: si
   mide otra cosa, va al lado, no adentro.

**Cobertura esperada, para no sorprenderse:** solo los insignia publican estos números. De 82
rankeados, probablemente ~20 tendrían dato. Una columna mayormente vacía es honesta, pero hay
que decidir si se muestra igual o solo en las fichas por modelo.

---

## 4. Lo que NO entra en v4.1

- **Los scorers huérfanos ya están** (`json_valid`, `json_exact`, `language_check`,
  12-ago). `rescore_all.py` **ya se aplicó** (13-ago): 10.503 runs. Destapó el bloqueante
  de §3.bis — sin publicar hasta decidir.
- **`else: return 5.0` → `raise`**: su propio commit, después del rescore validado.
- **`RUNS_PER_TEST`**: medido el ruido (±0,58 con n=1). Decisión de Cristian: próxima
  tanda, no ahora.
- **Rotación de prompts**: descartada (ver §0).
- **Migrar a lm-eval-harness**: descartado (ver §0).

---

## 5. Orden de ejecución

1. **Cerrar el lote de agosto** (11 modelos nuevos) — en curso
2. **`rescore_all.py`** con los 3 scorers → diff contra `baseline_20260812_pre_scorers.json`
   → explicar todo movimiento >0,3 → aplicar
3. **Implementar 2.1 + 2.2 + 2.3** (rama aparte, un cambio a la vez, `audit_anomalies.py`
   y `validate.py` como gate)
4. **Re-medir** lo que cambió de condiciones: suites de contenido (por `max_tokens`) + niah
   completo + `integridad_idioma`
5. **Medir cuánto se movería** sacando costo/velocidad del score → decidir §3
6. `export_for_pages.py --recalibrate --scoring-version v4.1` — el único recalibrado del
   año, sobre dataset completo
7. DATASHEET, CheatSheet, tag `v4.1.0`, `check_consistency.py` en verde

## 6. Criterio de cierre

v4.1 está listo cuando:

- Todo modelo rankeado rindió el **mismo examen en las mismas condiciones** (mismo
  `max_tokens`, mismo tratamiento del razonamiento, mismos prompts verificados por hash)
- `niah` se corre solo donde entra, con prompt canónico por celda
- Ningún run del ranking viene de una medición con condiciones distintas
- `validate.py`, `audit_anomalies.py` y `check_consistency.py` en verde
- El CHANGELOG dice **qué cambió de posición y por qué**, con el diff automático de
  `release_diff.py`
