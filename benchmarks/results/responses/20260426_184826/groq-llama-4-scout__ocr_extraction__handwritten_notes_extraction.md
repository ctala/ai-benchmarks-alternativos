# Llama 4 Scout 17B (Groq preview) — ocr_extraction/handwritten_notes_extraction

- model_id: `meta-llama/llama-4-scout-17b-16e-instruct`
- success: True  | final: 7.8 | quality: 8.44
- latency_total: 2.442s | tokens_per_second: 279.3
- input_tokens: 440 | output_tokens: 682
- judge_score: 4.4 | justificación: 

## Respuesta completa

Aquí te presento la respuesta en formato JSON:

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajo a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presup aprob: $8M CLP/mes x 3 pax\n   - JP hace JD p/ lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug p/ miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "14/04/26",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {"responsable": "Seba", "tarea": "Fix webhook bug", "fecha_limite": "16/04"},
    {"responsable": "MaJo", "tarea": "Actualizar roadmap en Notion", "fecha_limite": ""},
    {"responsable": "Cami", "tarea": "Preparar demo para cliente Falabella", "fecha_limite": "23/04"},
    {"responsable": "JP", "tarea": "Publicar JDs en LinkedIn + GetOnBrd", "fecha_limite": ""}
  ],
  "fechas_clave": [
    {"fecha": "14/04/26", "evento": "Reunión de equipo"},
    {"fecha": "16/04", "evento": "Fix webhook bug"},
    {"fecha": "21/04", "evento": "Próxima reunión"},
    {"fecha": "23/04", "evento": "Demo para cliente Falabella"},
    {"fecha": "28/04", "evento": "Lanzamiento v2.0 (previsto)"},
    {"fecha": "05/05", "evento": "Lanzamiento v2.0 (reprogramado)"}
  ],
  "decisiones": [
    {"descripcion": "Lanzamiento v2.0 reprogramado para el 05/05"},
    {"descripcion": "Contratación de 2 devs sr + 1 QA aprobada"},
    {"descripcion": "Presupuesto aprobado: $8M CLP/mes x 3 pax"}
  ]
}
```

Espero que esto sea lo que necesitas. ¡Si tienes alguna pregunta o necesitas más ayuda, no dudes en preguntar!