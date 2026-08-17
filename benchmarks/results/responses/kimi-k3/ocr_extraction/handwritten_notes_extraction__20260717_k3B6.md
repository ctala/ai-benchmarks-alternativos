# Kimi K3 — ocr_extraction/handwritten_notes_extraction

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 7.91 | quality: 10.0
- latency_total: 93.835s | tokens_per_second: 44.8
- input_tokens: 569 | output_tokens: 4203
- judge_score: 4.8 | justificación: 

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo producto - 14/04/2025\nAsisten: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover del 28 de abril al 5 de mayo\n   - Falta QA en módulo de pagos\n   - Bug crítico en API webhooks (lo toma Seba)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - Churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (¡muy bueno!)\n\n3) Contratar 2 devs senior + 1 QA\n   - Presupuesto aprobado: $8M CLP/mes x 3 personas\n   - JP hace JD para el lunes\n\n4) Próxima reunión: lunes 21/04 10am\n\nAction items:\n- Seba: fix bug webhooks para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "2025-04-14",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Arreglar bug crítico en API de webhooks",
      "fecha_limite": "2025-04-16"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": null
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "2025-04-23"
    },
    {
      "responsable": "JP",
      "tarea": "Redactar y publicar JDs en LinkedIn y GetOnBrd",
      "fecha_limite": "2025-04-21"
    }
  ],
  "fechas_clave": [
    {"fecha": "2025-04-14", "evento": "Reunión de equipo de producto"},
    {"fecha": "2025-04-16", "evento": "Límite: fix del bug de webhooks (Seba)"},
    {"fecha": "2025-04-21", "evento": "Próxima reunión 10:00 AM; límite para JDs de JP"},
    {"fecha": "2025-04-23", "evento": "Demo para cliente Falabella (Cami)"},
    {"fecha": "2025-04-28", "evento": "Fecha original de lanzamiento v2.0 (postergada)"},
    {"fecha": "2025-05-05", "evento": "Nueva fecha de lanzamiento v2.0"}
  ],
  "decisiones": [
    "Postergar el lanzamiento v2.0 del 28 de abril al 5 de mayo",
    "Seba asume la responsabilidad del bug crítico en la API de webhooks",
    "Aprobar contratación de 2 devs senior + 1 QA con presupuesto de $8M CLP/mes por 3 personas",
    "JP redacta las job descriptions para el lunes"
  ]
}
```

**Notas de interpretación:**

- **Año corregido (26 → 2025):** El OCR leyó "14/04/26", pero las referencias de días de semana solo cuadran con 2025: el 16/04/2025 es miércoles y el 21/04/2025 es lunes (en 2026 no coincidirían).
- **Deadline de JP:** No aparece en la lista de action items, pero se infiere del punto 3 ("JP hace JD p/ lunes") → lunes 21/04.
- **Abreviaciones expandidas:** `JD` = job description, `pax` = personas, `presup aprob` = presupuesto aprobado, `devs sr` = developers senior, `obj` = objetivo, `prep` = preparar.
- **"Re bueno"** (chilenismo) normalizado a "muy bueno".
- **MaJo** no tiene fecha límite explícita en las notas — podría valer la pena confirmarla en la próxima reunión.