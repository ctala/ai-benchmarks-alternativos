# Gemma 4 12B (Spark llama-server, reasoning) — ocr_extraction/screenshot_table_extraction

- model_id: `gemma-4-12b-it-Q4_K_M.gguf`
- success: True  | final: 5.76 | quality: 5.8
- latency_total: 93.176s | tokens_per_second: 25.5
- input_tokens: 434 | output_tokens: 2380
- judge_score: 3.2 | justificación: 

## Respuesta completa

```json
{
  "dashboard_info": {
    "title": "KPIs Marzo 2026",
    "trend_general": "Positiva en todas las métricas"
  },
  "raw_data": [
    {
      "metric": "MRR",
      "january": 45200,
      "february": 48700,
      "march": 52100,
      "var_m_m": "+7.0%"
    },
    {
      "metric": "Churn Rate",
      "january": 4.2,
      "february": 3.8,
      "march": 3.1,
      "var_m_m": "-0.7pp"
    },
    {
      "metric": "NPS",
      "january": 42,
      "february": 45,
      "march": 51,
      "var_m_m": "+6"
    },
    {
      "metric": "CAC",
      "january": 234,
      "february": 198,
      "march": 187,
      "var_m_m": "-$11"
    },
    {
      "metric": "LTV",
      "january": 1890,
      "february": 2010,
      "march": 2340,
      "var_m_m": "+$330"
    },
    {
      "metric": "Active Users",
      "january": 1234,
      "february": 1456,
      "march": 1678,
      "var_m_m": "+15.3%"
    },
    {
      "metric": "Support Tickets",
      "january": 89,
      "february": 76,
      "march": 63,
      "var_m_m": "-17.1%"
    },
    {
      "metric": "Avg Response (h)",
      "january": 4.2,
      "february": 3.1,
      "march": 2.4,
      "var_m_m": "-0.7"
    }
  ],
  "calculations": {
    "ltv_cac_ratio": {
      "january": 8.08,
      "february": 10.15,
      "march": 12.51
    }
  },
  "analysis": {
    "highest_improvement_metric": {
      "metric": "Avg Response (h)",
      "reasoning": "Presenta la mayor mejora porcentual relativa en el último periodo, con una reducción del 22.58% en el tiempo de respuesta (de 3.1 a 2.4 horas)."
    }
  },
  "projections_april_2026": {
    "methodology": "Proyección lineal basada en la tendencia del último mes (Marzo - Febrero)",
    "projected_values": {
      "MRR": "$55.5K",
      "Churn Rate": "2.4%",
      "NPS": 57,
      "CAC": "$176",
      "LTV": "$2,670",
      "Active Users": 1,900,
      "Support Tickets": 50,
      "Avg Response (h)": 1.7
    }
  }
}
```