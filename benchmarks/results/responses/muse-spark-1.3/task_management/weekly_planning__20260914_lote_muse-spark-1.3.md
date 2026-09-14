# Muse Spark 1.3 — task_management/weekly_planning

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.39 | quality: 10.0
- latency_total: 37.494s | tokens_per_second: 161.7
- input_tokens: 193 | output_tokens: 6061
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un plan semanal detallado que se ajusta perfectamente a las restricciones y tareas dadas.

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

Aquí tienes un plan semanal optimizado para tu energía y tus deadlines. Asumo jornada de 9:00 a 18:00 con almuerzo de 1-2 PM.

La lógica que usé:
1.  **La demo manda:** La presentación de 3h tiene que estar lista el martes, no el miércoles.
2.  **Martes = Maker Day:** Como lo tienes libre, lo reservamos para deep work (presentación + OKRs).
3.  **Lunes fragmentado = tareas ligeras:** No pongas deep work entre reunión y almuerzo con cliente.
4.  **Emails siempre a primera hora:** Para hacer inbox-zero y no arrastrarlos.

### LUNES - Día fragmentado, modo ligero
> 9:00 - 11:00 Reunión de directivos [BLOQUEADO]
> **11:00 - 12:00 Responder emails stakeholders (1h)**
> **12:00 - 13:00 Revisar métricas del producto (1h)**
> *Tip: Hazlo el lunes, así usas los datos frescos en la reunión de directivos y en la demo.*
> 13:00 - 14:00 Almuerzo con cliente [BLOQUEADO]
> **14:00 - 14:30 One-on-one Reporte #1**
> **14:30 - 15:00 One-on-one Reporte #2**
> **15:00 - 16:30 Preparar presentación demo - Parte 1/2 (1.5h)**
> Enfócate solo en storyline y estructura. No diseñes slides aún.
> 16:30 - 18:00 Buffer / admin ligero / preparar martes

### MARTES - Deep Work, sin reuniones
> **9:00 - 10:00 Responder emails stakeholders (1h)**
> **10:00 - 11:30 Preparar presentación demo - Parte 2/2 (1.5h)**
> Diseño, pulir y ensayar en voz alta. **A las 11:30 la presentación queda LISTA.**
> 11:30 - 13:00 Buffer estratégico: ensaya 30 min más y deja todo cerrado para el miércoles
> 13:00 - 14:00 Almuerzo
> **14:00 - 16:00 Escribir OKRs Q3 - Parte 1/2 (2h)**
> Bloque de foco total: notificaciones off, solo borrador de Objetivos. No busques perfección.
> 16:00 - 18:00 Tiempo protegido libre. No agendes nada. Úsalo si te atascaste o para salir temprano.

### MIÉRCOLES - Día Demo
> **9:00 - 10:00 Responder emails stakeholders (1h)**
> 10:00 - 11:30 Repaso final presentación + prueba técnica (no es trabajo extra, es ensayo)
> **11:30 - 12:00 One-on-one Reporte #3**
> Lo pongo aquí porque es un día de mañana tranquila, ideal para un 1:1.
> 12:00 - 13:00 Almuerzo temprano y desconexión
> 13:00 - 15:00 Bloque pre-demo: check técnico, repaso mental, llegar con calma
> 15:00 - 16:00 Demo de producto [BLOQUEADO]
> 16:00 - 18:00 Post-demo: apunta notas, follow-ups y feedback mientras está fresco

### JUEVES - Personas por la mañana, foco por la tarde
> **9:00 - 10:00 Responder emails stakeholders (1h)**
> 10:00 - 13:00 Entrevistas de hiring [BLOQUEADO]
> 13:00 - 14:00 Almuerzo + descanso real (lo necesitarás después de 3h de entrevistas)
> **14:00 - 16:00 Escribir OKRs Q3 - Parte 2/2 (2h)**
> Cierra Key Results, métricas y redactado final. Con esto completas las 4h.
> 16:00 - 18:00 Trabajo ligero: responder follow-ups de la demo, Slack, preparar retro

### VIERNES - Cierre y feedback a devs
> **9:00 - 10:00 Responder emails stakeholders (1h)**
> **10:00 - 12:00 Revisar PRDs pendientes (2h)**
> Perfecto para el viernes: les das feedback a los devs antes del finde en un solo bloque de foco.
> 12:00 - 13:00 Planificación semana siguiente + inbox zero
> 13:00 - 14:00 Almuerzo
> 14:00 - 16:00 Buffer para imprevistos / cerrar loops de la semana
> 16:00 - 17:00 Retrospectiva [BLOQUEADO]
> 17:00 - 17:30 Cierre semanal: ¿qué quedó pendiente?

**Verificación de que todo cabe:**
* Presentación: 1.5h (Lun) + 1.5h (Mar) = 3h ✓
* OKRs: 2h (Mar) + 2h (Jue) = 4h ✓
* PRDs: 2h (Vie) = 2h ✓
* Métricas: 1h (Lun) = 1h ✓
* 1:1s: 2x30 (Lun) + 1x30 (Mié) = 1.5h ✓
* Emails: 1h x 5 días = 5h ✓

¿Quieres que te lo pase en formato para copiar/pegar en Google Calendar?