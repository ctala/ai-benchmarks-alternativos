# Kimi K2.6 — ocr_extraction/handwritten_notes_extraction

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 8.4 | quality: 10.0
- latency_total: 51.263s | tokens_per_second: 137.0
- input_tokens: 485 | output_tokens: 7021
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al proporcionar detalles estructurados y útiles para un emprendedor, y los datos extraídos son exactos.

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo de producto - 14/04/26\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover del 28 de abril al 5 de mayo\n   - Falta QA en módulo de pagos\n   - Bug crítico en API de webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - Churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (¡re bueno!!)\n\n3) Contratar 2 desarrolladores senior + 1 QA\n   - Presupuesto aprobado: $8M CLP/mes por 3 personas\n   - JP hace descripciones de cargo para el lunes\n\n4) Próxima reunión: lunes 21/04 a las 10am\n\nAction items:\n- Seba: fix webhook bug para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar descripciones de cargo en LinkedIn + GetOnBoard",
  "fecha_reunion": "14/04/26",
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
      "fecha_limite": "16/04/26"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": null
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "23/04/26"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar descripciones de cargo en LinkedIn + GetOnBoard",
      "fecha_limite": null
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/26",
      "evento": "Reunión equipo de producto"
    },
    {
      "fecha": "16/04/26",
      "evento": "Deadline fix webhook bug (Seba)"
    },
    {
      "fecha": "21/04/26",
      "evento": "Próxima reunión (10am) / Entrega JDs (JP)"
    },
    {
      "fecha": "23/04/26",
      "evento": "Demo cliente Falabella (Cami)"
    },
    {
      "fecha": "28/04/26",
      "evento": "Fecha original lanzamiento v2.0 (movida)"
    },
    {
      "fecha": "05/05/26",
      "evento": "Nueva fecha lanzamiento v2.0"
    }
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 del 28 de abril al 5 de mayo debido a falta de QA en módulo de pagos y bug crítico en API de webhooks",
    "Asignar a Seba la resolución del bug crítico en API de webhooks",
    "Aprobar presupuesto de contratación de $8M CLP/mes por 3 personas (2 desarrolladores senior + 1 QA)",
    "Publicar descripciones de cargo en LinkedIn y GetOnBoard"
  ]
}
```