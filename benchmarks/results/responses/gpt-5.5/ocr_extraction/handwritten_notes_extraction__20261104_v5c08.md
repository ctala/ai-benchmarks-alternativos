# GPT-5.5 — ocr_extraction/handwritten_notes_extraction

- model_id: `gpt-5.5`
- success: True  | final: 8.45 | quality: 10.0
- latency_total: 8.012s | tokens_per_second: 109.0
- input_tokens: 437 | output_tokens: 873

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
  "texto_corregido": "Reunión equipo producto - 14/04/26\nAsistentes: JP, MaJo, Seba, Cami. Ausente: Nico.\n\n1) Lanzamiento v2.0: mover de 28/04 a 05/05.\n   - Falta QA en módulo pagos.\n   - Bug crítico en API webhooks. Seba lo toma.\n\n2) Métricas Q1:\n   - MRR: 52.1k, +15% vs Q4.\n   - Churn bajó a 3.1%; el objetivo era 3.5%.\n   - NPS subió a 51. Muy bueno.\n\n3) Contratar 2 desarrolladores senior + 1 QA.\n   - Presupuesto aprobado: $8M CLP/mes por 3 personas.\n   - JP hace la descripción de cargo para el lunes.\n\n4) Próxima reunión: lunes 21/04 a las 10:00.\n\nAction items:\n- Seba: corregir bug de webhooks para miércoles 16/04.\n- MaJo: actualizar roadmap en Notion.\n- Cami: preparar demo para cliente Falabella, 23/04.\n- JP: publicar descripciones de cargo en LinkedIn y GetOnBrd.",
  "fecha_reunion": "2026-04-14",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Corregir bug crítico en API webhooks",
      "fecha_limite": "2026-04-16"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": null
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "2026-04-23"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar descripciones de cargo en LinkedIn y GetOnBrd",
      "fecha_limite": null
    },
    {
      "responsable": "JP",
      "tarea": "Preparar descripciones de cargo para contratación",
      "fecha_limite": "2026-04-20"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "2026-04-14",
      "evento": "Reunión de equipo producto"
    },
    {
      "fecha": "2026-04-16",
      "evento": "Fecha límite para que Seba corrija el bug de webhooks"
    },
    {
      "fecha": "2026-04-20",
      "evento": "JP debe tener listas las descripciones de cargo"
    },
    {
      "fecha": "2026-04-21T10:00:00",
      "evento": "Próxima reunión de equipo"
    },
    {
      "fecha": "2026-04-23",
      "evento": "Demo para cliente Falabella"
    },
    {
      "fecha": "2026-04-28",
      "evento": "Fecha original del lanzamiento v2.0"
    },
    {
      "fecha": "2026-05-05",
      "evento": "Nueva fecha del lanzamiento v2.0"
    }
  ],
  "decisiones": [
    "Mover el lanzamiento v2.0 del 28/04 al 05/05.",
    "Seba se encargará del bug crítico en la API de webhooks.",
    "Aprobar la contratación de 2 desarrolladores senior y 1 QA.",
    "Presupuesto aprobado de $8M CLP mensuales para 3 personas.",
    "La próxima reunión será el lunes 21/04 a las 10:00."
  ]
}