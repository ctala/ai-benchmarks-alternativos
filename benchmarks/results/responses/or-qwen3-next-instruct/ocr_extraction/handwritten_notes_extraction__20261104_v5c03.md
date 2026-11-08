# Qwen 3-Next 80B Instruct — ocr_extraction/handwritten_notes_extraction

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 9.26 | quality: 10.0
- latency_total: 3.664s | tokens_per_second: 226.3
- input_tokens: 479 | output_tokens: 829

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
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR $52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (muy bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 pax\n   - JP hace JD para lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBoard",
  "fecha_reunion": "2026-04-14",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "fix webhook bug",
      "fecha_limite": "2026-04-16"
    },
    {
      "responsable": "MaJo",
      "tarea": "actualizar roadmap en Notion",
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "preparar demo para cliente Falabella",
      "fecha_limite": "2026-04-23"
    },
    {
      "responsable": "JP",
      "tarea": "publicar JDs en LinkedIn + GetOnBoard",
      "fecha_limite": "2026-04-21"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "2026-04-14",
      "evento": "Reunión del equipo de producto"
    },
    {
      "fecha": "2026-04-16",
      "evento": "Corrección del bug de webhooks por Seba"
    },
    {
      "fecha": "2026-04-21",
      "evento": "Próxima reunión del equipo"
    },
    {
      "fecha": "2026-04-23",
      "evento": "Demo para cliente Falabella"
    },
    {
      "fecha": "2026-05-05",
      "evento": "Lanzamiento v2.0 (nueva fecha)"
    }
  ],
  "decisiones": [
    "Mover el lanzamiento de v2.0 del 28 de abril al 5 de mayo",
    "Contratar 2 desarrolladores seniors y 1 QA con presupuesto aprobado de $8M CLP/mes",
    "JP se encarga de generar los JDs para el lunes",
    "Seba asume la responsabilidad del bug crítico en webhooks",
    "Se logró superar el objetivo de churn (3.1% vs 3.5%) y NPS mejoró significativamente (51)"
  ]
}