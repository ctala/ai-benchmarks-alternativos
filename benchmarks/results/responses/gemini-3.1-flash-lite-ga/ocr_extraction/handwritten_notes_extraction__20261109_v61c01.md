# Gemini 3.1 Flash Lite (GA) — ocr_extraction/handwritten_notes_extraction

- model_id: `google/gemini-3.1-flash-lite`
- success: True  | final: 7.21 | quality: 7.14
- latency_total: 2.882s | tokens_per_second: 260.2
- input_tokens: 458 | output_tokens: 750

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

```json
{
  "texto_corregido": "Reunión equipo producto - 14/04/26. Asistentes: JP, MaJo, Seba, Cami (faltó Nico). 1) Lanzamiento v2.0 - mover de 28 de abril a 5 de mayo: falta QA en módulo pagos, bug crítico en API webhooks (Seba lo toma). 2) Métricas Q1: MRR 52.1k (+15% vs Q4), churn bajó a 3.1% (objetivo era 3.5%), NPS subió a 51. 3) Contratar 2 devs senior + 1 QA: presupuesto aprobado $8M CLP/mes por 3 personas, JP hace JD para el lunes. 4) Próxima reunión: lunes 21/04, 10:00 am.",
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
      "tarea": "Publicar JDs en LinkedIn y GetOnBoard",
      "fecha_limite": null
    },
    {
      "responsable": "JP",
      "tarea": "Redactar JDs para nuevas contrataciones",
      "fecha_limite": "2026-04-20"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "2026-04-16",
      "evento": "Fecha límite fix bug webhooks"
    },
    {
      "fecha": "2026-04-20",
      "evento": "Fecha límite entrega JDs por JP"
    },
    {
      "fecha": "2026-04-21",
      "evento": "Próxima reunión de equipo"
    },
    {
      "fecha": "2026-04-23",
      "evento": "Demo para cliente Falabella"
    },
    {
      "fecha": "2026-05-05",
      "evento": "Nueva fecha de lanzamiento v2.0"
    }
  ],
  "decisiones": [
    "Reprogramar lanzamiento v2.0 del 28 de abril al 5 de mayo",
    "Aprobación de presupuesto de $8M CLP/mes para contratar 2 devs senior y 1 QA"
  ]
}
```