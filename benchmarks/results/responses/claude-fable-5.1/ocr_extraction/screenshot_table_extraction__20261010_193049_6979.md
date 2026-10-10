# Claude Fable 5.1 — ocr_extraction/screenshot_table_extraction

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 6.49 | quality: 8.0
- latency_total: 32.712s | tokens_per_second: 90.8
- input_tokens: 514 | output_tokens: 2969

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
    "tendencia_general": "Positiva en todas las métricas",
    "metricas": [
      {"nombre": "MRR", "unidad": "USD", "enero": 45200, "febrero": 48700, "marzo": 52100, "var_mm": "+7.0%", "menor_es_mejor": false},
      {"nombre": "Churn Rate", "unidad": "%", "enero": 4.2, "febrero": 3.8, "marzo": 3.1, "var_mm": "-0.7pp", "menor_es_mejor": true},
      {"nombre": "NPS", "unidad": "puntos", "enero": 42, "febrero": 45, "marzo": 51, "var_mm": "+6", "menor_es_mejor": false},
      {"nombre": "CAC", "unidad": "USD", "enero": 234, "febrero": 198, "marzo": 187, "var_mm": "-$11", "menor_es_mejor": true},
      {"nombre": "LTV", "unidad": "USD", "enero": 1890, "febrero": 2010, "marzo": 2340, "var_mm": "+$330", "menor_es_mejor": false},
      {"nombre": "Active Users", "unidad": "usuarios", "enero": 1234, "febrero": 1456, "marzo": 1678, "var_mm": "+15.3%", "menor_es_mejor": false},
      {"nombre": "Support Tickets", "unidad": "tickets", "enero": 89, "febrero": 76, "marzo": 63, "var_mm": "-17.1%", "menor_es_mejor": true},
      {"nombre": "Avg Response", "unidad": "horas", "enero": 4.2, "febrero": 3.1, "marzo": 2.4, "var_mm": "-0.7", "menor_es_mejor": true}
    ]
  },

  "analisis": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "formula": "LTV / CAC",
      "comentario": "Muy por encima del benchmark saludable (≥3x) y mejorando cada mes."
    },

    "mejora_porcentual": {
      "metodo": "Variación porcentual relativa; en métricas donde menor es mejor, una caída cuenta como mejora.",
      "feb_a_marzo": {
        "Avg Response": -22.58,
        "Churn Rate": -18.42,
        "Support Tickets": -17.11,
        "LTV": 16.42,
        "Active Users": 15.25,
        "NPS": 13.33,
        "MRR": 6.98,
        "CAC": -5.56
      },
      "enero_a_marzo": {
        "Avg Response": -42.86,
        "Active Users": 35.98,
        "Support Tickets": -29.21,
        "Churn Rate": -26.19,
        "LTV": 23.81,
        "NPS": 21.43,
        "CAC": -20.09,
        "MRR": 15.27
      },
      "metrica_mayor_mejora": {
        "nombre": "Avg Response (h)",
        "mejora_mm_pct": 22.58,
        "mejora_acumulada_pct": 42.86,
        "nota": "El dashboard muestra la variación como -0.7h (absoluta); en términos relativos es la mayor mejora tanto M/M como acumulada."
      }
    },

    "proyeccion_abril_2026": {
      "metodo": "Se mantiene la variación Feb→Marzo con la misma convención del dashboard: porcentual para MRR, Active Users y Tickets; absoluta para Churn (pp), NPS, CAC, LTV y Avg Response.",
      "valores": {
        "MRR": {"valor": 55740, "display": "$55.7K"},
        "Churn Rate": {"valor": 2.4, "display": "2.4%"},
        "NPS": {"valor": 57, "display": "57"},
        "CAC": {"valor": 176, "display": "$176"},
        "LTV": {"valor": 2670, "display": "$2,670"},
        "Active Users": {"valor": 1934, "display": "1,934"},
        "Support Tickets": {"valor": 52, "display": "52"},
        "Avg Response": {"valor": 1.7, "display": "1.7 h"}
      },
      "ltv_cac_ratio_proyectado": 15.17
    }
  },

  "notas": [
    "Las proyecciones son una extrapolación simple de un solo periodo; no consideran estacionalidad ni límites naturales (p. ej., Avg Response no puede bajar indefinidamente de forma lineal).",
    "La afirmación 'Positiva en todas las métricas' del dashboard es correcta: las 4 métricas que bajan (Churn, CAC, Tickets, Avg Response) son métricas donde menor es mejor."
  ]
}
```