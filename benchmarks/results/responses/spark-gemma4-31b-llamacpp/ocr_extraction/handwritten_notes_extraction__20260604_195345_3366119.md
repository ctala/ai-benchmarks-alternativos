# Gemma 4 31B (Spark llama-server Q4_K_M) — ocr_extraction/handwritten_notes_extraction

- model_id: `gemma-4-31B-it-Q4_K_M.gguf`
- success: True  | final: 7.21 | quality: 8.44
- latency_total: 92.783s | tokens_per_second: 9.6
- input_tokens: 476 | output_tokens: 893
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo producto - 14/04/26\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0: mover del 28 de abril al 5 de mayo.\n   - Falta QA en módulo de pagos.\n   - Bug crítico en API webhooks (Seba se encarga).\n\n2) Métricas Q1:\n   - MRR: 52.1k (+15% vs Q4).\n   - Churn: bajó a 3.1% (el objetivo era 3.5%).\n   - NPS: subió a 51.\n\n3) Contrataciones: 2 desarrolladores Senior + 1 QA.\n   - Presupuesto aprobado: $8M CLP mensuales por persona.\n   - JP redactará las descripciones de cargo (JD) para el lunes.\n\n4) Próxima reunión: lunes 21/04 a las 10:00 AM.\n\nAction items:\n- Seba: Corregir bug de webhook para el miércoles 16/04.\n- MaJo: Actualizar roadmap en Notion.\n- Cami: Preparar demo para el cliente Falabella (23/04).\n- JP: Publicar JDs en LinkedIn y GetOnBoard.",
  "fecha_reunion": "2026-04-14",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Corregir bug de webhook",
      "fecha_limite": "2026-04-16"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": "No especificada"
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "2026-04-23"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar descripciones de cargo (JDs) en LinkedIn y GetOnBoard",
      "fecha_limite": "2026-04-20"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "2026-04-14",
      "evento": "Reunión de equipo de producto"
    },
    {
      "fecha": "2026-04-16",
      "evento": "Fecha límite para fix de bug de webhooks"
    },
    {
      "fecha": "2026-04-20",
      "evento": "JP entrega/publica JDs"
    },
    {
      "fecha": "2026-04-21",
      "evento": "Próxima reunión de equipo (10:00 AM)"
    },
    {
      "fecha": "2026-04-23",
      "evento": "Demo cliente Falabella"
    },
    {
      "fecha": "2026-05-05",
      "evento": "Nueva fecha de lanzamiento v2.0"
    }
  ],
  "decisiones": [
    "Reprogramación del lanzamiento v2.0 del 28 de abril al 5 de mayo",
    "Aprobación de presupuesto de $8M CLP/mes por persona para 3 nuevas vacantes (2 Dev Sr, 1 QA)"
  ]
}
```