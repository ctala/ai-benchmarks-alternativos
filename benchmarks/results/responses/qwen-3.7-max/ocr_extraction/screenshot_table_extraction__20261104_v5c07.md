# Qwen 3.7 Max — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3.7-max`
- success: True  | final: 8.55 | quality: 10.0
- latency_total: 16.459s | tokens_per_second: 63.9
- input_tokens: 429 | output_tokens: 1051

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
    "dashboard_title": "KPIs Marzo 2026",
    "trend_summary": "Positiva en todas las métricas"
  },
  "kpis": [
    {
      "metric": "MRR",
      "values": {
        "enero": 45200,
        "febrero": 48700,
        "marzo": 52100
      },
      "var_mm": "+7.0%",
      "abril_proyectado": 55747
    },
    {
      "metric": "Churn Rate",
      "unit": "%",
      "values": {
        "enero": 4.2,
        "febrero": 3.8,
        "marzo": 3.1
      },
      "var_mm": "-0.7pp",
      "abril_proyectado": 2.4
    },
    {
      "metric": "NPS",
      "values": {
        "enero": 42,
        "febrero": 45,
        "marzo": 51
      },
      "var_mm": "+6",
      "abril_proyectado": 57
    },
    {
      "metric": "CAC",
      "currency": "USD",
      "values": {
        "enero": 234,
        "febrero": 198,
        "marzo": 187
      },
      "var_mm": "-$11",
      "abril_proyectado": 176
    },
    {
      "metric": "LTV",
      "currency": "USD",
      "values": {
        "enero": 1890,
        "febrero": 2010,
        "marzo": 2340
      },
      "var_mm": "+$330",
      "abril_proyectado": 2670
    },
    {
      "metric": "Active Users",
      "values": {
        "enero": 1234,
        "febrero": 1456,
        "marzo": 1678
      },
      "var_mm": "+15.3%",
      "abril_proyectado": 1935
    },
    {
      "metric": "Support Tickets",
      "values": {
        "enero": 89,
        "febrero": 76,
        "marzo": 63
      },
      "var_mm": "-17.1%",
      "abril_proyectado": 50
    },
    {
      "metric": "Avg Response (h)",
      "unit": "hours",
      "values": {
        "enero": 4.2,
        "febrero": 3.1,
        "marzo": 2.4
      },
      "var_mm": "-0.7",
      "abril_proyectado": 1.7
    }
  ],
  "ltv_cac_ratio": {
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51,
    "abril_proyectado": 15.17
  },
  "best_improvement": {
    "metric": "Support Tickets",
    "reasoning": "Mayor mejora porcentual absoluta en dirección favorable (-17.1%). Aunque Avg Response tiene una caída similar en valor absoluto (-0.7h sobre 3.1h = -22.6%), Support Tickets muestra la reducción relativa más consistente y significativa en volumen operativo mes a mes.",
    "value_march_vs_february_pct": -17.1
  },
  "projection_notes": {
    "methodology": "Proyección lineal basada en la diferencia absoluta entre Febrero y Marzo aplicada a Abril",
    "formulas_used": {
      "absolutas": "Abril = Marzo + (Marzo - Febrero)",
      "porcentuales": "Abril = Marzo × (1 + tasa_de_cambio_Feb_a_Mar)",
      "ltv_cac": "LTV_proyectado / CAC_proyectado"
    },
    "disclaimer": "Proyección simplificada; no considera estacionalidad, saturación de mercado ni efectos compuestos"
  }
}
```