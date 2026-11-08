# Claude Opus 5 — task_management/weekly_planning

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 8.04 | quality: 10.0
- latency_total: 34.423s | tokens_per_second: 82.9
- input_tokens: 320 | output_tokens: 2855
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando un plan semanal detallado que se ajusta perfectamente a las restricciones y tareas dadas.

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

**Supuestos:** jornada 9 AM–6 PM, email diario de 30 min × 2 bloques (mañana/tarde) para llegar a la hora diaria.

---

## LUNES — Día fragmentado (solo 4h útiles)

| Hora | Bloque |
|------|--------|
| 9:00–11:00 | 🔒 **Reunión de directivos** |
| 11:00–11:30 | Email stakeholders (parte 1) |
| 11:30–12:00 | Buffer / notas de la reunión de directivos |
| 12:00–1:00 | **Revisar métricas del producto** (1h) ✅ |
| 1:00–2:00 | 🔒 **Almuerzo con cliente** |
| 2:00–2:30 | Buffer / follow-up del cliente |
| 2:30–4:30 | **Revisar PRDs pendientes** (2h) ✅ |
| 4:30–5:00 | Email stakeholders (parte 2) ✅ |
| 5:00–6:00 | Colchón / imprevistos |

> **Por qué así:** las métricas antes del almuerzo con cliente te dan datos frescos para la conversación. Los PRDs van en la tarde porque son trabajo de revisión, no de creación — toleran mejor la energía baja post-almuerzo.

---

## MARTES — Día de deep work (el más valioso de tu semana)

| Hora | Bloque |
|------|--------|
| 9:00–9:30 | Email stakeholders (parte 1) |
| 9:30–11:30 | **OKRs Q3 — Bloque 1** (2h) 🧠 |
| 11:30–11:45 | Descanso |
| 11:45–1:00 | **OKRs Q3 — Bloque 2** (1.25h) |
| 1:00–2:00 | Almuerzo |
| 2:00–2:45 | **OKRs Q3 — Bloque 3** (0.75h) → **total 4h** ✅ |
| 2:45–3:00 | Descanso |
| 3:00–4:30 | **Preparar demo — Bloque 1** (1.5h) |
| 4:30–5:00 | Email stakeholders (parte 2) ✅ |
| 5:00–5:30 | 1:1 Reporte A ✅ |
| 5:30–6:00 | Colchón |

> **Por qué así:** los OKRs son tu tarea de mayor carga cognitiva y necesitan continuidad. Tu único día libre es el único lugar donde caben 4h sin fragmentarse. Protege este bloque agresivamente.

---

## MIÉRCOLES — Día de la demo

| Hora | Bloque |
|------|--------|
| 9:00–9:30 | Email stakeholders (parte 1) |
| 9:30–11:00 | **Preparar demo — Bloque 2** (1.5h) → **total 3h** ✅ |
| 11:00–11:30 | 1:1 Reporte B ✅ |
| 11:30–1:00 | Trabajo reactivo / Slack / revisiones |
| 1:00–2:00 | Almuerzo |
| 2:00–2:45 | **Ensayo de la demo + setup técnico** |
| 2:45–3:00 | Buffer pre-demo |
| 3:00–4:00 | 🔒 **DEMO DE PRODUCTO** |
| 4:00–4:30 | Notas de la demo + action items en caliente |
| 4:30–5:00 | Email stakeholders (parte 2) ✅ |
| 5:00–6:00 | Colchón |

> **Por qué así:** el ensayo el mismo día es crítico, no opcional. La ventana 4:00–4:30 captura feedback mientras está fresco — esto suele ser lo primero que se sacrifica y lo que más cuesta después.

---

## JUEVES — Día de hiring

| Hora | Bloque |
|------|--------|
| 9:00–9:30 | Email stakeholders (parte 1) |
| 9:30–10:00 | Prep de entrevistas (repasar CVs) |
| 10:00–1:00 | 🔒 **Entrevistas de hiring** |
| 1:00–2:00 | Almuerzo |
| 2:00–2:45 | **Debrief de entrevistas + scorecards** |
| 2:45–3:15 | 1:1 Reporte C ✅ |
| 3:15–4:30 | Follow-ups de la demo / trabajo de PRDs pendiente |
| 4:30–5:00 | Email stakeholders (parte 2) ✅ |
| 5:00–6:00 | Colchón |

> **Por qué así:** 3h de entrevistas te dejan agotado. No programes nada cognitivamente exigente después — el debrief es obligatorio hacerlo el mismo día o pierdes señal, pero es trabajo de recordar, no de crear.

---

## VIERNES — Cierre y preparación

| Hora | Bloque |
|------|--------|
| 9:00–9:30 | Email stakeholders (parte 1) |
| 9:30–11:00 | **Overflow buffer** (lo que se desbordó esta semana) |
| 11:00–1:00 | Trabajo flexible / colaboración con equipo |
| 1:00–2:00 | Almuerzo |
| 2:00–3:00 | **Revisión de OKRs Q3** (lectura fresca + pulido) |
| 3:00–3:45 | Prep de la retrospectiva |
| 3:45–4:00 | Buffer |
| 4:00–5:00 | 🔒 **Retrospectiva** |
| 5:00–5:30 | Email stakeholders (parte 2) ✅ |
| 5:30–6:00 | **Planificación de la próxima semana** |

> **Por qué así:** revisar los OKRs 3 días después de escribirlos es cuando detectas los problemas reales. El viernes es tu día con más colchón — úsalo para absorber lo que inevitablemente se corra.

---

## Verificación de cobertura

| Tarea | Requerido | Asignado | Estado |
|-------|-----------|----------|--------|
| Preparar demo | 3h | Mar 1.5h + Mié 1.5h | ✅ |
| Revisar PRDs | 2h | Lun 2h | ✅ |
| OKRs Q3 | 4h | Mar 4h (+1h revisión Vie) | ✅ |
| Emails stakeholders | 1h × 5 días | 2 × 30 min diarios | ✅ |
| Métricas de producto | 1h | Lun 12:00–1:00 | ✅ |
| 1:1s (3 × 30 min) | 1.5h | Mar, Mié, Jue | ✅ |
| **Total** | **~16h** | — | ✅ |

---

## Tres decisiones clave que tomé

**1. Los OKRs van completos el martes.** Partirlos en trozos de 1h en días distintos te costaría ~30 min de recontextualización por sesión. Tu único día libre es el único sitio donde caben enteros.

**2. Los 1:1s se distribuyen en días distintos.** Tentador agruparlos, pero separados te dan señal continua del equipo y te dejan reaccionar a lo que surja en el primero antes del tercero.

**3. Hay ~4h de colchón sin asignar.** Es intencional. Un plan al 100% de capacidad falla el martes a mediodía. Si no las usas, son tiempo para pensamiento estratégico — no lo rellenes por defecto.

## Reglas de protección

- **Bloques 🧠 = sin interrupciones.** Slack en "no molestar", calendario como "ocupado".
- **Si algo se cae:** sacrifica primero el buffer del viernes, luego los PRDs del lunes, nunca los OKRs ni el ensayo de la demo.
- **Los buffers post-reunión no son negociables.** 15–30 min después de directivos, demo y entrevistas es lo que evita que la semana se descarrile.

¿Quieres que ajuste algo? Puedo redistribuir si tu pico de energía no es por la mañana, o si prefieres agrupar los 1:1s en un solo día.