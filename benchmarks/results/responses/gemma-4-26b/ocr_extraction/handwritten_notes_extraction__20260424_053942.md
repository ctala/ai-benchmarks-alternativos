# Gemma 4 26B MoE (3.8B activos) — ocr_extraction/handwritten_notes_extraction

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 7.25 | quality: 8.44
- latency_total: 14.977s | tokens_per_second: 60.8
- input_tokens: 488 | output_tokens: 911
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 pax\n   - JP hace JD para lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBoard",
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
      "tarea": "Fix webhook bug",
      "fecha_limite": "16/04/26"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "23/04/26"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar JDs en LinkedIn + GetOnBoard",
      "fecha_limite": ""
    },
    {
      "responsable": "JP",
      "tarea": "Hacer JD (Job Description)",
      "fecha_limite": "17/04/26"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/26",
      "evento": "Reunión equipo prod"
    },
    {
      "fecha": "16/04/26",
      "evento": "Deadline fix webhook bug (Seba)"
    },
    {
      "fecha": "17/04/26",
      "evento": "Plazo para JP de terminar JDs"
    },
    {
      "fecha": "21/04/26",
      "evento": "Próxima reunión (10am)"
    },
    {
      "fecha": "23/04/26",
      "evento": "Demo cliente Falabella (Cami)"
    },
    {
      "fecha": "28/04/26",
      "evento": "Fecha original lanzamiento v2.0 (reprogramada)"
    },
    {
      "fecha": "05/05/26",
      "evento": "Nueva fecha lanzamiento v2.0"
    }
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 del 28 de abril al 5 de mayo",
    "Aprobar presupuesto de $8M CLP/mes para la contratación de 2 devs sr y 1 QA"
  ]
}
```