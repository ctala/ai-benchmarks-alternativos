# Gemini 3.7 Flash — business_audit/roadmap_restriccion_capacidad

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 8.83 | quality: 10.0
- latency_total: 13.524s | tokens_per_second: 100.6
- input_tokens: 242 | output_tokens: 1361

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

Tu capacidad real para este trimestre no son 8 semanas: son **160 horas de construcción** (8 semanas × 5 días × 4h/día). Esto equivale a solo **4 semanas de trabajo a tiempo completo**.

Con esos números en la mano, esta es tu realidad y el plan de ejecución:

---

### Lo que se descarta de inmediato

* **DESCARTADO: A) Reescribir la plataforma**
  * **Por qué:** Pide ~3 meses a tiempo completo (~480 horas). Tienes 160 horas. Si lo intentas, terminarás el trimestre con el código a medias, sin lanzar nada, frustrado y con la plataforma vieja igual de rota.
* **DESCARTADO: C) Panel de métricas**
  * **Por qué:** Depende de A (que no harás) y consumiría 120 de tus 160 horas disponibles. Cero margen de error.

---

### Tu plan de trimestre (Las 8 semanas)

Tu único foco debe ser: **tapar la fuga de dinero y luego meterle gente.**

#### **Fase 1: Semanas 1 y 2 (40 horas) → Iniciativa B (Arreglar el alta)**
* **Por qué primero:** Tienes un cubo agujereado perdiendo el 60% de los usuarios. Cualquier esfuerzo de marketing hoy es tirar el dinero.
* **Estimación real:** 1 semana a tiempo completo = 2 semanas a tu ritmo de 4h/día.
* **Meta:** Reducir la caída del paso 2 al menos a la mitad y medir el impacto directo en altas completadas.

#### **Fase 2: Semanas 3 a 6 (80 horas) → Iniciativa D (10 Videos de contenido)**
* **Por qué segundo:** Ahora que el embudo no pierde al 60% de la gente, tiene sentido atraer tráfico.
* **Estimación real:** 2 semanas a tiempo completo = 4 semanas a tu ritmo de 4h/día.
* **Consejo de solo founder:** No grabes y edites uno por uno. Agrupa por bloques: Semana 3 (guiones de los 10), Semana 4 (grabación en bloque), Semanas 5 y 6 (edición y programación).

#### **Fase 3: Semanas 7 y 8 (40 horas) → Buffer / Deuda técnica quirúrgica**
* **Qué hacer aquí:** **NO agregues features nuevas.**
* Utiliza estas 40 horas para:
  1. Atender los bugs que surjan de B y el tráfico de D.
  2. Automatizar o crear documentación para las partes más repetitivas de tus 2h diarias de soporte (para intentar liberar 30 min/día el próximo trimestre).
  3. Resolver *solamente* los cuellos de botella críticos de rendimiento del framework actual (parches, no reescritura).

---

### Resumen ejecutivo
1. **Semanas 1-2:** Arregla el alta (B).
2. **Semanas 3-6:** Produce los 10 videos (D).
3. **Semanas 7-8:** Margen de seguridad y optimización de soporte.
4. **A y C:** Fuera del roadmap hasta que tengas ingresos para contratar o capacidad real liberada.