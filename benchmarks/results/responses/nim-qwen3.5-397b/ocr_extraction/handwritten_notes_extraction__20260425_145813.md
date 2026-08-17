# Qwen 3.5 397B (NIM) — ocr_extraction/handwritten_notes_extraction

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 7.05 | quality: 8.44
- latency_total: 39.045s | tokens_per_second: 21.1
- input_tokens: 443 | output_tokens: 822
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0: mover de abr 28 a may 5. Falta QA en módulo pagos. Bug crítico en API webhooks (Seba lo toma).\n2) Métricas Q1: MRR 52.1k (+15% vs Q4), churn bajó a 3.1% (obj era 3.5%), NPS subió a 51 (¡re bueno!).\n3) Contratar 2 devs sr + 1 QA. Presup aprob: $8M CLP/mes x 3 pax. JP hace JD p/ lunes.\n4) Próx reunion: lun 21/04 10am.\n\nAction items:\n- Seba: fix webhook bug p/ miérc 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
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
      "tarea": "Publicar JDs en LinkedIn y GetOnBrd",
      "fecha_limite": "2026-04-21"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "2026-04-16",
      "evento": "Entrega fix bug webhooks (Seba)"
    },
    {
      "fecha": "2026-04-21",
      "evento": "Próxima reunión (10am)"
    },
    {
      "fecha": "2026-04-23",
      "evento": "Demo cliente Falabella"
    },
    {
      "fecha": "2026-04-28",
      "evento": "Fecha original lanzamiento v2.0 (movida)"
    },
    {
      "fecha": "2026-05-05",
      "evento": "Nueva fecha lanzamiento v2.0"
    }
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 del 28 de abril al 5 de mayo.",
    "Aprobar presupuesto de contratación: $8M CLP/mes por 3 personas (2 devs sr + 1 QA).",
    "Seba se hace cargo del bug crítico en API webhooks."
  ]
}
```