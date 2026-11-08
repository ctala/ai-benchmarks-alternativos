# DeepSeek V4 Pro (0813) — ocr_extraction/screenshot_table_extraction

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 8.61 | quality: 10.0
- latency_total: 12.611s | tokens_per_second: 92.3
- input_tokens: 386 | output_tokens: 1164

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
  "dashboard": "KPIs Marzo 2026",
  "metricas": [
    {
      "nombre": "MRR",
      "unidad": "USD",
      "valores": [
        {"mes": "Enero", "valor": 45200},
        {"mes": "Febrero", "valor": 48700},
        {"mes": "Marzo", "valor": 52100}
      ],
      "var_mensual_marzo": "+7.0%"
    },
    {
      "nombre": "Churn Rate",
      "unidad": "%",
      "valores": [
        {"mes": "Enero", "valor": 4.2},
        {"mes": "Febrero", "valor": 3.8},
        {"mes": "Marzo", "valor": 3.1}
      ],
      "var_mensual_marzo": "-0.7pp"
    },
    {
      "nombre": "NPS",
      "unidad": "puntos",
      "valores": [
        {"mes": "Enero", "valor": 42},
        {"mes": "Febrero", "valor": 45},
        {"mes": "Marzo", "valor": 51}
      ],
      "var_mensual_marzo": "+6"
    },
    {
      "nombre": "CAC",
      "unidad": "USD",
      "valores": [
        {"mes": "Enero", "valor": 234},
        {"mes": "Febrero", "valor": 198},
        {"mes": "Marzo", "valor": 187}
      ],
      "var_mensual_marzo": "-$11"
    },
    {
      "nombre": "LTV",
      "unidad": "USD",
      "valores": [
        {"mes": "Enero", "valor": 1890},
        {"mes": "Febrero", "valor": 2010},
        {"mes": "Marzo", "valor": 2340}
      ],
      "var_mensual_marzo": "+$330"
    },
    {
      "nombre": "Active Users",
      "unidad": "usuarios",
      "valores": [
        {"mes": "Enero", "valor": 1234},
        {"mes": "Febrero", "valor": 1456},
        {"mes": "Marzo", "valor": 1678}
      ],
      "var_mensual_marzo": "+15.3%"
    },
    {
      "nombre": "Support Tickets",
      "unidad": "tickets",
      "valores": [
        {"mes": "Enero", "valor": 89},
        {"mes": "Febrero", "valor": 76},
        {"mes": "Marzo", "valor": 63}
      ],
      "var_mensual_marzo": "-17.1%"
    },
    {
      "nombre": "Avg Response (h)",
      "unidad": "horas",
      "valores": [
        {"mes": "Enero", "valor": 4.2},
        {"mes": "Febrero", "valor": 3.1},
        {"mes": "Marzo", "valor": 2.4}
      ],
      "var_mensual_marzo": "-0.7"
    }
  ],
  "analisis": {
    "ltv_cac_ratio": [
      {"mes": "Enero", "ratio": 8.08},
      {"mes": "Febrero", "ratio": 10.15},
      {"mes": "Marzo", "ratio": 12.51}
    ],
    "metrica_mayor_mejora_porcentual": {
      "nombre": "Support Tickets",
      "mejora_porcentual": "-17.1%",
      "nota": "La mejora se interpreta como reducción de tickets, lo cual es positivo"
    },
    "proyeccion_abril": {
      "metodo": "Regresión lineal simple basada en tendencia de los últimos 3 meses",
      "valores_proyectados": [
        {"metrica": "MRR", "valor_abril": 55500, "unidad": "USD"},
        {"metrica": "Churn Rate", "valor_abril": 2.4, "unidad": "%"},
        {"metrica": "NPS", "valor_abril": 57, "unidad": "puntos"},
        {"metrica": "CAC", "valor_abril": 176, "unidad": "USD"},
        {"metrica": "LTV", "valor_abril": 2670, "unidad": "USD"},
        {"metrica": "Active Users", "valor_abril": 1900, "unidad": "usuarios"},
        {"metrica": "Support Tickets", "valor_abril": 50, "unidad": "tickets"},
        {"metrica": "Avg Response (h)", "valor_abril": 1.7, "unidad": "horas"}
      ],
      "nota": "Proyección lineal asumiendo que la tendencia de los últimos 3 meses se mantiene constante. No considera estacionalidad ni factores externos."
    }
  }
}
```