# Claude Haiku 5.5 — business_audit/roadmap_restriccion_capacidad

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.98 | quality: 10.0
- latency_total: 13.957s | tokens_per_second: 174.3
- input_tokens: 420 | output_tokens: 2432

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

**Orden:** B → D → spike de evaluación de A → reducir soporte. **C y A no entran en este trimestre.**

Asumo que B y D (1 y 2 semanas) están estimadas a tu capacidad real de 4h/día. Son unas 60h de las ~160h disponibles en 8 semanas.

**1. B: arreglar el flujo de alta (semana 1, ~20h).**
Es el mejor retorno del trimestre: impacto alto, esfuerzo bajo y efecto inmediato sobre todo lo que venga después. Antes de tocar nada, mide la tasa de paso por el paso 2 durante unos días para tener una línea base. Si no lo haces, no sabrás si funcionó.

**2. D: los 10 videos (semanas 2-3, ~40h).**
Va después de B a propósito: no quieres atraer tráfico hacia un embudo que pierde al 60% de la gente. Además, los videos pueden mostrar el flujo ya arreglado.

**3. Spike de evaluación de A (semana 4, ~20h, con límite estricto).**
A tal como está planteado no cabe: 3 meses a tiempo completo son unas 260h a tu ritmo, y solo tienes ~100h libres tras B y D. Empezarla y dejarla a medias sería el peor resultado, porque dejarías la plataforma en dos frameworks.

En lugar de eso, usa una semana para responder una pregunta concreta: **¿qué te está frenando hoy?** Anota cuántas horas a la semana pierdes por la plataforma actual (bugs, cambios lentos, deuda) y qué features concretas no puedes hacer. Si la lista es corta, A no se justifica todavía. Si es larga y costosa, tendrás datos para planificar A en el próximo trimestre, con alcance y fechas reales.

**4. Reducir las 2h diarias de soporte y operación (semanas 5-8, ~60-80h).**
Este es el movimiento que más pesa en tu capacidad. Cada hora que ahorras en operación equivale a una hora más de construcción durante todo el año. Automatiza las tareas repetitivas (respuestas plantilla, scripts, alertas, documentación de preguntas frecuentes) hasta liberar al menos 30-60 min diarios. No es delegar, así que encaja con tu restricción actual.

**Lo que sacas del trimestre:**
- **C:** depende de A, que no vas a terminar. Si las métricas para clientes son importantes, revisa si puedes construirlas sobre la plataforma actual con un alcance mínimo. Si no, pásalo al próximo trimestre.
- **A:** no se abandona, se decide con datos al final de la semana 4.

**Cosa que deberías revisar:** la justificación de A ("velocidad y todo lo futuro") es vaga. Antes de comprometer tres meses, pregúntate qué cosas concretas no puedes construir hoy y cuánto te cuestan. Si la respuesta no es clara, probablemente no es el momento de reescribir.