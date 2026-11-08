# Llama 4 Maverick — ocr_extraction/handwritten_notes_extraction

- model_id: `meta-llama/llama-4-maverick`
- success: True  | final: 9.06 | quality: 10.0
- latency_total: 7.957s | tokens_per_second: 87.2
- input_tokens: 440 | output_tokens: 694

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

Aquí está la respuesta en formato JSON:

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crit en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presup aprob: $8M CLP/mes x 3 pax\n   - JP hace JD p/ lunes\n\n4) Próx reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug p/ mierc 16/04\n- MaJo: actualizr roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "14/04/26",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {"responsable": "Seba", "tarea": "fix webhook bug", "fecha_limite": "16/04"},
    {"responsable": "MaJo", "tarea": "actualizar roadmap en Notion", "fecha_limite": null},
    {"responsable": "Cami", "tarea": "prep demo p/ cliente Falabella", "fecha_limite": "23/04"},
    {"responsable": "JP", "tarea": "publicar JDs en LinkedIn + GetOnBrd", "fecha_limite": null}
  ],
  "fechas_clave": [
    {"fecha": "14/04/26", "evento": "Reunión equipo prod"},
    {"fecha": "28/04", "evento": "Lanzamiento v2.0 (original)"},
    {"fecha": "05/05", "evento": "Lanzamiento v2.0 (nueva fecha)"},
    {"fecha": "16/04", "evento": "Fix webhook bug"},
    {"fecha": "21/04", "evento": "Próx reunión equipo prod"},
    {"fecha": "23/04", "evento": "Demo para cliente Falabella"}
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 de abr 28 a may 5",
    "Contratar 2 devs sr + 1 QA con presupuesto aprobado de $8M CLP/mes x 3 pax"
  ]
}
```

Nota que algunas fechas límite para los action items no están especificadas en el texto original, por lo que se han dejado como `null`. Además, se han identificado algunas decisiones importantes tomadas durante la reunión y se han incluido en el campo "decisiones".