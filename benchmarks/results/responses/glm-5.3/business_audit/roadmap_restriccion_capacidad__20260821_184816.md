# GLM 5.3 — business_audit/roadmap_restriccion_capacidad

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.26 | quality: 10.0
- latency_total: 79.354s | tokens_per_second: 65.7
- input_tokens: 263 | output_tokens: 5210

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

**El orden: B → D (reducido) → iterar B. C queda fuera por dependencia. A, no este trimestre. Ni empezar.**

## La matemática primero

8 semanas × 5 días × 4h = **~160h de construcción**. Y no planifiques al 100%: reserva 25–30% para imprevistos (bugs, picos de soporte, vida). Presupuesto planificable real: **~120h**.

Con eso en la mesa:

- **B** ≈ 20–40h → cabe sobrado
- **D** ≈ 80h → cabe justo, mejor descontar
- **C** ≈ 120h + bloqueado por A → no cabe
- **A** ≈ 3 meses a tiempo completo ≈ 480h. Son 3–4 veces tu trimestre entero. A tus 4h/día reales, son ~6 meses.

## Por qué este orden

**1. B (semana 1).** La decisión más fácil del trimestre: máximo impacto por hora, y todo lo demás depende de él. Con 60% cayendo en el paso 2, arreglarlo puede casi duplicar tus usuarios activados. Además, la secuencia importa: no metas tráfico (D) a un embudo que pierde 6 de cada 10.

**2. D, pero a la mitad (semanas 3–4).** 5 videos bien apuntados al tipo de usuario que llega a tu alta, no 10. El contenido tiene cola larga: publicar antes vale más que publicar más.

**3. C: fuera.** Está bloqueado por A, y A no va a existir este trimestre. Pregunta incómoda que te debes: ¿la dependencia de A es real o es cómoda? Si un panel read-only sobre el stack actual cabe en ~1 semana y tienes churn real entre clientes de pago, considéralo en semanas 5–6. Si no, al próximo trimestre.

**4. A: no.** Un rewrite a medio hacer en la semana 8 es el peor estado posible: cero valor enviado, código en dos estados, moral por los suelos. Si el dolor del framework es real, la respuesta no es big-bang: es migración incremental el próximo trimestre (empieza por el módulo que más duele, detrás de flags, con tope de tiempo). Y solo si después de arreglar B el framework sigue siendo el cuello de botella.

## El trimestre, semana a semana

| Semana | Foco |
|---|---|
| 1 | B: instrumentar el funnel (medio día, imprescindible), arreglar paso 2, deploy |
| 2 | Medir + iterar: el leak se moverá al paso 3. Outline de videos |
| 3–4 | D: grabar y editar 5 videos, publicar 1/semana desde la 4 |
| 5–6 | Segunda iteración de onboarding con datos reales. Opcional: C descopeado solo si cabe en ~1 semana |
| 7–8 | Buffer y cierre: números antes/después, decisión formal sobre A para el próximo Q |

## Dos cosas más

- **Instrumenta antes de arreglar.** Sin línea base del paso 2, no puedes demostrar la mejora ni aprender dónde se mueve el leak.
- **Vigila las 2h de soporte.** Si B reduce tickets (suele pasar: mucha confusión nace en el alta), esas horas vuelven a construcción. Mídelo — es la única forma de que tu presupuesto crezca este trimestre.

La regla que aplicué: no prioricé por impacto, prioricé por impacto por hora y por riesgo de quedar a medias. B gana por goleada; A pierde por las dos.