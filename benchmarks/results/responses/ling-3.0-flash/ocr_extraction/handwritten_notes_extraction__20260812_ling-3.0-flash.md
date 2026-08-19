# Ling 3.0 Flash — ocr_extraction/handwritten_notes_extraction

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 9.38 | quality: 10.0
- latency_total: 8.267s | tokens_per_second: 435.2
- input_tokens: 537 | output_tokens: 3598
- judge_score: 4.8 | justificación: 

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo producto - 14/04/26\nAsist: JP, MaJo, Seba, Cami (falta Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 personas\n   - JP hace JD para lunes\n\n4) Próxima reunión: lunes 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBoard",
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
      "fecha_limite": "Sin fecha límite especificada"
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "23/04/2026"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar JDs en LinkedIn + GetOnBoard",
      "fecha_limite": "Sin fecha límite especificada"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/2026",
      "evento": "Reunión equipo producto"
    },
    {
      "fecha": "16/04/2026",
      "evento": "Deadline fix webhook bug (Seba)"
    },
    {
      "fecha": "21/04/2026",
      "evento": "Próxima reunión (10am)"
    },
    {
      "fecha": "23/04/2026",
      "evento": "Demo cliente Falabella (Cami)"
    },
    {
      "fecha": "28/04/2026",
      "evento": "Lanzamiento v2.0 (fecha original, pospuesta)"
    },
    {
      "fecha": "05/05/2026",
      "evento": "Lanzamiento v2.0 (nueva fecha)"
    }
  ],
  "decisiones": [
    "Lanzamiento v2.0 se reprograma del 28/04 al 05/05",
    "Contratación de 2 devs Sr + 1 QA aprobada con presupuesto de $8M CLP/mes por 3 personas",
    "Bug crítico en API webhooks asignado a Seba"
  ]
}
```