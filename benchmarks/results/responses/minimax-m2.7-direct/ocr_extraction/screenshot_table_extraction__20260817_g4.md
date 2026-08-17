# MiniMax M2.7 (directo) — ocr_extraction/screenshot_table_extraction

- model_id: `MiniMax-M2.7`
- success: True  | final: 8.69 | quality: 10.0
- latency_total: 27.754s | tokens_per_second: 73.8
- input_tokens: 397 | output_tokens: 2048

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
    "nombre": "KPIs Marzo 2026",
    "periodo": "Enero - Marzo 2026",
    "tendencia_general": "Positiva en todas las metricas"
  },
  "metricas": {
    "MRR": {
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "unidad": "USD",
      "variacion_mensual": "+7.0%"
    },
    "Churn_Rate": {
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "unidad": "%",
      "variacion_mensual": "-0.7pp"
    },
    "NPS": {
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "unidad": "puntos",
      "variacion_mensual": "+6"
    },
    "CAC": {
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "unidad": "USD",
      "variacion_mensual": "-$11"
    },
    "LTV": {
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "unidad": "USD",
      "variacion_mensual": "+$330"
    },
    "Active_Users": {
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "unidad": "usuarios",
      "variacion_mensual": "+15.3%"
    },
    "Support_Tickets": {
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "unidad": "tickets",
      "variacion_mensual": "-17.1%"
    },
    "Avg_Response_Time": {
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "unidad": "horas",
      "variacion_mensual": "-0.7"
    }
  },
  "ltv_cac_ratio": {
    "enero": {
      "ltv": 1890,
      "cac": 234,
      "ratio": 8.08,
      "interpretacion": "Excelente (industria saludable: >3)"
    },
    "febrero": {
      "ltv": 2010,
      "cac": 198,
      "ratio": 10.15,
      "interpretacion": "Excelente (mejorando)"
    },
    "marzo": {
      "ltv": 2340,
      "cac": 187,
      "ratio": 12.51,
      "interpretacion": "Excelente (mejora de 54.9% vs enero)"
    }
  },
  "metricas_clave": {
    "mayor_mejora_porcentual": {
      "metrica": "Support_Tickets",
      "mejora": "17.1%",
      "detalle": "Reducción de 89 a 63 tickets (-26 unidades)",
      "interpretacion": "Mayor eficiencia en atención al cliente"
    },
    "ltv_cac_ratio": {
      "valor_actual": 12.51,
      "tendencia": "Al alza (+54.9% en 3 meses)",
      "estado": "Saludable"
    }
  },
  "proyecciones_abril": {
    "supuestos": {
      "metodo": "Tendencia lineal basada en promedio móvil de 3 meses",
      "consideraciones": "Suponiendo que las tendencias actuales se mantienen"
    },
    "valores": {
      "MRR": {
        "proyeccion": 55837,
        "unidad": "USD",
        "variacion_estimada": "+7.2%",
        "crecimiento_promedio_mensual": 2300
      },
      "Churn_Rate": {
        "proyeccion": 2.55,
        "unidad": "%",
        "variacion_estimada": "-0.55pp",
        "reduccion_promedio_mensual": 0.55
      },
      "NPS": {
        "proyeccion": 55.5,
        "unidad": "puntos",
        "variacion_estimada": "+4.5",
        "crecimiento_promedio_mensual": 4.5
      },
      "CAC": {
        "proyeccion": 163.5,
        "unidad": "USD",
        "variacion_estimada": "-$23.5",
        "reduccion_promedio_mensual": 23.5
      },
      "LTV": {
        "proyeccion": 2565,
        "unidad": "USD",
        "variacion_estimada": "+$225",
        "crecimiento_promedio_mensual": 225
      },
      "Active_Users": {
        "proyeccion": 1900,
        "unidad": "usuarios",
        "variacion_estimada": "+13.2%",
        "crecimiento_promedio_mensual": 222
      },
      "Support_Tickets": {
        "proye