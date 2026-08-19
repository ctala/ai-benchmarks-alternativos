# KAT Coder Air v2.5 — business_audit/roadmap_restriccion_capacidad

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 7.8 | quality: 8.0
- latency_total: 5.017s | tokens_per_second: 186.0
- input_tokens: 255 | output_tokens: 933

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



# Plan del Trimestre

## El problema de fondo

Tienes **32 horas** (8 semanas × 4h/día × 5 días). Las iniciativas suman **6 semanas**. Pero **A y C son una trampa**: C depende de A, y A no cabe en el trimestre.

---

## Qué hacer (y en qué orden)

### Semana 1 → B
El fix del flujo de alta. **1 semana, alto impacto, cero dependencia.** Si el 60% se cae en el paso 2, estás dejando dinero sobre la mesa *ahora*. Esto es prioridad cero.

### Semanas 2-3 → D
10 videos. **2 semanas, impacto medio, sin dependencias.** Contenido es activo a largo plazo y no bloquea nada.

### Semanas 4-8 → Elige una de dos

| Opción | Qué haces | Por qué |
|--------|-----------|---------|
| **A (versión MVP)** | Identifica el **1 problema** que la reescritura resolvería hoy y resuélvelo sin reescribir | Si no puedes validar que la reescritura trae ROI, no la hagas |
| **C (sin A)** | Métricas con lo que tienes, aunque sea manual | Si el producto actual aguanta, no esperes a A |

---

## Qué NO hacer este trimestre

- **A completo**: 3 meses a tiempo completo con 4h/día = **no cabe**. Si lo empiezas, no lo terminas y pierdes las 8 semanas.
- **C como plan principal**: Depende de A. Si A no está, C no existe.

---

## La pregunta que te debo

¿Qué problema te está frenando **hoy** más que otro? Porque si es el rendimiento de la plataforma actual, A podría ser necesario para el **próximo trimestre**, pero este debes cerrarlo con B y D.

**B → D → (A parcial o C con lo que hay).**