# Qwen 3.8 Max — ocr_extraction/handwritten_notes_extraction

- model_id: `qwen/qwen3.8-max`
- success: True  | final: 7.22 | quality: 8.57
- latency_total: 42.945s | tokens_per_second: 47.7
- input_tokens: 518 | output_tokens: 2050

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un sistema de OCR que interpreta notas manuscritas. Debes descifrar abreviaciones y organizar la informacion.

**user:**

Tengo una foto de notas manuscritas de una reunion. El texto reconocido (con errores tipicos de OCR en escritura a mano) es:

"Reunlon equlpo prod - 14/04/26
Asist: JP, MaJo, Seba, Cami (falt0 Nico)

1) Lanzamient0 v2.0 - mover de abr 28 a may 5
   - falta QA en modul0 pagos
   - bug crit en API webho0ks (Seba lo toma)

2) Metricas Q1:
   - MRR 52.1k (+15% vs Q4)
   - churn baj0 a 3.1% (obj era 3.5%)
   - NPS subio a 51 (re bueno!!)

3) Contratar 2 devs sr + 1 QA
   - presup aprob: $8M CLP/mes x 3 pax
   - JP hace JD p/ lunes

4) Prox reunion: lun 21/04 10am

Action items:
- Seba: fix webhook bug p/ mierc 16/04
- MaJo: actualzr roadmap en Notion
- Cami: prep demo p/ cliente Falabella (23/04)
- JP: publicar JDs en LinkedIn + GetOnBrd"

Tareas:
1. Corrige los errores de OCR y presenta el texto limpio
2. Extrae los action items en formato estructurado
3. Identifica las fechas mencionadas y crea un timeline

Responde en JSON:
{
  "texto_corregido": "",
  "fecha_reunion": "",
  "asistentes": [],
  "ausentes": [],
  "action_items": [{"responsable": "", "tarea": "", "fecha_limite": ""}],
  "fechas_clave": [{"fecha": "", "evento": ""}],
  "decisiones": []
}


## Respuesta completa

We need answer in JSON only likely. User asks Spanish. Need parse OCR, correct text, extract action items, dates timeline, etc. done. Now think through content.

We need produce valid JSON. Need include texto_corregido maybe multiline string with corrected notes. Need fecha_reunion: probably 2026-04-14? Original "14/04/26" likely 14 April 2026. Asistentes: JP, MaJo, Seba, Cami. Ausentes: Nico.

Action items:
- Seba: fix webhook bug p/ mierc 16/04. Need date: 16/04/2026? Since meeting 14/04/26. Note: 16/04/2026 is Thursday? Let's check: 2026-04-14 Tuesday? 2026-04-16 Thursday. They say mierc 16/04, inconsistency. But should maybe correct to miércoles 15/04? Hmm OCR says "p/ mierc 16/04". In 2026, April 16 is Thursday. Could be typo in handwritten notes or OCR. Need identify dates mentioned and timeline. Should we preserve given date? For action item fecha_limite maybe "2026-04-16 (miércoles, posible error; se asume 16/04)"? But structured likely date. Need decide. User asks corrige errores OCR. Could correct "mierc" to "miércoles". But date 16/04 may be wrong. If meeting Tue 14/04/26, next Wednesday is 15/04. But note says "prox reunion: lun 21/04 10am". 2026 April 21 is Tuesday? Let's verify. 2026-04-01 Wednesday? Let's calculate: 2026 Jan 1 Thursday? 2025 Jan1 Wed, 2025 non-leap -> 2026 Jan1 Thursday. Jan31, Feb28, Mar31 = 90 days to Apr1? Jan1 Thu, Apr1 = day 91? Jan1 +90 days. 90 mod7=6, Thu+6=Wed. So Apr1 Wed. Apr14 = Tue (Apr1 Wed, 8 Wed, 14 Tue). Apr16 Thu. Apr21 Tue. So "lun 21/04" also inconsistent: 21/04/2026 is Tuesday. Maybe year 2025? 14/04/25 Monday? 2025 Apr14 Monday, 16 Wednesday, 21 Monday. But text says 14/04/26 maybe OCR misread 25? It says "14/04/26". If meeting year 2025, dates align: 14/04 Monday? Wait 2025 Apr14 Monday, 16 Wed, 21 Mon. That matches "mierc 16/04" and "lun 21/04". But note says "14/04/26" maybe should be 2025? Could be 14/04/25 with OCR 6 for 5? But also "abr 28 a may 5" 2025: Apr28 Mon, May5 Mon. Q1 etc. Could be 2025. But user provided 26. We need likely correct OCR errors, but not infer year? Maybe "14/04/26" means 2026. Then weekday mismatches. Maybe in notes they used incorrect weekdays, not OCR. Task is OCR correction, not calendar validation. But could mention possible inconsistency? JSON doesn't allow comments maybe. Need output clean. Could set fecha_reunion "2026-04-14". For action item Seba fecha_limite "2026-04-16". For next meeting "2026-04-21". But if weekdays corrected? texto_corregido could say "martes 16/04"? Hmm.

Maybe better to normalize dates to ISO and keep event descriptions with original weekday? Need timeline. fechas_clave: 
- 2026-04-14 Reunión de equipo producto
- 2026-04-16 Fecha límite Seba fix webhook bug (nota dice miércoles; en 2026 es jueves)
- 2026-04-21 Próxima reunión (nota dice lunes; en 2026 es martes)
- 2026-04-23 Demo cliente Falabella (Cami)
- 2026-04-28 Lanzamiento v2.0 original? "mover de abr 28 a may 5" so original launch Apr28, new launch May5. Need include both? Timeline: 2026-04-28: fecha original lanzamiento v2.0 (movida), 2026-05-05: nueva fecha lanzamiento v2.0. Also "lunes" for JD: "JP hace JD p/ lunes". Which Monday? Meeting 14/04, next Monday is 20/04 if 2026? But if note says prox reunion lun 21/04, maybe Monday 21? Wait if meeting 14/04 and "JP hace JD p/ lunes" likely Monday 20/04? In 2026, Monday Apr20. In 2025, Monday Apr21. The action items list doesn't include JP's JD? Actually action items includes JP publish JDs in LinkedIn + GetOnBrd. No explicit date, but in decisions: JP hace JD p/ lunes. Could include fecha_clave: 2026-04-20? If we assume next Monday after 14 Apr 2026 is 20 Apr. But note says prox reunion lun 21/04, inconsistent. Could be 2025, Monday 21. Need decide.

Maybe the safe approach: Do not invent dates not explicit. For "JD p/ lunes", we can set fecha_limite maybe "2026-04-20 (lunes siguiente)"? But if meeting date is 2026-04-14, next Monday is 2026-04-20. But note "Prox reunion: lun 21/04" suggests they think Monday is 21, maybe they think 14/04/25? Hmm.

Could include action item for JP? The provided Action items includes JP: publicar JDs... no date. But also point 3 says JP hace JD p/ lunes. We can combine: responsible JP, tarea "Redactar JD y publicar en LinkedIn + GetOnBrd", fecha_limite "2026-04-20"? But if we use next Monday. Need maybe include two tasks? Action items from list: Seba, MaJo, Cami, JP. But point 3 says JP hace JD p/ lunes; action items says publicar JDs. Could set JP's fecha_limite "lunes siguiente a la reunión (2026-04-20)" or "2026-04-20". But if we consider 21/04 as lunes, maybe 2026-04-21? But 21 is not Monday. We need maybe output ISO date for "lunes 21/04" if note says so? But if fecha_reunion 2026, then 21/04 is Tuesday. Could set "2026-04-21" for next meeting anyway.

Need JSON valid, no trailing commas. Could include newline in texto_corregido using \n. Need ensure quotes escaped? final should be raw JSON. Could include accents. Need maybe use Spanish.

Let's craft corrected text:
"Reunión equipo producto - 14/04/26
Asistentes: JP, MaJo, Seba, Cami (faltó Nico)

1) Lanzamiento v2.0 - mover del 28 de abril al 5 de mayo
   - Falta QA en módulo pagos
   - Bug crítico en API webhooks (Seba lo toma)

2) Métricas Q1:
   - MRR 52.1k (+15% vs Q4)
   - Churn bajó a 3.1% (el objetivo era 3.5%)
   - NPS subió a 51 (¡muy bueno!)

3) Contratar 2 devs sr + 1 QA
   - Presupuesto aprobado: $8M CLP/mes por 3 personas
   - JP hace JD para el lunes

4) Próxima reunión: lunes 21/04 10am

Action items:
- Seba: corregir bug de webhooks para el miércoles 