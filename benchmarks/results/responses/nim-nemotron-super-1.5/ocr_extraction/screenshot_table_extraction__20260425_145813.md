# Nemotron Super 49B v1.5 (NIM) — ocr_extraction/screenshot_table_extraction

- model_id: `nvidia/llama-3.3-nemotron-super-49b-v1.5`
- success: True  | final: 5.4 | quality: 5.44
- latency_total: 278.077s | tokens_per_second: 16.8
- input_tokens: 358 | output_tokens: 4670
- judge_score: 3.2 | justificación: 

## Respuesta completa

```json
{
  "dashboard": [
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
      "Enero": "42",
      "Feb": "45",
      "Marzo": "51",
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
      "Enero": "1,234",
      "Feb": "1,456",
      "Marzo": "1,678",
      "Var M/M": "+15.3%"
    },
    {
      "Metrica": "Support Tickets",
      "Enero": "89",
      "Feb": "76",
      "Marzo": "63",
      "Var M/M": "-17.1%"
    },
    {
      "Metrica": "Avg Response (h)",
      "Enero": "4.2",
      "Feb": "3.1",
      "Marzo": "2.4",
      "Var M/M": "-0.7"
    }
  ],
  "ltv_cac_ratios": {
    "Enero": 8.08,
    "Feb": 10.15,
    "Marzo": 12.52
  },
  "highest_percentage_improvement": {
    "metric": "LTV",
    "percentage_change": 16.42
  },
  "projections": {
    "Abril": {
      "MRR": "$55.7K",
      "Churn Rate": "2.4%",
      "NPS": "57",
      "CAC": "$176",
      "LTV": "$2,670",
      "Active Users": "1,936",
      "Support Tickets": "52",
      "Avg Response (h)": "1.7"
    }
  }
}
```