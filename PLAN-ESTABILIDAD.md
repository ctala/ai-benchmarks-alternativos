<!-- doc: vigente | verificado: 2026-08-13 -->
# Plan de estabilidad — que dejemos de rehacer el benchmark todos los meses

> **Origen (13-ago-2026).** Cristian: *"Estoy super decepcionado de tener que rehacer todo,
> todos los meses."* Con razón. Este documento existe para que eso pare, y para no volver a
> discutirlo.

## 1. El diagnóstico, con los números de estos dos días

Lo primero es separar dos cosas que veníamos mezclando, y que explican casi toda la sensación
de inestabilidad:

| | ejemplos de esta sesión | costo |
|---|---|---|
| **Cambios de MEDICIÓN** | modelos nuevos, `max_tokens`, prompts, suites | **$78,82** |
| **Cambios de PRESENTACIÓN** | dos ejes, escala absoluta, sacar columnas, recalibrar, umbrales, OG, FAQ | **$0** |

Todo lo que se rehízo tres veces en dos días —el titular, la escala, las columnas— **fue
gratis**. Se regenera desde los runs que ya están en disco. Los $78 fueron medir 13 modelos
nuevos, que es el costo normal y útil del benchmark.

**El problema no es el dinero: es la rotación de decisiones.** Cambiamos de opinión sobre
cómo presentar, en público, tres veces. Eso desgasta aunque no cueste un peso, porque cada
vuelta obliga a revisar docs, blog, carrusel y calculadora.

## 2. Las tres reglas que lo cortan

### R1 — Presentación y medición se tratan distinto, siempre

- **Presentación** (composición del score, escala, columnas, etiquetas, orden): se puede
  cambiar cuando haga falta, **pero se simula ANTES contra los runs existentes**. Toda
  propuesta de scoring se puede probar en minutos sin gastar un centavo: los 29.000 runs ya
  están en disco. Si el cambio no mejora el diff simulado, no se hace.
- **Medición** (prompts, `max_tokens`, suites, criterios): **cambia una vez por trimestre**,
  en una versión declarada, y todo lo que rompe comparabilidad entra en ese mismo corte. Es
  la regla que ya inventamos para v4.1 sin nombrarla; acá queda escrita.

### R2 — Las suites se AGREGAN, no se reemplazan

Éste es el punto económico que hace viable mejorar sin rehacer:

```
suite nueva de  8 tests × 3 runs × 82 modelos = 1.968 runs ≈ $29
suite nueva de 12 tests × 3 runs × 82 modelos = 2.952 runs ≈ $43
```

Una suite nueva **no invalida nada de lo anterior**. No se re-mide el examen; se mide lo
nuevo y punto. Lo que invalida —y hay que evitar— es *editar* una suite existente: ahí sí
todos los runs viejos dejan de ser comparables.

**Corolario:** si una suite ya no sirve, **no se arregla: se jubila del score y se agrega
otra**. Jubilar es gratis.

### R3 — Ningún número publicado sin un instrumento que lo vigile

Ya está pasando (`check_consistency`, `check_calculator`, `validate`, `audit_*`, `canario`).
La regla es que **un guardrail nuevo acompaña a cada superficie nueva**, en el mismo commit.

## 3. Qué hacemos con las 5 suites saturadas — plan concreto

**Diagnóstico medido:** 5 de 28 suites tienen ≥60% de runs con 10,0 perfecto. No es rúbrica
blanda —todas usan scoring `verificable`, objetivo— es **techo de dificultad**: los modelos
las pasan.

| suite | perfectos | qué se hace | costo |
|---|---|---|---|
| `niah_es` | 91% | **recortar la grilla** (ver abajo) | **ahorra ~$40/lote** |
| `string_precision` | 96% | jubilar del score, queda como badge de "básicos" | $0 |
| `structured_output` | 78% | jubilar del score, queda como badge | $0 |
| `content_verificable` | 77% | mantener, está en el borde | $0 |
| `ocr_extraction` | 64% | mantener, está en el borde | $0 |

### `niah_es` es el caso que paga el plan entero

Hoy son **781 runs por lote** (20% del examen) con 91% de aprobación, y es la suite que hace
que medir un Claude Opus cueste $73. Contexto por contexto:

| contexto | % perfecto |
|---|---|
| 8K | 78% |
| 64K | 72% |
| 128K | 69% |
| **256K** | **41%** |
| **800K** | **45%** |

**Los tramos cortos ya no informan; los largos sí.** Recortar 8K/64K y quedarse con
128K+ mantiene toda la señal y **ahorra plata en cada lote futuro**.

⚠️ Antes de re-medir: **90 runs de 4K y 16K son needles v2 (`api_key_*`)**, los que se
reemplazaron el 2-jun porque medían negativa ante credenciales en vez de retrieval. Se
escaparon del archivado. Archivarlos es gratis y limpia la media.

### Las dos suites duras que se agregan (v4.2)

Se eligen por dónde el examen actual **sí** discrimina hoy, que es la señal de que ahí hay
dificultad real: `tool_calling` (0% perfectos, media 5,37) y `agent_capabilities` (5%, media
6,84). Ambas son agénticas — que además es el eje que le importa a quien va a poner el modelo
en Hermes o n8n.

1. **Tool calling adversarial** (~10 tests, ≈$36). Herramientas que se parecen entre sí,
   parámetros opcionales, casos donde la respuesta correcta es **no** llamar a ninguna
   herramienta. Categoría de alucinación de herramientas, tomada de BFCL.
2. **Retrieval con distractores** (~8 tests, ≈$29). Reemplaza lo que `niah_es` ya no mide:
   varios needles plausibles, uno correcto; y needles que exigen **combinar dos datos**
   separados en el corpus, no solo encontrarlos.

**Total v4.2: ~$65**, y no invalida ni un run de los que ya tenemos.

## 4. El calendario, para que deje de ser sorpresa

| cuándo | qué |
|---|---|
| **día 1 de cada mes** | release: modelos nuevos del mes + regeneración. Presentación **congelada**. |
| **una vez por trimestre** | ventana de cambios de medición (suites, prompts, límites). Se anuncia, se mide una vez. |
| **cuando haga falta** | correcciones de bug y guardrails. No tocan comparabilidad. |

**Las dos suites duras se miden AHORA (ago-2026)**, para que la base quede firme antes del
release de septiembre — decisión de Cristian, 13-ago. **Septiembre = modelos nuevos y nada
más** (los 23 detectados). La próxima ventana de medición queda libre para lo que aparezca.

## 5. Lo que FALTA cerrar — comprometido, con orden

> **Decisión de Cristian (13-ago):** se hace **después** de medir las dos suites nuevas y
> de actualizar el sitio. No antes: la base primero, el refinamiento después.

Cuatro riesgos quedaron **expuestos** al cierre de la sesión. Están acá para que no se
confundan con "ya está resuelto", y con el enfoque propuesto para cada uno:

### 5.1 Duplicidad entre documentos — el que más se parece a la frustración original

**Hoy no hay nada.** La dispersión de 34 docs en la raíz, con decisiones repartidas en 13,
se encontró **a mano**. Si mañana dos docs vuelven a decir lo mismo con distinta cifra,
nadie se entera hasta que alguien lo lea.

*Enfoque:* comparar los docs por similitud de contenido (shingles o TF-IDF sobre párrafos,
sin dependencias pesadas) y marcar pares con solapamiento alto. No para borrar
automáticamente — para **decidir cuál es la fuente y cuál se convierte en puntero**. Sale
como `check_duplicados.py`, en la familia de los otros guardrails.

*Señal de que funcionó:* que el primer reporte encuentre pares que hoy no sabemos que existen.

### 5.2 Un doc verificado pero igual equivocado

`check_docs.py` verifica que **alguien lo miró**, no que el contenido sea correcto. Es
honesto al respecto, pero es un techo real: la fecha se puede actualizar sin arreglar nada.

*Enfoque:* extender el chequeo de datos incrustados. Ya sabemos que **el patrón que pudre
un doc es la data pegada en la prosa** (`PROVEEDORES.md` con su lista de modelos de hace
113 días). Un chequeo que detecte nombres de modelo, precios y scores dentro de docs
curados —y exija que se enlacen en vez de copiarse— ataca la causa, no el síntoma.

### 5.3 Superficies nuevas sin guardrail

La regla R3 exige que cada superficie llegue con el suyo. **Nada lo verifica**: una página
creada mañana no está cubierta hasta que alguien lo note.

*Enfoque:* un inventario de superficies publicadas (docs vivos, páginas pSEO, calculadora,
OG, feeds) contra la lista de lo que cada guardrail cubre. Lo que quede sin cubrir, se
reporta.

### 5.4 Pérdida de trabajo si muere una sesión

Los commits automáticos durante los lotes de anoche fueron **ad-hoc** — un bloque que
agregué al script de estado, no un mecanismo del repo.

*Enfoque:* que el runner haga commit de sus resultados cada N tests, no que dependa de que
quien lo lanza se acuerde de armar el heartbeat. Es el mismo patrón del canario: la regla
existe, le falta el instrumento.

---

## 5.5 El eje que falta: tarea real end-to-end (dirección, no diseño)

**Origen (13-ago).** Cristian trajo dos observaciones de producción que el benchmark no
predecía: MiniMax M3 resolvió en 30 minutos lo que GPT-5.6 Terra no logró en un día, y al
cambiar Qwen 3.6 por Nemotron Omni en su Spark, Hermes "se siente más tonto —hace otras
cosas de las que le pido, no entiende bien la petición".

### Lo que ya sabemos, medido

1. **La señal existe y está enterrada.** Qwen le gana a Omni en `content_verificable`
   (+2,18) y `policy_adherence` (+0,96) — literalmente "hace lo que le pido" y "respeta la
   restricción". Omni le gana en `agent_long_horizon` (−1,41), que era **justo lo que
   publicábamos como `agentic_score`**.
2. **`agentic_score` era una etiqueta falsa.** Ninguno de los 12 tests de
   `agent_long_horizon` da herramientas: mide conversación multi-turno. Correlación con el
   tool calling real: **r = −0,230**, negativa. Renombrado a `multiturno_score`.
3. **Existe un eje de "adherencia a la instrucción"** (`policy_adherence` +
   `content_verificable`) que es **ortogonal al multi-turno (r = −0,02)** y predice la
   experiencia de Cristian en los dos casos. Hoy no se publica en ninguna parte.

### Lo que NO podemos resolver desde adentro

Todas nuestras métricas son proxies y **se contradicen entre sí**. Elegir cuál tiene razón
mirando solo nuestros datos es circular. Hace falta **verdad de terreno externa**.

### El camino: adoptar el harness, escribir las tareas

Decisión de Cristian: *"no reinventaría la rueda, cambiaría la tarea para algo de
emprendimiento, pero si alguien ya resolvió el test mucho mejor."*

**[Harbor](https://www.harborframework.com/)** — el harness de [Terminal-Bench
2.0](https://github.com/harbor-framework/terminal-bench-2) — es el candidato:

- **Task y scaffold desacoplados**: la misma tarea corre contra muchos agentes en igualdad
  de condiciones. Su formato ya se usó para adaptar **26 benchmarks preexistentes**.
- **Soporta los harnesses que importan**: Claude Code, Codex CLI, OpenHands, Mini-SWE-Agent.
- Mide **finalización de la tarea**, que es el único juicio end-to-end que vale.

**Lo que aportamos nosotros son las tareas**, y son las que nadie más escribe:

| tarea candidata | qué se verifica objetivamente |
|---|---|
| Integración con la API de MercadoLibre | ¿funciona? ¿maneja auth y paginación? |
| Flujo n8n vía su MCP | ¿usó los **nodos oficiales** o improvisó código? |

Métricas por corrida, todas objetivas: **lo logró / usó los componentes correctos /
iteraciones / tiempo / tokens de contexto / costo**.

⚠️ **Antes de construir nada**: correr el harness tal cual con una tarea suya, para ver si
el formato nos sirve. Adoptar mal cuesta más que no adoptar.

---

## 6. La prueba de si esto funcionó

Dentro de tres meses, la pregunta no es si el ranking mejoró: es **cuántas veces cambiamos
la presentación en público**. Si la respuesta es "una, en la ventana anunciada", funcionó.
