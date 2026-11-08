# Seed 2.1 Turbo — ocr_extraction/screenshot_table_extraction

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 7.22 | quality: 8.0
- latency_total: 17.737s | tokens_per_second: 78.2
- input_tokens: 476 | output_tokens: 1387

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
  "dashboard_info": {
    "nombre": "KPIs Marzo 2026",
    "periodo_visible": ["Enero 2026", "Febrero 2026", "Marzo 2026"],
    "tendencia_general": "Positiva en todas las métricas"
  },
  "metricas_historicas": [
    {
      "metrica": "MRR",
      "unidad": "dólares",
      "formato": "miles",
      "valores": {
        "enero": 45200,
        "febrero": 48700,
        "marzo": 52100
      },
      "variacion_mm": 0.07,
      "variacion_mm_texto": "+7.0%"
    },
    {
      "metrica": "Churn Rate",
      "unidad": "porcentaje",
      "formato": "porcentaje",
      "valores": {
        "enero": 0.042,
        "febrero": 0.038,
        "marzo": 0.031
      },
      "variacion_mm": -0.007,
      "variacion_mm_texto": "-0.7pp"
    },
    {
      "metrica": "NPS",
      "unidad": "puntos",
      "formato": "entero",
      "valores": {
        "enero": 42,
        "febrero": 45,
        "marzo": 51
      },
      "variacion_mm": 6,
      "variacion_mm_texto": "+6 puntos"
    },
    {
      "metrica": "CAC",
      "unidad": "dólares",
      "formato": "monto",
      "valores": {
        "enero": 234,
        "febrero": 198,
        "marzo": 187
      },
      "variacion_mm": -11,
      "variacion_mm_texto": "-$11"
    },
    {
      "metrica": "LTV",
      "unidad": "dólares",
      "formato": "monto",
      "valores": {
        "enero": 1890,
        "febrero": 2010,
        "marzo": 2340
      },
      "variacion_mm": 330,
      "variacion_mm_texto": "+$330"
    },
    {
      "metrica": "Active Users",
      "unidad": "usuarios",
      "formato": "entero",
      "valores": {
        "enero": 1234,
        "febrero": 1456,
        "marzo": 1678
      },
      "variacion_mm": 0.153,
      "variacion_mm_texto": "+15.3%"
    },
    {
      "metrica": "Support Tickets",
      "unidad": "tickets",
      "formato": "entero",
      "valores": {
        "enero": 89,
        "febrero": 76,
        "marzo": 63
      },
      "variacion_mm": -0.171,
      "variacion_mm_texto": "-17.1%"
    },
    {
      "metrica": "Avg Response (h)",
      "unidad": "horas",
      "formato": "decimal",
      "valores": {
        "enero": 4.2,
        "febrero": 3.1,
        "marzo": 2.4
      },
      "variacion_mm": -0.7,
      "variacion_mm_texto": "-0.7 horas"
    }
  ],
  "calculos_realizados": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "explicacion": "Ratio calculado como LTV / CAC para cada mes, redondeado a 2 decimales"
    },
    "metrica_mayor_mejora_porcentual": {
      "metrica": "LTV",
      "mejora_porcentual_mm": 16.42,
      "explicacion": "Se calculó la variación porcentual relativa de marzo vs febrero para todas las métricas, considerando como mejora el impacto positivo en el negocio: el LTV creció un 16.42% respecto a febrero, siendo la mayor mejora porcentual del período"
    }
  },
  "proyeccion_abril_2026": {
    "metodo": "Proyección basada en la tasa de variación mensual relativa observada entre febrero y marzo de 2026, manteniendo la tendencia",
    "valores_proyectados": {
      "MRR": "$55.7K",
      "Churn Rate": "2.5%",
      "NPS": 58,
      "CAC": "$177",
      "LTV": "$2,724",
      "Active Users": 1935,
      "Support Tickets": 52,
      "Avg Response (h)": 1.9,
      "LTV/CAC ratio": 15.39
    }
  }
}