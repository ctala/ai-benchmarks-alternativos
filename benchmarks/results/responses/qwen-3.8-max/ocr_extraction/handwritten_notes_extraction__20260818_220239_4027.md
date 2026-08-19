# Qwen 3.8 Max — ocr_extraction/handwritten_notes_extraction

- model_id: `qwen/qwen3.8-max`
- success: True  | final: 8.15 | quality: 10.0
- latency_total: 126.331s | tokens_per_second: 51.8
- input_tokens: 518 | output_tokens: 6542

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
  "texto_corregido": "Reunión equipo de producto - 14/04/25\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0: mover del 28/04 al 05/05\n   - Falta QA en módulo de pagos\n   - Bug crítico en API de webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - Churn bajó a 3.1% (el objetivo era 3.5%)\n   - NPS subió a 51 (¡muy bueno!)\n\n3) Contratar 2 desarrolladores senior + 1 QA\n   - Presupuesto aprobado: $8M CLP/mes por 3 personas\n   - JP prepara descripciones de cargo (JD) para el lunes\n\n4) Próxima reunión: lunes 21/04 10:00\n\nAction items:\n- Seba: corregir bug de webhooks para el miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBoard",
  "fecha_reunion": "2025-04-14",
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
      "fecha_limite": "2025-04-16"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "2025-04-23"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar JDs en LinkedIn y GetOnBoard",
      "fecha_limite": "2025-04-21"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "2025-04-14",
      "evento": "Reunión de equipo de producto"
    },
    {
      "fecha": "2025-04-16",
      "evento": "Fecha límite: Seba corrige bug crítico de webhooks"
    },
    {
      "fecha": "2025-04-21",
      "evento": "Próxima reunión (10:00) y fecha límite para que JP prepare/publique JDs"
    },
    {
      "fecha": "2025-04-23",
      "evento": "Demo de Cami para cliente Falabella"
    },
    {
      "fecha": "2025-04-28",
      "evento": "Fecha original de lanzamiento v2.0"
    },
    {
      "fecha": "2025-05-05",
      "evento": "Nueva fecha de lanzamiento v2.0"
    }
  ],
  "decisiones": [
    "Mover el lanzamiento v2.0 del 28/04 al 05/05",
    "Contratar 2 desarrolladores senior y 1 QA",
    "Aprobar presupuesto de $8M CLP/mes para 3 personas",
    "Asignar a Seba la corrección del bug crítico de webhooks",
    "Programar próxima reunión para el lunes 21/04 a las 10:00"
  ]
}