# GLM 5.3 Flash — ocr_extraction/screenshot_table_extraction

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 9.37 | quality: 10.0
- latency_total: 6.103s | tokens_per_second: 142.4
- input_tokens: 395 | output_tokens: 869

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
  "dashboard": "KPIs Marzo 2026",
  "datos_extraidos": [
    {"metrica": "MRR", "unidad": "USD", "enero": 45200, "febrero": 48700, "marzo": 52100, "var_mom": "+7.0%"},
    {"metrica": "Churn Rate", "unidad": "%", "enero": 4.2, "febrero": 3.8, "marzo": 3.1, "var_mom": "-0.7pp"},
    {"metrica": "NPS", "unidad": "puntos", "enero": 42, "febrero": 45, "marzo": 51, "var_mom": "+6"},
    {"metrica": "CAC", "unidad": "USD", "enero": 234, "febrero": 198, "marzo": 187, "var_mom": "-$11"},
    {"metrica": "LTV", "unidad": "USD", "enero": 1890, "febrero": 2010, "marzo": 2340, "var_mom": "+$330"},
    {"metrica": "Active Users", "unidad": "usuarios", "enero": 1234, "febrero": 1456, "marzo": 1678, "var_mom": "+15.3%"},
    {"metrica": "Support Tickets", "unidad": "tickets", "enero": 89, "febrero": 76, "marzo": 63, "var_mom": "-17.1%"},
    {"metrica": "Avg Response", "unidad": "horas", "enero": 4.2, "febrero": 3.1, "marzo": 2.4, "var_mom": "-0.7"}
  ],

  "analisis": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "metodologia": "LTV / CAC por mes",
      "interpretacion": "Ratio > 3 en todos los meses; mejora continua, indicativo de eficiencia en adquisición muy saludable."
    },

    "metrica_mayor_mejora": {
      "metrica": "Support Tickets",
      "mejora": "-17.1% (reducción)",
      "nota": "En términos de cambio porcentual reportado, Support Tickets muestra la mayor variación. Si se considera mejora relativa entre meses, Active Users (+15.3%) lidera entre métricas de crecimiento."
    },

    "proyeccion_abril": {
      "metodologia": "Extrapolación lineal simple del cambio Febrero→Marzo aplicado a Marzo",
      "valores": {
        "MRR": 55500,
        "Churn Rate": 2.4,
        "NPS": 57,
        "CAC": 176,
        "LTV": 2670,
        "Active Users": 1900,
        "Support Tickets": 50,
        "Avg Response": 1.7
      },
      "supuestos": [
        "Se mantiene el ritmo de cambio M/M de marzo",
        "Churn Rate continúa reduciéndose ~0.7pp/mes",
        "Proyección orientativa; no considera estacionalidad ni efectos no lineales"
      ]
    }
  },

  "resumen": {
    "tendencia": "Positiva en todas las métricas",
    "riesgos": [
      "LTV/CAC de 12.5 podría sugerir subinversión en adquisición (CAC muy bajo o LTV inflado)",
      "Proyección lineal de churn a 2.4% puede ser optimista"
    ]
  }
}
```