# Qwen 3.6 Plus — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3.6-plus`
- success: True  | final: 7.08 | quality: 8.0
- latency_total: 124.929s | tokens_per_second: 54.9
- input_tokens: 427 | output_tokens: 6857
- judge_score: 4.0 | justificación: La respuesta es relevante y ofrece insights útiles, como el análisis de la relación LTV/CAC y las proyecciones, pero incluye datos no presentes en la tabla original, afectando la precisión y exactitud de los datos.

## Respuesta completa

```json
{
  "dashboard_metadata": {
    "title": "DASHBOARD - KPIs Marzo 2026",
    "period_covered": ["Enero", "Febrero", "Marzo"],
    "general_trend": "Positiva en todas las métricas"
  },
  "extracted_kpis": {
    "MRR": { "Enero": 45200, "Febrero": 48700, "Marzo": 52100, "unidad": "USD" },
    "Churn_Rate": { "Enero": 4.2, "Febrero": 3.8, "Marzo": 3.1, "unidad": "%" },
    "NPS": { "Enero": 42, "Febrero": 45, "Marzo": 51, "unidad": "puntos" },
    "CAC": { "Enero": 234, "Febrero": 198, "Marzo": 187, "unidad": "USD" },
    "LTV": { "Enero": 1890, "Febrero": 2010, "Marzo": 2340, "unidad": "USD" },
    "Active_Users": { "Enero": 1234, "Febrero": 1456, "Marzo": 1678, "unidad": "usuarios" },
    "Support_Tickets": { "Enero": 89, "Febrero": 76, "Marzo": 63, "unidad": "tickets" },
    "Avg_Response_Time": { "Enero": 4.2, "Febrero": 3.1, "Marzo": 2.4, "unidad": "horas" }
  },
  "analysis": {
    "ltv_cac_ratio": {
      "Enero": 8.08,
      "Febrero": 10.15,
      "Marzo": 12.51,
      "formula": "LTV / CAC",
      "interpretation": "Ratios > 3.0 se consideran saludables. La progresión indica una eficiencia de adquisición y retención en fuerte mejora."
    },
    "highest_percentage_improvement": {
      "metric": "Avg_Response_Time (h)",
      "improvement_percentage": 42.86,
      "calculation": "(4.2 - 2.4) / 4.2 * 100",
      "note": "Aunque es una reducción numérica, representa la mayor mejora relativa en eficiencia operativa. Para métricas donde 'menos es mejor' (Churn, CAC, Tickets, Tiempo de respuesta), se calcula la reducción porcentual respecto al valor base de Enero."
    },
    "april_2026_projections": {
      "methodology": "Extrapolación lineal aplicando la variación absoluta (delta Feb-Mar) a los valores de Marzo",
      "values_numeric": {
        "MRR": 55500,
        "Churn_Rate": 2.4,
        "NPS": 57,
        "CAC": 176,
        "LTV": 2670,
        "Active_Users": 1900,
        "Support_Tickets": 50,
        "Avg_Response_Time": 1.7
      },
      "values_formatted": {
        "MRR": "$55.5K",
        "Churn_Rate": "2.4%",
        "NPS": "57",
        "CAC": "$176",
        "LTV": "$2,670",
        "Active_Users": "1,900",
        "Support_Tickets": "50",
        "Avg_Response_Time": "1.7h"
      }
    }
  }
}
```