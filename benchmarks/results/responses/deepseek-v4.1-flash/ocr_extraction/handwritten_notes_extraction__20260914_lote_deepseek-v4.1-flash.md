# DeepSeek V4.1 Flash — ocr_extraction/handwritten_notes_extraction

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 8.58 | quality: 10.0
- latency_total: 116.205s | tokens_per_second: 62.7
- input_tokens: 498 | output_tokens: 7282

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
  "texto_corregido": "Reunión equipo prod - 14/04/25\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (¡¡re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 pax\n   - JP hace JD para lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBoard",
  "fecha_reunion": "14/04/25",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Fix webhook bug",
      "fecha_limite": "16/04/25"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "23/04/25"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar JDs en LinkedIn + GetOnBoard",
      "fecha_limite": ""
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/25",
      "evento": "Reunión equipo prod"
    },
    {
      "fecha": "16/04/25",
      "evento": "Fix webhook bug (Seba)"
    },
    {
      "fecha": "21/04/25",
      "evento": "Próxima reunión (lunes 10am); JP entrega JDs"
    },
    {
      "fecha": "23/04/25",
      "evento": "Demo cliente Falabella (Cami)"
    },
    {
      "fecha": "28/04/25",
      "evento": "Fecha original de lanzamiento v2.0 (movida)"
    },
    {
      "fecha": "05/05/25",
      "evento": "Nuevo lanzamiento v2.0"
    }
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 del 28/04 al 05/05",
    "Falta QA en módulo pagos para v2.0",
    "Seba tomará el bug crítico en API webhooks",
    "Contratar 2 devs sr + 1 QA; presupuesto aprobado de $8M CLP/mes x 3 pax",
    "JP hará las JDs para el lunes",
    "Próxima reunión el lunes 21/04 a las 10am"
  ]
}