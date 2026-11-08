# Mistral Large 4.0 — task_management/weekly_planning

- model_id: `mistralai/mistral-large-4-0`
- success: True  | final: 8.19 | quality: 9.52
- latency_total: 38.347s | tokens_per_second: 162.5
- input_tokens: 199 | output_tokens: 6232
- judge_score: 4.8 | justificación: 

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

Aquí tienes un plan optimizado aprovechando que el **martes está libre** para *deep work* y distribuyendo los 1:1s para no saturar ningún día:

---

### **LUNES** (Día de ejecución post-reuniones)
| Horario | Tarea | Notas |
|---------|-------|-------|
| **09:00-11:00** | 🔴 Reunión de directivos | [Fijo] |
| **11:00-12:00** | 📧 Emails stakeholders | Aprovecha el contexto fresco de la reunión |
| **12:00-13:00** | 📊 Revisar métricas del producto | Antes del almuerzo, mente fresca para análisis |
| **13:00-14:00** | 🍽️ Almuerzo con cliente | [Fijo] |
| **14:00-17:00** | 🎯 **Preparar presentación demo (3h)** | Bloque profundo post-almuerzo. Ya quedará lista para el miércoles |
| **17:00-18:00** | Buffer / emails urgentes | |

---

### **MARTES** (Día de Deep Work - sin interrupciones)
| Horario | Tarea | Notas |
|---------|-------|-------|
| **09:00-11:00** | 🎯 **OKRs Q3 - Bloque 1 (2h)** | Máxima concentración por la mañana |
| **11:00-11:30** | 📧 Emails (30 min) | |
| **11:30-13:00** | 🎯 **OKRs Q3 - Bloque 2 (1.5h)** | |
| **13:00-14:00** | Almuerzo | |
| **14:00-14:30** | 🎯 Finalizar OKRs Q3 (30 min) | ✅ **Total OKRs: 4h completados** |
| **14:30-16:30** | 📄 **Revisar PRDs pendientes (2h)** | |
| **16:30-17:00** | 📧 Emails (30 min) | ✅ **Total martes: 1h emails** |
| **17:00-17:30** | 👤 1:1 Reporte #1 | |
| **17:30-18:00** | Tiempo libre / buffer | |

---

### **MIÉRCOLES** (Día de la demo)
| Horario | Tarea | Notas |
|---------|-------|-------|
| **09:00-10:00** | 📧 Emails stakeholders | |
| **10:00-10:30** | 👤 1:1 Reporte #2 | Antes de la demo para no estar con prisa |
| **10:30-12:00** | 🎯 Última revisión presentación / preparar Q&A | Pulir detalles de la demo |
| **12:00-13:00** | Almuerzo | |
| **13:00-15:00** | Trabajo flexible / análisis de datos / features | |
| **15:00-16:00** | 🚀 **DEMO DE PRODUCTO** | [Fijo] |
| **16:00-17:00** | Documentar feedback de la demo | Follow-ups inmediatos mientras está fresco |
| **17:00-18:00** | Buffer | |

---

### **JUEVES** (Día de hiring)
| Horario | Tarea | Notas |
|---------|-------|-------|
| **09:00-10:00** | 📧 Emails stakeholders | Antes de las entrevistas |
| **10:00-13:00** | 🎤 **Entrevistas de hiring** | [Fijo] |
| **13:00-14:00** | Almuerzo | |
| **14:00-14:30** | 👤 1:1 Reporte #3 | Después de entrevistas, antes de seguir con tareas pesadas |
| **14:30-16:00** | Roadmap / análisis post-entrevistas / tareas pendientes | |
| **16:00-18:00** | Tiempo flexible | Buffer para imprevistos de la semana |

---

### **VIERNES** (Cierre y planificación)
| Horario | Tarea | Notas |
|---------|-------|-------|
| **09:00-10:00** | 📧 Emails stakeholders | |
| **10:00-12:00** | Planificación semana siguiente / limpiar backlog | |
| **12:00-13:00** | Almuerzo | |
| **13:00-16:00** | Deep work: análisis semanal / reportes / trabajo pendiente | Lo que no se pudo hacer durante la semana |
| **16:00-17:00** | 🔄 **Retrospectiva** | [Fijo] |
| **17:00-18:00** | Cierre de semana | |

---

### **✅ Checklist de cumplimiento:**
- ✅ **Demo prep (3h):** Lunes 14-17h (lista 24h antes de la demo)
- ✅ **PRDs (2h):** Martes 14:30-16:30h
- ✅ **OKRs Q3 (4h):** Martes 9-11h + 11:30-13h + 14-14:30h (bloques protegidos)
- ✅ **Emails (1h/día):** Distribuidos en cada mañana (o 30+30 min el martes si prefieres fragmentar)
- ✅ **Métricas (1h):** Lunes 12-13h
- ✅ **1:1s (3x30min):** Martes 17h, Miércoles 10h, Jueves 14h (distribuidos para no saturar)

**💡 Tip:** Si los OKRs te cuestan arrancar, invierte los bloques del martes: haz PRDs primero (más liviano) y OKRs después del almuerzo cuando la energía baja menos.