<!-- doc: vigente | verificado: 2026-08-14 -->
# Resultados de las tareas agénticas — Harbor

**Setup:** `harbor run -p tareas-agente/<tarea> -a mini-swe-agent -m openrouter/<modelo>`,
3 intentos por modelo, en Docker, con herramientas reales. Reward = fracción de tests
pasados, parcial por diseño.

**Los datos versionados están en [`resultados.json`](resultados.json)** — generado por
`benchmarks/export_harbor.py` desde `jobs/`, que está gitignored. Este documento es la
lectura; el JSON es la fuente.

---

# Tarea 1 — cotizar un encargo (fácil)

**74 modelos · 231 corridas · US$ 2,66 · media global 0,899**

Un cliente pide por correo una implementación con cuatro trampas: un servicio que absorbe
a otro (cobrar los dos son US$ 2.370 de más), un diagnóstico que ya tiene hecho, una
migración sin descuento y una certificación ISO 27001 **que no está en el tarifario** y va
a cotización humana.

| resultado | modelos |
|---|---|
| perfecto en los 3 intentos | **48** |
| parcial (0,44 – 0,97) | **21** |
| **cero** | **5** |

*(2 corridas se descartaron por venir de una versión anterior de la tarea — distinto
`task_checksum`, distinto examen. El extractor lo hace solo.)*

## Un 0,00 no siempre significa lo mismo

Es la distinción que más importa de todo este documento, y la que se publica como
`estado` en lugar de dejar que la media la esconda:

| estado | qué pasó | ¿culpa del modelo? |
|---|---|---|
| `sin_herramientas` | **no existe endpoint con tool use.** Nunca vio el encargo | no como razonador — pero es inusable igual |
| `rompe_bucle` | tiene herramientas y **no sostiene el formato** de tool call | sí |
| `hizo_mal_la_tarea` | corrió, entregó, y lo entregado está mal | sí |

La causa no se escribe a mano: se deriva de la traza con firmas explícitas
(`export_harbor.py:FIRMAS`). Ya publiqué una vez un 0,0 que era del harness.

## Los 5 que no pueden

| modelo | calidad publicada | estado |
|---|---|---|
| `nousresearch/hermes-4-405b` | **8,20** | `sin_herramientas` |
| `meta-llama/llama-4-maverick` | 7,88 | `rompe_bucle` |
| `nousresearch/hermes-4-70b` | 7,70 | `sin_herramientas` |
| `qwen/qwen3-next-80b-a3b-thinking` | 7,49 | `rompe_bucle` |
| `meta-llama/llama-3.1-8b-instruct` | 7,10 | `rompe_bucle` |

**Hermes 4 405B tiene mejor índice de calidad que 40 de los modelos que resolvieron la
tarea.** Y no puede ejecutarla. Ese contraste es la razón de que la dimensión agéntica se
publique aparte y nunca dentro del índice de calidad.

> **Verificado el 14-ago con la fuente primaria:** no es un problema de ruteo. La
> documentación de **Nous Research** dice que Hermes 4 *"no está recomendado para usar
> dentro de Hermes Agent… está afinado para chat y razonamiento, no para el bucle rápido
> de tool-calling del que depende el agente"*. Para trabajo agéntico ellos mismos
> recomiendan otros modelos. No es que no lo pudimos medir: **su creador dice que es la
> herramienta equivocada.**

### El hallazgo más accionable del lote

| variante | reward |
|---|---|
| `qwen3-next-80b-a3b-**instruct**` | **0,81** |
| `qwen3-next-80b-a3b-**thinking**` | **0,00** |

Mismo modelo, mismo tamaño, mismo proveedor. **La variante que razona no sostiene el bucle
de herramientas.** Si estás eligiendo entre las dos para un agente, esa es toda la decisión
— y ningún índice de calidad te la iba a dar (7,93 vs 7,49, casi empatados).

## La cola — donde la tarea todavía discrimina

| modelo | calidad | reward | piso | estado |
|---|---|---|---|---|
| `openai/gpt-oss-20b` | 7,78 | 0,56 | **0,00** | `inestable` |
| `mistralai/mistral-small-2603` | 7,97 | 0,78 | 0,67 | parcial |
| `mistralai/ministral-14b-2512` | 8,13 | 0,78 | 0,67 | parcial |
| `qwen/qwen3-next-80b-a3b-instruct` | 7,93 | 0,81 | 0,67 | parcial |
| `deepseek/deepseek-chat` | 8,05 | 0,81 | **0,44** | parcial |
| `qwen/qwen3-coder` | 7,74 | 0,83 | 0,67 | parcial |
| `google/gemini-2.5-pro` | 7,65 | 0,85 | 0,78 | parcial |
| `x-ai/grok-4.20` | 7,66 | 0,85 | 0,78 | parcial |

**El piso importa más que la media.** `deepseek-chat` promedia 0,81 —parece decente— pero
tuvo una corrida en 0,44. Para trabajo desatendido eso es peor que un 0,78 constante: no
sabés cuál de las tres facturas va a salir mal.

## Qué NO mide esta tarea, y hay que decirlo

**48 de 74 sacan perfecto: la tarea está saturada en la cabeza.** Sirve como **piso de
usabilidad** —"¿este modelo puede operar dentro de un agente?"— y no para ordenar el top.

Y hay un límite de diseño que conviene ser explícito: los tests verifican **lo que las
reglas obligan** (qué se cobra, qué no, que el precio de referencia sea el del tarifario,
que el ajuste caiga dentro de la banda 0,85-2,00, que el total cuadre, que todo ajuste
esté justificado). La regla 2 dice que el recargo por urgencia *"se puede"* aplicar, no que
se deba — así que **factor 1,0 es una respuesta legítima** y no se penaliza.

Consecuencia medida: para el mismo encargo, con el mismo tarifario, los modelos cotizaron
entre **US$ 8.530 y 17.060** y todo eso es defendible. La dispersión no es un error de los
modelos: es una decisión comercial que el dueño del negocio no delegó explícitamente.

---

# Tarea 2 — cierre de facturación (media)

**Sub-segmento de 3 modelos.** Cada test corresponde a **plata real mal cobrada**. La
respuesta ingenua —sumar todo lo registrado sin mirar contratos ni duplicados— factura
**US$ 6.774,50 cuando corresponden 5.629,50: un 20% de más.**

| error | costo |
|---|---|
| Contar la línea duplicada del registro de horas | **+US$ 235** al cliente |
| Ignorar el tope contractual de 40 h | **+US$ 210** e incumplimiento |
| Facturar al cliente con contrato vencido | **+US$ 700** sin contrato vigente |

| modelo | reward | qué falló |
|---|---|---|
| `z-ai/glm-5` | **0,75** | el duplicado · el total |
| `qwen/qwen3-coder` | 0,62 | el duplicado · el total · no dejó constancia |
| `mistralai/ministral-14b-2512` | 0,62 | el duplicado · el total · no dejó constancia |

**Ninguno saca perfecto**, y GLM-5 —que acierta 3 de 3 en cotizar— baja a 0,75. La tarea
media separa donde la fácil satura.

## El hallazgo

**Los tres fallaron el MISMO test: no vieron la línea duplicada.** Los tres le habrían
cobrado US$ 235 de más al cliente.

Y lo que sí pasaron dice tanto como lo que fallaron: **los tres respetaron el tope
contractual y ninguno facturó al contrato vencido.** O sea que leyeron los contratos. Lo
que no hicieron fue **desconfiar de los datos**.

> Los modelos leen las reglas. Lo que no hacen es dudar de los datos.
> Un duplicado en una planilla —el error más común de cualquier operación— pasa derecho a
> la factura del cliente.

Segundo hallazgo: **dos de tres tampoco dejaron constancia** de lo que requería decisión
humana (el tope excedido, el contrato vencido). Ajustaron en silencio. Un asistente que
corrige solo y no avisa es peor que uno que se equivoca ruidosamente.

**Pendiente:** correr las 74 contra esta tarea (~US$ 3-4 estimados).

---

# Tarea 3 — procesar una reunión de socios (media)

**68 modelos · 204 corridas · US$ 2,28 · media global 0,966**

El input no son datos limpios: es una **conversación**, con el ruido de una conversación
real. Alguien se corrige, algo se propone y se descarta, algo se da por cerrado y no lo
está. El artefacto es el **tablero de tareas actualizado**, no un resumen.

| resultado | modelos |
|---|---|
| perfecto en los 3 intentos | **49** |
| parcial | 16 |
| inestable (piso 0,00) | **3** |

*(12 corridas se descartaron solas por `task_checksum` distinto: son del sub-segmento
previo al arreglo del verificador. La disciplina de R17 funcionando sin que nadie la
recuerde.)*

## ⚠️ Esta tarea SATURA, y hay que decirlo

**49 de 68 sacan perfecto (72%).** Por R12, eso la convierte en un **piso de usabilidad**
—"¿este modelo puede procesar una reunión sin romper nada?"— y **no** en un ranking. No
sirve para ordenar la cabeza.

Parte de la saturación es culpa mía: la primera versión del verificador tenía un falso
negativo que penalizaba respuestas correctas. Al arreglarlo, subieron todos. El número
honesto es éste, no el inflado.

## El hallazgo: 14 modelos inventaron un acuerdo que nadie tomó

En la reunión, los socios discuten qué hacer cuando el técnico encuentra una falla no
prevista. Ninguno lo tiene claro. Acuerdan **anotarlo como pendiente, sin respuesta**.

**14 de 68 modelos escribieron una política igual.** Es el fallo más frecuente del lote
—16 corridas, más del doble que el segundo— y no discrimina por calidad: la lista va
desde 8,43 hasta 7,66.

| modelo | calidad |
|---|---|
| `deepseek/deepseek-r1` | 8,43 |
| `google/gemma-4-26b-a4b-it` | 8,28 |
| `openai/gpt-5.6-terra` | 8,21 |
| `meta/muse-glimmer-30b` | 8,14 |
| `deepseek/deepseek-v4-flash` | 8,10 |
| …y 9 más | |

> El tablero queda afirmando una política que los socios nunca acordaron, y que alguien
> va a ejecutar creyendo que se decidió. A diferencia de una factura mal emitida, **de
> esto nadie se entera**: el resumen se ve perfectamente razonable.

## Los otros modos de fallo

| trampa | corridas | modelos |
|---|---|---|
| Inventar la decisión que nadie tomó | 16 | **14** |
| No cerrar el precio que SÍ se decidió | 9 | 6 |
| Cerrar el checkout que sigue abierto | 7 | 4 |
| Crear la tarea de la app que se descartó | 7 | 5 |
| No anotar la decisión pendiente | 7 | 4 |
| Entregar un artefacto inválido | 6 | 4 |
| Quedarse con el precio viejo (12.000) | 6 | 4 |

**Todas las trampas cazaron a alguien.** Ninguna quedó decorativa.

## La cola

| modelo | media | piso | causa del cero |
|---|---|---|---|
| `meta-llama/llama-4-scout` | **0,00** | 0,00 | `hizo_mal_la_tarea` — 3 de 3 |
| `x-ai/grok-4.20` | 0,67 | **0,00** | `rompe_bucle` |
| `meta-llama/llama-3.3-70b-instruct` | 0,62 | **0,00** | `hizo_mal_la_tarea` |

**Verificado que ninguno es culpa del harness** (lo pidió Cristian: *"revisa si los
inestables son culpa nuestra, en especial por la evidencia de llama 4 scout"*). Los cinco
ceros del lote se clasificaron leyendo la traza:

- **`llama-4-scout`, 3 de 3.** Su último paso literal fue
  `cp /app/tablero.json /app/tablero_actualizado.json`: intentó editar el archivo de
  **entrada** en el lugar, lo corrompió, y copió el resultado roto. Ese mismo modelo saca
  **1,00 en cotizar**, así que no es incapacidad general — es que acá eligió una
  estrategia que se rompe sola.
- **`grok-4.20`.** Respondió sin tool calls hasta que el harness lo cortó
  (`RepeatedFormatError`). Las otras dos corridas fueron perfectas.
- **`llama-3.3-70b`.** JSON malformado en una corrida; las otras dos, 1,00 y 0,85.

**Y la pregunta destapó un fallo en el instrumento**, no en los modelos: `inestable` era
una etiqueta sin diagnóstico. Grok promedia 0,67 porque **rompe el bucle**; llama-3.3-70b
promedia 0,62 porque **escribe JSON inválido**. Misma etiqueta, causas opuestas, y solo
una de las dos se arregla con una instrucción mejor. Ahora `resultados.json` guarda
`causas_de_los_ceros` para todo modelo que tenga alguna corrida en cero, aunque promedie
bien.

---

## Lo que costó, y por qué eso cambia el plan

| | costo |
|---|---|
| Lote agéntico completo (74 modelos × 3) | **US$ 2,66** |
| Una suite del runner (91 tests × 70 modelos) | US$ 29-43 |

Un escalón agéntico entero sale **diez veces menos** que una suite tradicional, porque son
3 corridas por modelo en vez de 91. Eso invierte la economía: **construir tareas nuevas es
barato; el costo real es diseñarlas bien.**
