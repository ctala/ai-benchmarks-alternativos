# GPT-6 Luna — ocr_extraction/screenshot_table_extraction

- model_id: `openai/gpt-6-luna`
- success: True  | final: 9.27 | quality: 10.0
- latency_total: 6.269s | tokens_per_second: 119.8
- input_tokens: 379 | output_tokens: 751

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

{
  "periodo": "Marzo 2026",
  "datos": [
    {
      "metrica": "MRR",
      "enero": "$45.2K",
      "febrero": "$48.7K",
      "marzo": "$52.1K",
      "variacion_mes_a_mes": "+7.0%"
    },
    {
      "metrica": "Churn Rate",
      "enero": "4.2%",
      "febrero": "3.8%",
      "marzo": "3.1%",
      "variacion_mes_a_mes": "-0.7pp"
    },
    {
      "metrica": "NPS",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "variacion_mes_a_mes": "+6"
    },
    {
      "metrica": "CAC",
      "enero": "$234",
      "febrero": "$198",
      "marzo": "$187",
      "variacion_mes_a_mes": "-$11"
    },
    {
      "metrica": "LTV",
      "enero": "$1,890",
      "febrero": "$2,010",
      "marzo": "$2,340",
      "variacion_mes_a_mes": "+$330"
    },
    {
      "metrica": "Active Users",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "variacion_mes_a_mes": "+15.3%"
    },
    {
      "metrica": "Support Tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "variacion_mes_a_mes": "-17.1%"
    },
    {
      "metrica": "Avg Response (h)",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "variacion_mes_a_mes": "-0.7"
    }
  ],
  "ltv_cac_ratio": {
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51
  },
  "mayor_mejora_porcentual": {
    "metrica": "Support Tickets",
    "mejora": "17.1% de reducción",
    "nota": "Es la mayor variación porcentual favorable entre las métricas con variación reportada. La comparación considera que una reducción de tickets es una mejora."
  },
  "proyecciones_abril": {
    "metodo": "Extrapolación lineal de la última variación mensual disponible; no se proporcionó una variación porcentual para todas las métricas.",
    "MRR": "$55.7K",
    "Churn Rate": "2.4%",
    "NPS": 57,
    "CAC": "$176",
    "LTV": "$2,670",
    "Active Users": 1935,
    "Support Tickets": 52,
    "Avg Response (h)": 1.7,
    "nota": "Para Active Users se aplicó +15.3% y para Support Tickets -17.1%; se redondeó al entero más cercano. Son estimaciones, no predicciones garantizadas."
  },
  "tendencia_general_reportada": "Positiva en todas las métricas"
}