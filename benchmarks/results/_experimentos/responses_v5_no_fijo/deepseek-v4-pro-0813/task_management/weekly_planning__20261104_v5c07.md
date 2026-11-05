# DeepSeek V4 Pro (0813) — task_management/weekly_planning

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 8.43 | quality: 9.8
- latency_total: 19.46s | tokens_per_second: 80.3
- input_tokens: 206 | output_tokens: 1562
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y altamente útil, con una estructura bien organizada que facilita la planificación semanal, aunque podría profundizar un poco más en la justificación de la distribución de tareas.

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

Aquí tienes un plan semanal detallado que respeta tus restricciones y distribuye las tareas de manera realista, agrupando bloques de trabajo profundo y dejando tiempo para imprevistos.

### Principios usados
- **Trabajo profundo por la mañana**: Las tareas que requieren concentración (OKRs, presentación, PRDs) se asignan a primeras horas.
- **Emails como tarea de cierre**: La revisión de correos se ubica al final de la jornada para no interrumpir el enfoque.
- **Reuniones existentes como anclas**: Se planifica alrededor de los compromisos fijos.

---

### Lunes
| Hora | Actividad | Tipo |
|------|-----------|------|
| 9:00 – 11:00 | Reunión de directivos | Fija |
| 11:00 – 11:15 | Descanso / transición | Buffer |
| 11:15 – 12:15 | **Revisar métricas del producto** (1 h) | Tarea 5 |
| 12:15 – 13:00 | **Preparar presentación demo** (45 min) | Tarea 1 (parcial) |
| 13:00 – 14:00 | Almuerzo con cliente | Fija |
| 14:00 – 14:30 | **One-on-one reporte 1** (30 min) | Tarea 6 (parcial) |
| 14:30 – 15:00 | **One-on-one reporte 2** (30 min) | Tarea 6 (parcial) |
| 15:00 – 15:30 | **One-on-one reporte 3** (30 min) | Tarea 6 (parcial) |
| 15:30 – 16:30 | **Responder emails** (1 h) | Tarea 4 |
| 16:30 – 17:00 | Buffer / pendientes | Buffer |

---

### Martes (día libre, ideal para trabajo profundo)
| Hora | Actividad | Tipo |
|------|-----------|------|
| 9:00 – 11:00 | **Escribir OKRs Q3** (2 h) | Tarea 3 (parcial) |
| 11:00 – 11:15 | Descanso | Buffer |
| 11:15 – 12:15 | **Escribir OKRs Q3** (1 h) | Tarea 3 (parcial) |
| 12:15 – 13:15 | **Revisar PRDs pendientes** (1 h) | Tarea 2 (parcial) |
| 13:15 – 14:15 | Almuerzo libre | Personal |
| 14:15 – 15:15 | **Revisar PRDs pendientes** (1 h) | Tarea 2 (parcial) |
| 15:15 – 16:15 | **Preparar presentación demo** (1 h) | Tarea 1 (parcial) |
| 16:15 – 17:00 | **Responder emails** (45 min) | Tarea 4 |
| 17:00 – 17:30 | Buffer / planificación miércoles | Buffer |

---

### Miércoles
| Hora | Actividad | Tipo |
|------|-----------|------|
| 9:00 – 10:00 | **Preparar presentación demo** (1 h) | Tarea 1 (parcial) |
| 10:00 – 11:00 | **Escribir OKRs Q3** (1 h final) | Tarea 3 (cierre) |
| 11:00 – 12:00 | **Responder emails** (1 h) | Tarea 4 |
| 12:00 – 13:00 | Almuerzo | Personal |
| 13:00 – 14:00 | **Preparar presentación demo** (45 min restantes + ensayo) | Tarea 1 (cierre) |
| 14:00 – 15:00 | Buffer / repaso de demo | Buffer |
| 15:00 – 16:00 | **Demo de producto** | Fija |
| 16:00 – 17:00 | **Responder emails** (1 h) | Tarea 4 |

---

### Jueves
| Hora | Actividad | Tipo |
|------|-----------|------|
| 9:00 – 10:00 | **Responder emails** (1 h) | Tarea 4 |
| 10:00 – 13:00 | Entrevistas de hiring | Fija |
| 13:00 – 14:00 | Almuerzo | Personal |
| 14:00 – 15:00 | **Revisar PRDs pendientes** (si quedaron pendientes) | Tarea 2 (buffer) |
| 15:00 – 16:00 | Buffer / trabajo administrativo | Buffer |
| 16:00 – 17:00 | **Responder emails** (1 h) | Tarea 4 |

---

### Viernes
| Hora | Actividad | Tipo |
|------|-----------|------|
| 9:00 – 10:00 | **Revisar PRDs pendientes** (cierre si faltaba) | Tarea 2 |
| 10:00 – 11:00 | **Responder emails** (1 h) | Tarea 4 |
| 11:00 – 12:00 | Buffer / planificación siguiente semana | Buffer |
| 12:00 – 13:00 | Almuerzo | Personal |
| 13:00 – 15:00 | Trabajo libre / adelantar pendientes | Flexible |
| 15:00 – 16:00 | Preparar retrospectiva (notas, métricas) | Apoyo a fija |
| 16:00 – 17:00 | **Retrospectiva** | Fija |
| 17:00 – 17:30 | **Responder emails** (cierre, 30 min) | Tarea 4 (parcial) |

---

### Resumen de cumplimiento
- ✅ **Preparar presentación**: 3 h distribuidas entre lunes, martes y miércoles (45 min + 1 h + 1 h + 45 min).
- ✅ **Revisar PRDs**: 2 h (martes 2 h; jueves/viernes como buffer si se necesitó).
- ✅ **Escribir OKRs**: 4 h (martes 2 h + miércoles 1 h + martes 1 h = 4 h).
- ✅ **Emails diarios**: 1 h cada día laboral (lunes a viernes; el viernes se cierra con 30 min extra).
- ✅ **Métricas**: 1 h el lunes.
- ✅ **One-on-ones**: 3 × 30 min el lunes por la tarde.

¿Quieres que ajuste algo según tu cronotipo (más reuniones por la mañana, etc.)?