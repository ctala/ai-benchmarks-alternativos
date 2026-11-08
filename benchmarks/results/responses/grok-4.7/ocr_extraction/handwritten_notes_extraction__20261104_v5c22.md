# Grok 4.7 — ocr_extraction/handwritten_notes_extraction

- model_id: `x-ai/grok-4.7`
- success: True  | final: 8.31 | quality: 10.0
- latency_total: 31.42s | tokens_per_second: 77.5
- input_tokens: 1679 | output_tokens: 2434

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
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presup aprob: $8M CLP/mes x 3 pax\n   - JP hace JD p/ lunes\n\n4) Prox reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug p/ miérc 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "14/04/2026",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Corregir el bug crítico de la API de webhooks",
      "fecha_limite": "16/04/2026"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar el roadmap en Notion",
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para el cliente Falabella",
      "fecha_limite": "23/04/2026"
    },
    {
      "responsable": "JP",
      "tarea": "Redactar y publicar las JDs en LinkedIn y GetOnBrd",
      "fecha_limite": "20/04/2026"
    }
  ],
  "fechas_clave": [
    {"fecha": "14/04/2026", "evento": "Reunión de equipo de producto"},
    {"fecha": "16/04/2026", "evento": "Fecha límite: fix del bug de webhooks (Seba)"},
    {"fecha": "20/04/2026", "evento": "Fecha límite inferida: JP entrega/publica JDs (anotado como lunes)"},
    {"fecha": "21/04/2026", "evento": "Próxima reunión, 10:00 (anotada como lunes)"},
    {"fecha": "23/04/2026", "evento": "Demo para cliente Falabella (Cami)"},
    {"fecha": "28/04/2026", "evento": "Fecha original de lanzamiento v2.0 (movida)"},
    {"fecha": "05/05/2026", "evento": "Nueva fecha de lanzamiento v2.0"}
  ],
  "decisiones": [
    "Mover el lanzamiento de v2.0 del 28 de abril al 5 de mayo",
    "Seba se hace cargo del bug crítico de la API de webhooks",
    "Contratar 2 desarrolladores senior y 1 QA",
    "Presupuesto aprobado: $8M CLP/mes por 3 personas",
    "JP prepara las descripciones de cargo para el lunes"
  ]
}