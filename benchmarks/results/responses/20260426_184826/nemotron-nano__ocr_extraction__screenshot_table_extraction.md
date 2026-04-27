# Nemotron 3 Nano 30B — ocr_extraction/screenshot_table_extraction

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 6.5 | quality: 5.44
- latency_total: 44.798s | tokens_per_second: 94.5
- input_tokens: 435 | output_tokens: 4234
- judge_score: 3.2 | justificación: 

## Respuesta completa

```json
{
  "extracted_data": {
    "January": {
      "MRR": 45200,
      "Churn_Rate": 4.2,
      "NPS": 42,
      "CAC": 234,
      "LTV": 1890,
      "Active_Users": 1234,
      "Support_Tickets": 89,
      "Avg_Response_h": 4.2
    },
    "February": {
      "MRR": 48700,
      "Churn_Rate": 3.8,
      "NPS": 45,
      "CAC": 198,
      "LTV": 2010,
      "Active_Users": 1456,
      "Support_Tickets": 76,
      "Avg_Response_h": 3.1
    },
    "March": {
      "MRR": 52100,
      "Churn_Rate": 3.1,
      "NPS": 51,
      "CAC": 187,
      "LTV": 2340,
      "Active_Users": 1678,
      "Support_Tickets": 63,
      "Avg_Response_h": 2.4
    }
  },

  "ltv_cac_ratio": {
    "January": 8.08,
    "February": 10.15,
    "March": 12.51
  },

  "greatest_improvement_metric": {
    "metric": "Avg_Response_h",
    "percentage_improvement": -22.58,
    "note": "Largest month‑over‑month improvement (percentage decrease) among all metrics"
  },

  "projection_april": {
    "MRR": 55747,
    "Churn_Rate": 2.53,
    "NPS": 57,
    "CAC": 176,
    "LTV": 2670,
    "Active_Users": 1936,
    "Support_Tickets": 52,
    "Avg_Response_h": 1.86
  }
}
```