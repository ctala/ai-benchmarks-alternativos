# Claude Fable 5.1 — business_audit/roadmap_restriccion_capacidad

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 6.59 | quality: 8.0
- latency_total: 28.901s | tokens_per_second: 62.0
- input_tokens: 420 | output_tokens: 1793

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

**Primero, la cuenta real.**

4h/día × 5 días × 8 semanas = **160 horas** de construcción este trimestre. Y eso si no se enferma nadie, no hay un incendio de soporte y tus estimaciones se cumplen (no se cumplen; suma 30% a todo).

Asumo que tus esfuerzos están en semanas a tiempo completo (40h), porque así se estima. Traducido a tu capacidad real:

| | Esfuerzo | Tus semanas |
|---|---|---|
| A | ~480h | 24 semanas |
| B | ~40h | 2 semanas |
| C | ~120h (+A) | 6 semanas, bloqueado |
| D | ~80h | 4 semanas |

**El orden del trimestre:**

**1. B – Arreglar el alta. Semanas 1-2.**
Pierdes al 60% en el paso 2. Es el mejor ratio impacto/esfuerzo que vas a ver en el año. Cualquier otra cosa que hagas antes de esto está echando agua en un cubo roto. Va primero y sin discusión.

**2. D – Los videos. Semanas 3-6.**
Solo después de B, porque el contenido trae gente, y la gente ahora llega a un alta que funciona. Si lo haces al revés, grabas 10 videos para que el 60% se vaya en el paso 2.

**3. Semanas 7-8: colchón.**
No lo rellenes. Las 40h sobrantes se las va a comer el desfase de B y D. Si milagrosamente sobran, úsalas en lo siguiente que digo abajo.

**Lo que no haces:**

**A – No.** No este trimestre, y te diría que probablemente nunca en esa forma. Tres meses a tiempo completo son seis meses a tu ritmo real durante los cuales no sale nada: ni arreglos, ni contenido, ni features. Una reescritura es la iniciativa con más probabilidad de duplicar su estimación y la menos probable de que un cliente la note. "Velocidad y todo lo futuro" es exactamente lo que dice toda reescritura antes de empezar. Si hay dolor concreto con el framework actual, escríbelo en una lista de problemas específicos y resuélvelos uno a uno cuando aparezcan.

**C – No, está bloqueado por A.** Pero cuestiona esa dependencia: ¿un panel con tres números para tus clientes de verdad necesita la reescritura, o es que ya tenías decidido hacer A y C es la excusa? Si la versión mínima se puede hacer en el stack actual, pasa a la lista del próximo trimestre como candidata.

**Una cosa más, que importa más que todo lo anterior:**

Las 2h diarias de soporte y operación son tu verdadero cuello de botella. Reducirlas a 1h te da un 25% más de capacidad de construcción, cada semana, para siempre. Eso es más "velocidad futura" que cualquier framework. Con el colchón de las semanas 7-8, o en huecos, dedica tiempo a lo que mate soporte: respuestas enlatadas, una página de FAQ, automatizar la tarea operativa que más se repite. Es la iniciativa E que no listaste y es la que más te conviene.

**Resumen:** B → D → colchón. A y C fuera. Y empieza a comerte las 2h de soporte.