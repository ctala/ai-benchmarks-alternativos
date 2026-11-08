# Seed 2.0 Code — ocr_extraction/screenshot_table_extraction

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.5 | quality: 10.0
- latency_total: 28.524s | tokens_per_second: 78.5
- input_tokens: 461 | output_tokens: 2239

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
    "periodo": "Enero - Marzo 2026",
    "metricas": [
      {
        "nombre": "MRR",
        "unidad": "$",
        "enero": 45200,
        "febrero": 48700,
        "marzo": 52100,
        "variacion_mes": 0.07,
        "formato_enero": "$45.2K",
        "formato_febrero": "$48.7K",
        "formato_marzo": "$52.1K",
        "formato_variacion": "+7.0%"
      },
      {
        "nombre": "Churn Rate",
        "unidad": "%",
        "enero": 0.042,
        "febrero": 0.038,
        "marzo": 0.031,
        "variacion_mes": -0.007,
        "formato_enero": "4.2%",
        "formato_febrero": "3.8%",
        "formato_marzo": "3.1%",
        "formato_variacion": "-0.7pp"
      },
      {
        "nombre": "NPS",
        "unidad": "puntos",
        "enero": 42,
        "febrero": 45,
        "marzo": 51,
        "variacion_mes": 6,
        "formato_enero": "42",
        "formato_febrero": "45",
        "formato_marzo": "51",
        "formato_variacion": "+6"
      },
      {
        "nombre": "CAC",
        "unidad": "$",
        "enero": 234,
        "febrero": 198,
        "marzo": 187,
        "variacion_mes": -11,
        "formato_enero": "$234",
        "formato_febrero": "$198",
        "formato_marzo": "$187",
        "formato_variacion": "-$11"
      },
      {
        "nombre": "LTV",
        "unidad": "$",
        "enero": 1890,
        "febrero": 2010,
        "marzo": 2340,
        "variacion_mes": 330,
        "formato_enero": "$1,890",
        "formato_febrero": "$2,010",
        "formato_marzo": "$2,340",
        "formato_variacion": "+$330"
      },
      {
        "nombre": "Active Users",
        "unidad": "usuarios",
        "enero": 1234,
        "febrero": 1456,
        "marzo": 1678,
        "variacion_mes": 0.153,
        "formato_enero": "1,234",
        "formato_febrero": "1,456",
        "formato_marzo": "1,678",
        "formato_variacion": "+15.3%"
      },
      {
        "nombre": "Support Tickets",
        "unidad": "tickets",
        "enero": 89,
        "febrero": 76,
        "marzo": 63,
        "variacion_mes": -0.171,
        "formato_enero": "89",
        "formato_febrero": "76",
        "formato_marzo": "63",
        "formato_variacion": "-17.1%"
      },
      {
        "nombre": "Avg Response (h)",
        "unidad": "horas",
        "enero": 4.2,
        "febrero": 3.1,
        "marzo": 2.4,
        "variacion_mes": -0.7,
        "formato_enero": "4.2",
        "formato_febrero": "3.1",
        "formato_marzo": "2.4",
        "formato_variacion": "-0.7"
      }
    ],
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "descripcion": "Ratio LTV/CAC (valor: >3 es saludable)",
      "interpretacion": "El ratio ha mejorado consistentemente, pasando de 8.08x a 12.51x, indicando una eficiencia mucho mayor en la adquisición de clientes y una mayor rentabilidad por usuario."
    },
    "mayor_mejora_porcentual": {
      "metrica": "Support Tickets",
      "valor_enero": 89,
      "valor_marzo": 63,
      "mejora_porcentual": 29.21,
      "descripcion": "Reducción de tickets de soporte (mejora porcentual calculada como: (valor_inicial - valor_final)/valor_inicial * 100 para métricas que deben disminuir)"
    },
    "proyeccion_abril": {
      "metodologia": "Proyección basada en la tasa de crecimiento promedio de los últimos 2 meses (Febrero y Marzo)",
      "metricas_proyectadas": [
        {
          "nombre": "MRR",
          "valor_proyectado": 55948,
          "formateado": "$55.9K",
          "crecimiento_mensual": 7.38
        },
        {
          "nombre": "Churn Rate",
          "valor_proyectado": 0.024,
          "formateado": "2.4%",
          "crecimiento_mensual": -22.62
        },
        {
          "nombre": "NPS",
          "valor_proyectado": 58,
          "formateado": "58",
          "crecimiento_mensual": 12.70
        },
        {
          "nombre": "CAC",
          "valor_proyectado": 158,
          "formateado": "$158",
          "crecimiento_mensual": -15.95
        },
        {
          "nombre": "LTV",
          "valor_proyectado": 2725,
          "formateado": "$2,725",
          "crecimiento_mensual": 16.43
        },
        {
          "nombre": "Active Users",
          "valor_proyectado": 1962,
          "formateado": "1,962",
          "crecimiento_mensual": 16.94
        },
        {
          "nombre": "Support Tickets",
          "valor_proyectado": 50,
          "formateado": "50",
          "crecimiento_mensual": -20.63
        },
        {
          "nombre": "Avg Response (h)",
          "valor_proyectado": 1.7,
          "formateado": "1.7",
          "crecimiento_mensual": -26.19
        },
        {
          "nombre": "LTV/CAC Ratio",
          "valor_proyectado": 17.25,
          "formateado": "17.25x",
          "crecimiento_mensual": 37.89
        }
      ]
    },
    "resumen_ejecutivo": {
      "tendencia_general": "Positiva en todas las métricas",
      "puntos_clave": [
        "MRR creció un 15.3% de Enero a Marzo",
        "Churn Rate disminuyó de 4.2% a 3.1% (mejora de 1.1 puntos porcentuales)",
        "NPS experimentó un aumento significativo de 42 a 51 puntos",
        "CAC se redujo un 20.1% mientras que LTV aumentó un 23.8%",
        "El ratio LTV/CAC mejoró de 8.08x a 12.51x, muy por encima del umbral saludable de 3x",
        "Usuarios activos crecieron un 36.0% en el trimestre",
        "Tickets de soporte y tiempo de respuesta mejoraron drásticamente (-29.2% y -42.9% respectivamente)"
      ],
      "conclusion": "El negocio muestra una trayectoria de crecimiento saludable con mejoras significativas en adquisición, retención y satisfacción del cliente. La eficiencia operativa ha aumentado considerablemente, generando mayor rentabilidad por usuario."
    }
  }
}