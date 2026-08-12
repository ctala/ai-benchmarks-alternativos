# Muse Spark 1.2 — ocr_extraction/screenshot_table_extraction

- model_id: `meta/muse-spark-1.2`
- success: True  | final: 7.23 | quality: 8.0
- latency_total: 9.244s | tokens_per_second: 264.3
- input_tokens: 362 | output_tokens: 2443

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
    { "metrica": "MRR", "enero": 45200, "febrero": 48700, "marzo": 52100, "var_mm_marzo": "+7.0%" },
    { "metrica": "Churn Rate", "enero": 4.2, "febrero": 3.8, "marzo": 3.1, "var_mm_marzo": "-0.7pp", "unidad": "%" },
    { "metrica": "NPS", "enero": 42, "febrero": 45, "marzo": 51, "var_mm_marzo": "+6" },
    { "metrica": "CAC", "enero": 234, "febrero": 198, "marzo": 187, "var_mm_marzo": "-$11", "unidad": "USD" },
    { "metrica": "LTV", "enero": 1890, "febrero": 2010, "marzo": 2340, "var_mm_marzo": "+$330", "unidad": "USD" },
    { "metrica": "Active Users", "enero": 1234, "febrero": 1456, "marzo": 1678, "var_mm_marzo": "+15.3%" },
    { "metrica": "Support Tickets", "enero": 89, "febrero": 76, "marzo": 63, "var_mm_marzo": "-17.1%" },
    { "metrica": "Avg Response (h)", "enero": 4.2, "febrero": 3.1, "marzo": 2.4, "var_mm_marzo": "-0.7" }
  ],
  "calculo_ltv_cac_ratio": {
    "formula": "LTV / CAC",
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51,
    "detalle": {
      "enero": "1890 / 234 = 8.08",
      "febrero": "2010 / 198 = 10.15",
      "marzo": "2340 / 187 = 12.51"
    },
    "interpretacion": "Ratio mejora cada mes, ideal >3. En marzo es excelente (12.51)"
  },
  "metrica_mayor_mejora_porcentual": {
    "periodo_analizado": "Febrero -> Marzo (Var M/M)",
    "variaciones_porcentuales": {
      "MRR": 6.98,
      "Churn Rate": -18.42,
      "NPS": 13.33,
      "CAC": -5.56,
      "LTV": 16.42,
      "Active Users": 15.25,
      "Support Tickets": -17.11,
      "Avg Response (h)": -22.58
    },
    "mayor_mejora_absoluta": {
      "metrica": "Avg Response (h)",
      "variacion": "-22.58%",
      "detalle": "(2.4 - 3.1) / 3.1 * 100"
    },
    "mayor_mejora_por_crecimiento": {
      "metrica": "LTV",
      "variacion": "+16.42%",
      "detalle": "(2340 - 2010) / 2010 * 100"
    },
    "nota": "Si se considera mejora como reducción de métricas negativas, Avg Response es la mayor. Si se considera solo crecimiento positivo, LTV es la mayor."
  },
  "proyeccion_abril_2026": {
    "metodologia": "Se aplica la misma variación M/M de Marzo (absoluta para Churn, NPS, CAC, LTV, Avg Response y porcentual para MRR, Active Users, Support Tickets)",
    "valores_proyectados": {
      "MRR": 55747,
      "MRR_formateado": "$55.7K",
      "calculo_MRR": "52100 * 1.07",
      "Churn Rate": 2.4,
      "Churn Rate_formateado": "2.4%",
      "calculo_Churn": "3.1 - 0.7",
      "NPS": 57,
      "calculo_NPS": "51 + 6",
      "CAC": 176,
      "CAC_formateado": "$176",
      "calculo_CAC": "187 - 11",
      "LTV": 2670,
      "LTV_formateado": "$2,670",
      "calculo_LTV": "2340 + 330",
      "Active Users": 1935,
      "calculo_Active_Users": "1678 * 1.153",
      "Support Tickets": 52,
      "calculo_Support_Tickets": "63 * (1 - 0.171)",
      "Avg Response (h)": 1.7,
      "calculo_Avg_Response": "2.4 - 0.7",
      "LTV_CAC_ratio_proyectado": 15.17,
      "calculo_ratio": "2670 / 176"
    },
    "advertencia": "Proyección lineal simple. No considera estacionalidad ni límites naturales (ej. Churn no puede ser <0, Avg Response tiene límite inferior)."
  }
}
```