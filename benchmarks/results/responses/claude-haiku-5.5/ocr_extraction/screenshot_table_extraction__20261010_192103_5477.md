# Claude Haiku 5.5 — ocr_extraction/screenshot_table_extraction

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.93 | quality: 10.0
- latency_total: 13.111s | tokens_per_second: 245.4
- input_tokens: 514 | output_tokens: 3217

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
  "dashboard": "KPIs Marzo 2026",
  "datos": {
    "MRR": {
      "unidad": "USD",
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "variacion_mm": {"valor": 7.0, "unidad": "%"}
    },
    "churn_rate": {
      "unidad": "%",
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "variacion_mm": {"valor": -0.7, "unidad": "pp"}
    },
    "NPS": {
      "unidad": "puntos",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "variacion_mm": {"valor": 6, "unidad": "puntos"}
    },
    "CAC": {
      "unidad": "USD",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "variacion_mm": {"valor": -11, "unidad": "USD"}
    },
    "LTV": {
      "unidad": "USD",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "variacion_mm": {"valor": 330, "unidad": "USD"}
    },
    "active_users": {
      "unidad": "usuarios",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "variacion_mm": {"valor": 15.3, "unidad": "%"}
    },
    "support_tickets": {
      "unidad": "tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "variacion_mm": {"valor": -17.1, "unidad": "%"}
    },
    "avg_response_time": {
      "unidad": "horas",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "variacion_mm": {"valor": -0.7, "unidad": "h"}
    }
  },
  "tendencia_general": "positiva",
  "ltv_cac_ratio": {
    "enero": {"valor": 8.08, "calculo": "1890 / 234"},
    "febrero": {"valor": 10.15, "calculo": "2010 / 198"},
    "marzo": {"valor": 12.51, "calculo": "2340 / 187"}
  },
  "mayor_mejora_porcentual": {
    "periodo_analizado": "enero a marzo",
    "metrica": "avg_response_time",
    "cambio_porcentual": -42.86,
    "nota": "Reducción del tiempo de respuesta, considerada mejora. Si se analiza solo la variación mensual (feb a mar), la mayor mejora es también avg_response_time (-22.6%)."
  },
  "cambios_porcentuales_enero_a_marzo": {
    "MRR": 15.27,
    "churn_rate": -26.19,
    "NPS": 21.43,
    "CAC": -20.09,
    "LTV": 23.81,
    "active_users": 35.98,
    "support_tickets": -29.21,
    "avg_response_time": -42.86
  },
  "proyeccion_abril": {
    "metodo": "Extrapolación lineal usando la variación de febrero a marzo",
    "supuestos": "La tendencia se mantiene constante y la variación mensual es la misma que en marzo",
    "valores": {
      "MRR": {"valor": 55500, "unidad": "USD"},
      "churn_rate": {"valor": 2.4, "unidad": "%"},
      "NPS": {"valor": 57, "unidad": "puntos"},
      "CAC": {"valor": 176, "unidad": "USD"},
      "LTV": {"valor": 2670, "unidad": "USD"},
      "active_users": {"valor": 1900, "unidad": "usuarios"},
      "support_tickets": {"valor": 50, "unidad": "tickets"},
      "avg_response_time": {"valor": 1.7, "unidad": "horas"}
    },
    "ltv_cac_ratio": {"valor": 15.17, "calculo": "2670 / 176"}
  }
}
```