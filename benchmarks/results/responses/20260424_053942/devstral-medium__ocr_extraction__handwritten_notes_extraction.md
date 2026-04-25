# Devstral Medium — ocr_extraction/handwritten_notes_extraction

- model_id: `mistralai/devstral-medium`
- success: True  | final: 7.4 | quality: 8.44
- latency_total: 5.227s | tokens_per_second: 138.9
- input_tokens: 468 | output_tokens: 726
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presupuesto aprob: $8M CLP/mes x 3 pax\n   - JP hace JD p/ lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug p/ miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "14/04/26",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {"responsable": "Seba", "tarea": "fix webhook bug", "fecha_limite": "16/04"},
    {"responsable": "MaJo", "tarea": "actualizar roadmap en Notion", "fecha_limite": ""},
    {"responsable": "Cami", "tarea": "prep demo p/ cliente Falabella", "fecha_limite": "23/04"},
    {"responsable": "JP", "tarea": "publicar JDs en LinkedIn + GetOnBrd", "fecha_limite": ""}
  ],
  "fechas_clave": [
    {"fecha": "14/04/26", "evento": "Reunión equipo prod"},
    {"fecha": "28/04", "evento": "Lanzamiento v2.0 (original)"},
    {"fecha": "05/05", "evento": "Lanzamiento v2.0 (nueva fecha)"},
    {"fecha": "16/04", "evento": "Fecha límite para fix webhook bug"},
    {"fecha": "23/04", "evento": "Demo para cliente Falabella"},
    {"fecha": "21/04", "evento": "Próxima reunión"}
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 de 28/04 a 05/05",
    "Contratar 2 desarrolladores senior y 1 QA",
    "Presupuesto aprobado: $8M CLP/mes x 3 personas",
    "JP hace JD para lunes"
  ]
}
```