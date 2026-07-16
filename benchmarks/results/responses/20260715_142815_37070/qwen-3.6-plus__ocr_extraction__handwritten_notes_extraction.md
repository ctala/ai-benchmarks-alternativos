# Qwen 3.6 Plus — ocr_extraction/handwritten_notes_extraction

- model_id: `qwen/qwen3.6-plus`
- success: True  | final: 8.55 | quality: 10.0
- latency_total: 91.13s | tokens_per_second: 54.6
- input_tokens: 480 | output_tokens: 4976
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una buena estructura y utilidad práctica, proporcionando detalles útiles para un emprendedor, y los datos extraídos son exactos.

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 pax\n   - JP hace JD para lunes\n\n4) Próxima reunión: lunes 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "14/04/26",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {"responsable": "Seba", "tarea": "Corregir bug crítico en API de webhooks", "fecha_limite": "16/04/26"},
    {"responsable": "MaJo", "tarea": "Actualizar roadmap en Notion", "fecha_limite": "Sin fecha específica"},
    {"responsable": "Cami", "tarea": "Preparar demo para cliente Falabella", "fecha_limite": "23/04/26"},
    {"responsable": "JP", "tarea": "Redactar y publicar JDs en LinkedIn y GetOnBrd", "fecha_limite": "21/04/26"}
  ],
  "fechas_clave": [
    {"fecha": "14/04/26", "evento": "Reunión actual de equipo de producto"},
    {"fecha": "16/04/26", "evento": "Deadline corrección bug webhooks"},
    {"fecha": "21/04/26", "evento": "Próxima reunión y publicación de ofertas laborales"},
    {"fecha": "23/04/26", "evento": "Demo para cliente Falabella"},
    {"fecha": "28/04/26", "evento": "Fecha original programada para lanzamiento v2.0 (pospuesta)"},
    {"fecha": "05/05/26", "evento": "Nueva fecha de lanzamiento v2.0"}
  ],
  "decisiones": [
    "Reprogramar el lanzamiento de la versión 2.0 del 28/04 al 05/05.",
    "Asignar a Seba la corrección del bug crítico en la API de webhooks.",
    "Aprobar la contratación de 2 desarrolladores senior y 1 QA con presupuesto de $8M CLP/mes por persona.",
    "JP se encargará de redactar y publicar las descripciones de puesto (JD) para el lunes.",
    "Agendar próxima reunión de seguimiento para el lunes 21/04 a las 10:00 a.m."
  ]
}
```