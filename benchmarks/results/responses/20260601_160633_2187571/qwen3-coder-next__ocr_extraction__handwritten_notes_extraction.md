# Qwen3-Coder-Next (OpenRouter FP8) — ocr_extraction/handwritten_notes_extraction

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 7.91 | quality: 9.28
- latency_total: 6.334s | tokens_per_second: 128.8
- input_tokens: 479 | output_tokens: 816
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una estructura bien organizada que facilita la comprensión y la acción, ofreciendo información útil para un emprendedor.

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (¡muy bueno!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 pax\n   - JP hace JD para lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBoard",
  "fecha_reunion": "2026-04-14",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Fix bug crítico en API webhooks",
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
      "tarea": "Publicar JDs en LinkedIn y GetOnBoard",
      "fecha_limite": "2026-04-14"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "2026-04-14",
      "evento": "Reunión equipo prod"
    },
    {
      "fecha": "2026-04-16",
      "evento": "Entrega fix webhook bug (Seba)"
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
      "evento": "Lanzamiento v2.0 originalmente planeado (postergado)"
    },
    {
      "fecha": "2026-05-05",
      "evento": "Lanzamiento v2.0 reprogramado"
    }
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 del 28/04 al 05/05",
    "Contratar 2 desarrolladores seniors y 1 QA",
    "Aprobar presupuesto de $8M CLP/mes para los 3 nuevos roles"
  ]
}
```