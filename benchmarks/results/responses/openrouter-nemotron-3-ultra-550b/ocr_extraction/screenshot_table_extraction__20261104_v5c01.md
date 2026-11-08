# Nemotron 3 Ultra 550B — ocr_extraction/screenshot_table_extraction

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 7.64 | quality: 8.0
- latency_total: 4.163s | tokens_per_second: 264.5
- input_tokens: 435 | output_tokens: 1101

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
    "title": "KPIs Marzo 2026",
    "period": "Enero - Marzo 2026",
    "metrics": [
      {
        "name": "MRR",
        "unit": "USD",
        "values": {
          "Enero": 45200,
          "Febrero": 48700,
          "Marzo": 52100
        },
        "mom_change_pct": 7.0,
        "mom_change_abs": 3400
      },
      {
        "name": "Churn Rate",
        "unit": "%",
        "values": {
          "Enero": 4.2,
          "Febrero": 3.8,
          "Marzo": 3.1
        },
        "mom_change_pp": -0.7,
        "mom_change_pct": -18.4
      },
      {
        "name": "NPS",
        "unit": "score",
        "values": {
          "Enero": 42,
          "Febrero": 45,
          "Marzo": 51
        },
        "mom_change_abs": 6,
        "mom_change_pct": 13.3
      },
      {
        "name": "CAC",
        "unit": "USD",
        "values": {
          "Enero": 234,
          "Febrero": 198,
          "Marzo": 187
        },
        "mom_change_abs": -11,
        "mom_change_pct": -5.6
      },
      {
        "name": "LTV",
        "unit": "USD",
        "values": {
          "Enero": 1890,
          "Febrero": 2010,
          "Marzo": 2340
        },
        "mom_change_abs": 330,
        "mom_change_pct": 16.4
      },
      {
        "name": "Active Users",
        "unit": "count",
        "values": {
          "Enero": 1234,
          "Febrero": 1456,
          "Marzo": 1678
        },
        "mom_change_pct": 15.3,
        "mom_change_abs": 222
      },
      {
        "name": "Support Tickets",
        "unit": "count",
        "values": {
          "Enero": 89,
          "Febrero": 76,
          "Marzo": 63
        },
        "mom_change_pct": -17.1,
        "mom_change_abs": -13
      },
      {
        "name": "Avg Response Time",
        "unit": "hours",
        "values": {
          "Enero": 4.2,
          "Febrero": 3.1,
          "Marzo": 2.4
        },
        "mom_change_abs": -0.7,
        "mom_change_pct": -22.6
      }
    ]
  },
  "ltv_cac_ratio": {
    "Enero": 8.08,
    "Febrero": 10.15,
    "Marzo": 12.51
  },
  "best_improvement": {
    "metric": "Avg Response Time",
    "mom_change_pct": -22.6,
    "note": "Mayor mejora porcentual absoluta (reducción 22.6% mes a mes). En métricas de crecimiento positivo: LTV (+16.4%)"
  },
  "april_projection": {
    "method": "Linear extrapolation based on March MoM absolute change",
    "assumptions": "Tendencia lineal simple; no considera estacionalidad ni saturación",
    "projected_values": {
      "MRR": 55500,
      "Churn Rate": 2.4,
      "NPS": 57,
      "CAC": 176,
      "LTV": 2670,
      "Active Users": 1900,
      "Support Tickets": 50,
      "Avg Response Time": 1.7
    },
    "projected_ltv_cac_ratio": 15.17
  },
  "summary": {
    "overall_trend": "Positiva en todas las métricas",
    "ltv_cac_trend": "Mejora sostenida: 8.1x → 10.2x → 12.5x (proyectado 15.2x)",
    "key_highlight": "LTV crece +16.4% mientras CAC cae -5.6% → expansión eficiente"
  }
}
```