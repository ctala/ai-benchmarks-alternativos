# Gemma 4 12B (Spark llama-server Q4_K_M) — ocr_extraction/screenshot_table_extraction

- model_id: `gemma-4-12b-it-Q4_K_M.gguf`
- success: True  | final: 5.98 | quality: 5.8
- latency_total: 33.928s | tokens_per_second: 25.2
- input_tokens: 431 | output_tokens: 854
- judge_score: 3.2 | justificación: 

## Respuesta completa

Aquí tienes la extracción de datos y el análisis solicitado en formato JSON estructurado:

```json
{
  "metadata": {
    "dashboard_name": "KPIs Marzo 2026",
    "currency": "USD",
    "period_analyzed": ["Enero", "Feb", "Marzo"]
  },
  "raw_data": [
    {
      "metrica": "MRR",
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "var_m_m": "+7.0%"
    },
    {
      "metrica": "Churn Rate",
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "var_m_m": "-0.7pp"
    },
    {
      "metrica": "NPS",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "var_m_m": "+6"
    },
    {
      "metrica": "CAC",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "var_m_m": "-$11"
    },
    {
      "metrica": "LTV",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "var_m_m": "+$330"
    },
    {
      "metrica": "Active Users",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "var_m_m": "+15.3%"
    },
    {
      "metrica": "Support Tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "var_m_m": "-17.1%"
    },
    {
      "metrica": "Avg Response (h)",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "var_m_m": "-0.7"
    }
  ],
  "analysis": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51
    },
    "top_improvement_metric": {
      "metric_name": "Support Tickets",
      "improvement_percentage": "-17.1%",
      "note": "Mayor mejora porcentual en términos de reducción de carga de soporte."
    },
    "projections_abril_2026": {
      "note": "Proyecciones basadas en la tendencia de crecimiento/reducción del último mes (Marzo).",
      "MRR": 55667,
      "Churn Rate": 2.4,
      "NPS": 57,
      "CAC": 176,
      "LTV": 2670,
      "Active Users": 1934,
      "Support Tickets": 51,
      "Avg Response (h)": 1.7
    }
  }
}
```