# Mistral Large 3 675B (NIM) — ocr_extraction/handwritten_notes_extraction

- model_id: `mistralai/mistral-large-3-675b-instruct-2512`
- success: True  | final: 6.9 | quality: 8.44
- latency_total: 197.418s | tokens_per_second: 4.4
- input_tokens: 449 | output_tokens: 876
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/26\n\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0:\n   - Mover de abril 28 a mayo 5\n   - Falta QA en módulo pagos\n   - Bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR: 52.1k (+15% vs Q4)\n   - Churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (¡muy bueno!)\n\n3) Contratar 2 devs senior + 1 QA:\n   - Presupuesto aprobado: $8M CLP/mes por 3 personas\n   - JP hace JD para lunes\n\n4) Próxima reunión: lunes 21/04 a las 10am\n\nAction items:\n   - Seba: fix bug webhook para miércoles 16/04\n   - MaJo: actualizar roadmap en Notion\n   - Cami: preparar demo para cliente Falabella (23/04)\n   - JP: publicar JDs en LinkedIn + GetOnBoard",

  "fecha_reunion": "2026-04-14",

  "asistentes": ["JP", "MaJo", "Seba", "Cami"],

  "ausentes": ["Nico"],

  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Fix bug webhook en API",
      "fecha_limite": "2026-04-16"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "2026-04-23"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar JDs (job descriptions) en LinkedIn y GetOnBoard",
      "fecha_limite": "2026-04-20"
    }
  ],

  "fechas_clave": [
    {
      "fecha": "2026-04-16",
      "evento": "Corrección bug crítico en API webhooks"
    },
    {
      "fecha": "2026-04-20",
      "evento": "Publicación de job descriptions"
    },
    {
      "fecha": "2026-04-21",
      "evento": "Próxima reunión del equipo"
    },
    {
      "fecha": "2026-04-23",
      "evento": "Demo para cliente Falabella"
    },
    {
      "fecha": "2026-04-28",
      "evento": "Fecha original del lanzamiento v2.0 (postergado)"
    },
    {
      "fecha": "2026-05-05",
      "evento": "Nueva fecha para lanzamiento v2.0"
    }
  ],

  "decisiones": [
    "Mover fecha de lanzamiento v2.0 de abril 28 a mayo 5",
    "Corregir bug crítico en API webhooks lo antes posible (Seba encargado)",
    "Contratar 2 desarrolladores senior y 1 QA con presupuesto aprobado de $8M CLP/mes",
    "JP encargarse de redactar y publicar las job descriptions para el lunes siguiente"
  ]
}
```