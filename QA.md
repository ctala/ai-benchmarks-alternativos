<!-- doc: vigente | verificado: 2026-08-16 -->
# QA — cómo verificamos que no publicamos algo que la data no sostiene

> **Un comando.** `python benchmarks/qa.py`. Si pasa, se puede mergear.
> Antes de mergear corre solo: el hook `pre-push` lo dispara.

## Por qué existe este documento

El 16-ago-2026 Cristian encontró **tres fallos distintos en un día usando el sitio**, no
revisando código: el wizard le recomendaba un modelo que falla del todo en una de tres
tareas; la calculadora ponía #3 del pilar Agentes a uno que no tiene endpoint con
herramientas; y una página ordenaba por un criterio con correlación **negativa** contra la
realidad medida. Ninguno rompía nada — las páginas cargaban perfecto.

Su diagnóstico fue el correcto: *"No puede ser que todo siempre esté roto y no nos demos
cuenta"*. Y la causa raíz también la nombró él: *"tenemos solo una fuente de la verdad, la
idea es que todos usen la misma"*.

Porque no la teníamos. Medido ese día: **76 condicionales de filtrado en 25 archivos**
decidiendo a mano si un modelo se puede recomendar. Y se puede fechar por qué se
multiplicaron — cada regla nació de un fallo distinto y se aplicó **donde dolía ese día**:

| campo | nació | por qué |
|---|---|---|
| `score_by_pillar` | 25-abr-2026 | con la calculadora original |
| `retired` · `provider_variant` | 13-jul-2026 | Devstral Small llevaba meses **#5 con el endpoint apagado** |
| `sirve_para_agentes` | 14-ago-2026 | Hermes 4 405B: calidad 8,20 y **0,00** dentro de un agente |

Lo escrito antes no las tenía. Lo escrito después las copiaba del vecino que las tuviera a
mano. Y nada verificaba que estuvieran todas.

---

## La regla de oro

> **La elegibilidad se decide UNA vez, en el export, y se graba en el dato.**
> Ninguna superficie la recalcula: leen `m["elegible"]`.

`benchmarks/elegibilidad.py` es esa fuente. Da un veredicto en tres contextos, con motivo:

| contexto | qué significa | ejemplo de exclusión |
|---|---|---|
| `catalogo` | aparece en listados y datos | retirado: su endpoint ya no existe |
| `ranking` | compite por un puesto | examen a medias, muestra chica, `:free`, variante de esfuerzo |
| `agentico` | se puede recomendar para operar un agente | sin herramientas, o **sin evidencia** de haberlo hecho |

Los tres son distintos a propósito. Gemini 3.6 Flash es **#3 de 80 en calidad agéntica y
#76 en el índice general**: un flag binario no puede decir eso.

**Si estás por escribir `[m for m in models if not m["retired"] and ...]`, lo que buscabas
es `elegibilidad.filtrar(models, ctx)`.**

---

## Las seis áreas

`qa.py` agrupa por área para que no se pierda ninguna cuando se agregue algo nuevo:

| área | qué cubre | instrumento |
|---|---|---|
| **datos** | invariantes del dataset, funciones puras del núcleo | `test_unitarios.py` · `check_consistency.py` |
| **suites** | el registro de ejes es uno y todos tienen nombre humano | `check_suites.py` |
| **calculadora** | el `app.js` REAL contra los datos reales, **wizard incluido** | `qa_calculadora.mjs` · `check_calculator.py` |
| **paginas** | las 71 publicadas: ¿lo que dicen lo sostiene la data? | `auditar_paginas.py` · `check_cortes.py` · `check_claims.py` |
| **guardrails** | que cada guardrail falle cuando debe | `test_guardrails.py` · `check_caminos.py` |
| **version** | las 7 superficies + tag + CHANGELOG | `check_version.py` |

```bash
python benchmarks/qa.py                    # todo (~5 s)
python benchmarks/qa.py --rapido           # lo que corre en segundos
python benchmarks/qa.py --area calculadora
python benchmarks/qa.py --pre-merge        # solo lo bloqueante
```

### Bloqueante vs informativo

Un chequeo **bloqueante** que falla impide mergear. Uno **informativo** reporta deuda
conocida y no frena. Bloquear por deuda convierte al QA en algo que se saltea, y un QA que
se saltea no existe.

---

## Cuándo corre

| momento | qué |
|---|---|
| **antes de mergear** | `qa.py --pre-merge` — lo dispara el hook `pre-push` |
| al regenerar | `regenerate_all.py` corre los guardrails de datos y páginas |
| al agregar un modelo | `qa.py --area datos` verifica precio ≠ $0, no-`:free`, sin duplicados, umbral de runs |
| al tocar la calculadora | `qa.py --area calculadora` — 21 chequeos sobre el `app.js` real |
| al publicar versión | `qa.py --area version` — las 7 superficies |

Instalar el hook (una vez):

```bash
python benchmarks/instalar_hooks.py
```

---

## Las tres capas, y por qué hacen falta las tres

Cada una caza lo que las otras no ven. El bug del wizard lo prueba: `wizEje` leía
`tareas["harbor-cotizar"]` y nada más, así que juzgaba el trabajo agéntico con **una de
tres tareas, la más fácil**.

| capa | qué prueba | por qué no bastaba sola |
|---|---|---|
| **unitaria** (`test_unitarios.py`) | la función sola, con su caso borde | — |
| **funcional** (`qa_calculadora.mjs`) | el flujo real contra datos reales | el flujo funcionaba **perfecto, sobre el dato equivocado** |
| **de producto** (`auditar_paginas.py`) | lo publicado vs la data que lo sostiene | mira el resultado, no el camino |

Y una cuarta, que es la que hace que las otras tres valgan: **`test_guardrails.py` verifica
que cada guardrail FALLE cuando debe.** Un chequeo que nunca falla no es un chequeo.

---

## Cobertura

`python benchmarks/cobertura.py` mide el núcleo — los módulos que deciden lo que se
publica. **Piso: 80%.** Medido antes de escribir tests el 16-ago: **4%**. Hoy: **71%**,
con 120 tests unitarios y 21 funcionales.

Lo que falta para el piso está identificado y no es misterio: `export_harbor.recolectar()`
necesita `jobs/`, que está gitignored, y `simular_pilares.main()` corre el export dos veces
(minutos). Se cubren cuando haya una forma barata de fijar esas entradas — subir el número
sacándolos de la lista sería mover la portería, que es exactamente lo que este repo no hace.

**No se cuentan** los generadores de HTML completos: cubrir 900 líneas de f-strings sube el
porcentaje y no atrapa un fallo más. Lo que sí atrapa fallos ahí es `auditar_paginas.py`,
que mira el HTML **ya generado** y pregunta si la data lo sostiene.

---

## Al agregar algo nuevo

1. **¿Es una regla sobre qué se puede recomendar?** → va a `elegibilidad.py`, no a un `if`
   en tu generador.
2. **¿Es una superficie nueva?** → llega con su chequeo, **en el mismo commit**. Corolario
   de la regla de oro del repo: *una regla sin instrumento que la haga cumplir es una regla
   que ya se rompió*.
3. **¿Es un chequeo nuevo?** → se agrega a `CHEQUEOS` en `qa.py` con su área, y a
   `test_guardrails.py` con la prueba de que falla cuando debe.
4. **¿Es una función del núcleo?** → lleva su test unitario con el **caso borde real** que
   la motivó, no un ejemplo inventado. Así el test explica por qué la función es como es.

---

## Chequeos de FLUJO vs chequeos de PROMESA

> Cristian, tras el barrido del wizard: *"muchos de los errores que estás encontrando
> deberían haber sido capturados por QA. Para que mejoremos el proceso de validación."*

Tenía razón, y el patrón es de una sola clase. Los cinco chequeos que existían preguntaban
todos lo mismo:

| | preguntaba |
|---|---|
| W1 | ¿devuelve **algo**? |
| W2 | ¿**no** recomienda algo inválido? |
| W3 | ¿los ejes **existen**? |
| W4 | ¿el paso **aparece** cuando debe? |
| W5 | ¿la tabla **coincide** con el cálculo? |

**Los cinco verifican que el flujo no esté roto. Ninguno verificaba que la respuesta fuera
correcta.** Y los tres bugs del 17-ago los pasaron todos: el wizard devolvía una
recomendación válida, con ejes existentes, en el paso correcto y coherente con su propia
tabla — mientras **ignoraba el presupuesto en 12 de 32 combinaciones** y recomendaba algo
que costaba 4,7 veces lo declarado.

Es la misma distinción que el repo ya tiene escrita para los detectores de datos —*cazan
ausencia; la contaminación es presencia*— un nivel más arriba: **cazan «no funciona», no
cazan «funciona y está mal».**

### La regla que sale de ahí

> **Cada palabra de la interfaz es una promesa, y toda promesa necesita su verificador.**

No alcanza con probar el camino: hay que probar que la respuesta cumple lo que la pantalla
prometió. Literalmente lo que dice el texto:

| lo que la interfaz promete | el chequeo que lo hace cumplir |
|---|---|
| «~$5/mes · uso personal» | **W8** — lo recomendado cabe en ese presupuesto |
| «elegí cuánto vas a gastar» | **W7** — cambiarlo cambia la recomendación |
| «Chat en vivo · respuesta rápida» | **W6** — no recomienda nada que tarde >20 s |
| «Agentes / automatizar» | **W2** — nada que no corra dentro de un agente |
| «tipo de agente» | **W6** — usa las tareas medidas, todas |

### Cómo se agrega una pantalla nueva

1. **Escribí las promesas primero.** Cada opción, cada etiqueta, cada preset es una
   afirmación: «esto cuesta ~$5», «esto es rápido», «esto sirve para agentes».
2. **Una promesa sin verificador no se publica.** Es la regla de oro del repo aplicada a
   la interfaz: *una regla sin instrumento que la haga cumplir es una regla que ya se
   rompió.*
3. **Barré el espacio completo, no un caso.** Las 32 combinaciones del wizard son 32; el
   bug del presupuesto solo se ve comparando dos extremos, y el de la tarea agéntica solo
   se veía mirando las cuatro tareas juntas. Un caso de ejemplo habría pasado.
4. **El test usa la función real, nunca una copia.** Pasó dos veces en dos días: `APTOS`
   replicando `wizCandidatos` y el barrido replicando `wizResult`. Una réplica prueba la
   réplica — y peor: da verde mientras el código real está roto.
