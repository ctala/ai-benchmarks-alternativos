# Qwen 3.5 397B (NIM) — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 6.13 | quality: 5.8
- latency_total: 44.182s | tokens_per_second: 19.7
- input_tokens: 376 | output_tokens: 871
- judge_score: 3.2 | justificación: 

## Respuesta completa

```json
{
  "dashboard_info": {
    "title": "DASHBOARD - KPIs Marzo 2026",
    "trend_summary": "Positiva en todas las metricas"
  },
  "extracted_data": [
    {
      "metric": "MRR",
      "jan": "$45.2K",
      "feb": "$48.7K",
      "mar": "$52.1K",
      "var_m_m": "+7.0%"
    },
    {
      "metric": "Churn Rate",
      "jan": "4.2%",
      "feb": "3.8%",
      "mar": "3.1%",
      "var_m_m": "-0.7pp"
    },
    {
      "metric": "NPS",
      "jan": 42,
      "feb": 45,
      "mar": 51,
      "var_m_m": "+6"
    },
    {
      "metric": "CAC",
      "jan": "$234",
      "feb": "$198",
      "mar": "$187",
      "var_m_m": "-$11"
    },
    {
      "metric": "LTV",
      "jan": "$1,890",
      "feb": "$2,010",
      "mar": "$2,340",
      "var_m_m": "+$330"
    },
    {
      "metric": "Active Users",
      "jan": 1234,
      "feb": 1456,
      "mar": 1678,
      "var_m_m": "+15.3%"
    },
    {
      "metric": "Support Tickets",
      "jan": 89,
      "feb": 76,
      "mar": 63,
      "var_m_m": "-17.1%"
    },
    {
      "metric": "Avg Response (h)",
      "jan": 4.2,
      "feb": 3.1,
      "mar": 2.4,
      "var_m_m": "-0.7"
    }
  ],
  "analysis": {
    "ltv_cac_ratio": {
      "jan": 8.08,
      "feb": 10.15,
      "mar": 12.51,
      "calculation_note": "Calculado dividiendo LTV entre CAC (valores numéricos extraídos sin símbolos de moneda)."
    },
    "highest_percentage_improvement": {
      "metric": "Support Tickets",
      "value": "-17.1%",
      "reasoning": "Aunque el signo es negativo, representa una mejora (reducción de carga). En magnitud absoluta de cambio positivo, es la mayor variación porcentual registrada en la columna 'Var M/M'. Si se considera estrictamente crecimiento positivo, sería 'Active Users' con +15.3%."
    },
    "april_projection": {
      "methodology": "Proyección lineal basada en el delta absoluto promedio de los últimos dos meses (Feb->Mar) aplicado a los valores de Marzo.",
      "projections": {
        "MRR": "$55.5K",
        "Churn Rate": "2.4%",
        "NPS": 57,
        "CAC": "$176",
        "LTV": "$2,670",
        "Active Users": 1900,
        "Support Tickets": 50,
        "Avg Response (h)": 1.7
      }
    }
  }
}
```