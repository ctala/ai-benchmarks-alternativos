# Gemini 3.8 Flash — ocr_extraction/screenshot_table_extraction

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 7.12 | quality: 8.0
- latency_total: 22.279s | tokens_per_second: 156.8
- input_tokens: 418 | output_tokens: 3494

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
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "tendencia_general": "Positiva en todas las metricas"
  },
  "datos_extraidos": [
    {
      "metrica": "MRR",
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "unidad": "USD",
      "variacion_mm": "+7.0%"
    },
    {
      "metrica": "Churn Rate",
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "unidad": "%",
      "variacion_mm": "-0.7pp"
    },
    {
      "metrica": "NPS",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "unidad": "puntos",
      "variacion_mm": "+6"
    },
    {
      "metrica": "CAC",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "unidad": "USD",
      "variacion_mm": "-$11"
    },
    {
      "metrica": "LTV",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "unidad": "USD",
      "variacion_mm": "+$330"
    },
    {
      "metrica": "Active Users",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "unidad": "usuarios",
      "variacion_mm": "+15.3%"
    },
    {
      "metrica": "Support Tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "unidad": "tickets",
      "variacion_mm": "-17.1%"
    },
    {
      "metrica": "Avg Response (h)",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "unidad": "horas",
      "variacion_mm": "-0.7"
    }
  ],
  "analisis": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "interpretacion": "El ratio muestra un crecimiento sostenido y muy saludable (>3x considerado optimo)."
    },
    "metrica_mayor_mejora_porcentual": {
      "metrica": "Avg Response (h)",
      "mejora_porcentual": "22.58%",
      "tipo_mejora": "Reduccion de tiempo de respuesta (de 3.1h a 2.4h)",
      "segundo_lugar": "Churn Rate con 18.42% de reduccion relativa (de 3.8% a 3.1%)",
      "mayor_crecimiento_positivo": "LTV con +16.42% de incremento"
    },
    "proyecciones_abril_2026": {
      "metodo": "Extrapolacion basada en la variacion mes a mes (M/M) reportada de Marzo",
      "valores": {
        "MRR": {
          "valor_estimado": 55747,
          "formato": "$55.7K",
          "calculo": "+7.0% sobre Marzo"
        },
        "Churn Rate": {
          "valor_estimado": 2.4,
          "formato": "2.4%",
          "calculo": "-0.7 pp sobre Marzo"
        },
        "NPS": {
          "valor_estimado": 57,
          "formato": "57",
          "calculo": "+6 puntos sobre Marzo"
        },
        "CAC": {
          "valor_estimado": 176,
          "formato": "$176",
          "calculo": "-$11 sobre Marzo"
        },
        "LTV": {
          "valor_estimado": 2670,
          "formato": "$2,670",
          "calculo": "+$330 sobre Marzo"
        },
        "Active Users": {
          "valor_estimado": 1935,
          "formato": "1,935",
          "calculo": "+15.3% sobre Marzo"
        },
        "Support Tickets": {
          "valor_estimado": 52,
          "formato": "52",
          "calculo": "-17.1% sobre Marzo"
        },
        "Avg Response (h)": {
          "valor_estimado": 1.7,
          "formato": "1.7 h",
          "calculo": "-0.7 h sobre Marzo"
        }
      },
      "ltv_cac_ratio_proyectado": 15.17
    }
  }
}
```