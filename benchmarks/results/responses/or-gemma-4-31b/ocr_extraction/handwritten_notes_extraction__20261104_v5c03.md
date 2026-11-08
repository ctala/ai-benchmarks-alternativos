# Gemma 4 31B — ocr_extraction/handwritten_notes_extraction

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 9.17 | quality: 10.0
- latency_total: 9.736s | tokens_per_second: 85.9
- input_tokens: 476 | output_tokens: 836

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
  "texto_corregido": "Reunión equipo producto - 14/04/26\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0: mover del 28 de abril al 5 de mayo\n   - Falta QA en módulo de pagos\n   - Bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR: 52.1k (+15% vs Q4)\n   - Churn: bajó a 3.1% (objetivo era 3.5%)\n   - NPS: subió a 51 (excelente)\n\n3) Contratar 2 desarrolladores Senior + 1 QA\n   - Presupuesto aprobado: $8M CLP/mes por persona\n   - JP redacta la descripción del cargo (JD) para el lunes\n\n4) Próxima reunión: lunes 21/04 a las 10:00 am\n\nAction items:\n- Seba: corregir bug de webhook para el miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar descripciones de cargo (JDs) en LinkedIn y GetOnBoard",
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
      "tarea": "Corregir bug de API webhooks",
      "fecha_limite": "2026-04-16"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": "No especificada"
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "2026-04-23"
    },
    {
      "responsable": "JP",
      "tarea": "Redactar y publicar JDs en LinkedIn y GetOnBoard",
      "fecha_limite": "2026-04-20"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "2026-04-16",
      "evento": "Fecha límite para fix de webhook (Seba)"
    },
    {
      "fecha": "2026-04-21",
      "evento": "Próxima reunión de equipo (10:00 am)"
    },
    {
      "fecha": "2026-04-23",
      "evento": "Demo cliente Falabella"
    },
    {
      "fecha": "2026-05-05",
      "evento": "Nueva fecha de lanzamiento v2.0"
    }
  ],
  "decisiones": [
    "Reprogramación del lanzamiento v2.0 del 28 de abril al 5 de mayo",
    "Aprobación de presupuesto de $8M CLP mensuales por persona para la contratación de 2 Devs Sr y 1 QA"
  ]
}
```