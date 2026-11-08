# Tencent Hy4 preview — ocr_extraction/handwritten_notes_extraction

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.68 | quality: 10.0
- latency_total: 13.57s | tokens_per_second: 66.0
- input_tokens: 494 | output_tokens: 895

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
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (muy bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presupuesto aprobado: $8M CLP/mes por 3 personas\n   - JP hace JD para el lunes\n\n4) Próxima reunión: lunes 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para el miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
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
      "tarea": "Fix webhook bug (bug crítico en API webhooks)",
      "fecha_limite": "16/04/26"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": ""
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "23/04/26"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar JDs en LinkedIn + GetOnBrd (y hacer JD para el lunes)",
      "fecha_limite": "21/04/26"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "14/04/26",
      "evento": "Reunión de equipo de producto"
    },
    {
      "fecha": "16/04/26",
      "evento": "Fecha límite para que Seba arregle el bug de webhook"
    },
    {
      "fecha": "21/04/26",
      "evento": "Próxima reunión (10am) y fecha límite para JP de tener la JD"
    },
    {
      "fecha": "23/04/26",
      "evento": "Demo para cliente Falabella (Cami)"
    },
    {
      "fecha": "28/04/26 (original) / 05/05/26 (nueva)",
      "evento": "Lanzamiento v2.0 (movido de abril 28 a mayo 5)"
    }
  ],
  "decisiones": [
    "Mover el lanzamiento de la versión v2.0 del 28 de abril al 5 de mayo debido a falta de QA en el módulo de pagos y bug crítico en API webhooks.",
    "Aprobar presupuesto de $8M CLP/mes para la contratación de 2 desarrolladores senior y 1 QA (3 personas).",
    "JP se encargará de crear la descripción del puesto (JD) para el lunes y publicarla en LinkedIn y GetOnBrd."
  ]
}
```