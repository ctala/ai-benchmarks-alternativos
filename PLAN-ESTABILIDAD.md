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

Septiembre = release normal (los 23 modelos detectados). **v4.2 = ventana de octubre.**

## 5. La prueba de si esto funcionó

Dentro de tres meses, la pregunta no es si el ranking mejoró: es **cuántas veces cambiamos
la presentación en público**. Si la respuesta es "una, en la ventana anunciada", funcionó.
