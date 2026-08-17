# Claude Opus 5 — task_management/weekly_planning

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 7.9 | quality: 10.0
- latency_total: 70.049s | tokens_per_second: 82.5
- input_tokens: 320 | output_tokens: 5778
- judge_score: 5 | justificación: La respuesta es precisa, altamente relevante, ofrece una planificación detallada y estructurada, es clara y fácil de entender, y es extremadamente útil para un emprendedor al integrar eficazmente las tareas y reuniones en un horario semanal.

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

# Plan Semanal — Product Manager

**Supuestos** (ajústalos si no aplican): jornada 9:00–17:30, almuerzo ~13:00–14:00, viernes con foco en cierre. Total de trabajo a colocar: **16,5 h** de tareas + 8 h de reuniones fijas = holgura razonable.

**Decisiones clave del plan:**
- La **prep de la demo** es lo único con deadline duro (miércoles 15:00) → se parte en 2 bloques y termina la mañana del miércoles, con ensayo aparte.
- Las **métricas van el lunes**, antes de los OKRs, porque son insumo directo del Q3.
- Los **OKRs (4 h)** van completos el martes: es tu único día sin interrupciones y es la tarea que más exige foco profundo.
- Los **emails** se hacen en bloque diario fijo, nunca a demanda.
- Los **1:1s** se distribuyen (lun/mar/mié) para no acumularlos y llegar limpio a jueves/viernes.

---

## LUNES — Día de inputs externos

| Hora | Bloque |
|---|---|
| 9:00–11:00 | 🔒 Reunión de directivos |
| 11:00–11:30 | Descarga de notas + accionables de directivos |
| 11:30–12:30 | **Revisar métricas del producto (1 h)** ✅ |
| 12:30–13:00 | Prep almuerzo cliente (agenda + 3 preguntas clave) |
| 13:00–14:00 | 🔒 Almuerzo con cliente |
| 14:00–14:15 | Notas del cliente (en caliente) |
| 14:15–15:15 | **Emails stakeholders (1 h)** ✅ |
| 15:15–15:30 | Pausa |
| 15:30–17:00 | **Demo prep — bloque 1 (1,5 h)**: storyline, guion, qué NO mostrar |
| 17:00–17:30 | **1:1 reporte #1** ✅ |

*Por qué:* aprovechas que sales de directivos y del cliente con contexto fresco para métricas y emails; la demo arranca temprano para tener margen.

---

## MARTES — Deep work (protégelo, sin excepciones)

| Hora | Bloque |
|---|---|
| 9:00–11:00 | **OKRs Q3 — bloque 1 (2 h)**: objetivos y alineación con métricas del lunes |
| 11:00–11:15 | Pausa |
| 11:15–13:15 | **OKRs Q3 — bloque 2 (2 h)**: key results, targets, owners ✅ (4 h completas) |
| 13:15–14:15 | Almuerzo |
| 14:15–16:15 | **Revisar PRDs pendientes (2 h)** ✅ |
| 16:15–16:45 | **1:1 reporte #2** ✅ |
| 16:45–17:45 | **Emails stakeholders (1 h)** ✅ |

*Por qué:* mañana = trabajo creativo/estratégico (OKRs), tarde = trabajo analítico/reactivo (PRDs, emails). Calendario bloqueado como "Focus – no disponible".

---

## MIÉRCOLES — Día de la demo

| Hora | Bloque |
|---|---|
| 9:00–9:15 | Revisión del día |
| 9:15–10:45 | **Demo prep — bloque 2 (1,5 h)**: slides finales + datos ✅ (3 h completas) |
| 10:45–11:00 | Pausa |
| 11:00–12:00 | **Emails stakeholders (1 h)** ✅ |
| 12:00–12:30 | **1:1 reporte #3** ✅ |
| 12:30–13:00 | Colchón |
| 13:00–14:00 | Almuerzo |
| 14:00–14:45 | Ensayo en voz alta + check técnico (audio, pantalla, links) |
| 14:45–15:00 | Respirar / no hacer nada |
| 15:00–16:00 | 🔒 **DEMO DE PRODUCTO** |
| 16:00–16:30 | Notas post-demo + envío de seguimiento el mismo día |
| 16:30–17:30 | Colchón libre |

*Regla:* el ensayo no cuenta como "preparar"; si el bloque 2 se alarga, la prep se recorta, no el ensayo.

---

## JUEVES — Día de hiring

| Hora | Bloque |
|---|---|
| 9:00–9:45 | Prep entrevistas: CVs, rúbrica, reparto de preguntas |
| 9:45–10:00 | Pausa |
| 10:00–13:00 | 🔒 Entrevistas de hiring |
| 13:00–14:00 | Almuerzo (obligatorio, vienes de 3 h intensas) |
| 14:00–14:45 | Scorecards y feedback de entrevistas (en caliente, no lo dejes) |
| 15:00–16:00 | **Emails stakeholders (1 h)** ✅ |
| 16:00–17:00 | Colchón: seguimiento de demo / retoques OKRs |

*Por qué:* jueves ya está cargado cognitivamente; no se le asigna ninguna tarea nueva de la lista salvo emails. El bloque de 16:00 es tu red de seguridad de la semana.

---

## VIERNES — Cierre y consolidación

| Hora | Bloque |
|---|---|
| 9:00–10:00 | **Emails stakeholders (1 h)** ✅ (5/5 completos) |
| 10:00–11:00 | Colchón: cualquier tarea que se haya desbordado |
| 11:00–12:30 | Circular OKRs Q3 para feedback + incorporar comentarios de PRDs |
| 12:30–13:00 | Seguimientos pendientes de la semana |
| 13:00–14:00 | Almuerzo |
| 14:00–15:30 | Trabajo ligero / desbloquear al equipo |
| 15:30–16:00 | Preparar retrospectiva (datos, temas, tono) |
| 16:00–17:00 | 🔒 Retrospectiva |
| 17:00–17:30 | Weekly review + planificar semana siguiente |

---

## Checklist de tareas

| Tarea | Horas | Ubicación | ✔ |
|---|---|---|---|
| Prep presentación demo | 3 h | Lun 15:30 + Mié 9:15 | ✅ |
| Revisar PRDs | 2 h | Mar 14:15 | ✅ |
| Escribir OKRs Q3 | 4 h | Mar 9:00 + 11:15 | ✅ |
| Emails stakeholders | 5 × 1 h | Diario | ✅ |
| Métricas del producto | 1 h | Lun 11:30 | ✅ |
| 1:1s (3) | 1,5 h | Lun / Mar / Mié | ✅ |

---

## Reglas de contingencia

1. **Si algo se cae, cae en este orden:** revisión de PRDs → pulido de OKRs → nunca la prep de la demo ni los 1:1s.
2. **Colchones de rescate:** Mié 16:30, Jue 16:00, Vie 10:00. Úsalos, no los llenes de antemano.
3. **Si aparece un incendio el lunes**, mueve las métricas al martes 9:00 y desplaza los OKRs a Mar 10:00–14:00 (sigue cabiendo).
4. **Si la demo se adelanta o llega antes**, el bloque 2 sube al martes 9:00 y los OKRs se dividen mar/jue.
5. **Emails:** máximo 1 h con timer. Lo que no entre, se convierte en tarea agendada, no en horas extra.
6. **Bloquea el martes en el calendario ya** — es el día que sostiene todo el plan.