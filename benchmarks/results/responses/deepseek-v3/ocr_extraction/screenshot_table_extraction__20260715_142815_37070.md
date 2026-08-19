# DeepSeek V3.2 — ocr_extraction/screenshot_table_extraction

- model_id: `deepseek/deepseek-chat`
- success: True  | final: 9.02 | quality: 10.0
- latency_total: 19.821s | tokens_per_second: 30.3
- input_tokens: 386 | output_tokens: 601
- judge_score: 3.0 | justificación: La respuesta incluye datos no presentes en la tabla original y proyecciones sin base, afectando la precisión y exactitud de datos, pero ofrece análisis útiles y está bien organizada.

## Respuesta completa

```json
{
  "data": [
    {
      "Metrica": "MRR",
      "Enero": "$45.2K",
      "Feb": "$48.7K",
      "Marzo": "$52.1K",
      "Var M/M": "+7.0%"
    },
    {
      "Metrica": "Churn Rate",
      "Enero": "4.2%",
      "Feb": "3.8%",
      "Marzo": "3.1%",
      "Var M/M": "-0.7pp"
    },
    {
      "Metrica": "NPS",
      "Enero": 42,
      "Feb": 45,
      "Marzo": 51,
      "Var M/M": "+6"
    },
    {
      "Metrica": "CAC",
      "Enero": "$234",
      "Feb": "$198",
      "Marzo": "$187",
      "Var M/M": "-$11"
    },
    {
      "Metrica": "LTV",
      "Enero": "$1,890",
      "Feb": "$2,010",
      "Marzo": "$2,340",
      "Var M/M": "+$330"
    },
    {
      "Metrica": "Active Users",
      "Enero": 1234,
      "Feb": 1456,
      "Marzo": 1678,
      "Var M/M": "+15.3%"
    },
    {
      "Metrica": "Support Tickets",
      "Enero": 89,
      "Feb": 76,
      "Marzo": 63,
      "Var M/M": "-17.1%"
    },
    {
      "Metrica": "Avg Response (h)",
      "Enero": 4.2,
      "Feb": 3.1,
      "Marzo": 2.4,
      "Var M/M": -0.7
    }
  ],
  "analisis": {
    "ltv_cac_ratio": {
      "Enero": 8.08,
      "Feb": 10.15,
      "Marzo": 12.51
    },
    "mayor_mejora_porcentual": {
      "Metrica": "Support Tickets",
      "Variacion": "-17.1%"
    },
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
}
```