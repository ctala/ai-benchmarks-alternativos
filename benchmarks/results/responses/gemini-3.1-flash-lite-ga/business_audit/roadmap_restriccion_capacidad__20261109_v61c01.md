# Gemini 3.1 Flash Lite (GA) — business_audit/roadmap_restriccion_capacidad

- model_id: `google/gemini-3.1-flash-lite`
- success: True  | final: 7.81 | quality: 8.0
- latency_total: 3.916s | tokens_per_second: 201.5
- input_tokens: 242 | output_tokens: 789

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

Como tu jefe de producto, mi trabajo es protegerte del "suicidio técnico" y asegurar que el trimestre cierre con crecimiento real, no con deuda técnica o promesas a medio terminar.

Tienes **120 horas de construcción real** para las próximas 8 semanas (4 horas/día * 5 días/semana * 8 semanas).

Aquí tienes la hoja de ruta priorizada basándome estrictamente en tu capacidad de 4 horas/día:

### El Plan de Acción

| Prioridad | Iniciativa | Tiempo estimado | Impacto |
| :--- | :--- | :--- | :--- |
| **1** | **B: Arreglar flujo de alta** | 1 semana (20h) | Alto |
| **2** | **D: 10 videos de contenido** | 2 semanas (40h) | Medio |
| **3** | **Buffer / Iteración** | 1 semana (20h) | N/A |
| **4** | **C: Panel de métricas (MVP)** | 3 semanas (40h) | Medio |

---

### Por qué descartamos la A (Reescritura)
**Directamente: No la hagas.**
Tienes 120 horas totales disponibles. La reescritura requiere ~360 horas (3 meses a tiempo completo). Intentar hacer esto mientras gestionas soporte te llevará al burnout y dejará tu producto actual estancado durante 3 meses. En una empresa de una sola persona, **la reescritura es el camino más rápido a la irrelevancia.** Si tu código actual funciona, optimízalo, no lo destruyas.

### Justificación del orden:

1.  **Prioridad 1 (B - El flujo de alta):** Es tu "balde agujereado". No tiene sentido traer más tráfico (videos) si pierdes al 60% de los que ya llegan. Es una victoria rápida de alto impacto que paga dividendos inmediatos en tu tasa de conversión. **Haz esto la semana 1.**
2.  **Prioridad 2 (D - Contenido):** Una vez arreglado el flujo, necesitas llenar el embudo. Los videos son activos perennes que trabajan para ti mientras duermes o haces soporte. Es el marketing de mayor apalancamiento para un fundador solo. **Semanas 2 y 3.**
3.  **Prioridad 3 (Buffer):** En tu realidad de 2 horas de soporte diario, las emergencias van a ocurrir. He asignado la **semana 4** como margen de error. Si no hay emergencias, adelanta el panel de métricas.
4.  **Prioridad 4 (C - Panel de métricas):** Como dijiste que depende de A, **aquí está la trampa:** no vas a reescribir, así que vas a construir este panel sobre tu arquitectura actual. Será un "hack" funcional. Si el esfuerzo era de 3 semanas bajo la arquitectura A, bajo la arquitectura actual debería ser de 2 semanas. **Semanas 5, 6 y 7.**

### Tu realidad de jefe de producto:
*   **Semana 8 (Cierre):** La dejamos libre para ajustes finales, corrección de bugs post-lanzamiento de las métricas y cierre de trimestre.
*   **Regla de oro:** Si el soporte diario sube a 3 horas, **se recorta el alcance de C**, nunca el tiempo de B o D.

**¿Estás de acuerdo con ignorar la reescritura (A) para salvar el trimestre o sientes que el framework actual te impide sobrevivir?**