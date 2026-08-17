# Nemotron 3 Super 120B (DGX Spark Q4_K_M) — ocr_extraction/screenshot_table_extraction

- model_id: `nemotron-3-super:120b`
- success: True  | final: 5.53 | quality: 5.8
- latency_total: 194.644s | tokens_per_second: 18.5
- input_tokens: 442 | output_tokens: 3599
- judge_score: 3.2 | justificación: 

## Respuesta completa

{
  "datos_extraidos": {
    "MRR": {
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "var_m_m": "+7.0%"
    },
    "Churn Rate": {
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "var_m_m": "-0.7pp"
    },
    "NPS": {
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "var_m_m": "+6"
    },
    "CAC": {
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "var_m_m": "-$11"
    },
    "LTV": {
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "var_m_m": "+$330"
    },
    "Active Users": {
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "var_m_m": "+15.3%"
    },
    "Support Tickets": {
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "var_m_m": "-17.1%"
    },
    "Avg Response (h)": {
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "var_m_m": "-0.7"
    }
  },
  "ltv_cac_ratio": {
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51
  },
  "metrica_mejor_mejora": {
    "nombre": "Avg Response (h)",
    "mejora_porcentual": 22.58
  },
  "proyeccion_abril": {
    "MRR": 55747,
    "Churn Rate": "2.4%",
    "NPS": 57,
    "CAC": 176,
    "LTV": 2670,
    "Active Users": 1935,
    "Support Tickets": 52,
    "Avg Response (h)": 1.7
  }
}