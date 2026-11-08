# GPT-5.6 Terra — ocr_extraction/screenshot_table_extraction

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 8.43 | quality: 10.0
- latency_total: 10.891s | tokens_per_second: 157.0
- input_tokens: 379 | output_tokens: 1710

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
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "periodo": "Marzo 2026",
    "tendencia_general": "Positiva en todas las metricas"
  },
  "metricas": [
    {
      "metrica": "MRR",
      "enero": {
        "valor": 45.2,
        "unidad": "K USD",
        "valor_usd": 45200
      },
      "febrero": {
        "valor": 48.7,
        "unidad": "K USD",
        "valor_usd": 48700
      },
      "marzo": {
        "valor": 52.1,
        "unidad": "K USD",
        "valor_usd": 52100
      },
      "variacion_mensual": {
        "valor": 7.0,
        "unidad": "%"
      }
    },
    {
      "metrica": "Churn Rate",
      "enero": {
        "valor": 4.2,
        "unidad": "%"
      },
      "febrero": {
        "valor": 3.8,
        "unidad": "%"
      },
      "marzo": {
        "valor": 3.1,
        "unidad": "%"
      },
      "variacion_mensual": {
        "valor": -0.7,
        "unidad": "puntos porcentuales"
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
        "unidad": "puntos"
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
        "unidad": "USD"
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
        "unidad": "USD"
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
        "unidad": "%"
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
        "unidad": "%"
      }
    },
    {
      "metrica": "Avg Response (h)",
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
        "unidad": "horas"
      }
    }
  ],
  "calculos": {
    "ltv_cac_ratio": {
      "enero": {
        "ltv_usd": 1890,
        "cac_usd": 234,
        "ratio": 8.08
      },
      "febrero": {
        "ltv_usd": 2010,
        "cac_usd": 198,
        "ratio": 10.15
      },
      "marzo": {
        "ltv_usd": 2340,
        "cac_usd": 187,
        "ratio": 12.51
      }
    },
    "metrica_con_mayor_mejora_porcentual": {
      "metrica": "Support Tickets",
      "mejora_porcentual": 17.1,
      "direccion": "reduccion",
      "detalle": "La reducción de tickets de soporte es favorable; descendió de 76 en febrero a 63 en marzo."
    }
  },
  "proyeccion_abril": {
    "metodologia": "Se replica la variación observada entre febrero y marzo. Para métricas expresadas en porcentaje se aplica la misma variación relativa cuando corresponde; para métricas con variación absoluta mostrada en el dashboard se aplica el mismo cambio absoluto.",
    "valores": [
      {
        "metrica": "MRR",
        "abril": {
          "valor": 55.75,
          "unidad": "K USD",
          "valor_usd": 55747
        },
        "supuesto": "Crecimiento mensual de 7.0%"
      },
      {
        "metrica": "Churn Rate",
        "abril": {
          "valor": 2.4,
          "unidad": "%"
        },
        "supuesto": "Reducción de 0.7 puntos porcentuales"
      },
      {
        "metrica": "NPS",
        "abril": {
          "valor": 57,
          "unidad": "puntos"
        },
        "supuesto": "Aumento de 6 puntos"
      },
      {
        "metrica": "CAC",
        "abril": {
          "valor": 176,
          "unidad": "USD"
        },
        "supuesto": "Reducción de 11 USD"
      },
      {
        "metrica": "LTV",
        "abril": {
          "valor": 2670,
          "unidad": "USD"
        },
        "supuesto": "Aumento de 330 USD"
      },
      {
        "metrica": "Active Users",
        "abril": {
          "valor": 1935,
          "unidad": "usuarios"
        },
        "supuesto": "Crecimiento mensual de 15.3%"
      },
      {
        "metrica": "Support Tickets",
        "abril": {
          "valor": 52,
          "unidad": "tickets"
        },
        "supuesto": "Reducción mensual de 17.1%"
      },
      {
        "metrica": "Avg Response (h)",
        "abril": {
          "valor": 1.7,
          "unidad": "horas"
        },
        "supuesto": "Reducción de 0.7 horas"
      }
    ],
    "ltv_cac_ratio_proyectado": {
      "abril": {
        "ltv_usd": 2670,
        "cac_usd": 176,
        "ratio": 15.17
      }
    }
  }
}