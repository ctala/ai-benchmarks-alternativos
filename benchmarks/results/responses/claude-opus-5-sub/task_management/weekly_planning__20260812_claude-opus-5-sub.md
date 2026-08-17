# Claude Opus 5 (suscripción) — task_management/weekly_planning

- model_id: `claude-opus-5`
- success: True  | final: 7.8 | quality: 10.0
- latency_total: 131.953s | tokens_per_second: 76.1
- input_tokens: 2 | output_tokens: 10039
- judge_score: 5 | justificación: La respuesta es precisa, altamente relevante, ofrece una planificación detallada y estructurada, es clara y fácil de entender, y es extremadamente útil para un emprendedor.

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

# Plan semanal

**Supuestos** (ajusta si no calzan): jornada 9:00–18:00, almuerzo 13:00–14:00, bloques con ±15 min de holgura.

**Tres decisiones que ordenan la semana:**
1. **La demo se prepara en tres pasos separados, no en un bloque.** Guión → slides → ensayo. Nunca terminando el deck la mañana del miércoles.
2. **El martes en la mañana es para los OKRs.** Es tu único bloque de 3 horas sin interrupciones en toda la semana. Cualquier otra cosa que metas ahí te cuesta el trabajo más caro que tienes.
3. **Los OKRs se cierran el viernes, no el martes.** El borrador necesita distancia. Escribir 4 horas seguidas produce OKRs que suenan bien y no miden nada.

---

## Lunes — contexto y alineación

| Hora | Bloque |
|---|---|
| 09:00–11:00 | 🔒 Reunión de directivos |
| 11:00–11:20 | Buffer: descargar notas y compromisos que salieron |
| 11:20–12:20 | **Revisión de métricas del producto (1h)** ✅ tarea 5 |
| 12:20–12:50 | Emails, tanda 1 |
| 12:50–13:00 | Preparar almuerzo con cliente |
| 13:00–14:00 | 🔒 Almuerzo con cliente |
| 14:00–14:30 | Notas del almuerzo + emails tanda 2 ✅ tarea 4 |
| 14:30–15:30 | **Demo: estructura y guión (1h)** — sin abrir slides |
| 15:30–16:00 | Buffer |
| 16:00–16:30 | **1:1 reporte #1** |
| 16:30–18:00 | Reactivo / lo que explotó |

**Por qué las métricas van aquí:** salen frescas de la reunión de directivos y alimentan las otras dos cosas de la semana (el guión de la demo y los OKRs). Revisarlas el jueves las vuelve un informe; revisarlas el lunes las vuelve un insumo.

---

## Martes — día de foco (protegido)

| Hora | Bloque |
|---|---|
| 09:00–10:30 | 🧠 **OKRs Q3 — bloque 1: objetivos** (1.5h) |
| 10:30–10:45 | Break sin pantalla |
| 10:45–12:15 | 🧠 **OKRs Q3 — bloque 2: key results y cómo se miden** (1.5h) |
| 12:15–13:15 | Emails ✅ tarea 4 |
| 13:15–14:15 | Almuerzo |
| 14:15–15:45 | **Demo: construcción de slides (1.5h)** |
| 15:45–16:15 | **1:1 reporte #2** |
| 16:30–17:00 | **1:1 reporte #3** ✅ tarea 6 |
| 17:00–18:00 | Colchón: si los OKRs quedaron cortos, aquí |

**Reglas para que el martes en la mañana sobreviva:** calendario bloqueado como ocupado, Slack cerrado, teléfono en otra habitación. Si alguien pide ese espacio, ofrece el miércoles a las 10:30. Los 1:1 van en la tarde a propósito: después de 3 horas escribiendo no sirves para trabajo profundo, pero sí para escuchar.

---

## Miércoles — día de demo

| Hora | Bloque |
|---|---|
| 09:00–09:30 | **Demo: ensayo cronometrado en voz alta (30 min)** ✅ tarea 1 |
| 09:30–10:30 | Arreglar lo que rompió el ensayo — **este bloque no es opcional** |
| 10:30–11:30 | Reactivo / disponible |
| 11:30–12:30 | Emails ✅ tarea 4 |
| 12:30–13:30 | Almuerzo temprano |
| 13:30–14:30 | Trabajo liviano (nada que te absorba) |
| 14:30–15:00 | Setup técnico: links, pantalla, backup del deck, respirar |
| 15:00–16:00 | 🔒 **DEMO DE PRODUCTO** |
| 16:00–16:30 | Notas post-demo en caliente: objeciones, preguntas, promesas |
| 16:30–18:00 | Reactivo |

El ensayo a las 9:00 existe para que el bloque de 9:30 tenga algo que arreglar. Un ensayo que no encuentra problemas significa que no ensayaste en serio.

---

## Jueves — hiring y revisión

| Hora | Bloque |
|---|---|
| 09:00–10:00 | Emails ✅ tarea 4 (adelantado: el mediodía está bloqueado) |
| 10:00–13:00 | 🔒 Entrevistas de hiring |
| 13:00–14:00 | Almuerzo |
| 14:00–14:30 | **Scorecards de las entrevistas** — decisión escrita mientras la tienes fresca |
| 14:30–16:30 | **Revisión de PRDs (2h)** ✅ tarea 2 |
| 16:30–18:00 | Buffer |

Los PRDs van aquí porque revisar es trabajo de criterio, no de creación: aguanta el desgaste de tres horas de entrevistas. Los scorecards de 14:00 son la tarea que todo PM posterga y termina decidiendo por recuerdo tres días después.

---

## Viernes — cerrar

| Hora | Bloque |
|---|---|
| 09:00–10:00 | **OKRs Q3 — cierre: pulir, recortar, mandar a revisión (1h)** ✅ tarea 3 |
| 10:00–12:00 | **Colchón de la semana**: lo que se corrió de lugar cae acá |
| 12:00–13:00 | Emails ✅ tarea 4 |
| 13:00–14:00 | Almuerzo |
| 14:00–15:30 | Reactivo |
| 15:30–16:00 | Preparar retro: 3 datos concretos, no impresiones |
| 16:00–17:00 | 🔒 Retrospectiva |
| 17:00–17:30 | Cierre: qué queda pendiente para el lunes |

---

## Cuadre de horas

| Tarea | Comprometido | Dónde |
|---|---|---|
| 1. Presentación demo | 3h ✅ | Lun 1h + Mar 1.5h + Mié 0.5h |
| 2. PRDs pendientes | 2h ✅ | Jue 14:30–16:30 |
| 3. OKRs Q3 | 4h ✅ | Mar 3h + Vie 1h |
| 4. Emails stakeholders | 5h ✅ | 1h diaria, en bloque |
| 5. Métricas de producto | 1h ✅ | Lun 11:20 |
| 6. Tres 1:1 | 1.5h ✅ | Lun 1, Mar 2 |
| **Total tareas** | **16.5h** | |
| Reuniones fijas | 8h | |
| **Comprometido** | **24.5h de 40h (61%)** | |
| Libre para lo imprevisto | ~15h | |

Ese 39% libre no es holgura de más: es lo que un PM consume en interrupciones reales cada semana. Si lo llenas, el plan se cae el martes.

---

## Puntos de riesgo y qué hacer

| Riesgo | Plan B |
|---|---|
| Alguien pide tu martes en la mañana | Ofrece miércoles 10:30. Es lo único innegociable de la semana. |
| El ensayo del miércoles revela que la demo no funciona | Ya tienes 09:30–11:30 disponibles. Por eso el ensayo es a las 9:00 y no a las 14:00. |
| La reunión de directivos genera un incendio | Sacrifica la revisión de PRDs del jueves. Es lo más postergable de la lista. |
| Se cae un 1:1 | Muévelo al colchón del viernes 10:00–12:00. |
| Los OKRs se pasan de 4h | Es la señal más común de que el alcance está mal definido, no de que falta tiempo. Antes de agregar horas, recorta objetivos. |

**Lo primero que se corta si la semana se descontrola:** PRDs → uno de los 1:1 (reagendado, no cancelado) → métricas. **Lo que no se toca nunca:** el ensayo de la demo y el bloque de OKRs del martes.