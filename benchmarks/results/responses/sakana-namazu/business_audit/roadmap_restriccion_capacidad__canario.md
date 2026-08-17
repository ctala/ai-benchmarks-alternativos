# Sakana Namazu — business_audit/roadmap_restriccion_capacidad

- model_id: `sakana/sakana-namazu`
- success: True  | final: 8.68 | quality: 10.0
- latency_total: 9.804s | tokens_per_second: 208.9
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

El usuario es un fundador solitario (one-person business). Tiene restricciones de tiempo muy claras:
- 6 horas de trabajo enfocado al día.
- 2 horas se van en soporte y operación diaria no delegable.
- Le quedan ~4 horas/día reales para construir.
- Quedan 8 semanas hasta el cierre del trimestre.

Necesita priorizar 4 iniciativas (A, B, C, D) y quiere que le ordene el trimestre.

Tengo que pensar como jefe de producto que prioriza con la capacidad real del equipo (él solo, 4h/día), no con la ideal.

Primero, calculemos la capacidad real:
- 8 semanas × 5 días hábiles (asumiendo semana laboral estándar, aunque podría ser 7, pero mejor asumir 5-6 para ser realista; el usuario no especifica, pero lo habitual es 5-6 días para un founder. Sin embargo, debería ser conservador. Asumamos 5 días para ser seguros, o mejor, pregunta implícita: debería asumir 5 días laborables. Pero muchos founders trabajan 6. Voy a hacer cálculos para 5-6 días, pero usaré 5 para ser conservador, o quizás 6 si es un "one person". Mejor dar un rango o asumir 6 días si es founder, pero para ser realista y no quemarlo, 5 días es más sano. Usemos 5 días hábiles x 8 semanas = 40 días. 40 días x 4h = 160h reales de construcción. Si trabaja 6 días: 48 días x 4h = 192h. Digamos entre 160 y 192h. Usemos ~160h como base conservadora (5 días/semana).

Ahora evaluemos las iniciativas:

A) Reescribir plataforma en otro framework. Impacto: alto. Esfuerzo: ~3 meses a tiempo completo.
- 3 meses a tiempo completo asumiendo 40h/semana = 12 semanas × 40h = 480h. Él tiene 160h. Esto es imposible en 8 semanas. Ni siquiera cercano. Además, el impacto es "alto pero futuro" y existe riesgo de never-ending rewrite. En un equipo de una persona, una rewrite es una trampa mortal: no hay nada que funcione mientras tanto, y el negocio se detiene. Prioridad: NO HACER. Posponer al próximo trimestre o cancelar.

B) Arreglar flujo de alta. Impacto: alto. Esfuerzo: ~1 semana.
- 1 semana a tiempo completo = 40h. Él tiene 4h/día, así que en una semana de 5 días tiene 20h. Si dice ~1 semana, quizás son 1 semana de trabajo full-time, o sea ~40h, lo cual serían 2 semanas suyas (20h efectivas). Pero quizás el usuario estimó "1 semana" a su ritmo. Sin embargo, dado que sus estimaciones parecen a "full-time" (ej. A son 3 meses full-time), asumiré que las semanas son laborales full-time (~40h). Entonces B = 40h → 2 semanas suyas (20h/semana). Aún así, cabe perfectamente. Impacto alto inmediato en conversión. Es quick win. Debería ser el #1.

C) Añadir panel de métricas. Impacto: medio. Esfuerzo: ~3 semanas full-time = 120h. En su tiempo: 6 semanas (120h / 20h semanales). Depende de A terminado.
- Como depende de A, y A no se hará este trimestre, C es imposible a menos que haga un workaround o use el framework actual. Pero el usuario dice "depende de que A esté terminado". Por tanto, C está bloqueado. Prioridad: NO HACER este trimestre.

D) Grabar 10 videos de contenido. Impacto: medio. Esfuerzo: ~2 semanas full-time = 80h. En su tiempo: 4 semanas (80h / 20h semanales).
- Esto consume todo el trimestre restante si lo hace entero. Impacto medio. Pero hay que ver el contexto: ¿necesita clientes? El flujo de alta está roto (60% abandono en paso 2). No tiene sentido traer tráfico (vía contenido) si el embudo está roto. Por tanto, D debería venir después de B, o quizás hacerse en paralelo si es posible, pero el esfuerzo es alto. Podría reducirse scope: ¿realmente necesita 10 videos? Podría hacer 2-3 videos cortos. Pero con la info dada, D debería ser secundario o recortado.

Orden lógico:
1. B: arreglar el flujo de alta. Es el cuello de botella más claro. 60% de abandono en paso 2 es dinero tirado. Impacto alto, esfuerzo relativamente bajo. Primeras 2 semanas.
2. D: Contenido, pero con scope reducido o diferido. O mejor, tras B, usar el resto para D pero evaluar si es sostenible. Sin embargo, es 3-4 semanas. Quedarían unas 3-4 semanas después de B (si B toma 2 semanas). Así que podría hacerse parcialmente.
3. A y C: Al cubo. No se tocan este trimestre.

Pero quizás el usuario quiera un roadmap claro. Necesito ser muy directo y franco: A es una trampa. C está bloqueado. B es prioritario. D es opcional si queda tiempo, pero probablemente deba recortarse o posponerse.

Además, debo considerar: ¿hay alguna iniciativa no listada? Soporte y operación ya están contemplados. Pero quizás debería sugerir un "E" implícito: usar alguna de las horas para automatizar o reducir las 2h de operación/soporte. Pero el usuario no preguntó eso directamente, aunque como jefe de producto podría sugerirlo como meta "shadow".

El prompt dice "Eres jefe de producto de una empresa de una sola persona. Priorizas con la capacidad real del equipo, no con la ideal." Debo actuar así: directo, sin azúcar, enfocado en lo que cabe en 8 semanas a 4h/día.

Cálculos más precisos:
- Capacidad total: 8 semanas × 5 días × 4h = 160h. (Si trabaja 6 días: 192h).
- B: ~1 semana full-time = 40h → ~2 semanas a su ritmo (con 20h/semana productivas de build). O quizás la estimación ya es a su ritmo. Para ser prudentes, asumamos que las estimaciones son en "persona-semana". Es decir, si estuviera 100% en eso. Entonces semana = 40h. Entonces 40h / 4h día = 10 días = 2 semanas calendario.
- D: ~2 semanas full-time = 80h → ~4 semanas calendario a su ritmo.
- B + D = 6 semanas. Quedan 2 semanas de holgura o imprevistos. Eso cabe en el trimestre.

Entonces el plan podría ser:
- Semanas 1-2: B (fix onboarding).
- Semanas 3-6: D (contenido), pero con matiz: quizás debería recortar D a 5 videos en vez de 10 para dejar margen. O si el impacto es "medio" y B es "alto", quizás debería hacerse B y luego dedicar el resto a mejorar onboarding más o a reducir deuda técnica, pero dado que A es too big, D es la única que cabe.
- A y C: No. Y específicamente, A es "muerte por rewrite".

Pero el usuario pide "Ordename el trimestre". Debo dar una lista ordenada y justificar.

Estructura de respuesta:
1. Estado de capacidad real (los números crudos).
2. Veredicto claro: qué