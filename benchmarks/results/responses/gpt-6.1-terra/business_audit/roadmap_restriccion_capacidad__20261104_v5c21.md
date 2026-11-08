# GPT-6.1 Terra — business_audit/roadmap_restriccion_capacidad

- model_id: `openai/gpt-6.1-terra`
- success: True  | final: 7.2 | quality: 8.0
- latency_total: 10.928s | tokens_per_second: 71.3
- input_tokens: 241 | output_tokens: 779

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

## Prioridad: B → D. No iniciar A ni C este trimestre.

**Capacidad real:** suponiendo 5 días por semana, tienes 8 × 5 × 4 = **160 horas de construcción**. Las 2 horas diarias de soporte y operación ya quedan fuera.

Para ordenar el calendario, supongo que tus estimaciones de «1 semana» y «2 semanas» equivalen a semanas de 40 horas. Si ya estaban calculadas con tus 4 horas diarias, el plan se acorta.

| Semanas | Trabajo | Capacidad |
|---|---|---:|
| 1–2 | **B: arreglar el alta.** Incluye diagnóstico, implementación y comprobación del resultado. | ~40 h |
| 3–6 | **D: grabar los 10 videos.** Prepara, graba y publica; revisa la respuesta antes de completar toda la tanda. | ~80 h |
| 7–8 | **Reserva:** imprevistos y seguimiento de B. Si no se consume, aborda la siguiente mejora según lo aprendido. | ~40 h |

### Por qué

- **B va primero:** tiene impacto alto, esfuerzo acotado y ataca una pérdida concreta del 60% en el paso 2. Mide esa tasa antes y después, usando el mismo criterio.
- **D va después:** cabe sin depender de otra iniciativa. Publicar por tandas te permite ajustar el contenido con señales reales.
- **A queda fuera:** tres meses a tiempo completo no caben en tus 160 horas trimestrales. No la empezaría «un poco» sin una versión más pequeña y útil por sí sola.
- **C queda bloqueada por A:** aunque su esfuerzo aislado podría caber, no está disponible bajo la dependencia actual. Solo la reconsideraría si descubres una forma viable de ofrecer una versión útil sin A.

Si tus estimaciones ya usan jornadas de 4 horas, B ocuparía una semana y D dos; te quedarían cinco. No las llenaría automáticamente: usaría primero los resultados de B y D para decidir el siguiente trabajo.