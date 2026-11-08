# Mercury 3 — ocr_extraction/screenshot_table_extraction

- model_id: `inception/mercury-3`
- success: True  | final: 8.22 | quality: 8.0
- latency_total: 1.386s | tokens_per_second: 580.1
- input_tokens: 365 | output_tokens: 804

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

Aquí tienes el JSON estructurado con los datos extraídos, los cálculos solicitados y las proyecciones para abril:

```json
{
  "dashboard_info": {
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "tendencia_general": "Positiva en todas las métricas"
  },
  "datos_extraidos": [
    {
      "metrica": "MRR",
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "var_m_m": 7.0
    },
    {
      "metrica": "Churn Rate",
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "var_m_m": -0.7
    },
    {
      "metrica": "NPS",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "var_m_m": 6
    },
    {
      "metrica": "CAC",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "var_m_m": -11
    },
    {
      "metrica": "LTV",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "var_m_m": 330
    },
    {
      "metrica": "Active Users",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "var_m_m": 15.3
    },
    {
      "metrica": "Support Tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "var_m_m": -17.1
    },
    {
      "metrica": "Avg Response (h)",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "var_m_m": -0.7
    }
  ],
  "calculos": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51
    },
    "metrica_mayor_mejora_porcentual": {
      "metrica": "LTV/CAC ratio",
      "mejora_porcentual": 54.8,
      "nota": "Calculado como el cambio porcentual del ratio entre enero (8.08) y marzo (12.51). Si se consideran solo las métricas directas, Active Users lidera con +15.3% de mejora mensual."
    }
  },
  "proyeccion_abril": {
    "metodologia": "Proyección lineal basada en el cambio promedio mensual (enero→febrero→marzo) o en la última variación M/M si el cambio no es constante.",
    "valores": {
      "MRR": 55747,
      "Churn Rate": 2.4,
      "NPS": 57,
      "CAC": 176,
      "LTV": 2670,
      "Active Users": 1935,
      "Support Tickets": 52,
      "Avg Response (h)": 1.7
    },
    "ltv_cac_ratio_proyectado": 15.17,
    "nota": "Las proyecciones asumen que la tendencia actual se mantiene sin cambios estacionales ni eventos atípicos."
  }
}
```