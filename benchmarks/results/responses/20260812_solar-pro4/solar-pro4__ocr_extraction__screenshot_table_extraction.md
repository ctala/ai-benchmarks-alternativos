# Solar Pro 4 — ocr_extraction/screenshot_table_extraction

- model_id: `upstage/solar-pro4`
- success: True  | final: 9.25 | quality: 10.0
- latency_total: 8.158s | tokens_per_second: 97.8
- input_tokens: 450 | output_tokens: 798

## Respuesta completa

{
  "dashboard_info": {
    "title": "DASHBOARD - KPIs Marzo 2026",
    "period": "Marzo 2026",
    "trend_assessment": "Positiva en todas las metricas"
  },
  "metrics_raw": [
    {
      "metric": "MRR",
      "values": { "Enero": 45200, "Feb": 48700, "Marzo": 52100 },
      "var_mm_raw": "+7.0%"
    },
    {
      "metric": "Churn Rate",
      "values": { "Enero": 4.2, "Feb": 3.8, "Marzo": 3.1 },
      "var_mm_raw": "-0.7pp"
    },
    {
      "metric": "NPS",
      "values": { "Enero": 42, "Feb": 45, "Marzo": 51 },
      "var_mm_raw": "+6"
    },
    {
      "metric": "CAC",
      "values": { "Enero": 234, "Feb": 198, "Marzo": 187 },
      "var_mm_raw": "-$11"
    },
    {
      "metric": "LTV",
      "values": { "Enero": 1890, "Feb": 2010, "Marzo": 2340 },
      "var_mm_raw": "+$330"
    },
    {
      "metric": "Active Users",
      "values": { "Enero": 1234, "Feb": 1456, "Marzo": 1678 },
      "var_mm_raw": "+15.3%"
    },
    {
      "metric": "Support Tickets",
      "values": { "Enero": 89, "Feb": 76, "Marzo": 63 },
      "var_mm_raw": "-17.1%"
    },
    {
      "metric": "Avg Response (h)",
      "values": { "Enero": 4.2, "Feb": 3.1, "Marzo": 2.4 },
      "var_mm_raw": "-0.7"
    }
  ],
  "ltv_cac_ratio": {
    "Enero": 8.08,
    "Feb": 10.15,
    "Marzo": 12.51
  },
  "best_improvement": {
    "metric": "Support Tickets",
    "value": -17.1,
    "unit": "%",
    "note": "Mayor magnitud de mejora porcentual entre las metricas comparables (MRR +7.0%, Active Users +15.3%, Support Tickets -17.1%). Se interpreta como mejora por la reduccion de tickets."
  },
  "april_projection": {
    "methodology": "Proyeccion basada en la tasa de variacion mes a mes observada en Feb-Marzo, asumiendo mantenimiento de la tendencia.",
    "MRR": 55757,
    "Churn_Rate": 2.4,
    "NPS": 57,
    "CAC": 176,
    "LTV": 2670,
    "Active_Users": 1935,
    "Support_Tickets": 52,
    "Avg_Response_h": 1.7,
    "projected_LTV_CAC_ratio": 15.17
  }
}