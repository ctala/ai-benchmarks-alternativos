# Grok 4.6 — ocr_extraction/screenshot_table_extraction

- model_id: `x-ai/grok-4.6`
- success: True  | final: 8.28 | quality: 10.0
- latency_total: 46.796s | tokens_per_second: 71.6
- input_tokens: 566 | output_tokens: 3352

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
  "periodo": ["Enero", "Febrero", "Marzo"],
  "datos": {
    "MRR": { "enero": 45200, "febrero": 48700, "marzo": 52100, "var_mm": "+7.0%" },
    "Churn Rate": { "enero": 0.042, "febrero": 0.038, "marzo": 0.031, "var_mm": "-0.7pp" },
    "NPS": { "enero": 42, "febrero": 45, "marzo": 51, "var_mm": "+6" },
    "CAC": { "enero": 234, "febrero": 198, "marzo": 187, "var_mm": "-$11" },
    "LTV": { "enero": 1890, "febrero": 2010, "marzo": 2340, "var_mm": "+$330" },
    "Active Users": { "enero": 1234, "febrero": 1456, "marzo": 1678, "var_mm": "+15.3%" },
    "Support Tickets": { "enero": 89, "febrero": 76, "marzo": 63, "var_mm": "-17.1%" },
    "Avg Response (h)": { "enero": 4.2, "febrero": 3.1, "marzo": 2.4, "var_mm": "-0.7" }
  },
  "ltv_cac_ratio": {
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51,
    "formula": "LTV / CAC",
    "detalle": {
      "enero": "1890 / 234 = 8.08",
      "febrero": "2010 / 198 = 10.15",
      "marzo": "2340 / 187 = 12.51"
    }
  },
  "mayor_mejora_porcentual": {
    "metrica": "Avg Response (h)",
    "variacion_ene_mar": -42.86,
    "unidad": "%",
    "interpretacion": "Menor es mejor: 4.2h → 2.4h",
    "ranking_mejora_ene_mar_pct": [
      { "metrica": "Avg Response (h)", "cambio_pct": -42.86, "mejora": 42.86, "sentido": "baja" },
      { "metrica": "Active Users", "cambio_pct": 35.98, "mejora": 35.98, "sentido": "sube" },
      { "metrica": "Support Tickets", "cambio_pct": -29.21, "mejora": 29.21, "sentido": "baja" },
      { "metrica": "Churn Rate", "cambio_pct": -26.19, "mejora": 26.19, "sentido": "baja" },
      { "metrica": "LTV", "cambio_pct": 23.81, "mejora": 23.81, "sentido": "sube" },
      { "metrica": "NPS", "cambio_pct": 21.43, "mejora": 21.43, "sentido": "sube" },
      { "metrica": "CAC", "cambio_pct": -20.09, "mejora": 20.09, "sentido": "baja" },
      { "metrica": "MRR", "cambio_pct": 15.27, "mejora": 15.27, "sentido": "sube" }
    ]
  },
  "proyeccion_abril": {
    "metodo": "Se aplica la variación M/M de Feb→Marzo (mismos criterios que Var M/M del dashboard)",
    "valores": {
      "MRR": 55747,
      "Churn Rate": 0.024,
      "NPS": 57,
      "CAC": 176,
      "LTV": 2670,
      "Active Users": 1935,
      "Support Tickets": 52,
      "Avg Response (h)": 1.7
    },
    "detalle_calculo": {
      "MRR": "52100 × 1.07 = 55747",
      "Churn Rate": "3.1% - 0.7pp = 2.4%",
      "NPS": "51 + 6 = 57",
      "CAC": "187 - 11 = 176",
      "LTV": "2340 + 330 = 2670",
      "Active Users": "1678 × 1.153 ≈ 1935",
      "Support Tickets": "63 × (1 - 0.171) ≈ 52",
      "Avg Response (h)": "2.4 - 0.7 = 1.7"
    },
    "ltv_cac_ratio_abril": 15.17
  },
  "nota": "Tendencia general positiva en todas las métricas. Proyección lineal del último salto mensual; no incorpora estacionalidad ni techos (p. ej. churn/tiempos no pueden ser negativos)."
}
```