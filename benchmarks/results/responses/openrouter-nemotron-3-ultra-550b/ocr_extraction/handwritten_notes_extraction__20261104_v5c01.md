# Nemotron 3 Ultra 550B — ocr_extraction/handwritten_notes_extraction

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 9.1 | quality: 10.0
- latency_total: 3.792s | tokens_per_second: 207.6
- input_tokens: 479 | output_tokens: 787

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

{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (falta Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crit en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presup aprob: $8M CLP/mes x 3 pax\n   - JP hace JD p/ lunes\n\n4) Próx reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug p/ miérc 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "2026-04-14",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {"responsable": "Seba", "tarea": "Fix webhook bug en API", "fecha_limite": "2026-04-16"},
    {"responsable": "MaJo", "tarea": "Actualizar roadmap en Notion", "fecha_limite": null},
    {"responsable": "Cami", "tarea": "Preparar demo para cliente Falabella", "fecha_limite": "2026-04-23"},
    {"responsable": "JP", "tarea": "Publicar JDs en LinkedIn y GetOnBoard", "fecha_limite": "2026-04-20"}
  ],
  "fechas_clave": [
    {"fecha": "2026-04-14", "evento": "Reunión equipo producto"},
    {"fecha": "2026-04-16", "evento": "Deadline fix webhook bug (Seba)"},
    {"fecha": "2026-04-20", "evento": "Deadline JP publica JDs (lunes)"},
    {"fecha": "2026-04-21", "evento": "Próxima reunión equipo 10am"},
    {"fecha": "2026-04-23", "evento": "Demo cliente Falabella (Cami)"},
    {"fecha": "2026-05-05", "evento": "Lanzamiento v2.0 (movido desde 28 abr)"}
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 del 28 abril al 5 mayo por falta de QA en módulo pagos",
    "Aprobar presupuesto $8M CLP/mes para contratar 2 devs senior + 1 QA",
    "Seba se hace cargo del bug crítico en API webhooks"
  ]
}