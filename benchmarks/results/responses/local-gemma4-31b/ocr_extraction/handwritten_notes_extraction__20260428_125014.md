# Gemma 4 31B (DGX Spark Q4_K_M) — ocr_extraction/handwritten_notes_extraction

- model_id: `gemma4:31b`
- success: True  | final: 6.65 | quality: 8.44
- latency_total: 225.432s | tokens_per_second: 9.2
- input_tokens: 474 | output_tokens: 2084
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo producto - 14/04/26\nAsistentes: JP, MaJo, Seba, Cami (Ausente: Nico)\n\n1) Lanzamiento v2.0: Se mueve la fecha del 28 de abril al 5 de mayo.\n   - Pendiente: QA en módulo de pagos.\n   - Problema: Bug crítico en API de webhooks (Seba se encarga).\n\n2) Métricas Q1:\n   - MRR: 52.1k (+15% vs Q4).\n   - Churn: bajó a 3.1% (el objetivo era 3.5%).\n   - NPS: subió a 51 (resultado muy positivo).\n\n3) Contrataciones: Contratar 2 desarrolladores Senior y 1 QA.\n   - Presupuesto aprobado: $8M CLP mensual por persona (3 personas).\n   - JP redactará las Job Descriptions (JD) para el lunes.\n\n4) Próxima reunión: lunes 21/04 a las 10:00 am.\n\nAction items:\n- Seba: Corregir bug de webhooks para el miércoles 16/04.\n- MaJo: Actualizar roadmap en Notion.\n- Cami: Preparar demo para el cliente Falabella (23/04).\n- JP: Publicar JDs en LinkedIn y GetOnBoard.",
  "fecha_reunion": "14/04/26",
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
      "tarea": "Corregir bug crítico en API de webhooks",
      "fecha_limite": "16/04/26"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": "No especificada"
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "23/04/26"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar Job Descriptions (JDs) en LinkedIn y GetOnBoard",
      "fecha_limite": "No especificada"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/26",
      "evento": "Reunión de equipo de producto"
    },
    {
      "fecha": "16/04/26",
      "evento": "Fecha límite para fix de bug de webhooks"
    },
    {
      "fecha": "21/04/26",
      "evento": "Próxima reunión de equipo (10:00 am)"
    },
    {
      "fecha": "23/04/26",
      "evento": "Demo cliente Falabella"
    },
    {
      "fecha": "28/04/26",
      "evento": "Fecha original de lanzamiento v2.0 (cancelada)"
    },
    {
      "fecha": "05/05/26",
      "evento": "Nueva fecha de lanzamiento v2.0"
    }
  ],
  "decisiones": [
    "Reprogramación del lanzamiento v2.0 del 28 de abril al 5 de mayo.",
    "Aprobación de presupuesto de $8M CLP mensuales por persona para la contratación de 2 Devs Senior y 1 QA."
  ]
}
```