# GPT-6 Luna — ocr_extraction/handwritten_notes_extraction

- model_id: `openai/gpt-6-luna`
- success: True  | final: 9.26 | quality: 10.0
- latency_total: 6.259s | tokens_per_second: 126.1
- input_tokens: 437 | output_tokens: 789

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
  "texto_corregido": "Reunión equipo producto - 14/04/26\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0: mover del 28 de abril al 5 de mayo.\n   - Falta QA en el módulo de pagos.\n   - Bug crítico en la API de webhooks (Seba se encarga).\n\n2) Métricas del Q1:\n   - MRR: 52.1k (+15% vs. Q4).\n   - Churn bajó a 3.1% (objetivo: 3.5%).\n   - NPS subió a 51 (¡muy bueno!).\n\n3) Contratar 2 desarrolladores senior y 1 QA.\n   - Presupuesto aprobado: $8M CLP/mes para 3 personas.\n   - JP prepara las descripciones de puesto para el lunes.\n\n4) Próxima reunión: lunes 21/04 a las 10:00.\n\nAction items:\n- Seba: corregir el bug de webhooks para el miércoles 16/04.\n- MaJo: actualizar el roadmap en Notion.\n- Cami: preparar una demo para el cliente Falabella (23/04).\n- JP: publicar las descripciones de puesto en LinkedIn y GetOnBrd.",
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
      "tarea": "Preparar una demo para el cliente Falabella",
      "fecha_limite": "23/04/2026"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar las descripciones de puesto en LinkedIn y GetOnBrd",
      "fecha_limite": "lunes (fecha no especificada)"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/2026",
      "evento": "Reunión de equipo de producto"
    },
    {
      "fecha": "28/04/2026",
      "evento": "Fecha original prevista para el lanzamiento v2.0"
    },
    {
      "fecha": "16/04/2026",
      "evento": "Fecha límite para corregir el bug de webhooks"
    },
    {
      "fecha": "21/04/2026, 10:00",
      "evento": "Próxima reunión"
    },
    {
      "fecha": "23/04/2026",
      "evento": "Demo para el cliente Falabella"
    },
    {
      "fecha": "05/05/2026",
      "evento": "Nueva fecha prevista para el lanzamiento v2.0"
    }
  ],
  "decisiones": [
    "Aplazar el lanzamiento v2.0 del 28 de abril al 5 de mayo.",
    "Contratar 2 desarrolladores senior y 1 QA.",
    "Presupuesto aprobado: $8M CLP al mes para 3 personas."
  ]
}