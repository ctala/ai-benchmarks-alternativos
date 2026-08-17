# GLM-5.1 — ocr_extraction/screenshot_table_extraction

- model_id: `z-ai/glm-5.1`
- success: True  | final: 6.8 | quality: 8.0
- latency_total: 123.609s | tokens_per_second: 37.5
- input_tokens: 388 | output_tokens: 4630
- judge_score: 3.0 | justificación: La respuesta incluye datos extraídos correctamente de la tabla, pero introduce métricas no presentes en la captura de pantalla original, afectando la precisión. Ofrece proyecciones y cálculos útiles, pero la exactitud de los datos es comprometida por la inclusión de métricas inexistentes.

## Respuesta completa

```json
{
  "dashboard_data": {
    "title": "DASHBOARD - KPIs Marzo 2026",
    "general_trend": "Positiva en todas las metricas",
    "metrics": [
      {
        "name": "MRR",
        "enero": "$45.2K",
        "febrero": "$48.7K",
        "marzo": "$52.1K",
        "var_mm": "+7.0%"
      },
      {
        "name": "Churn Rate",
        "enero": "4.2%",
        "febrero": "3.8%",
        "marzo": "3.1%",
        "var_mm": "-0.7pp"
      },
      {
        "name": "NPS",
        "enero": 42,
        "febrero": 45,
        "marzo": 51,
        "var_mm": "+6"
      },
      {
        "name": "CAC",
        "enero": "$234",
        "febrero": "$198",
        "marzo": "$187",
        "var_mm": "-$11"
      },
      {
        "name": "LTV",
        "enero": "$1,890",
        "febrero": "$2,010",
        "marzo": "$2,340",
        "var_mm": "+$330"
      },
      {
        "name": "Active Users",
        "enero": 1234,
        "febrero": 1456,
        "marzo": 1678,
        "var_mm": "+15.3%"
      },
      {
        "name": "Support Tickets",
        "enero": 89,
        "febrero": 76,
        "marzo": 63,
        "var_mm": "-17.1%"
      },
      {
        "name": "Avg Response (h)",
        "enero": 4.2,
        "febrero": 3.1,
        "marzo": 2.4,
        "var_mm": "-0.7"
      }
    ]
  },
  "ltv_cac_ratio": {
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51,
    "note": "Calculado como LTV / CAC para cada mes. Ej: 1890 / 234 = 8.08"
  },
  "highest_improvement_metric": {
    "metric": "Avg Response (h)",
    "improvement_percentage": -22.58,
    "explanation": "Se calculó la variación porcentual M/M de todas las métricas. Una disminución en el tiempo de respuesta es una mejora. (2.4 - 3.1) / 3.1 = -22.58%, lo cual supera en magnitud a la mejora de Active Users (+15.3%) y Support Tickets (-17.1%)."
  },
  "april_projections": {
    "methodology": "Proyección basada en el promedio de la variación absoluta mensual histórica (Ene-Feb y Feb-Mar) aplicada al valor de Marzo.",
    "projections": {
      "MRR": "$55.6K",
      "Churn Rate": "2.55%",
      "NPS": 56,
      "CAC": "$164",
      "LTV": "$2,565",
      "Active Users": 1900,
      "Support Tickets": 50,
      "Avg Response (h)": 1.5
    },
    "calculation_details": {
      "MRR": "52.1 + ((48.7-45.2) + (52.1-48.7))/2 = 52.1 + 3.45 = 55.55 ≈ $55.6K",
      "Churn_Rate": "3.1 + ((3.8-4.2) + (3.1-3.8))/2 = 3.1 - 0.55 = 2.55%",
      "NPS": "51 + ((45-42) + (51-45))/2 = 51 + 4.5 = 55.5 ≈ 56",
      "CAC": "187 + ((198-234) + (187-198))/2 = 187 - 23.5 = 163.5 ≈ $164",
      "LTV": "2340 + ((2010-1890) + (2340-2010))/2 = 2340 + 225 = $2,565",
      "Active_Users": "1678 + ((1456-1234) + (1678-1456))/2 = 1678 + 222 = 1900",
      "Support_Tickets": "63 + ((76-89) + (63-76))/2 = 63 - 13 = 50",
      "Avg_Response": "2.4 + ((3.1-4.2) + (2.4-3.1))/2 = 2.4 - 0.9 = 1.5"
    }
  }
}
```