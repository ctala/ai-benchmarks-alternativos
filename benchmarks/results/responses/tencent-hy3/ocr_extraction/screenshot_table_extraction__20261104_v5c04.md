# Tencent Hy3 — ocr_extraction/screenshot_table_extraction

- model_id: `tencent/hy3`
- success: True  | final: 9.0 | quality: 10.0
- latency_total: 15.101s | tokens_per_second: 59.0
- input_tokens: 404 | output_tokens: 891

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
    "title": "DASHBOARD - KPIs Marzo 2026",
    "metrics": [
      {
        "metric": "MRR",
        "enero": 45200,
        "febrero": 48700,
        "marzo": 52100,
        "var_mm": "+7.0%"
      },
      {
        "metric": "Churn Rate",
        "enero": 4.2,
        "febrero": 3.8,
        "marzo": 3.1,
        "var_mm": "-0.7pp"
      },
      {
        "metric": "NPS",
        "enero": 42,
        "febrero": 45,
        "marzo": 51,
        "var_mm": "+6"
      },
      {
        "metric": "CAC",
        "enero": 234,
        "febrero": 198,
        "marzo": 187,
        "var_mm": "-$11"
      },
      {
        "metric": "LTV",
        "enero": 1890,
        "febrero": 2010,
        "marzo": 2340,
        "var_mm": "+$330"
      },
      {
        "metric": "Active Users",
        "enero": 1234,
        "febrero": 1456,
        "marzo": 1678,
        "var_mm": "+15.3%"
      },
      {
        "metric": "Support Tickets",
        "enero": 89,
        "febrero": 76,
        "marzo": 63,
        "var_mm": "-17.1%"
      },
      {
        "metric": "Avg Response (h)",
        "enero": 4.2,
        "febrero": 3.1,
        "marzo": 2.4,
        "var_mm": "-0.7"
      }
    ],
    "tendencia_general": "Positiva en todas las metricas"
  },
  "ltv_cac_ratio": {
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51
  },
  "mayor_mejora_porcentual": {
    "metric": "Support Tickets",
    "var_mm_marzo": "-17.1%",
    "nota": "Es la mayor reducción porcentual (mejora operativa). En cuanto a crecimiento positivo, Active Users tuvo +15.3%."
  },
  "proyeccion_abril": {
    "metodo": "Extrapolación lineal/mensual basada en la tendencia de los últimos meses",
    "values": {
      "MRR": 55747,
      "Churn Rate": 2.4,
      "NPS": 57,
      "CAC": 176,
      "LTV": 2670,
      "Active Users": 1934,
      "Support Tickets": 52,
      "Avg Response (h)": 1.7
    },
    "detalle_calculo": {
      "MRR": "52100 * 1.07 ≈ 55747",
      "Churn Rate": "3.1 - 0.7 = 2.4",
      "NPS": "51 + 6 = 57",
      "CAC": "187 - 11 = 176",
      "LTV": "2340 + 330 = 2670",
      "Active Users": "1678 * 1.153 ≈ 1934",
      "Support Tickets": "63 * 0.829 ≈ 52",
      "Avg Response (h)": "2.4 - 0.7 = 1.7"
    }
  }
}
```