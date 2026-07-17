# MiMo-V2.5 Pro — ocr_extraction/handwritten_notes_extraction

- model_id: `xiaomi/mimo-v2.5-pro`
- success: True  | final: 8.51 | quality: 10.0
- latency_total: 24.166s | tokens_per_second: 84.7
- input_tokens: 477 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con una buena profundidad al incluir detalles adicionales como los action items y la próxima reunión.

## Respuesta completa

```json
{
  "texto_corregido": "Reunión equipo producto - 14/04/26\nAsistentes: JP, MaJo, Seba, Cami (faltó Nico)\n\n1) Lanzamiento v2.0 - mover de abril 28 a mayo 5\n   - Falta QA en módulo pagos\n   - Bug crítico en API webhooks (Seba lo toma)\n\n2) Métricas Q1:\n   - MRR 52.1k (+15% vs Q4)\n   - Churn bajó a 3.1% (objetivo era 3.5%)\n   - NPS subió a 51 (¡¡muy bueno!!)\n\n3) Contratar 2 desarrolladores senior + 1 QA\n   - Presupuesto aprobado: $8M CLP/mes x 3 personas\n   - JP hace descripción de puesto (JD) para lunes\n\n4) Próxima reunión: lunes 21/04 10am\n\nAction items:\n- Seba: fix webhook bug para miércoles 16/04\n- MaJo: actualizar roadmap en Notion\n- Cami: preparar demo para cliente Falabella (23/04)\n- JP: publicar descripciones de puesto en LinkedIn + GetOnBrd",
  "fecha_reunion": "14/04/26",
  "asistentes": ["JP", "MaJo", "Seba", "Cami"],
  "ausentes": ["Nico"],
  "action_items": [
    {"responsable": "Seba", "tarea": "Fix webhook bug", "fecha_limite": "16/04/26"},
    {"responsable": "MaJo", "tarea": "Actualizar roadmap en Notion