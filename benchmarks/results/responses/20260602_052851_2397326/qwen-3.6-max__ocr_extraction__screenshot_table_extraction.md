# Qwen 3.6 Max — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3.6-max-preview`
- success: True  | final: 5.57 | quality: 6.72
- latency_total: 145.137s | tokens_per_second: 44.6
- input_tokens: 427 | output_tokens: 6479
- judge_score: 3.6 | justificación: 

## Respuesta completa

```json
{
  "dashboard_metadata": {
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "periodo": "Enero - Marzo 2026",
    "tendencia_general": "↑ Positiva en todas las métricas"
  },
  "datos_extraidos": [
    {"metrica": "MRR", "enero": "$45.2K", "febrero": "$48.7K", "marzo": "$52.1K", "var_mm": "+7.0%"},
    {"metrica": "Churn Rate", "enero": "4.2%", "febrero": "3.8%", "marzo": "3.1%", "var_mm": "-0.7pp"},
    {"metrica": "NPS", "enero": 42, "febrero": 45, "marzo": 51, "var_mm": "+6"},
    {"metrica": "CAC", "enero": "$234", "febrero": "$198", "marzo": "$187", "var_mm": "-$11"},
    {"metrica": "LTV", "enero": "$1,890", "febrero": "$2,010", "marzo": "$2,340", "var_mm": "+$330"},
    {"metrica": "Active Users", "enero": 1234, "febrero": 1456, "marzo": 1678, "var_mm": "+15.3%"},
    {"metrica": "Support Tickets", "enero": 89, "febrero": 76, "marzo": 63, "var_mm": "-17.1%"},
    {"metrica": "Avg Response (h)", "enero": 4.2, "febrero": 3.1, "marzo": 2.4, "var_mm": "-0.7"}
  ],
  "ltv_cac_ratio": {
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51,
    "formula_utilizada": "LTV / CAC",
    "interpretacion": "Un ratio >3 es saludable. La evolución de 8.08 a 12.51 indica una eficiencia de adquisición y retención en fuerte mejora."
  },
  "metrica_mayor_mejora_porcentual": {
    "metrica": "Avg Response (h)",
    "variacion_real_feb_mar_pct": -22.58,
    "nota_metodologica": "Se calculó el cambio porcentual real (Feb→Mar) para todas las métricas. Dado que para tiempos de respuesta, churn, CAC y tickets una reducción es positiva, esta métrica muestra la mayor mejora relativa (-22.6%). Si se considera únicamente crecimiento positivo, LTV lidera con +16.42%."
  },
  "proyeccion_abril": {
    "metodologia": "Se aplicó la tasa de variación Mes-a-Mes (Feb→Mar) de cada métrica sobre el valor de Marzo, asumiendo que la tendencia se mantiene linealmente.",
    "valores_proyectados": {
      "MRR": "$55.7K",
      "Churn Rate": "2.5%",
      "NPS": 58,
      "CAC": "$177",
      "LTV": "$2,724",
      "Active Users": 1934,
      "Support Tickets": 52,
      "Avg Response (h)": 1.9
    },
    "advertencia": "Proyección puramente matemática basada en inercia reciente. Factores estacionales, capacidad operativa o saturación de mercado pueden alterar los resultados reales."
  }
}
```