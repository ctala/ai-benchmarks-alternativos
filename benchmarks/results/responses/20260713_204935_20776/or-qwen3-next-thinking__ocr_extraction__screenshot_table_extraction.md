# Qwen 3-Next 80B Thinking — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3-next-80b-a3b-thinking`
- success: True  | final: 7.24 | quality: 8.0
- latency_total: 48.781s | tokens_per_second: 192.0
- input_tokens: 424 | output_tokens: 9364
- judge_score: 3.0 | justificación: La respuesta incluye datos no presentes en la tabla original, como 'LTV', 'Active Users', 'Support Tickets', y 'Avg Response (h)', lo que afecta la precisión y relevancia; sin embargo, ofrece proyecciones y un análisis de mejora que añaden profundidad, y está claramente organizada.

## Respuesta completa

{
  "data": [
    {
      "metrica": "MRR",
      "enero": 45200,
      "feb": 48700,
      "marzo": 52100,
      "var_mm": "+7.0%"
    },
    {
      "metrica": "Churn Rate",
      "enero": 4.2,
      "feb": 3.8,
      "marzo": 3.1,
      "var_mm": "-0.7pp"
    },
    {
      "metrica": "NPS",
      "enero": 42,
      "feb": 45,
      "marzo": 51,
      "var_mm": "+6"
    },
    {
      "metrica": "CAC",
      "enero": 234,
      "feb": 198,
      "marzo": 187,
      "var_mm": "-$11"
    },
    {
      "metrica": "LTV",
      "enero": 1890,
      "feb": 2010,
      "marzo": 2340,
      "var_mm": "+$330"
    },
    {
      "metrica": "Active Users",
      "enero": 1234,
      "feb": 1456,
      "marzo": 1678,
      "var_mm": "+15.3%"
    },
    {
      "metrica": "Support Tickets",
      "enero": 89,
      "feb": 76,
      "marzo": 63,
      "var_mm": "-17.1%"
    },
    {
      "metrica": "Avg Response (h)",
      "enero": 4.2,
      "feb": 3.1,
      "marzo": 2.4,
      "var_mm": "-0.7"
    }
  ],
  "ltv_cac_ratio": {
    "enero": 8.08,
    "feb": 10.15,
    "marzo": 12.51
  },
  "metrica_mayor_mejora": "Avg Response (h)",
  "proyeccion_abril": {
    "MRR": 55747,
    "Churn Rate": 2.4,
    "NPS": 57,
    "CAC": 176,
    "LTV": 2670,
    "Active Users": 1935,
    "Support Tickets": 52,
    "Avg Response (h)": 1.7
  }
}