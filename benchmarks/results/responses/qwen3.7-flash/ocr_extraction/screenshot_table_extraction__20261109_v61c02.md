# Qwen 3.7 Flash — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 9.4 | quality: 10.0
- latency_total: 9.39s | tokens_per_second: 122.2
- input_tokens: 429 | output_tokens: 1147

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
  "dashboard_info": {
    "title": "DASHBOARD - KPIs Marzo 2026",
    "period": "Enero 2026 - Marzo 2026"
  },
  "raw_data": [
    {
      "metrica": "MRR",
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "var_m_m": "+7.0%"
    },
    {
      "metrica": "Churn Rate",
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "var_m_m": "-0.7pp"
    },
    {
      "metrica": "NPS",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "var_m_m": "+6"
    },
    {
      "metrica": "CAC",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "var_m_m": "-$11"
    },
    {
      "metrica": "LTV",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "var_m_m": "+$330"
    },
    {
      "metrica": "Active Users",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "var_m_m": "+15.3%"
    },
    {
      "metrica": "Support Tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "var_m_m": "-17.1%"
    },
    {
      "metrica": "Avg Response (h)",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "var_m_m": "-0.7"
    }
  ],
  "ltv_cac_ratio": {
    "enero": {
      "ltv": 1890,
      "cac": 234,
      "ratio": 8.08
    },
    "febrero": {
      "ltv": 2010,
      "cac": 198,
      "ratio": 10.15
    },
    "marzo": {
      "ltv": 2340,
      "cac": 187,
      "ratio": 12.51
    }
  },
  "mejor_metrica_mejora": {
    "metrica": "Support Tickets",
    "mejora_pct": -17.1,
    "nota": "Reducción del 17.1% en tickets de soporte (mejora positiva)"
  },
  "proyeccion_abril_2026": {
    "metodo": "Tendencia lineal basada en crecimiento mensual promedio (M/M)",
    "proyecciones": {
      "MRR": {
        "valor": 55748.7,
        "crecimiento_estimado": "+7.0%"
      },
      "Churn Rate": {
        "valor": 2.4,
        "cambio_estimado": "-0.7pp"
      },
      "NPS": {
        "valor": 57,
        "cambio_estimado": "+6"
      },
      "CAC": {
        "valor": 176,
        "cambio_estimado": "-$11"
      },
      "LTV": {
        "valor": 2670,
        "cambio_estimado": "+$330"
      },
      "Active Users": {
        "valor": 1935,
        "crecimiento_estimado": "+15.3%"
      },
      "Support Tickets": {
        "valor": 52,
        "cambio_estimado": "-17.1%"
      },
      "Avg Response (h)": {
        "valor": 1.7,
        "cambio_estimado": "-0.7"
      }
    },
    "ltv_cac_ratio_proyectado": {
      "ltv": 2670,
      "cac": 176,
      "ratio": 15.17
    }
  }
}
```