# Qwen 3.8 Max 0902 — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 6.5 | quality: 8.0
- latency_total: 254.335s | tokens_per_second: 43.9
- input_tokens: 478 | output_tokens: 11175

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

{
  "dashboard": "DASHBOARD - KPIs Marzo 2026",
  "tendencia_general": "↑ Positiva en todas las metricas",
  "datos_extraidos": {
    "MRR": {
      "Enero": "$45.2K",
      "Feb": "$48.7K",
      "Marzo": "$52.1K",
      "Var_M/M": "+7.0%",
      "valores_numericos_usd": {
        "Enero": 45200,
        "Feb": 48700,
        "Marzo": 52100
      }
    },
    "Churn Rate": {
      "Enero": "4.2%",
      "Feb": "3.8%",
      "Marzo": "3.1%",
      "Var_M/M": "-0.7pp",
      "valores_numericos_pct": {
        "Enero": 4.2,
        "Feb": 3.8,
        "Marzo": 3.1
      }
    },
    "NPS": {
      "Enero": 42,
      "Feb": 45,
      "Marzo": 51,
      "Var_M/M": "+6"
    },
    "CAC": {
      "Enero": "$234",
      "Feb": "$198",
      "Marzo": "$187",
      "Var_M/M": "-$11",
      "valores_numericos_usd": {
        "Enero": 234,
        "Feb": 198,
        "Marzo": 187
      }
    },
    "LTV": {
      "Enero": "$1,890",
      "Feb": "$2,010",
      "Marzo": "$2,340",
      "Var_M/M": "+$330",
      "valores_numericos_usd": {
        "Enero": 1890,
        "Feb": 2010,
        "Marzo": 2340
      }
    },
    "Active Users": {
      "Enero": 1234,
      "Feb": 1456,
      "Marzo": 1678,
      "Var_M/M": "+15.3%"
    },
    "Support Tickets": {
      "Enero": 89,
      "Feb": 76,
      "Marzo": 63,
      "Var_M/M": "-17.1%"
    },
    "Avg Response (h)": {
      "Enero": 4.2,
      "Feb": 3.1,
      "Marzo": 2.4,
      "Var_M/M": "-0.7"
    }
  },
  "ltv_cac_ratio": {
    "formula": "LTV / CAC",
    "Enero": 8.08,
    "Feb": 10.15,
    "Marzo": 12.51
  },
  "mejoras_porcentuales_calculadas_feb_mar_pct": {
    "MRR": 6.98,
    "Churn Rate": 18.42,
    "NPS": 13.33,
    "CAC": 5.56,
    "LTV": 16.42,
    "Active Users": 15.25,
    "Support Tickets": 17.11,
    "Avg Response (h)": 22.58,
    "nota": "En Churn Rate, CAC, Support Tickets y Avg Response (h), una reducción se interpreta como mejora; por eso se calculó la reducción relativa."
  },
  "metrica_con_mayor_mejora_porcentual": {
    "metrica": "Avg Response (h)",
    "mejora_pct": 22.58,
    "explicacion": "El tiempo medio de respuesta bajó de 3.1 h en Feb a 2.4 h en Marzo, lo que equivale a una mejora relativa de 22.58%.",
    "nota": "Si se consideran solo las variaciones porcentuales visibles en la columna Var M/M, Support Tickets muestra -17.1% como mayor reducción favorable y Active Users +15.3% como mayor incremento favorable."
  },
  "proyeccion_abril": {
    "supuesto": "Se mantiene la variación mensual Feb->Mar mostrada en el dashboard: porcentual para MRR, Active Users y Support Tickets; puntos porcentuales para Churn Rate; variación absoluta para NPS, CAC, LTV y Avg Response (h).",
    "valores_proyectados": {
      "MRR": {
        "valor": "$55.7K",
        "numerico_usd": 55700
      },
      "Churn Rate": {
        "valor": "2.4%",
        "numerico_pct": 2.4
      },
      "NPS": {
        "valor": 57,
        "numerico": 57
      },
      "CAC": {
        "valor": "$176",
        "numerico_usd": 176
      },
      "LTV": {
        "valor": "$2,670",
        "numerico_usd": 2670
      },
      "Active Users": {
        "valor": 1935,
        "numerico": 1935
      },
      "Support Tickets": {
        "valor": 52,
        "numerico": 52
      },
      "Avg Response (h)": {
        "valor": 1.7,
        "numerico_horas": 1.7
      }
    },
    "ltv_cac_ratio_proyectado_abril": 15.17
  }
}