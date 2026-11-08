# Mistral Large 3 675B — ocr_extraction/screenshot_table_extraction

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 7.54 | quality: 8.0
- latency_total: 9.979s | tokens_per_second: 136.2
- input_tokens: 422 | output_tokens: 1359

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

Aquí tienes la respuesta en formato JSON estructurado con los cálculos y proyecciones solicitadas:

```json
{
  "dashboard_data": {
    "titulo": "KPIs Marzo 2026",
    "periodos": ["Enero", "Febrero", "Marzo"],
    "metricas": [
      {
        "nombre": "MRR",
        "valores": [45200, 48700, 52100],
        "unidad": "USD",
        "variacion_mes_mes": "+7.0%"
      },
      {
        "nombre": "Churn Rate",
        "valores": [0.042, 0.038, 0.031],
        "unidad": "%",
        "variacion_mes_mes": "-0.7pp"
      },
      {
        "nombre": "NPS",
        "valores": [42, 45, 51],
        "unidad": "puntos",
        "variacion_mes_mes": "+6"
      },
      {
        "nombre": "CAC",
        "valores": [234, 198, 187],
        "unidad": "USD",
        "variacion_mes_mes": "-$11"
      },
      {
        "nombre": "LTV",
        "valores": [1890, 2010, 2340],
        "unidad": "USD",
        "variacion_mes_mes": "+$330"
      },
      {
        "nombre": "Active Users",
        "valores": [1234, 1456, 1678],
        "unidad": "usuarios",
        "variacion_mes_mes": "+15.3%"
      },
      {
        "nombre": "Support Tickets",
        "valores": [89, 76, 63],
        "unidad": "tickets",
        "variacion_mes_mes": "-17.1%"
      },
      {
        "nombre": "Avg Response Time",
        "valores": [4.2, 3.1, 2.4],
        "unidad": "horas",
        "variacion_mes_mes": "-0.7"
      }
    ],
    "tendencia_general": "Positiva en todas las métricas"
  },
  "calculos_adicionales": {
    "ltv_cac_ratio": {
      "Enero": 8.08,
      "Febrero": 10.15,
      "Marzo": 12.51
    },
    "metrica_mayor_mejora_porcentual": {
      "nombre": "Active Users",
      "mejora": "+15.3%",
      "valor_absoluto": 15.3
    }
  },
  "proyecciones_abril": {
    "metodo": "Extrapolación lineal basada en la variación mensual promedio de los últimos 2 meses",
    "valores_proyectados": {
      "MRR": {
        "valor": 55800,
        "variacion": "+7.1%",
        "nota": "Basado en crecimiento promedio de +$3,450 mensual"
      },
      "Churn Rate": {
        "valor": 0.024,
        "variacion": "-0.7pp",
        "nota": "Reducción constante de 0.7pp mensual"
      },
      "NPS": {
        "valor": 57,
        "variacion": "+6",
        "nota": "Aumento constante de 6 puntos mensuales"
      },
      "CAC": {
        "valor": 176,
        "variacion": "-$11",
        "nota": "Reducción constante de $11 mensual"
      },
      "LTV": {
        "valor": 2670,
        "variacion": "+$330",
        "nota": "Aumento constante de $330 mensual"
      },
      "Active Users": {
        "valor": 1920,
        "variacion": "+14.4%",
        "nota": "Basado en crecimiento promedio de +222 usuarios mensuales"
      },
      "Support Tickets": {
        "valor": 50,
        "variacion": "-20.6%",
        "nota": "Basado en reducción promedio de 13 tickets mensuales"
      },
      "Avg Response Time": {
        "valor": 1.7,
        "variacion": "-0.7",
        "nota": "Reducción constante de 0.7 horas mensuales"
      },
      "LTV_CAC_Ratio": {
        "valor": 15.17,
        "variacion": "+21.3%",
        "nota": "Basado en mejora continua de ambos indicadores"
      }
    },
    "tendencia_proyectada": "Continúa positiva con mejoras en todas las métricas clave"
  },
  "observaciones": {
    "destacadas": [
      "El LTV/CAC ratio muestra una mejora significativa (de 8.08 a 12.51 en 3 meses)",
      "La reducción de Support Tickets y tiempo de respuesta sugiere mayor eficiencia en soporte",
      "El crecimiento de Active Users (+36% en 3 meses) es el más acelerado",
      "El NPS muestra una mejora notable (de 42 a 51 en 3 meses)"
    ],
    "recomendaciones": [
      "Analizar las causas del crecimiento acelerado de Active Users para replicar estrategias",
      "Investigar si la reducción de CAC está afectando la calidad de adquisición",
      "Monitorear si la mejora en NPS se mantiene con el crecimiento de usuarios",
      "Evaluar si la reducción de Support Tickets podría afectar la satisfacción del cliente"
    ]
  }
}
```