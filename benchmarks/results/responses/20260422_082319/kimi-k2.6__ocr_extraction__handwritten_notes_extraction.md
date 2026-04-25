# Kimi K2.6 — ocr_extraction/handwritten_notes_extraction

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 6.65 | quality: 8.44
- latency_total: 65.377s | tokens_per_second: 68.4
- input_tokens: 485 | output_tokens: 4471
- judge_score: 4.4 | justificación: 

## Respuesta completa

 ```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de 28 abr a 5 may\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (¡re bueno!)\n\n3) Contratar 2 desarrolladores senior + 1 QA\n   - presupuesto aprobado: $8M CLP/mes por 3 personas\n   - JP hace descripciones de cargo (JD) para lunes\n\n4) Próxima reunión: lun 21/04 10:00\n\nAction items:\n- Seba: fix webhook bug para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "14/04/26",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {"responsable": "Seba", "tarea": "Fix webhook bug", "fecha_limite": "16/04/26"},
    {"responsable": "MaJo", "tarea": "Actualizar roadmap en Notion", "fecha_limite": null},
    {"responsable": "Cami", "tarea": "Preparar demo para cliente Falabella", "fecha_limite": "23/04/26"},
    {"responsable": "JP", "tarea": "Publicar JDs en LinkedIn + GetOnBrd", "fecha_limite": "21/04/26"}
  ],
  "fechas_clave": [
    {"fecha": "14/04/26", "evento": "Reunión equipo prod"},
    {"fecha": "16/04/26", "evento": "Fix webhook bug (Seba)"},
    {"fecha": "21/04/26", "evento": "Entrega JDs (JP) / Próxima reunión 10:00"},
    {"fecha": "23/04/26", "evento": "Demo cliente Falabella (Cami)"},
    {"fecha": "28/04/26", "evento": "Fecha original lanzamiento v2.0 (pospuesto)"},
    {"fecha": "05/05/26", "evento": "Nueva fecha lanzamiento v2.0"}
  ],
  "decisiones": [
    "Postergar lanzamiento v2.0 del 28 de abril al 5 de mayo por falta de QA en módulo de pagos y bug crítico en API webhooks",
    "Asignar a Seba la corrección del bug crítico en API webhooks",
    "Aprobar presupuesto de $8M CLP/mes por 3 personas para contratar 2 desarrolladores senior y 1 QA",
    "JP elabora descripciones de cargo (JD) para el lunes 21/04"
  ]
}
```