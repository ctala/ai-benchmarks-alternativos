# Muse Spark 1.3 — ocr_extraction/screenshot_table_extraction

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.49 | quality: 10.0
- latency_total: 11.725s | tokens_per_second: 300.1
- input_tokens: 362 | output_tokens: 3519

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
  "titulo": "DASHBOARD - KPIs Marzo 2026",
  "tendencia_general": "Positiva en todas las metricas",
  "datos_extraidos": [
    {
      "metrica": "MRR",
      "unidad": "USD",
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "var_mm": "+7.0%"
    },
    {
      "metrica": "Churn Rate",
      "unidad": "%",
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "var_mm": "-0.7pp"
    },
    {
      "metrica": "NPS",
      "unidad": "puntos",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "var_mm": "+6"
    },
    {
      "metrica": "CAC",
      "unidad": "USD",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "var_mm": "-11"
    },
    {
      "metrica": "LTV",
      "unidad": "USD",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "var_mm": "+330"
    },
    {
      "metrica": "Active Users",
      "unidad": "usuarios",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "var_mm": "+15.3%"
    },
    {
      "metrica": "Support Tickets",
      "unidad": "tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "var_mm": "-17.1%"
    },
    {
      "metrica": "Avg Response",
      "unidad": "horas",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "var_mm": "-0.7"
    }
  ],
  "ltv_cac_ratio": {
    "formula": "LTV / CAC",
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51,
    "detalle": [
      {
        "mes": "Enero",
        "calculo": "1890 / 234",
        "resultado": 8.08
      },
      {
        "mes": "Febrero",
        "calculo": "2010 / 198",
        "resultado": 10.15
      },
      {
        "mes": "Marzo",
        "calculo": "2340 / 187",
        "resultado": 12.51
      }
    ]
  },
  "mejora_porcentual_mm_feb_mar": [
    {
      "metrica": "MRR",
      "cambio_porcentual": 6.98,
      "es_mejora": true
    },
    {
      "metrica": "Churn Rate",
      "cambio_porcentual": -18.42,
      "es_mejora": true
    },
    {
      "metrica": "NPS",
      "cambio_porcentual": 13.33,
      "es_mejora": true
    },
    {
      "metrica": "CAC",
      "cambio_porcentual": -5.56,
      "es_mejora": true
    },
    {
      "metrica": "LTV",
      "cambio_porcentual": 16.42,
      "es_mejora": true
    },
    {
      "metrica": "Active Users",
      "cambio_porcentual": 15.25,
      "es_mejora": true
    },
    {
      "metrica": "Support Tickets",
      "cambio_porcentual": -17.11,
      "es_mejora": true
    },
    {
      "metrica": "Avg Response (h)",
      "cambio_porcentual": -22.58,
      "es_mejora": true
    }
  ],
  "metrica_mayor_mejora_porcentual": {
    "metrica": "Avg Response (h)",
    "cambio_porcentual_mm": -22.58,
    "mejora_porcentual_abs": 22.58,
    "valores": {
      "febrero": 3.1,
      "marzo": 2.4
    },
    "calculo": "(2.4 - 3.1) / 3.1 * 100 = -22.58%",
    "justificacion": "Es la mayor mejora porcentual M/M entre Febrero y Marzo. Al ser una metrica donde menor es mejor, la reduccion del 22.58% supera a Churn Rate (-18.42%), Support Tickets (-17.11%), LTV (+16.42%), Active Users (+15.25%), NPS (+13.33%), MRR (+6.98%) y CAC (-5.56%)."
  },
  "proyeccion_abril_2026": {
    "metodologia": "Se mantiene la misma variacion M/M de Marzo (absoluta para Churn, NPS, CAC, LTV, Avg Response y porcentual para MRR, Active Users, Support Tickets)",
    "valores_proyectados": [
      {
        "metrica": "MRR",
        "valor": 55747,
        "formato": "$55.7K",
        "calculo": "52100 * 1.07"
      },
      {
        "metrica": "Churn Rate",
        "valor": 2.4,
        "formato": "2.4%",
        "calculo": "3.1 - 0.7"
      },
      {
        "metrica": "NPS",
        "valor": 57,
        "formato": "57",
        "calculo": "51 + 6"
      },
      {
        "metrica": "CAC",
        "valor": 176,
        "formato": "$176",
        "calculo": "187 - 11"
      },
      {
        "metrica": "LTV",
        "valor": 2670,
        "formato": "$2670",
        "calculo": "2340 + 330"
      },
      {
        "metrica": "Active Users",
        "valor": 1935,
        "formato": "1935",
        "calculo": "1678 * 1.153"
      },
      {
        "metrica": "Support Tickets",
        "valor": 52,
        "formato": "52",
        "calculo": "63 * (1 - 0.171)"
      },
      {
        "metrica": "Avg Response (h)",
        "valor": 1.7,
        "formato": "1.7h",
        "calculo": "2.4 - 0.7"
      }
    ],
    "ltv_cac_ratio_proyectado_abril": 15.17
  }
}