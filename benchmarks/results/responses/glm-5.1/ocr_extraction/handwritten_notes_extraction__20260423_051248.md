# GLM-5.1 — ocr_extraction/handwritten_notes_extraction

- model_id: `z-ai/glm-5.1`
- success: True  | final: 6.65 | quality: 8.44
- latency_total: 65.625s | tokens_per_second: 53.9
- input_tokens: 452 | output_tokens: 3535
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsisten: JP, MaJo, Seba, Cami (falta Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 pax\n   - JP hace JD para lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "14/04/2026",
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
      "tarea": "Fix webhook bug",
      "fecha_limite": "16/04/2026"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "Prep demo para cliente Falabella",
      "fecha_limite": "23/04/2026"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar JDs en LinkedIn + GetOnBrd",
      "fecha_limite": "Lunes 21/04/2026"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/2026",
      "evento": "Reunión equipo prod"
    },
    {
      "fecha": "16/04/2026",
      "evento": "Entrega fix webhook bug (Seba)"
    },
    {
      "fecha": "21/04/2026",
      "evento": "Próxima reunión / JP hace JD"
    },
    {
      "fecha": "23/04/2026",
      "evento": "Demo para cliente Falabella (Cami)"
    },
    {
      "fecha": "28/04/2026",
      "evento": "Lanzamiento v2.0 (fecha original)"
    },
    {
      "fecha": "05/05/2026",
      "evento": "Lanzamiento v2.0 (nueva fecha)"
    }
  ],
  "decisiones": [
    "Mover la fecha de lanzamiento v2.0 del 28 de abril al 5 de mayo",
    "Aprobar presupuesto de $8M CLP/mes para contratar 2 devs sr + 1 QA"
  ]
}
```