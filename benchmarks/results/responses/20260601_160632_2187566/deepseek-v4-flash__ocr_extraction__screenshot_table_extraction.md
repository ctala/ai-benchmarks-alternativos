# DeepSeek V4 Flash (OpenRouter) — ocr_extraction/screenshot_table_extraction

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 6.31 | quality: 5.52
- latency_total: 27.762s | tokens_per_second: 131.0
- input_tokens: 386 | output_tokens: 3636
- judge_score: 3.0 | justificación: La respuesta incluye datos que no estaban en la captura de pantalla original, como 'LTV', 'Active Users', 'Support Tickets', y 'Avg Response (h)', lo que afecta la precisión y relevancia, pero ofrece algunos insights útiles y está bien organizada.

## Respuesta completa

```json
{
  "datos_extraidos": [
    {
      "metrica": "MRR",
      "enero": "$45.2K",
      "feb": "$48.7K",
      "mar": "$52.1K",
      "var_mm": "+7.0%"
    },
    {
      "metrica": "Churn Rate",
      "enero": "4.2%",
      "feb": "3.8%",
      "mar": "3.1%",
      "var_mm": "-0.7pp"
    },
    {
      "metrica": "NPS",
      "enero": 42,
      "feb": 45,
      "mar": 51,
      "var_mm": "+6"
    },
    {
      "metrica": "CAC",
      "enero": "$234",
      "feb": "$198",
      "mar": "$187",
      "var_mm": "-$11"
    },
    {
      "metrica": "LTV",
      "enero": "$1,890",
      "feb": "$2,010",
      "mar": "$2,340",
      "var_mm": "+$330"
    },
    {
      "metrica": "Active Users",
      "enero": 1234,
      "feb": 1456,
      "mar": 1678,
      "var_mm": "+15.3%"
    },
    {
      "metrica": "Support Tickets",
      "enero": 89,
      "feb": 76,
      "mar": 63,
      "var_mm": "-17.1%"
    },
    {
      "metrica": "Avg Response (h)",
      "enero": 4.2,
      "feb": 3.1,
      "mar": 2.4,
      "var_mm": "-0.7"
    }
  ],
  "ltv_cac_ratio": {
    "enero": 8.08,
    "feb": 10.15,
    "mar": 12.51
  },
  "mayor_mejora_porcentual": "Avg Response (h) – reducción del 22.58% en el tiempo de respuesta (de 3.1h a 2.4h)",
  "proyeccion_abril": {
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