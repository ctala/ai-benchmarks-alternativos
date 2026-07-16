# MiniMax M2.7 — ocr_extraction/screenshot_table_extraction

- model_id: `minimax/minimax-m2.7`
- success: True  | final: 8.76 | quality: 10.0
- latency_total: 26.675s | tokens_per_second: 53.3
- input_tokens: 397 | output_tokens: 1422
- judge_score: 4.0 | justificación: La respuesta es relevante y ofrece insights útiles, pero contiene datos incorrectos (como el valor de CAC para marzo y la inclusión de métricas no presentes en la tabla original), afectando la precisión y exactitud de los datos.

## Respuesta completa

```json
{
  "dashboard_metadata": {
    "nombre": "KPIs Marzo 2026",
    "periodo": "Enero - Marzo 2026",
    "tendencia_general": "Positiva en todas las metricas"
  },
  "metricas": {
    "MRR": {
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "variacion_mes": "+7.0%",
      "tipo": "moneda"
    },
    "churn_rate": {
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "variacion_mes": "-0.7pp",
      "tipo": "porcentaje"
    },
    "NPS": {
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "variacion_mes": "+6",
      "tipo": "indice"
    },
    "CAC": {
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "variacion_mes": "-$11",
      "tipo": "moneda"
    },
    "LTV": {
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "variacion_mes": "+$330",
      "tipo": "moneda"
    },
    "active_users": {
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "variacion_mes": "+15.3%",
      "tipo": "cantidad"
    },
    "support_tickets": {
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "variacion_mes": "-17.1%",
      "tipo": "cantidad"
    },
    "avg_response_hours": {
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "variacion_mes": "-0.7",
      "tipo": "horas"
    }
  },
  "ltv_cac_ratio": {
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51,
    "tendencia": "mejorando"
  },
  "analisis": {
    "mayor_mejora_porcentual": {
      "metrica": "Support Tickets",
      "valor": "-17.1%",
      "nota": "Mejora maxima en porcentaje entre meses"
    },
    "metrica_destacada": "LTV/CAC Ratio",
    "interpretacion": "El ratio LTV/CAC mejoro de 8.08 a 12.51 (+54.8% en 3 meses), superando el benchmark saludable de 3.0x"
  },
  "proyecciones_abril": {
    "metodo": "tendencia_lineal",
    "MRR": 55747,
    "churn_rate": 2.4,
    "NPS": 57,
    "CAC": 176,
    "LTV": 2670,
    "active_users": 1935,
    "support_tickets": 52,
    "avg_response_hours": 1.7,
    "ltv_cac_ratio_proyectado": 15.17,
    "nota": "Proyecciones basadas en la variacion M/M observada"
  }
}
```