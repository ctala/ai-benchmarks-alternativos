# Nemotron Nano 9B v2 (NIM) — ocr_extraction/handwritten_notes_extraction

- model_id: `nvidia/nvidia-nemotron-nano-9b-v2`
- success: True  | final: 7.06 | quality: 8.16
- latency_total: 29.12s | tokens_per_second: 48.4
- input_tokens: 475 | output_tokens: 1409
- judge_score: 4.2 | justificación: 

## Respuesta completa



{
  "texto_corregido": "Reunión equipo producto - 14/04/26\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abril 28 a mayo 5\n   - falta QA en módulo de pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Metricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs senior + 1 QA\n   - presup aprob: $8M CLP/mes x 3 personas\n   - JP hará JD para lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAcciones pendientes:\n- Seba: corregir el bug de webhook para el miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn y GetOnBoard",
  "fecha_reunion": "14/04/26",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {"responsable": "Seba", "tarea": "corregir el bug de webhook", "fecha_limite": "16/04"},
    {"responsable": "MaJo", "tarea": "actualizar roadmap en Notion", "fecha_limite": ""},
    {"responsable": "Cami", "tarea": "preparar demo para cliente Falabella", "fecha_limite": "23/04"},
    {"responsable": "JP", "tarea": "publicar JDs en LinkedIn y GetOnBoard", "fecha_limite": ""}
  ],
  "fechas_clave": [
    {"fecha": "14/04/26", "evento": "Reunión equipo producto"},
    {"fecha": "16/04", "evento": "Fecha límite para Seba corregir bug webhook"},
    {"fecha": "21/04", "evento": "Próxima reunión"},
    {"fecha": "23/04", "evento": "Límite para demo de Falabella"}
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 de abril 28 a mayo 5",
    "Contratar 2 devs senior y 1 QA ($8M CLP/mes)",
    "Aprobación de presupuesto para contrataciones"
  ]
}
