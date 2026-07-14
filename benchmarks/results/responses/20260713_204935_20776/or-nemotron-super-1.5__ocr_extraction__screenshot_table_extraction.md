# Nemotron Super 49B v1.5 — ocr_extraction/screenshot_table_extraction

- model_id: `nvidia/llama-3.3-nemotron-super-49b-v1.5`
- success: True  | final: 7.28 | quality: 8.0
- latency_total: 126.325s | tokens_per_second: 51.5
- input_tokens: 401 | output_tokens: 6508
- judge_score: 3.0 | justificación: La respuesta incluye datos no presentes en la captura de pantalla original, afectando la precisión y relevancia, pero ofrece algunos insights útiles y está claramente organizada.

## Respuesta completa

```json
{
  "data": {
    "MRR": {"Enero": "$45.2K", "Feb": "$48.7K", "Marzo": "$52.1K", "Var M/M": "+7.0%"},
    "Churn Rate": {"Enero": "4.2%", "Feb": "3.8%", "Marzo": "3.1%", "Var M/M": "-0.7pp"},
    "NPS": {"Enero": "42", "Feb": "45", "Marzo": "51", "Var M/M": "+6"},
    "CAC": {"Enero": "$234", "Feb": "$198", "Marzo": "$187", "Var M/M": "-$11"},
    "LTV": {"Enero": "$1,890", "Feb": "$2,010", "Marzo": "$2,340", "Var M/M": "+$330"},
    "Active Users": {"Enero": "1,234", "Feb": "1,456", "Marzo": "1,678", "Var M/M": "+15.3%"},
    "Support Tickets": {"Enero": "89", "Feb": "76", "Marzo": "63", "Var M/M": "-17.1%"},
    "Avg Response (h)": {"Enero": "4.2", "Feb": "3.1", "Marzo": "2.4", "Var M/M": "-0.7"}
  },
  "ltv_cac_ratio": {
    "Enero": 8.08,
    "Feb": 10.15,
    "Marzo": 12.52
  },
  "metrica_mejor_mejora": {
    "metrica": "Avg Response (h)",
    "mejora_porcentual": "-22.58%"
  },
  "proyeccion_abril": {
    "MRR": "$55.7K",
    "Churn Rate": "2.4%",
    "NPS": "57",
    "CAC": "$176",
    "LTV": "$2,670",
    "Active Users": "1,935",
    "Support Tickets": "52",
    "Avg Response (h)": "1.7"
  }
}
```