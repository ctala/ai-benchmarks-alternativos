# Qwen 3.7 Max — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3.7-max`
- success: True  | final: 5.48 | quality: 6.32
- latency_total: 41.545s | tokens_per_second: 69.1
- input_tokens: 427 | output_tokens: 2870
- judge_score: 3.2 | justificación: 

## Respuesta completa

```json
{
  "dashboard": {
    "titulo": "KPIs Marzo 2026",
    "tendencia_general": "Positiva en todas las métricas"
  },
  "datos_extraidos": [
    { "metrica": "MRR",              "enero": "$45.2K", "febrero": "$48.7K", "marzo": "$52.1K", "var_mm": "+7.0%"  },
    { "metrica": "Churn Rate",       "enero": "4.2%",   "febrero": "3.8%",   "marzo": "3.1%",   "var_mm": "-0.7pp" },
    { "metrica": "NPS",              "enero": 42,        "febrero": 45,        "marzo": 51,        "var_mm": "+6"     },
    { "metrica": "CAC",              "enero": "$234",    "febrero": "$198",    "marzo": "$187",    "var_mm": "-$11"   },
    { "metrica": "LTV",              "enero": "$1,890",  "febrero": "$2,010",  "marzo": "$2,340",  "var_mm": "+$330"  },
    { "metrica": "Active Users",     "enero": 1234,      "febrero": 1456,      "marzo": 1678,      "var_mm": "+15.3%" },
    { "metrica": "Support Tickets",  "enero": 89,        "febrero": 76,        "marzo": 63,        "var_mm": "-17.1%" },
    { "metrica": "Avg Response (h)", "enero": 4.2,       "febrero": 3.1,       "marzo": 2.4,       "var_mm": "-0.7"   }
  ],

  "ltv_cac_ratio": {
    "descripcion": "Relación Lifetime Value / Customer Acquisition Cost (mayor = más eficiente)",
    "valores": {
      "enero":   { "ltv": 1890, "cac": 234, "ratio": 8.08 },
      "febrero": { "ltv": 2010, "cac": 198, "ratio": 10.15 },
      "marzo":   { "ltv": 2340, "cac": 187, "ratio": 12.51 }
    },
    "interpretacion": "El ratio se duplicó casi en un trimestre (8.08 → 12.51), lo que indica una mejora drástica en eficiencia de adquisición."
  },

  "metrica_mayor_mejora": {
    "metrica": "Avg Response (h)",
    "categoria": "Soporte",
    "valor_anterior": 3.1,
    "valor_actual": 2.4,
    "mejora_porcentual": "22.58%",
    "detalle_calculos": [
      { "metrica": "Avg Response (h)", "mejora_pct": 22.58, "direccion": "menor_es_mejor" },
      { "metrica": "Churn Rate",       "mejora_pct": 18.42, "direccion": "menor_es_mejor" },
      { "metrica": "Support Tickets",  "mejora_pct": 17.10, "direccion": "menor_es_mejor" },
      { "metrica": "LTV",              "mejora_pct": 16.42, "direccion": "mayor_es_mejor" },
      { "metrica": "Active Users",     "mejora_pct": 15.30, "direccion": "mayor_es_mejor" },
      { "metrica": "NPS",              "mejora_pct": 13.33, "direccion": "mayor_es_mejor" },
      { "metrica": "MRR",              "mejora_pct":  7.00, "direccion": "mayor_es_mejor" },
      { "metrica": "CAC",              "mejora_pct":  5.56, "direccion": "menor_es_mejor" }
    ]
  },

  "proyeccion_abril": {
    "metodo": "Extrapolación lineal de la variación M/M (Feb→Mar) aplicada sobre el valor de Marzo",
    "valores": {
      "MRR":              { "valor": "$55.7K", "calculo": "$52.1K × 1.07"        },
      "Churn Rate":       { "valor": "2.4%",   "calculo": "3.1% - 0.7pp"         },
      "NPS":              { "valor": 57,        "calculo": "51 + 6"               },
      "CAC":              { "valor": "$176",    "calculo": "$187 - $11"           },
      "LTV":              { "valor": "$2,670",  "calculo": "$2,340 + $330"        },
      "Active Users":     { "valor": 1935,      "calculo": "1,678 × 1.153"        },
      "Support Tickets":  { "valor": 52,        "calculo": "63 × 0.829"           },
      "Avg Response (h)": { "valor": 1.7,       "calculo": "2.4 - 0.7"            }
    },
    "ltv_cac_proyectado": {
      "ratio": 15.17,
      "calculo": "$2,670 / $176"
    },
    "advertencia": "Proyección lineal simplificada. En la práctica, las métricas suelen mostrar rendimientos decrecientes y estacionalidad."
  }
}
```

### Resumen ejecutivo rápido

| Insight | Hallazgo |
|---|---|
| **LTV/CAC** | Pasó de **8.08** a **12.51** en 3 meses. Se proyecta **15.17** para abril — el negocio es cada vez más eficiente adquiriendo usuarios. |
| **Mayor mejora** | **Avg Response (h)** con **-22.58%** — el equipo de soporte está respondiendo casi una hora más rápido cada mes. |
| **Riesgo a vigilar** | El Churn Rate bajando a **2.4%** proyectado es agresivo; por debajo del 2% es difícil de sostir sin cambios estructurales. |