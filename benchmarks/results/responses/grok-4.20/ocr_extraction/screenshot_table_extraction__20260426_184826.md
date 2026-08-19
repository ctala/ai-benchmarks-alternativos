# Grok 4.20 — ocr_extraction/screenshot_table_extraction

- model_id: `x-ai/grok-4.20`
- success: True  | final: 6.48 | quality: 5.8
- latency_total: 5.276s | tokens_per_second: 113.7
- input_tokens: 476 | output_tokens: 600
- judge_score: 3.2 | justificación: 

## Respuesta completa

```json
{
  "dashboard_title": "DASHBOARD - KPIs Marzo 2026",
  "data": {
    "MRR": {
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "var_mm": 0.07
    },
    "Churn_Rate": {
      "enero": 0.042,
      "febrero": 0.038,
      "marzo": 0.031,
      "var_mm": -0.007
    },
    "NPS": {
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "var_mm": 6
    },
    "CAC": {
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "var_mm": -11
    },
    "LTV": {
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "var_mm": 330
    },
    "Active_Users": {
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "var_mm": 0.153
    },
    "Support_Tickets": {
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "var_mm": -0.171
    },
    "Avg_Response_Hours": {
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "var_mm": -0.7
    }
  },
  "ltv_cac_ratio": {
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51
  },
  "mejor_mejora_porcentual": {
    "metrica": "Support_Tickets",
    "mejora_porcentual": -17.1,
    "descripcion": "Reducción del 17.1% (mejoría más significativa)"
  },
  "proyeccion_abril": {
    "MRR": 55757,
    "Churn_Rate": 2.4,
    "NPS": 57,
    "CAC": 176,
    "LTV": 2670,
    "Active_Users": 1930,
    "Support_Tickets": 52,
    "Avg_Response_Hours": 1.7,
    "LTV_CAC_ratio": 15.17
  },
  "tendencia_general": "↑ Positiva en todas las metricas"
}
```