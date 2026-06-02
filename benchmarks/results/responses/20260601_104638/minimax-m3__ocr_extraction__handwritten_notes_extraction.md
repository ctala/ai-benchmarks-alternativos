# MiniMax M3 — ocr_extraction/handwritten_notes_extraction

- model_id: `minimax/minimax-m3`
- success: True  | final: 7.62 | quality: 9.28
- latency_total: 44.24s | tokens_per_second: 36.8
- input_tokens: 602 | output_tokens: 1628
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al proporcionar detalles y estructura, y los datos extraídos son exactos.

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (¡re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 pax\n   - JP hace JD para lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para miérc 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "14/04/2026",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Fixear bug crítico en API webhooks",
      "fecha_limite": "16/04/2026 (miércoles)"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": "No especificada"
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "23/04/2026"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar Job Descriptions en LinkedIn + GetOnBrd",
      "fecha_limite": "21/04/2026 (lunes)"
    },
    {
      "responsable": "JP",
      "tarea": "Redactar JD para 2 devs sr + 1 QA",
      "fecha_limite": "21/04/2026 (lunes)"
    },
    {
      "responsable": "Seba",
      "tarea": "Tomar/liderar resolución del bug crítico en API webhooks",
      "fecha_limite": "16/04/2026 (miércoles)"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/2026",
      "evento": "Reunión de equipo de producto"
    },
    {
      "fecha": "16/04/2026",
      "evento": "Fecha límite para fixear bug de webhooks (Seba)"
    },
    {
      "fecha": "21/04/2026",
      "evento": "Próxima reunión de equipo (10am) + publicación de JDs"
    },
    {
      "fecha": "23/04/2026",
      "evento": "Demo para cliente Falabella (Cami)"
    },
    {
      "fecha": "28/04/2026",
      "evento": "Fecha original de lanzamiento v2.0 (desestimada)"
    },
    {
      "fecha": "05/05/2026",
      "evento": "Nueva fecha de lanzamiento v2.0"
    }
  ],
  "decisiones": [
    "Mover el lanzamiento de la v2.0 del 28 de abril al 5 de mayo de 2026",
    "Asignar a Seba como responsable del bug crítico en API webhooks",
    "Contratar 2 desarrolladores senior + 1 QA con un presupuesto aprobado de $8M CLP/mes para 3 personas",
    "JP será responsable de redactar y publicar las Job Descriptions"
  ]
}
```