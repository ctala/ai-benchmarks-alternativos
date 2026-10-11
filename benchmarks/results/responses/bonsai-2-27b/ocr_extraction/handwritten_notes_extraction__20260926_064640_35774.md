# Bonsai 2 27B — ocr_extraction/handwritten_notes_extraction

- model_id: `prism-ml/ternary-bonsai-2-27b`
- success: True  | final: 8.39 | quality: 10.0
- latency_total: 273.093s | tokens_per_second: 40.2
- input_tokens: 518 | output_tokens: 10974

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
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de 28/04/26 a 05/05/26\n   - Falta QA en módulo pagos\n   - Bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - Churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (¡re bueno!!)\n\n3) Contratar 2 desarrolladores senior + 1 QA\n   - Presupuesto aprobado: $8M CLP/mes x 3 personas\n   - JP hace descripción de puesto para lunes\n\n4) Próxima reunión: lunes 21/04/26 10am\n\nAction items:\n- Seba: fix webhook bug para miércoles 16/04/26\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04/26)\n- JP: publicar descripciones de puesto en LinkedIn + GetOnBoard",
  "fecha_reunion": "2026-04-14",
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
      "tarea": "Fix webhook bug",
      "fecha_limite": "2026-04-16"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "2026-04-23"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar descripciones de puesto en LinkedIn + GetOnBoard",
      "fecha_limite": ""
    },
    {
      "responsable": "JP",
      "tarea": "Hacer descripción de puesto",
      "fecha_limite": "lunes"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "2026-04-14",
      "evento": "Reunión equipo prod"
    },
    {
      "fecha": "2026-04-16",
      "evento": "Fix webhook bug por Seba"
    },
    {
      "fecha": "2026-04-21",
      "evento": "Próxima reunión"
    },
    {
      "fecha": "2026-04-23",
      "evento": "Demo para cliente Falabella por Cami"
    },
    {
      "fecha": "2026-04-28",
      "evento": "Fecha original de lanzamiento v2.0"
    },
    {
      "fecha": "2026-05-05",
      "evento": "Nueva fecha de lanzamiento v2.0"
    },
    {
      "fecha": "lunes",
      "evento": "JP hace descripción de puesto"
    }
  ],
  "decisiones": [
    "Reprogramar el lanzamiento de v2.0 del 28/04/26 al 05/05/26",
    "Contratar 2 desarrolladores senior y 1 QA",
    "Aprobar presupuesto de $8M CLP/mes para 3 personas",
    "Definir próxima reunión el 21/04/26 a las 10am"
  ]
}