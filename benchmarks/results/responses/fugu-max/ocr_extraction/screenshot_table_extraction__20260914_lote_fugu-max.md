# Fugu Max — ocr_extraction/screenshot_table_extraction

- model_id: `sakana/fugu-max`
- success: True  | final: 6.58 | quality: 8.0
- latency_total: 169.493s | tokens_per_second: 92.6
- input_tokens: 540 | output_tokens: 15696

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
  "dashboard": "DASHBOARD - KPIs Marzo 2026",
  "tendencia_general": "↑ Positiva en todas las metricas",
  "metricas": [
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
      "var_mm": "-$11"
    },
    {
      "metrica": "LTV",
      "unidad": "USD",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "var_mm": "+$330"
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
      "metrica": "Avg Response (h)",
      "unidad": "horas",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "var_mm": "-0.7"
    }
  ],
  "ltv_cac_ratio": {
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51
  },
  "metrica_mayor_mejora_porcentual": {
    "metrica": "Avg Response (h)",
    "cambio_porcentual_feb_mar": -22.58,
    "mejora_porcentual_ajustada": 22.58,
    "criterio": "Se tomó la magnitud del cambio porcentual Feb→Mar, considerando mejora cuando la métrica baja y menor es mejor."
  },
  "nota_alternativa": "Si se consideran solo incrementos porcentuales en métricas donde mayor es mejor, LTV es la mayor mejora con +16.42%.",
  "proyeccion_abril": {
    "metodo": "Manteniendo la variación intermensual Feb→Mar: porcentual exacta para MRR, Active Users y Support Tickets; absoluta/pp para el resto. Valores redondeados.",
    "valores": {
      "MRR": 55737,
      "Churn Rate": 2.4,
      "NPS": 57,
      "CAC": 176,
      "LTV": 2670,
      "Active Users": 1934,
      "Support Tickets": 52,
      "Avg Response (h)": 1.7
    }
  }
}