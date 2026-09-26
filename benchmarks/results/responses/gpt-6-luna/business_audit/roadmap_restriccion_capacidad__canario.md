# GPT-6 Luna — business_audit/roadmap_restriccion_capacidad

- model_id: `openai/gpt-6-luna`
- success: True  | final: 6.13 | quality: 6.0
- latency_total: 18.587s | tokens_per_second: 77.9
- input_tokens: 241 | output_tokens: 1447

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

Asumiendo que las estimaciones son de **semanas a tiempo completo** (40 h/semana), tienes **160 horas reales** en el trimestre: 20 h/semana durante 8 semanas.

## Orden

1. **B — Arreglar el alta**
2. **D — Probar el contenido**, si puedes medir si atrae clientes
3. **A y C — No hacerlos este trimestre**

## Plan de 8 semanas

| Semanas | Trabajo | Horas |
|---|---|---:|
| 1–2 | **B:** diagnosticar y arreglar el paso 2 | ~40 h |
| 3 | Medir el cambio en altas y corregir problemas que aparezcan | ~20 h |
| 4–7 | **D:** producir los 10 videos | ~80 h |
| 8 | Margen para imprevistos; medir resultados y decidir siguientes pasos | ~20 h |

B va primero: hay una pérdida grande y localizada en el flujo, y es la iniciativa más acotada. Mide la conversión antes y después —idealmente también la activación, no solo completar el formulario— para confirmar que el arreglo mejora el resultado.

D entra después, pero trata los videos como una prueba: define de antemano qué resultado buscas y cómo lo atribuirás. Si no tienes un canal claro para distribuirlos o medir si generan demanda, no gastes automáticamente las 80 horas; conserva ese tiempo para iterar B o atender imprevistos.

**No empezaría A ahora:** tres meses a tiempo completo son aproximadamente 480 horas, o unas 24 semanas con tu capacidad actual. En ocho semanas solo podrías avanzar una parte del cambio y probablemente no llegar a un resultado utilizable. **C tampoco cabe**: depende de A y además requiere unas seis semanas de tu capacidad actual. Revisaría la decisión sobre A cuando tengas evidencia de que la plataforma limita el negocio y una migración acotada con hitos entregables.