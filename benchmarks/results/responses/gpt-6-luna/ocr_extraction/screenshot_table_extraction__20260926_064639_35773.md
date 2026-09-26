# GPT-6 Luna — ocr_extraction/screenshot_table_extraction

- model_id: `openai/gpt-6-luna`
- success: True  | final: 9.04 | quality: 10.0
- latency_total: 12.0s | tokens_per_second: 145.7
- input_tokens: 379 | output_tokens: 1748

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
  "titulo": "Dashboard - KPIs Marzo 2026",
  "datos": [
    {
      "metrica": "MRR",
      "unidad": "USD",
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "variacion_mom_reportada": "+7.0%"
    },
    {
      "metrica": "Churn Rate",
      "unidad": "%",
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "variacion_mom_reportada": "-0.7 pp"
    },
    {
      "metrica": "NPS",
      "unidad": "puntos",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "variacion_mom_reportada": "+6"
    },
    {
      "metrica": "CAC",
      "unidad": "USD",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "variacion_mom_reportada": "-$11"
    },
    {
      "metrica": "LTV",
      "unidad": "USD",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "variacion_mom_reportada": "+$330"
    },
    {
      "metrica": "Active Users",
      "unidad": "usuarios",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "variacion_mom_reportada": "+15.3%"
    },
    {
      "metrica": "Support Tickets",
      "unidad": "tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "variacion_mom_reportada": "-17.1%"
    },
    {
      "metrica": "Avg Response",
      "unidad": "horas",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "variacion_mom_reportada": "-0.7"
    }
  ],
  "ltv_cac_ratio": {
    "formula": "LTV / CAC",
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51
  },
  "mayor_mejora_porcentual": {
    "metrica": "Avg Response",
    "cambio_febrero_a_marzo": "-22.6%",
    "interpretacion": "El tiempo de respuesta disminuyó un 22.6%, la mayor mejora porcentual favorable entre las métricas."
  },
  "proyeccion_abril": {
    "metodo": "Se extiende a abril el cambio absoluto observado entre febrero y marzo.",
    "valores": [
      {
        "metrica": "MRR",
        "valor": 55500,
        "unidad": "USD"
      },
      {
        "metrica": "Churn Rate",
        "valor": 2.4,
        "unidad": "%"
      },
      {
        "metrica": "NPS",
        "valor": 57,
        "unidad": "puntos"
      },
      {
        "metrica": "CAC",
        "valor": 176,
        "unidad": "USD"
      },
      {
        "metrica": "LTV",
        "valor": 2670,
        "unidad": "USD"
      },
      {
        "metrica": "Active Users",
        "valor": 1900,
        "unidad": "usuarios"
      },
      {
        "metrica": "Support Tickets",
        "valor": 50,
        "unidad": "tickets"
      },
      {
        "metrica": "Avg Response",
        "valor": 1.7,
        "unidad": "horas"
      }
    ],
    "ltv_cac_ratio_proyectado": 15.17
  },
  "tendencia_general_reportada": "Positiva en todas las métricas"
}