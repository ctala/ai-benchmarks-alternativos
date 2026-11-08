# Gemini 4 Argon — ocr_extraction/handwritten_notes_extraction

- model_id: `google/gemini-4-argon`
- success: True  | final: 8.39 | quality: 10.0
- latency_total: 19.464s | tokens_per_second: 54.9
- input_tokens: 492 | output_tokens: 1068

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
  "texto_corregido": "Reunión equipo de producto - 14/04/2026\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de 28 de abril a 5 de mayo\n   - Falta QA (Control de Calidad) en módulo de pagos\n   - Bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1 (Primer Trimestre):\n   - MRR (Ingresos Recurrentes Mensuales) 52.1k (+15% vs Q4)\n   - Churn (Tasa de cancelación) bajó a 3.1% (objetivo era 3.5%)\n   - NPS (Net Promoter Score) subió a 51 (¡muy bueno!)\n\n3) Contratar 2 desarrolladores Senior + 1 QA\n   - Presupuesto aprobado: $8M CLP/mes por 3 personas\n   - JP hace las descripciones de puesto (JD) para el lunes\n\n4) Próxima reunión: lunes 21/04 a las 10:00 am\n\nAction items (Tareas pendientes):\n- Seba: arreglar bug de webhook para el miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar descripciones de puesto (JDs) en LinkedIn + GetOnBrd",
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
      "tarea": "Solucionar bug crítico en API de webhooks",
      "fecha_limite": "2026-04-16"
    },
    {
      "responsable": "JP",
      "tarea": "Redactar las descripciones de cargo (JDs) y publicarlas en LinkedIn y GetOnBrd",
      "fecha_limite": "2026-04-20"
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demostración (demo) para el cliente Falabella",
      "fecha_limite": "2026-04-23"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar el roadmap en Notion",
      "fecha_limite": "No especificada"
    }
  ],
  "fechas_clave": [
    {
      "fecha": "2026-04-14",
      "evento": "Reunión actual del equipo de producto"
    },
    {
      "fecha": "2026-04-16",
      "evento": "Fecha límite para solucionar el bug de webhook (Seba)"
    },
    {
      "fecha": "2026-04-20",
      "evento": "Entrega de las descripciones de puesto (JDs) por parte de JP (Lunes)"
    },
    {
      "fecha": "2026-04-21",
      "evento": "Próxima reunión de equipo (10:00 am)"
    },
    {
      "fecha": "2026-04-23",
      "evento": "Presentación de demo al cliente Falabella"
    },
    {
      "fecha": "2026-04-28",
      "evento": "Fecha original del lanzamiento v2.0 (Cancelada/Movida)"
    },
    {
      "fecha": "2026-05-05",
      "evento": "Nueva fecha oficial para el lanzamiento de la v2.0"
    }
  ],
  "decisiones": [
    "Posponer el lanzamiento de la versión 2.0 del 28 de abril al 5 de mayo debido a falta de QA en el módulo de pagos y un bug crítico.",
    "Asignar a Seba la resolución inmediata del bug crítico en la API de webhooks.",
    "Aprobar la contratación de 3 nuevas personas (2 Desarrolladores Senior y 1 QA) con un presupuesto total de $8.000.000 CLP mensuales."
  ]
}
```