# MiniMax M3 — ocr_extraction/handwritten_notes_extraction

- model_id: `minimax/minimax-m3`
- success: True  | final: 8.84 | quality: 10.0
- latency_total: 10.293s | tokens_per_second: 82.8
- input_tokens: 589 | output_tokens: 852

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
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (¡re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 pax\n   - JP hace JD p/ lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug p/ miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBoard",
  "fecha_reunion": "14/04/26",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Corregir el bug de la API de webhooks",
      "fecha_limite": "16/04/26"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar el roadmap en Notion",
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para el cliente Falabella",
      "fecha_limite": "23/04/26"
    },
    {
      "responsable": "JP",
      "tarea": "Preparar la JD (descripción de puesto) para el lunes",
      "fecha_limite": "20/04/26"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar las JDs en LinkedIn y GetOnBoard",
      "fecha_limite": ""
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/26",
      "evento": "Reunión del equipo de producción"
    },
    {
      "fecha": "16/04/26",
      "evento": "Fecha límite para corregir el bug de la API de webhooks (Seba)"
    },
    {
      "fecha": "20/04/26",
      "evento": "JP debe tener lista la JD"
    },
    {
      "fecha": "21/04/26",
      "evento": "Próxima reunión a las 10:00"
    },
    {
      "fecha": "23/04/26",
      "evento": "Demo para el cliente Falabella"
    },
    {
      "fecha": "28/04/26",
      "evento": "Fecha original de lanzamiento de v2.0 (aplazada)"
    },
    {
      "fecha": "05/05/26",
      "evento": "Nueva fecha de lanzamiento de v2.0"
    }
  ],
  "decisiones": [
    "Mover el lanzamiento de v2.0 del 28 de abril al 5 de mayo.",
    "Seba se hace cargo del bug crítico en la API de webhooks.",
    "Contratar 2 devs senior y 1 QA con un presupuesto aprobado de $8M CLP/mes por 3 personas.",
    "JP preparará la JD y publicará los avisos de empleo en LinkedIn y GetOnBoard."
  ]
}