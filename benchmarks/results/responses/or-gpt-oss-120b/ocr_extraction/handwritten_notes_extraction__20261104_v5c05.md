# GPT-OSS 120B — ocr_extraction/handwritten_notes_extraction

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 8.9 | quality: 10.0
- latency_total: 64.614s | tokens_per_second: 34.1
- input_tokens: 488 | output_tokens: 2201

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
  "texto_corregido": "Reunión equipo prod - 14/04/2024\nAsistentes: JP, MaJo, Seba, Cami (ausente: Nico)\n\n1) Lanzamiento v2.0 - mover de 28 abr a 5 may\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (¡re bueno!)\n\n3) Contratar 2 devs senior + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 pax\n   - JP hará JD para el lunes\n\n4) Próxima reunión: lun 21/04 10 am\n\nAction items:\n- Seba: fix webhook bug para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBoard",
  "fecha_reunion": "2024-04-14",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Fix webhook bug",
      "fecha_limite": "2024-04-16"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "2024-04-23"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar JDs en LinkedIn y GetOnBoard",
      "fecha_limite": ""
    }
  ],
  "fechas_clave": [
    {
      "fecha": "2024-04-14",
      "evento": "Reunión del equipo de producto"
    },
    {
      "fecha": "2024-04-28",
      "evento": "Fecha original de lanzamiento v2.0 (reprogramada)"
    },
    {
      "fecha": "2024-05-05",
      "evento": "Nueva fecha de lanzamiento v2.0"
    },
    {
      "fecha": "2024-04-16",
      "evento": "Fecha límite para corregir bug de webhook (Seba)"
    },
    {
      "fecha": "2024-04-21",
      "evento": "Próxima reunión del equipo (lunes 10 am)"
    },
    {
      "fecha": "2024-04-23",
      "evento": "Demo para cliente Falabella (Cami)"
    }
  ],
  "decisiones": [
    "Se movió la fecha de lanzamiento v2.0 del 28/04 al 05/05.",
    "Se identificó la necesidad de QA en el módulo de pagos.",
    "Se acordó contratar 2 desarrolladores senior y 1 QA con presupuesto aprobado de $8 M CLP/mes para 3 personas.",
    "JP se encargará de crear la descripción del puesto (JD) para el lunes siguiente a la reunión.",
    "Se publicarán los JD en LinkedIn y en la plataforma GetOnBoard."
  ]
}
```