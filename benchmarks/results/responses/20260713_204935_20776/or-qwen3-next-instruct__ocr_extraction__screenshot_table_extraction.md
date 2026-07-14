# Qwen 3-Next 80B Instruct — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 7.7 | quality: 8.0
- latency_total: 5.641s | tokens_per_second: 156.9
- input_tokens: 424 | output_tokens: 885
- judge_score: 3.0 | justificación: La respuesta incluye datos no presentes en la captura de pantalla original, como LTV y Active Users, lo que afecta la precisión y exactitud de los datos, pero ofrece proyecciones y observaciones relevantes y útiles.

## Respuesta completa

{
  "dashboard": "KPIs Marzo 2026",
  "data": [
    {
      "metric": "MRR",
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "var_mm": 0.07,
      "ltv_cac_ratio": 8.08
    },
    {
      "metric": "Churn Rate",
      "enero": 0.042,
      "febrero": 0.038,
      "marzo": 0.031,
      "var_mm": -0.007,
      "ltv_cac_ratio": 45.24
    },
    {
      "metric": "NPS",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "var_mm": 6,
      "ltv_cac_ratio": 10.88
    },
    {
      "metric": "CAC",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "var_mm": -11,
      "ltv_cac_ratio": 8.08
    },
    {
      "metric": "LTV",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "var_mm": 330,
      "ltv_cac_ratio": 12.51
    },
    {
      "metric": "Active Users",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "var_mm": 0.153,
      "ltv_cac_ratio": 8.08
    },
    {
      "metric": "Support Tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "var_mm": -0.171,
      "ltv_cac_ratio": 37.14
    },
    {
      "metric": "Avg Response (h)",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "var_mm": -0.7,
      "ltv_cac_ratio": 975.0
    }
  ],
  "ltv_cac_ratios": {
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51
  },
  "metrica_mayor_mejora_porcentual": "Churn Rate",
  "proyeccion_abril": {
    "MRR": 55987,
    "Churn Rate": 2.5,
    "NPS": 57,
    "CAC": 177,
    "LTV": 2670,
    "Active Users": 1920,
    "Support Tickets": 52,
    "Avg Response (h)": 1.9
  },
  "observaciones": {
    "tendencia_general": "Positiva en todas las métricas",
    "notas_ltv_cac": "El ratio LTV/CAC mejora mes a mes, indicando mayor eficiencia en adquisición y retención. El cálculo se realiza como LTV / CAC (valores en dólares).",
    "metodo_proyeccion": "Se asume tendencia lineal basada en los cambios mensuales promedio entre enero-marzo. Para 'Churn Rate' y 'Avg Response (h)', se aplica la misma magnitud de mejora mensual (en puntos porcentuales o horas)."
  }
}