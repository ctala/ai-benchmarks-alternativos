# MiMo V2.5 (Xiaomi) — ocr_extraction/handwritten_notes_extraction

- model_id: `mimo-v2.5`
- success: True  | final: 7.55 | quality: 8.44
- latency_total: 15.379s | tokens_per_second: 80.8
- input_tokens: 477 | output_tokens: 1242
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo producto - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presup aprob: $8M CLP/mes x 3 pax\n   - JP hace JD p/ lunes\n\n4) Próx reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug p/ miér 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
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
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "2026-04-23"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar JDs en LinkedIn y GetOnBrd",
      "fecha_limite": ""
    }
  ],
  "fechas_clave": [
    {
      "fecha": "2026-04-14",
      "evento": "Reunión de equipo producto"
    },
    {
      "fecha": "2026-04-16",
      "evento": "Fecha límite para fix de webhook (Seba)"
    },
    {
      "fecha": "2026-04-21",
      "evento": "Próxima reunión de equipo (10am)"
    },
    {
      "fecha": "2026-04-23",
      "evento": "Demo para cliente Falabella (Cami)"
    },
    {
      "fecha": "2026-05-05",
      "evento": "Nueva fecha de lanzamiento v2.0 (postergado desde 28/04)"
    }
  ],
  "decisiones": [
    "Postergar lanzamiento v2.0 del 28 de abril al 5 de mayo",
    "Aprobar presupuesto de $8M CLP/mes para contratación de 3 personas (2 devs sr + 1 QA)",
    "Seba se encarga del bug crítico en API webhooks"
  ]
}
```