# Llama 4 Scout 17B (Groq preview) — ocr_extraction/screenshot_table_extraction

- model_id: `meta-llama/llama-4-scout-17b-16e-instruct`
- success: True  | final: 7.06 | quality: 6.32
- latency_total: 2.719s | tokens_per_second: 392.4
- input_tokens: 365 | output_tokens: 1067
- judge_score: 3.2 | justificación: 

## Respuesta completa

**Resumen de datos y análisis**

```json
{
  "dashboard": {
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "metricas": [
      {
        "nombre": "MRR",
        "enero": 45200,
        "febrero": 48700,
        "marzo": 52100,
        "var_mensual": 7.0
      },
      {
        "nombre": "Churn Rate",
        "enero": 4.2,
        "febrero": 3.8,
        "marzo": 3.1,
        "var_mensual": -0.7
      },
      {
        "nombre": "NPS",
        "enero": 42,
        "febrero": 45,
        "marzo": 51,
        "var_mensual": 6
      },
      {
        "nombre": "CAC",
        "enero": 234,
        "febrero": 198,
        "marzo": 187,
        "var_mensual": -11
      },
      {
        "nombre": "LTV",
        "enero": 1890,
        "febrero": 2010,
        "marzo": 2340,
        "var_mensual": 330
      },
      {
        "nombre": "Active Users",
        "enero": 1234,
        "febrero": 1456,
        "marzo": 1678,
        "var_mensual": 15.3
      },
      {
        "nombre": "Support Tickets",
        "enero": 89,
        "febrero": 76,
        "marzo": 63,
        "var_mensual": -17.1
      },
      {
        "nombre": "Avg Response (h)",
        "enero": 4.2,
        "febrero": 3.1,
        "marzo": 2.4,
        "var_mensual": -0.7
      }
    ]
  },
  "calculos": {
    "ltv_cac_ratio": [
      {"mes": "Enero", "ratio": 1890 / 234},
      {"mes": "Febrero", "ratio": 2010 / 198},
      {"mes": "Marzo", "ratio": 2340 / 187}
    ],
    "metrica_mejor_porcentual": {
      "nombre": "Active Users",
      "porcentaje": 15.3
    },
    "proyecciones_abril": [
      {"nombre": "MRR", "proyeccion": 52100 * 1.07},
      {"nombre": "Churn Rate", "proyeccion": 3.1 * 0.9},
      {"nombre": "NPS", "proyeccion": 51 + 6},
      {"nombre": "CAC", "proyeccion": 187 - 11},
      {"nombre": "LTV", "proyeccion": 2340 + 330},
      {"nombre": "Active Users", "proyeccion": 1678 * 1.153},
      {"nombre": "Support Tickets", "proyeccion": 63 * 0.829},
      {"nombre": "Avg Response (h)", "proyeccion": 2.4 - 0.7}
    ]
  }
}
```

**Cálculos detallados**

### LTV/CAC ratio para cada mes

| Mes     | LTV   | CAC   | LTV/CAC |
|---------|-------|-------|---------|
| Enero   | $1890 | $234  | 8.08    |
| Febrero | $2010 | $198  | 10.15   |
| Marzo   | $2340 | $187  | 12.51   |

### Identificación de la métrica con mayor mejora porcentual

La métrica con mayor mejora porcentual es **Active Users** con un aumento del **15.3%**.

### Proyección de valores para Abril

Asumiendo que la tendencia se mantiene, se proyectan los valores para Abril de la siguiente manera:

*   MRR: `$52.1K * 1.07 = $55.8K`
*   Churn Rate: `3.1% * 0.9 = 2.79%`
*   NPS: `51 + 6 = 57`
*   CAC: `$187 - $11 = $176`
*   LTV: `$2,340 + $330 = $2,670`
*   Active Users: `1,678 * 1.153 = 1,935`
*   Support Tickets: `63 * 0.829 = 52`
*   Avg Response (h): `2.4 - 0.7 = 1.7`

Es importante tener en cuenta que estas proyecciones son solo una estimación y pueden variar según factores externos e internos que afecten las métricas.