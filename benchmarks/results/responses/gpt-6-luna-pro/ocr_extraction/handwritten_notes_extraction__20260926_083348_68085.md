# GPT-6 Luna Pro — ocr_extraction/handwritten_notes_extraction

- model_id: `openai/gpt-6-luna-pro`
- success: True  | final: 8.83 | quality: 10.0
- latency_total: 21.91s | tokens_per_second: 193.2
- input_tokens: 6336 | output_tokens: 4234

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
  "texto_corregido": "Reunión de equipo de producto — 14/04/2026\nAsistentes: JP, MaJo, Seba y Cami (faltó Nico).\n\n1. Lanzamiento v2.0: mover del 28 de abril al 5 de mayo.\n   - Falta QA en el módulo de pagos.\n   - Bug crítico en la API de webhooks (Seba se encarga).\n\n2. Métricas del Q1:\n   - MRR: 52,1 k (+15 % respecto del Q4).\n   - El churn bajó a 3,1 % (objetivo: 3,5 %).\n   - El NPS subió a 51.\n\n3. Contratar a 2 desarrolladores sénior y 1 QA.\n   - Presupuesto aprobado: $8M CLP/mes × 3 personas.\n   - JP prepara las descripciones de cargo para el lunes.\n\n4. Próxima reunión: lunes 21/04, 10:00.\n\nAcciones:\n- Seba: corregir el bug de webhooks para el miércoles 16/04.\n- MaJo: actualizar la hoja de ruta en Notion.\n- Cami: preparar la demo para el cliente Falabella (23/04).\n- JP: publicar las descripciones de cargo en LinkedIn y GetOnBoard.",
  "fecha_reunion": "2026-04-14",
  "asistentes": [
    "JP",
    "MaJo",
    "Seba",
    "Cami"
  ],
  "ausentes": [
    "Nico"
  ],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Corregir el bug crítico de la API de webhooks.",
      "fecha_limite": "2026-04-16"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar la hoja de ruta en Notion.",
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar la demo para el cliente Falabella.",
      "fecha_limite": "2026-04-23"
    },
    {
      "responsable": "JP",
      "tarea": "Preparar las descripciones de cargo para los puestos de contratación.",
      "fecha_limite": "Lunes (fecha exacta no especificada)"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar las descripciones de cargo en LinkedIn y GetOnBoard.",
      "fecha_limite": ""
    }
  ],
  "fechas_clave": [
    {
      "fecha": "2026-04-14",
      "evento": "Reunión de equipo de producto."
    },
    {
      "fecha": "2026-04-16",
      "evento": "Fecha límite para que Seba corrija el bug de webhooks (anotada como miércoles)."
    },
    {
      "fecha": "2026-04-21",
      "evento": "Próxima reunión, a las 10:00 (anotada como lunes)."
    },
    {
      "fecha": "2026-04-23",
      "evento": "Demo para el cliente Falabella."
    },
    {
      "fecha": "2026-04-28",
      "evento": "Fecha original del lanzamiento de la versión 2.0."
    },
    {
      "fecha": "2026-05-05",
      "evento": "Nueva fecha prevista para el lanzamiento de la versión 2.0."
    },
    {
      "fecha": "Lunes (fecha exacta no especificada)",
      "evento": "JP debe preparar las descripciones de cargo."
    }
  ],
  "decisiones": [
    "Aplazar el lanzamiento de la versión 2.0 del 28 de abril al 5 de mayo.",
    "Contratar a 2 desarrolladores sénior y 1 QA, con un presupuesto indicado de $8M CLP/mes × 3 personas.",
    "Verificar el año de las fechas: si corresponde a 2026, los días de la semana anotados no coinciden con el calendario (por ejemplo, el 16/04/2026 cae jueves y el 21/04/2026, martes)."
  ]
}