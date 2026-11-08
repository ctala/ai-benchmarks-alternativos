# Tencent Hy3 — business_audit/roadmap_restriccion_capacidad

- model_id: `tencent/hy3`
- success: True  | final: 8.68 | quality: 10.0
- latency_total: 83.827s | tokens_per_second: 59.5
- input_tokens: 302 | output_tokens: 4991

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

Como PM de tu empresa de una sola persona, mi primer trabajo es proteger tu tiempo y evitar que quemes el trimestre en algo que no vas a terminar. Vamos a los hechos con la capacidad real:

### 1. El filtro de realidad (Capacidad vs. Esfuerzo)
*   **Tu capacidad real de construcción:** 8 semanas x 4h/día = ~160h (si haces 5 días) o ~224h (si haces 7).
*   **Iniciativa A (Reescribir):** 3 meses a tiempo completo = ~480-600h. **Es matemáticamente imposible.** Empezarla es firmar una deuda técnica a medias y estrés garantizado para ti.
*   **Iniciativa C (Panel):** Depende de A. Si A no se hace, C no existe. Queda bloqueada por dependencia.

### 2. El plan de ejecución (Lo que SÍ haces)

**Semanas 1-2: Iniciativa B (Arreglar el flujo de alta) -> PRIORIDAD #1**
*   **Por qué:** Tienes un agujero del 60% en el paso 2. Es como llenar una bañera con el tapón abierto. Es el único *Quick Win* de impacto alto que tienes.
*   **Esfuerzo:** ~1 semana real de trabajo (posiblemente 2 semanas calendario a tus 4h/día). Hazlo primero, pásalo a producción y testéalo bien.

**Semanas 3-6: Iniciativa D (10 videos de contenido) -> PRIORIDAD #2**
*   **Por qué:** Impacto medio, pero necesario para tracción. Solo tiene sentido hacerlo *después* de B: si no arreglas el alta, los leads que generen los videos se van a seguir perdiendo en el paso 2.
*   **Esfuerzo:** ~2 semanas reales (4 semanas calendario a tu ritmo de 4h/día).

**Semanas 7-8: El tiempo sobrante (Iteración, no reescritura)**
*   Dependiendo de si tus estimaciones de B y D son a tiempo completo o a tu tiempo parcial, te van a quedar entre 2 y 4 semanas libres al final del trimestre.
*   **Qué hacer:** **NO empieces A.** Usa ese tiempo para pulir el resto del funnel (B fase 2) o hacer más contenido (escalar D). Si quieres tocar código, haz refactors quirúrgicos en tu framework actual para aliviar dolores puntuales, no una reescritura total.

### Resumen de priorización del trimestre:
1.  **B** (Alta impacto, viable, desbloquea ingresos de inmediato).
2.  **D** (Media impacto, viable, alimenta el funnel ya arreglado).
3.  **Descartar A** (Inviables en 8 semanas con 4h/día).
4.  **Descartar C** (Bloqueada por A).