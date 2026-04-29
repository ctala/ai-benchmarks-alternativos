# Nemotron 3 Nano Omni 30B-A3B Reasoning (NIM) — ocr_extraction/screenshot_table_extraction

- model_id: `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning`
- success: True  | final: 5.41 | quality: 4.6
- latency_total: 17.313s | tokens_per_second: 192.8
- input_tokens: 395 | output_tokens: 3338
- judge_score: 2.6 | justificación: 

## Respuesta completa

{
  "extracted_metrics": {
    "MRR": {
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100
    },
    "Churn Rate": {
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1
    },
    "NPS": {
      "enero": 42,
      "febrero": 45,
      "marzo": 51
    },
    "CAC": {
      "enero": 234,
      "febrero": 198,
      "marzo": 187
    },
    "LTV": {
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340
    },
    "Active Users": {
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678
    },
    "Support Tickets": {
      "enero": 89,
      "febrero": 76,
      "marzo": 63
    },
    "Avg Response (h)": {
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4
    }
  },
  "LTV_CAC_Ratios": {
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51
  },
  "largest_percent_improvement": "LTV",
  "april_projections": {
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