# Claude Opus 5 Fast — task_management/weekly_planning

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 7.92 | quality: 10.0
- latency_total: 23.342s | tokens_per_second: 236.6
- input_tokens: 320 | output_tokens: 5523
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente estructurada, ofreciendo un plan semanal detallado que un emprendedor podría usar directamente.

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

**Supuestos** (dime si cambian y ajusto): jornada 9:00–18:00, almuerzo 13:00–14:00, viernes con energía baja después de las 15:00.

---

## 🗓️ LUNES — "Alinear y arrancar"

| Hora | Bloque | Tipo |
|---|---|---|
| 9:00–11:00 | 🔒 Reunión de directivos | Fijo |
| 11:00–11:30 | Descarga de acuerdos + action items del comité | Buffer |
| 11:30–12:30 | **Emails stakeholders (1h)** | Tarea 4 |
| 12:30–13:00 | Prep almuerzo con cliente (repasar cuenta, 3 preguntas clave) | Buffer |
| 13:00–14:00 | 🔒 Almuerzo con cliente | Fijo |
| 14:00–14:30 | Notas del cliente → tickets/insights | Buffer |
| 14:30–16:30 | **Preparar demo — bloque 1 (2h)** | Tarea 1 |
| 16:30–17:00 | **1:1 Reporte #1** | Tarea 6 |
| 17:00–18:00 | Colchón / desbordes del día | Buffer |

**Por qué:** los emails van justo después del comité, cuando tienes contexto fresco de decisiones ejecutivas y puedes responder con autoridad en una sola pasada.

---

## 🗓️ MARTES — "Día de trabajo profundo" ⭐

| Hora | Bloque | Tipo |
|---|---|---|
| 9:00–10:00 | **Emails stakeholders (1h)** | Tarea 4 |
| 10:00–12:00 | **OKRs Q3 — bloque 1 (2h)** · borrador de objetivos | Tarea 3 |
| 12:00–13:00 | Colchón / trabajo reactivo | Buffer |
| 13:00–14:00 | Almuerzo | — |
| 14:00–16:00 | **OKRs Q3 — bloque 2 (2h)** · key results + métricas | Tarea 3 |
| 16:00–17:00 | **Revisar PRDs — bloque 1 (1h)** | Tarea 2 |
| 17:00–17:30 | **1:1 Reporte #2** | Tarea 6 |
| 17:30–18:00 | Cierre / preparar miércoles | Buffer |

**Por qué:** los OKRs son la tarea más cognitivamente cara (4h). Este es el único día sin interrupciones — protégelo con bloqueo en calendario y estado "no disponible".

---

## 🗓️ MIÉRCOLES — "Día de demo"

| Hora | Bloque | Tipo |
|---|---|---|
| 9:00–10:00 | **Emails stakeholders (1h)** | Tarea 4 |
| 10:00–11:00 | **Preparar demo — bloque 2 (1h)** · cierre de slides | Tarea 1 |
| 11:00–12:00 | **Revisar PRDs — bloque 2 (1h)** | Tarea 2 |
| 12:00–13:00 | Colchón | Buffer |
| 13:00–14:00 | Almuerzo | — |
| 14:00–14:45 | **Ensayo en voz alta + prueba técnica** (audio, pantalla, entorno) | Crítico |
| 14:45–15:00 | Respirar / no agendar nada | Buffer |
| 15:00–16:00 | 🔒 **DEMO DE PRODUCTO** | Fijo |
| 16:00–16:30 | Debrief: feedback recibido → backlog | Buffer |
| 16:30–18:00 | Libre / seguimiento de demo | Buffer |

**Regla de oro:** nada se agenda entre 14:00 y 15:00. La causa #1 de demos malas es no ensayar en el entorno real.

---

## 🗓️ JUEVES — "Personas"

| Hora | Bloque | Tipo |
|---|---|---|
| 9:00–9:45 | **Emails stakeholders (45 min, versión comprimida)** | Tarea 4 |
| 9:45–10:00 | Repaso de CVs y guion de entrevista | Buffer |
| 10:00–13:00 | 🔒 Entrevistas de hiring | Fijo |
| 13:00–14:00 | Almuerzo (real, sin pantalla — vienes de 3h intensas) | — |
| 14:00–14:45 | Scorecards de candidatos **el mismo día** | Crítico |
| 14:45–15:15 | **1:1 Reporte #3** | Tarea 6 |
| 15:15–16:15 | **Emails — completar los 15 min pendientes + colchón** | Tarea 4 |
| 16:15–18:00 | Colchón / trabajo reactivo acumulado | Buffer |

**Por qué:** llenar scorecards inmediatamente después de las entrevistas es innegociable; a las 24h tu recuerdo pierde ~50% de precisión.

---

## 🗓️ VIERNES — "Medir y cerrar"

| Hora | Bloque | Tipo |
|---|---|---|
| 9:00–10:00 | **Emails stakeholders (1h)** | Tarea 4 |
| 10:00–11:00 | **Revisar métricas del producto (1h)** | Tarea 5 |
| 11:00–12:00 | **OKRs Q3 — pulido final** (buffer de la tarea 3) | Tarea 3 |
| 12:00–13:00 | Colchón | Buffer |
| 13:00–14:00 | Almuerzo | — |
| 14:00–15:00 | Cierre de PRDs / desbordes de la semana | Buffer |
| 15:00–16:00 | Prep retro: revisar sprint, datos, temas a levantar | Buffer |
| 16:00–17:00 | 🔒 Retrospectiva | Fijo |
| 17:00–18:00 | Planificación semana siguiente + inbox a cero | Cierre |

**Por qué las métricas van el viernes:** llegas a la retro con datos frescos **y** llegas al comité del lunes 9:00 con los números ya digeridos. Mata dos pájaros.

---

## ✅ Verificación de cobertura

| # | Tarea | Requerido | Asignado | Estado |
|---|---|---|---|---|
| 1 | Preparar demo | 3h | Lun 2h + Mié 1h (+45 min ensayo) | ✅ |
| 2 | Revisar PRDs | 2h | Mar 1h + Mié 1h | ✅ |
| 3 | OKRs Q3 | 4h | Mar 4h (+1h pulido vie) | ✅ |
| 4 | Emails stakeholders | 5h (1h/día) | Lun/Mar/Mié/Vie 1h + Jue 45+15 min | ✅ |
| 5 | Métricas | 1h | Vie 10:00–11:00 | ✅ |
| 6 | 1:1s (3×30 min) | 1.5h | Lun, Mar, Jue | ✅ |
| | **Total comprometido** | **16.5h** | | |
| | Reuniones fijas | 8h | | |
| | **Colchón disponible** | **~11h** | | |

Ese colchón de ~11h no es tiempo libre: es tu seguro contra lo inevitable (escalaciones, un bug en producción, un directivo que "solo necesita 5 minutos").

---

## 🛡️ Reglas para que el plan sobreviva

1. **Bloquea todo en el calendario ya**, incluidos los buffers, con títulos que disuadan ("Focus – OKRs Q3", no "Disponible").
2. **Prioridad si algo se cae:** Demo (Mié) > Scorecards (Jue) > OKRs > 1:1s > PRDs > Métricas. Los emails se comprimen a 30 min antes de sacrificar otra cosa.
3. **Regla de reprogramación de 1:1s:** si mueves uno, se mueve *dentro de la misma semana*, nunca se cancela. Cancelar 1:1s es la señal más rápida de que el equipo deja de confiar.
4. **Martes es sagrado.** Si algo tiene que entrar el martes, que entre 12:00–13:00. Si el martes se rompe, los OKRs se van a la semana siguiente.
5. **Emails en batch, no en goteo.** Una sola ventana al día, notificaciones apagadas el resto del tiempo.

---

## ⚠️ Riesgos que veo

- **Lunes está muy cargado**: comité de 2h + almuerzo de cliente parte el día en trozos pequeños. Los 2h de demo prep de 14:30 son tu bloque más frágil de la semana. Si sabes que sueles salir agotado del comité, considera mover 1h de demo prep al martes por la mañana.
- **Jueves**: 3h de entrevistas seguidas te dejan sin batería. No metas nada creativo después de las 15:00 ese día — por eso ahí solo hay emails y colchón.
- **4h de OKRs en un solo día es ambicioso.** Divide el objetivo: bloque 1 = borrador feo y completo; bloque 2 = refinar. No intentes escribir en limpio a la primera.

¿Quieres que ajuste algo? Por ejemplo: si tu jornada real es 8:00–17:00, si los 1:1s tienen días fijos ya acordados, o si los OKRs necesitan input de otras personas antes de que puedas escribirlos (eso cambiaría bastante el orden).