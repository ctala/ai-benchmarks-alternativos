# MiMo V2.5-Pro (Xiaomi) — ocr_extraction/screenshot_table_extraction

- model_id: `mimo-v2.5-pro`
- success: True  | final: 7.08 | quality: 7.08
- latency_total: 34.374s | tokens_per_second: 59.6
- input_tokens: 667 | output_tokens: 2048
- judge_score: 3.8 | justificación: 

## Respuesta completa

# Dashboard KPIs — Análisis Completo

```json
{
  "dashboard": "KPIs Marzo 2026",

  "datos_mensuales": {
    "enero": {
      "mrr": 45200,
      "churn_rate": 4.2,
      "nps": 42,
      "cac": 234,
      "ltv": 1890,
      "active_users": 1234,
      "support_tickets": 89,
      "avg_response_hours": 4.2
    },
    "febrero": {
      "mrr": 48700,
      "churn_rate": 3.8,
      "nps": 45,
      "cac": 198,
      "ltv": 2010,
      "active_users": 1456,
      "support_tickets": 76,
      "avg_response_hours": 3.1
    },
    "marzo": {
      "mrr": 52100,
      "churn_rate": 3.1,
      "nps": 51,
      "cac": 187,
      "ltv": 2340,
      "active_users": 1678,
      "support_tickets": 63,
      "avg_response_hours": 2.4
    }
  },

  "ltv_cac_ratio": {
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51,
    "variacion_enero_a_marzo": "+54.8%",
    "interpretacion": "Ratio saludable y en fuerte mejora. Por cada $1 invertido en adquisición, se generan $12.51 de valor de vida. El benchmark SaaS saludable está en 3:1, así que están muy por encima."
  },

  "metrica_mayor_mejora": {
    "metrica": "Avg Response Time",
    "valor_febrero": 3.1,
    "valor_marzo": 2.4,
    "cambio_porcentual": "-22.6%",
    "tipo_cambio": "reducción (mejora)",
    "ranking_mejoras_marzo": [
      { "posicion": 1, "metrica": "Avg Response Time", "cambio": "-22.6%" },
      { "posicion": 2, "metrica": "Support Tickets",    "cambio": "-17.1%" },
      { "posicion": 3, "metrica": "Active Users",       "cambio": "+15.3%" },
      { "posicion": 4, "metrica": "LTV/CAC Ratio",      "cambio": "+23.3%" },
      { "posicion": 5, "metrica": "MRR",                "cambio": "+7.0%" }
    ]
  },

  "proyeccion_abril": {
    "metodo": "Extrapolación lineal basada en la variación Feb→Mar",
    "valores": {
      "mrr":               { "valor": 55600,  "unidad": "USD",  "variacion": "+$3,500" },
      "churn_rate":        { "valor": 2.4,    "unidad": "%",    "variacion": "-0.7pp" },
      "nps":               { "valor": 57,     "unidad": "pts",  "variacion": "+6" },
      "cac":               { "valor": 176,    "unidad": "USD",  "variacion": "-$11" },
      "ltv":               { "valor": 2670,   "