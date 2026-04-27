# MiMo V2.5-Pro (Xiaomi) — ocr_extraction/handwritten_notes_extraction

- model_id: `mimo-v2.5-pro`
- success: True  | final: 7.55 | quality: 8.44
- latency_total: 28.45s | tokens_per_second: 72.0
- input_tokens: 477 | output_tokens: 2048
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/2026\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - Falta QA en módulo pagos\n   - Bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - Churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - Presupuesto aprobado: $8M CLP/mes x 3 personas\n   - JP hace JD para lunes\n\n4) Próxima reunión: lunes 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",

  "fecha_reunion": "2026-04-14",

  "asistentes": ["JP", "MaJo", "Seba", "Cami"],

  "ausentes": ["Nico"],

  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Fix bug crítico en API webhooks",
      "fecha_limite": "2026-04-16"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "2026-04-23"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar Job Descriptions en LinkedIn + GetOnBrd",
      "fecha_limite": "2026-04-21"
    }
  ],

  "fechas_clave": [
    {
      "fecha": "2026-04-14",
      "evento": "Reunión equipo prod"
    },
    {
      "fecha": "2026-04-16",
      "evento": "Deadline: fix bug webhooks (Seba)"
    },
    {
      "fecha": "2026-04-21",
      "evento": "Próxima reunión equipo (10am) / JP publica JDs"
    },
    {
      "fecha": "2026-04-23",
      "evento": "Demo cliente Falabella"
    },
    {
      "fecha": "2026-04-28",
      "evento": "Fecha original de lanzamiento v2.0"
    },
    {
      "fecha": "2026-05-05",
      "evento": "Nueva fecha de lanzamiento v2.0"
    }
  ],

  "decisiones": [
    "Mover lanzamiento v2.0 del 28 de abril al 5 de mayo por falta de QA en módulo pagos y bug crítico en API webhooks",
    "Aprobar presupuesto de $8M CLP/mes para contratar 2 desarrolladores senior y 1 QA",
    "JP se compromete a redactar y public