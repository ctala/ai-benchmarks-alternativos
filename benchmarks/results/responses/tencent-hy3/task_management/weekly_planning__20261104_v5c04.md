# Tencent Hy3 — task_management/weekly_planning

- model_id: `tencent/hy3`
- success: True  | final: 8.98 | quality: 10.0
- latency_total: 15.949s | tokens_per_second: 64.3
- input_tokens: 227 | output_tokens: 1025
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y altamente util, con una estructura detallada que facilita la planificación semanal, aunque podría profundizar un poco más en la gestión de imprevistos.

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

¡Hola! Como product manager, tu semana tiene espacios libres y bloqueos fijos. Aquí tienes un plan detallado que respeta tus restricciones, distribuye las tareas y deja margen para imprevistos.

**Supuestos:**
- Horario laboral estándar: 9 AM – 6 PM.
- Los emails de stakeholders (1h diaria) se hacen en bloque fijo a primera hora o al final para proteger el foco.
- Los 1:1 con reportes se reparten en días libres o con huecos.

---

### LUNES
- **9:00 – 11:00** Reunión de directivos (fijo)
- **11:00 – 12:00** Responder emails de stakeholders (1h)
- **12:00 – 1:00** Revisar PRDs pendientes (1h de 2h totales)
- **1:00 – 2:00** Almuerzo con cliente (fijo)
- **2:00 – 3:00** Revisar PRDs pendientes (1h restante)
- **3:00 – 4:00** Revisar métricas del producto (1h)
- **4:00 – 6:00** Tiempo libre / buffer

### MARTES (día libre)
- **9:00 – 10:00** Responder emails de stakeholders (1h)
- **10:00 – 1:00** Escribir OKRs Q3 (3h de 4h)
- **1:00 – 2:00** Almuerzo
- **2:00 – 3:00** Escribir OKRs Q3 (1h restante)
- **3:00 – 3:30** 1:1 con Reporte A (30 min)
- **3:30 – 4:00** 1:1 con Reporte B (30 min)
- **4:00 – 4:30** 1:1 con Reporte C (30 min)
- **4:30 – 6:00** Preparar presentación para demo (1h de 3h)

### MIÉRCOLES
- **9:00 – 10:00** Responder emails de stakeholders (1h)
- **10:00 – 12:00** Preparar presentación para demo (2h restantes de 3h)
- **12:00 – 1:00** Almuerzo
- **1:00 – 3:00** Buffer / ajustes menores demo
- **3:00 – 4:00** Demo de producto (fijo)
- **4:00 – 6:00** Tiempo libre / seguimiento post-demo

### JUEVES
- **9:00 – 10:00** Responder emails de stakeholders (1h)
- **10:00 – 1:00** Entrevistas de hiring (fijo)
- **1:00 – 2:00** Almuerzo
- **2:00 – 3:00** Revisar PRDs pendientes (ya hechos) → usar para OKRs si faltó, si no buffer
- **3:00 – 4:00** Preparar presentación (ya hecha) → buffer / emails sueltos
- **4:00 – 6:00** Tiempo libre

### VIERNES
- **9:00 – 10:00** Responder emails de stakeholders (1h)
- **10:00 – 12:00** Repaso general / imprevistos
- **12:00 – 1:00** Almuerzo
- **1:00 – 4:00** Tiempo libre / catch-up
- **4:00 – 5:00** Retrospectiva (fijo)
- **5:00 – 6:00** Cierre semanal

---

**Resumen de cumplimiento:**
1. Prep demo: Mar (1h) + Mié (2h) = 3h ✅  
2. PRDs: Lun (2h) ✅  
3. OKRs Q3: Mar (4h) ✅  
4. Emails: 1h diaria Lun–Vie ✅  
5. Métricas: Lun (1h) ✅  
6. 1:1s: Mar (3×30min) ✅  

¿Quieres que ajuste algo (p. ej. mover 1:1s a jueves tarde o cambiar bloques de OKRs)?