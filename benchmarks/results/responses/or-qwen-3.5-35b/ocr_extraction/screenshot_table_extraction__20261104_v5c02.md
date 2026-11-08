# Qwen 3.5 35B — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3.5-35b-a3b`
- success: True  | final: 7.56 | quality: 8.0
- latency_total: 8.256s | tokens_per_second: 181.4
- input_tokens: 429 | output_tokens: 1498

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
    "dashboard_title": "DASHBOARD - KPIs Marzo 2026",
    "tendencia_general": "Positiva"
  },
  "raw_data": [
    {
      "metrica": "MRR",
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "var_m_m_pct": 7.0,
      "unidad": "USD"
    },
    {
      "metrica": "Churn Rate",
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "var_m_m_pp": -0.7,
      "unidad": "Porcentaje"
    },
    {
      "metrica": "NPS",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "var_m_m_abs": 6,
      "unidad": "Puntos"
    },
    {
      "metrica": "CAC",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "var_m_m_abs": -11,
      "unidad": "USD"
    },
    {
      "metrica": "LTV",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "var_m_m_abs": 330,
      "unidad": "USD"
    },
    {
      "metrica": "Active Users",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "var_m_m_pct": 15.3,
      "unidad": "Cuenta"
    },
    {
      "metrica": "Support Tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "var_m_m_pct": -17.1,
      "unidad": "Ticket"
    },
    {
      "metrica": "Avg Response (h)",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "var_m_m_abs": -0.7,
      "unidad": "Horas"
    }
  ],
  "calculated_metrics": {
    "ltv_cac_ratio": [
      {
        "mes": "Enero",
        "ltv": 1890,
        "cac": 234,
        "ratio": 8.08
      },
      {
        "mes": "Febrero",
        "ltv": 2010,
        "cac": 198,
        "ratio": 10.15
      },
      {
        "mes": "Marzo",
        "ltv": 2340,
        "cac": 187,
        "ratio": 12.51
      }
    ]
  },
  "insights": {
    "metrica_mayor_mejora_porcentual": {
      "metrica": "Churn Rate",
      "valor_inicial": 4.2,
      "valor_final": 3.1,
      "mejora_total_pct": 26.19,
      "nota": "Reducción de la tasa de abandono en un 26.19% desde Enero a Marzo."
    },
    "proyeccion_abril": {
      "metodo": "Promedio de crecimiento M/M (Tendencia lineal simple basada en el último mes y promedio histórico cercano)",
      "valores_proyectados": [
        {
          "metrica": "MRR",
          "valor_marzo": 52100,
          "factor_crecimiento_promedio": 1.06,
          "proyeccion_abril": 55226,
          "unidades": "USD"
        },
        {
          "metrica": "Churn Rate",
          "valor_marzo": 3.1,
          "reduccion_promedio_pp": 0.45,
          "proyeccion_abril": 2.65,
          "unidades": "Porcentaje"
        },
        {
          "metrica": "NPS",
          "valor_marzo": 51,
          "crecimiento_promedio_abs": 4.5,
          "proyeccion_abril": 55.5,
          "unidades": "Puntos"
        },
        {
          "metrica": "CAC",
          "valor_marzo": 187,
          "reduccion_promedio_abs": 10,
          "proyeccion_abril": 177,
          "unidades": "USD"
        },
        {
          "metrica": "LTV",
          "valor_marzo": 2340,
          "crecimiento_promedio_abs": 285,
          "proyeccion_abril": 2625,
          "unidades": "USD"
        },
        {
          "metrica": "Active Users",
          "valor_marzo": 1678,
          "crecimiento_promedio_pct": 12.5,
          "proyeccion_abril": 1888,
          "unidades": "Usuarios"
        },
        {
          "metrica": "Support Tickets",
          "valor_marzo": 63,
          "reduccion_promedio_pct": 12.0,
          "proyeccion_abril": 55.4,
          "unidades": "Tickets"
        },
        {
          "metrica": "Avg Response (h)",
          "valor_marzo": 2.4,
          "reduccion_promedio_abs": 0.6,
          "proyeccion_abril": 1.8,
          "unidades": "Horas"
        }
      ]
    }
  }
}
```