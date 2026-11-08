# Seed 2.1 Turbo — task_management/weekly_planning

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 8.24 | quality: 9.52
- latency_total: 24.386s | tokens_per_second: 72.5
- input_tokens: 256 | output_tokens: 1768
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

### Plan semanal de Product Manager  
Horario base: 9 AM - 6 PM (incluye almuerzo de 12 PM - 1 PM, excepto lunes que se ajusta por almuerzo con cliente)  
Principios aplicados:  
- Tareas de deep work (preparación de demo, OKRs, PRDs) en bloques de 1.5-2h sin interrupciones, en horarios de mayor energía (mañana temprano o tarde después de reuniones)  
- Emails de stakeholders en bloques cortos al inicio y fin del día para no fragmentar el trabajo  
- One-on-ones agrupados para reducir cambio de contexto  
- Tareas alineadas con sus deadlines (ej: preparación de demo antes del miércoles)

---

#### Lunes  
| Horario       | Actividad                                                                 |
|---------------|---------------------------------------------------------------------------|
| 9:00 - 11:00  | Reunión de directivos (restricción fija)                                 |
| 11:00 - 12:00 | Responder emails de stakeholders (bloque 1) + planificación de la semana |
| 12:00 - 13:00 | Almuerzo ligero (ajuste por almuerzo con cliente)                        |
| 13:00 - 14:00 | Almuerzo con cliente (restricción fija)                                  |
| 14:00 - 16:00 | Escribir OKRs Q3 (bloque 1 de 2h, deep work)                             |
| 16:00 - 16:15 | Pausa corta                                                               |
| 16:15 - 17:15 | Revisar métricas del producto (1h)                                       |
| 17:15 - 18:00 | Responder emails de stakeholders (bloque 2, cierre de día)               |

---

#### Martes (día libre de reuniones fijas, ideal para deep work)  
| Horario       | Actividad                                                                 |
|---------------|---------------------------------------------------------------------------|
| 9:00 - 10:00  | Responder emails de stakeholders (bloque 1)                               |
| 10:00 - 12:00 | Preparar presentación para la demo (bloque 1 de 2h, deep work)           |
| 12:00 - 13:00 | Almuerzo                                                                  |
| 13:00 - 14:00 | Preparar presentación para la demo (bloque 2 de 1h, finalización + prueba) |
| 14:00 - 14:15 | Pausa corta                                                               |
| 14:15 - 16:15 | Escribir OKRs Q3 (bloque 2 de 2h, finalización)                          |
| 16:15 - 17:15 | Revisar PRDs pendientes (bloque 1 de 1h)                                 |
| 17:15 - 18:00 | Responder emails de stakeholders (bloque 2, cierre de día)               |

---

#### Miércoles  
| Horario       | Actividad                                                                 |
|---------------|---------------------------------------------------------------------------|
| 9:00 - 10:00  | Responder emails de stakeholders (bloque 1)                               |
| 10:00 - 11:00 | Revisar PRDs pendientes (bloque 2 de 1h, finalización)                   |
| 11:00 - 12:00 | Repaso final de la presentación de demo + ajustes de último minuto       |
| 12:00 - 13:00 | Almuerzo                                                                  |
| 13:00 - 15:00 | One-on-one con reportes directos (2 de 3: 13:00-13:30 y 13:30-14:00) + 1h de buffer por preguntas post-reunión |
| 15:00 - 16:00 | Demo de producto (restricción fija)                                      |
| 16:00 - 16:30 | One-on-one con el tercer reporte directo                                 |
| 16:30 - 17:30 | Recoger feedback de la demo + registrar acciones pendientes              |
| 17:30 - 18:00 | Responder emails de stakeholders (bloque 2, cierre de día)               |

---

#### Jueves  
| Horario       | Actividad                                                                 |
|---------------|---------------------------------------------------------------------------|
| 9:00 - 10:00  | Responder emails de stakeholders (bloque 1) + preparación previa a entrevistas |
| 10:00 - 13:00 | Entrevistas de hiring (restricción fija)                                 |
| 13:00 - 14:00 | Almuerzo                                                                  |
| 14:00 - 16:00 | Registro de feedback de entrevistas + actualización de pipeline de hiring |
| 16:00 - 16:15 | Pausa corta                                                               |
| 16:15 - 17:30 | Tiempo flexible para resolver imprevistos (ej: seguimiento de acciones de demo) |
| 17:30 - 18:00 | Responder emails de stakeholders (bloque 2, cierre de día)               |

---

#### Viernes  
| Horario       | Actividad                                                                 |
|---------------|---------------------------------------------------------------------------|
| 9:00 - 10:00  | Responder emails de stakeholders (bloque 1)                               |
| 10:00 - 12:00 | Cierre de tareas pendientes de la semana + actualización de backlog de producto |
| 12:00 - 13:00 | Almuerzo                                                                  |
| 13:00 - 16:00 | Planificación de la semana siguiente + revisión de prioridades           |
| 16:00 - 17:00 | Retrospectiva (restricción fija)                                         |
| 17:00 - 18:00 | Responder emails de stakeholders (bloque 2, cierre de semana)            |

---

### Cumplimiento de tareas:
1. Preparar presentación para la demo (3h): ✅ Martes 10-12h + 13-14h  
2. Revisar PRDs pendientes (2h): ✅ Martes 16:15-17:15 + Miércoles 10-11h  
3. Escribir OKRs Q3 (4h): ✅ Lunes 14-16h + Martes 14:15-16:15h  
4. Responder emails de stakeholders (1h/día): ✅ 2 bloques de ~30min cada día (suman 1h diario)  
5. Revisar métricas del producto (1h): ✅ Lunes 16:15-17:15h  
6. One-on-one con 3 reportes (30min c/u): ✅ Miércoles 13:00-13:30, 13:30-14:00, 16:00-16:30