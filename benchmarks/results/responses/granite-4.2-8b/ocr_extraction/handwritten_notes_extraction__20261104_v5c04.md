# Granite 4.2 8B — ocr_extraction/handwritten_notes_extraction

- model_id: `ibm-granite/granite-4.2-8b`
- success: True  | final: 9.37 | quality: 10.0
- latency_total: 6.679s | tokens_per_second: 132.2
- input_tokens: 498 | output_tokens: 883

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
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abril 28 a mayo 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (¡bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 pax\n   - JP hace JD para lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para miérc 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBoard",
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
      "tarea": "actualizar roadmap en Notion",
      "fecha_limite": null
    },
    {
      "responsable": "Cami",
      "tarea": "preparar demo para cliente Falabella",
      "fecha_limite": "23/04"
    },
    {
      "responsable": "JP",
      "tarea": "publicar JDs en LinkedIn + GetOnBoard",
      "fecha_limite": null
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/26",
      "evento": "Reunión actual"
    },
    {
      "fecha": "21/04",
      "evento": "Próxima reunión"
    },
    {
      "fecha": "28/04",
      "evento": "Fecha original de lanzamiento (mover a mayo 5)"
    },
    {
      "fecha": "05/05",
      "evento": "Nueva fecha de lanzamiento v2.0"
    },
    {
      "fecha": "16/04",
      "evento": "Fecha límite para fix webhook bug (Seba)"
    },
    {
      "fecha": "23/04",
      "evento": "Fecha límite para preparar demo para Falabella (Cami)"
    }
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 de abril 28 a mayo 5",
    "Contratar 2 devs senior + 1 QA con presupuesto aprobado de $8M CLP/mes x 3 pax",
    "JP elaborará el documento de requisitos (JD) para lunes",
    "Seba asume la corrección del bug crítico en API webhooks",
    "Actualización de métricas Q1: MRR 52.1k (+15% vs Q4), churn bajó a 3.1% (objetivo 3.5%), NPS subió a 51"
  ]
}