# Qwen 3.6 Plus — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3.6-plus`
- success: True  | final: 8.67 | quality: 10.0
- latency_total: 23.944s | tokens_per_second: 56.8
- input_tokens: 429 | output_tokens: 1360

## Entrada exacta (lo que recibió el modelo)

**user:**

Tengo una captura de pantalla de un dashboard de metricas. El contenido visible es:

DASHBOARD - KPIs Marzo 2026

+------------------+--------+--------+--------+---------+
| Metrica          | Enero  | Feb    | Marzo  | Var M/M |
+------------------+--------+--------+--------+---------+
| MRR              | $45.2K | $48.7K | $52.1K | +7.0%   |
| Churn Rate       | 4.2%   | 3.8%   | 3.1%   | -0.7pp  |
| NPS              | 42     | 45     | 51     | +6      |
| CAC              | $234   | $198   | $187   | -$11    |
| LTV              | $1,890 | $2,010 | $2,340 | +$330   |
| Active Users     | 1,234  | 1,456  | 1,678  | +15.3%  |
| Support Tickets  | 89     | 76     | 63     | -17.1%  |
| Avg Response (h) | 4.2    | 3.1    | 2.4    | -0.7    |
+------------------+--------+--------+--------+---------+

Tendencia general: ↑ Positiva en todas las metricas

Extrae los datos en formato JSON y ademas:
1. Calcula el LTV/CAC ratio para cada mes
2. Identifica la metrica con mayor mejora porcentual
3. Proyecta los valores de Abril si la tendencia se mantiene

Responde en JSON estructurado.


## Respuesta completa

```json
{
  "dashboard_metadata": {
    "title": "KPIs Marzo 2026",
    "trend_summary": "Positiva en todas las metricas"
  },
  "extracted_data": [
    {
      "metric": "MRR",
      "unit": "currency_k",
      "jan": 45200,
      "feb": 48700,
      "mar": 52100,
      "var_mom_pct": 7.0
    },
    {
      "metric": "Churn Rate",
      "unit": "percentage",
      "jan": 4.2,
      "feb": 3.8,
      "mar": 3.1,
      "var_mom_pp": -0.7
    },
    {
      "metric": "NPS",
      "unit": "score",
      "jan": 42,
      "feb": 45,
      "mar": 51,
      "var_mom_abs": 6
    },
    {
      "metric": "CAC",
      "unit": "currency",
      "jan": 234,
      "feb": 198,
      "mar": 187,
      "var_mom_abs": -11
    },
    {
      "metric": "LTV",
      "unit": "currency",
      "jan": 1890,
      "feb": 2010,
      "mar": 2340,
      "var_mom_abs": 330
    },
    {
      "metric": "Active Users",
      "unit": "count",
      "jan": 1234,
      "feb": 1456,
      "mar": 1678,
      "var_mom_pct": 15.3
    },
    {
      "metric": "Support Tickets",
      "unit": "count",
      "jan": 89,
      "feb": 76,
      "mar": 63,
      "var_mom_pct": -17.1
    },
    {
      "metric": "Avg Response (h)",
      "unit": "hours",
      "jan": 4.2,
      "feb": 3.1,
      "mar": 2.4,
      "var_mom_abs": -0.7
    }
  ],
  "analysis": {
    "ltv_cac_ratio": {
      "january": 8.08,
      "february": 10.15,
      "march": 12.51,
      "calculation_note": "Calculado como LTV / CAC para cada mes."
    },
    "biggest_percentage_improvement": {
      "metric": "Support Tickets",
      "improvement_pct": 17.1,
      "direction": "decrease_is_positive",
      "reasoning": "Aunque 'Active Users' creció un 15.3%, la reducción de tickets de soporte en un 17.1% representa la mayor variación porcentual relativa positiva en eficiencia/costo. Si se considera crecimiento puro, sería 'Active Users'. Dado que el dashboard marca tendencia positiva en todas, asumimos que bajar tickets es una mejora operativa mayor porcentualmente que el crecimiento de usuarios."
    },
    "april_projections": {
      "methodology": "Proyección lineal basada en el cambio absoluto promedio mensual (Enero->Febrero y Febrero->Marzo) o compuesto si es porcentual.",
      "projected_values": {
        "MRR": 55814,
        "Churn_Rate": 2.5,
        "NPS": 56,
        "CAC": 171,
        "LTV": 2595,
        "Active_Users": 1889,
        "Support_Tickets": 51,
        "Avg_Response_h": 1.8
      },
      "calculations_detail": {
        "MRR": "Tendencia de crecimiento acelerado. Promedio de crecimiento absoluto ~$3.4k. $52.1k + $3.7k (aceleración) ≈ $55.8k",
        "Churn_Rate": "Reducción de -0.4pp y -0.7pp. Proyección conservadora -0.6pp: 3.1 - 0.6 = 2.5%",
        "NPS": "+3 y +6. Tendencia acelerada. Proyección +5: 51 + 5 = 56",
        "CAC": "-$36 y -$11. Promedio de reducción -$23.5. Proyección conservadora -$16: 187 - 16 = 171",
        "LTV": "+$120 y +$330. Aceleración fuerte. Proyección +$255: 2340 + 255 = 2595",
        "Active_Users": "+222 y +222. Crecimiento lineal exacto. 1678 + 222 = 1900 (ajustado a 1889 por ligera desaceleración natural estimada)",
        "Support_Tickets": "-13 y -13. Reducción lineal exacta. 63 - 13 = 50 (ajustado a 51 por ley de rendimientos decrecientes)",
        "Avg_Response_h": "-1.1 y -0.7. Promedio -0.9. Proyección -0.6: 2.4 - 0.6 = 1.8h"
      }
    }
  }
}
```