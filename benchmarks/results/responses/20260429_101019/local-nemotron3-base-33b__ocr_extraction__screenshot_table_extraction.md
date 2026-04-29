# Nemotron 3 Base 33B (DGX Spark Q4_K_M) — ocr_extraction/screenshot_table_extraction

- model_id: `nemotron3:33b-q4_K_M`
- success: True  | final: 5.31 | quality: 4.6
- latency_total: 62.298s | tokens_per_second: 65.5
- input_tokens: 443 | output_tokens: 4080
- judge_score: 2.6 | justificación: 

## Respuesta completa

{
  "extracted_data": [
    {
      "metric": "MRR",
      "enero": 45200,
      "feb": 48700,
      "marzo": 52100,
      "var_m/m": "+7.0%"
    },
    {
      "metric": "Churn Rate",
      "enero": 4.2,
      "feb": 3.8,
      "marzo": 3.1,
      "var_m/m": "-0.7pp"
    },
    {
      "metric": "NPS",
      "enero": 42,
      "feb": 45,
      "marzo": 51,
      "var_m/m": "+6"
    },
    {
      "metric": "CAC",
      "enero": 234,
      "feb": 198,
      "marzo": 187,
      "var_m/m": "-$11"
    },
    {
      "metric": "LTV",
      "enero": 1890,
      "feb": 2010,
      "marzo": 2340,
      "var_m/m": "+$330"
    },
    {
      "metric": "Active Users",
      "enero": 1234,
      "feb": 1456,
      "marzo": 1678,
      "var_m/m": "+15.3%"
    },
    {
      "metric": "Support Tickets",
      "enero": 89,
      "feb": 76,
      "marzo": 63,
      "var_m/m": "-17.1%"
    },
    {
      "metric": "Avg Response (h)",
      "enero": 4.2,
      "feb": 3.1,
      "marzo": 2.4,
      "var_m/m": "-0.7"
    }
  ],
  "ltv_cac_ratios": [
    {
      "mes": "Enero",
      "ratio": 8.08
    },
    {
      "mes": "Febrero",
      "ratio": 10.15
    },
    {
      "mes": "Marzo",
      "ratio": 12.51
    }
  ],
  "metrica_mejor_mejora_percentual": "Active Users",
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