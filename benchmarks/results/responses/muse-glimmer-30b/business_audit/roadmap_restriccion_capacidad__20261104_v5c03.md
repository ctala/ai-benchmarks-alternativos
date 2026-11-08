# Muse Glimmer 30B — business_audit/roadmap_restriccion_capacidad

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 8.83 | quality: 10.0
- latency_total: 13.138s | tokens_per_second: 136.2
- input_tokens: 266 | output_tokens: 1789

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

Con tu capacidad real no puedes hacer A y C este trimestre. Son 4h/día de construcción = ~160h en 8 semanas.

**Capacidad real:**
* A Reescribir plataforma: 3 meses full time ≈ 480h. Necesitas 24 semanas a tu ritmo. Imposible y bloquea todo.
* B Flujo de alta: 1 semana full time ≈ 40h. A tu ritmo 2 semanas.
* C Panel métricas: 3 semanas full time ≈ 120h. A tu ritmo 6 semanas + depende de A terminado. Imposible ahora.
* D 10 videos: 2 semanas full time ≈ 80h. A tu ritmo 4 semanas.

### Orden para el trimestre

**1. B - Arreglar el flujo de alta. Semanas 1-2**
Impacto alto, esfuerzo bajo, sin dependencias. Pierdes el 60% en el paso 2. Eso es dinero que se va ahora.
Hazlo primero y mide antes/después: tasa de completado paso 2, conversiones de alta a pago.
Objetivo: 40h de foco = 2 semanas reales. Si lo acortas a 1 semana de foco intenso, mejor.

**2. D - Grabar 10 videos de contenido. Semanas 3-6**
Impacto medio, independiente, y genera demanda para el embudo que acabas de arreglar.
Con 4h/día puedes hacer 2-3 videos/semana. Batch de grabación + edición simple.
No necesitas A para esto.

**3. A - Reescribir plataforma. NO este trimestre**
Es una trampa de fundador solo. Alto impacto futuro pero te consume todo el trimestre y no entrega valor al cliente hoy. Con 2h/día de soporte que no puedes delegar, un rewrite te deja sin soporte y sin ingresos.
Déjalo para Q siguiente y solo si B+D no mueven métricas.

**4. C - Panel de métricas. NO este trimestre**
Impacto medio y depende de A terminado. No tiene sentido planificarlo ahora. Si realmente lo necesitas, haz un MVP de métricas con lo que tienes hoy sin reescribir.

### Plan de 8 semanas realista

* **Semana 1-2:** B. Auditoría del paso 2, prototipo rápido, test con 5 usuarios, deploy.
* **Semana 3-6:** D. 10 videos. 1 día de guion/batch, 3 días de grabación, 1 día de edición/publicación.
* **Semana 7-8:** Buffer y medición. Revisa impacto de B en conversión, repite los videos que mejor funcionen y documenta el plan técnico para A en Q siguiente.

Con esto usas ~120h de tus 160h disponibles y dejas 40h de colchón para soporte que se desborde.

Regla de oro para ti como solo founder: primero lo que reduce fricción de ingresos hoy, después lo que genera demanda, y nunca un rewrite grande sin equipo.