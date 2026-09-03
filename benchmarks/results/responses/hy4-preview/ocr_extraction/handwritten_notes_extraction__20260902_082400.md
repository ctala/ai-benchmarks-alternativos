# Tencent Hy4 preview — ocr_extraction/handwritten_notes_extraction

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.16 | quality: 10.0
- latency_total: 215.303s | tokens_per_second: 71.0
- input_tokens: 491 | output_tokens: 15276

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
  "texto_corregido": "Reunión equipo producto - 14/04/25\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover del 28 de abril al 5 de mayo\n   - Falta QA en módulo de pagos\n   - Bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - Churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 desarrolladores senior + 1 QA\n   - Presupuesto aprobado: $8M CLP/mes por 3 personas\n   - JP hace las descripciones de puesto (JDs) para el lunes (21/04)\n\n4) Próxima reunión: lunes 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para el miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBoard",
  "fecha_reunion": "14/04/25",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Corregir bug crítico en API webhooks (fix webhook bug)",
      "fecha_limite": "16/04/25"
    },
    {
      "responsable": "JP",
      "tarea": "Hacer las descripciones de puesto (JDs) para las contrataciones de 2 desarrolladores senior y 1 QA",
      "fecha_limite": "21/04/25"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "23/04/25"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar las descripciones de puesto (JDs) en LinkedIn y GetOnBoard",
      "fecha_limite": ""
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/25",
      "evento": "Reunión de equipo producto (asistentes: JP, MaJo, Seba, Cami; faltó Nico)"
    },
    {
      "fecha": "16/04/25",
      "evento": "Fecha límite: Seba corrige bug crítico en API webhooks (miércoles)"
    },
    {
      "fecha": "21/04/25",
      "evento": "Próxima reunión de equipo (lunes 21/04 a las 10am)"
    },
    {
      "fecha": "21/04/25",
      "evento": "Fecha límite: JP entrega las descripciones de puesto (JDs) listas (para el lunes)"
    },
    {
      "fecha": "23/04/25",
      "evento": "Cami prepara demo para cliente Falabella"
    },
    {
      "fecha": "28/04/25",
      "evento": "Fecha original de lanzamiento v2.0 (reprogramada)"
    },
    {
      "fecha": "05/05/25",
      "evento": "Nueva fecha de lanzamiento v2.0 (movida desde el 28/04)"
    }
  ],
  "decisiones": [
    "Reprogramar el lanzamiento de la v2.0: se mueve del 28 de abril al 5 de mayo debido a falta de QA en módulo de pagos y un bug crítico en API webhooks.",
    "Aprobar la contratación de 2 desarrolladores senior y 1 QA.",
    "Aprobar el presupuesto de $8M CLP/mes para 3 personas (2 desarrolladores senior + 1 QA).",
    "Asignar a Seba la corrección del bug crítico en la API de webhooks.",
    "JP será el responsable de realizar las descripciones de puesto (JDs) para el lunes 21/04."
  ]
}