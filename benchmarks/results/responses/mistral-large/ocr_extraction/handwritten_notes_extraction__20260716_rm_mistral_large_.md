# Mistral Large — ocr_extraction/handwritten_notes_extraction

- model_id: `mistralai/mistral-large`
- success: True  | final: 8.51 | quality: 10.0
- latency_total: 12.032s | tokens_per_second: 76.5
- input_tokens: 468 | output_tokens: 921
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al proporcionar detalles estructurados y accionables, y los datos extraídos son exactos.

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/2026\n\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abril 28 a mayo 5\n   - Falta QA en módulo pagos\n   - Bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - Churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (¡muy bueno!)\n\n3) Contratar 2 devs senior + 1 QA\n   - Presupuesto aprobado: $8M CLP/mes x 3 personas\n   - JP hace JD para lunes\n\n4) Próxima reunión: lunes 21/04 a las 10am\n\nAction items:\n- Seba: fix webhook bug para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBoard",

  "fecha_reunion": "14/04/2026",

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
      "tarea": "Arreglar bug crítico en API webhooks",
      "fecha_limite": "16/04/2026"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "23/04/2026"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar JDs (descripciones de trabajo) en LinkedIn y GetOnBoard",
      "fecha_limite": ""
    }
  ],

  "fechas_clave": [
    {
      "fecha": "14/04/2026",
      "evento": "Reunión equipo de producción"
    },
    {
      "fecha": "16/04/2026",
      "evento": "Fecha límite para arreglar bug en API webhooks (Seba)"
    },
    {
      "fecha": "21/04/2026",
      "evento": "Próxima reunión del equipo de producción"
    },
    {
      "fecha": "23/04/2026",
      "evento": "Demo para cliente Falabella (Cami)"
    },
    {
      "fecha": "28/04/2026",
      "evento": "Fecha original de lanzamiento v2.0 (movida a mayo 5)"
    },
    {
      "fecha": "05/05/2026",
      "evento": "Nueva fecha de lanzamiento v2.0"
    }
  ],

  "decisiones": [
    "Mover lanzamiento de la versión 2.0 de abril 28 a mayo 5.",
    "Seba se hará cargo del bug crítico en la API de webhooks.",
    "Contratar 2 desarrolladores senior y 1 QA con un presupuesto aprobado de $8M CLP/mes para 3 personas.",
    "JP se encargará de redactar las descripciones de trabajo (JDs) para el próximo lunes.",
    "Próxima reunión programada para el lunes 21/04 a las 10am."
  ]
}
```