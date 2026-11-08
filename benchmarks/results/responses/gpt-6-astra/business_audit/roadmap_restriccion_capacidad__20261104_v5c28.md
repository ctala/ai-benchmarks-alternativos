# GPT-6 Astra — business_audit/roadmap_restriccion_capacidad

- model_id: `openai/gpt-6-astra`
- success: True  | final: 6.58 | quality: 8.0
- latency_total: 23.128s | tokens_per_second: 37.8
- input_tokens: 241 | output_tokens: 875

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

**Este trimestre: B primero, D después en tandas. A y C quedan fuera.** No intentaría encajar las cuatro.

### Tu capacidad real

Asumiendo 5 días de trabajo por semana:

- 8 semanas × 5 días × 4 horas = **160 horas para construir**.
- Comprometería **120 horas** y reservaría **40 horas** para imprevistos, correcciones y seguimiento. Las 2 horas diarias de soporte ya están descontadas.

Para comparar, asumo que las semanas de esfuerzo de B, C y D son de 40 horas. Si ya las calculaste a 4 horas diarias, el calendario se acorta; la prioridad no cambia.

### Decisión por iniciativa

| Iniciativa | Decisión | Motivo |
|---|---|---|
| **B. Arreglar el alta** | **Primera prioridad** | Impacto alto sobre una fuga concreta, con alcance pequeño: unas 40 h, equivalentes a 2 semanas tuyas. |
| **D. Grabar contenido** | **Segunda, por tandas** | Unas 80 h, equivalentes a 4 semanas tuyas. Conviene atraer gente después de mejorar el alta. |
| **A. Reescribir plataforma** | **Fuera del trimestre** | Tres meses a tiempo completo son aproximadamente 480 h: unas 24 semanas a tu ritmo. No cabe, y empezarla consumiría el trimestre sin terminarla. |
| **C. Panel de métricas** | **Bloqueada; fuera del trimestre** | Depende de A. No es una opción ejecutable ahora, aunque su esfuerzo aislado pareciera asumible. |

### Calendario de las 8 semanas

**Semanas 1–2: arreglar B**
- Comprobar la medición del paso 2 e identificar la causa principal del abandono.
- Corregir el problema con el menor cambio posible, sin convertirlo en un rediseño completo.
- Publicar y medir tanto el abandono de ese paso como la finalización del alta.

**Semanas 3–6: ejecutar D en tandas**
- Empezar con 2–3 vídeos y publicarlos; no producir los 10 antes de aprender nada.
- Usar las preguntas de soporte y los obstáculos del alta como temas.
- Continuar hasta 10 si las primeras piezas muestran señales útiles: visitas cualificadas, altas o conversaciones con potenciales clientes.
- Si B sigue fallando, **recortar vídeos antes que dejar roto el alta**.

**Semanas 7–8: margen protegido y cierre**
- Absorber imprevistos y correcciones.
- Revisar los resultados de B y D.
- Aprovechar el margen que sobreviva para ajustes pequeños, **no para arrancar A**.

### Dos reglas para no desbordarte

1. **Una sola iniciativa en ejecución a la vez.**
2. **El objetivo no es “hacer diez vídeos”; es mejorar la conversión y después generar demanda que puedas convertir.**

La reescritura solo volvería a la mesa si puedes demostrar qué problema concreto impide resolver hoy y por qué un cambio acotado no basta. “Acelerar todo lo futuro” no justifica consumir una capacidad que este trimestre no tienes.