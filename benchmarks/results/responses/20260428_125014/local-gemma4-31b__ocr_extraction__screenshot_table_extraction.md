# Gemma 4 31B (DGX Spark Q4_K_M) — ocr_extraction/screenshot_table_extraction

- model_id: `gemma4:31b`
- success: True  | final: 5.68 | quality: 5.8
- latency_total: 565.096s | tokens_per_second: 4.2
- input_tokens: 433 | output_tokens: 2398
- judge_score: 3.2 | justificación: 

## Respuesta completa

```json
{
  "extracted_data": [
    {
      "metrica": "MRR",
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "var_mm": "7.0%"
    },
    {
      "metrica": "Churn Rate",
      "enero": 0.042,
      "febrero": 0.038,
      "marzo": 0.031,
      "var_mm": "-0.7pp"
    },
    {
      "metrica": "NPS",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "var_mm": "+6"
    },
    {
      "metrica": "CAC",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "var_mm": "-$11"
    },
    {
      "metrica": "LTV",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "var_mm": "+$330"
    },
    {
      "metrica": "Active Users",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "var_mm": "15.3%"
    },
    {
      "metrica": "Support Tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "var_mm": "-17.1%"
    },
    {
      "metrica": "Avg Response (h)",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "var_mm": "-0.7"
    }
  ],
  "analysis": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51
    },
    "highest_percentage_improvement": {
      "metrica": "Support Tickets",
      "value": "-17.1%",
      "note": "La reducción en tickets de soporte representa la mayor mejora porcentual en el último mes."
    }
  },
  "projections_april": {
    "MRR": "$55.7K",
    "Churn Rate": "2.4%",
    "NPS": 57,
    "CAC": "$176",
    "LTV": "$2,670",
    "Active Users": 1935,
    "Support Tickets": 52,
    "Avg Response (h)": 1.7
  }
}
```