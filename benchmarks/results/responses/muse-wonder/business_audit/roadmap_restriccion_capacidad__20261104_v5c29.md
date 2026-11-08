# Muse Wonder — business_audit/roadmap_restriccion_capacidad

- model_id: `meta/muse-wonder`
- success: True  | final: 6.74 | quality: 8.0
- latency_total: 24.301s | tokens_per_second: 88.4
- input_tokens: 265 | output_tokens: 2147

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres jefe de producto de una empresa de una sola persona. Priorizas con la capacidad real del equipo, no con la ideal.

**user:**

Soy fundador solo. Tengo 6 horas al día de trabajo enfocado y ya gasto 2 de esas 6 en soporte y operación diaria que no puedo delegar todavía. Me quedan ~4h/día reales para construir. Quedan 8 semanas hasta el cierre del trimestre.

Tengo cuatro iniciativas y quiero saber qué hago:

A) Reescribir la plataforma en otro framework. Impacto estimado: alto (velocidad y todo lo futuro). Esfuerzo: ~3 meses a tiempo completo.
B) Arreglar el flujo de alta, que hoy pierde al 60% de la gente en el paso 2. Impacto: alto. Esfuerzo: ~1 semana.
C) Añadir un panel de métricas para mis clientes. Impacto: medio. Esfuerzo: ~3 semanas. Depende de que A esté terminado.
D) Grabar 10 videos de contenido. Impacto: medio. Esfuerzo: ~2 semanas.

Ordename el trimestre.


## Respuesta completa

Como fundador solo, tu capacidad no es 8 semanas. Es esto:

**4h/día de construcción x 5 días x 8 semanas = 160 horas reales.**

Y los esfuerzos que me das están estimados "a tiempo completo". Traducidos a tu ritmo de 20h/semana para construir, se duplican en calendario:

- **A) Reescritura:** ~3 meses = ~24 semanas reales para ti. Más de 2 trimestres.
- **B) Flujo de alta:** ~1 semana = ~2 semanas reales
- **C) Panel de métricas:** ~3 semanas = ~6 semanas reales, *después* de A
- **D) 10 videos:** ~2 semanas = ~4 semanas reales

Con esa cuenta, el trimestre se ordena solo.

### El orden de este trimestre

**1. B - Arreglar el alta. Semanas 1-2.**
Es lo único que tienes que hacer sí o sí.

Impacto alto, esfuerzo mínimo, valor en días. Hoy pierdes al 60% en el paso 2. Si solo recuperas a una parte de esa gente, eso es más usuarios, más ingresos y más feedback sin construir nada nuevo. Todo lo demás que hagas después vale más si entra más gente por la puerta.

Semana 1: arreglarlo y lanzarlo.
Semana 2: medir, corregir fricciones y dejarlo estable.

**2. D - Videos de contenido. Semanas 3-6.**
Impacto medio, esfuerzo medio, pero es independiente, de bajo riesgo y lo puedes terminar.

No lo haría perfecto. Graba en bloques, 2-3 videos por semana, publica y fuera. Es el único otro proyecto de la lista que cabe entero en el trimestre y te deja un activo que sigue trabajando mientras tú haces soporte.

**3. Nada nuevo. Semanas 7-8 de colchón e iteración.**
No las rellenes ahora. Eres una persona, habrá soporte extra, bugs de B y cansancio.

Usa esas 2 semanas para: 1) iterar B con datos reales, 2) distribuir los videos, y 3) si sobra tiempo, hacer un *spike* de máximo 3 días para documentar por qué crees que necesitas A. Nada de empezar a reescribir.

### Lo que NO haces este trimestre

**A) Reescritura: FUERA.**
No es que sea mala, es que es matemáticamente imposible y estratégicamente peligrosa para un solo founder.

Son 3 meses ideales = 6 meses reales sin entregar valor a ningún cliente, mientras sigues gastando 2h/día en soporte sobre la plataforma vieja. Su "impacto alto" es futuro e hipotético. El de B es presente y medible.

La reescritura solo se revisa el próximo trimestre si puedes responder con datos: "El framework actual me bloquea cada semana para entregar algo que los clientes pagan". Si no, se hace migración incremental, nunca big-bang.

**C) Panel de métricas: FUERA, por dependencia.**
Aunque quisieras, C depende de A. Sería A (24 semanas) + C (6 semanas). Estás hablando de 2026, no de este trimestre.

Si los clientes te piden métricas de verdad, la pregunta para el próximo trimestre no es "¿cuándo hago A para poder hacer C?", sino "¿puedo entregar una versión lite de C en el stack actual en 1 semana?". Probablemente sí.

### Tu trimestre en una línea

**B (2 sem) -> D (4 sem) -> Buffer/Iterar (2 sem) | A y C aparcados.**

Eso suma 6 semanas comprometidas sobre 8. Ese 25% de margen no es pereza, es la única forma de que un equipo de una persona cumpla un plan.