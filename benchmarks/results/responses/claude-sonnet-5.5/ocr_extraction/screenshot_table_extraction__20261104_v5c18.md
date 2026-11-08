# Claude Sonnet 5.5 — ocr_extraction/screenshot_table_extraction

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 6.9 | quality: 8.0
- latency_total: 25.107s | tokens_per_second: 156.2
- input_tokens: 514 | output_tokens: 3922

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
  "fuente": "Datos transcritos del texto del dashboard",
  "datos_extraidos": {
    "MRR":              { "unidad": "USD (miles)", "enero": 45.2, "febrero": 48.7, "marzo": 52.1, "var_mm_reportada": "+7.0%", "mejor_si": "sube" },
    "churn_rate":       { "unidad": "%", "enero": 4.2, "febrero": 3.8, "marzo": 3.1, "var_mm_reportada": "-0.7pp", "mejor_si": "baja" },
    "NPS":              { "unidad": "puntos", "enero": 42, "febrero": 45, "marzo": 51, "var_mm_reportada": "+6", "mejor_si": "sube" },
    "CAC":              { "unidad": "USD", "enero": 234, "febrero": 198, "marzo": 187, "var_mm_reportada": "-11", "mejor_si": "baja" },
    "LTV":              { "unidad": "USD", "enero": 1890, "febrero": 2010, "marzo": 2340, "var_mm_reportada": "+330", "mejor_si": "sube" },
    "usuarios_activos": { "unidad": "usuarios", "enero": 1234, "febrero": 1456, "marzo": 1678, "var_mm_reportada": "+15.3%", "mejor_si": "sube" },
    "tickets_soporte":  { "unidad": "tickets", "enero": 89, "febrero": 76, "marzo": 63, "var_mm_reportada": "-17.1%", "mejor_si": "baja" },
    "respuesta_promedio": { "unidad": "horas", "enero": 4.2, "febrero": 3.1, "marzo": 2.4, "var_mm_reportada": "-0.7", "mejor_si": "baja" }
  },
  "tendencia_general_reportada": "Positiva en todas las metricas",

  "verificacion_variaciones_mm": {
    "MRR": "+6.98% (coincide con +7.0%)",
    "usuarios_activos": "+15.25% (coincide con +15.3%)",
    "tickets_soporte": "-17.11% (coincide con -17.1%)",
    "resto": "Las variaciones absolutas coinciden con los datos",
    "inconsistencias": []
  },

  "1_ratio_LTV_CAC": {
    "enero":   { "LTV": 1890, "CAC": 234, "ratio": 8.08 },
    "febrero": { "LTV": 2010, "CAC": 198, "ratio": 10.15 },
    "marzo":   { "LTV": 2340, "CAC": 187, "ratio": 12.51 },
    "variacion_ene_a_mar": "+54.9%",
    "lectura": "Muy por encima del benchmark de 3x. Un ratio tan alto puede indicar subinversión en adquisición."
  },

  "2_mayor_mejora_porcentual": {
    "metrica": "Tiempo de respuesta promedio (h)",
    "mejora_mm_feb_a_mar": "-22.58% (3.1h a 2.4h)",
    "mejora_ene_a_mar": "-42.86% (4.2h a 2.4h)",
    "ranking_mm_feb_a_mar": [
      { "metrica": "respuesta_promedio", "mejora_pct": 22.58 },
      { "metrica": "churn_rate", "mejora_pct": 18.42 },
      { "metrica": "tickets_soporte", "mejora_pct": 17.11 },
      { "metrica": "LTV", "mejora_pct": 16.42 },
      { "metrica": "usuarios_activos", "mejora_pct": 15.25 },
      { "metrica": "NPS", "mejora_pct": 13.33 },
      { "metrica": "MRR", "mejora_pct": 6.98 },
      { "metrica": "CAC", "mejora_pct": 5.56 }
    ],
    "nota": "Si se mide Ene→Mar, la mejor sigue siendo respuesta_promedio. El mayor crecimiento en valor positivo es usuarios_activos (+35.98%)."
  },

  "3_proyeccion_abril": {
    "metodos": {
      "lineal": "Marzo + promedio de cambios mensuales absolutos ((Mar - Ene) / 2)",
      "geometrico": "Marzo × tasa de crecimiento compuesto mensual ((Mar / Ene)^(1/2))"
    },
    "valores": {
      "MRR_K_USD":          { "lineal": 55.55, "geometrico": 55.9 },
      "churn_rate_pct":     { "lineal": 2.55,  "geometrico": 2.66 },
      "NPS":                { "lineal": 55.5,  "geometrico": 56.2 },
      "CAC_USD":            { "lineal": 163.5, "geometrico": 167.2 },
      "LTV_USD":            { "lineal": 2565,  "geometrico": 2604 },
      "usuarios_activos":   { "lineal": 1900,  "geometrico": 1957 },
      "tickets_soporte":    { "lineal": 50,    "geometrico": 53 },
      "respuesta_promedio_h": { "lineal": 1.5, "geometrico": 1.81 },
      "LTV_CAC_ratio":      { "lineal": 15.69, "geometrico": 15.58 }
    },
    "rango_recomendado": "Usar ambos valores como rango (escenario conservador y optimista)"
  },

  "advertencias": [
    "Solo hay 3 puntos de datos, así que las proyecciones tienen baja confiabilidad estadística.",
    "Las metricas con piso natural (churn, tiempo de respuesta, tickets, CAC) probablemente no mantengan la tendencia: habrá rendimientos decrecientes.",
    "El NPS tiene un máximo de 100 y la mejora suele desacelerarse al subir.",
    "El LTV depende del churn; si el churn se estabiliza, el LTV proyectado podría estar sobreestimado.",
    "Los datos están transcritos del texto. Conviene validarlos contra la captura original."
  ]
}
```

Si quieres, puedo añadir una proyección con otro método, como regresión o escenarios con desaceleración, o convertir esto a CSV.