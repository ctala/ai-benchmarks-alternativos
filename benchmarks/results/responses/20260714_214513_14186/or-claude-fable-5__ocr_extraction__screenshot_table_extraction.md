# Claude Fable 5 — ocr_extraction/screenshot_table_extraction

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 6.56 | quality: 8.0
- latency_total: 23.047s | tokens_per_second: 88.9
- input_tokens: 512 | output_tokens: 2048
- judge_score: 4.0 | justificación: La respuesta es generalmente precisa y relevante, pero incluye datos no presentes en la tabla original, afectando la precisión; sin embargo, ofrece un análisis profundo y útil con claridad.

## Respuesta completa

```json
{
  "dashboard": {
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "tendencia_general": "Positiva en todas las métricas",
    "metricas": [
      {
        "nombre": "MRR",
        "enero": 45200,
        "febrero": 48700,
        "marzo": 52100,
        "variacion_mm": "+7.0%",
        "unidad": "USD"
      },
      {
        "nombre": "Churn Rate",
        "enero": 4.2,
        "febrero": 3.8,
        "marzo": 3.1,
        "variacion_mm": "-0.7pp",
        "unidad": "%"
      },
      {
        "nombre": "NPS",
        "enero": 42,
        "febrero": 45,
        "marzo": 51,
        "variacion_mm": "+6",
        "unidad": "puntos"
      },
      {
        "nombre": "CAC",
        "enero": 234,
        "febrero": 198,
        "marzo": 187,
        "variacion_mm": "-$11",
        "unidad": "USD"
      },
      {
        "nombre": "LTV",
        "enero": 1890,
        "febrero": 2010,
        "marzo": 2340,
        "variacion_mm": "+$330",
        "unidad": "USD"
      },
      {
        "nombre": "Active Users",
        "enero": 1234,
        "febrero": 1456,
        "marzo": 1678,
        "variacion_mm": "+15.3%",
        "unidad": "usuarios"
      },
      {
        "nombre": "Support Tickets",
        "enero": 89,
        "febrero": 76,
        "marzo": 63,
        "variacion_mm": "-17.1%",
        "unidad": "tickets"
      },
      {
        "nombre": "Avg Response",
        "enero": 4.2,
        "febrero": 3.1,
        "marzo": 2.4,
        "variacion_mm": "-0.7",
        "unidad": "horas"
      }
    ]
  },
  "analisis": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "interpretacion": "Ratio muy saludable (benchmark >3). Tendencia creciente indica mejora en eficiencia de adquisición y retención."
    },
    "mayor_mejora_porcentual": {
      "feb_a_marzo": {
        "metrica": "Avg Response Time",
        "cambio": "-22.6%",
        "detalle": "De 3.1h a 2.4h"
      },
      "enero_a_marzo": {
        "metrica": "Avg Response Time",
        "cambio": "-42.9%",
        "detalle": "De 4.2h a 2.4h"
      },
      "ranking_mejora_feb_marzo": [
        { "metrica": "Avg Response Time", "mejora_pct": 22.6 },
        { "metrica": "Churn Rate", "mejora_pct": 18.4 },
        { "metrica": "Support Tickets", "mejora_pct": 17.1 },
        { "metrica": "LTV", "mejora_pct": 16.4 },
        { "metrica": "Active Users", "mejora_pct": 15.3 },
        { "metrica": "NPS", "mejora_pct": 13.3 },
        { "metrica": "MRR", "mejora_pct": 7.0 },
        { "metrica": "CAC", "mejora_pct": 5.6 }
      ]
    },
    "proyeccion_abril": {
      "metodologia": "Extrapolación de la variación M/M de marzo",
      "valores": {
        "mrr": { "valor": 55750, "formato": "$55.7K", "supuesto": "+7.0% mantenido" },
        "churn_rate": { "valor": 2.4, "formato": "2.4%", "supuesto": "-0.7pp mantenido" },
        "nps": { "valor":