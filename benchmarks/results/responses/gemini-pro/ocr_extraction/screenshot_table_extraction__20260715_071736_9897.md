# Gemini 2.5 Pro — ocr_extraction/screenshot_table_extraction

- model_id: `google/gemini-2.5-pro`
- success: True  | final: 6.84 | quality: 8.0
- latency_total: 45.361s | tokens_per_second: 118.3
- input_tokens: 418 | output_tokens: 5364
- judge_score: 3.0 | justificación: La respuesta incluye datos no presentes en la tabla original, afectando la precisión y exactitud de los datos, pero ofrece un análisis estructurado y relevante.

## Respuesta completa

Claro, aquí tienes los datos extraídos y los análisis solicitados en un formato JSON estructurado.

```json
{
  "resumen_dashboard": {
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "periodo_analizado": "Enero 2026 - Marzo 2026",
    "tendencia_general_observada": "Positiva en todas las métricas"
  },
  "datos_extraidos": [
    {
      "mes": "Enero",
      "metricas": {
        "MRR": { "valor": 45200, "unidad": "USD" },
        "Churn_Rate": { "valor": 4.2, "unidad": "%" },
        "NPS": { "valor": 42, "unidad": "puntos" },
        "CAC": { "valor": 234, "unidad": "USD" },
        "LTV": { "valor": 1890, "unidad": "USD" },
        "Active_Users": { "valor": 1234, "unidad": "usuarios" },
        "Support_Tickets": { "valor": 89, "unidad": "tickets" },
        "Avg_Response_h": { "valor": 4.2, "unidad": "horas" }
      }
    },
    {
      "mes": "Febrero",
      "metricas": {
        "MRR": { "valor": 48700, "unidad": "USD" },
        "Churn_Rate": { "valor": 3.8, "unidad": "%" },
        "NPS": { "valor": 45, "unidad": "puntos" },
        "CAC": { "valor": 198, "unidad": "USD" },
        "LTV": { "valor": 2010, "unidad": "USD" },
        "Active_Users": { "valor": 1456, "unidad": "usuarios" },
        "Support_Tickets": { "valor": 76, "unidad": "tickets" },
        "Avg_Response_h": { "valor": 3.1, "unidad": "horas" }
      }
    },
    {
      "mes": "Marzo",
      "metricas": {
        "MRR": { "valor": 52100, "unidad": "USD" },
        "Churn_Rate": { "valor": 3.1, "unidad": "%" },
        "NPS": { "valor": 51, "unidad": "puntos" },
        "CAC": { "valor": 187, "unidad": "USD" },
        "LTV": { "valor": 2340, "unidad": "USD" },
        "Active_Users": { "valor": 1678, "unidad": "usuarios" },
        "Support_Tickets": { "valor": 63, "unidad": "tickets" },
        "Avg_Response_h": { "valor": 2.4, "unidad": "horas" }
      }
    }
  ],
  "analisis_y_calculos": {
    "ltv_cac_ratio": {
      "descripcion": "Ratio que compara el Valor de Vida del Cliente (LTV) con el Costo de Adquisición de Cliente (CAC). Un ratio > 3 generalmente se considera saludable.",
      "valores_mensuales": [
        { "mes": "Enero", "valor": 8.08 },
        { "mes": "Febrero", "valor": 10.15 },
        { "mes": "Marzo", "valor": 12.51 }
      ]
    },
    "metrica_mayor_mejora_porcentual": {
      "descripcion": "Métrica con la mayor mejora porcentual en el último período (Febrero a Marzo). Una disminución en métricas como Churn, CAC, Tickets o Tiempo de Respuesta se considera una mejora.",
      "metrica": "Avg Response (h)",
      "variacion_porcentual": -22.6,
      "interpretacion": "El tiempo promedio de respuesta se redujo en un 22.6% de Febrero a Marzo, representando la mejora relativa más significativa de todas las KPIs."
    },
    "proyeccion_abril_2026": {
      "descripcion": "Proyección para Abril 2026 asumiendo que la tasa de cambio observada entre Febrero y Marzo se mantiene constante.",
      "metricas_proyectadas": {
        "MRR": { "valor": 55747, "unidad": "USD" },
        "Churn_Rate": { "valor": 2.4, "unidad": "%" },
        "NPS": { "valor": 57, "unidad": "puntos" },
        "CAC": { "valor": 176, "unidad": "USD" },
        "LTV": { "valor": 2670, "unidad": "USD" },
        "Active_Users": { "valor": 1934, "unidad": "usuarios" },
        "Support_Tickets": { "valor": 52, "unidad": "tickets" },
        "Avg_Response_h": { "valor": 1.7, "unidad": "horas" },
        "LTV_CAC_Ratio": { "valor": 15.17, "unidad": "ratio" }
      }
    }
  }
}
```