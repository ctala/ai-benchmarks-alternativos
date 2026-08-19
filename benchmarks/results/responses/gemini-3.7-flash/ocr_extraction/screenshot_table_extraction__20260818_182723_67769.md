# Gemini 3.7 Flash — ocr_extraction/screenshot_table_extraction

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 7.31 | quality: 8.0
- latency_total: 17.169s | tokens_per_second: 154.1
- input_tokens: 418 | output_tokens: 2645

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
  "dashboard": {
    "titulo": "KPIs Marzo 2026",
    "tendencia_general": "Positiva en todas las metricas",
    "metricas": [
      {
        "metrica": "MRR",
        "enero": "$45.2K",
        "febrero": "$48.7K",
        "marzo": "$52.1K",
        "var_mom": "+7.0%"
      },
      {
        "metrica": "Churn Rate",
        "enero": "4.2%",
        "febrero": "3.8%",
        "marzo": "3.1%",
        "var_mom": "-0.7pp"
      },
      {
        "metrica": "NPS",
        "enero": 42,
        "febrero": 45,
        "marzo": 51,
        "var_mom": "+6"
      },
      {
        "metrica": "CAC",
        "enero": "$234",
        "febrero": "$198",
        "marzo": "$187",
        "var_mom": "-$11"
      },
      {
        "metrica": "LTV",
        "enero": "$1,890",
        "febrero": "$2,010",
        "marzo": "$2,340",
        "var_mom": "+$330"
      },
      {
        "metrica": "Active Users",
        "enero": 1234,
        "febrero": 1456,
        "marzo": 1678,
        "var_mom": "+15.3%"
      },
      {
        "metrica": "Support Tickets",
        "enero": 89,
        "febrero": 76,
        "marzo": 63,
        "var_mom": "-17.1%"
      },
      {
        "metrica": "Avg Response (h)",
        "enero": 4.2,
        "febrero": 3.1,
        "marzo": 2.4,
        "var_mom": "-0.7"
      }
    ]
  },
  "analisis_adicional": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "interpretacion": "Excelente salud financiera (ratio > 3:1), con incremento constante mes a mes."
    },
    "mayor_mejora_porcentual": {
      "metrica": "Avg Response (h)",
      "mejora_porcentual": "-22.58%",
      "descripcion": "El tiempo promedio de respuesta tuvo la mayor optimización relativa favorable (pasó de 3.1h a 2.4h). En métricas de crecimiento directo, la mayor alza fue LTV con +16.42% MoM."
    },
    "proyeccion_abril_2026": {
      "metodologia": "Proyección basada en la tendencia MoM (Febrero -> Marzo)",
      "valores_estimados": {
        "mrr": "$55.7K",
        "churn_rate": "2.4%",
        "nps": 57,
        "cac": "$176",
        "ltv": "$2,670",
        "active_users": 1934,
        "support_tickets": 52,
        "avg_response_h": 1.7
      }
    }
  }
}
```