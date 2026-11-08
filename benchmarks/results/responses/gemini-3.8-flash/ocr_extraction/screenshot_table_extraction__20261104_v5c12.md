# Gemini 3.8 Flash — ocr_extraction/screenshot_table_extraction

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 7.15 | quality: 8.0
- latency_total: 20.543s | tokens_per_second: 140.0
- input_tokens: 418 | output_tokens: 2877

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
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "tendencia_general": "Positiva en todas las metricas"
  },
  "datos_extraidos": [
    {
      "metrica": "MRR",
      "enero": "$45.2K",
      "febrero": "$48.7K",
      "marzo": "$52.1K",
      "var_mm": "+7.0%"
    },
    {
      "metrica": "Churn Rate",
      "enero": "4.2%",
      "febrero": "3.8%",
      "marzo": "3.1%",
      "var_mm": "-0.7pp"
    },
    {
      "metrica": "NPS",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "var_mm": "+6"
    },
    {
      "metrica": "CAC",
      "enero": "$234",
      "febrero": "$198",
      "marzo": "$187",
      "var_mm": "-$11"
    },
    {
      "metrica": "LTV",
      "enero": "$1,890",
      "febrero": "$2,010",
      "marzo": "$2,340",
      "var_mm": "+$330"
    },
    {
      "metrica": "Active Users",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "var_mm": "+15.3%"
    },
    {
      "metrica": "Support Tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "var_mm": "-17.1%"
    },
    {
      "metrica": "Avg Response (h)",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "var_mm": "-0.7"
    }
  ],
  "analisis": {
    "ltv_cac_ratio": {
      "enero": {
        "formula": "$1,890 / $234",
        "ratio": 8.08
      },
      "febrero": {
        "formula": "$2,010 / $198",
        "ratio": 10.15
      },
      "marzo": {
        "formula": "$2,340 / $187",
        "ratio": 12.51
      }
    },
    "metrica_mayor_mejora_porcentual": {
      "metrica": "Avg Response (h)",
      "mejora_porcentual_mm": "22.58%",
      "detalle": "El tiempo promedio de respuesta se redujo de 3.1h a 2.4h (una reducción del 22.58%, siendo la mayor optimización relativa M/M). En métricas de crecimiento positivo, la mayor mejora fue LTV con +16.42% (+$330 sobre $2,010)."
    },
    "proyeccion_abril_2026": [
      {
        "metrica": "MRR",
        "valor_proyectado": "$55.7K",
        "metodo": "Tasa M/M (+6.98%)"
      },
      {
        "metrica": "Churn Rate",
        "valor_proyectado": "2.4%",
        "metodo": "Variación absoluta (-0.7pp)"
      },
      {
        "metrica": "NPS",
        "valor_proyectado": 57,
        "metodo": "Variación absoluta (+6 pts)"
      },
      {
        "metrica": "CAC",
        "valor_proyectado": "$176",
        "metodo": "Variación absoluta (-$11)"
      },
      {
        "metrica": "LTV",
        "valor_proyectado": "$2,670",
        "metodo": "Variación absoluta (+$330)"
      },
      {
        "metrica": "Active Users",
        "valor_proyectado": 1934,
        "metodo": "Tasa M/M (+15.25%)"
      },
      {
        "metrica": "Support Tickets",
        "valor_proyectado": 52,
        "metodo": "Tasa M/M (-17.11%)"
      },
      {
        "metrica": "Avg Response (h)",
        "valor_proyectado": 1.7,
        "metodo": "Variación absoluta (-0.7h)"
      }
    ]
  }
}
```