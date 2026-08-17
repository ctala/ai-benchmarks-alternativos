# GPT-5.5 — ocr_extraction/screenshot_table_extraction

- model_id: `gpt-5.5`
- success: True  | final: 5.82 | quality: 6.64
- latency_total: 18.101s | tokens_per_second: 100.6
- input_tokens: 379 | output_tokens: 1821
- judge_score: 3.8 | justificación: 

## Respuesta completa

{
  "titulo": "DASHBOARD - KPIs Marzo 2026",
  "periodo": "Marzo 2026",
  "datos": [
    {
      "metrica": "MRR",
      "unidad": "USD_K",
      "enero": 45.2,
      "febrero": 48.7,
      "marzo": 52.1,
      "variacion_mom": {
        "valor": 7.0,
        "unidad": "%"
      }
    },
    {
      "metrica": "Churn Rate",
      "unidad": "%",
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "variacion_mom": {
        "valor": -0.7,
        "unidad": "pp"
      }
    },
    {
      "metrica": "NPS",
      "unidad": "puntos",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "variacion_mom": {
        "valor": 6,
        "unidad": "puntos"
      }
    },
    {
      "metrica": "CAC",
      "unidad": "USD",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "variacion_mom": {
        "valor": -11,
        "unidad": "USD"
      }
    },
    {
      "metrica": "LTV",
      "unidad": "USD",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "variacion_mom": {
        "valor": 330,
        "unidad": "USD"
      }
    },
    {
      "metrica": "Active Users",
      "unidad": "usuarios",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "variacion_mom": {
        "valor": 15.3,
        "unidad": "%"
      }
    },
    {
      "metrica": "Support Tickets",
      "unidad": "tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "variacion_mom": {
        "valor": -17.1,
        "unidad": "%"
      }
    },
    {
      "metrica": "Avg Response",
      "unidad": "horas",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "variacion_mom": {
        "valor": -0.7,
        "unidad": "horas"
      }
    }
  ],
  "calculos": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51
    },
    "mayor_mejora_porcentual": {
      "metrica": "Avg Response",
      "periodo_comparado": "Febrero a Marzo",
      "valor_febrero": 3.1,
      "valor_marzo": 2.4,
      "mejora_porcentual": 22.58,
      "unidad": "%",
      "criterio": "Menor tiempo de respuesta es mejor"
    }
  },
  "proyeccion_abril": {
    "supuesto": "Se mantiene la misma variacion mensual observada de Febrero a Marzo",
    "valores": [
      {
        "metrica": "MRR",
        "marzo": 52.1,
        "abril_proyectado": 55.75,
        "unidad": "USD_K",
        "metodo": "Marzo * 1.07"
      },
      {
        "metrica": "Churn Rate",
        "marzo": 3.1,
        "abril_proyectado": 2.4,
        "unidad": "%",
        "metodo": "Marzo - 0.7pp"
      },
      {
        "metrica": "NPS",
        "marzo": 51,
        "abril_proyectado": 57,
        "unidad": "puntos",
        "metodo": "Marzo + 6"
      },
      {
        "metrica": "CAC",
        "marzo": 187,
        "abril_proyectado": 176,
        "unidad": "USD",
        "metodo": "Marzo - 11"
      },
      {
        "metrica": "LTV",
        "marzo": 2340,
        "abril_proyectado": 2670,
        "unidad": "USD",
        "metodo": "Marzo + 330"
      },
      {
        "metrica": "Active Users",
        "marzo": 1678,
        "abril_proyectado": 1935,
        "unidad": "usuarios",
        "metodo": "Marzo * 1.153"
      },
      {
        "metrica": "Support Tickets",
        "marzo": 63,
        "abril_proyectado": 52,
        "unidad": "tickets",
        "metodo": "Marzo * 0.829"
      },
      {
        "metrica": "Avg Response",
        "marzo": 2.4,
        "abril_proyectado": 1.7,
        "unidad": "horas",
        "metodo": "Marzo - 0.7"
      }
    ],
    "ltv_cac_ratio_abril_proyectado": 15.17
  },
  "tendencia_general": {
    "direccion": "positiva",
    "descripcion": "Todas las metricas muestran mejora: crecimiento en MRR, NPS, LTV y usuarios activos; reduccion en churn, CAC, tickets de soporte y tiempo promedio de respuesta."
  }
}