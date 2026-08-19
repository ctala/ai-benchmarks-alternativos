# Sakana Namazu — business_audit/roadmap_restriccion_capacidad

- model_id: `sakana/sakana-namazu`
- success: True  | final: 7.28 | quality: 8.0
- latency_total: 9.817s | tokens_per_second: 208.6
- input_tokens: 304 | output_tokens: 2048

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

El usuario es un fundador solo (empresa de una sola persona) con restricciones claras de tiempo y recursos. Necesita priorización de producto basada en capacidad real, no ideal.

Datos clave:
- 6 horas/día trabajo enfocado total
- 2 horas/día en soporte/operación (no delegable)
- 4 horas/día (~4h) para construir
- Quedan 8 semanas hasta cierre de trimestre
- 4 iniciativas: A, B, C, D con diferentes impactos y esfuerzos

Cálculo de capacidad disponible:
- 8 semanas × 5 días hábiles (asumiendo semana laboral estándar, aunque como founder probablemente trabaje más días, pero dice "trabajo enfocado 6h/día", debería ser conservador)
- Si asumimos 5 días a la semana: 8 × 5 = 40 días × 4h = 160h de construcción
- Si trabaja 6-7 días: 8 × 6 = 48 días × 4h = 192h, o 8 × 7 = 224h. Pero mejor ser conservador y asumir 5-6 días. Digamos entre 160-200h reales de construcción.

Análisis de iniciativas:

A) Reescribir plataforma: Impacto alto (futuro), Esfuerzo ~3 meses a tiempo completo. 
- 3 meses ≈ 12-13 semanas a tiempo completo. A tiempo completo con 4h/día constructivas sería el doble. O sea, ~6 meses con su ritmo actual. 
- Esto es un "hoyo negro" de tiempo. Con solo 8 semanas, es imposible terminarlo.
- Además: dependencia para C.

B) Arreglar flujo de alta: Impacto alto, Esfuerzo ~1 semana.
- 1 semana a tiempo completo = quizás 20-40h. Con 4h/día, son 2 semanas reales (máximo).
- Bajo esfuerzo, alto impacto. Claro ganador. Quick win.
- 60% de abandono en paso 2 es una hemorragia masiva. Esto está matando todo el funnel.

C) Panel de métricas: Impacto medio, Esfuerzo ~3 semanas. Depende de A.
- No se puede hacer hasta que A esté terminado (según dice el usuario).
- Si A no se hace este trimestre, C no se puede hacer tampoco (o habría que adaptarla a la plataforma actual, pero el usuario dice expresamente "Depende de que A esté terminado").
- Incluso si se hiciera: 3 semanas a tiempo completo = 6+ semanas a 4h/día. Consume casi todo el trimestre.

D) Videos de contenido: Impacto medio, Esfuerzo ~2 semanas.
- 2 semanas a tiempo completo = 4 semanas a 4h/día (20 días).
- Es marketing/contenido. Impacto medio. Puede atraer tráfico pero si el funnel pierde 60% en el paso 2, es como echar agua a un cubo con agujero.

Priorización (orden del trimestre):

1. B (Arreglar flujo de alta) - Imperativo. Es la hemorragia. 60% de abandono es un problema crítico. Si arreglas esto, todo lo demás que ya tienes (tráfico, usuarios) rinde más. Esfuerzo manejable (~2 semanas a ritmo de founder solo). ROI inmediato y masivo.

2. D (Videos de contenido) - Después de B. Pero hay que evaluar si tiene sentido. Si arreglas el funnel, necesitas más gente arriba del funnel para aprovechar la mejora. Sin embargo, el esfuerzo es significativo (2 semanas TC = ~4 semanas reales). Impacto medio. 
   - Alternativa: quizás hacer menos videos (3-5 en vez de 10) para reducir esfuerzo a ~1 semana TC.
   - Pero el usuario pide ordenar las 4 iniciativas. D debería ir después de B y antes de A (que no se hará).

3. C (Panel de métricas) - No se puede hacer por la dependencia. Y aunque se pudiera, effort alto para impacto medio. Además, el usuario es solo founder, los clientes probablemente prefieran que la herramienta funcione mejor (B) a tener un panel bonito (C). Dejar para después de A (que será en otro trimestre).

4. A (Reescribir) - No hacer este trimestre. Es una trampa. 3 meses a TC = imposible en 8 semanas con 4h/día. Además paraliza todo lo demás. Posponer al siguiente trimestre, pero planificarlo bien.

Espera, el usuario dice "Ordename el trimestre". Eso significa que quiere un roadmap/plan secuencial.

Plan propuesto:

Semanas 1-2 (o lo que tarde): B. Arreglar flujo de alta. 
Semanas 3-6: D. Contenido (ajustado). Aunque quizás debería decirle que haga D pero recortado.
Semanas 7-8: Buffer, soporte intenso, o planificar A.
A: Descartado para este trimestre.
C: Bloqueado por A, así que se pospone junto con A.

Pero hay que ser más específico con los números:
- Capacidad real: 8 semanas × 5 días × 4h = 160h (base conservadora). Si trabaja 6 días: 192h.
- B: Si es 1 semana a TC (40h), a su ritmo son 4 semanas (160h/40h = 4). Espera, eso no cuadra. Si "1 semana" significa 5 días a 8h = 40h. A 4h/día son 10 días hábiles = 2 semanas. OK.
- D: Si es 2 semanas a TC = 80h. A su ritmo son 20 días hábiles = 4 semanas.
Total B + D = 2 semanas + 4 semanas = 6 semanas. Caben justo en las 8, dejando 2 semanas de buffer/imprevistos/soporte extra.

Pero si B fuera más rápido (1 semana TC podría ser 5 días × 8h = 40h), sí son 2 semanas a 4h/día. 
Si trabaja 6 días a la semana: B = 1.7 semanas, D = 3.3 semanas. Total ~5 semanas.

Entonces el orden ideal:
1. B (semanas 1-2)
2. D (semanas 3-6, ajustando alcance si es posible)
3. C (no este trimestre, depende de A)
4. A (no este trimestre)

Pero debo ser claro: A y C se eliminan del trimestre. A es una trampa de premature rewrite / "big rewrite". Con recursos limitados, es suicidio de producto.

Además, debo dar un consejo de product manager: no se hace rewrite a menos que sea absolutamente necesario (la plataforma actual no permita escalar ni siquiera para los próximos 6 meses). Con 4h/día, un rewrite de 3 meses a TC se convierte en 6-9 meses reales (porque los rewrites siempre se extienden y hay que mantener la actual paralelamente). Es decir, A es un proyecto de medio año para él. Imposible.

También debo señalar que C depende de A. Si A no se hace, C no arranca. Y C tiene impacto medio, esfuerzo alto (3 semanas TC = 6 semanas reales). No rentable ahora.

Refinando D: El usuario dice "Grabar 10 videos de contenido". Como founder solo, quizás debería sugerirle reducir a 3-5 videos si ve que el funnel de B mejora mucho y necesita más tráfico. O mantenerlos pero entendiendo que consumirá la mayor parte del tiempo restante.

Espera, hay una alternativa interesante: ¿Y si D se hace antes que B? No, porque el funnel está roto. Echar