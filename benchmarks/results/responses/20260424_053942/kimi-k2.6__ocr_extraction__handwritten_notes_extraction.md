# Kimi K2.6 — ocr_extraction/handwritten_notes_extraction

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 6.45 | quality: 8.44
- latency_total: 369.107s | tokens_per_second: 16.4
- input_tokens: 485 | output_tokens: 6059
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/2026\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover del 28/04 al 05/05\n   - Falta QA en módulo pagos\n   - Bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - Churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (¡re bueno!)\n\n3) Contratar 2 desarrolladores senior + 1 QA\n   - Presupuesto aprobado: $8M CLP/mes por 3 personas\n   - JP prepara JD para el lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "14/04/2026",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Fix bug crítico en API webhooks",
      "fecha_limite": "16/04/2026"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "23/04/2026"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar JDs en LinkedIn + GetOnBrd",
      "fecha_limite": "21/04/2026"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/2026",
      "evento": "Reunión equipo producto"
    },
    {
      "fecha": "16/04/2026",
      "evento": "Entrega fix bug webhooks (Seba)"
    },
    {
      "fecha": "21/04/2026",
      "evento": "Próxima reunión / Publicación JDs (JP)"
    },
    {
      "fecha": "23/04/2026",
      "evento": "Demo cliente Falabella (Cami)"
    },
    {
      "fecha": "28/04/2026",
      "evento": "Fecha original lanzamiento v2.0"
    },
    {
      "fecha": "05/05/2026",
      "evento": "Nueva fecha lanzamiento v2.0"
    }
  ],
  "decisiones": [
    "Postergar lanzamiento v2.0 del 28/04 al 05/05 debido a pendientes de QA en módulo pagos y bug crítico en API webhooks",
    "Aprobar presupuesto de $8M CLP/mes para contratar 2 desarrolladores senior y 1 QA (3 personas)",
    "Asignar a Seba la corrección del bug crítico en API webhooks"
  ]
}
```