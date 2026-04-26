# Qwen 3.5 397B (Ollama Cloud) — ocr_extraction/screenshot_table_extraction

- model_id: `qwen3.5:397b-cloud`
- success: True  | final: 6.78 | quality: 5.8
- latency_total: 27.431s | tokens_per_second: 74.7
- input_tokens: 427 | output_tokens: 2048
- judge_score: 3.2 | justificación: 

## Respuesta completa

```json
{
  "dashboard_metadata": {
    "title": "DASHBOARD - KPIs Marzo 2026",
    "period": "Q1 2026",
    "trend_summary": "Positiva en todas las metricas"
  },
  "extracted_data": [
    {
      "metric": "MRR",
      "jan": 45200,
      "feb": 48700,
      "mar": 52100,
      "var_mm_percent": 7.0,
      "unit": "USD"
    },
    {
      "metric": "Churn Rate",
      "jan": 4.2,
      "feb": 3.8,
      "mar": 3.1,
      "var_mm_points": -0.7,
      "unit": "percent"
    },
    {
      "metric": "NPS",
      "jan": 42,
      "feb": 45,
      "mar": 51,
      "var_mm_points": 6,
      "unit": "score"
    },
    {
      "metric": "CAC",
      "jan": 234,
      "feb": 198,
      "mar": 187,
      "var_mm_value": -11,
      "unit": "USD"
    },
    {
      "metric": "LTV",
      "jan": 1890,
      "feb": 2010,
      "mar": 2340,
      "var_mm_value": 330,
      "unit": "USD"
    },
    {
      "metric": "Active Users",
      "jan": 1234,
      "feb": 1456,
      "mar": 1678,
      "var_mm_percent": 15.3,
      "unit": "count"
    },
    {
      "metric": "Support Tickets",
      "jan": 89,
      "feb": 76,
      "mar": 63,
      "var_mm_percent": -17.1,
      "unit": "count"
    },
    {
      "metric": "Avg Response (h)",
      "jan": 4.2,
      "feb": 3.1,
      "mar": 2.4,
      "var_mm_value": -0.7,
      "unit": "hours"
    }
  ],
  "analysis": {
    "ltv_cac_ratio": {
      "january": 8.08,
      "february": 10.15,
      "march": 12.51,
      "interpretation": "Saludable y en crecimiento (Ratio > 3 es ideal)"
    },
    "best_improvement_metric": {
      "metric_name": "Avg Response (h)",
      "reason": "Aunque 'Active Users' tiene el mayor crecimiento positivo explícito (+15.3%), la reducción en el tiempo de respuesta de 3.1h a 2.4h representa una mejora de eficiencia del 22.6%, siendo el cambio relativo más impactante en el periodo M/M.",
      "improvement_percentage": 22.6
    },
    "april_projection": {
      "methodology": "Proyección lineal basada en la variación Month-over-Month (M/M) de Marzo",
      "values": {
        "MRR": "$55,747",
        "Churn Rate": "2.4%",
        "NPS": 57,
        "CAC": "$176",
        "LTV": "$2,670",
        "Active Users": 1935,
        "Support Tickets":