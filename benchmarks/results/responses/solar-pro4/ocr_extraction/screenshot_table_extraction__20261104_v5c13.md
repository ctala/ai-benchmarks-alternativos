# Solar Pro 4 — ocr_extraction/screenshot_table_extraction

- model_id: `upstage/solar-pro4`
- success: True  | final: 8.94 | quality: 10.0
- latency_total: 20.596s | tokens_per_second: 39.1
- input_tokens: 450 | output_tokens: 806

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
  "dashboard_info": {
    "title": "KPIs Marzo 2026",
    "period": "Enero - Marzo 2026",
    "trend": "Positiva en todas las metricas"
  },
  "metrics": [
    {
      "name": "MRR",
      "values": {
        "Enero": 45200,
        "Feb": 48700,
        "Marzo": 52100
      },
      "currency": "USD"
    },
    {
      "name": "Churn Rate",
      "values": {
        "Enero": 4.2,
        "Feb": 3.8,
        "Marzo": 3.1
      },
      "unit": "porcentaje",
      "direction": "lower_is_better"
    },
    {
      "name": "NPS",
      "values": {
        "Enero": 42,
        "Feb": 45,
        "Marzo": 51
      },
      "unit": "puntos"
    },
    {
      "name": "CAC",
      "values": {
        "Enero": 234,
        "Feb": 198,
        "Marzo": 187
      },
      "currency": "USD"
    },
    {
      "name": "LTV",
      "values": {
        "Enero": 1890,
        "Feb": 2010,
        "Marzo": 2340
      },
      "currency": "USD"
    },
    {
      "name": "Active Users",
      "values": {
        "Enero": 1234,
        "Feb": 1456,
        "Marzo": 1678
      },
      "unit": "usuarios"
    },
    {
      "name": "Support Tickets",
      "values": {
        "Enero": 89,
        "Feb": 76,
        "Marzo": 63
      },
      "unit": "tickets"
    },
    {
      "name": "Avg Response (h)",
      "values": {
        "Enero": 4.2,
        "Feb": 3.1,
        "Marzo": 2.4
      },
      "unit": "horas",
      "direction": "lower_is_better"
    }
  ],
  "analysis": {
    "ltv_cac_ratio": {
      "Enero": 8.08,
      "Feb": 10.15,
      "Marzo": 12.51
    },
    "best_improvement_metric": {
      "name": "Support Tickets",
      "percentage_change": -29.21,
      "note": "Mayor reduccion porcentual entre Enero y Marzo (considerada mejora por ser metrica inversa)"
    },
    "april_projection": {
      "methodology": "Extrapolacion lineal basada en crecimiento promedio mensual (Enero-Feb y Feb-Mar)",
      "projection_notes": "Los valores son estimaciones si la tendencia se mantiene constante. No son garantias.",
      "metrics": {
        "MRR": 55693.55,
        "Churn Rate": 2.4,
        "NPS": 57,
        "CAC": 176,
        "LTV": 2670,
        "Active Users": 1921,
        "Support Tickets": 50,
        "Avg Response (h)": 1.7
      }
    }
  }
}