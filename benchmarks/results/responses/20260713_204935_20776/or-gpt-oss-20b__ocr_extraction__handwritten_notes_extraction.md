# GPT-OSS 20B — ocr_extraction/handwritten_notes_extraction

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 9.26 | quality: 10.0
- latency_total: 13.53s | tokens_per_second: 151.4
- input_tokens: 488 | output_tokens: 2048
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, corrigiendo efectivamente los errores de OCR y estructurando la información de manera útil, aunque podría haber sido más clara en la interpretación de la fecha de la reunión.

## Respuesta completa

We need to produce JSON with corrected text, date of meeting, attendees, absentees, action items, key dates, decisions. Let's parse the text.

Original with errors:

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

We correct OCR errors: "Reunlon" -> "Reunión", "equlpo" -> "equipo", "prod" -> "prod." maybe "producto" or "product" but likely "product" team. "14/04/26" is 14/04/2026? Actually likely 14/04/2026? But meeting date might be 14/04/2026? But meeting is in 2026? Unlikely. Could be 14/04/2026 as a future date. But "Prox reunion: lun 21/04 10am" indicates next meeting 21/04 at 10am. So current meeting likely 14/04/2026. But maybe they use two-digit year: 26 indicates 2026. So yes.

"Asist" -> "Asistentes" maybe. "falt0" -> "falta". So "falt0" means "falta" (absent). So "Nico" absent.

"Lanzamient0" -> "Lanzamiento". "de abr 28 a may 5" -> "de abril 28 a mayo 5". "falta QA en modul0 pagos" -> "falta QA en módulo pagos". "bug crit en API webho0ks" -> "bug crítico en API webhooks". "Seba lo toma" remains.

"Metricas Q1:" -> "Métricas Q1". "churn baj0 a 3.1%" -> "churn bajó a 3.1%". "NPS subio a 51" -> "NPS subió a 51". "(re bueno!!)" -> "¡re bueno!!".

"Contratar 2 devs sr + 1 QA" -> "Contratar 2 devs senior + 1 QA". "presup aprob: $8M CLP/mes x 3 pax" -> "presupuesto aprobado: $8M CLP/mes x 3 personas". "JP hace JD p/ lunes" -> "JP hace JD para lunes".

"Prox reunion: lun 21/04 10am" -> "Próxima reunión: lunes 21/04 10am".

Action items: "Seba: fix webhook bug p/ mierc 16/04" -> "Seba: arreglar bug de webhook para miércoles 16/04". "MaJo: actualzr roadmap en Notion" -> "MaJo: actualizar roadmap en Notion". "Cami: prep demo p/ cliente Falabella (23/04)" -> "Cami: preparar demo para cliente Falabella (23/04)". "JP: publicar JDs en LinkedIn + GetOnBrd" -> "JP: publicar JDs en LinkedIn + GetOnBoard".

Also "JP hace JD p/ lunes" earlier: maybe same as action item. But we need action items structured: responsable, tarea, fecha_limite.

List:

1. Seba: arreglar bug de webhook para miércoles 16/04. date: 16/04 (year same as meeting). Format: 2026? likely 2026.

2. MaJo: actualizar roadmap en Notion. No deadline given. Might be by next meeting? But no explicit date. We could set fecha_limite as null.

3. Cami: preparar demo para cliente Falabella (23/04). date: 23/04.

4. JP: publicar JDs en LinkedIn + GetOnBoard. Deadline? Not specified. Could be by next meeting. But maybe implicitly by meeting? We can set null.

Also action item: "JP hace JD p/ lunes" earlier, that's same as JP action: publish job descriptions by Monday. Monday after meeting: 17/04? Actually meeting on 14/04, Monday 17/04. But they mention "p/ lunes" maybe meaning "para lunes" - next Monday. So we can set date 17/04. But we also have JP action to publish JDs. So we can treat as same. Let's include date 17/04.

But we already have JP action: "publicar JDs en LinkedIn + GetOnBoard". So incorporate date 17/04. So action item: JP: publicar JDs en LinkedIn + GetOnBoard by lunes 17/04.

Also maybe "JP hace JD p/ lunes" is a subaction. We'll include.

Now timeline: key dates:

- 14/04/26: Reunión de equipo product.
- 28/04: Lanzamiento v2.0 originally scheduled? Actually "mover de abr 28 a may 5" indicates move from April 28 to May 5. So original launch date April 28 moved to May 5. So event: Launch v2.0 scheduled for 05/05/26.
- 16/04: Eve: Seba fix webhook bug.
- 17/04: JP publish JDs.
- 21/04: Próxima reunión.
- 23/04: Cami demo Falabella.

Also metrics: MRR 52.1k, churn 3.1% vs Q4, NPS 51.

Decisions: 1) Change launch date to May 5. 2) Hire 2 senior devs + 1 QA with budget. 3) JP will create job descriptions. 4) Next meeting scheduled. 5) QA pending in payments module. 6) Bug critical in API webhooks. But those are action items.

We need "decisiones": list decisions.

Possible decisions extracted:

- Launch v2.0 moved from April 28 to May 5.
- Hire 2 senior developers and 1 QA with budget of $8M CLP per month for 3 people.
- JP will create job descriptions by Monday.
- Next meeting scheduled for Monday 21/04 at 10am.

Also maybe "QA needed in payments module" is a pending issue, not decision.

Now produce JSON with fields.

"texto_corregido": we need present cleaned up text. Provide corrected version of entire notes. We might format as a paragraph or maintain numbering. Provide a cleaned text.

"fecha_reunion": "2026-04-14" (ISO). "asistentes": ["JP", "MaJo", "Seba", "Cami"].

"ausentes": ["Nico"].

"action_items": array of objects. Provide fields.

"fechas_clave": list of objects with date and event. Provide key events: meeting, launch, bug fix, JD publication, next meeting, demo.

"decisiones": list of decision strings.

Let's craft.

Action items:

1. {"responsable":"Seba","tarea":"Arreglar bug de webhook","fecha_limite":"2026-04-16"}.

2. {"responsable":"MaJo","tarea":"Actualizar roadmap en Notion","fecha_limite":null}.

3. {"responsable":"Cami","tarea":"Preparar demo para cliente Falabella","fecha_limite":"2026-04-23"}.

4. {"responsable":"JP","tarea":"Publicar JDs en LinkedIn + GetOnBoard","fecha_limite":"2026-04-17"}.

Also, optionally "JP": "Crear JD para puestos" same as above.

Now fechas clave:

- 2026-04-14: Reunión de equipo product.
- 2026-04-28: Fecha original de lanzamiento v2.0 (moved).
- 2026-05-05: Nueva fecha de lanzamiento v2.0.
- 2026-04-16: Fecha límite para bug webhook.
- 2026-04-17: Fecha límite para publicar JDs.
- 2026-04-21: Próxima reunión.
- 2026-04-23: Demo Falabella.

Also metrics: maybe not needed.

Decisions: list strings.

Let's produce JSON.

Ensure proper escaping.

Also "texto_corregido": produce corrected notes text, maybe with proper punctuation.

Let's craft corrected text:

"Reunión de equipo product - 14/04/26
Asistentes: JP, MaJo, Seba, Cami (ausente: Nico)

1) Lanzamiento v2.0 - mover de abril 28 a mayo 5
   - falta QA en