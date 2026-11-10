# Gemini 3.1 Flash Lite (GA) — task_management/weekly_planning

- model_id: `google/gemini-3.1-flash-lite`
- success: True  | final: 9.19 | quality: 10.0
- latency_total: 4.302s | tokens_per_second: 202.7
- input_tokens: 199 | output_tokens: 872
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, ofreciendo una planificación detallada y estratégica que un product manager podría implementar directamente.

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

Como Product Manager, tu agenda requiere equilibrar el trabajo profundo (*deep work*) con la gestión de expectativas. He estructurado tu semana priorizando las tareas de mayor carga cognitiva (OKRs y PRDs) en tus bloques de mayor disponibilidad, y dejando los correos como "anclas" de inicio o fin de jornada.

Aquí tienes tu plan semanal optimizado:

### Resumen de disponibilidad
*   **Total horas disponibles:** 30 horas hábiles (descontando reuniones fijas).
*   **Total horas de tareas:** 14.5 horas.
*   **Buffer:** 15.5 horas (para imprevistos, reuniones ad-hoc y slack).

---

### Planificación Semanal

| Día | Bloque AM | Bloque PM |
| :--- | :--- | :--- |
| **Lunes** | 9-11: Reunión Directivos | 1-2: Almuerzo Cliente / 2-3: Emails |
| **Martes** | 9-1: **Escribir OKRs Q3** (4h) | 2-4: **Preparar Demo** (2h) / 4-5: Emails |
| **Miércoles** | 9-11: **Revisar PRDs** (2h) / 11-12: **Métricas** (1h) | 1-3: 1:1s (1.5h) + Emails / 3-4: **Demo** |
| **Jueves** | 10-1: **Entrevistas Hiring** | 2-3: **Preparar Demo** (1h) / 3-4: Emails |
| **Viernes** | 9-11: Buffer / Admin | 1-4: Buffer / Admin / 4-5: **Retrospectiva** |

---

### Detalles de la Estrategia:

1.  **Bloques de "Deep Work" (OKRs y PRDs):**
    *   Los **Martes** son tu día de oro. He asignado las 4 horas completas de los OKRs a la mañana, cuando tu energía mental está al máximo.
    *   Los **Miércoles** antes de la demo, cierras los PRDs y revisas métricas para estar bien preparado para cualquier pregunta técnica.

2.  **Preparación de la Demo:**
    *   Dividí las 3 horas en dos bloques: 2 horas el martes (estructura y contenido) y 1 hora el jueves (refinamiento final y pruebas). Esto te permite iterar después de haber descansado.

3.  **Gestión de Stakeholders (Emails):**
    *   He asignado 1 hora diaria al final de la tarde (o justo después de almuerzo). Esto evita que el inbox dicte tu agenda durante las horas de mayor productividad.

4.  **One-on-Ones:**
    *   Agrupados el miércoles después de la demo. Al ser 30 minutos cada uno, tendrás 1.5 horas totales. He dejado un margen de 30 minutos extra ese bloque para gestionar cualquier urgencia post-demo antes de cerrar el día.

5.  **Buffer (Viernes):**
    *   El viernes está intencionalmente ligero. Como PM, siempre surgen incendios o peticiones urgentes de ingeniería/diseño. Usar el viernes como bloque de "limpieza" te permitirá cerrar la semana sin pendientes acumulados.

### Consejos adicionales:
*   **Bloquea tu calendario:** Marca estas tareas como "Ocupado" para que nadie agende encima.
*   **Modo enfoque:** Durante los bloques de OKRs y PRDs, desactiva notificaciones de Slack/Teams. Son tareas que requieren flujo creativo.
*   **Flexibilidad:** Si el lunes surge una emergencia, mueve el bloque de "Revisar Métricas" al jueves por la tarde, ya que el jueves es tu día más flexible después de las entrevistas.