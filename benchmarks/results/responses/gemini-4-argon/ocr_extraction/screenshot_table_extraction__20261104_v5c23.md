# Gemini 4 Argon — ocr_extraction/screenshot_table_extraction

- model_id: `google/gemini-4-argon`
- success: True  | final: 6.95 | quality: 8.0
- latency_total: 22.619s | tokens_per_second: 62.7
- input_tokens: 426 | output_tokens: 1418

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
  "metadata": {
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
      "var_mm_texto": "+7.0%"
    },
    {
      "metrica": "Churn Rate",
      "unidad": "%",
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "var_mm_texto": "-0.7pp"
    },
    {
      "metrica": "NPS",
      "unidad": "puntos",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "var_mm_texto": "+6"
    },
    {
      "metrica": "CAC",
      "unidad": "USD",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "var_mm_texto": "-$11"
    },
    {
      "metrica": "LTV",
      "unidad": "USD",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "var_mm_texto": "+$330"
    },
    {
      "metrica": "Active Users",
      "unidad": "usuarios",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "var_mm_texto": "+15.3%"
    },
    {
      "metrica": "Support Tickets",
      "unidad": "tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "var_mm_texto": "-17.1%"
    },
    {
      "metrica": "Avg Response (h)",
      "unidad": "horas",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "var_mm_texto": "-0.7"
    }
  ],
  "analisis_adicional": {
    "1_ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "nota": "Calculado como LTV / CAC redondeado a 2 decimales."
    },
    "2_mayor_mejora_porcentual": {
      "comparativa_marzo_vs_febrero": {
        "metrica": "Avg Response (h)",
        "mejora_porcentual": "22.58%",
        "detalle": "Reducción de 3.1h a 2.4h (-22.58% en tiempo de respuesta, lo cual es una mejora)."
      },
      "comparativa_acumulada_trimestre": {
        "metrica": "Avg Response (h)",
        "mejora_porcentual": "42.86%",
        "detalle": "Reducción de 4.2h en Enero a 2.4h en Marzo."
      }
    },
    "3_proyeccion_abril": {
      "metodologia": "Se aplica la variación de la columna 'Var M/M' al valor de Marzo (manteniendo el tipo de variación: porcentual o lineal según cada métrica).",
      "metricas_proyectadas": {
        "MRR": {
          "valor": 55747,
          "formato_dashboard": "$55.7K",
          "calculo": "+7.0% sobre $52.1K"
        },
        "Churn Rate": {
          "valor": 2.4,
          "formato_dashboard": "2.4%",
          "calculo": "-0.7pp sobre 3.1%"
        },
        "NPS": {
          "valor": 57,
          "formato_dashboard": "57",
          "calculo": "+6 puntos sobre 51"
        },
        "CAC": {
          "valor": 176,
          "formato_dashboard": "$176",
          "calculo": "-$11 sobre $187"
        },
        "LTV": {
          "valor": 2670,
          "formato_dashboard": "$2,670",
          "calculo": "+$330 sobre $2,340"
        },
        "Active Users": {
          "valor": 1935,
          "formato_dashboard": "1,935",
          "calculo": "+15.3% sobre 1,678 (Nota: si fuera lineal serían 1,900 ya que sube exactamente 222/mes)"
        },
        "Support Tickets": {
          "valor": 52,
          "formato_dashboard": "52",
          "calculo": "-17.1% sobre 63 (Nota: si fuera lineal serían 50 ya que baja exactamente 13/mes)"
        },
        "Avg Response (h)": {
          "valor": 1.7,
          "formato_dashboard": "1.7",
          "calculo": "-0.7h sobre 2.4h"
        }
      }
    }
  }
}
```