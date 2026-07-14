# Ministral 14B — ocr_extraction/handwritten_notes_extraction

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 9.2 | quality: 10.0
- latency_total: 9.702s | tokens_per_second: 98.2
- input_tokens: 468 | output_tokens: 953
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al proporcionar detalles y estructura, y los datos extraídos son exactos.

## Respuesta completa

```json
{
  "texto_corregido": "
  **Reunión equipo producto - 14/04/2026**
  Asistentes: JP, MaJo, Seba, Cami
  Ausente: Nico

  **Puntos tratados:**
  1) **Lanzamiento v2.0**: Postergado de 28/04 a 05/05
     - Falta revisión QA en módulo pagos.
     - Bug crítico en API webhooks (Seba se hace cargo).

  2) **Métricas Q1**:
     - MRR: $52.1k (+15% vs Q4).
     - Churn: 3.1% (objetivo era 3.5%).
     - NPS: 51 (¡muy bueno!).

  3) **Contratación**:
     - 2 desarrolladores senior + 1 QA.
     - Presupuesto aprobado: $8M CLP/mes por 3 personas.
     - JP redactará las JD para lunes.

  4) **Próxima reunión**: Lunes 21/04 a las 10:00 AM.
  ",

  "fecha_reunion": "14/04/2026",

  "asistentes": ["JP", "MaJo", "Seba", "Cami"],

  "ausentes": ["Nico"],

  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Corregir bug en webhooks de la API",
      "fecha_limite": "16/04/2026 (miércoles)"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": "Sin fecha específica (prioridad alta)"
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "23/04/2026"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar JDs en LinkedIn y GetOnBoard",
      "fecha_limite": "Sin fecha específica (prioridad alta)"
    }
  ],

  "fechas_clave": [
    {
      "fecha": "28/04/2026 (original)",
      "evento": "Fecha inicial planificada para lanzamiento v2.0 (postergada)"
    },
    {
      "fecha": "05/05/2026",
      "evento": "Nueva fecha de lanzamiento v2.0"
    },
    {
      "fecha": "16/04/2026",
      "evento": "Fecha límite para resolver bug en webhooks"
    },
    {
      "fecha": "21/04/2026",
      "evento": "Próxima reunión del equipo"
    },
    {
      "fecha": "23/04/2026",
      "evento": "Demo para cliente Falabella"
    },
    {
      "fecha": "15/04/2026 (lunes)",
      "evento": "Entrega de JD para contratación (redacción)"
    }
  ],

  "decisiones": [
    {
      "punto": "Lanzamiento v2.0",
      "detalle": "Postergación de la fecha de 28/04 a 05/05 por pendientes en QA y bug crítico en API."
    },
    {
      "punto": "Contratación",
      "detalle": "Aprobación de presupuesto para 3 nuevos roles (2 devs senior + 1 QA) con un costo de $8M CLP/mes."
    },
    {
      "punto": "Métricas Q1",
      "detalle": "Destacar el buen desempeño en MRR, churn y NPS, superando objetivos en churn y NPS."
    },
    {
      "punto": "Asignación de tareas",
      "detalle": "Distribución clara de action items por responsable."
    }
  ]
}
```