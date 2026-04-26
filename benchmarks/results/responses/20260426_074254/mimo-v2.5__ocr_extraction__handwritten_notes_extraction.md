# MiMo-V2.5 (omnimodal) — ocr_extraction/handwritten_notes_extraction

- model_id: `xiaomi/mimo-v2.5`
- success: True  | final: 7.35 | quality: 8.44
- latency_total: 10.858s | tokens_per_second: 134.1
- input_tokens: 477 | output_tokens: 1456
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo producto - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (muy bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 personas\n   - JP hace JD para lunes\n\n4) Próx reunión: lunes 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
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
    {"fecha": "2026-04-14", "evento": "Reunión de equipo producto"},
    {"fecha": "2026-04-16", "evento": "Deadline fix webhook bug (Seba)"},
    {"fecha": "2026-04-21", "evento": "Próxima reunión de equipo (10am)"},
    {"fecha": "2026-04-23", "evento": "Demo cliente Falabella (Cami)"},
    {"fecha": "2026-04-28", "evento": "Fecha original de lanzamiento v2.0 (aplazada)"},
    {"fecha": "2026-05-05", "evento": "Nueva fecha de lanzamiento v2.0"}
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 del 28 de abril al 5 de mayo",
    "Seba asume fix del bug crítico en API webhooks",
    "Aprobado presupuesto de $8M CLP/mes para contratar 2 devs senior + 1 QA",
    "JP elabora job descriptions para publicar en lunes"
  ]
}
```