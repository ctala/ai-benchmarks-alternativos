# Qwen 3.7 Max — ocr_extraction/handwritten_notes_extraction

- model_id: `qwen/qwen3.7-max`
- success: True  | final: 6.59 | quality: 8.44
- latency_total: 77.316s | tokens_per_second: 71.1
- input_tokens: 480 | output_tokens: 5495
- judge_score: 4.4 | justificación: 

## Respuesta completa

{
  "texto_corregido": "Reunión equipo prod - 14/04/2026\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover del 28 de abril al 5 de mayo\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (el objetivo era 3.5%)\n   - NPS subió a 51 (¡re bueno!)\n\n3) Contratar 2 devs senior + 1 QA\n   - presupuesto aprobado: $8M CLP/mes por 3 personas\n   - JP hace las descripciones de cargo (JD) para el lunes\n\n4) Próxima reunión: lunes 21/04 10:00 am\n\nAction items:\n- Seba: arreglar bug de webhook para el miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar descripciones de cargo (JDs) en LinkedIn y GetOnBrd",
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
      "tarea": "Arreglar bug crítico en API webhooks",
      "fecha_limite": "16/04/2026"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": "No especificada"
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "23/04/2026"
    },
    {
      "responsable": "JP",
      "tarea": "Crear y publicar JDs (descripciones de cargo) en LinkedIn y GetOnBrd",
      "fecha_limite": "21/04/2026"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/2026",
      "evento": "Reunión de equipo prod"
    },
    {
      "fecha": "16/04/2026",
      "evento": "Fecha límite para arreglo de bug en webhooks"
    },
    {
      "fecha": "21/04/2026",
      "evento": "Próxima reunión de equipo y entrega de JDs"
    },
    {
      "fecha": "23/04/2026",
      "evento": "Demo para cliente Falabella"
    },
    {
      "fecha": "28/04/2026",
      "evento": "Fecha original de lanzamiento v2.0"
    },
    {
      "fecha": "05/05/2026",
      "evento": "Nueva fecha de lanzamiento v2.0"
    }
  ],
  "decisiones": [
    "Posponer el lanzamiento de la v2.0 del 28 de abril al 5 de mayo debido a la falta de QA en el módulo de pagos y un bug crítico en la API de webhooks.",
    "Aprobar un presupuesto de $8M CLP mensuales para la contratación de 2 desarrolladores senior y 1 QA.",
    "Delegar a JP la redacción de las descripciones de cargo (JD) para el lunes 21/04, como paso previo a la publicación de las ofertas."
  ]
}