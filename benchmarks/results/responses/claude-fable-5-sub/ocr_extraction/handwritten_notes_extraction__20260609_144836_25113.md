# Claude Fable 5 (suscripción) — ocr_extraction/handwritten_notes_extraction

- model_id: `claude-fable-5`
- success: True  | final: 6.39 | quality: 7.87
- latency_total: 17.958s | tokens_per_second: 84.3
- input_tokens: 2 | output_tokens: 1513

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abril 28 a mayo 5\n   - Falta QA en módulo de pagos\n   - Bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR: $52.1k (+15% vs Q4)\n   - Churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (muy bueno)\n\n3) Contratar 2 devs senior + 1 QA\n   - Presupuesto aprobado: $8M CLP/mes x 3 personas\n   - JP hace job descriptions para el lunes\n\n4) Próxima reunión: lunes 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "2026-04-14",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Corregir bug crítico en API de webhooks",
      "fecha_limite": "2026-04-16"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": "no especificada"
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "2026-04-23"
    },
    {
      "responsable": "JP",
      "tarea": "Redactar job descriptions (2 devs senior + 1 QA) y publicarlas en LinkedIn + GetOnBrd",
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
      "evento": "Deadline fix de bug en webhooks (Seba)"
    },
    {
      "fecha": "2026-04-20",
      "evento": "Entrega de job descriptions (JP) — 'el lunes' previo a la próxima reunión"
    },
    {
      "fecha": "2026-04-21",
      "evento": "Próxima reunión de equipo (10:00 am)"
    },
    {
      "fecha": "2026-04-23",
      "evento": "Demo para cliente Falabella (Cami)"
    },
    {
      "fecha": "2026-04-28",
      "evento": "Fecha original de lanzamiento v2.0 (descartada)"
    },
    {
      "fecha": "2026-05-05",
      "evento": "Nueva fecha de lanzamiento v2.0"
    }
  ],
  "decisiones": [
    "Posponer el lanzamiento de v2.0 del 28 de abril al 5 de mayo por QA pendiente en módulo de pagos y bug crítico en API de webhooks",
    "Contratar 2 desarrolladores senior y 1 QA con presupuesto aprobado de $8M CLP/mes por persona (3 personas)",
    "Asignar a Seba la corrección del bug crítico en API de webhooks"
  ]
}
```

**Notas de interpretación:**
- "p/ lunes" en el ítem 3 se interpretó como el lunes 20/04 (día hábil previo a la próxima reunión del 21/04). Hay ambigüedad: la próxima reunión es lunes 21/04, así que podría referirse a esa fecha.
- "JD" = job description; "pax" = personas; "presup aprob" = presupuesto aprobado.
- El "JP: publicar JDs" del action items y el "JP hace JD p/ lunes" del punto 3 se consolidaron como una sola tarea con dos pasos (redactar + publicar).