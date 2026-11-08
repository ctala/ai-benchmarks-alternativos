# Ministral 14B — ocr_extraction/screenshot_table_extraction

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 7.53 | quality: 8.0
- latency_total: 30.956s | tokens_per_second: 42.6
- input_tokens: 422 | output_tokens: 1318

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
  "dashboard_metadata": {
    "title": "DASHBOARD - KPIs Marzo 2026",
    "period": "Marzo 2026",
    "trend": "↑ Positiva en todas las métricas"
  },
  "data": {
    "metrics": [
      {
        "name": "MRR",
        "values": {
          "Enero": 45200,
          "Febrero": 48700,
          "Marzo": 52100,
          "var_m/m": 7.0
        },
        "unit": "$"
      },
      {
        "name": "Churn Rate",
        "values": {
          "Enero": 4.2,
          "Febrero": 3.8,
          "Marzo": 3.1,
          "var_m/m": -0.7
        },
        "unit": "%",
        "type": "percentage_points"
      },
      {
        "name": "NPS",
        "values": {
          "Enero": 42,
          "Febrero": 45,
          "Marzo": 51,
          "var_m/m": 6
        },
        "unit": "puntos"
      },
      {
        "name": "CAC",
        "values": {
          "Enero": 234,
          "Febrero": 198,
          "Marzo": 187,
          "var_m/m": -11
        },
        "unit": "$"
      },
      {
        "name": "LTV",
        "values": {
          "Enero": 1890,
          "Febrero": 2010,
          "Marzo": 2340,
          "var_m/m": 330
        },
        "unit": "$"
      },
      {
        "name": "Active Users",
        "values": {
          "Enero": 1234,
          "Febrero": 1456,
          "Marzo": 1678,
          "var_m/m": 15.3
        },
        "unit": "usuarios"
      },
      {
        "name": "Support Tickets",
        "values": {
          "Enero": 89,
          "Febrero": 76,
          "Marzo": 63,
          "var_m/m": -17.1
        },
        "unit": "tickets"
      },
      {
        "name": "Avg Response (h)",
        "values": {
          "Enero": 4.2,
          "Febrero": 3.1,
          "Marzo": 2.4,
          "var_m/m": -0.7
        },
        "unit": "horas"
      }
    ]
  },
  "calculations": {
    "ltv_cac_ratio": {
      "Enero": 1890 / 234,
      "Febrero": 2010 / 198,
      "Marzo": 2340 / 187,
      "values": {
        "Enero": 8.0769,
        "Febrero": 10.1515,
        "Marzo": 12.5134
      },
      "unit": "ratio"
    },
    "metric_with_greatest_improvement": {
      "name": "Active Users",
      "improvement": 15.3,
      "unit": "%",
      "reason": "Mayor mejora porcentual en términos absolutos (15.3% MoM)"
    }
  },
  "projection_april": {
    "method": "Mantenimiento de la tendencia MoM (Marzo → Abril)",
    "assumptions": {
      "type": "lineal",
      "note": "Se aplica el mismo % de cambio MoM observado en Marzo para proyectar Abril"
    },
    "projected_values": [
      {
        "metric": "MRR",
        "value": 52100 * (1 + 7.0 / 100),
        "unit": "$",
        "projected": 55747
      },
      {
        "metric": "Churn Rate",
        "value": 3.1 - 0.7,
        "unit": "%",
        "projected": 2.4
      },
      {
        "metric": "NPS",
        "value": 51 + 6,
        "unit": "puntos",
        "projected": 57
      },
      {
        "metric": "CAC",
        "value": 187 - 11,
        "unit": "$",
        "projected": 176
      },
      {
        "metric": "LTV",
        "value": 2340 + 330,
        "unit": "$",
        "projected": 2670
      },
      {
        "metric": "Active Users",
        "value": 1678 * (1 + 15.3 / 100),
        "unit": "usuarios",
        "projected": 1933
      },
      {
        "metric": "Support Tickets",
        "value": 63 * (1 - 17.1 / 100),
        "unit": "tickets",
        "projected": 52
      },
      {
        "metric": "Avg Response (h)",
        "value": 2.4 - 0.7,
        "unit": "horas",
        "projected": 1.7
      }
    ],
    "ltv_cac_ratio_april": {
      "value": 2670 / 176,
      "projected": 15.1648
    }
  }
}
```