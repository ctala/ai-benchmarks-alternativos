# Qwen 3.7 Max — task_management/weekly_planning

- model_id: `qwen/qwen3.7-max`
- success: True  | final: 8.44 | quality: 10.0
- latency_total: 33.165s | tokens_per_second: 60.6
- input_tokens: 212 | output_tokens: 2010
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y prácticamente útil, ofreciendo un plan semanal bien estructurado que se ajusta perfectamente a las restricciones y necesidades del product manager.

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

Hola. Como Product Manager, entiendo perfectamente la necesidad de proteger tu tiempo de trabajo profundo (deep work) mientras cumples con las obligaciones operativas y estratégicas.

He diseñado este plan semanal siguiendo tres principios clave de gestión de tiempo para PMs:
1.  **Context Switching Minimization:** Agrupar tareas similares (ej. los 1:1s juntos).
2.  **Preparación Anticipada:** La demo del miércoles se prepara el martes para evitar estrés de última hora.
3.  **Bloques de Estrategia vs. Táctica:** Separar la escritura de OKRs (estratégico) de la revisión de PRDs/Métricas (táctico).

Aquí tienes tu planificación detallada:

### 🗓️ Plan Semanal Detallado

#### Lunes: Alineación Estratégica y Gestión de Stakeholders
*El lunes está fragmentado por reuniones externas. Usamos los huecos para tareas tácticas y comunicación.*

| Horario | Actividad | Notas / Contexto |
| :--- | :--- | :--- |
| 09:00 - 11:00 | 🔒 Reunión de Directivos | Fijo. Tomar notas para alinear OKRs. |
| 11:00 - 12:00 | 📧 Emails de Stakeholders | Responder pendientes post-reunión directiva. |
| 12:00 - 13:00 | 📊 Revisar Métricas del Producto | Mejor hacer esto tras la reunión directiva para tener contexto fresco. |
| 13:00 - 14:00 | 🍽️ Almuerzo con Cliente | Fijo. Networking / Feedback directo. |
| 14:00 - 16:00 | 📝 Revisar PRDs Pendientes (2h) | Bloque ininterrumpido. Modo "revisor técnico". |
| 16:00 - 17:30 | Buffer / Tareas Ad-hoc | Espacio amortiguador antes de cerrar el día. |

#### Martes: Deep Work Estratégico (Día Libre de Reuniones Fijas)
*Aprovechamos que es tu día más limpio para el trabajo cognitivo más pesado: OKRs y Preparación de Demo.*

| Horario | Actividad | Notas / Contexto |
| :--- | :--- | :--- |
| 09:00 - 10:00 | 📧 Emails de Stakeholders | Limpieza matutina para no arrastrar deuda. |
| 10:00 - 12:00 | 🎯 Escribir OKRs Q3 (Parte 1: 2h) | **Deep Work.** Cerebro fresco para estrategia pura. |
| 12:00 - 13:00 | ☕ Descanso / Almuerzo | Desconexión real antes del segundo bloque fuerte. |
| 13:00 - 15:00 | 🎯 Escribir OKRs Q3 (Parte 2: 2h) | Completar borrador. Validar con insights del lunes. |
| 15:00 - 16:30 | 🎤 Preparar Presentación Demo (1.5h) | Inicio de preparación. Estructura y narrativa. |
| 16:30 - 17:30 | Buffer / Revisión ligera | Cierre suave del día de alto rendimiento. |

#### Miércoles: Ejecución y Equipo
*Día centrado en la Demo y en conectar con tu equipo mediante los 1:1s.*

| Horario | Actividad | Notas / Contexto |
| :--- | :--- | :--- |
| 09:00 - 10:00 | 📧 Emails de Stakeholders | Gestión diaria. |
| 10:00 - 11:30 | 🎤 Preparar Presentación Demo (1.5h) | Finalizar slides y ensayo. Deja 30 min buffer antes de la demo. |
| 11:30 - 12:00 | 👥 One-on-one Reporte #1 | Agrupados antes del almuerzo. |
| 12:00 - 12:30 | 👥 One-on-one Reporte #2 | Back-to-back para proteger el resto del día. |
| 12:30 - 13:30 | ☕ Almuerzo | |
| 13:30 - 14:30 | Buffer / Repaso final Demo | Último chequeo técnico o de contenido. |
| 15:00 - 16:00 | 🔒 Demo de Producto | Fijo. |
| 16:00 - 17:00 | 📋 Debrief Post-Demo | Documentar feedback inmediato mientras está fresco. |

#### Jueves: Hiring y Conexión con el Equipo
*Las entrevistas consumen energía mental. Dejamos el último 1:1 aquí y evitamos deep work pesado.*

| Horario | Actividad | Notas / Contexto |
| :--- | :--- | :--- |
| 09:00 - 10:00 | 📧 Emails de Stakeholders | Preparar agenda de entrevistas y revisar CVs. |
| 10:00 - 13:00 | 🔒 Entrevistas de Hiring | Fijo (3 horas). Pausa de 5-10 min entre cada entrevista. |
| 13:00 - 14:00 | ☕ Almuerzo / Decompress | Las entrevistas cansan. No agendes nada pesado aquí. |
| 14:00 - 14:30 | 👥 One-on-one Reporte #3 | Último 1:1 de la semana. |
| 14:30 - 16:00 | 📝 Revisión PRDs / Follow-ups | Tarea táctica ligera post-entrevistas. |
| 16:00 - 17:00 | Buffer / Preparación Retro | Reflexionar sobre qué llevar a la retro del viernes. |

#### Viernes: Cierre, Retrospectiva y Planificación
*Día de baja intensidad cognitiva. Enfocado en mejorar procesos y cerrar cabos.*

| Horario | Actividad | Notas / Contexto |
| :--- | :--- | :--- |
| 09:00 - 10:00 | 📧 Emails de Stakeholders | Cerrar temas pendientes de la semana. |
| 10:00 - 12:00 | 🔄 Refinar OKRs / Planif. Siguiente Semana | Usar el borrador del martes + feedback de directivos del lunes. |
| 12:00 - 13:00 | ☕ Almuerzo | |
| 13:00 - 15:00 | Buffer Generoso / Tareas Pendientes | Espacio para lo que se desbordó durante la semana. |
| 15:00 - 16:00 | 🧹 Inbox Zero / Admin | Limpiar bandeja antes de la retro. |
| 16:00 - 17:00 | 🔒 Retrospectiva | Fijo. Acción > Queja. |

---

### 💡 Recomendaciones Clave para este Plan

1.  **Los Emails son un bloque, no una reacción constante:** He asignado 1 hora *diaria* en bloque. Fuera de ese horario, cierra la pestaña de correo/Slack. Como PM, si estás siempre reactivo, nunca avanzarás en OKRs ni PRDs.
2.  **Protege el Martes como Oro:** Es tu único día sin reuniones fijas. Si alguien pide una reunión urgente ese día, ofrécele jueves por la tarde o viernes mañana, pero **no cedas el martes**.
3.  **Buffer Intencional:** He dejado bloques de "Buffer" explícitos. En producto, los imprevistos son la norma, no la excepción. Si no usas el buffer, se convertirá en horas extra o en deuda técnica/estratégica.
4.  **1:1s Agrupados:** Los puse back-to-back el miércoles y uno el jueves. Esto evita que tu día tenga "queso suizo" (huecos de 30 min inutilizables entre reuniones). Además, te permite entrar en "modo people manager" de forma concentrada.
5.  **OKRs en Dos Sesiones:** 4 horas seguidas de escritura estratégica generan fatiga de decisión. Dividirlo en 2h+2h el martes garantiza mayor calidad en la segunda sesión, donde refinas y aterrizas lo escrito en la primera.

¿Te gustaría que ajuste algún bloque según tus niveles de energía personales (ej. si eres más productivo por las tardes) o que agregue alguna herramienta específica para gestionar estos bloques?