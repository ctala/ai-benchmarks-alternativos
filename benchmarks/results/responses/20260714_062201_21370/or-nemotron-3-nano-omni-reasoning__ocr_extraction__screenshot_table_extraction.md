# Nemotron 3 Nano Omni 30B-A3B Reasoning — ocr_extraction/screenshot_table_extraction

- model_id: `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`
- success: True  | final: 6.6 | quality: 6.0
- latency_total: 9.489s | tokens_per_second: 287.4
- input_tokens: 435 | output_tokens: 2727
- judge_score: 3.0 | justificación: La respuesta incluye datos no presentes en la tabla original y proyecciones sin base, pero está bien organizada y ofrece algunos insights útiles.

## Respuesta completa

{
  "extracted_data": {
    "Jan": {
      "MRR": 45200,
      "Churn Rate": 4.2,
      "NPS": 42,
      "CAC": 234,
      "LTV": 1890,
      "Active Users": 1234,
      "Support Tickets": 89,
      "Avg Response (h)": 4.2
    },
    "Feb": {
      "MRR": 48700,
      "Churn Rate": 3.8,
      "NPS": 45,
      "CAC": 198,
      "LTV": 2010,
      "Active Users": 1456,
      "Support Tickets": 76,
      "Avg Response (h)": 3.1
    },
    "Mar": {
      "MRR": 52100,
      "Churn Rate": 3.1,
      "NPS": 51,
      "CAC": 187,
      "LTV": 2340,
      "Active Users": 1678,
      "Support Tickets": 63,
      "Avg Response (h)": 2.4
    }
  },
  "ltc_cac_ratios": {
    "Jan": 8.12,
    "Feb": 10.15,
    "Mar": 12.51
  },
  "metric_with_greatest_improvement": "Active Users",
  "april_projections": {
    "MRR": 55500,
    "Churn Rate": 2.4,
    "NPS": 57,
    "CAC": 176,
    "LTV": 2670,
    "Active Users": 1900,
    "Support Tickets": 50,
    "Avg Response (h)": 1.7
  }
}