# Kimi K2.7 Code — ocr_extraction/screenshot_table_extraction

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 4.75 | quality: 5.8
- latency_total: 366.951s | tokens_per_second: 18.7
- input_tokens: 386 | output_tokens: 6880
- judge_score: 3.2 | justificación: 

## Respuesta completa

 ```json
{
  "dashboard": {
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "metricas": [
      {
        "nombre": "MRR",
        "unidad": "$K",
        "enero": 45.2,
        "febrero": 48.7,
        "marzo": 52.1,
        "variacion_marzo": "+7.0%"
      },
      {
        "nombre": "Churn Rate",
        "unidad": "%",
        "enero": 4.2,
        "febrero": 3.8,
        "marzo": 3.1,
        "variacion_marzo": "-0.7pp"
      },
      {
        "nombre": "NPS",
        "unidad": "puntos",
        "enero": 42,
        "febrero": 45,
        "marzo": 51,
        "variacion_marzo": "+6"
      },
      {
        "nombre": "CAC",
        "unidad": "$",
        "enero": 234,
        "febrero": 198,
        "marzo": 187,
        "variacion_marzo": "-$11"
      },
      {
        "nombre": "LTV",
        "unidad": "$",
        "enero": 1890,
        "febrero": 2010,
        "marzo": 2340,
        "variacion_marzo": "+$330"
      },
      {
        "nombre": "Active Users",
        "unidad": "usuarios",
        "enero": 1234,
        "febrero": 1456,
        "marzo": 1678,
        "variacion_marzo": "+15.3%"
      },
      {
        "nombre": "Support Tickets",
        "unidad": "tickets",
        "enero": 89,
        "febrero": 76,
        "marzo": 63,
        "variacion_marzo": "-17.1%"
      },
      {
        "nombre": "Avg Response (h)",
        "unidad": "horas",
        "enero": 4.2,
        "febrero": 3.1,
        "marzo": 2.4,
        "variacion_marzo": "-0.7"
      }
    ]
  },
  "ltv_cac_ratio": {
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51
  },
  "mayor_mejora_porcentual": {
    "metrica": "Avg Response (h)",
    "cambio_porcentual_marzo_vs_febrero": "-22.58%",
    "nota": "Para métricas donde menor valor es mejor, el cambio negativo representa una mejora; es la mayor mejora relativa de marzo."
  },
  "proyeccion_abril": {
    "metodo": "Extrapolación lineal: promedio de los incrementos absolutos observados entre Ene→Feb y Feb→Mar",
    "valores": [
      {
        "metrica": "MRR",
        "valor": 55.55,
        "unidad": "$K"
      },
      {
        "metrica": "Churn Rate",
        "valor": 2.55,
        "unidad": "%"
      },
      {
        "metrica": "NPS",
        "valor": 55.5,
        "unidad": "puntos"
      },
      {
        "metrica": "CAC",
        "valor": 163.5,
        "unidad": "$"
      },
      {
        "metrica": "LTV",
        "valor": 2565,
        "unidad": "$"
      },
      {
        "metrica": "Active Users",
        "valor": 1900,
        "unidad": "usuarios"
      },
      {
        "metrica": "Support Tickets",
        "valor": 50,
        "unidad": "tickets"
      },
      {
        "metrica": "Avg Response (h)",
        "valor": 1.5,
        "unidad": "horas"
      }
    ],
    "ltv_cac_ratio_abril": 15.69
  }
}
```