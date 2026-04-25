# Mistral Nemo — ocr_extraction/handwritten_notes_extraction

- model_id: `mistralai/mistral-nemo`
- success: True  | final: 7.28 | quality: 8.24
- latency_total: 31.083s | tokens_per_second: 28.8
- input_tokens: 468 | output_tokens: 894
- judge_score: 4.2 | justificación: 

## Respuesta completa

Texto corregido:

"Reunión equipo prod - 14/04/26
Asist: JP, MaJo, Seba, Cami (faltó Nico)

1) Lanzamiento v2.0 - mover de abr 28 a may 5
   - falta QA en módulo pagos
   - bug crítico en API webhooks (Seba lo toma)

2) Metricas Q1:
   - MRR 52.1k (+15% vs Q4)
   - churn bajó a 3.1% (obj era 3.5%)
   - NPS subió a 51 (¡re bueno!)

3) Contratar 2 devs sr + 1 QA
   - presup aprob: $8M CLP/mes x 3 pax
   - JP hace JD p/ lunes

4) Próxima reunión: lun 21/04 10am

Action items:
- Seba: fix webhook bug p/ mierc 16/04
- MaJo: actualizar roadmap en Notion
- Cami: prep demo p/ cliente Falabella (23/04)
- JP: publicar JDs en LinkedIn + GetOnBrd"

Structura en JSON:
```json
{
  "texto_corregido": "Reunión equipo prod - 14/04/26\nAsist: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abr 28 a may 5\n   - falta QA en módulo pagos\n   - bug crítico en API webhooks (Seba lo toma)\n\n2) Metricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - churn bajó a 3.1% (obj era 3.5%)\n   - NPS subió a 51 (¡re bueno!)\n\n3) Contratar 2 devs sr + 1 QA\n   - presup aprob: $8M CLP/mes x 3 pax\n   - JP hace JD p/ lunes\n\n4) Próxima reunión: lun 21/04 10am\n\nAction items:\n- Seba: fix webhook bug p/ mierc 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: prep demo p/ cliente Falabella (23/04)\n- JP: publicar JDs en LinkedIn + GetOnBrd",
  "fecha_reunion": "14/04/26",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {"responsable": "Seba", "tarea": "fix webhook bug", "fecha_limite": "16/04"},
    {"responsable": "MaJo", "tarea": "actualizar roadmap en Notion", "fecha_limite": ""},
    {"responsable": "Cami", "tarea": "prep demo p/ cliente Falabella", "fecha_limite": "23/04"},
    {"responsable": "JP", "tarea": "publicar JDs en LinkedIn + GetOnBrd", "fecha_limite": ""}
  ],
  "fechas_clave": [
    {"fecha": "28/04", "evento": "Lanzamiento v2.0"},
    {"fecha": "05/05", "evento": "Lanzamiento v2.0"},
    {"fecha": "21/04", "evento": "Próxima reunión"}
  ],
  "decisiones": [
    "Lanzamiento v2.0 movido de 28/04 a 05/05",
    "Contratar 2 devs sr + 1 QA con presup