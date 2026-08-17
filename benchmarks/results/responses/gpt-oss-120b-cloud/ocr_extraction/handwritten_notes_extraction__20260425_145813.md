# GPT-OSS 120B (Ollama Cloud) — ocr_extraction/handwritten_notes_extraction

- model_id: `gpt-oss:120b-cloud`
- success: True  | final: 7.7 | quality: 8.44
- latency_total: 29.706s | tokens_per_second: 68.4
- input_tokens: 502 | output_tokens: 2033
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/2026\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de 28 abr a 5 may\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (¡re bueno!)\n\n3) Contratar 2 devs senior + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 pax\n   - JP hace JD para lunes\n\n4) Próx reunión: lun 21/04 10:00\n\nAction items:\n- Seba: arreglar bug del webhook para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBoard",
  "fecha_reunion": "2026-04-14",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Arreglar bug del webhook",
      "fecha_limite": "2026-04-16"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": null
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "2026-04-23"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar JDs en LinkedIn + GetOnBoard",
      "fecha_limite": null
    }
  ],
  "fechas_clave": [
    {
      "fecha": "2026-04-14",
      "evento": "Reunión del equipo de producto"
    },
    {
      "fecha": "2026-04-28",
      "evento": "Fecha original del lanzamiento v2.0 (reprogramada)"
    },
    {
      "fecha": "2026-05-05",
      "evento": "Nuevo lanzamiento v2.0"
    },
    {
      "fecha": "2026-04-16",
      "evento": "Deadline para arreglar bug del webhook"
    },
    {
      "fecha": "2026-04-21",
      "evento": "Próxima reunión del equipo"
    },
    {
      "fecha": "2026-04-23",
      "evento": "Demo para cliente Falabella"
    }
  ],
  "decisiones": [
    "Reprogramar el lanzamiento de la versión 2.0 del producto del 28‑abr al 5‑may.",
    "Asignar QA al módulo de pagos.",
    "Priorizar la corrección del bug crítico en la API de webhooks (responsable: Seba).",
    "Contratar 2 desarrolladores senior y 1 QA con presupuesto aprobado de $8 M CLP/mes para 3 personas.",
    "JP redactará la descripción del puesto (JD) para el lunes siguiente.",
    "Se definió la fecha de la próxima reunión: lunes 21‑abr a las 10:00."
  ]
}
```