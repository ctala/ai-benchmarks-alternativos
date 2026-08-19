# Seed 2.0 Code — ocr_extraction/handwritten_notes_extraction

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.29 | quality: 10.0
- latency_total: 109.255s | tokens_per_second: 60.1
- input_tokens: 522 | output_tokens: 6570

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
  "texto_corregido": "Reunión equipo producto - 14/04/2024\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abril 28 a mayo 5\n   - falta QA en módulo de pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (realmente bueno!!)\n\n3) Contratar 2 desarrolladores senior + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 pax\n   - JP hace JDs para el lunes\n\n4) Próxima reunión: lunes 21/04 10:00\n\nAction items:\n- Seba: corregir bug de webhooks para el miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBoard",
  "fecha_reunion": "14/04/2024",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {"responsable": "Seba", "tarea": "Corregir bug crítico en API webhooks", "fecha_limite": "16/04/2024 (miércoles)"},
    {"responsable": "MaJo", "tarea": "Actualizar roadmap en Notion", "fecha_limite": "No especificada"},
    {"responsable": "Cami", "tarea": "Preparar demo para cliente Falabella", "fecha_limite": "23/04/2024"},
    {"responsable": "JP", "tarea": "Elaborar y publicar descripciones de puesto (JDs) en LinkedIn + GetOnBoard", "fecha_limite": "21/04/2024 (lunes)"}
  ],
  "fechas_clave": [
    {"fecha": "14/04/2024", "evento": "Reunión equipo producto"},
    {"fecha": "16/04/2024", "evento": "Fecha límite corrección bug crítico API webhooks (responsable: Seba)"},
    {"fecha": "21/04/2024 10:00", "evento": "Próxima reunión equipo producto; Fecha límite elaboración y publicación de JDs (responsable: JP)"},
    {"fecha": "23/04/2024", "evento": "Fecha límite preparación demo para cliente Falabella (responsable: Cami)"},
    {"fecha": "28/04/2024", "evento": "Fecha original postergada de lanzamiento v2.0"},
    {"fecha": "05/05/2024", "evento": "Nueva fecha de lanzamiento v2.0"},
    {"fecha": "Q1 2024", "evento": "Revisión de métricas trimestrales: MRR $52.1k (+15% vs Q4 2023), Churn 3.1% (objetivo: 3.5%), NPS 51"},
    {"fecha": "Q4 2023", "evento": "Trimestre de comparación para métricas MRR Q1 2024"}
  ],
  "decisiones": [
    "Postergar lanzamiento de la versión 2.0 del producto del 28 de abril al 5 de mayo, debido a falta de QA en el módulo de pagos y un bug crítico en la API de webhooks",
    "Aprobar presupuesto mensual de $8.000.000 CLP para la contratación de 2 desarrolladores senior y 1 profesional QA (total 3 puestos)",
    "Definir la próxima reunión de equipo para el lunes 21 de abril a las 10:00 horas",
    "Asignar action items específicos a cada asistente para dar seguimiento a las tareas pendientes"
  ]
}