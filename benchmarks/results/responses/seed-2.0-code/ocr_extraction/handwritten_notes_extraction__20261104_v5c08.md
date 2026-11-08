# Seed 2.0 Code — ocr_extraction/handwritten_notes_extraction

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.67 | quality: 10.0
- latency_total: 11.307s | tokens_per_second: 76.5
- input_tokens: 521 | output_tokens: 865

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
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsistentes: JP, MaJo, Seba, Cami (falta Nico)\n\n1) Lanzamiento v2.0 - mover del 28 de abril al 5 de mayo\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (¡muy bueno!)\n\n3) Contratar 2 devs senior + 1 QA\n   - presupuesto aprobado: $8M CLP/mes por 3 personas\n   - JP hace las descripciones de puesto para el lunes\n\n4) Próxima reunión: lunes 21/04 10am\n\nAction items:\n- Seba: fix bug de webhook para el miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar descripciones de puesto en LinkedIn + GetOnBrd",
  "fecha_reunion": "14/04/2026",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {"responsable": "Seba", "tarea": "Fix bug crítico de API webhooks", "fecha_limite": "16/04/2026"},
    {"responsable": "MaJo", "tarea": "Actualizar roadmap en Notion", "fecha_limite": "Sin fecha límite definida"},
    {"responsable": "Cami", "tarea": "Preparar demo para cliente Falabella", "fecha_limite": "23/04/2026"},
    {"responsable": "JP", "tarea": "Crear y publicar descripciones de puesto (JDs) para 2 devs senior y 1 QA en LinkedIn + GetOnBrd", "fecha_limite": "21/04/2026"}
  ],
  "fechas_clave": [
    {"fecha": "14/04/2026", "evento": "Reunión de equipo de producto"},
    {"fecha": "16/04/2026", "evento": "Fecha límite para fix de bug de webhooks (Seba)"},
    {"fecha": "21/04/2026", "evento": "Próxima reunión de equipo (10am) | Fecha límite para publicación de JDs (JP)"},
    {"fecha": "23/04/2026", "evento": "Demo para cliente Falabella"},
    {"fecha": "05/05/2026", "evento": "Nueva fecha de lanzamiento de v2.0 (postergado del 28/04)"}
  ],
  "decisiones": [
    "Postergar lanzamiento de v2.0 del 28 de abril al 5 de mayo por falta de QA en módulo pagos y bug crítico en webhooks",
    "Aprobar presupuesto de $8M CLP/mes para contratar 2 desarrolladores senior y 1 QA",
    "Definir próxima reunión de equipo para el lunes 21 de abril a las 10am"
  ]
}