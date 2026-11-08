# Claude Fable 5.1 — ocr_extraction/screenshot_table_extraction

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 6.51 | quality: 8.0
- latency_total: 28.404s | tokens_per_second: 95.0
- input_tokens: 514 | output_tokens: 2699

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
    "titulo": "KPIs Marzo 2026",
    "periodo": ["Enero", "Febrero", "Marzo"],
    "tendencia_general": "Positiva en todas las métricas"
  },
  "metricas": [
    { "nombre": "MRR", "unidad": "USD", "enero": 45200, "febrero": 48700, "marzo": 52100, "var_mm": "+7.0%" },
    { "nombre": "Churn Rate", "unidad": "%", "enero": 4.2, "febrero": 3.8, "marzo": 3.1, "var_mm": "-0.7pp" },
    { "nombre": "NPS", "unidad": "puntos", "enero": 42, "febrero": 45, "marzo": 51, "var_mm": "+6" },
    { "nombre": "CAC", "unidad": "USD", "enero": 234, "febrero": 198, "marzo": 187, "var_mm": "-$11" },
    { "nombre": "LTV", "unidad": "USD", "enero": 1890, "febrero": 2010, "marzo": 2340, "var_mm": "+$330" },
    { "nombre": "Active Users", "unidad": "usuarios", "enero": 1234, "febrero": 1456, "marzo": 1678, "var_mm": "+15.3%" },
    { "nombre": "Support Tickets", "unidad": "tickets", "enero": 89, "febrero": 76, "marzo": 63, "var_mm": "-17.1%" },
    { "nombre": "Avg Response", "unidad": "horas", "enero": 4.2, "febrero": 3.1, "marzo": 2.4, "var_mm": "-0.7" }
  ],
  "analisis": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "nota": "LTV / CAC. Un ratio > 3 se considera saludable; la tendencia es claramente creciente."
    },
    "mayor_mejora_porcentual": {
      "metrica": "Avg Response (h)",
      "variacion_feb_marzo": "-22.6%",
      "variacion_enero_marzo": "-42.9%",
      "nota": "El dashboard muestra -0.7 (variación absoluta en horas), pero en términos relativos es la métrica con mayor mejora.",
      "ranking_feb_marzo": [
        { "metrica": "Avg Response (h)", "mejora": "22.6%" },
        { "metrica": "Churn Rate", "mejora": "18.4%" },
        { "metrica": "Support Tickets", "mejora": "17.1%" },
        { "metrica": "LTV", "mejora": "16.4%" },
        { "metrica": "Active Users", "mejora": "15.3%" },
        { "metrica": "NPS", "mejora": "13.3%" },
        { "metrica": "MRR", "mejora": "7.0%" },
        { "metrica": "CAC", "mejora": "5.6%" }
      ]
    },
    "proyeccion_abril": {
      "metodo": "Se aplica la misma variación M/M de Marzo (porcentual para MRR, Active Users y Tickets; absoluta para Churn, NPS, CAC, LTV y Avg Response, tal como las reporta el dashboard).",
      "valores": {
        "MRR": "$55.7K",
        "Churn Rate": "2.4%",
        "NPS": 57,
        "CAC": "$176",
        "LTV": "$2,670",
        "Active Users": 1934,
        "Support Tickets": 52,
        "Avg Response (h)": 1.7,
        "LTV/CAC ratio": 15.17
      },
      "advertencias": [
        "Proyección lineal simple con solo 3 puntos de datos; no considera estacionalidad ni saturación.",
        "Churn y Avg Response no pueden seguir bajando indefinidamente al mismo ritmo (tienen piso natural).",
        "Si se usara el promedio de las dos variaciones mensuales en lugar de la última, los valores serían ligeramente distintos (p. ej. MRR ≈ $55.9K, Active Users ≈ 1,941)."
      ]
    }
  }
}
```