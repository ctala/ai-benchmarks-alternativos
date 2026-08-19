# KAT Coder Air v2.5 — business_audit/roadmap_restriccion_capacidad

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 8.0 | quality: 8.0
- latency_total: 4.028s | tokens_per_second: 175.3
- input_tokens: 255 | output_tokens: 706

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



# Trimestre realista

## El problema con A

**A no cabe en este trimestre.** Son 3 meses a tiempo completo. Con 4h/día, serían **~6 meses**. Si lo empiezas, no terminarás ninguna otra cosa.

Y como **C depende de A**, C tampoco cabe.

---

## Tu trimestre

### Semana 1 — B: Arreglar el flujo de alta
Impacto alto, 1 semana. Es el **cuello de botella más caro** que tienes. Pierdes 60% en el paso 2, eso es dinero que se va *ahora*. Si B funciona, te ahorra soporte también.

### Semanas 2–3 — D: Grabar 10 videos
Impacto medio, 2 semanas. Contenido es inversión de crecimiento. No depende de nada.

### Semanas 4–8 — A: Empezar la reescritura
La inicias, pero con la conciencia de que **no terminas**. En 5 semanas tendrás un MVP del nuevo framework, suficiente para validar que va en la dirección correcta. El resto del trimestre que viene lo cierras.

### C queda para el próximo trimestre
Porque depende de A. No intentes forzarlo.

---

## Resumen visual

| Semana | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|--------|---|---|---|---|---|---|---|---|
| **B** | ✅ | | | | | | | |
| **D** | | ✅ | ✅ | | | | | |
| **A** | | | | ✅ | ✅ | ✅ | ✅ | ✅ |
| **C** | | | | | | | | |

---

## Una pregunta que te hago

El 60% de pérdida en el paso 2 del alta… **¿ya lo has diagnosticado?** A veces el "arreglar" es más de 1 semana si no sabes qué está rompiendo. Si no lo has visto con usuarios reales, dedica medio día a grabar sesiones de onboarding antes de tocar código.