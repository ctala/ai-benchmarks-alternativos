# Gemini 3.1 Flash Lite — ocr_extraction/handwritten_notes_extraction

- model_id: `google/gemini-3.1-flash-lite-preview`
- success: True  | final: 7.5 | quality: 8.44
- latency_total: 3.442s | tokens_per_second: 202.8
- input_tokens: 460 | output_tokens: 698
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo producto - 14/04/26\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abril 28 a mayo 5\n   - Falta QA en módulo pagos\n   - Bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - Churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (¡excelente!)\n\n3) Contratar 2 devs senior + 1 QA\n   - Presupuesto aprobado: $8M CLP/mes por 3 personas\n   - JP hace JD para el lunes\n\n4) Próxima reunión: lunes 21/04, 10 am",
  "fecha_reunion": "14/04/26",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Corregir bug en API webhooks",
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
      "tarea": "Publicar JDs en LinkedIn + GetOnBoard",
      "fecha_limite": "No especificada"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "16/04/26",
      "evento": "Fecha límite fix webhook (Seba)"
    },
    {
      "fecha": "21/04/26",
      "evento": "Próxima reunión de equipo"
    },
    {
      "fecha": "23/04/26",
      "evento": "Demo para cliente Falabella"
    },
    {
      "fecha": "05/05/26",
      "evento": "Nueva fecha lanzamiento v2.0"
    }
  ],
  "decisiones": [
    "Postergación del lanzamiento v2.0 del 28 de abril al 5 de mayo",
    "Aprobación de presupuesto de $8M CLP/mes para la contratación de 3 nuevos integrantes (2 devs senior y 1 QA)"
  ]
}
```