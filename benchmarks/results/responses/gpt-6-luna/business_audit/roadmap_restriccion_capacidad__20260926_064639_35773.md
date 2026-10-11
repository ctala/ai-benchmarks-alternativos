# GPT-6 Luna — business_audit/roadmap_restriccion_capacidad

- model_id: `openai/gpt-6-luna`
- success: True  | final: 7.46 | quality: 8.0
- latency_total: 23.807s | tokens_per_second: 88.5
- input_tokens: 241 | output_tokens: 2108

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

**No intentaría meter las cuatro iniciativas en este trimestre.** Tu capacidad son unas **160 horas** en ocho semanas (4 h/día, cinco días por semana), y conviene no comprometerlas todas por completo.

### Orden recomendado

1. **B — Arreglar el alta.** Es la prioridad clara: una pérdida del 60% en el paso 2 es un problema concreto y la solución cabe en una semana.
2. **D — Videos, con una condición.** Hazlos solo si ya tienes claro dónde se publicarán y cómo llegarán a clientes. Si no, prueba primero con 2–3 videos y mide si generan conversaciones o registros; no optimices por “terminar 10”.
3. **C — No construirlo este trimestre.** Está bloqueado por A. Antes, valida la demanda con entrevistas o un informe manual para clientes: quizá puedas comprobar el valor sin el panel ni la reescritura.
4. **A — No iniciar la reescritura este trimestre.** Tres meses a tiempo completo equivalen a unas **480 horas**; a tu ritmo, son aproximadamente **24 semanas**, no las ocho disponibles. Además, “más velocidad para todo lo futuro” necesita convertirse en beneficios concretos antes de comprometerte.

### Plan de ocho semanas

- **Semana 1:** B: implementar y lanzar el arreglo.
- **Semana 2:** medir el alta, corregir problemas y confirmar que mejora la conversión.
- **Semanas 3–4:** D, si tienes distribución y una hipótesis clara de impacto. Si no, dedica ese tiempo a iterar el alta.
- **Semanas 5–6:** seguir mejorando el punto de mayor fricción que revelen los datos y validar manualmente el interés por C.
- **Semanas 7–8:** conservar como margen para imprevistos y, si la reescritura sigue pareciendo necesaria, hacer un **diagnóstico acotado**, no empezar A: identificar qué limita hoy el desarrollo y si hay una solución incremental.

**Éxito de B:** mide cuántas personas completan el paso 2 y cuántas terminan el alta, comparado con la situación actual.  
**Decisión sobre A:** tómala con evidencia de que el framework actual está causando un coste importante, no solo porque una reescritura prometa acelerar el futuro.