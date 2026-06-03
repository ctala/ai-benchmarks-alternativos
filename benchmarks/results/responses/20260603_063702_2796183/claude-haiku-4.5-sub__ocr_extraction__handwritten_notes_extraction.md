# Claude Haiku 4.5 (suscripción) — ocr_extraction/handwritten_notes_extraction

- model_id: `claude-haiku-4-5`
- success: True  | final: 7.47 | quality: 9.1
- latency_total: 12.957s | tokens_per_second: 171.2
- input_tokens: 10 | output_tokens: 2218
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al proporcionar detalles estructurados y útiles para un emprendedor, y los datos extraídos son exactos.

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/2026\nAsistentes: JP, Majo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - Falta QA en módulo pagos\n   - Bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR $52.1k (+15% vs Q4)\n   - Churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (¡muy bueno!)\n\n3) Contratar 2 devs senior + 1 QA\n   - Presupuesto aprobado: $8M CLP/mes × 3 personas\n   - JP hace Job Description para lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction Items:\n- Seba: Arreglar webhook bug para miércoles 16/04\n- Majo: Actualizar roadmap en Notion\n- Cami: Preparar demo para cliente Falabella (23/04)\n- JP: Publicar JDs en LinkedIn + GetOnBoard",
  "fecha_reunion": "2026-04-14",
  "asistentes": [
    "JP",
    "Majo",
    "Seba",
    "Cami"
  ],
  "ausentes": [
    "Nico"
  ],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Arreglar bug crítico en API webhooks",
      "fecha_limite": "2026-04-16",
      "prioridad": "crítica"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar Job Descriptions en LinkedIn y GetOnBoard",
      "fecha_limite": "2026-04-21",
      "prioridad": "alta"
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "2026-04-23",
      "prioridad": "alta"
    },
    {
      "responsable": "Majo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": null,
      "prioridad": "media"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "2026-04-14",
      "evento": "Reunión equipo prod"
    },
    {
      "fecha": "2026-04-16",
      "evento": "Deadline: fix webhook bug (Seba)"
    },
    {
      "fecha": "2026-04-21",
      "evento": "Próxima reunión + deadline JDs (JP)"
    },
    {
      "fecha": "2026-04-23",
      "evento": "Demo cliente Falabella (Cami)"
    },
    {
      "fecha": "2026-04-28",
      "evento": "Fecha original lanzamiento v2.0 (MOVIDA)"
    },
    {
      "fecha": "2026-05-05",
      "evento": "Nueva fecha lanzamiento v2.0"
    }
  ],
  "decisiones": [
    {
      "tema": "Lanzamiento v2.0",
      "decision": "Mover de 28 abril a 5 mayo (una semana de delay)",
      "razon": "Falta QA en módulo pagos + bug crítico en webhooks"
    },
    {
      "tema": "Contrataciones",
      "decision": "Aprobar presupuesto $8M CLP/mes para 2 devs senior + 1 QA",
      "status": "Aprobado"
    },
    {
      "tema": "Métricas Q1",
      "decision": "MRR $52.1k (+15% YoQ), churn 3.1% (meta: 3.5% ✓), NPS 51",
      "status": "Objetivos cumplidos"
    }
  ]
}
```

**Resumen de correcciones OCR principales:**
- Acrónimos: "Reunlon" → "Reunión", "equlpo" → "equipo", "modul0" → "módulo"
- Errores visuales (0→o): "falt0" → "faltó", "webho0ks" → "webhooks", "dem0" → "demo", "actualzr" → "actualizar"
- Abreviaturas expandidas: "crit" → "crítico", "baj0" → "bajó", "presup" → "presupuesto", "mierc" → "miércoles"
- Siglas: "JD" → "Job Description", "GetOnBrd" → "GetOnBoard"
- Contexto temporal: "abr 28" → "28 abril", "may 5" → "5 mayo"