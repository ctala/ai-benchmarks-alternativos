# Gemma 4 12B (Spark llama-server, reasoning) — ocr_extraction/handwritten_notes_extraction

- model_id: `gemma-4-12b-it-Q4_K_M.gguf`
- success: True  | final: 7.33 | quality: 8.44
- latency_total: 100.246s | tokens_per_second: 25.5
- input_tokens: 474 | output_tokens: 2558
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/2026\nAsistentes: JP, MaJo, Seba, Cami (Faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (muy bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 personas\n   - JP hace JD para lunes\n\n4) Próxima reunión: lun 21/04 10:00 am\n\nAction items:\n- Seba: fix webhook bug para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
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
      "fecha_limite": "16/04"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": null
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "23/04"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar JDs en LinkedIn + GetOnBrd",
      "fecha_limite": null
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/2026",
      "evento": "Reunión de equipo producción"
    },
    {
      "fecha": "16/04/2026",
      "evento": "Límite para corrección de bug en webhook (Seba)"
    },
    {
      "fecha": "21/04/2026",
      "evento": "Próxima reunión (10:00 am)"
    },
    {
      "fecha": "23/04/2026",
      "evento": "Demo para cliente Falabella"
    },
    {
      "fecha": "28/04/2026",
      "evento": "Fecha original de lanzamiento v2.0 (postergada)"
    },
    {
      "fecha": "05/05/2026",
      "evento": "Nueva fecha de lanzamiento v2.0"
    }
  ],
  "decisiones": [
    "Postergación del lanzamiento v2.0 del 28 de abril al 5 de mayo.",
    "Aprobación de presupuesto de $8M CLP/mes para la contratación de 3 nuevos integrantes (2 devs sr + 1 QA).",
    "Asignación de Seba para resolver el bug crítico en la API de webhooks."
  ]
}
```