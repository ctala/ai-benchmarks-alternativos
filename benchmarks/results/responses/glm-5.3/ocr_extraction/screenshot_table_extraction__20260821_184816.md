# GLM 5.3 — ocr_extraction/screenshot_table_extraction

- model_id: `z-ai/glm-5.3`
- success: True  | final: 6.66 | quality: 8.0
- latency_total: 155.25s | tokens_per_second: 93.9
- input_tokens: 395 | output_tokens: 14576

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
  "datos_extraidos": {
    "tendencia_general": "Positiva en todas las métricas",
    "metricas": [
      { "metrica": "MRR", "unidad": "USD (miles)", "enero": 45.2, "febrero": 48.7, "marzo": 52.1, "var_mm_reportado": "+7.0%" },
      { "metrica": "Churn Rate", "unidad": "%", "enero": 4.2, "febrero": 3.8, "marzo": 3.1, "var_mm_reportado": "-0.7pp" },
      { "metrica": "NPS", "unidad": "puntos", "enero": 42, "febrero": 45, "marzo": 51, "var_mm_reportado": "+6" },
      { "metrica": "CAC", "unidad": "USD", "enero": 234, "febrero": 198, "marzo": 187, "var_mm_reportado": "-$11" },
      { "metrica": "LTV", "unidad": "USD", "enero": 1890, "febrero": 2010, "marzo": 2340, "var_mm_reportado": "+$330" },
      { "metrica": "Active Users", "unidad": "usuarios", "enero": 1234, "febrero": 1456, "marzo": 1678, "var_mm_reportado": "+15.3%" },
      { "metrica": "Support Tickets", "unidad": "tickets", "enero": 89, "febrero": 76, "marzo": 63, "var_mm_reportado": "-17.1%" },
      { "metrica": "Avg Response", "unidad": "horas", "enero": 4.2, "febrero": 3.1, "marzo": 2.4, "var_mm_reportado": "-0.7" }
    ]
  },
  "analisis": {
    "ltv_cac_ratio": {
      "formula": "LTV / CAC",
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "variacion_enero_marzo_pct": 54.9,
      "interpretacion": "Ratio muy superior al umbral de referencia de 3.0; la eficiencia de adquisición mejoró ~55% en el trimestre"
    },
    "mayor_mejora_porcentual": {
      "metrica": "Avg Response (h)",
      "mejora_pct_enero_marzo": 42.9,
      "detalle": "Pasó de 4.2h a 2.4h. Al ser una métrica donde menor es mejor, la reducción del 42.9% es la mayor mejora relativa del dashboard. También lidera el cambio M/M (-22.6%)",
      "aclaracion": "Si solo se consideran métricas donde mayor valor es mejor, la mayor mejora sería Active Users (+36.0% Enero→Marzo)",
      "ranking_enero_marzo": [
        { "metrica": "Avg Response (h)", "mejora_pct": 42.9, "direccion_favorable": "menor" },
        { "metrica": "Active Users", "mejora_pct": 36.0, "direccion_favorable": "mayor" },
        { "metrica": "Support Tickets", "mejora_pct": 29.2, "direccion_favorable": "menor" },
        { "metrica": "Churn Rate", "mejora_pct": 26.2, "direccion_favorable": "menor" },
        { "metrica": "LTV", "mejora_pct": 23.8, "direccion_favorable": "mayor" },
        { "metrica": "NPS", "mejora_pct": 21.4, "direccion_favorable": "mayor" },
        { "metrica": "CAC", "mejora_pct": 20.1, "direccion_favorable": "menor" },
        { "metrica": "MRR", "mejora_pct": 15.3, "direccion_favorable": "mayor" }
      ]
    }
  },
  "proyeccion_abril": {
    "metodologia": "Se aplica a marzo el mismo cambio porcentual observado entre febrero y marzo (calculado sobre los valores crudos)",
    "valores": [
      { "metrica": "MRR", "abril_proyectado": 55.7, "unidad": "USD (miles)", "cambio_aplicado_pct": 7.0 },
      { "metrica": "Churn Rate", "abril_proyectado": 2.5, "unidad": "%", "cambio_aplicado_pct": -18.4 },
      { "metrica": "NPS", "abril_proyectado": 58, "unidad": "puntos", "cambio_aplicado_pct": 13.3 },
      { "metrica": "CAC", "abril_proyectado": 177, "unidad": "USD", "cambio_aplicado_pct": -5.6 },
      { "metrica": "LTV", "abril_proyectado": 2724, "unidad": "USD", "cambio_aplicado_pct": 16.4 },
      { "metrica": "Active Users", "abril_proyectado": 1934, "unidad": "usuarios", "cambio_aplicado_pct": 15.2 },
      { "metrica": "Support Tickets", "abril_proyectado": 52, "unidad": "tickets", "cambio_aplicado_pct": -17.1 },
      { "metrica": "Avg Response", "abril_proyectado": 1.9, "unidad": "horas", "cambio_aplicado_pct": -22.6 }
    ],
    "ltv_cac_ratio_abril_proyectado": 15.4
  },
  "notas": [
    "El Var M/M reportado para Active Users (+15.3%) difiere levemente del calculado con los valores crudos (+15.2%); las proyecciones usan los valores crudos.",
    "Active Users (+222/mes) y Support Tickets (-13/mes) muestran variación absoluta constante; una proyección lineal daría 1,900 y 50 respectivamente.",
    "Las proyecciones asumen continuidad de la tendencia reciente; métricas con cambio acelerado (Churn, LTV) o desacelerado (CAC) podrían desviarse del modelo."
  ]
}
```