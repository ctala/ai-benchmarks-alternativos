# Gemini 4 Argon — task_management/weekly_planning

- model_id: `google/gemini-4-argon`
- success: True  | final: 8.2 | quality: 9.8
- latency_total: 23.57s | tokens_per_second: 64.7
- input_tokens: 225 | output_tokens: 1524
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un plan semanal detallado que se ajusta perfectamente a las restricciones y necesidades del product manager.

## Entrada exacta (lo que recibió el modelo)

**user:**

Soy product manager. Mi semana tiene estas restricciones:
- Lunes: reunion de directivos 9-11 AM, almuerzo con cliente 1-2 PM
- Martes: libre todo el dia
- Miercoles: demo de producto 3-4 PM
- Jueves: entrevistas de hiring 10 AM - 1 PM
- Viernes: retrospectiva 4-5 PM

Necesito meter estas tareas en la semana:
1. Preparar presentacion para la demo (3 horas)
2. Revisar PRDs pendientes (2 horas)
3. Escribir OKRs Q3 (4 horas)
4. Responder emails de stakeholders (1 hora diaria)
5. Revisar metricas del producto (1 hora)
6. One-on-one con 3 reportes directos (30 min cada uno)

Crea un plan semanal detallado con bloques de tiempo especificos.


## Respuesta completa

Como Product Manager, la clave de tu semana es proteger los bloques de "trabajo profundo" (como escribir los OKRs y preparar la demo) y agrupar las reuniones operativas. 

Aquí tienes una propuesta de calendario optimizada asumiendo una jornada estándar de **9:00 AM a 5:00 PM**, dejando siempre 1 hora para almorzar y espacios libres (buffers) para imprevistos o trabajo ad-hoc que siempre surge en producto.

### Estrategia aplicada:
*   **Trabajo profundo por las mañanas:**Aprovechamos el martes y miércoles temprano para las tareas más pesadas (Demo y OKRs).
*   **Emails por la tarde:** Puse la hora de responder emails al final del día (excepto el viernes) para evitar que empieces la mañana de forma reactiva.
*   **1-on-1s agrupados:** Los puse juntos el jueves por la tarde, ya que tu mente ya estará en "modo conversación" después de las entrevistas de la mañana.

---

### 📅 Plan Semanal Detallado

#### **Lunes: Alineación y Métricas**
*El objetivo de hoy es sobrevivir a las reuniones largas y entender cómo está el producto antes de planificar la semana.*
*   **09:00 - 11:00:** 🔴 Reunión de directivos (Restricción)
*   **11:00 - 12:00:** ✅ **Revisar métricas del producto (1h)** - *Ideal hacerlo después de ver a los directivos para tener contexto fresco.*
*   **12:00 - 13:00:** *Buffer / Preparación para el almuerzo y traslado*
*   **13:00 - 14:00:** 🔴 Almuerzo con cliente (Restricción)
*   **14:00 - 16:00:** *Tiempo libre para trabajo ad-hoc / Slack / Seguimiento del cliente*
*   **16:00 - 17:00:** ✅ **Responder emails de stakeholders (1h)**

#### **Martes: Día de Foco Profundo (Deep Work)**
*Aprovechamos tu día libre de reuniones para avanzar en los entregables más pesados.*
*   **09:00 - 12:00:** ✅ **Preparar presentación para la demo (3h)** - *Hacerlo hoy te deja 24 horas de margen antes de la demo real para iterar si algo falla.*
*   **12:00 - 13:00:** *Buffer / Tareas menores*
*   **13:00 - 14:00:** 🥗 Almuerzo
*   **14:00 - 16:00:** ✅ **Revisar PRDs pendientes (2h)** - *Para no bloquear al equipo de ingeniería/diseño.*
*   **16:00 - 17:00:** ✅ **Responder emails de stakeholders (1h)**

#### **Miércoles: Estrategia y Día de Demo**
*Mañana estratégica y tarde de ejecución.*
*   **09:00 - 13:00:** ✅ **Escribir OKRs Q3 (4h)** - *Bloque ininterrumpido. Te recomiendo apagar Slack durante estas 4 horas.*
*   **13:00 - 14:00:** 🥗 Almuerzo
*   **14:00 - 15:00:** *Buffer / Ensayo final y setup técnico para la Demo*
*   **15:00 - 16:00:** 🔴 Demo de producto (Restricción)
*   **16:00 - 17:00:** ✅ **Responder emails de stakeholders (1h)** - *Aprovecha para enviar el seguimiento de la demo.*

#### **Jueves: Día de Personas (Hiring & Equipo)**
*Hoy es un día de alta carga social. No programamos tareas analíticas pesadas.*
*   **09:00 - 10:00:** ✅ **Responder emails de stakeholders (1h)** - *Adelantamos esto a la mañana para limpiar la bandeja antes de las entrevistas.*
*   **10:00 - 13:00:** 🔴 Entrevistas de hiring (Restricción)
*   **13:00 - 14:00:** 🥗 Almuerzo (¡Descansa la voz!)
*   **14:00 - 14:30:** *Buffer / Escribir feedback de los candidatos entrevistados*
*   **14:30 - 15:00:** ✅ **One-on-one: Reporte Directo 1 (30m)**
*   **15:00 - 15:30:** ✅ **One-on-one: Reporte Directo 2 (30m)**
*   **15:30 - 16:00:** *Descanso de 30 min entre reuniones*
*   **16:00 - 16:30:** ✅ **One-on-one: Reporte Directo 3 (30m)**
*   **16:30 - 17:00:** *Cierre del día / Slack*

#### **Viernes: Cierre y Mejora Continua**
*El trabajo pesado ya está hecho. Si algo se atrasó en la semana, tienes la mañana del viernes para recuperarte.*
*   **09:00 - 13:00:** *Bloque flexible: Tiempo para imprevistos, refinar los OKRs, o trabajar en el backlog.*
*   **13:00 - 14:00:** 🥗 Almuerzo
*   **14:00 - 15:00:** *Planificación de la próxima semana / Limpieza de Jira o Linear*
*   **15:00 - 16:00:** ✅ **Responder emails de stakeholders (1h)** - *Dejas todo limpio antes de la retro.*
*   **16:00 - 17:00:** 🔴 Retrospectiva (Restricción) - *Excelente forma de cerrar la semana con el equipo.*

### Resumen de cumplimiento:
*   [x] **Demo (3h):** Martes AM.
*   [x] **PRDs (2h):** Martes PM.
*   [x] **OKRs (4h):** Miércoles AM.
*   [x] **Emails (1h/día):** Lunes, Martes, Miércoles (4pm), Jueves (9am), Viernes (3pm).
*   [x] **Métricas (1h):** Lunes AM.
*   [x] **1-on-1s (1.5h total):** Jueves PM.