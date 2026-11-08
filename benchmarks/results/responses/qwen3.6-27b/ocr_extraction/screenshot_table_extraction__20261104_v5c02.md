# Qwen 3.6 27B base (OpenRouter FP8) — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3.6-27b`
- success: True  | final: 7.26 | quality: 8.0
- latency_total: 18.97s | tokens_per_second: 74.9
- input_tokens: 429 | output_tokens: 1420

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
  "dashboard_info": {
    "title": "DASHBOARD - KPIs Marzo 2026",
    "period": "Marzo 2026"
  },
  "raw_data": [
    {
      "metrica": "MRR",
      "Enero": "$45.2K",
      "Feb": "$48.7K",
      "Marzo": "$52.1K",
      "Var_M/M": "+7.0%"
    },
    {
      "metrica": "Churn Rate",
      "Enero": "4.2%",
      "Feb": "3.8%",
      "Marzo": "3.1%",
      "Var_M/M": "-0.7pp"
    },
    {
      "metrica": "NPS",
      "Enero": 42,
      "Feb": 45,
      "Marzo": 51,
      "Var_M/M": "+6"
    },
    {
      "metrica": "CAC",
      "Enero": "$234",
      "Feb": "$198",
      "Marzo": "$187",
      "Var_M/M": "-$11"
    },
    {
      "metrica": "LTV",
      "Enero": "$1,890",
      "Feb": "$2,010",
      "Marzo": "$2,340",
      "Var_M/M": "+$330"
    },
    {
      "metrica": "Active Users",
      "Enero": 1234,
      "Feb": 1456,
      "Marzo": 1678,
      "Var_M/M": "+15.3%"
    },
    {
      "metrica": "Support Tickets",
      "Enero": 89,
      "Feb": 76,
      "Marzo": 63,
      "Var_M/M": "-17.1%"
    },
    {
      "metrica": "Avg Response (h)",
      "Enero": 4.2,
      "Feb": 3.1,
      "Marzo": 2.4,
      "Var_M/M": "-0.7"
    }
  ],
  "ltv_cac_ratio": {
    "Enero": {
      "value": 8.08,
      "calculation": "1890 / 234"
    },
    "Feb": {
      "value": 10.15,
      "calculation": "2010 / 198"
    },
    "Marzo": {
      "value": 12.51,
      "calculation": "2340 / 187"
    }
  },
  "mayor_mejora_porcentual": {
    "metrica": "Active Users",
    "valor_variacion": "+15.3%",
    "nota": "Es la mayor variación porcentual positiva entre las métricas con porcentaje explícito. Si se considera la reducción de Support Tickets (-17.1%) como mejora operativa, esta sería la mayor magnitud absoluta de cambio positivo en eficiencia."
  },
  "proyeccion_abril": {
    "metodologia": "Proyección lineal basada en la variación mes a mes (M/M) de Febrero a Marzo aplicada al valor de Marzo.",
    "datos_proyectados": [
      {
        "metrica": "MRR",
        "valor_marzo": 52100,
        "variacion_mm": 0.07,
        "valor_abril_proyectado": "$55.75K",
        "detalle": "52100 * 1.07"
      },
      {
        "metrica": "Churn Rate",
        "valor_marzo": 3.1,
        "variacion_pp": -0.7,
        "valor_abril_proyectado": "2.4%",
        "detalle": "3.1 - 0.7"
      },
      {
        "metrica": "NPS",
        "valor_marzo": 51,
        "variacion_absoluta": 6,
        "valor_abril_proyectado": 57,
        "detalle": "51 + 6"
      },
      {
        "metrica": "CAC",
        "valor_marzo": 187,
        "variacion_dolar": -11,
        "valor_abril_proyectado": "$176",
        "detalle": "187 - 11"
      },
      {
        "metrica": "LTV",
        "valor_marzo": 2340,
        "variacion_dolar": 330,
        "valor_abril_proyectado": "$2,670",
        "detalle": "2340 + 330"
      },
      {
        "metrica": "Active Users",
        "valor_marzo": 1678,
        "variacion_pct": 0.153,
        "valor_abril_proyectado": 1935,
        "detalle": "1678 * 1.153"
      },
      {
        "metrica": "Support Tickets",
        "valor_marzo": 63,
        "variacion_pct": -0.171,
        "valor_abril_proyectado": 52,
        "detalle": "63 * (1 - 0.171)"
      },
      {
        "metrica": "Avg Response (h)",
        "valor_marzo": 2.4,
        "variacion_horas": -0.7,
        "valor_abril_proyectado": "1.7 h",
        "detalle": "2.4 - 0.7"
      }
    ]
  }
}
```