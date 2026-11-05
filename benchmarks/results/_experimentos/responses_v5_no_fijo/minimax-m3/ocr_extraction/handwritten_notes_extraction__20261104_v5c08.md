# MiniMax M3 — ocr_extraction/handwritten_notes_extraction

- model_id: `minimax/minimax-m3`
- success: True  | final: 9.04 | quality: 10.0
- latency_total: 7.777s | tokens_per_second: 124.6
- input_tokens: 589 | output_tokens: 969

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
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presup aprob: $8M CLP/mes x 3 pax\n   - JP hace JD p/ lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug p/ miérc 16/04\n- MaJo: actualzr roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "14/04/2026",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Fix bug crítico en API webhooks",
      "fecha_limite": "16/04/2026"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": "No especificada"
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "23/04/2026"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar JDs en LinkedIn + GetOnBrd",
      "fecha_limite": "20/04/2026 (lunes)"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/2026",
      "evento": "Reunión de equipo de producto"
    },
    {
      "fecha": "16/04/2026",
      "evento": "Fecha límite: fix de bug crítico en API webhooks (Seba)"
    },
    {
      "fecha": "20/04/2026",
      "evento": "Fecha límite: publicación de JDs por JP (lunes)"
    },
    {
      "fecha": "21/04/2026",
      "evento": "Próxima reunión de equipo (10am)"
    },
    {
      "fecha": "23/04/2026",
      "evento": "Demo para cliente Falabella (Cami)"
    },
    {
      "fecha": "05/05/2026",
      "evento": "Nueva fecha de lanzamiento v2.0 (movido desde 28/04)"
    }
  ],
  "decisiones": [
    "Mover lanzamiento v2.0 del 28 de abril al 5 de mayo",
    "Seba se hace cargo del bug crítico en API webhooks",
    "Aprobar presupuesto de $8M CLP/mes para contratar 2 devs sr + 1 QA",
    "JP elaborará las descripciones de cargo (JD) para el lunes 20/04",
    "Próxima reunión programada para el lunes 21/04 a las 10am"
  ],
  "notas_adicionales": {
    "cambios_lanzamiento": {
      "fecha_original": "28/04/2026",
      "fecha_nueva": "05/05/2026",
      "motivo": "Falta QA en módulo pagos + bug crítico en webhooks"
    },
    "metricas_q1": {
      "MRR": "52.1k (+15% vs Q4)",
      "churn": "3.1% (objetivo era 3.5%)",
      "NPS": "51"
    },
    "pendientes_lanzamiento": [
      "QA en módulo pagos",
      "Resolución bug crítico API webhooks"
    ]
  }
}
```