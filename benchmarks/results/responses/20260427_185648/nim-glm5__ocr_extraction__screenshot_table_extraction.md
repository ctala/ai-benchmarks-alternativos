# GLM 5 (NIM) — ocr_extraction/screenshot_table_extraction

- model_id: `z-ai/glm5`
- success: True  | final: 6.03 | quality: 5.8
- latency_total: 98.126s | tokens_per_second: 10.1
- input_tokens: 349 | output_tokens: 990
- judge_score: 3.2 | justificación: 

## Respuesta completa

```json
{
  "dashboard_data": {
    "title": "DASHBOARD - KPIs Marzo 2026",
    "trend": "Positiva en todas las metricas",
    "extracted_metrics": [
      {
        "metrica": "MRR",
        "Enero": "$45.2K",
        "Feb": "$48.7K",
        "Marzo": "$52.1K",
        "Var M/M": "+7.0%"
      },
      {
        "metrica": "Churn Rate",
        "Enero": "4.2%",
        "Feb": "3.8%",
        "Marzo": "3.1%",
        "Var M/M": "-0.7pp"
      },
      {
        "metrica": "NPS",
        "Enero": 42,
        "Feb": 45,
        "Marzo": 51,
        "Var M/M": "+6"
      },
      {
        "metrica": "CAC",
        "Enero": "$234",
        "Feb": "$198",
        "Marzo": "$187",
        "Var M/M": "-$11"
      },
      {
        "metrica": "LTV",
        "Enero": "$1,890",
        "Feb": "$2,010",
        "Marzo": "$2,340",
        "Var M/M": "+$330"
      },
      {
        "metrica": "Active Users",
        "Enero": 1234,
        "Feb": 1456,
        "Marzo": 1678,
        "Var M/M": "+15.3%"
      },
      {
        "metrica": "Support Tickets",
        "Enero": 89,
        "Feb": 76,
        "Marzo": 63,
        "Var M/M": "-17.1%"
      },
      {
        "metrica": "Avg Response (h)",
        "Enero": 4.2,
        "Feb": 3.1,
        "Marzo": 2.4,
        "Var M/M": "-0.7"
      }
    ]
  },
  "calculations": {
    "ltv_cac_ratio": {
      "Enero": 8.08,
      "Feb": 10.15,
      "Marzo": 12.51,
      "trend": "Mejora sostenida y acelerada"
    },
    "metrica_mayor_mejora_porcentual": {
      "metrica": "LTV",
      "mejora_porcentual": "+23.81%",
      "detalle": "El LTV pasó de $1,890 a $2,340, lo que representa un incremento del 23.81% respecto al mes anterior. Nota: El Churn Rate tuvo una caída porcentual del 18.42% (de 3.8% a 3.1%), pero al ser una tasa base pequeña, el impacto absoluto es menor comparado con el crecimiento del LTV."
    }
  },
  "proyeccion_abril": {
    "metodologia": "Proyección basada en la variación porcentual o absoluta constante del último mes (Feb->Marzo)",
    "metricas_proyectadas": {
      "MRR": {
        "valor": "$55,747",
        "calculo": "$52,100 * 1.07"
      },
      "Churn Rate": {
        "valor": "2.40%",
        "calculo": "3.1% - 0.7pp (asumiendo reducción constante de puntos porcentuales)"
      },
      "NPS": {
        "valor": 57,
        "calculo": "51 + 6"
      },
      "CAC": {
        "valor": "$176",
        "calculo": "$187 - $11"
      },
      "LTV": {
        "valor": "$2,670",
        "calculo": "$2,340 + $330"
      },
      "Active Users": {
        "valor": 1935,
        "calculo": "1678 * 1.153"
      },
      "Support Tickets": {
        "valor": 52,
        "calculo": "63 * (1 - 0.171)"
      },
      "Avg Response (h)": {
        "valor": 1.7,
        "calculo": "2.4 - 0.7"
      }
    },
    "ltv_cac_ratio_abril_proyectado": 15.17
  }
}
```