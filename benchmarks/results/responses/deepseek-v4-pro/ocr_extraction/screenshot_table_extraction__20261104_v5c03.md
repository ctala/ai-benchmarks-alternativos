# DeepSeek V4 Pro — ocr_extraction/screenshot_table_extraction

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 8.72 | quality: 10.0
- latency_total: 12.794s | tokens_per_second: 101.8
- input_tokens: 386 | output_tokens: 1303

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
  "datos_originales": {
    "metricas": [
      {
        "metrica": "MRR",
        "unidad": "USD",
        "enero": 45200,
        "febrero": 48700,
        "marzo": 52100,
        "variacion_mensual_porcentaje": 7.0
      },
      {
        "metrica": "Churn Rate",
        "unidad": "porcentaje",
        "enero": 4.2,
        "febrero": 3.8,
        "marzo": 3.1,
        "variacion_mensual_puntos_porcentuales": -0.7
      },
      {
        "metrica": "NPS",
        "unidad": "puntos",
        "enero": 42,
        "febrero": 45,
        "marzo": 51,
        "variacion_mensual_absoluta": 6
      },
      {
        "metrica": "CAC",
        "unidad": "USD",
        "enero": 234,
        "febrero": 198,
        "marzo": 187,
        "variacion_mensual_absoluta": -11
      },
      {
        "metrica": "LTV",
        "unidad": "USD",
        "enero": 1890,
        "febrero": 2010,
        "marzo": 2340,
        "variacion_mensual_absoluta": 330
      },
      {
        "metrica": "Active Users",
        "unidad": "usuarios",
        "enero": 1234,
        "febrero": 1456,
        "marzo": 1678,
        "variacion_mensual_porcentaje": 15.3
      },
      {
        "metrica": "Support Tickets",
        "unidad": "tickets",
        "enero": 89,
        "febrero": 76,
        "marzo": 63,
        "variacion_mensual_porcentaje": -17.1
      },
      {
        "metrica": "Avg Response (h)",
        "unidad": "horas",
        "enero": 4.2,
        "febrero": 3.1,
        "marzo": 2.4,
        "variacion_mensual_absoluta": -0.7
      }
    ]
  },
  "analisis": {
    "ltv_cac_ratio": {
      "enero": {
        "LTV": 1890,
        "CAC": 234,
        "ratio": 8.08
      },
      "febrero": {
        "LTV": 2010,
        "CAC": 198,
        "ratio": 10.15
      },
      "marzo": {
        "LTV": 2340,
        "CAC": 187,
        "ratio": 12.51
      }
    },
    "metrica_mayor_mejora_porcentual": {
      "metrica": "Support Tickets",
      "variacion_porcentual_marzo_vs_febrero": -17.11,
      "tendencia": "Reducción (mejora en métrica de soporte)",
      "nota": "Se considera mejora porcentual en valor absoluto. Support Tickets bajó un 17.1%, siendo la mayor variación positiva (menos tickets es mejor)."
    },
    "proyeccion_abril": {
      "supuesto": "Se mantiene la variación intermensual promedio (Feb-Mar) para cada métrica.",
      "valores_proyectados": {
        "MRR": {
          "valor": 55747,
          "unidad": "USD",
          "metodo": "Crecimiento absoluto promedio: (52100-48700)=3400. Proyección: 52100+3400"
        },
        "Churn Rate": {
          "valor": 2.4,
          "unidad": "porcentaje",
          "metodo": "Reducción absoluta promedio: (3.1-3.8)=-0.7. Proyección: 3.1-0.7"
        },
        "NPS": {
          "valor": 57,
          "unidad": "puntos",
          "metodo": "Incremento absoluto promedio: (51-45)=6. Proyección: 51+6"
        },
        "CAC": {
          "valor": 176,
          "unidad": "USD",
          "metodo": "Reducción absoluta promedio: (187-198)=-11. Proyección: 187-11"
        },
        "LTV": {
          "valor": 2670,
          "unidad": "USD",
          "metodo": "Incremento absoluto promedio: (2340-2010)=330. Proyección: 2340+330"
        },
        "Active Users": {
          "valor": 1900,
          "unidad": "usuarios",
          "metodo": "Incremento absoluto promedio: (1678-1456)=222. Proyección: 1678+222"
        },
        "Support Tickets": {
          "valor": 50,
          "unidad": "tickets",
          "metodo": "Reducción absoluta promedio: (63-76)=-13. Proyección: 63-13"
        },
        "Avg Response (h)": {
          "valor": 1.7,
          "unidad": "horas",
          "metodo": "Reducción absoluta promedio: (2.4-3.1)=-0.7. Proyección: 2.4-0.7"
        }
      }
    }
  }
}
```