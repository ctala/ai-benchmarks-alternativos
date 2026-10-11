# MiMo V2.6 Flash — ocr_extraction/handwritten_notes_extraction

- model_id: `xiaomi/mimo-v2.6-flash`
- success: True  | final: 8.52 | quality: 10.0
- latency_total: 216.604s | tokens_per_second: 20.9
- input_tokens: 477 | output_tokens: 4535

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
  "texto_corregido": "Reunión equipo producto - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abril 28 a mayo 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (re bueno!!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presupuesto aprobado: $8M CLP/mes x 3 personas\n   - JP hace JD para lunes\n\n4) Próx reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",

  "fecha_reunion": "14/04/2026",

  "asistentes": ["JP", "MaJo", "Seba", "Cami"],

  "ausentes": ["Nico"],

  "action_items": [
    {
      "responsable": "Seba",
      "tarea": "Fix de bug crítico en API webhooks",
      "fecha_limite": "16/04/2026"
    },
    {
      "responsable": "MaJo",
      "tarea": "Actualizar roadmap en Notion",
      "fecha_limite": "sin fecha explícita"
    },
    {
      "responsable": "Cami",
      "tarea": "Preparar demo para cliente Falabella",
      "fecha_limite": "23/04/2026"
    },
    {
      "responsable": "JP",
      "tarea": "Publicar JDs en LinkedIn + GetOnBrd (previamente: crear JD para lunes)",
      "fecha_limite": "20/04/2026"
    }
  ],

  "fechas_clave": [
    {
      "fecha": "14/04/2026",
      "evento": "Reunión del equipo producto"
    },
    {
      "fecha": "16/04/2026",
      "evento": "Seba debe entregar fix de bug webhooks (miércoles)"
    },
    {
      "fecha": "20/04/2026",
      "evento": "JP debe tener JDs listas (lunes)"
    },
    {
      "fecha": "21/04/2026",
      "evento": "Próxima reunión del equipo (10:00 hrs)"
    },
    {
      "fecha": "23/04/2026",
      "evento": "Demo preparada para cliente Falabella"
    },
    {
      "fecha": "28/04/2026",
      "evento": "Lanzamiento v2.0 original (postergado)"
    },
    {
      "fecha": "05/05/2026",
      "evento": "Nueva fecha de lanzamiento v2.0 (reprogramado)"
    }
  ],

  "decisiones": [
    "Se postergó el lanzamiento de v2.0 del 28/04 al 05/05 por falta de QA en módulo pagos y bug crítico en API webhooks",
    "Se asignó a Seba el bug crítico de API webhooks",
    "Se aprobó presupuesto de $8.000.000 CLP/mes para contratar 3 personas (2 devs senior + 1 QA)",
    "JP se encargará de crear las JD (Job Descriptions) para el lunes"
  ]
}
```

### Correcciones de OCR aplicadas

| Error OCR | Corrección |
|---|---|
| Reunlon | **Reunión** |
| equlpo | **equipo** |
| falt0 | **faltó** |
| modul0 | **módulo** |
| webho0ks | **webhooks** |
| Metricas | **Métricas** |
| baj0 | **bajó** |
| subio | **subió** |
| presup | **presupuesto** |
| actualzr | **actualizar** |
| crít | **crítico** |
| p/ | **para** (abreviatura) |
| prod | **producto** (abreviatura) |
| mierc | **miércoles** |
| prep | **preparar** |
| pax | **personas** (jerga) |
| re bueno | **re bueno** ✅ (chilenismo intencional = "muy bueno") |