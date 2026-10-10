# Claude Haiku 5.5 — business_audit/roadmap_restriccion_capacidad

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 7.63 | quality: 8.0
- latency_total: 10.86s | tokens_per_second: 176.2
- input_tokens: 420 | output_tokens: 1914

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

# Orden del trimestre

**1. B: Arreglar el flujo de alta (semanas 1–2)**
Es el mayor impacto por hora. Cerca de 20h de trabajo para recuperar parte del 60% que se pierde en el paso 2. Además, mejorar la conversión antes que todo lo demás hace que cada euro o minuto de adquisición rinda más.

**2. D: Grabar 10 videos (semanas 2–5)**
Impacto medio con unas 40h. Empieza después de B, para que el contenido dirija a un flujo que ya funciona.

**3. Decidir sobre A (semana 5 en adelante)**
No cabe en este trimestre. Tres meses a tiempo completo son unas 400h, y tú tienes unas 100h libres tras B y D. Aunque las tuvieras, la reescritura no entrega valor hasta terminar, y no sabrías si va bien hasta el final.

**4. C: Aplazar**
Depende de A, así que no puede empezar este trimestre. Si A se aplaza, C también.

# Qué hacer con las ~100h restantes

- **Reserva del 20–30% (~25h)** para lo que sale mal. Con una persona y estimaciones optimistas, casi siempre sale mal algo.
- **Medir B** durante las semanas siguientes: tasa de conversión del paso 2 antes y después. Si no mejora, el problema no es el flujo y conviene saberlo pronto.
- **Investigación acotada para A (~10h):** qué es lo que hoy duele de la plataforma (velocidad de desarrollo, rendimiento, deuda concreta) y si se puede resolver con una refactorización parcial. Eso te da una decisión con datos para el próximo trimestre.

# Lo más importante que no aparece en la lista

Tus 2h diarias de soporte y operación son un tercio de tu capacidad. Cualquier cosa que automatices, documentes o delegues (plantillas de respuesta, FAQ, scripts de operación) devuelve horas a todas las iniciativas, incluida A. Dedica una pequeña parte del trimestre a reducir esa carga, porque el resto del plan depende de ella.

# Resumen

| Semanas | Iniciativa | Horas aprox. |
|---|---|---|
| 1–2 | B: flujo de alta | ~20h |
| 2–5 | D: 10 videos | ~40h |
| 5–6 | Medición de B + investigación de A | ~10h |
| 5–8 | Reducción de soporte/operación | ~20h |
| Todo el trimestre | Reserva | ~25–30h |
| — | A y C | Próximo trimestre |

Si tus estimaciones de esfuerzo cambian al empezar (B tarda más, por ejemplo), recalcula desde la reserva y no desde A.