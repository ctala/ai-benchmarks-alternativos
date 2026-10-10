# Claude Haiku 5.5 — ocr_extraction/handwritten_notes_extraction

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.92 | quality: 10.0
- latency_total: 13.322s | tokens_per_second: 243.1
- input_tokens: 674 | output_tokens: 3238

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
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (muy bueno)\n\n3) Contratar 2 devs senior + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 personas\n   - JP hace JD para el lunes\n\n4) Próxima reunión: lunes 21/04, 10:00\n\nAction items:\n- Seba: corregir bug de webhooks para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn y GetOnBrd",
  "fecha_reunion": "14/04/2026",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Corregir el bug crítico de la API de webhooks",
      "fecha_limite": "16/04/2026 (miércoles)"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar el roadmap en Notion",
      "fecha_limite": "No especificada"
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar la demo para el cliente Falabella",
      "fecha_limite": "23/04/2026"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar las JDs en LinkedIn y GetOnBrd",
      "fecha_limite": "No especificada"
    },
    {
      "responsable": "JP",
      "tarea": "Redactar las descripciones de puesto (JD) para contratar 2 devs senior + 1 QA",
      "fecha_limite": "21/04/2026 (lunes, inferido de 'p/ lunes')"
    }
  ],
  "fechas_clave": [
    {"fecha": "14/04/2026", "evento": "Reunión de equipo de producto"},
    {"fecha": "16/04/2026", "evento": "Fecha límite para corregir el bug de webhooks (Seba)"},
    {"fecha": "21/04/2026", "evento": "Próxima reunión (10:00) y fecha límite para la JD"},
    {"fecha": "23/04/2026", "evento": "Demo para el cliente Falabella (Cami)"},
    {"fecha": "28/04/2026", "evento": "Fecha original de lanzamiento v2.0 (será movida)"},
    {"fecha": "05/05/2026", "evento": "Nueva fecha de lanzamiento v2.0"}
  ],
  "decisiones": [
    "Mover el lanzamiento v2.0 del 28/04 al 05/05",
    "Seba toma el bug crítico de la API de webhooks",
    "Aprobar el presupuesto para contratar 2 devs senior + 1 QA ($8M CLP/mes x 3 personas)",
    "JP redacta y publica las JDs de contratación"
  ],
  "advertencias": [
    "Año ambiguo: la nota dice '14/04/26', pero los días de la semana indicados (lunes 21/04, miércoles 16/04) coinciden con 2025, no con 2026. Conviene confirmar el año.",
    "Presupuesto ambiguo: '$8M CLP/mes x 3 pax' puede significar $8M en total para las 3 contrataciones o $8M por persona. Confirmar antes de usar la cifra.",
    "Varias correcciones de OCR (por ejemplo 'prod' o 'Falabella') se mantuvieron tal cual porque no hay certeza de la forma original."
  ]
}
```