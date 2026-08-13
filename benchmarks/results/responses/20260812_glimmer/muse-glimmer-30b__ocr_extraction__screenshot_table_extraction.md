# Muse Glimmer 30B — ocr_extraction/screenshot_table_extraction

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 7.28 | quality: 8.0
- latency_total: 19.689s | tokens_per_second: 194.4
- input_tokens: 411 | output_tokens: 3828
- judge_score: 3.8 | justificación: 

## Respuesta completa

```json
{
  "dashboard": "DASHBOARD - KPIs Marzo 2026",
  "tendencia_general": "↑ Positiva en todas las metricas",
  "metricas": [
    {
      "nombre": "MRR",
      "unidad": "K USD",
      "Enero": 45.2,
      "Feb": 48.7,
      "Marzo": 52.1,
      "Var_M_M": "+7.0%"
    },
    {
      "nombre": "Churn Rate",
      "unidad": "%",
      "Enero": 4.2,
      "Feb": 3.8,
      "Marzo": 3.1,
      "Var_M_M": "-0.7pp"
    },
    {
      "nombre": "NPS",
      "unidad": "pts",
      "Enero": 42,
      "Feb": 45,
      "Marzo": 51,
      "Var_M_M": "+6"
    },
    {
      "nombre": "CAC",
      "unidad": "USD",
      "Enero": 234,
      "Feb": 198,
      "Marzo": 187,
      "Var_M_M": "-$11"
    },
    {
      "nombre": "LTV",
      "unidad": "USD",
      "Enero": 1890,
      "Feb": 2010,
      "Marzo": 2340,
      "Var_M_M": "+$330"
    },
    {
      "nombre": "Active Users",
      "unidad": "usuarios",
      "Enero": 1234,
      "Feb": 1456,
      "Marzo": 1678,
      "Var_M_M": "+15.3%"
    },
    {
      "nombre": "Support Tickets",
      "unidad": "tickets",
      "Enero": 89,
      "Feb": 76,
      "Marzo": 63,
      "Var_M_M": "-17.1%"
    },
    {
      "nombre": "Avg Response (h)",
      "unidad": "horas",
      "Enero": 4.2,
      "Feb": 3.1,
      "Marzo": 2.4,
      "Var_M_M": "-0.7"
    }
  ],
  "ltv_cac_ratio": {
    "Enero": 8.08,
    "Feb": 10.15,
    "Marzo": 12.51
  },
  "cambio_porcentual_feb_mar": {
    "MRR": 6.98,
    "Churn Rate": -18.42,
    "NPS": 13.33,
    "CAC": -5.56,
    "LTV": 16.42,
    "Active Users": 15.25,
    "Support Tickets": -17.11,
    "Avg Response (h)": -22.58
  },
  "metrica_mayor_mejora_porcentual": {
    "nombre": "Avg Response (h)",
    "cambio_porcentual_feb_mar": -22.58,
    "interpretacion": "mejora por reduccion",
    "nota": "Mayor mejora positiva en valor absoluto es LTV +16.42%. Entre metricas con Var M/M en % la mayor mejora es Support Tickets -17.1%"
  },
  "proyeccion_abril_mismo_delta_feb_mar": {
    "MRR": 55.7,
    "Churn Rate": 2.4,
    "NPS": 57,
    "CAC": 176,
    "LTV": 2670,
    "Active Users": 1935,
    "Support Tickets": 52,
    "Avg Response (h)": 1.7
  }
}
```

* LTV/CAC = LTV / CAC. Enero 1890/234 = 8.08, Feb 2010/198 = 10.15, Marzo 2340/187 = 12.51.
* La mayor mejora en magnitud porcentual Feb→Mar es Avg Response (h) -22.58%. La mayor mejora positiva es LTV +16.42%.
* Proyección Abril se mantiene el mismo delta Feb→Mar: % se aplica sobre Marzo, valores absolutos se suman/restan el mismo cambio.