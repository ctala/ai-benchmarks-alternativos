# GLM-5.1 — task_management/weekly_planning

- model_id: `z-ai/glm-5.1`
- success: True  | final: 8.58 | quality: 10.0
- latency_total: 24.575s | tokens_per_second: 58.4
- input_tokens: 205 | output_tokens: 1436
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y ofrece una estructura detallada y útil para la planificación semanal, con una clara consideración de las restricciones y necesidades del product manager.

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

Como Product Manager, la clave para ser productivo es agrupar tareas similares (batching) y proteger tus bloques de tiempo profundo (deep work). 

Aquí tienes el análisis de tu capacidad y el plan semanal detallado.

### 📊 Análisis de capacidad
*   **Horas fijas (reuniones/obligaciones):** 11 horas en total.
*   **Horas de tareas a meter:** 19 horas en total (3h demo + 2h PRDs + 4h OKRs + 5h emails + 1h métricas + 1.5h 1-on-1s).
*   **Estrategia:** El **martes es tu día más valioso**. Lo usaremos para el "Deep Work" (OKRs y PRDs). Prepararemos la demo el martes y miércoles por la mañana para que esté fresca. Las métricas y los 1-on-1s los colocaremos estratégicamente alrededor de tus reuniones fijas.

---

### 🗓️ Plan Semanal Detallado

#### **Lunes (Día de alineación y contexto)**
*Tu semana arranca con reuniones de alto nivel. El objetivo es salir de ellas con contexto para alimentar tu trabajo profundo del martes.*
*   **08:00 - 09:00 AM:** Responder emails de stakeholders (1h).
*   **09:00 - 11:00 AM:** 🔴 *Reunión de directivos* (Restricción).
*   **11:00 AM - 01:00 PM:** Buffer post-reunión / Tareas operativas rápidas derivadas de la reunión.
*   **01:00 - 02:00 PM:** 🔴 *Almuerzo con cliente* (Restricción).
*   **02:00 - 03:00 PM:** Revisar métricas del producto (1h). *Ideal hacerlo hoy para saber cómo va el trimestre antes de pensar en los OKRs.*
*   **03:00 - 04:30 PM:** One-on-one con Reporte Directo #1 (30 min) y Reporte Directo #2 (30 min), con 30 min de buffer para anotar action items.

#### **Martes (Día de Deep Work - Sin interrupciones)**
*Tienes el día libre de reuniones. Es tu día para pensar estratégicamente y crear.*
*   **09:00 - 10:00 AM:** Responder emails de stakeholders (1h).
*   **10:00 AM - 01:00 PM:** 🟢 Escribir OKRs Q3 (3 horas - Bloque 1). *Tu cerebro está fresco para estrategia.*
*   **01:00 - 02:00 PM:** *Almuerzo y desconexión.*
*   **02:00 - 03:00 PM:** 🟢 Escribir OKRs Q3 (1 hora - Bloque 2). *Cierre de OKRs.*
*   **03:00 - 05:00 PM:** 🟢 Preparar presentación para la demo (2 horas - Bloque 1). *Avance estructural de la presentación.*

#### **Miércoles (Enfoque en Producto y Demo)**
*Día de asegurar que todo lo que se mostrará al cliente/equipo esté perfecto.*
*   **09:00 - 10:00 AM:** Responder emails de stakeholders (1h).
*   **10:00 AM - 01:00 PM:** Revisar PRDs pendientes (2 horas) + 1 hora de buffer para ajustes con el equipo de diseño/ingeniería si surgen dudas.
*   **01:00 - 02:00 PM:** *Almuerzo.*
*   **02:00 - 03:00 PM:** 🟢 Preparar presentación para la demo (1 hora - Bloque 2). *Pulido final y ensayo.*
*   **03:00 - 04:00 PM:** 🔴 *Demo de producto* (Restricción).
*   **04:00 - 04:30 PM:** One-on-one con Reporte Directo #3 (30 min). *Perfecto para finales de semana para ver el progreso de la semana.*

#### **Jueves (Día de Crecimiento / Hiring)**
*Tienes un bloque grande de entrevistas. Evita meter tareas que requieran mucho foco entre ellas.*
*   **09:00 - 10:00 AM:** Responder emails de stakeholders (1h).
*   **10:00 AM - 01:00 PM:** 🔴 *Entrevistas de hiring* (Restricción).
*   **01:00 - 02:00 PM:** *Almuerzo.*
*   **02:00 - 04:00 PM:** Revisar PRDs pendientes (Tiempo restante para completar las 2h en total de la semana) y/o Debriefs de las entrevistas de la mañana.

#### **Viernes (Cierre y Retrospectiva)**
*Día de atar cabos sueltos, documentar aprendizajes y cerrar la semana.*
*   **09:00 - 10:00 AM:** Responder emails de stakeholders (1h). *Última revisión de la semana.*
*   **10:00 AM - 01:00 PM:** Tiempo buffer para imprevistos, deudas de reuniones de la semana, o adelantar trabajo de la próxima semana.
*   **01:00 - 02:00 PM:** *Almuerzo.*
*   **02:00 - 04:00 PM:** Tiempo libre / Trabajo asíncrono (documentar decisiones tomadas en la semana).
*   **04:00 - 05:00 PM:** 🔴 *Retrospectiva* (Restricción).

---

### 💡 Consejos extra para este plan:
1. **Protege tu martes:** Al ser tu único día libre, es tentador aceptar reuniones rápidas ("¿tienes 15 min?"). Declina todas o regrésalas al jueves por la tarde.
2. **Gestión de Emails:** Si te fijas, metí el bloque de 1 hora de correos a primera hora todos los días. Si terminas antes, usa ese tiempo extra para tomar café o prepararte para la siguiente reunión, pero no abras correos el resto del día.
3. **Preparación de la Demo:** Dividí las 3 horas en 2 horas el martes (estructura) y 1 hora el miércoles (pulido). Así no llegas agotado mentalmente al momento de armar la presentación.