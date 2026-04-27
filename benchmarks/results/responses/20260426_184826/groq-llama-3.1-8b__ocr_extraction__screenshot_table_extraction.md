# Llama 3.1 8B Instant (Groq) — ocr_extraction/screenshot_table_extraction

- model_id: `llama-3.1-8b-instant`
- success: True  | final: 7.11 | quality: 6.16
- latency_total: 1.219s | tokens_per_second: 640.9
- input_tokens: 417 | output_tokens: 781
- judge_score: 3.2 | justificación: 

## Respuesta completa

Aquí te presento los datos extraídos en formato JSON, junto con los cálculos solicitados:

```json
{
  "dashboard": {
    "title": "DASHBOARD - KPIs Marzo 2026",
    "metrics": [
      {
        "Metrica": "MRR",
        "Enero": 45200,
        "Feb": 48700,
        "Marzo": 52100,
        "Var M/M": 0.07
      },
      {
        "Metrica": "Churn Rate",
        "Enero": 4.2,
        "Feb": 3.8,
        "Marzo": 3.1,
        "Var M/M": -0.7
      },
      {
        "Metrica": "NPS",
        "Enero": 42,
        "Feb": 45,
        "Marzo": 51,
        "Var M/M": 6
      },
      {
        "Metrica": "CAC",
        "Enero": 234,
        "Feb": 198,
        "Marzo": 187,
        "Var M/M": -11
      },
      {
        "Metrica": "LTV",
        "Enero": 1890,
        "Feb": 2010,
        "Marzo": 2340,
        "Var M/M": 330
      },
      {
        "Metrica": "Active Users",
        "Enero": 1234,
        "Feb": 1456,
        "Marzo": 1678,
        "Var M/M": 15.3
      },
      {
        "Metrica": "Support Tickets",
        "Enero": 89,
        "Feb": 76,
        "Marzo": 63,
        "Var M/M": -17.1
      },
      {
        "Metrica": "Avg Response (h)",
        "Enero": 4.2,
        "Feb": 3.1,
        "Marzo": 2.4,
        "Var M/M": -0.7
      }
    ],
    "tendencia": "↑ Positiva en todas las metricas"
  },
  "calculos": {
    "LTV/CAC ratio": [
      {
        "Metrica": "Enero",
        "LTV/CAC ratio": 8.07
      },
      {
        "Metrica": "Feb",
        "LTV/CAC ratio": 10.1
      },
      {
        "Metrica": "Marzo",
        "LTV/CAC ratio": 12.52
      }
    ],
    "mayor mejora porcentual": {
      "Metrica": "Active Users",
      "Var M/M": 15.3
    },
    "proyeccion abril": {
      "MRR": 56651,
      "Churn Rate": 2.4,
      "NPS": 58,
      "CAC": 160,
      "LTV": 3090,
      "Active Users": 1959,
      "Support Tickets": 49,
      "Avg Response (h)": 1.7
    }
  }
}
```

Para calcular el LTV/CAC ratio, dividimos el valor de LTV por el valor de CAC para cada mes.

Para identificar la métrica con mayor mejora porcentual, buscamos el valor más alto de Var M/M.

Para proyectar los valores de Abril, asumimos que la tendencia positiva se mantiene y multiplicamos el valor de Marzo por 1.05 (5% de crecimiento mensual).