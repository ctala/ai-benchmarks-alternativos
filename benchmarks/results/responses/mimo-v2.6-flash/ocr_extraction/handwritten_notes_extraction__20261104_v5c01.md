# MiMo V2.6 Flash — ocr_extraction/handwritten_notes_extraction

- model_id: `xiaomi/mimo-v2.6-flash`
- success: True  | final: 8.97 | quality: 10.0
- latency_total: 16.689s | tokens_per_second: 47.6
- input_tokens: 479 | output_tokens: 794

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
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (¡re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presup aprob: $8M CLP/mes x 3 pax\n   - JP hace JD p/ lunes\n\n4) Próx reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug p/ mierc 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "14/04/26",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {"responsable": "Seba", "tarea": "Fix webhook bug (API webhooks)", "fecha_limite": "16/04"},
    {"responsable": "MaJo", "tarea": "Actualizar roadmap en Notion", "fecha_limite": null},
    {"responsable": "Cami", "tarea": "Preparar demo para cliente Falabella", "fecha_limite": "23/04"},
    {"responsable": "JP", "tarea": "Hacer JDs de los 3 puestos (2 devs sr + 1 QA)", "fecha_limite": "Lunes 21/04"},
    {"responsable": "JP", "tarea": "Publicar JDs en LinkedIn + GetOnBrd", "fecha_limite": null}
  ],
  "fechas_clave": [
    {"fecha": "14/04", "evento": "Reunión de equipo prod"},
    {"fecha": "16/04", "evento": "Fix del bug de webhooks (Seba)"},
    {"fecha": "21/04", "evento": "Próxima reunión (10am) / JP entrega JDs"},
    {"fecha": "23/04", "evento": "Demo para cliente Falabella (Cami)"},
    {"fecha": "28/04", "evento": "Fecha original de lanzamiento v2.0 (movida)"},
    {"fecha": "05/05", "evento": "Nueva fecha de lanzamiento v2.0"}
  ],
  "decisiones": [
    "Postergar lanzamiento v2.0 del 28 de abril al 5 de mayo",
    "Seba toma el bug crítico de la API de webhooks",
    "Aprobar presupuesto de $8M CLP/mes para contratar 3 personas (2 devs senior + 1 QA)",
    "JP se encarga de los JDs y su publicación en LinkedIn + GetOnBrd"
  ]
}