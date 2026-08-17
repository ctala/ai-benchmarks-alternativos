# Qwen 3.8 27B — ocr_extraction/handwritten_notes_extraction

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 8.2 | quality: 10.0
- latency_total: 72.867s | tokens_per_second: 28.1
- input_tokens: 518 | output_tokens: 2048

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

Necesito responder en JSON. Debo corregir OCR, extraer action items, fechas, asistentes, ausentes, decisiones. Analizo texto:

"Reunlon equlpo prod - 14/04/26" -> "Reunión equipo prod - 14/04/26"
"Asist: JP, MaJo, Seba, Cami (falt0 Nico)" -> "Asist: JP, MaJo, Seba, Cami (faltó Nico)"

1) Lanzamient0 v2.0 - mover de abr 28 a may 5
   - falta QA en modul0 pagos
   - bug crit en API webho0ks (Seba lo toma)
Corrección: "1) Lanzamiento v2.0 - mover de abr 28 a may 5
   - falta QA en módulo pagos
   - bug crítico en API webhooks (Seba lo toma)"

2) Metricas Q1:
   - MRR 52.1k (+15% vs Q4)
   - churn baj0 a 3.1% (obj era 3.5%)
   - NPS subio a 51 (re bueno!!)
Corrección: "2) Métricas Q1:
   - MRR 52.1k (+15% vs Q4)
   - churn bajó a 3.1% (obj era 3.5%)
   - NPS subió a 51 (re bueno!!)"

3) Contratar 2 devs sr + 1 QA
   - presup aprob: $8M CLP/mes x 3 pax
   - JP hace JD p/ lunes
Corrección: "3) Contratar 2 devs sr + 1 QA
   - presup aprob: $8M CLP/mes x 3 pax
   - JP hace JD p/ lunes"

4) Prox reunion: lun 21/04 10am
Corrección: "4) Próxima reunión: lun 21/04 10am"

Action items:
- Seba: fix webhook bug p/ mierc 16/04
- MaJo: actualzr roadmap en Notion
- Cami: prep demo p/ cliente Falabella (23/04)
- JP: publicar JDs en LinkedIn + GetOnBrd

Corrección: "Action items:
- Seba: fix webhook bug p/ mierc 16/04
- MaJo: actualizar roadmap en Notion
- Cami: prep demo p/ cliente Falabella (23/04)
- JP: publicar JDs en LinkedIn + GetOnBoard"

GetOnBrd probablemente GetOnBoard, plataforma de reclutamiento. Debo decidir. En Chile, GetOnBoard es un job board. Sí, corregir a GetOnBoard. "JD" job descriptions. "fix" se puede dejar en inglés o corregir a "arreglar"? El texto limpio debe corregir errores OCR, no necesariamente traducir. "fix" no es error OCR, pero "actualzr" -> actualizar. "prep" no es error OCR, puede ser abreviatura. Debo mantener estilo? Tarea: corrige errores de OCR y presenta texto limpio. Puede normalizar abreviaciones? "prep" podría ser "preparar". Pero si es OCR, "prep" no es error. "actualzr" claramente OCR por "actualizar". "fix" puede ser jerga. "p/" por para. Dejo p/ o corrijo? "p/" es abreviatura no error OCR. Pero "texto limpio" puede incluir corrección de abreviaturas? El prompt dice descifrar abreviaciones y organizar. Debo probablemente expandir abreviaciones en texto corregido: "para", "lunes", "miércoles". Pero si mantengo texto original, podría ser más fiel. En JSON, texto_corregido puede ser un string con saltos de línea. Debo usar \n.

Asistentes: JP, MaJo, Seba, Cami. Ausentes: Nico.

Action items estructurados:
1 responsable Seba, tarea "Fix webhook bug" o "Arreglar bug de webhooks en API"? El texto dice "fix webhook bug p/ mierc 16/04". Debo extraer. Fecha límite 16/04/26 (miércoles). ¿2026? La reunión es 14/04/26. Sí.
2 MaJo: "actualizar roadmap en Notion". Fecha límite? No mencionada. Puede ser "" o null. El esquema pide string. Usar "" si no hay.
3 Cami: "preparar demo para cliente Falabella" fecha 23/04/26.
4 JP: "publicar JDs en LinkedIn + GetOnBoard" fecha límite? No explícita. En sección 3 dice JP hace JD p/ lunes. Pero action item no tiene fecha. Podría inferir lunes? ¿Lunes siguiente? Reunión 14/04/26 (¿lunes? 14/04/2026 es lunes? Veamos: 2026-04-14. 2026-01-01 jueves? No importa. Próxima reunión lun 21/04. Si 21/04 es lunes, 14/04 también lunes. Entonces "lunes" podría ser 20/04? Si reunión es lunes 14, el lunes siguiente es 21, pero "JP hace JD p/ lunes" en sección 3 probablemente próximo lunes (21/04). Action item JP: publicar JDs no tiene fecha, pero podría estar relacionado. Sin embargo no debe inventar. Dejar "" o inferir "lunes 21/04/26"? La tarea dice identifica fechas mencionadas y crea timeline. No pide inferir límites no mencionados. En action_items fecha_limite puede ser null/"". Para JP, no hay fecha límite explícita en action items. Pero en texto "JP hace JD p/ lunes" es una tarea con fecha lunes. ¿Debería incluir como action item? Los action items listados ya incluyen JP publicar JDs. Podría combinar: responsable JP, tarea "Hacer JD y publicar JDs en LinkedIn + GetOnBoard", fecha_límite "21/04/26"? Pero "hace JD p/ lunes" no está en Action items, pero es un compromiso. Tarea 2: Extrae los action items. Probablemente solo la sección Action items. Pero puede incluir decisiones/fechas. Para no perder info, en decisiones incluir "JP hará JDs para lunes". En action items, JP publicar JDs sin fecha o con fecha 21/04? Si "p/ lunes" se refiere a preparar JD, no publicar. Publicar JDs podría ser después. Mejor dejar fecha_limite "" para JP.

Pero el esquema action_items: [{"responsable": "", "tarea": "", "fecha_limite": ""}]. Si no hay fecha, usar null? JSON permite null. Pero especifica string. Usar "". Para fechas_clave, fechas mencionadas:
- 14/04/26: Reunión equipo prod
- 28/04/26: Lanzamiento v2.0 original (mover de abr 28)
- 05/05/26: Lanzamiento v2.0 nuevo (may 5)
- 16/04/26: Fix webhook bug (Seba)
- 20/04/26? "lunes" para JD. Si 14/04/26 es lunes, el lunes mencionado podría ser 20/04/26? Próxima reunión lun 21/04, así que si 21 es lunes, 14 es lunes. "JP hace JD p/ lunes" en una reunión lunes 14 probablemente se refiere al lunes siguiente, 21/04. Pero también podría ser el mismo lunes? No, "p/ lunes" en reunión lunes 14, a futuro, el lunes siguiente 21. Próxima reunión también lunes 21. Entonces fecha clave: 21/04/26: JDs (JP) y próxima reunión 10am.
- 21/04/26: Próxima reunión 10am
- 23/04/26: Demo cliente Falabella (Cami)
También Q1/Q4 no fechas exactas. MRR etc no fechas.

Debo verificar días: 14/04/26. ¿Es lunes? Calculo: 2026 no bisiesto. 1 ene 2026? 2024-01-01 lunes. 2025-01-01 miércoles (2024 bisiesto +366 -> +1). 2026-01-01 jueves (2025 no bisiesto +365 -> +1). Días hasta 14 abr: ene 31, feb 28, mar 31, abr 1