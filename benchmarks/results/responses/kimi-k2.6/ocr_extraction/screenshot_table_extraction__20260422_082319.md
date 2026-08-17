# Kimi K2.6 — ocr_extraction/screenshot_table_extraction

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 5.33 | quality: 5.8
- latency_total: 296.162s | tokens_per_second: 33.2
- input_tokens: 386 | output_tokens: 9836
- judge_score: 3.2 | justificación: 

## Respuesta completa

```json
{
  "dashboard": {
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "tendencia_general": "↑ Positiva en todas las metricas",
    "metricas": [
      {
        "nombre": "MRR",
        "enero": 45200,
        "febrero": 48700,
        "marzo": 52100,
        "unidad": "USD",
        "variacion_mes_a_mes": "+7.0%"
      },
      {
        "nombre": "Churn Rate",
        "enero": 4.2,
        "febrero": 3.8,
        "marzo": 3.1,
        "unidad": "%",
        "variacion_mes_a_mes": "-0.7pp"
      },
      {
        "nombre": "NPS",
        "enero": 42,
        "febrero": 45,
        "marzo": 51,
        "unidad": "puntos",
        "variacion_mes_a_mes": "+6"
      },
      {
        "nombre": "CAC",
        "enero": 234,
        "febrero": 198,
        "marzo": 187,
        "unidad": "USD",
        "variacion_mes_a_mes": "-$11"
      },
      {
        "nombre": "LTV",
        "enero": 1890,
        "febrero": 2010,
        "marzo": 2340,
        "unidad": "USD",
        "variacion_mes_a_mes": "+$330"
      },
      {
        "nombre": "Active Users",
        "enero": 1234,
        "febrero": 1456,
        "marzo": 1678,
        "unidad": "usuarios",
        "variacion_mes_a_mes": "+15.3%"
      },
      {
        "nombre": "Support Tickets",
        "enero": 89,
        "febrero": 76,
        "marzo": 63,
        "unidad": "tickets",
        "variacion_mes_a_mes": "-17.1%"
      },
      {
        "nombre": "Avg Response (h)",
        "enero": 4.2,
        "febrero": 3.1,
        "marzo": 2.4,
        "unidad": "horas",
        "variacion_mes_a_mes": "-0.7"
      }
    ]
  },
  "analisis": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "interpretacion": "La eficiencia de adquisición mejora consistentemente; el ratio supera 12x en marzo."
    },
    "metrica_con_mayor_mejora_porcentual": {
      "nombre": "Avg Response (h)",
      "valor_febrero": 3.1,
      "valor_marzo": 2.4,
      "cambio_porcentual": "-22.58%",
      "observacion": "Presenta la mayor mejora relativa mes a mes. Le siguen Churn Rate (-18.42%) y Support Tickets (-17.11%)."
    },
    "proyeccion_abril_2026": {
      "metodologia": "Se aplica la variación M/M observada (Marzo vs Febrero) sobre el valor de Marzo. Para métricas con variación porcentual en la tabla se usa el mismo %; para métricas con variación absoluta se usa el delta absoluto.",
      "valores": [
        {
          "nombre": "MRR",
          "valor_proyectado": 55747,
          "unidad": "USD",
          "detalle": "52100 * (1 + 0.070)"
        },
        {
          "nombre": "Churn Rate",
          "valor_proyectado": 2.4,
          "unidad": "%",
          "detalle": "3.1 - 0.7pp"
        },
        {
          "nombre": "NPS",
          "valor_proyectado": 57,
          "unidad": "puntos",
          "detalle": "51 + 6"
        },
        {
          "nombre": "CAC",
          "valor_proyectado": 176,
          "unidad": "USD",
          "detalle": "187 - 11"
        },
        {
          "nombre": "LTV",
          "valor_proyectado": 2670,
          "unidad": "USD",
          "detalle": "2340 + 330"
        },
        {
          "nombre": "Active Users",
          "valor_proyectado": 1935,
          "unidad": "usuarios",
          "detalle": "1678 * (1 + 0.153)"
        },
        {
          "nombre": "Support Tickets",
          "valor_proyectado": 52,
          "unidad": "tickets",
          "detalle": "63 * (1 - 0.171)"
        },
        {
          "nombre": "Avg Response (h)",
          "valor_proyectado": 1.7,
          "unidad": "horas",
          "detalle": "2.4 - 0.7"
        }
      ]
    }
  }
}
```