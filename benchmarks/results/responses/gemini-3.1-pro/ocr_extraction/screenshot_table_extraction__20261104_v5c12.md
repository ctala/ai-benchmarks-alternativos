# Gemini 3.1 Pro — ocr_extraction/screenshot_table_extraction

- model_id: `google/gemini-3.1-pro-preview`
- success: True  | final: 6.84 | quality: 8.0
- latency_total: 41.557s | tokens_per_second: 109.9
- input_tokens: 418 | output_tokens: 4569

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
    "tendencia_general": "Positiva en todas las metricas"
  },
  "datos_extraidos": [
    {
      "metrica": "MRR",
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "variacion_mensual": "+7.0%",
      "unidad": "USD"
    },
    {
      "metrica": "Churn Rate",
      "enero": 0.042,
      "febrero": 0.038,
      "marzo": 0.031,
      "variacion_mensual": "-0.7pp",
      "unidad": "Porcentaje"
    },
    {
      "metrica": "NPS",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "variacion_mensual": "+6",
      "unidad": "Puntos"
    },
    {
      "metrica": "CAC",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "variacion_mensual": "-$11",
      "unidad": "USD"
    },
    {
      "metrica": "LTV",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "variacion_mensual": "+$330",
      "unidad": "USD"
    },
    {
      "metrica": "Active Users",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "variacion_mensual": "+15.3%",
      "unidad": "Usuarios"
    },
    {
      "metrica": "Support Tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "variacion_mensual": "-17.1%",
      "unidad": "Tickets"
    },
    {
      "metrica": "Avg Response (h)",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "variacion_mensual": "-0.7",
      "unidad": "Horas"
    }
  ],
  "analisis_solicitado": {
    "1_ratio_ltv_cac": {
      "descripcion": "Relación entre el Valor del Ciclo de Vida del Cliente (LTV) y el Costo de Adquisición (CAC)",
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51
    },
    "2_mayor_mejora_porcentual": {
      "metrica": "Avg Response (h)",
      "mejora_porcentual": "22.58%",
      "explicacion": "El tiempo de respuesta bajó de 3.1h a 2.4h, lo que representa una mejora relativa del 22.58% de febrero a marzo (la mayor entre todas las métricas)."
    },
    "3_proyeccion_abril": {
      "descripcion": "Proyección calculada aplicando la Variación M/M del tablero a los valores de Marzo.",
      "proyecciones": {
        "MRR": {
          "valor_proyectado": 55747,
          "formato": "$55.7K",
          "calculo": "52.1K * 1.07"
        },
        "Churn Rate": {
          "valor_proyectado": 0.024,
          "formato": "2.4%",
          "calculo": "3.1% - 0.7pp"
        },
        "NPS": {
          "valor_proyectado": 57,
          "formato": "57",
          "calculo": "51 + 6"
        },
        "CAC": {
          "valor_proyectado": 176,
          "formato": "$176",
          "calculo": "187 - 11"
        },
        "LTV": {
          "valor_proyectado": 2670,
          "formato": "$2,670",
          "calculo": "2340 + 330"
        },
        "Active Users": {
          "valor_proyectado": 1935,
          "formato": "1,935",
          "calculo": "1678 * 1.153 (redondeado)"
        },
        "Support Tickets": {
          "valor_proyectado": 52,
          "formato": "52",
          "calculo": "63 * (1 - 0.171) (redondeado)"
        },
        "Avg Response (h)": {
          "valor_proyectado": 1.7,
          "formato": "1.7",
          "calculo": "2.4 - 0.7"
        }
      }
    }
  }
}
```