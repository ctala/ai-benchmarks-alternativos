# DeepSeek V4 Pro (0813) — ocr_extraction/handwritten_notes_extraction

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 8.58 | quality: 10.0
- latency_total: 40.273s | tokens_per_second: 117.8
- input_tokens: 472 | output_tokens: 4743

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
  "texto_corregido": "Reunión equipo prod - 14/04/2025\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de 28/04 a 05/05\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (¡muy bueno!)\n\n3) Contratar 2 devs senior + 1 QA\n   - presupuesto aprobado: $8M CLP/mes por 3 personas\n   - JP hace JD para el lunes\n\n4) Próxima reunión: lunes 21/04 10 am\n\nAction items:\n- Seba: corregir bug de webhook para el miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBoard",
  "fecha_reunion": "14/04/2025",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Corregir bug de webhook",
      "fecha_limite": "16/04/2025"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": null
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "23/04/2025"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar JDs en LinkedIn y GetOnBoard",
      "fecha_limite": null
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/2025",
      "evento": "Reunión de equipo prod"
    },
    {
      "fecha": "16/04/2025",
      "evento": "Fecha límite para que Seba corrija bug de webhook"
    },
    {
      "fecha": "21/04/2025",
      "evento": "Próxima reunión (10 am) y fecha para que JP haga las JD"
    },
    {
      "fecha": "23/04/2025",
      "evento": "Demo para cliente Falabella"
    },
    {
      "fecha": "28/04/2025",
      "evento": "Fecha original de lanzamiento v2.0 (se mueve)"
    },
    {
      "fecha": "05/05/2025",
      "evento": "Nueva fecha de lanzamiento v2.0"
    }
  ],
  "decisiones": [
    "Mover el lanzamiento v2.0 del 28/04 al 05/05",
    "Contratar 2 developers senior y 1 QA con presupuesto aprobado de $8M CLP/mes por 3 personas",
    "JP preparará las descripciones de puesto (JD) para el lunes 21/04",
    "Próxima reunión el lunes 21/04 a las 10 am"
  ]
}