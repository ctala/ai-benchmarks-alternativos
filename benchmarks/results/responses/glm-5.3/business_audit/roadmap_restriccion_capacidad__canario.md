# GLM 5.3 — business_audit/roadmap_restriccion_capacidad

- model_id: `z-ai/glm-5.3`
- success: True  | final: 6.87 | quality: 8.0
- latency_total: 61.143s | tokens_per_second: 79.8
- input_tokens: 263 | output_tokens: 4880

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

## La cuenta primero, porque decide todo

Tus 8 semanas reales son: 8 × 5 días × 4h = **~160h brutas**. Planifica ~140h (algo siempre se rompe).

A necesita ~3 meses a tiempo completo = **260h+ incluso a tu ritmo**. No cabe ni dándole el trimestre entero. Y como C depende de A, en este escenario C también muere. A no es "prioridad baja": es un **no** para este trimestre.

## El orden

**1. B — Semana 1.** El ROI más alto del trimestre por mucho. Antes de tocar código, captura el funnel actual como baseline: si pierdes 60% en el paso 2, cualquier mejora la vas a querer demostrar con número al cierre.

**2. B otra vez — Semana 2.** Sí, leer bien: medir el lift e iterar el paso 2 una vez más. Un funnel que pierde 60% rara vez se arregla en un solo intento. No pases a lo siguiente hasta tener el dato.

**3. D — Semanas 3-4.** Grabar en batch y publicar 2/semana desde la semana 4. Va *después* de B a propósito: el contenido alimenta un funnel que ya no pierde 60%.

**4. Semanas 5-8 — aquí está la decisión real.** Reto la premisa: ¿un panel de métricas para clientes *de verdad* necesita el rewrite? Casi nunca (es reporting de solo-lectura sobre datos que ya tienes). Dos caminos:

- **Si la dependencia es rompible (mi apuesta):** C-v0 sobre el stack actual, descopeado a las 2-3 métricas que los clientes piden de verdad. ~3 semanas, cabe.
- **Si es real:** C queda para el próximo trimestre. Usa las semanas 5-8 en pre-vender C a 3 clientes (validación casi gratis) y, si A es inevitable, a lo sumo una semana en partirlo en slices que entreguen valor por sí solas (migración incremental). **No empieces el rewrite en grande con 4 semanas left.**

**Transversal:** 3h/semana matando el ticket de soporte más frecuente. Es la única inversión que compra horas para el próximo trimestre.

## Si algo se retrasa, el orden de recorte es:

1. Videos: 10 → 6
2. C-v0: menos métricas
3. **Nunca** la iteración de B

## Cómo cierras el trimestre

Con este plan: activación mejorada con número verificable, contenido alimentando un funnel que convierte, y C validado o en v0 con clientes usándolo.

El escenario alternativo (empezar A): 60% de un rewrite terminado, cero cosas nuevas en producción, el funnel igual de roto mientras grabas nada y publicas nada. Ese trimestre no se puede defender ni ante ti mismo.

A no desaparece: se decide en la planificación del Q+1, con datos del funnel arreglado y C validado en la mano.