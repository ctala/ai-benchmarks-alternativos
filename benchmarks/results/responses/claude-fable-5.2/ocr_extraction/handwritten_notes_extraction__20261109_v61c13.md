# Claude Fable 5.2 — ocr_extraction/handwritten_notes_extraction

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 8.06 | quality: 10.0
- latency_total: 30.587s | tokens_per_second: 111.5
- input_tokens: 674 | output_tokens: 3412

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
  "texto_corregido": "Reunión equipo producto - 14/04/26\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover del 28 de abril al 5 de mayo\n   - Falta QA en módulo de pagos\n   - Bug crítico en API de webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - Churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (¡¡re bueno!!)\n\n3) Contratar 2 devs senior + 1 QA\n   - Presupuesto aprobado: $8M CLP/mes x 3 personas\n   - JP hace job description para el lunes\n\n4) Próxima reunión: lunes 21/04, 10:00 am\n\nAction items:\n- Seba: fix del bug de webhooks para el miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar job descriptions en LinkedIn + Get on Board",
  "fecha_reunion": "2026-04-14",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Corregir el bug crítico en la API de webhooks",
      "fecha_limite": "2026-04-16"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar el roadmap en Notion",
      "fecha_limite": null
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para el cliente Falabella (la demo es el 23/04)",
      "fecha_limite": "2026-04-23"
    },
    {
      "responsable": "JP",
      "tarea": "Redactar las job descriptions (2 devs senior + 1 QA)",
      "fecha_limite": "2026-04-21"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar las job descriptions en LinkedIn y Get on Board",
      "fecha_limite": null
    }
  ],
  "fechas_clave": [
    { "fecha": "2026-04-14", "evento": "Reunión del equipo de producto" },
    { "fecha": "2026-04-16", "evento": "Fecha límite: fix del bug de webhooks (Seba)" },
    { "fecha": "2026-04-21", "evento": "Próxima reunión (10:00 am) y entrega de las job descriptions (JP)" },
    { "fecha": "2026-04-23", "evento": "Demo para el cliente Falabella (Cami)" },
    { "fecha": "2026-04-28", "evento": "Fecha original del lanzamiento v2.0 (descartada)" },
    { "fecha": "2026-05-05", "evento": "Nueva fecha del lanzamiento v2.0" }
  ],
  "decisiones": [
    "Postergar el lanzamiento de v2.0 del 28 de abril al 5 de mayo, porque falta QA en el módulo de pagos y hay un bug crítico en la API de webhooks",
    "Seba se hace cargo del bug crítico de webhooks",
    "Contratar 2 desarrolladores senior y 1 QA, con presupuesto aprobado de $8M CLP/mes x 3 personas",
    "Próxima reunión: lunes 21/04 a las 10:00 am"
  ],
  "observaciones": [
    "Posible error en el año: en 2026 el 16/04 cae jueves y el 21/04 cae martes, no miércoles y lunes como dicen las notas. Los días calzan con 2025, así que el '26' podría ser un '25' mal reconocido; conviene verificarlo en el original. Mantuve 2026 en todas las fechas.",
    "Interpreté 'prod' como 'producto' (por el roadmap y las métricas), aunque podría ser 'producción'.",
    "'$8M CLP/mes x 3 pax' es ambiguo: no queda claro si son $8M en total o por persona.",
    "Interpreté 'p/ lunes' (job descriptions de JP) como el lunes 21/04, día de la próxima reunión.",
    "Agregué el campo 'observaciones' fuera del esquema pedido para dejar constancia de estas dudas."
  ]
}
```