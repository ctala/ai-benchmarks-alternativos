# Kimi K2.7 Code — ocr_extraction/screenshot_table_extraction

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 6.85 | quality: 8.0
- latency_total: 105.697s | tokens_per_second: 64.4
- input_tokens: 385 | output_tokens: 6812

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
  "titulo": "DASHBOARD - KPIs Marzo 2026",
  "datos_extraidos": {
    "periodos": ["Enero", "Febrero", "Marzo"],
    "metricas": [
      {
        "nombre": "MRR",
        "unidad": "USD",
        "formato": "miles",
        "valores": { "enero": 45.2, "febrero": 48.7, "marzo": 52.1 },
        "variacion_mm": "+7.0%"
      },
      {
        "nombre": "Churn Rate",
        "unidad": "%",
        "valores": { "enero": 4.2, "febrero": 3.8, "marzo": 3.1 },
        "variacion_mm": "-0.7pp"
      },
      {
        "nombre": "NPS",
        "unidad": "puntos",
        "valores": { "enero": 42, "febrero": 45, "marzo": 51 },
        "variacion_mm": "+6"
      },
      {
        "nombre": "CAC",
        "unidad": "USD",
        "valores": { "enero": 234, "febrero": 198, "marzo": 187 },
        "variacion_mm": "-$11"
      },
      {
        "nombre": "LTV",
        "unidad": "USD",
        "valores": { "enero": 1890, "febrero": 2010, "marzo": 2340 },
        "variacion_mm": "+$330"
      },
      {
        "nombre": "Active Users",
        "unidad": "usuarios",
        "valores": { "enero": 1234, "febrero": 1456, "marzo": 1678 },
        "variacion_mm": "+15.3%"
      },
      {
        "nombre": "Support Tickets",
        "unidad": "tickets",
        "valores": { "enero": 89, "febrero": 76, "marzo": 63 },
        "variacion_mm": "-17.1%"
      },
      {
        "nombre": "Avg Response",
        "unidad": "horas",
        "valores": { "enero": 4.2, "febrero": 3.1, "marzo": 2.4 },
        "variacion_mm": "-0.7"
      }
    ]
  },
  "calculos": {
    "ltv_cac_ratio": {
      "descripcion": "LTV dividido por CAC. Ratio > 3x generalmente considerado saludable.",
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "tendencia": "Mejora continua: de 8.08x a 12.51x en el trimestre"
    }
  },
  "analisis": {
    "mayor_mejora_porcentual": {
      "metrica": "Avg Response (h)",
      "mejora_porcentual": "22.58%",
      "detalle": "El tiempo de respuesta promedio se redujo de 3.1h a 2.4h, siendo la mayor mejora relativa del mes."
    },
    "ranking_mejoras_marzo_vs_febrero": [
      { "metrica": "Avg Response (h)", "mejora_porcentual": 22.58, "tipo": "disminucion_es_mejor" },
      { "metrica": "Churn Rate", "mejora_porcentual": 18.42, "tipo": "disminucion_es_mejor" },
      { "metrica": "Support Tickets", "mejora_porcentual": 17.11, "tipo": "disminucion_es_mejor" },
      { "metrica": "LTV", "mejora_porcentual": 16.42, "tipo": "aumento_es_mejor" },
      { "metrica": "Active Users", "mejora_porcentual": 15.25, "tipo": "aumento_es_mejor" },
      { "metrica": "NPS", "mejora_porcentual": 13.33, "tipo": "aumento_es_mejor" },
      { "metrica": "MRR", "mejora_porcentual": 6.98, "tipo": "aumento_es_mejor" },
      { "metrica": "CAC", "mejora_porcentual": 5.56, "tipo": "disminucion_es_mejor" }
    ]
  },
  "proyeccion_abril": {
    "metodologia": "Aplicar la variación mes/mes observada en marzo sobre los valores de marzo",
    "supuestos": "Se mantiene la tendencia reciente de cada métrica",
    "valores": {
      "MRR": "$55.7K",
      "Churn Rate": "2.4%",
      "NPS": 57,
      "CAC": "$176",
      "LTV": "$2,670",
      "Active Users": 1935,
      "Support Tickets": 52,
      "Avg Response (h)": 1.7
    },
    "ltv_cac_ratio_proyectado": 15.17,
    "nota": "Proyección lineal basada en la última variación reportada. No considera estacionalidad ni factores externos."
  }
}
```