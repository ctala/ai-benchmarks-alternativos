# Seed 2.1 Turbo — ocr_extraction/handwritten_notes_extraction

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 8.14 | quality: 10.0
- latency_total: 294.231s | tokens_per_second: 57.3
- input_tokens: 522 | output_tokens: 16871

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
  "texto_corregido": "Reunión equipo de producto - 14/04/2026\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - se mueve del 28 de abril al 5 de mayo\n   - Falta realizar QA en el módulo de pagos\n   - Bug crítico en API de webhooks (Seba se encarga de su resolución)\n\n2) Métricas del primer trimestre (Q1):\n   - MRR: 52,1k (+15% respecto al Q4)\n   - Churn bajó a 3,1% (el objetivo era 3,5%)\n   - NPS subió a 51 (muy bueno!!)\n\n3) Contratación de 2 desarrolladores senior + 1 QA\n   - Presupuesto aprobado: $8.000.000 CLP por mes para 3 personas\n   - JP elabora las descripciones de puesto (JD) para el día lunes\n\n4) Próxima reunión: lunes 21/04 a las 10:00 hs\n\nÍtems de acción:\n- Seba: Corregir el bug de webhooks para el miércoles 16/04\n- MaJo: Actualizar el roadmap en Notion\n- Cami: Preparar demo para el cliente Falabella (para el 23/04)\n- JP: Publicar las descripciones de puesto (JD) en LinkedIn y GetOnBrd",
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
      "tarea": "Actualizar el roadmap del producto en Notion",
      "fecha_limite": "Sin fecha límite especificada"
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar la demo para el cliente Falabella",
      "fecha_limite": "23/04/2026"
    },
    {
      "responsable": "JP",
      "tarea": "Elaborar las descripciones de puesto (JD) para las contrataciones de 2 desarrolladores senior y 1 QA",
      "fecha_limite": "21/04/2026"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar las descripciones de puesto (JD) en LinkedIn y GetOnBrd",
      "fecha_limite": "Sin fecha límite especificada"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/2026",
      "evento": "Reunión del equipo de producto"
    },
    {
      "fecha": "16/04/2026",
      "evento": "Fecha límite para corrección del bug de la API de webhooks (responsable: Seba)"
    },
    {
      "fecha": "21/04/2026",
      "evento": "Fecha límite para elaboración de descripciones de puesto (JD) (responsable: JP)"
    },
    {
      "fecha": "21/04/2026",
      "evento": "Próxima reunión del equipo de producto a las 10:00 hs"
    },
    {
      "fecha": "23/04/2026",
      "evento": "Fecha límite para preparación de demo para el cliente Falabella (responsable: Cami)"
    },
    {
      "fecha": "28/04/2026",
      "evento": "Fecha original de lanzamiento de la versión 2.0 (reprogramada)"
    },
    {
      "fecha": "05/05/2026",
      "evento": "Nueva fecha de lanzamiento de la versión 2.0"
    }
  ],
  "decisiones": [
    "Reprogramar el lanzamiento de la versión 2.0 del producto, pasando del 28 de abril al 5 de mayo de 2026, debido a pendientes de QA en el módulo de pagos y un bug crítico en la API de webhooks",
    "Aprobar el presupuesto de $8.000.000 CLP mensuales para la contratación de 2 desarrolladores senior y 1 profesional de QA",
    "Definir que la próxima reunión del equipo de producto se realizará el lunes 21 de abril de 2026 a las 10:00 hs"
  ]
}