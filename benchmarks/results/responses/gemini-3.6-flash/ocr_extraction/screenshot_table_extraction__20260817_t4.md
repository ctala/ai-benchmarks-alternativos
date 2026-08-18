# Gemini 3.6 Flash — ocr_extraction/screenshot_table_extraction

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 7.15 | quality: 8.0
- latency_total: 12.831s | tokens_per_second: 230.9
- input_tokens: 418 | output_tokens: 2963

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

Aquí tienes la respuesta estructurada en formato JSON con la extracción de datos, los cálculos requeridos y la proyección para el mes de abril.

```json
{
  "dashboard_metadata": {
    "titulo": "KPIs Marzo 2026",
    "periodo_evaluado": "Enero - Marzo 2026",
    "tendencia_general": "Positiva"
  },
  "datos_extraidos": [
    {
      "metrica": "MRR",
      "enero": "$45.2K",
      "febrero": "$48.7K",
      "marzo": "$52.1K",
      "variacion_mensual": "+7.0%"
    },
    {
      "metrica": "Churn Rate",
      "enero": "4.2%",
      "febrero": "3.8%",
      "marzo": "3.1%",
      "variacion_mensual": "-0.7pp"
    },
    {
      "metrica": "NPS",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "variacion_mensual": "+6"
    },
    {
      "metrica": "CAC",
      "enero": "$234",
      "febrero": "$198",
      "marzo": "$187",
      "variacion_mensual": "-$11"
    },
    {
      "metrica": "LTV",
      "enero": "$1,890",
      "febrero": "$2,010",
      "marzo": "$2,340",
      "variacion_mensual": "+$330"
    },
    {
      "metrica": "Active Users",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "variacion_mensual": "+15.3%"
    },
    {
      "metrica": "Support Tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "variacion_mensual": "-17.1%"
    },
    {
      "metrica": "Avg Response (h)",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "variacion_mensual": "-0.7"
    }
  ],
  "analisis_adicional": {
    "1_ratio_ltv_cac": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "interpretacion": "El ratio mejora constantemente cada mes, mostrando mayor eficiencia en la adquisición y retención de valor por cliente."
    },
    "2_metrica_mayor_mejora_porcentual": {
      "metrica": "Avg Response (h)",
      "mejora_porcentual_relativa": "22.58%",
      "detalle": "El tiempo medio de respuesta se redujo de 3.1h a 2.4h entre febrero y marzo, lo que representa la mayor optimización en términos porcentuales absolutos."
    },
    "3_proyeccion_abril_2026": {
      "metodologia": "Aplicación de la variación MoM (Feb-Mar) a los datos de Marzo",
      "valores_proyectados": {
        "MRR": "$55.75K",
        "Churn Rate": "2.4%",
        "NPS": 57,
        "CAC": "$176",
        "LTV": "$2,670",
        "Active Users": 1934,
        "Support Tickets": 52,
        "Avg Response (h)": 1.7
      }
    }
  }
}
```