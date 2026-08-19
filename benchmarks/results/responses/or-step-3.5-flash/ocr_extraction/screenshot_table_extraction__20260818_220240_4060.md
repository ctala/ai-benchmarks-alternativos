# Step 3.5 Flash — ocr_extraction/screenshot_table_extraction

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 7.33 | quality: 8.0
- latency_total: 100.978s | tokens_per_second: 69.2
- input_tokens: 394 | output_tokens: 6985

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
  "datos_tabla": [
    {
      "metrica": "MRR",
      "Enero": 45.2,
      "Febrero": 48.7,
      "Marzo": 52.1,
      "Var_M_M": 7.0,
      "unidad": "K USD"
    },
    {
      "metrica": "Churn Rate",
      "Enero": 4.2,
      "Febrero": 3.8,
      "Marzo": 3.1,
      "Var_M_M": -0.7,
      "unidad": "%"
    },
    {
      "metrica": "NPS",
      "Enero": 42,
      "Febrero": 45,
      "Marzo": 51,
      "Var_M_M": 6,
      "unidad": "puntos"
    },
    {
      "metrica": "CAC",
      "Enero": 234,
      "Febrero": 198,
      "Marzo": 187,
      "Var_M_M": -11,
      "unidad": "USD"
    },
    {
      "metrica": "LTV",
      "Enero": 1890,
      "Febrero": 2010,
      "Marzo": 2340,
      "Var_M_M": 330,
      "unidad": "USD"
    },
    {
      "metrica": "Active Users",
      "Enero": 1234,
      "Febrero": 1456,
      "Marzo": 1678,
      "Var_M_M": 15.3,
      "unidad": "usuarios"
    },
    {
      "metrica": "Support Tickets",
      "Enero": 89,
      "Febrero": 76,
      "Marzo": 63,
      "Var_M_M": -17.1,
      "unidad": "tickets"
    },
    {
      "metrica": "Avg Response",
      "Enero": 4.2,
      "Febrero": 3.1,
      "Marzo": 2.4,
      "Var_M_M": -0.7,
      "unidad": "horas"
    }
  ],
  "ltv_cac_ratio": {
    "Enero": 8.08,
    "Febrero": 10.15,
    "Marzo": 12.51
  },
  "mayor_mejora_porcentual": {
    "metrica": "Avg Response",
    "porcentaje_mejora": 22.58,
    "explicacion": "El tiempo promedio de respuesta redujo de 3.1 horas en febrero a 2.4 horas en marzo, una mejora del 22.58%."
  },
  "proyeccion_abril": {
    "MRR": 55.7,
    "Churn Rate": 2.4,
    "NPS": 57,
    "CAC": 176,
    "LTV": 2670,
    "Active Users": 1935,
    "Support Tickets": 52,
    "Avg Response": 1.7
  }
}
```