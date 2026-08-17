# Gemini 2.5 Flash Lite — ocr_extraction/handwritten_notes_extraction

- model_id: `google/gemini-2.5-flash-lite`
- success: True  | final: 9.43 | quality: 10.0
- latency_total: 3.422s | tokens_per_second: 259.8
- input_tokens: 458 | output_tokens: 889
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al proporcionar detalles estructurados y útiles para un emprendedor, y los datos extraídos son exactos.

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/2026\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crit en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presup aprob: $8M CLP/mes x 3 pax\n   - JP hace JD p/ lunes\n\n4) Prox reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug p/ mierc 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
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
      "tarea": "Fix webhook bug",
      "fecha_limite": "16/04/2026"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": null
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "23/04/2026"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar JDs en LinkedIn + GetOnBrd",
      "fecha_limite": null
    }
  ],
  "fechas_clave": [
    {
      "fecha": "28/04/2026",
      "evento": "Lanzamiento v2.0 (originalmente planeado)"
    },
    {
      "fecha": "05/05/2026",
      "evento": "Lanzamiento v2.0 (nueva fecha)"
    },
    {
      "fecha": "16/04/2026",
      "evento": "Fecha límite para fix webhook bug (Seba)"
    },
    {
      "fecha": "21/04/2026",
      "evento": "Próxima reunión"
    },
    {
      "fecha": "23/04/2026",
      "evento": "Fecha límite para demo cliente Falabella (Cami)"
    }
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 del 28 de abril al 5 de mayo.",
    "Se requiere QA en módulo de pagos para el lanzamiento v2.0.",
    "Seba se encargará de arreglar el bug crítico en la API de webhooks.",
    "Contratar 2 desarrolladores senior y 1 QA.",
    "Presupuesto aprobado de $8M CLP/mes para los 3 contratados.",
    "JP creará las descripciones de puestos (JD) para el lunes."
  ]
}
```