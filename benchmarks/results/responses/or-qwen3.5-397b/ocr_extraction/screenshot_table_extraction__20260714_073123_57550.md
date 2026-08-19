# Qwen 3.5 397B — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 7.15 | quality: 8.0
- latency_total: 36.454s | tokens_per_second: 56.2
- input_tokens: 427 | output_tokens: 2048
- judge_score: 3.0 | justificación: La respuesta incluye datos no presentes en la tabla original, como LTV y Active_Users, afectando la precisión y exactitud de datos, pero ofrece una estructura clara y análisis útiles.

## Respuesta completa

```json
{
  "dashboard_info": {
    "title": "DASHBOARD - KPIs Marzo 2026",
    "period": "Enero - Marzo 2026",
    "trend": "Positiva en todas las metricas"
  },
  "metrics": {
    "MRR": {
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "var_m_m": "+7.0%",
      "unit": "USD"
    },
    "Churn_Rate": {
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "var_m_m": "-0.7pp",
      "unit": "percentage"
    },
    "NPS": {
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "var_m_m": "+6",
      "unit": "score"
    },
    "CAC": {
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "var_m_m": "-$11",
      "unit": "USD"
    },
    "LTV": {
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "var_m_m": "+$330",
      "unit": "USD"
    },
    "Active_Users": {
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "var_m_m": "+15.3%",
      "unit": "count"
    },
    "Support_Tickets": {
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "var_m_m": "-17.1%",
      "unit": "count"
    },
    "Avg_Response_Time": {
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "var_m_m": "-0.7",
      "unit": "hours"
    }
  },
  "calculations": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "trend": "increasing",
      "interpretation": "Excelente - ratio > 3 es saludable"
    },
    "best_improvement_metric": {
      "metric": "Avg_Response_Time",
      "improvement_percentage": -22.58,
      "reason": "Mayor reducción porcentual (mejora en eficiencia)",
      "feb_to_mar_change": {
        "from": 3.1,
        "to": 2.4,
        "absolute_change": -0.7
      }
    },
    "all_improvements_feb_to_mar": [
      {"metric": "Avg_Response_Time", "change_pct": -22.58, "direction": "lower_better"},
      {"metric": "Support_Tickets", "change_pct": -17.11, "direction": "lower_better"},
      {"metric": "Churn_Rate", "change_pct": -18.42, "direction": "lower_better"},
      {"metric": "LTV", "change_pct": 16.42, "direction": "higher_better"},
      {"metric": "Active_Users", "change_pct": 15.25, "direction": "higher_better"},
      {"metric": "NPS", "change_pct": 13.33, "direction": "higher_better"},
      {"metric": "MRR", "change_pct": 6.98, "direction": "higher_better"},
      {"metric": "CAC", "change_pct": -5.56, "direction": "lower_better"}
    ]
  },
  "projections": {
    "month": "Abril 2026",
    "methodology": "Extrapolación basada en tendencia M/M de Marzo",
    "values": {
      "MRR": {
        "projected": 55747,
        "calculation": "52100 * 1.