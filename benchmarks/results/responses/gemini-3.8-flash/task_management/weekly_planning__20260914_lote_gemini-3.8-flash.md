# Gemini 3.8 Flash — task_management/weekly_planning

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.49 | quality: 10.0
- latency_total: 26.137s | tokens_per_second: 157.1
- input_tokens: 199 | output_tokens: 4107
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

Para optimizar tu semana como Product Manager, el plan aplica principios de **Deep Work** (aprovechando el martes despejado), agrupa reuniones similares para reducir el cambio de contexto y asegura que la preparación de la demo quede lista antes del miércoles.

Asumimos una jornada estándar de **9:00 AM a 6:00 PM**.

---

### **Lunes**
*Foco: Alineación estratégica y contexto semanal*
* **09:00 - 11:00 AM | [Fijo] Reunión de directivos**
* **11:00 - 12:00 PM | Responder emails de stakeholders (1h)** *(Clave para responder de inmediato a prioridades surgidas de la reunión directiva)*
* **12:00 - 01:00 PM |** Buffer / Procesamiento de notas y priorización semanal
* **01:00 - 02:00 PM | [Fijo] Almuerzo con cliente**
* **02:00 - 03:00 PM | Revisar métricas del producto (1h)** *(Ideal en lunes para arrancar la semana con visibilidad del rendimiento)*
* **03:00 - 05:00 PM |** Tiempo de soporte al equipo / Follow-ups de directivos y cliente
* **05:00 - 06:00 PM |** Cierre de jornada y planificación del martes

---

### **Martes**
*Foco: Deep Work (Estrategia y preparación clave)*
* **09:00 - 10:00 AM | Responder emails de stakeholders (1h)**
* **10:00 - 12:00 PM | Escribir OKRs Q3 - Bloque 1 (2h)**
* **12:00 - 01:00 PM |** Descanso cognitivo / Buffer
* **01:00 - 02:00 PM |** Almuerzo
* **02:00 - 04:00 PM | Escribir OKRs Q3 - Bloque 2 (2h)** *(Completas las 4 horas en tu día más despejado)*
* **04:00 - 06:00 PM | Preparar presentación para la demo - Bloque 1 (2h de 3h)**

---

### **Miércoles**
*Foco: Cierre de entregables y Demo Day*
* **09:00 - 10:00 AM | Responder emails de stakeholders (1h)**
* **10:00 - 11:00 AM | Preparar presentación para la demo - Bloque 2 (1h)** *(Completas las 3h requeridas)*
* **11:00 - 01:00 PM | Revisar PRDs pendientes (2h)**
* **01:00 - 02:00 PM |** Almuerzo
* **02:00 - 03:00 PM |** Ensayo final y verificación del entorno técnico para la demo
* **03:00 - 04:00 PM | [Fijo] Demo de producto**
* **04:00 - 05:00 PM |** Consolidación de feedback de la demo y action items
* **05:00 - 06:00 PM |** Buffer / Trabajo reactivo

---

### **Jueves**
*Foco: Talento y Hiring*
* **09:00 - 10:00 AM | Responder emails de stakeholders (1h)**
* **10:00 - 01:00 PM | [Fijo] Entrevistas de hiring (3h)**
* **01:00 - 02:00 PM |** Almuerzo
* **02:00 - 03:00 PM |** Llenado de scorecards y feedback de entrevistas *(Recomendable hacerlo con la memoria fresca)*
* **03:00 - 05:00 PM |** Interacción con ingeniería / QA / Diseño
* **05:00 - 06:00 PM |** Buffer / Puesta al día

---

### **Viernes**
*Foco: Personas, mejora continua y cierre de semana*
* **09:00 - 10:00 AM | Responder emails de stakeholders (1h)**
* **10:00 - 11:30 AM | One-on-Ones con reportes directos (1.5h en bloque)**
  * *10:00 - 10:30:* 1:1 Reporte 1
  * *10:30 - 11:00:* 1:1 Reporte 2
  * *11:00 - 11:30:* 1:1 Reporte 3
* **11:30 - 01:00 PM |** Documentación de acuerdos de los 1:1s y tareas operativas
* **01:00 - 02:00 PM |** Almuerzo
* **02:00 - 04:00 PM |** Preparación de inputs para la retro y revisión de la semana
* **04:00 - 05:00 PM | [Fijo] Retrospectiva**
* **05:00 - 06:00 PM |** Cierre semanal (Inbox 0 y balance final)

---

### **Puntos clave de esta distribución:**
1. **Protección del Martes:** Se dedicaron 6 horas netas de trabajo profundo (OKRs + 2h de demo) sin interrupciones.
2. **Buffer post-eventos críticos:** Se dejaron espacios tras las entrevistas de hiring (para subir scorecards) y tras la demo (para procesar el feedback).
3. **1:1s agrupados:** Colocarlos consecutivos en la mañana del viernes ahorra fragmentación mental y permite evaluar la semana del equipo antes de la retrospectiva.