# Ministral 14B (NIM) — ocr_extraction/handwritten_notes_extraction

- model_id: `mistralai/ministral-14b-instruct-2512`
- success: True  | final: 7.08 | quality: 8.52
- latency_total: 52.582s | tokens_per_second: 22.5
- input_tokens: 468 | output_tokens: 1182
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
{
  "texto_corregido": "
  **Reunión equipo producto - 14/04/2026**
  **Asistentes:** JP, MaJo, Seba, Cami
  **Faltó:** Nico

  **1) Lanzamiento v2.0** → Postergado de **28/04** a **05/05**
  - Falta revisión QA en **módulo pagos**
  - Bug crítico en **API webhooks** → Seba lo gestiona

  **2) Métricas Q1 (vs Q4):**
  - **MRR:** $52.1k (+15%)
  - **Churn:** 3.1% (objetivo era 3.5%)
  - **NPS:** 51 (¡buen resultado!)

  **3) Contrataciones:**
  - **2 Devs Senior + 1 QA** aprobados
  - Presupuesto: **$8M CLP/mes** por 3 personas
  - JP elaborará las **JDs** para **Lunes 15/04**

  **4) Próxima reunión:** **Lunes 21/04** a las **10:00 AM**

  **Action items:**
  - Seba: Resolver bug de webhooks para **miércoles 16/04**
  - MaJo: Actualizar roadmap en Notion
  - Cami: Preparar demo para cliente Falabella (**23/04**)
  - JP: Publicar JD en LinkedIn + GetOnBoard",

  "fecha_reunion": "14/04/2026",

  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],

  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Resolver bug crítico en API webhooks",
      "fecha_limite": "16/04/2026 (miércoles)"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": "Sin fecha específica (prioridad inmediata)"
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "23/04/2026"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar JD en LinkedIn y GetOnBoard",
      "fecha_limite": "Sin fecha específica (depende de preparación JD)"
    },
    {
      "responsable": "JP",
      "tarea": "Elaborar JD para contrataciones",
      "fecha_limite": "15/04/2026 (lunes)"
    }
  ],

  "fechas_clave": [
    {
      "fecha": "14/04/2026",
      "evento": "Reunión producto (acta incluida)"
    },
    {
      "fecha": "15/04/2026 (lunes)",
      "evento": "Entrega de JD para contrataciones (JP)"
    },
    {
      "fecha": "16/04/2026 (miércoles)",
      "evento": "Plazo para resolver bug webhooks (Seba)"
    },
    {
      "fecha": "21/04/2026 (lunes)",
      "evento": "Próxima reunión del equipo (10:00 AM)"
    },
    {
      "fecha": "23/04/2026",
      "evento": "Demo para cliente Falabella (Cami)"
    },
    {
      "fecha": "28/04 → 05/05/2026",
      "evento": "Lanzamiento v2.0 postergado (original: 28/04, nueva fecha: 05/05)"
    }
  ],

  "decisiones": [
    {
      "descripcion": "Postergar lanzamiento v2.0 del 28/04 al 05/05 por pendientes en QA (módulo pagos) y bug en API webhooks",
      "responsables": ["Equipo QA", "Seba (bug API)"]
    },
    {
      "descripcion": "Aprobación de contratación de 2 Devs Senior + 1 QA con presupuesto de $8M CLP/mes por 3 personas",
      "detalles": "JDs a elaborar por JP para publicación el lunes 15/04"
    },
    {
      "descripcion": "Fijar métricas de Q1 como base para ajustes futuros (churn, NPS, MRR)",
      "contexto": "Resultados superaron objetivos en churn (3.1% vs 3.5%) y NPS mejoró a 51"
    },
    {
      "descripcion": "Siguiente reunión programada para el lunes 21/04 a las 10:00 AM"
    }
  ]
}
```