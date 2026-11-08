# GPT-6 Luna Pro — business_audit/roadmap_restriccion_capacidad

- model_id: `openai/gpt-6-luna-pro`
- success: True  | final: 6.04 | quality: 6.0
- latency_total: 35.723s | tokens_per_second: 113.5
- input_tokens: 5668 | output_tokens: 4055

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

Asumo que las estimaciones están expresadas en semanas a tiempo completo. Con 4 horas enfocadas al día, tienes unas **20 h por semana**, o **160 h en el trimestre**. En esa escala:

- **B:** ~40 h → 2 semanas de calendario.
- **D:** ~80 h → 4 semanas.
- **C:** ~120 h → 6 semanas, pero está bloqueada por A.
- **A:** ~12 semanas a tiempo completo → unas **24 semanas de calendario** a tu capacidad actual.

## Orden del trimestre

1. **Semanas 1–2: B — arreglar el alta.**  
   Es la prioridad clara: problema cuantificado, impacto alto y esfuerzo acotado. Instrumenta el flujo antes de cambiarlo y mide si mejora la finalización del paso 2 y la activación, no solo si el nuevo flujo se ve mejor.

2. **Semanas 3–6: D — solo si tienes un plan de distribución.**  
   Grabar 10 videos no garantiza impacto. Hazlos si sabes dónde se publicarán, a quién van dirigidos y qué acción esperas que genere cada uno. Si ese plan no existe, no gastaría 80 horas en producirlos todavía.

3. **Semanas 7–8: reservar capacidad para medir e iterar.**  
   Usa ese tiempo para ajustar B con los datos, atender imprevistos o validar la demanda del panel de métricas. No hace falta llenar cada hora con una iniciativa nueva.

## Qué dejar fuera

- **A: no este trimestre.** A tu capacidad real, no es un proyecto de 3 meses, sino de aproximadamente 6 meses de calendario. Además, te consumiría el trimestre y no hay evidencia aquí de que reescribir sea mejor que arreglar problemas concretos.
- **C: no este trimestre.** Está bloqueada por A, y no empezaría una reescritura solo para desbloquear un panel de impacto medio.

**En resumen:** B primero; D después solo si puedes medir su efecto; A y C fuera del plan trimestral. Si las duraciones que diste ya están calculadas para tus 4 horas diarias, el calendario cambia, pero la dependencia y la prioridad de B siguen igual.