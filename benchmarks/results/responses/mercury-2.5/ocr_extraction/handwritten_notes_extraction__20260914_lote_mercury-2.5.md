# Mercury 2.5 — ocr_extraction/handwritten_notes_extraction

- model_id: `inception/mercury-2.5`
- success: True  | final: 9.39 | quality: 10.0
- latency_total: 4.237s | tokens_per_second: 725.3
- input_tokens: 476 | output_tokens: 3073

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
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (falta Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en modulo pagos\n   - bug crit en API webhooks (Seba lo toma)\n\n2) Metrics Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presup aprob: $8M CLP/mes x 3 pax\n   - JP hace JD p/ lunes\n\n4) Prox reunion: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug p/ mierc 16/04\n- MaJo: actualzar roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "14/04/26",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "fix webhook bug",
      "fecha_limite": "16/04"
    },
    {
      "responsable": "MaJo",
      "tarea": "actualzar roadmap en Notion",
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "prep demo p/ cliente Falabella",
      "fecha_limite": "23/04"
    },
    {
      "responsable": "JP",
      "tarea": "publicar JDs en LinkedIn + GetOnBrd",
      "fecha_limite": ""
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/26",
      "evento": "Reunión"
    },
    {
      "fecha": "16/04",
      "evento": "Fix webhook bug (Seba)"
    },
    {
      "fecha": "21/04",
      "evento": "Próxima reunión"
    },
    {
      "fecha": "23/04",
      "evento": "Demo cliente Falabella (Cami)"
    },
    {
      "fecha": "28/04",
      "evento": "Lanzamiento v2.0 (original)"
    },
    {
      "fecha": "05/05",
      "evento": "Lanzamiento v2.0 (nuevo)"
    }
  ],
  "decisiones": [
    "Lanzamiento v2.0 movido de abr 28 a may 5",
    "Contratar 2 devs sr + 1 QA",
    "Presupuesto aprobado: $8M CLP/mes x 3 pax"
  ]
}