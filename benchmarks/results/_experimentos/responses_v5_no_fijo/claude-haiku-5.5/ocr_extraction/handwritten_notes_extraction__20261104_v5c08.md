# Claude Haiku 5.5 — ocr_extraction/handwritten_notes_extraction

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 9.15 | quality: 10.0
- latency_total: 5.171s | tokens_per_second: 265.9
- input_tokens: 673 | output_tokens: 1375

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un sistema de OCR que interpreta notas manuscritas. Debes descifrar abreviaciones y organizar la informacion.

**user:**

Tengo una foto de notas manuscritas de una reunion. El texto reconocido (con errores tipicos de OCR en escritura a mano) es:

"Reunlon equlpo prod - 14/04/26
Asist: JP, MaJo, Seba, Cami (falt0 Nico)

1) Lanzamient0 v2.0 - mover de abr 28 a may 5
   - falta QA en modul0 pagos
   - bug crit en API webho0ks (Seba lo toma)

2) Metricas Q1:
   - MRR 52.1k (+15% vs Q4)
   - churn baj0 a 3.1% (obj era 3.5%)
   - NPS subio a 51 (re bueno!!)

3) Contratar 2 devs sr + 1 QA
   - presup aprob: $8M CLP/mes x 3 pax
   - JP hace JD p/ lunes

4) Prox reunion: lun 21/04 10am

Action items:
- Seba: fix webhook bug p/ mierc 16/04
- MaJo: actualzr roadmap en Notion
- Cami: prep demo p/ cliente Falabella (23/04)
- JP: publicar JDs en LinkedIn + GetOnBrd"

Tareas:
1. Corrige los errores de OCR y presenta el texto limpio
2. Extrae los action items en formato estructurado
3. Identifica las fechas mencionadas y crea un timeline

Responde en JSON:
{
  "texto_corregido": "",
  "fecha_reunion": "",
  "asistentes": [],
  "ausentes": [],
  "action_items": [{"responsable": "", "tarea": "", "fecha_limite": ""}],
  "fechas_clave": [{"fecha": "", "evento": ""}],
  "decisiones": []
}


## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (¡muy bueno!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 personas\n   - JP hace JD para el lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix bug webhook para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn y GetOnBoard",
  "fecha_reunion": "2026-04-14",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {"responsable": "Seba", "tarea": "Corregir bug de webhooks (bug crítico en API, tomado por Seba)", "fecha_limite": "2026-04-16"},
    {"responsable": "MaJo", "tarea": "Actualizar roadmap en Notion", "fecha_limite": ""},
    {"responsable": "Cami", "tarea": "Preparar demo para cliente Falabella", "fecha_limite": "2026-04-23"},
    {"responsable": "JP", "tarea": "Publicar JDs (descripciones de puesto) en LinkedIn y GetOnBoard", "fecha_limite": "2026-04-20"}
  ],
  "fechas_clave": [
    {"fecha": "2026-04-14", "evento": "Reunión de equipo de producto"},
    {"fecha": "2026-04-16", "evento": "Fecha límite para corregir bug de webhooks (Seba)"},
    {"fecha": "2026-04-20", "evento": "Lunes: JP debe tener lista la JD para contratación y publicarla"},
    {"fecha": "2026-04-21", "evento": "Próxima reunión de equipo (10:00)"},
    {"fecha": "2026-04-23", "evento": "Demo para cliente Falabella (Cami)"},
    {"fecha": "2026-04-28", "evento": "Fecha original de lanzamiento v2.0 (movida)"},
    {"fecha": "2026-05-05", "evento": "Nueva fecha de lanzamiento v2.0"}
  ],
  "decisiones": [
    "Mover el lanzamiento de v2.0 del 28 de abril al 5 de mayo",
    "Contratar 2 desarrolladores senior y 1 QA",
    "Aprobar presupuesto de $8M CLP/mes para 3 personas",
    "Falta QA en el módulo de pagos antes del lanzamiento (pendiente de resolver)"
  ]
}
```

**Notas:**
- Asumí que "JP hace JD p/ lunes" se refiere al lunes 20/04, anterior a la reunión del 21/04. Si el plazo era otro, corrígelo.
- El action item de MaJo no tiene fecha límite en las notas, así que quedó vacío.
- Asumí que "Reunlon equlpo prod" corresponde a "Reunión equipo prod" y que "GetOnBrd" es "GetOnBoard" (plataforma de empleo).
- Las métricas y el presupuesto son propios del texto original; no los verifiqué contra otras fuentes.