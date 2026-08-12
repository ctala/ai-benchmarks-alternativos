# Inkling Small — ocr_extraction/handwritten_notes_extraction

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 8.47 | quality: 10.0
- latency_total: 92.856s | tokens_per_second: 67.8
- input_tokens: 444 | output_tokens: 6293

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
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abril 28 a mayo 5\n   - Falta QA en módulo pagos\n   - Bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - Churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (¡re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - Presupuesto aprobado: $8M CLP/mes x 3 pax\n   - JP hace JD para lunes\n\n4) Próx reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "14/04/26",
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
      "fecha_limite": "16/04"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "Prep demo para cliente Falabella",
      "fecha_limite": "23/04"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar JDs en LinkedIn + GetOnBrd",
      "fecha_limite": ""
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/26",
      "evento": "Reunión equipo prod"
    },
    {
      "fecha": "16/04",
      "evento": "Deadline fix webhook bug (Seba)"
    },
    {
      "fecha": "21/04",
      "evento": "Próxima reunión 10am / JP entrega JD"
    },
    {
      "fecha": "23/04",
      "evento": "Demo cliente Falabella (prep Cami)"
    },
    {
      "fecha": "28/04",
      "evento": "Fecha original lanzamiento v2.0 (movida)"
    },
    {
      "fecha": "05/05",
      "evento": "Nuevo lanzamiento v2.0"
    }
  ],
  "decisiones": [
    "Postergar lanzamiento v2.0 de 28/04 a 05/05 por falta de QA en módulo pagos y bug crítico en webhooks",
    "Aprobar presupuesto de $8M CLP/mes para contratar 2 desarrolladores senior + 1 QA",
    "JP debe elaborar las Job Descriptions (JD) para el lunes 21/04"
  ]
}
```