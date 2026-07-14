# DeepSeek V3 — ocr_extraction/screenshot_table_extraction

- model_id: `deepseek/deepseek-v3.2`
- success: True  | final: 8.75 | quality: 10.0
- latency_total: 33.544s | tokens_per_second: 29.5
- input_tokens: 386 | output_tokens: 988
- judge_score: 3.0 | justificación: 

## Respuesta completa

```json
{
  "datos_dashboard": {
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "metricas": [
      {
        "nombre": "MRR",
        "enero": 45200,
        "febrero": 48700,
        "marzo": 52100,
        "var_mes_anterior": "+7.0%"
      },
      {
        "nombre": "Churn Rate",
        "enero": 4.2,
        "febrero": 3.8,
        "marzo": 3.1,
        "var_mes_anterior": "-0.7pp"
      },
      {
        "nombre": "NPS",
        "enero": 42,
        "febrero": 45,
        "marzo": 51,
        "var_mes_anterior": "+6"
      },
      {
        "nombre": "CAC",
        "enero": 234,
        "febrero": 198,
        "marzo": 187,
        "var_mes_anterior": "-$11"
      },
      {
        "nombre": "LTV",
        "enero": 1890,
        "febrero": 2010,
        "marzo": 2340,
        "var_mes_anterior": "+$330"
      },
      {
        "nombre": "Active Users",
        "enero": 1234,
        "febrero": 1456,
        "marzo": 1678,
        "var_mes_anterior": "+15.3%"
      },
      {
        "nombre": "Support Tickets",
        "enero": 89,
        "febrero": 76,
        "marzo": 63,
        "var_mes_anterior": "-17.1%"
      },
      {
        "nombre": "Avg Response (h)",
        "enero": 4.2,
        "febrero": 3.1,
        "marzo": 2.4,
        "var_mes_anterior": "-0.7"
      }
    ],
    "tendencia_general": "↑ Positiva en todas las metricas"
  },
  "calculos": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51
    },
    "metrica_mayor_mejora_porcentual": {
      "nombre": "Support Tickets",
      "mejora_porcentual_marzo_vs_febrero": -17.1,
      "explicacion": "Support Tickets redujo un 17.1% de febrero a marzo, la mayor mejora porcentual (reducción) entre todas las métricas."
    }
  },
  "proyeccion_abril": {
    "suposicion": "Se mantiene el mismo cambio porcentual o absoluto observado de febrero a marzo",
    "metricas": [
      {
        "nombre": "MRR",
        "valor_proyectado": 55747.0,
        "cambio_aplicado": "+7.0%"
      },
      {
        "nombre": "Churn Rate",
        "valor_proyectado": 2.4,
        "cambio_aplicado": "-0.7pp"
      },
      {
        "nombre": "NPS",
        "valor_proyectado": 57,
        "cambio_aplicado": "+6"
      },
      {
        "nombre": "CAC",
        "valor_proyectado": 176,
        "cambio_aplicado": "-$11"
      },
      {
        "nombre": "LTV",
        "valor_proyectado": 2670,
        "cambio_aplicado": "+$330"
      },
      {
        "nombre": "Active Users",
        "valor_proyectado": 1935,
        "cambio_aplicado": "+15.3%"
      },
      {
        "nombre": "Support Tickets",
        "valor_proyectado": 52,
        "cambio_aplicado": "-17.1%"
      },
      {
        "nombre": "Avg Response (h)",
        "valor_proyectado": 1.7,
        "cambio_aplicado": "-0.7"
      }
    ],
    "ltv_cac_ratio_proyectado": 15.17
  }
}
```