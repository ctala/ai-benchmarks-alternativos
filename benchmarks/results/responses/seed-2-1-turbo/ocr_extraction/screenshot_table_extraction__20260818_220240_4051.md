# Seed 2.1 Turbo — ocr_extraction/screenshot_table_extraction

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 6.83 | quality: 8.0
- latency_total: 148.694s | tokens_per_second: 71.5
- input_tokens: 477 | output_tokens: 10639

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
  "metadata": {
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "periodos_disponibles": [
      "Enero 2026",
      "Febrero 2026",
      "Marzo 2026"
    ],
    "tendencia_general": "Positiva en todas las métricas"
  },
  "datos_metricas_extraidos": [
    {
      "nombre": "MRR",
      "unidad": "miles de USD",
      "valores": {
        "enero": 45.2,
        "febrero": 48.7,
        "marzo": 52.1
      },
      "variacion_mm": {
        "valor": 7.0,
        "unidad": "porcentaje"
      },
      "direccion_mejora": "aumento"
    },
    {
      "nombre": "Churn Rate",
      "unidad": "porcentaje",
      "valores": {
        "enero": 4.2,
        "febrero": 3.8,
        "marzo": 3.1
      },
      "variacion_mm": {
        "valor": -0.7,
        "unidad": "puntos porcentuales"
      },
      "direccion_mejora": "disminución"
    },
    {
      "nombre": "NPS",
      "unidad": "puntos",
      "valores": {
        "enero": 42,
        "febrero": 45,
        "marzo": 51
      },
      "variacion_mm": {
        "valor": 6,
        "unidad": "puntos"
      },
      "direccion_mejora": "aumento"
    },
    {
      "nombre": "CAC",
      "unidad": "USD",
      "valores": {
        "enero": 234,
        "febrero": 198,
        "marzo": 187
      },
      "variacion_mm": {
        "valor": -11,
        "unidad": "USD"
      },
      "direccion_mejora": "disminución"
    },
    {
      "nombre": "LTV",
      "unidad": "USD",
      "valores": {
        "enero": 1890,
        "febrero": 2010,
        "marzo": 2340
      },
      "variacion_mm": {
        "valor": 330,
        "unidad": "USD"
      },
      "direccion_mejora": "aumento"
    },
    {
      "nombre": "Active Users",
      "unidad": "usuarios",
      "valores": {
        "enero": 1234,
        "febrero": 1456,
        "marzo": 1678
      },
      "variacion_mm": {
        "valor": 15.3,
        "unidad": "porcentaje"
      },
      "direccion_mejora": "aumento"
    },
    {
      "nombre": "Support Tickets",
      "unidad": "tickets",
      "valores": {
        "enero": 89,
        "febrero": 76,
        "marzo": 63
      },
      "variacion_mm": {
        "valor": -17.1,
        "unidad": "porcentaje"
      },
      "direccion_mejora": "disminución"
    },
    {
      "nombre": "Avg Response (h)",
      "unidad": "horas",
      "valores": {
        "enero": 4.2,
        "febrero": 3.1,
        "marzo": 2.4
      },
      "variacion_mm": {
        "valor": -0.7,
        "unidad": "horas"
      },
      "direccion_mejora": "disminución"
    }
  ],
  "calculos_adicionales": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "explicacion": "Ratio calculado como LTV dividido CAC, redondeado a dos decimales"
    },
    "metrica_mayor_mejora_porcentual": {
      "nombre": "Avg Response (h)",
      "mejora_porcentual": 22.58,
      "explicacion": "Se calculó la variación porcentual relativa al mes de febrero para cada métrica, considerando su dirección de mejora (aumento para métricas donde mayor valor es mejor, reducción para métricas donde menor valor es mejor). El tiempo de respuesta promedio registró una reducción del 22.58%, la mayor entre todas las métricas"
    },
    "proyeccion_abril_2026": {
      "metodo": "Aplicación de la tasa de cambio porcentual mensual observada entre febrero y marzo de 2026 a los valores de marzo, asumiendo que la tendencia se mantiene constante. Valores discretos (usuarios, tickets) redondeados a número entero",
      "valores_proyectados": {
        "MRR": {
          "valor": 55.74,
          "unidad": "miles de USD"
        },
        "Churn Rate": {
          "valor": 2.53,
          "unidad": "porcentaje"
        },
        "NPS": {
          "valor": 57.8,
          "unidad": "puntos"
        },
        "CAC": {
          "valor": 176.61,
          "unidad": "USD"
        },
        "LTV": {
          "valor": 2724.18,
          "unidad": "USD"
        },
        "Active Users": {
          "valor": 1934,
          "unidad": "usuarios"
        },
        "Support Tickets": {
          "valor": 52,
          "unidad": "tickets"
        },
        "Avg Response (h)": {
          "valor": 1.86,
          "unidad": "horas"
        }
      }
    }
  }
}