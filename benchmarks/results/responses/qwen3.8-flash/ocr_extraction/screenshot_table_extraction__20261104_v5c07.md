# Qwen 3.8 Flash — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 9.0 | quality: 10.0
- latency_total: 16.818s | tokens_per_second: 58.8
- input_tokens: 442 | output_tokens: 989

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
  "extracted_data": [
    {
      "metrica": "MRR",
      "enero": "$45.2K",
      "febrero": "$48.7K",
      "marzo": "$52.1K",
      "var_m_m": "+7.0%"
    },
    {
      "metrica": "Churn Rate",
      "enero": "4.2%",
      "febrero": "3.8%",
      "marzo": "3.1%",
      "var_m_m": "-0.7pp"
    },
    {
      "metrica": "NPS",
      "enero": "42",
      "febrero": "45",
      "marzo": "51",
      "var_m_m": "+6"
    },
    {
      "metrica": "CAC",
      "enero": "$234",
      "febrero": "$198",
      "marzo": "$187",
      "var_m_m": "-$11"
    },
    {
      "metrica": "LTV",
      "enero": "$1,890",
      "febrero": "$2,010",
      "marzo": "$2,340",
      "var_m_m": "+$330"
    },
    {
      "metrica": "Active Users",
      "enero": "1,234",
      "febrero": "1,456",
      "marzo": "1,678",
      "var_m_m": "+15.3%"
    },
    {
      "metrica": "Support Tickets",
      "enero": "89",
      "febrero": "76",
      "marzo": "63",
      "var_m_m": "-17.1%"
    },
    {
      "metrica": "Avg Response (h)",
      "enero": "4.2",
      "febrero": "3.1",
      "marzo": "2.4",
      "var_m_m": "-0.7"
    }
  ],
  "analysis": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "note": "Calculated as LTV / CAC. Values rounded to two decimal places."
    },
    "best_improvement_metric": {
      "metric_name": "Support Tickets",
      "improvement_percentage": -17.1,
      "context": "La reducción del 17.1% en tickets de soporte representa la mayor mejora porcentual en eficiencia operativa entre las métricas con variación porcentual explícita o calculable. Si se considera la mejora absoluta en términos de impacto positivo para el negocio, 'Churn Rate' (-0.7pp) y 'Avg Response Time' (-0.7h) también son destacables, pero en porcentaje de cambio relativo, Support Tickets lidera."
    },
    "projection_april": {
      "methodology": "Linear extrapolation based on the average monthly growth/decline trend from Jan-Mar or applying the latest MoM change.",
      "values": {
        "MRR": "$55.5K",
        "Churn Rate": "2.4%",
        "NPS": "57",
        "CAC": "$176",
        "LTV": "$2,670",
        "Active Users": "1,900",
        "Support Tickets": "50",
        "Avg Response (h)": "1.7"
      },
      "notes": "Projections assume the continuation of the current positive trends. MRR grows by ~6.6% avg; Churn decreases by ~0.55pp avg; NPS increases by ~4.5 pts avg; CAC decreases by ~$11 avg; LTV increases by ~$225 avg; Active Users increase by ~15% avg; Support Tickets decrease by ~17% avg; Avg Response decreases by ~0.7h avg."
    }
  }
}
```