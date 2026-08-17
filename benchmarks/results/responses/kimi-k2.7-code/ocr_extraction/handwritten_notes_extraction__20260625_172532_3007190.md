# Kimi K2.7 Code — ocr_extraction/handwritten_notes_extraction

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 6.71 | quality: 8.44
- latency_total: 68.354s | tokens_per_second: 49.1
- input_tokens: 484 | output_tokens: 3357
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 pax\n   - JP hace JD para lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para miér 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
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
      "tarea": "Fix del bug crítico en API webhooks",
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
      "tarea": "Publicar JDs en LinkedIn + GetOnBrd",
      "fecha_limite": "2026-04-21"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "2026-04-14",
      "evento": "Reunión equipo prod"
    },
    {
      "fecha": "2026-04-16",
      "evento": "Entrega fix del bug en webhooks (Seba)"
    },
    {
      "fecha": "2026-04-21",
      "evento": "Próxima reunión del equipo (10:00) / JP entrega JDs"
    },
    {
      "fecha": "2026-04-23",
      "evento": "Demo para cliente Falabella (Cami)"
    },
    {
      "fecha": "2026-04-28",
      "evento": "Fecha original del lanzamiento v2.0 (pospuesta)"
    },
    {
      "fecha": "2026-05-05",
      "evento": "Nueva fecha de lanzamiento v2.0"
    }
  ],
  "decisiones": [
    "El lanzamiento v2.0 se mueve del 28 de abril al 5 de mayo.",
    "Se requiere completar QA del módulo de pagos antes del lanzamiento.",
    "Seba se hace cargo del bug crítico en API de webhooks.",
    "Se aprueba presupuesto de $8M CLP/mes para contratar 2 devs senior y 1 QA.",
    "JP prepara las JDs para el lunes 21/04."
  ]
}
```