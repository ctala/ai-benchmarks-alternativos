# Gemini 3.1 Pro — ocr_extraction/handwritten_notes_extraction

- model_id: `google/gemini-3.1-pro-preview`
- success: True  | final: 8.29 | quality: 10.0
- latency_total: 31.55s | tokens_per_second: 112.7
- input_tokens: 458 | output_tokens: 3557

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
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (¡re bueno!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 pax\n   - JP hace JD para el lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para miérc 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBoard",
  "fecha_reunion": "14/04/2026",
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
      "tarea": "Arreglar bug crítico en API webhooks",
      "fecha_limite": "16/04/2026"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": "No especificada"
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para el cliente Falabella",
      "fecha_limite": "23/04/2026"
    },
    {
      "responsable": "JP",
      "tarea": "Crear Job Descriptions (JD) y publicarlas en LinkedIn y GetOnBoard",
      "fecha_limite": "21/04/2026"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/2026",
      "evento": "Reunión del equipo de producto"
    },
    {
      "fecha": "16/04/2026",
      "evento": "Fecha límite para arreglar el bug de webhooks"
    },
    {
      "fecha": "21/04/2026",
      "evento": "Próxima reunión de equipo (10:00 am) y fecha límite para redactar las JDs"
    },
    {
      "fecha": "23/04/2026",
      "evento": "Demo programada para el cliente Falabella"
    },
    {
      "fecha": "28/04/2026",
      "evento": "Fecha original de lanzamiento de la v2.0 (Cancelada/Pospuesta)"
    },
    {
      "fecha": "05/05/2026",
      "evento": "Nueva fecha de lanzamiento de la v2.0"
    }
  ],
  "decisiones": [
    "Posponer el lanzamiento de la versión 2.0 del 28 de abril al 5 de mayo debido a la falta de QA en el módulo de pagos y un bug crítico.",
    "Aprobar la contratación de 2 Desarrolladores Senior y 1 QA con un presupuesto total de $8.000.000 CLP mensuales por las 3 personas."
  ]
}
```