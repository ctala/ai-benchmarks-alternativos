# Granite 4.2 8B — ocr_extraction/handwritten_notes_extraction

- model_id: `ibm-granite/granite-4.2-8b`
- success: True  | final: 8.67 | quality: 10.0
- latency_total: 112.574s | tokens_per_second: 99.7
- input_tokens: 498 | output_tokens: 11220

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
  "texto_corregido": "Reunión equipo prod - 14/04/2026\nAsistieron: JP, MaJo, Seba, Cami (Nico faltó)\n\n1) Lanzamiento v2.0 - mover de abril 28 a mayo 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (bueno!!)\n\n3) Contratar 2 devs senior + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 pax\n   - JP hace JD para lunes\n\n4) Próxima reunión: lunes 21/04 10:00\n\nAction items:\n- Seba: corregir bug de webhook para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn y GetOnBoard",
  "fecha_reunion": "14/04/2026",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "corregir bug de webhook",
      "fecha_limite": "16/04"
    },
    {
      "responsable": "MaJo",
      "tarea": "actualizar roadmap en Notion",
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "preparar demo para cliente Falabella",
      "fecha_limite": "23/04"
    },
    {
      "responsable": "JP",
      "tarea": "publicar JDs en LinkedIn y GetOnBoard",
      "fecha_limite": ""
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/2026",
      "evento": "Reunión actual"
    },
    {
      "fecha": "28/04",
      "evento": "Fecha original de lanzamiento (abr 28)"
    },
    {
      "fecha": "05/05",
      "evento": "Fecha nueva de lanzamiento (mayo 5)"
    },
    {
      "fecha": "16/04",
      "evento": "Fecha límite corregir bug (miércoles)"
    },
    {
      "fecha": "21/04",
      "evento": "Próxima reunión"
    },
    {
      "fecha": "23/04",
      "evento": "Fecha prep demo para Falabella"
    }
  ],
  "decisiones": [
    "Lanzamiento v2.0 se mueve de abril 28 a mayo 5; falta QA en módulo pagos; bug crítico en webhooks asignado a Seba",
    "Métricas Q1: MRR 52.1k (+15% vs Q4), churn 3.1% (objetivo 3.5%), NPS 51",
    "Contratar 2 devs senior + 1 QA; presupuesto $8M CLP/mes x 3; JD para lunes",
    "Próxima reunión: lunes 21/04 10:00"
  ]
}