# Solar Pro 4 — ocr_extraction/handwritten_notes_extraction

- model_id: `upstage/solar-pro4`
- success: True  | final: 8.88 | quality: 10.0
- latency_total: 30.129s | tokens_per_second: 27.7
- input_tokens: 523 | output_tokens: 835

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (falta Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presup aprobado: $8M CLP/mes x 3 pax\n   - JP hace JD p/ lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug p/ miér 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "2026-04-14",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Fix bug en API webhooks",
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
      "tarea": "Publicar JDs en LinkedIn + GetOnBrd",
      "fecha_limite": ""
    }
  ],
  "fechas_clave": [
    {
      "fecha": "2026-04-14",
      "evento": "Reunión equipo de producto"
    },
    {
      "fecha": "2026-04-16",
      "evento": "Fecha límite para fix del bug de webhooks (Seba)"
    },
    {
      "fecha": "2026-04-21",
      "evento": "Próxima reunión (10am)"
    },
    {
      "fecha": "2026-04-28",
      "evento": "Fecha original de lanzamiento v2.0 (postergado)"
    },
    {
      "fecha": "2026-05-05",
      "evento": "Nueva fecha de lanzamiento v2.0"
    },
    {
      "fecha": "2026-04-23",
      "evento": "Demo para cliente Falabella (Cami)"
    }
  ],
  "decisiones": [
    "Postergar lanzamiento v2.0 de 28/04 a 05/05",
    "Aprobar presupuesto de $8M CLP/mes por 3 personas para contratar 2 devs senior + 1 QA",
    "Asignar a Seba la corrección del bug crítico en API webhooks"
  ]
}
```