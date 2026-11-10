# Muse Ember — ocr_extraction/screenshot_table_extraction

- model_id: `meta/muse-ember`
- success: True  | final: 7.53 | quality: 8.0
- latency_total: 7.052s | tokens_per_second: 674.2
- input_tokens: 363 | output_tokens: 4754

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
      "unidad": "USD",
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "variacion_mensual_reportada": "+7.0%"
    },
    {
      "metrica": "Churn Rate",
      "unidad": "%",
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "variacion_mensual_reportada": "-0.7pp"
    },
    {
      "metrica": "NPS",
      "unidad": "puntos",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "variacion_mensual_reportada": "+6"
    },
    {
      "metrica": "CAC",
      "unidad": "USD",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "variacion_mensual_reportada": "-$11"
    },
    {
      "metrica": "LTV",
      "unidad": "USD",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "variacion_mensual_reportada": "+$330"
    },
    {
      "metrica": "Active Users",
      "unidad": "usuarios",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "variacion_mensual_reportada": "+15.3%"
    },
    {
      "metrica": "Support Tickets",
      "unidad": "tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "variacion_mensual_reportada": "-17.1%"
    },
    {
      "metrica": "Avg Response (h)",
      "unidad": "horas",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "variacion_mensual_reportada": "-0.7"
    }
  ],
  "calculos": {
    "ltv_cac_ratio": {
      "formula": "LTV / CAC",
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "detalle": {
        "enero": "1890 / 234 = 8.0769",
        "febrero": "2010 / 198 = 10.1515",
        "marzo": "2340 / 187 = 12.5134"
      },
      "mejora_enero_marzo_porcentaje": 54.85
    },
    "metrica_mayor_mejora_porcentual": {
      "metrica": "Avg Response (h)",
      "mejora_mensual_feb_marzo_porcentaje": -22.58,
      "mejora_acumulada_enero_marzo_porcentaje": -42.86,
      "criterio": "Menor es mejor. Mejora calculada como variacion porcentual Feb->Mar, convirtiendo pp y valores absolutos a %",
      "ranking_mejora_mensual_porcentaje": [
        {
          "metrica": "Avg Response (h)",
          "mejora_porcentaje": 22.58
        },
        {
          "metrica": "Churn Rate",
          "mejora_porcentaje": 18.42
        },
        {
          "metrica": "Support Tickets",
          "mejora_porcentaje": 17.11
        },
        {
          "metrica": "LTV",
          "mejora_porcentaje": 16.42
        },
        {
          "metrica": "Active Users",
          "mejora_porcentaje": 15.25
        },
        {
          "metrica": "NPS",
          "mejora_porcentaje": 13.33
        },
        {
          "metrica": "MRR",
          "mejora_porcentaje": 6.98
        },
        {
          "metrica": "CAC",
          "mejora_porcentaje": 5.56
        }
      ]
    },
    "proyeccion_abril": {
      "metodologia": "Aplicando la variacion M/M Feb->Mar reportada a los valores de Marzo",
      "valores": {
        "MRR": 55747,
        "Churn Rate": 2.4,
        "NPS": 57,
        "CAC": 176,
        "LTV": 2670,
        "Active Users": 1935,
        "Support Tickets": 52,
        "Avg Response (h)": 1.7,
        "LTV/CAC ratio": 15.17
      },
      "detalle": {
        "MRR": "52100 * 1.07 = 55747",
        "Churn Rate": "3.1 - 0.7pp = 2.4%",
        "NPS": "51 + 6 = 57",
        "CAC": "187 - 11 = 176",
        "LTV": "2340 + 330 = 2670",
        "Active Users": "1678 * 1.153 = 1935",
        "Support Tickets": "63 * 0.829 = 52",
        "Avg Response (h)": "2.4 - 0.7 = 1.7",
        "LTV/CAC ratio": "2670 / 176 = 15.17"
      }
    }
  }
}
```