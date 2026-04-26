# DeepSeek V4 Flash (NIM) — ocr_extraction/handwritten_notes_extraction

- model_id: `deepseek-ai/deepseek-v4-flash`
- success: True  | final: 6.95 | quality: 8.44
- latency_total: 123.854s | tokens_per_second: 6.4
- input_tokens: 472 | output_tokens: 793
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (¡muy bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 pax\n   - JP hace JD para lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "2026-04-14",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "fix webhook bug",
      "fecha_limite": "2026-04-16"
    },
    {
      "responsable": "MaJo",
      "tarea": "actualizar roadmap en Notion",
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "preparar demo para cliente Falabella",
      "fecha_limite": "2026-04-23"
    },
    {
      "responsable": "JP",
      "tarea": "publicar JDs en LinkedIn + GetOnBrd",
      "fecha_limite": ""
    }
  ],
  "fechas_clave": [
    {
      "fecha": "2026-04-14",
      "evento": "Reunión equipo prod"
    },
    {
      "fecha": "2026-04-16",
      "evento": "Fecha límite fix webhook bug (Seba)"
    },
    {
      "fecha": "2026-04-21",
      "evento": "Próxima reunión 10am"
    },
    {
      "fecha": "2026-04-23",
      "evento": "Demo cliente Falabella (Cami)"
    },
    {
      "fecha": "2026-04-28",
      "evento": "Lanzamiento v2.0 (original)"
    },
    {
      "fecha": "2026-05-05",
      "evento": "Lanzamiento v2.0 (nueva fecha)"
    }
  ],
  "decisiones": [
    "Lanzamiento v2.0 se mueve del 28 de abril al 5 de mayo",
    "Se aprueba presupuesto de $8M CLP/mes para contratar 2 devs sr + 1 QA",
    "JP debe preparar la descripción del cargo (JD) para el lunes siguiente"
  ]
}
```