<!-- doc: vigente | verificado: 2026-08-13 -->
# Post-mortem — la primera corrida de la tarea agéntica

**Qué pasó:** 60 corridas, 6 modelos, **$0,47**. Barato por suerte. Antes de llegar al
resultado hubo que relanzar el lote **tres veces** por bugs míos, y los tres estaban ya
resueltos en el repo.

## La causa raíz, en una línea

**Escribí `correr.py` como camino paralelo al runner del repo.** Al hacerlo perdí todos
los guardrails de golpe:

    menciones al canario en correr.py: 0

| El pozo que pisé | Dónde ya estaba tapado |
|---|---|
| `max_tokens=1500` → los 6 modelos devolvieron `content=""` | `THINKING_MIN_TOKENS=8192` en `providers/adapters.py`, desde abril |
| El verificador dio **7/17 a una respuesta vacía** | el runner distingue **tres estados** de vacío desde julio |
| Corrí los modelos **en secuencia** (~75 min en vez de ~12) | **Regla 0** del RUNBOOK, con nombre y apellido |
| **Sin canario** | el gate que se agregó a `runner.py` ese mismo día |

El segundo es el más grave: **un scorer que premia el silencio**. Tres modelos empataron
en 7,0 con varianza cero — la señal de instrumento que este repo ya sabe leer— y si no se
hubiera mirado, el ranking entero habría sido mentira.

> **La lección de ayer, aplicada a mí:** una regla sin instrumento se rompe. Y **un
> instrumento que se puede esquivar escribiendo un script nuevo, se esquiva.**

## Lo que sí encontró la corrida (y vale la pena)

| modelo | media | rango | perfectas | calidad publicada |
|---|---|---|---|---|
| **GPT-5.6 Luna** | **13,9** | **12-17** | 3/10 | 8,43 (#2) |
| GLM-5.1 | 12,2 | 6-17 | 2/10 | 8,26 |
| DeepSeek V4 Flash | 10,6 | 4-12 | 0/10 | 8,10 |
| Qwen 3.5 397B | 10,3 | 0-17 | 1/10 | 7,94 |
| Laguna S 2.1 | 10,0 | 0-14 | 0/10 | 7,78 |
| **Tencent Hy3** | 9,8 | 9-14 | 0/10 | **8,53 (#1)** |

1. **El índice de calidad NO predice esta tarea.** El #1 publicado sale último.
2. **Lo que separa es el piso, no la media.** Luna nunca baja de 12; GLM cae a 6. Para
   trabajo desatendido el piso es la métrica.
3. **Ninguno es apto para facturar solo.** El mejor acierta 3 de 10.
4. **Laguna S 2.1 quemó los 64.000 tokens razonando y devolvió CERO caracteres.** No es
   truncamiento: nunca empezó la respuesta. Subir el techo no lo arregla — usa más. Un
   modelo que a veces consume 64k y no devuelve nada es peligroso **y** caro.

## Qué hacer para que el test agéntico sirva para decidir

### 1. Matar `correr.py`. La tarea agéntica va DENTRO del runner

No como script aparte. Integrada, hereda gratis: el gate del canario, el presupuesto de
los thinking models, los tres estados de respuesta vacía, la paralelización, el resume
idempotente y `calculate_costs --gastado`.

**Es la única forma de que no vuelva a pasar**: mientras exista un camino alternativo,
alguien (yo) lo va a usar.

### 2. El resultado tiene que ser una decisión, no un puntaje

Hoy sale "Luna 13,9 / Hy3 9,8". Eso no responde *"¿cuál pongo en mi agente?"*. Debería
salir en tres cubetas:

| | criterio |
|---|---|
| **Desatendido** | piso ≥ 15/17 en 10 corridas |
| **Con revisión humana** | media ≥ 12 pero piso < 15 |
| **No usar** | algún 0, o piso < 9 |

Con los datos de hoy: **nadie califica para desatendido**, Luna y GLM entran en "con
revisión", y Laguna queda fuera por el cero.

### 3. Falta más de una tarea

Una tarea mide una cosa. Están diseñadas `cierre-facturacion` (7 capas) y `facturar-como-
siempre` (ambigüedad de cliente); falta correrlas. Un modelo bueno cotizando puede ser
malo diagnosticando.

### 4. Y la señal más barata que no usamos: el canario

Correr **1 modelo × 1 corrida** antes del lote habría mostrado la respuesta vacía en 30
segundos y $0,01. Los tres relanzamientos se evitaban con eso.
