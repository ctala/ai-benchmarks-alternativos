# MiniMax M3 — ocr_extraction/screenshot_table_extraction

- model_id: `minimax/minimax-m3`
- success: True  | final: 7.57 | quality: 8.0
- latency_total: 8.735s | tokens_per_second: 172.6
- input_tokens: 532 | output_tokens: 1508

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
    "tendencia_general": "Positiva",
    "nota": "Los valores de abril se proyectan aplicando a marzo el cambio porcentual observado entre febrero y marzo. En las métricas donde la mejora equivale a una reducción, se conserva el sentido favorable de la tendencia."
  },
  "metricas": [
    {
      "nombre": "MRR",
      "unidad": "USD",
      "valores": {
        "enero": 45200,
        "febrero": 48700,
        "marzo": 52100
      },
      "variacion_marzo_vs_febrero": {
        "valor": 3400,
        "porcentaje": 7.0,
        "unidad": "pp",
        "tipo": "aumento"
      }
    },
    {
      "nombre": "Churn Rate",
      "unidad": "%",
      "valores": {
        "enero": 4.2,
        "febrero": 3.8,
        "marzo": 3.1
      },
      "variacion_marzo_vs_febrero": {
        "valor": -0.7,
        "porcentaje": -18.42,
        "unidad": "pp",
        "tipo": "disminucion"
      }
    },
    {
      "nombre": "NPS",
      "unidad": "puntos",
      "valores": {
        "enero": 42,
        "febrero": 45,
        "marzo": 51
      },
      "variacion_marzo_vs_febrero": {
        "valor": 6,
        "porcentaje": 13.33,
        "unidad": "puntos",
        "tipo": "aumento"
      }
    },
    {
      "nombre": "CAC",
      "unidad": "USD",
      "valores": {
        "enero": 234,
        "febrero": 198,
        "marzo": 187
      },
      "variacion_marzo_vs_febrero": {
        "valor": -11,
        "porcentaje": -5.56,
        "unidad": "pp",
        "tipo": "disminucion"
      }
    },
    {
      "nombre": "LTV",
      "unidad": "USD",
      "valores": {
        "enero": 1890,
        "febrero": 2010,
        "marzo": 2340
      },
      "variacion_marzo_vs_febrero": {
        "valor": 330,
        "porcentaje": 16.42,
        "unidad": "pp",
        "tipo": "aumento"
      }
    },
    {
      "nombre": "Active Users",
      "unidad": "usuarios",
      "valores": {
        "enero": 1234,
        "febrero": 1456,
        "marzo": 1678
      },
      "variacion_marzo_vs_febrero": {
        "valor": 222,
        "porcentaje": 15.25,
        "unidad": "pp",
        "tipo": "aumento"
      }
    },
    {
      "nombre": "Support Tickets",
      "unidad": "tickets",
      "valores": {
        "enero": 89,
        "febrero": 76,
        "marzo": 63
      },
      "variacion_marzo_vs_febrero": {
        "valor": -13,
        "porcentaje": -17.11,
        "unidad": "pp",
        "tipo": "disminucion"
      }
    },
    {
      "nombre": "Avg Response",
      "unidad": "horas",
      "valores": {
        "enero": 4.2,
        "febrero": 3.1,
        "marzo": 2.4
      },
      "variacion_marzo_vs_febrero": {
        "valor": -0.7,
        "porcentaje": -22.58,
        "unidad": "pp",
        "tipo": "disminucion"
      }
    }
  ],
  "ltv_cac_ratio": {
    "formula": "LTV / CAC",
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51,
    "variacion_marzo_vs_febrero": 2.36,
    "variacion_porcentual": 23.26
  },
  "mayor_mejora_porcentual": {
    "metrica": "Avg Response",
    "cambio_porcentual": -22.58,
    "interpretacion": "La mejora porcentual favorable es del 22.58%, pues el tiempo promedio de respuesta disminuyó de 3.1 a 2.4 horas."
  },
  "proyeccion_abril_2026": {
    "metodo": "Valor de marzo multiplicado por (1 + cambio porcentual entre febrero y marzo).",
    "metricas": [
      {
        "nombre": "MRR",
        "valor_proyectado": 55747,
        "unidad": "USD",
        "cambio_aplicado": 7.0
      },
      {
        "nombre": "Churn Rate",
        "valor_proyectado": 2.53,
        "unidad": "%",
        "cambio_aplicado": -18.42
      },
      {
        "nombre": "NPS",
        "valor_proyectado": 57.8,
        "unidad": "puntos",
        "cambio_aplicado": 13.33
      },
      {
        "nombre": "CAC",
        "valor_proyectado": 176.6,
        "unidad": "USD",
        "cambio_aplicado": -5.56
      },
      {
        "nombre": "LTV",
        "valor_proyectado": 2724.23,
        "unidad": "USD",
        "cambio_aplicado": 16.42
      },
      {
        "nombre": "Active Users",
        "valor_proyectado": 1933.95,
        "unidad": "usuarios",
        "cambio_aplicado": 15.25
      },
      {
        "nombre": "Support Tickets",
        "valor_proyectado": 52.21,
        "unidad": "tickets",
        "cambio_aplicado": -17.11
      },
      {
        "nombre": "Avg Response",
        "valor_proyectado": 1.86,
        "unidad": "horas",
        "cambio_aplicado": -22.58
      }
    ],
    "ltv_cac_ratio_proyectado": 15.43
  }
}