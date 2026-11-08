# GPT-6 Astra — ocr_extraction/handwritten_notes_extraction

- model_id: `openai/gpt-6-astra`
- success: True  | final: 8.03 | quality: 10.0
- latency_total: 19.698s | tokens_per_second: 71.7
- input_tokens: 437 | output_tokens: 1413

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

{
  "texto_corregido": "Reunión del equipo de producto — 14/04/2026\nAsistentes: JP, MaJo, Seba y Cami. Ausente: Nico.\n\n1) Lanzamiento de la versión 2.0: mover del 28 de abril al 5 de mayo.\n- Falta realizar el aseguramiento de calidad (QA) del módulo de pagos.\n- Hay un error crítico en la API de webhooks. Seba se encargará.\n\n2) Métricas del primer trimestre (Q1):\n- Ingresos recurrentes mensuales (MRR): 52,1 mil (+15 % respecto al cuarto trimestre, Q4). Moneda no indicada.\n- La tasa de cancelación (churn) bajó al 3,1 %; el objetivo era el 3,5 %.\n- El índice de recomendación neta (NPS) subió a 51. ¡Muy bueno!\n\n3) Contratar a 2 desarrolladores sénior y 1 especialista en QA.\n- Presupuesto aprobado: 8 millones de pesos chilenos (CLP) al mes × 3 personas. No queda claro si el importe es total o por persona.\n- JP redactará las descripciones de los puestos (JD) para el lunes.\n\n4) Próxima reunión: 21/04 a las 10:00, anotada como lunes.\n\nAcciones pendientes:\n- Seba: corregir el error de webhooks para el 16/04, anotado como miércoles.\n- MaJo: actualizar la hoja de ruta en Notion.\n- Cami: preparar la demostración para el cliente Falabella del 23/04.\n- JP: publicar las descripciones de los puestos en LinkedIn y Get on Board.\n\nNota sobre las fechas: se toma 2026 como año de referencia. El 16/04/2026 es jueves y el 21/04/2026 es martes, por lo que los días de la semana anotados no coinciden. Se conservan las fechas numéricas; es necesario confirmarlas. El lunes indicado para las descripciones de puestos no tiene una fecha numérica explícita.",
  "fecha_reunion": "2026-04-14",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Corregir el error crítico en la API de webhooks. Confirmar el plazo: la nota indica miércoles, pero el 16/04/2026 es jueves.",
      "fecha_limite": "2026-04-16"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar la hoja de ruta en Notion.",
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar la demostración para Falabella prevista para el 23/04.",
      "fecha_limite": "2026-04-23"
    },
    {
      "responsable": "JP",
      "tarea": "Redactar las descripciones de los puestos para el lunes; fecha exacta por confirmar.",
      "fecha_limite": ""
    },
    {
      "responsable": "JP",
      "tarea": "Publicar las descripciones de los puestos en LinkedIn y Get on Board.",
      "fecha_limite": ""
    },
    {
      "responsable": "",
      "tarea": "Completar el aseguramiento de calidad del módulo de pagos, pendiente para el lanzamiento. Responsable y plazo no especificados.",
      "fecha_limite": ""
    }
  ],
  "fechas_clave": [
    {
      "fecha": "2026-04-14",
      "evento": "Reunión del equipo de producto."
    },
    {
      "fecha": "2026-04-16",
      "evento": "Plazo anotado para corregir el error de webhooks. Hay discrepancia con el día de la semana indicado."
    },
    {
      "fecha": "2026-04-21T10:00:00",
      "evento": "Próxima reunión. Hay discrepancia con el día de la semana indicado; zona horaria no especificada."
    },
    {
      "fecha": "2026-04-23",
      "evento": "Demostración para Falabella."
    },
    {
      "fecha": "2026-04-28",
      "evento": "Fecha original del lanzamiento de la versión 2.0, sustituida por el 5 de mayo."
    },
    {
      "fecha": "2026-05-05",
      "evento": "Nueva fecha del lanzamiento de la versión 2.0."
    }
  ],
  "decisiones": [
    "Posponer el lanzamiento de la versión 2.0 del 28 de abril al 5 de mayo.",
    "Asignar a Seba la corrección del error crítico en la API de webhooks.",
    "Contratar a 2 desarrolladores sénior y 1 especialista en QA.",
    "Aprobar el presupuesto de contratación anotado como 8 millones de CLP al mes × 3 personas; confirmar si el importe es total o individual."
  ]
}