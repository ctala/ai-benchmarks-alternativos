# Nemotron Super 49B v1.5 (NIM) — ocr_extraction/handwritten_notes_extraction

- model_id: `nvidia/llama-3.3-nemotron-super-49b-v1.5`
- success: True  | final: 6.75 | quality: 8.44
- latency_total: 82.129s | tokens_per_second: 28.2
- input_tokens: 447 | output_tokens: 2314
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/2024 Asist: JP, MaJo, Seba, Cami (falta Nico) 1) Lanzamiento v2.0 - mover de abr 28 a may 5 - falta QA en módulo pagos - bug crít en API webhooks (Seba lo toma) 2) Métricas Q1: - MRR 52.1k (+15% vs Q4) - churn bajó a 3.1% (obj era 3.5%) - NPS subió a 51 (muy bueno!!) 3) Contratar 2 devs sr + 1 QA - presupuesto aprobado: $8M CLP/mes x 3 pax - JP hace JD p/ lunes 4) Próxima reunión: lun 21/04 10am Action items: - Seba: fix webhook bug p/ miércoles 16/04 - MaJo: actualizar roadmap en Notion - Cami: prep demo p/ cliente Falabella (23/04) - JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "14/04/2024",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Arreglar bug de webhook",
      "fecha_limite": "16/04/2024"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "23/04/2024"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar JDs en LinkedIn y GetOnBrd",
      "fecha_limite": ""
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/2024",
      "evento": "Reunión equipo producto"
    },
    {
      "fecha": "16/04/2024",
      "evento": "Deadline: Arreglar bug de webhook (Seba)"
    },
    {
      "fecha": "21/04/2024",
      "evento": "Próxima reunión (10am)"
    },
    {
      "fecha": "23/04/2024",
      "evento": "Deadline: Demo para Falabella (Cami)"
    },
    {
      "fecha": "28/04/2024",
      "evento": "Fecha original de lanzamiento v2.0"
    },
    {
      "fecha": "05/05/2024",
      "evento": "Nueva fecha de lanzamiento v2.0"
    }
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 de 28/04/2024 a 05/05/2024",
    "Aprobar presupuesto de $8M CLP/mes para contratar 2 devs sr + 1 QA",
    "JP crear JDs para publicar en LinkedIn y GetOnBrd antes del lunes"
  ]
}
```