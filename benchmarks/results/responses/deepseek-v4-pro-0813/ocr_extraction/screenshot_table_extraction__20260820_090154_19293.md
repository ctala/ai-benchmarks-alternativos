# DeepSeek V4 Pro (0813) — ocr_extraction/screenshot_table_extraction

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 6.77 | quality: 8.0
- latency_total: 223.756s | tokens_per_second: 81.8
- input_tokens: 465 | output_tokens: 18298

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
  "tendencia_general": "↑ Positiva en todas las métricas",
  "datos_extraidos": [
    {
      "metrica": "MRR",
      "unidad": "USD",
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "var_mm": {
        "valor": 0.07,
        "tipo": "relativa"
      }
    },
    {
      "metrica": "Churn Rate",
      "unidad": "porcentaje",
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "var_mm": {
        "valor": -0.7,
        "tipo": "puntos_porcentuales"
      }
    },
    {
      "metrica": "NPS",
      "unidad": "puntos",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "var_mm": {
        "valor": 6,
        "tipo": "absoluta"
      }
    },
    {
      "metrica": "CAC",
      "unidad": "USD",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "var_mm": {
        "valor": -11,
        "tipo": "absoluta"
      }
    },
    {
      "metrica": "LTV",
      "unidad": "USD",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "var_mm": {
        "valor": 330,
        "tipo": "absoluta"
      }
    },
    {
      "metrica": "Active Users",
      "unidad": "usuarios",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "var_mm": {
        "valor": 0.153,
        "tipo": "relativa"
      }
    },
    {
      "metrica": "Support Tickets",
      "unidad": "tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "var_mm": {
        "valor": -0.171,
        "tipo": "relativa"
      }
    },
    {
      "metrica": "Avg Response (h)",
      "unidad": "horas",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "var_mm": {
        "valor": -0.7,
        "tipo": "absoluta"
      }
    }
  ],
  "ltv_cac_ratio": {
    "enero": {
      "ltv": 1890,
      "cac": 234,
      "ratio": 8.08
    },
    "febrero": {
      "ltv": 2010,
      "cac": 198,
      "ratio": 10.15
    },
    "marzo": {
      "ltv": 2340,
      "cac": 187,
      "ratio": 12.51
    }
  },
  "metrica_con_mayor_mejora_porcentual": {
    "criterio": "Mejora porcentual absoluta del cambio Febrero → Marzo",
    "metrica": "Avg Response (h)",
    "cambio_porcentual": -22.58,
    "mejora_porcentual_absoluta": 22.58,
    "nota": "La reducción de -22.58% en tiempo de respuesta es la mayor mejora relativa. Si solo se consideran métricas con Var M/M expresada en %, Support Tickets tiene -17.1%."
  },
  "ranking_mejoras_porcentuales_feb_mar": [
    {
      "metrica": "Avg Response (h)",
      "cambio_porcentual": -22.58
    },
    {
      "metrica": "Churn Rate",
      "cambio_porcentual": -18.42
    },
    {
      "metrica": "Support Tickets",
      "cambio_porcentual": -17.11
    },
    {
      "metrica": "LTV",
      "cambio_porcentual": 16.42
    },
    {
      "metrica": "Active Users",
      "cambio_porcentual": 15.25
    },
    {
      "metrica": "NPS",
      "cambio_porcentual": 13.33
    },
    {
      "metrica": "MRR",
      "cambio_porcentual": 6.98
    },
    {
      "metrica": "CAC",
      "cambio_porcentual": -5.56
    }
  ],
  "proyeccion_abril": {
    "metodo": "Se aplicó a Marzo la variación M/M observada entre Febrero y Marzo, según la columna Var M/M.",
    "valores": [
      {
        "metrica": "MRR",
        "unidad": "USD",
        "valor": 55747
      },
      {
        "metrica": "Churn Rate",
        "unidad": "porcentaje",
        "valor": 2.4
      },
      {
        "metrica": "NPS",
        "unidad": "puntos",
        "valor": 57
      },
      {
        "metrica": "CAC",
        "unidad": "USD",
        "valor": 176
      },
      {
        "metrica": "LTV",
        "unidad": "USD",
        "valor": 2670
      },
      {
        "metrica": "Active Users",
        "unidad": "usuarios",
        "valor": 1935,
        "nota": "Redondeado desde 1934.734"
      },
      {
        "metrica": "Support Tickets",
        "unidad": "tickets",
        "valor": 52,
        "nota": "Redondeado desde 52.227"
      },
      {
        "metrica": "Avg Response (h)",
        "unidad": "horas",
        "valor": 1.7
      }
    ]
  },
  "ltv_cac_ratio_abril_proyectado": 15.17
}