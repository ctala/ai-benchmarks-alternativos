# GLM 5.2 — business_audit/roadmap_restriccion_capacidad

- model_id: `z-ai/glm-5.2`
- success: True  | final: 7.17 | quality: 8.0
- latency_total: 28.387s | tokens_per_second: 76.4
- input_tokens: 263 | output_tokens: 2170

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

Como tu Jefe de Producto, mi trabajo es protegerte de ti mismo. Los fundadores solos tienden a planificar como si tuvieran un equipo de 5 personas, y luego se frustran cuando no llegan a las metas. 

Vamos a hacer las matemáticas de la realidad primero:
*   Tienes **8 semanas** hasta fin de trimestre.
*   Tienes **4 horas diáticas** para construir (20 horas a la semana).
*   Capacidad real total: **160 horas** (equivalente a 4 semanas a tiempo completo de 40h).

Con esa capacidad en mente, aquí tienes el veredicto y el plan del trimestre:

### Veredicto: Qué entra y qué se queda fuera

*   **A (Reescribir plataforma): FUERA.** Requiere 3 meses a tiempo completo (unas 480 horas). Tú tienes 160. Si empiezas esto, en 8 semanas tendrás una plataforma mitad vieja y mitad nueva, rota, y sin tiempo para arreglarla. Es una trampa mortal para un solo fundador.
*   **C (Panel de métricas): FUERA.** Depende de A. Como A no entra, C tampoco. Además, no vamos a bloquear 3 semanas de tu trimestre por algo de impacto "medio" con dependencias.
*   **B (Arreglar flujo de alta): ENTRA.** Impacto alto, pierdes al 60% de tus usuarios. Es tu mayor sangría actual. Esfuerzo mínimo. Prioridad absoluta.
*   **D (Grabar 10 videos): ENTRA.** Impacto medio, pero es esfuerzo contenido y no tiene dependencias. Genera tráfico y autoridad mientras duermes.

---

### El Plan del Trimestre (8 Semanas)

**Semana 1: B (Arreglar flujo de alta)**
*   Dedica tus 20 horas de esta semana a diagnosticar y solucionar el paso 2. 
*   *Objetivo:* Reducir la caída del 60% a algo razonable (ej. 30%). Cada usuario que se salve aquí es dinero/crecimiento directa para el negocio.

**Semanas 2 y 3: D (Grabar 10 videos)**
*   Con el flujo de alta arreglado, ahora nos enfocamos en atraer más gente a la parte superior del embudo.
*   *Objetivo:* Grabar, editar y programar/publicar 10 videos. No perfeccionismos, contenido útil y rápido.

**Semanas 4 a 8: Preparación estratégica y Quick Wins (5 semanas)**
Aquí es donde un buen PM marca la diferencia. Tienes 100 horas de capacidad disponible. No vamos a tocar A todavía, pero vamos a usar este tiempo para asegurar que el *próximo* trimestre sea un éxito y este no se desperdicie:

1.  **Spike de Arquitectura (Semana 4):** Dedica 20 horas a planificar la reescritura (A). No escribas código de producción. Haz diagramas, define la estructura de la base de datos, decide qué se mueve primero. Un plan de 3 meses requiere al menos 1 semana de diseño técnico para no fracasar.
2.  **Quick Wins de Retención (Semanas 5-6):** Ya no pierdes tanta gente en el alta (gracias a B). Ahora, mira los datos: ¿dónde se pierde la gente *después* de registrarse? Usa estas 40 horas para arreglar 2 o 3 cosas pequeñas que retengan a los usuarios que ya entraron.
3.  **Buffer y Deuda Técnica (Semanas 7-8):** Reserva este tiempo. Siempre surgen bugs, el soporte puede subir, o necesitarás iterar sobre los cambios del flujo de alta. Si sobra tiempo, paga deuda técnica menor que facilite la futura reescritura (A).

### Resumen de la orden del PM:
No empieces la reescritura. Arregla el embudo hoy (B), crea el contenido para llenarlo mañana (D), y usa el resto del trimestre para preparar el terreno para que el próximo trimestre puedas ejecutar la reescritura (A) sin que el negocio se muera en el intento.