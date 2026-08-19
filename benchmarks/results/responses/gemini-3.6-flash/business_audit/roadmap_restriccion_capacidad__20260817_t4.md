# Gemini 3.6 Flash — business_audit/roadmap_restriccion_capacidad

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 8.61 | quality: 10.0
- latency_total: 14.286s | tokens_per_second: 155.9
- input_tokens: 244 | output_tokens: 2227

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

Como tu Jefe de Producto, mi trabajo es proteger tu recurso más escaso: **tus 20 horas semanales de construcción** (4h/día x 5 días).

En 8 semanas tienes un total de **160 horas reales de capacidad**. Cualquier plan que asuma 161 horas es una fantasía que te llevará al *burnout*.

Aquí tienes el diagnóstico frío y el orden del trimestre:

---

### Diagnóstico de Iniciativas

*   **A) Reescribir la plataforma:** **CANCELADA.** Es una trampa mortal de solo-founder. 3 meses a tiempo completo son ~480 horas. A tu ritmo actual te llevaría **medio año** sin sacar nada nuevo. Si la empresa no se cae a pedazos hoy, se queda como está.
*   **B) Arreglar el flujo de alta:** **PRIORIDAD 1.** Tienes un cubo con un agujero por el que se te cae el 60% del agua. Arreglar esto multiplica el retorno de cualquier esfuerzo de marketing posterior.
*   **C) Panel de métricas:** **BLOQUEADA.** Si depende de A y A no se hace, C se cae. *Nota: Si más adelante descubrimos que se puede hacer una versión "mínima" en la plataforma actual, la reevaluamos.*
*   **D) 10 videos de contenido:** **PRIORIDAD 2.** Genera demanda, pero no mandes tráfico a un producto que pierde al 60% de los usuarios. Se hace *después* de B.

---

### Tu Trimestre (Semana a Semana)

#### **Semana 1: Tapa el agujero (Iniciativa B)**
*   **Objetivo:** Reducir la caída del paso 2 de alta.
*   **Capacidad usada:** 20 horas.
*   **Por qué:** Es la tarea con mayor ROI inmediato. Si entra gente esta semana, que no se vaya.

#### **Semanas 2 y 3: Captación (Iniciativa D)**
*   **Objetivo:** Grabar y editar los 10 videos.
*   **Capacidad usada:** 40 horas.
*   **Por qué:** Ahora que el onboarding funciona (o pierde mucho menos), llenamos el embudo con el contenido.

#### **Semanas 4, 5 y 6: Versión "Desarmada" de C (O Iteración de B)**
*   **Objetivo:** Evaluar si puedes hacer un panel de métricas *extremadamente básico* en el framework actual sin reescribir nada.
*   **Capacidad usada:** 60 horas.
*   **Por qué:** Da valor a los clientes actuales. Si descubres que requiere reescribir la base de datos, abortas y dedicas este tiempo a pulir las ventas/operación.

#### **Semanas 7 y 8: BUFFER REALISTA (Margen de maniobra)**
*   **Objetivo:** Absorber el caos.
*   **Capacidad usada:** 40 horas.
*   **Por qué:** Eres solo-founder. El soporte va a aumentar, te vas a poner enfermo un par de días, o una actualización va a romper algo. Si no planificas semanas vacías, tu trimestre fracasa en la primera interrupción.

---

### Tu orden de ejecución para hoy mismo:

1.  **Olvida la reescritura (Iniciativa A).** Quítatela de la cabeza, no hay presupuesto de tiempo.
2.  **Abre el código hoy y mira solo el paso 2 del alta.** Tu único objetivo este viernes es que ese 60% de pérdida baje, aunque sea, al 30%.