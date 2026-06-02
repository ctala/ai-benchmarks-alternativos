# Qwen 3.6 Max — ocr_extraction/handwritten_notes_extraction

- model_id: `qwen/qwen3.6-max-preview`
- success: True  | final: 7.1 | quality: 9.28
- latency_total: 84.708s | tokens_per_second: 51.3
- input_tokens: 480 | output_tokens: 4343
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al proporcionar detalles adicionales como fechas clave y decisiones, y los datos extraídos son exactos.

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo producto - 14/04/2026\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (¡muy bueno!)\n\n3) Contratar 2 devs senior + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 personas\n   - JP redacta JD (Job Description) para el lunes\n\n4) Próxima reunión: lunes 21/04 10:00 am\n\nAction items:\n- Seba: corregir bug de webhooks para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBoard",
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
      "tarea": "Corregir bug crítico en API de webhooks",
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
      "tarea": "Redactar y publicar JDs en LinkedIn y GetOnBoard",
      "fecha_limite": "21/04/2026"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/2026",
      "evento": "Reunión de equipo de producto"
    },
    {
      "fecha": "16/04/2026",
      "evento": "Fecha límite: Corrección de bug de webhooks (Seba)"
    },
    {
      "fecha": "21/04/2026",
      "evento": "Fecha límite: Publicación de JDs (JP) y próxima reunión de equipo (10:00 am)"
    },
    {
      "fecha": "23/04/2026",
      "evento": "Demo para cliente Falabella (Cami)"
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
    "Postergar el lanzamiento de la versión 2.0 del 28 de abril al 5 de mayo debido a pendientes de QA y un bug crítico.",
    "Asignar a Seba la responsabilidad de corregir el bug crítico en la API de webhooks.",
    "Aprobar un presupuesto de $8M CLP/mes para contratar a 2 desarrolladores senior y 1 QA.",
    "Encargar a JP la redacción y publicación de las descripciones de puesto (JDs) antes del lunes 21/04."
  ]
}
```