# Grok 4.3 — ocr_extraction/screenshot_table_extraction

- model_id: `x-ai/grok-4.3`
- success: True  | final: 4.83 | quality: 4.4
- latency_total: 10.344s | tokens_per_second: 137.3
- input_tokens: 484 | output_tokens: 1420

## Respuesta completa

{
  "data": {
    "periodo": "Marzo 2026",
    "metricas": [
      {"nombre": "MRR", "Enero": "45.2K", "Febrero": "48.7K", "Marzo": "52.1K", "Var_MM": "+7.0%"},
      {"nombre": "Churn Rate", "Enero": "4.2%", "Febrero": "3.8%", "Marzo": "3.1%", "Var_MM": "-0.7pp"},
      {"nombre": "NPS", "Enero": 42, "Febrero": 45, "Marzo": 51, "Var_MM": "+6"},
      {"nombre": "CAC", "Enero": 234, "Febrero": 198, "Marzo": 187, "Var_MM": -11},
      {"nombre": "LTV", "Enero": 1890, "Febrero": 2010, "Marzo": 2340, "Var_MM": 330},
      {"nombre": "Active Users", "Enero": 1234, "Febrero": 1456, "Marzo": 1678, "Var_MM": "+15.3%"},
      {"nombre": "Support Tickets", "Enero": 89, "Febrero": 76, "Marzo": 63, "Var_MM": "-17.1%"},
      {"nombre": "Avg Response (h)", "Enero": 4.2, "Febrero": 3.1, "Marzo": 2.4, "Var_MM": -0.7}
    ]
  },
  "ltv_cac_ratio": {
    "Enero": 8.08,
    "Febrero": 10.15,
    "Marzo": 12.51
  },
  "metrica_mayor_mejora_porcentual": "Support Tickets",
  "proyeccion_abril": {
    "MRR": "55.7K",
    "Churn Rate": "2.4%",
    "NPS": 57,
    "CAC": 176,
    "LTV": 2670,
    "Active Users": 1935,
    "Support Tickets": 52,
    "Avg Response (h)": 1.7
  }
}