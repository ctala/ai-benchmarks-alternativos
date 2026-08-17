# Gemini 3.7 Flash — business_audit/roadmap_restriccion_capacidad

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 8.81 | quality: 10.0
- latency_total: 14.687s | tokens_per_second: 106.4
- input_tokens: 242 | output_tokens: 1562

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

Tu presupuesto real para construir este trimestre es de **160 horas** (8 semanas × 5 días × 4h). 

Cualquier estimación en "tiempo completo" (asumiendo 8h/día) a ti te cuesta el **doble de semanas calendario**. Con esa realidad sobre la mesa, aquí tienes el orden de tu trimestre:

---

### Lo que NO vas a hacer (y por qué)

*   **A (Reescritura): DESCARTADA.** Te tomaría unas 480 horas (~6 meses a tu ritmo actual). Si te metes aquí, congelas el negocio medio año y te quemas. La reescritura es un lujo que un fundador solo no se puede permitir sin tracción validada.
*   **C (Panel de métricas): DESCARTADA.** Depende de A, por lo que queda bloqueada automáticamente. Además, impacto medio frente a resolver la adquisición/activación no justifica el esfuerzo ahora.

---

### El plan de 8 semanas

#### 1. Prioridad Absoluta: Iniciativa B (Arreglar el flujo de alta)
* **Tiempo estimado:** Semanas 1 y 2 (~40 horas).
* **Por qué:** Tienes un agujero en el barco donde pierdes al 60% de los usuarios. Cualquier esfuerzo de marketing o soporte es tirar el tiempo si la gente no pasa del paso 2. Es la victoria más rápida y de mayor ROI.

#### 2. Prioridad Secundaria: Iniciativa D (10 videos de contenido)
* **Tiempo estimado:** Semanas 3 a 6 (~80 horas).
* **Por qué:** Ahora que el embudo no pierde al 60% en el paso 2, tiene sentido meter tráfico nuevo. No grabes los 10 de golpe: produce, edita y publica en bloques de 2 o 3 para medir si realmente atraen clientes antes de gastar las 80 horas completas.

#### 3. Prioridad Oculta: Buffer y Reducción de Operación
* **Tiempo estimado:** Semanas 7 y 8 (~40 horas).
* **Por qué:** 
  1. Las estimaciones siempre se desvían (imprevistos de soporte te van a comer horas).
  2. **Objetivo estratégico:** Usa el tiempo sobrante para documentar FAQs, crear respuestas automáticas o mejorar procesos internos. Si bajas esas 2h de soporte a 1h/día, habrás ganado un 25% más de capacidad de desarrollo para el próximo trimestre.

---

### Resumen del Trimestre
* **Semanas 1-2:** Arreglar y validar el paso 2 del alta (Iniciativa B).
* **Semanas 3-6:** Crear y distribuir contenido (Iniciativa D, iterando en lotes).
* **Semanas 7-8:** Margen para imprevistos + automatizar soporte para comprar tiempo futuro.
* **Iniciativas A y C:** Archivadas hasta nuevo aviso.