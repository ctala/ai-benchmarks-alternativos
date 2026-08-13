# GPT-5.6 Terra Pro — ocr_extraction/screenshot_table_extraction

- model_id: `openai/gpt-5.6-terra-pro`
- success: True  | final: 6.86 | quality: 8.0
- latency_total: 27.646s | tokens_per_second: 242.4
- input_tokens: 9163 | output_tokens: 6702

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
  "dashboard": {
    "titulo": "KPIs Marzo 2026",
    "tendencia_general": "Positiva en todas las métricas"
  },
  "datos": [
    {
      "metrica": "MRR",
      "enero": {
        "valor": 45.2,
        "unidad": "miles_USD"
      },
      "febrero": {
        "valor": 48.7,
        "unidad": "miles_USD"
      },
      "marzo": {
        "valor": 52.1,
        "unidad": "miles_USD"
      },
      "variacion_mensual": {
        "valor": 7.0,
        "unidad": "porcentaje",
        "direccion": "aumento"
      }
    },
    {
      "metrica": "Churn Rate",
      "enero": {
        "valor": 4.2,
        "unidad": "porcentaje"
      },
      "febrero": {
        "valor": 3.8,
        "unidad": "porcentaje"
      },
      "marzo": {
        "valor": 3.1,
        "unidad": "porcentaje"
      },
      "variacion_mensual": {
        "valor": -0.7,
        "unidad": "puntos_porcentuales",
        "direccion": "reduccion"
      }
    },
    {
      "metrica": "NPS",
      "enero": {
        "valor": 42,
        "unidad": "puntos"
      },
      "febrero": {
        "valor": 45,
        "unidad": "puntos"
      },
      "marzo": {
        "valor": 51,
        "unidad": "puntos"
      },
      "variacion_mensual": {
        "valor": 6,
        "unidad": "puntos",
        "direccion": "aumento"
      }
    },
    {
      "metrica": "CAC",
      "enero": {
        "valor": 234,
        "unidad": "USD"
      },
      "febrero": {
        "valor": 198,
        "unidad": "USD"
      },
      "marzo": {
        "valor": 187,
        "unidad": "USD"
      },
      "variacion_mensual": {
        "valor": -11,
        "unidad": "USD",
        "direccion": "reduccion"
      }
    },
    {
      "metrica": "LTV",
      "enero": {
        "valor": 1890,
        "unidad": "USD"
      },
      "febrero": {
        "valor": 2010,
        "unidad": "USD"
      },
      "marzo": {
        "valor": 2340,
        "unidad": "USD"
      },
      "variacion_mensual": {
        "valor": 330,
        "unidad": "USD",
        "direccion": "aumento"
      }
    },
    {
      "metrica": "Active Users",
      "enero": {
        "valor": 1234,
        "unidad": "usuarios"
      },
      "febrero": {
        "valor": 1456,
        "unidad": "usuarios"
      },
      "marzo": {
        "valor": 1678,
        "unidad": "usuarios"
      },
      "variacion_mensual": {
        "valor": 15.3,
        "unidad": "porcentaje",
        "direccion": "aumento"
      }
    },
    {
      "metrica": "Support Tickets",
      "enero": {
        "valor": 89,
        "unidad": "tickets"
      },
      "febrero": {
        "valor": 76,
        "unidad": "tickets"
      },
      "marzo": {
        "valor": 63,
        "unidad": "tickets"
      },
      "variacion_mensual": {
        "valor": -17.1,
        "unidad": "porcentaje",
        "direccion": "reduccion"
      }
    },
    {
      "metrica": "Avg Response",
      "enero": {
        "valor": 4.2,
        "unidad": "horas"
      },
      "febrero": {
        "valor": 3.1,
        "unidad": "horas"
      },
      "marzo": {
        "valor": 2.4,
        "unidad": "horas"
      },
      "variacion_mensual": {
        "valor": -0.7,
        "unidad": "horas",
        "direccion": "reduccion"
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
    "metrica": "Avg Response",
    "variacion_febrero_a_marzo": {
      "valor_absoluto": -0.7,
      "unidad": "horas"
    },
    "mejora_porcentual": 22.58,
    "criterio": "La reducción del tiempo de respuesta es positiva; se calcula como 0.7 / 3.1 × 100."
  },
  "proyeccion_abril_2026": {
    "metodologia": "Se aplica la variación mensual observada entre febrero y marzo. Para métricas porcentuales se aplica la tasa indicada; para variaciones expresadas en valores absolutos o puntos porcentuales se mantiene el mismo incremento o reducción.",
    "metricas": [
      {
        "metrica": "MRR",
        "valor_proyectado": 55.75,
        "unidad": "miles_USD",
        "formato_display": "$55.7K",
        "supuesto": "Aumento de 7.0%"
      },
      {
        "metrica": "Churn Rate",
        "valor_proyectado": 2.4,
        "unidad": "porcentaje",
        "formato_display": "2.4%",
        "supuesto": "Reducción de 0.7 puntos porcentuales"
      },
      {
        "metrica": "NPS",
        "valor_proyectado": 57,
        "unidad": "puntos",
        "supuesto": "Aumento de 6 puntos"
      },
      {
        "metrica": "CAC",
        "valor_proyectado": 176,
        "unidad": "USD",
        "formato_display": "$176",
        "supuesto": "Reducción de $11"
      },
      {
        "metrica": "LTV",
        "valor_proyectado": 2670,
        "unidad": "USD",
        "formato_display": "$2,670",
        "supuesto": "Aumento de $330"
      },
      {
        "metrica": "Active Users",
        "valor_proyectado": 1935,
        "unidad": "usuarios",
        "supuesto": "Aumento de 15.3%, redondeado al usuario más cercano"
      },
      {
        "metrica": "Support Tickets",
        "valor_proyectado": 52,
        "unidad": "tickets",
        "supuesto": "Reducción de 17.1%, redondeado al ticket más cercano"
      },
      {
        "metrica": "Avg Response",
        "valor_proyectado": 1.7,
        "unidad": "horas",
        "supuesto": "Reducción de 0.7 horas"
      }
    ],
    "ltv_cac_ratio_proyectado": 15.17
  }
}