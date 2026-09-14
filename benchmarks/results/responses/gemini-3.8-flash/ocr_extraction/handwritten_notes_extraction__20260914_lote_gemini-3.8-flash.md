# Gemini 3.8 Flash — ocr_extraction/handwritten_notes_extraction

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.61 | quality: 10.0
- latency_total: 14.005s | tokens_per_second: 149.1
- input_tokens: 458 | output_tokens: 2088

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
  "texto_corregido": "Reunión equipo producto - 14/04/26\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abril 28 a mayo 5\n   - Falta QA en módulo pagos\n   - Bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR: $52.1k (+15% vs Q4)\n   - Churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (¡re bueno!)\n\n3) Contratar 2 devs senior + 1 QA\n   - Presupuesto aprobado: $8M CLP/mes por 3 personas\n   - JP hace Job Description para el lunes\n\n4) Próxima reunión: lunes 21/04 a las 10:00 am\n\nAction items:\n- Seba: Arreglar bug de webhook para miércoles 16/04\n- MaJo: Actualizar roadmap en Notion\n- Cami: Preparar demo para cliente Falabella (23/04)\n- JP: Publicar Job Descriptions en LinkedIn + Get on Board",
  "fecha_reunion": "14/04/2026",
  "asistentes": [
    "JP",
    "MaJo",
    "Seba",
    "Cami"
  ],
  "ausentes": [
    "Nico"
  ],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Corregir bug crítico en API de webhooks",
      "fecha_limite": "16/04/2026"
    },
    {
      "responsable": "JP",
      "tarea": "Redactar Job Descriptions (JD) y publicarlas en LinkedIn y Get on Board",
      "fecha_limite": "21/04/2026"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": "Sin fecha explícita"
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "23/04/2026"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/2026",
      "evento": "Reunión de equipo de producto"
    },
    {
      "fecha": "16/04/2026",
      "evento": "Entrega de corrección de bug en API webhooks (Seba)"
    },
    {
      "fecha": "21/04/2026",
      "evento": "Próxima reunión de equipo (10:00 am) y entrega de JDs (JP)"
    },
    {
      "fecha": "23/04/2026",
      "evento": "Demo para cliente Falabella"
    },
    {
      "fecha": "28/04/2026",
      "evento": "Fecha original de lanzamiento v2.0 (cancelada)"
    },
    {
      "fecha": "05/05/2026",
      "evento": "Nueva fecha programada para lanzamiento v2.0"
    }
  ],
  "decisiones": [
    "Postergar el lanzamiento de v2.0 del 28 de abril al 5 de mayo debido a QA pendiente en módulo de pagos y bug crítico en API de webhooks.",
    "Aprobar presupuesto de $8.000.000 CLP mensuales para la contratación de 3 vacantes: 2 desarrolladores Senior y 1 QA."
  ]
}
```