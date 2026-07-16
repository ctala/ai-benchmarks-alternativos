# MiniMax M2.7 — ocr_extraction/handwritten_notes_extraction

- model_id: `minimax/minimax-m2.7`
- success: True  | final: 8.76 | quality: 10.0
- latency_total: 26.953s | tokens_per_second: 50.7
- input_tokens: 446 | output_tokens: 1367
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al proporcionar detalles estructurados y accionables, y los datos extraídos son exactos.

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 26/04/14\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crit en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajo a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presup aprob: $8M CLP/mes x 3 pax\n   - JP hace JD para lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBoard",
  
  "fecha_reunion": "26/04/14 (14 de abril de 2026)",
  
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  
  "ausentes": ["Nico"],
  
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Corregir bug de webhooks",
      "fecha_limite": "16/04/2026"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": null
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "23/04/2026"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar JDs en LinkedIn + GetOnBoard",
      "fecha_limite": null
    },
    {
      "responsable": "JP",
      "tarea": "Hacer JD (Job Description) para nuevos hires",
      "fecha_limite": "21/04/2026 (lunes)"
    }
  ],
  
  "fechas_clave": [
    {"fecha": "14/04/2026", "evento": "Reunión de equipo prod"},
    {"fecha": "16/04/2026", "evento": "Fecha límite: fix webhook bug (Seba)"},
    {"fecha": "21/04/2026", "evento": "Próxima reunión - 10am"},
    {"fecha": "23/04/2026", "evento": "Demo para Falabella (Cami)"},
    {"fecha": "05/05/2026", "evento": "Lanzamiento v2.0"}
  ],
  
  "decisiones": [
    "Postergar lanzamiento v2.0 del 28 de abr al 5 de mayo",
    "Asignar a Seba la corrección del bug crítico en webhooks",
    "Contratar 2 devs senior + 1 QA (presupuesto aprobado: $8M CLP/mes x 3 personas)"
  ]
}
```

**Correcciones OCR aplicadas:**
| Error | Corrección |
|-------|------------|
| Reunlon | Reunión |
| equlpo prod | equipo prod |
| falt0 | faltó |
| Lanzamient0 | Lanzamiento |
| modul0 | módulo |
| webho0ks | webhooks |
| baj0 | bajo |
| actualzr | actualizar |
| presup | presupuesto |
| GetOnBrd | GetOnBoard |