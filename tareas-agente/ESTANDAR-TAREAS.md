<!-- doc: vigente | verificado: 2026-08-14 -->
# Estándar para crear tareas agénticas

> **Este estándar NO es nuestro.** Es la [rúbrica de implementación de tareas de
> Terminal-Bench Science](https://github.com/harbor-framework/terminal-bench-science/blob/main/rubrics/task-implementation.toml)
> —25 criterios, del mismo Harbor que usamos— **adaptada de «ciencia» a «negocio»**, más
> las piezas de diseño de dominio de [τ²-bench](https://github.com/sierra-research/tau2-bench).
>
> La versión anterior de este documento tenía 18 reglas que yo había deducido de mis
> propios errores, una por una, pagando cada una. **Dos de los criterios de esta rúbrica
> describen exactamente los dos fallos que costaron correcciones el 14-ago** — estaban
> publicados desde antes. Es la Regla #10 del repo aplicada a nosotros mismos: *antes de
> construir un mecanismo de medición, buscar quién lo resolvió.*

**Lo que sigue siendo nuestro y no se adopta de nadie:** el dominio. Las tareas son la
operación real de un emprendedor hispanohablante —cotizar, facturar, procesar reuniones,
rutear modelos— con casos, cifras y español de verdad. Ese es el *QUÉ medimos*; el *CÓMO*
se adopta.

---

## Los 25 criterios

### Verificación y especificación

| # | Criterio | Qué exige, en nuestro contexto |
|---|---|---|
| 1 | **`verifiable`** | El verificador es determinista, fiable y rápido, sobre salidas concretas y chequeables. |
| 2 | **`well_specified`** | **La consigna describe COMPLETAMENTE lo que los tests verifican**, sin ambigüedad. |
| 3 | **`functional_verification`** | Los tests verifican **comportamiento por ejecución**, NO coincidencia de palabras en el texto. |

> ⚠️ **El criterio 3 es el que más nos costó.** El 14-ago hice coincidencia de subcadenas
> dos veces y las dos dieron **falsos negativos contra respuestas correctas**: prohibí
> mencionar «12.000» cuando la mejor redacción dice *«14.000 (se corrigió el 12.000
> inicial)»*, y busqué «se cobra aparte» dentro de *«¿se cobra aparte, se incluye, o se
> avisa?»*, que es la pregunta abierta. Se verifica el **dato**, nunca la redacción.

> ⚠️ **El criterio 2 lo violan nuestras tareas hoy.** `harbor-reunion` tiene **13 tests y
> una consigna de 93 palabras**: los tests verifican reglas que la consigna nunca enuncia.
> **La solución la da τ-bench: un documento de POLÍTICA que el agente sí recibe.**
> Oculto ≠ no especificado — las *reglas* van escritas, las *situaciones* van escondidas
> en los datos. `harbor-ruteo` ya lo hace (`politica.md`); `harbor-reunion` no.

### Dificultad y mérito

| # | Criterio | Qué exige |
|---|---|---|
| 4 | **`difficult`** | Debe desafiar a alguien con experiencia en el oficio. |
| 5 | **`realistically_grounded`** *(era `scientifically_grounded`)* | Sale de un flujo de trabajo real, no de un ejercicio de manual. |
| 6 | **`novel`** | No se resuelve de memoria del corpus de entrenamiento. |
| 7 | **`essential_difficulty`** | **La dificultad viene del razonamiento del negocio, NO de minucias de formato.** |

> ⚠️ **El criterio 7 reprueba a `harbor-ruteo` tal como está.** En su sub-segmento, los 4
> modelos que entregaron sacaron **11 de 11 en las decisiones de ruteo**; los 2 que
> fallaron lo hicieron por **sintaxis JSON y un script Python con las comillas mal
> cerradas**. Toda la dificultad quedó en la mecánica. Hay que rediseñarlo.

### Solución y calidad de la verificación

| # | Criterio | Qué exige |
|---|---|---|
| 8 | **`solvable`** | Existe una solución que pasa TODOS los tests. |
| 9 | **`solution_quality`** | La solución **computa**, no trae la respuesta pegada. |
| 10 | **`deterministic_reproducible`** | Mismo resultado entre corridas; sin servicios externos vivos. |
| 11 | **`anti_cheat_robustness`** | Los tests resisten atajos; la respuesta no está en un archivo accesible. |

### Diseño de la tarea

| # | Criterio | Qué exige |
|---|---|---|
| 12 | **`agentic`** | Requiere varios pasos reales; no se resuelve con una sola llamada. |
| 13 | **`outcome_verified`** | Se califica el **resultado**, nunca el proceso ni qué herramienta usó. |
| 14 | **`scope`** | Cae dentro del dominio declarado: **la operación de un negocio chico**. |
| 15 | **`test_instruction_alignment`** | Mapeo **1:1** entre lo que la consigna pide y lo que cada test afirma. |

> El criterio 13 es lo que hace la tarea **independiente del harness**: se verifica el
> artefacto, nunca el camino. Un test que premie «usó tal herramienta» mide n8n, no al
> modelo — y quien use Claude Code, opencode, Hermes u OpenClaw se queda sin respuesta.

### Documentación y claridad

| # | Criterio | Qué exige |
|---|---|---|
| 16 | **`instruction_clarity`** | Prosa mínima, orientada al resultado, rutas absolutas, **sin pistas de la solución**. |
| 17 | **`structured_data_schema`** | El esquema exacto de toda salida estructurada, documentado. |
| 18 | **`verification_explanation_quality`** | Explica cómo verifican los tests y **justifica cada tolerancia con datos**. |
| 19 | **`difficulty_explanation_quality`** | El desafío central se entiende sin ser del rubro. |

> El 18 es el que me hizo recalibrar la tolerancia de J-06: con 1,5× el test era «¿elegiste
> exactamente el más barato?» y castigaba US$ 9 al mes; el error real que debe cazar
> cuesta 8× a 38×. La tolerancia se justifica con la tabla a la vista, no a ojo.

### Implementación

| # | Criterio | Qué exige |
|---|---|---|
| 20 | **`task_security`** | Sin código malicioso, exfiltración de credenciales ni escape del contenedor. |
| 21 | **`environment_hygiene`** | **La imagen Docker NO incluye `tests/` ni `solution/`**; deps de test en `test.sh`. |
| 22 | **`separate_verifier_configured`** | El verificador tiene lo que necesita; los assets duplicados coinciden byte a byte. |
| 23 | **`no_extraneous_files`** | Solo los archivos requeridos. |
| 24 | **`typos`** | Sin erratas en rutas, comandos ni variables. |

### Metadatos y revisión

| # | Criterio | Qué exige |
|---|---|---|
| 25 | **`expert_time_estimate`** | Cuánto tardaría alguien del oficio **con foco perfecto**. Calibra dificultad y timeouts. |
| — | **`reviewable`** | Alguien de afuera puede verificar que está bien; **los valores esperados se DERIVAN**. |

---

## Lo que se adopta de τ²-bench (diseño de dominio)

| Pieza | Qué es | Estado acá |
|---|---|---|
| **Documento de política** | Las reglas, entregadas al agente | ✅ `harbor-ruteo` · ❌ falta en las otras 3 |
| **Verificación por estado final** | Se compara el estado resultante contra el de una trayectoria de referencia | ❌ hoy usamos aserciones campo por campo |
| **Usuario simulado** | El agente debe **preguntar** lo que falta | ❌ sin implementar |
| **`reward_basis` como PRODUCTO** | Todos los componentes deben pasar, no una fracción | ❌ hoy damos reward parcial |
| **`pass^k`** | Fiabilidad sobre k intentos, no el promedio | ✅ 3 intentos, se publica el **piso** |

**Sobre el reward parcial vs producto:** el nuestro es más informativo para diagnosticar
(sabés *qué* falló), el de ellos es más honesto para decidir (una factura mal emitida está
mal, no «al 80%»). La decisión: **se conserva el parcial para el diagnóstico y se publica
también el binario** — cuántos resolvieron la tarea ENTERA. Un modelo con 0,92 en facturar
no facturó bien.

---

## Qué medir: eso sí es nuestro

La rúbrica dice **cómo** construir una tarea. **Qué** tarea construir sale de la operación
real de un emprendedor hispanohablante — hoy: cotizar, facturar, procesar reuniones,
rutear modelos. La lista viva de casos está en `RESULTADOS.md`.

`validar_tarea.py` verifica lo automatizable de esta rúbrica. **Lo que ningún script puede
verificar es el criterio 5** —que valga la pena medirlo— y eso sigue siendo una
conversación, no un chequeo.

---

## Deuda conocida contra este estándar

Declarada a propósito, para que no se confunda «hay estándar» con «cumplimos»:

| Tarea | Criterio | Estado |
|---|---|---|
| `harbor-reunion` | 2 · `well_specified` | ✅ **resuelto 14-ago** — `politica.md` con 9 reglas |
| `harbor-ruteo` | 7 · `essential_difficulty` | ✅ **resuelto 14-ago** — el artefacto lo produce `asignar.py` |
| `harbor-cotizar` · `harbor-facturacion` | 7 · `essential_difficulty` | ⚠️ siguen pidiendo JSON a mano |
| las 4 | τ · verificación por estado final | ❌ aserciones campo por campo |
| las 4 | τ · usuario simulado | ❌ ninguna obliga a preguntar |
| `harbor-cotizar` | 18 · justificar tolerancias | ⚠️ 7 tests sin consecuencia declarada |

**Sobre el chequeo de C2:** cuenta líneas con forma de norma y **avisa**, no falla, salvo
que no haya ninguna. Se intentó automatizar mejor cuatro veces —por nombre de archivo, por
verbos, ampliando el patrón— y cada versión dejaba otra forma afuera. Un script puede
decir *«acá hay 2 líneas normativas para 13 tests, miralo»*; no puede decir *«las reglas
están completas»*. Fingir lo segundo daría confianza falsa.
