# Ministral 14B — ocr_extraction/handwritten_notes_extraction

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 8.97 | quality: 10.0
- latency_total: 25.536s | tokens_per_second: 37.3
- input_tokens: 468 | output_tokens: 953

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
  "texto_corregido": "
  **Reunión equipo producto - 14/04/2026**
  Asistentes: JP, MaJo, Seba, Cami
  Ausente: Nico

  **1) Lanzamiento v2.0**
  - Postergar fecha de lanzamiento de **abril 28 a mayo 5**
  - Pendiente: QA en módulo pagos
  - Bug crítico en API webhooks (Seba se hace cargo)

  **2) Métricas Q1**
  - MRR: $52.1k (+15% vs Q4)
  - Churn: 3.1% (objetivo era 3.5%)
  - NPS: 51 (¡muy bueno!)

  **3) Contrataciones**
  - Contratar: 2 devs senior + 1 QA
  - Presupuesto aprobado: **$8M CLP/mes x 3 personas**
  - JP elaborará las JD (Job Descriptions) para lunes

  **4) Próxima reunión**
  - Lunes 21/04 a las 10:00 AM",

  "fecha_reunion": "14/04/2026",

  "asistentes": ["JP", "MaJo", "Seba", "Cami"],

  "ausentes": ["Nico"],

  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Resolver el bug en API webhooks",
      "fecha_limite": "miércoles 16/04/2026"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": "No especificada (prioridad alta)"
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "23/04/2026"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar las JD en LinkedIn y GetOnBoard",
      "fecha_limite": "No especificada (prioridad alta)"
    }
  ],

  "fechas_clave": [
    {
      "fecha": "28/04/2026",
      "evento": "Fecha original de lanzamiento v2.0 (postergado)"
    },
    {
      "fecha": "05/05/2026",
      "evento": "Nueva fecha de lanzamiento v2.0"
    },
    {
      "fecha": "16/04/2026",
      "evento": "Fecha límite para resolver bug de webhooks"
    },
    {
      "fecha": "21/04/2026",
      "evento": "Próxima reunión a las 10:00 AM"
    },
    {
      "fecha": "23/04/2026",
      "evento": "Demo para cliente Falabella"
    },
    {
      "fecha": "15/04/2026 (lunes)",
      "evento": "Entrega de JD elaboradas por JP"
    }
  ],

  "decisiones": [
    {
      "punto": "Lanzamiento v2.0",
      "detalle": "Postergación de la fecha de lanzamiento de abril 28 a mayo 5 por pendientes en QA y bug crítico en API webhooks."
    },
    {
      "punto": "Contrataciones",
      "detalle": "Aprobación de presupuesto para contratar 2 desarrolladores senior y 1 QA, con un costo de $8M CLP/mes por persona."
    },
    {
      "punto": "Métricas Q1",
      "detalle": "Reconocimiento positivo por cumplimiento de objetivos de MRR, churn y NPS."
    },
    {
      "punto": "Próxima reunión",
      "detalle": "Confirmación de reunión el lunes 21/04 a las 10:00 AM."
    }
  ]
}
```