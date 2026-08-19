# DeepSeek R1 (reasoning) — ocr_extraction/handwritten_notes_extraction

- model_id: `deepseek/deepseek-r1`
- success: True  | final: 7.25 | quality: 9.24
- latency_total: 66.793s | tokens_per_second: 25.7
- input_tokens: 473 | output_tokens: 1719
- judge_score: 4.8 | justificación: 

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de 28 abr a 5 may\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (muy bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 personas\n   - JP hace Job Description para lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "2026-04-14",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {"responsable": "Seba", "tarea": "Corregir bug crítico en API webhooks", "fecha_limite": "2026-04-16"},
    {"responsable": "MaJo", "tarea": "Actualizar roadmap en Notion", "fecha_limite": null},
    {"responsable": "Cami", "tarea": "Preparar demo para cliente Falabella", "fecha_limite": "2026-04-23"},
    {"responsable": "JP", "tarea": "Publicar Job Descriptions en LinkedIn + GetOnBrd", "fecha_limite": "2026-04-17"}
  ],
  "fechas_clave": [
    {"fecha": "2026-04-16", "evento": "Fecha límite corrección bug webhooks (Seba)"},
    {"fecha": "2026-04-17", "evento": "Entrega de Job Descriptions (JP)"},
    {"fecha": "2026-04-21", "evento": "Próxima reunión de equipo"},
    {"fecha": "2026-04-23", "evento": "Demo para cliente Falabella (Cami)"},
    {"fecha": "2026-04-28", "evento": "Fecha original lanzamiento v2.0"},
    {"fecha": "2026-05-05", "evento": "Nueva fecha lanzamiento v2.0"}
  ],
  "decisiones": [
    "Retrasar lanzamiento de v2.0 del 28 de abril al 5 de mayo",
    "Aprobar presupuesto de $8M CLP/mes para contratación de 2 desarrolladores senior y 1 QA"
  ]
}
```

### Notas explicativas:
1. **Correcciones OCR principales**:
   - "Reunlon" → "Reunión", "Lanzamient0" → "Lanzamiento"
   - "falt0" → "faltó", "modul0" → "módulo", "webho0ks" → "webhooks"
   - Fechas en formato completo (ej. "mierc 16/04" → "miércoles 16/04")
   - Abreviaturas expandidas: "obj" → "objetivo", "JD" → "Job Description"

2. **Manejo de fechas**:
   - Todas las fechas asumen año 2026 (por "14/04/26"), excepto:
   - "lunes 21/04" se infiere como 21/04/2026 (coherente con fecha reunión)
   - Fechas límite sin año se contextualizan con 2026.

3. **Action Items**:
   - Fecha de JP ("para lunes") calculada como 17/04/2026 (lunes posterior a reunión del 14/04).
   - Tareas sin fecha explícita (ej. actualizar roadmap) no tienen fecha límite.

4. **Contexto adicional**:
   - "Q1" se refiere al primer trimestre del año (previo a abril 2026).
   - "MaJo" y "Seba" se conservan como abreviaturas recurrentes en notas.
   - "re bueno" interpretado como "muy bueno" en contexto profesional.