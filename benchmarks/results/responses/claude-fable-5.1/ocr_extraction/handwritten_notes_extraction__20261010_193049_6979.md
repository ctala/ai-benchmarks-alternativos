# Claude Fable 5.1 — ocr_extraction/handwritten_notes_extraction

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 7.93 | quality: 10.0
- latency_total: 26.999s | tokens_per_second: 87.1
- input_tokens: 674 | output_tokens: 2352

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
  "texto_corregido": "Reunión equipo producto - 14/04/26\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abril 28 a mayo 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (¡muy bueno!)\n\n3) Contratar 2 desarrolladores senior + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 personas\n   - JP hace job description para el lunes\n\n4) Próxima reunión: lunes 21/04 10:00 am\n\nAction items:\n- Seba: fix webhook bug para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "2026-04-14",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Corregir bug crítico en API de webhooks",
      "fecha_limite": "2026-04-16"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion (reflejar nueva fecha de lanzamiento v2.0)",
      "fecha_limite": "No especificada"
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "2026-04-23"
    },
    {
      "responsable": "JP",
      "tarea": "Redactar job descriptions (2 devs senior + 1 QA) y publicarlas en LinkedIn y GetOnBrd",
      "fecha_limite": "2026-04-20 (lunes)"
    }
  ],
  "fechas_clave": [
    {"fecha": "2026-04-14", "evento": "Reunión equipo producto"},
    {"fecha": "2026-04-16", "evento": "Deadline fix bug webhooks (Seba)"},
    {"fecha": "2026-04-20", "evento": "JP entrega job descriptions ('para el lunes')"},
    {"fecha": "2026-04-21", "evento": "Próxima reunión de equipo, 10:00 am"},
    {"fecha": "2026-04-23", "evento": "Demo para cliente Falabella (Cami)"},
    {"fecha": "2026-04-28", "evento": "Fecha original de lanzamiento v2.0 (descartada)"},
    {"fecha": "2026-05-05", "evento": "Nueva fecha de lanzamiento v2.0"}
  ],
  "decisiones": [
    "Posponer el lanzamiento de v2.0 del 28 de abril al 5 de mayo por falta de QA en módulo de pagos y bug crítico en webhooks",
    "Seba asume la corrección del bug crítico en la API de webhooks",
    "Contratar 2 desarrolladores senior y 1 QA, con presupuesto aprobado de $8M CLP/mes para las 3 posiciones",
    "JP es responsable de redactar y publicar las job descriptions",
    "Próxima reunión fijada para el 21/04 a las 10:00 am"
  ],
  "observaciones": [
    "Inconsistencia de calendario: en 2026 el 14/04 es martes, por lo que el 16/04 es jueves (no miércoles) y el 21/04 es martes (no lunes). Es posible que el autor se haya equivocado en el día de la semana o que el OCR haya leído mal los dígitos (ej. 15/04 y 20/04). Conviene confirmar estas fechas.",
    "El deadline de JP para las JDs ('para el lunes') se interpretó como el lunes siguiente a la reunión, 20/04.",
    "El año '26' se interpretó como 2026.",
    "MaJo no tiene fecha límite explícita para actualizar el roadmap; se sugiere hacerlo antes de la próxima reunión."
  ]
}
```