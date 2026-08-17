# Gemma 4 31B (NIM) — ocr_extraction/handwritten_notes_extraction

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 7.25 | quality: 8.44
- latency_total: 81.75s | tokens_per_second: 10.9
- input_tokens: 450 | output_tokens: 894
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo producto - 14/04/26. Asistentes: JP, MaJo, Seba, Cami (faltó Nico). 1) Lanzamiento v2.0: mover del 28 de abril al 5 de mayo. Falta QA en módulo de pagos; bug crítico en API webhooks (Seba lo toma). 2) Métricas Q1: MRR 52.1k (+15% vs Q4), churn bajó a 3.1% (objetivo era 3.5%), NPS subió a 51 (muy bueno). 3) Contratar 2 desarrolladores senior + 1 QA. Presupuesto aprobado: $8M CLP/mes por persona. JP hace la descripción del cargo (JD) para el lunes. 4) Próxima reunión: lunes 21/04 a las 10am. Action items: Seba debe corregir el bug de webhook para el miércoles 16/04; MaJo debe actualizar el roadmap en Notion; Cami debe preparar la demo para el cliente Falabella (23/04); JP debe publicar las JD en LinkedIn y GetOnBoard.",
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
      "tarea": "Fix webhook bug",
      "fecha_limite": "2026-04-16"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": "No especificada"
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "2026-04-23"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar JDs en LinkedIn y GetOnBoard",
      "fecha_limite": "No especificada"
    },
    {
      "responsable": "JP",
      "tarea": "Redactar Job Descriptions (JD)",
      "fecha_limite": "2026-04-20"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "2026-04-14",
      "evento": "Reunión de equipo de producto"
    },
    {
      "fecha": "2026-04-16",
      "evento": "Fecha límite para corrección de bug de webhook"
    },
    {
      "fecha": "2026-04-20",
      "evento": "Entrega de JDs por parte de JP"
    },
    {
      "fecha": "2026-04-21",
      "evento": "Próxima reunión de equipo (10:00 AM)"
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
    "Reprogramación del lanzamiento v2.0 del 28 de abril al 5 de mayo",
    "Aprobación de presupuesto para contratación de 2 Devs Sr y 1 QA ($8M CLP/mes por persona)"
  ]
}
```