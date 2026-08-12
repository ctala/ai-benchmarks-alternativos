# Poolside Laguna S 2.1 — ocr_extraction/handwritten_notes_extraction

- model_id: `poolside/laguna-s-2.1`
- success: True  | final: 9.25 | quality: 10.0
- latency_total: 8.619s | tokens_per_second: 96.8
- input_tokens: 515 | output_tokens: 834
- judge_score: 4.8 | justificación: 

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presup aprobado: $8M CLP/mes x 3 pax\n   - JP hace JD p/ lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug p/ miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "14/04/26",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {"responsable": "Seba", "tarea": "Fix webhook bug", "fecha_limite": "16/04/26"},
    {"responsable": "MaJo", "tarea": "Actualizar roadmap en Notion", "fecha_limite": ""},
    {"responsable": "Cami", "tarea": "Preparar demo para cliente Falabella", "fecha_limite": "23/04/26"},
    {"responsable": "JP", "tarea": "Publicar JDs en LinkedIn + GetOnBrd", "fecha_limite": ""}
  ],
  "fechas_clave": [
    {"fecha": "14/04/26", "evento": "Reunión equipo prod"},
    {"fecha": "28/04/26", "evento": "Lanzamiento v2.0 (fecha original)"},
    {"fecha": "05/05/26", "evento": "Lanzamiento v2.0 (nueva fecha)"},
    {"fecha": "16/04/26", "evento": "Entrega fix webhook bug (Seba)"},
    {"fecha": "21/04/26", "evento": "Próxima reunión equipo prod"},
    {"fecha": "23/04/26", "evento": "Demo cliente Falabella (Cami)"},
    {"fecha": "lunes posterior a 14/04/26", "evento": "Entrega JD de contratación (JP)"}
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 de abril 28 a mayo 5",
    "Aprobar presupuesto de $8M CLP/mes por 3 personas para contratación",
    "Seba asume resolución de bug crítico en API webhooks",
    "JP responsable de crear y publicar JDs de contratación"
  ]
}
```