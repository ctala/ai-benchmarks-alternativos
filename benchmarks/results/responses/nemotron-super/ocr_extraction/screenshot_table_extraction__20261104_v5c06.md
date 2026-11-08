# Nemotron 3 Super — ocr_extraction/screenshot_table_extraction

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 7.94 | quality: 8.0
- latency_total: 4.193s | tokens_per_second: 362.0
- input_tokens: 435 | output_tokens: 1518

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
  "periodo": "Marzo 2026",
  "datos_mensuales": [
    {
      "mes": "Enero",
      "metrica": "MRR",
      "valor": 45200,
      "unidad": "USD"
    },
    {
      "mes": "Febrero",
      "metrica": "MRR",
      "valor": 48700,
      "unidad": "USD"
    },
    {
      "mes": "Marzo",
      "metrica": "MRR",
      "valor": 52100,
      "unidad": "USD",
      "variacion_mensual": "+7.0%"
    },
    {
      "mes": "Enero",
      "metrica": "Churn Rate",
      "valor": 4.2,
      "unidad": "%"
    },
    {
      "mes": "Febrero",
      "metrica": "Churn Rate",
      "valor": 3.8,
      "unidad": "%"
    },
    {
      "mes": "Marzo",
      "metrica": "Churn Rate",
      "valor": 3.1,
      "unidad": "%",
      "variacion_mensual": "-0.7pp"
    },
    {
      "mes": "Enero",
      "metrica": "NPS",
      "valor": 42,
      "unidad": "puntos"
    },
    {
      "mes": "Febrero",
      "metrica": "NPS",
      "valor": 45,
      "unidad": "puntos"
    },
    {
      "mes": "Marzo",
      "metrica": "NPS",
      "valor": 51,
      "unidad": "puntos",
      "variacion_mensual": "+6"
    },
    {
      "mes": "Enero",
      "metrica": "CAC",
      "valor": 234,
      "unidad": "USD"
    },
    {
      "mes": "Febrero",
      "metrica": "CAC",
      "valor": 198,
      "unidad": "USD"
    },
    {
      "mes": "Marzo",
      "metrica": "CAC",
      "valor": 187,
      "unidad": "USD",
      "variacion_mensual": "-$11"
    },
    {
      "mes": "Enero",
      "metrica": "LTV",
      "valor": 1890,
      "unidad": "USD"
    },
    {
      "mes": "Febrero",
      "metrica": "LTV",
      "valor": 2010,
      "unidad": "USD"
    },
    {
      "mes": "Marzo",
      "metrica": "LTV",
      "valor": 2340,
      "unidad": "USD",
      "variacion_mensual": "+$330"
    },
    {
      "mes": "Enero",
      "metrica": "Active Users",
      "valor": 1234,
      "unidad": "usuarios"
    },
    {
      "mes": "Febrero",
      "metrica": "Active Users",
      "valor": 1456,
      "unidad": "usuarios"
    },
    {
      "mes": "Marzo",
      "metrica": "Active Users",
      "valor": 1678,
      "unidad": "usuarios",
      "variacion_mensual": "+15.3%"
    },
    {
      "mes": "Enero",
      "metrica": "Support Tickets",
      "valor": 89,
      "unidad": "tickets"
    },
    {
      "mes": "Febrero",
      "metrica": "Support Tickets",
      "valor": 76,
      "unidad": "tickets"
    },
    {
      "mes": "Marzo",
      "metrica": "Support Tickets",
      "valor": 63,
      "unidad": "tickets",
      "variacion_mensual": "-17.1%"
    },
    {
      "mes": "Enero",
      "metrica": "Avg Response (h)",
      "valor": 4.2,
      "unidad": "horas"
    },
    {
      "mes": "Febrero",
      "metrica": "Avg Response (h)",
      "valor": 3.1,
      "unidad": "horas"
    },
    {
      "mes": "Marzo",
      "metrica": "Avg Response (h)",
      "valor": 2.4,
      "unidad": "horas",
      "variacion_mensual": "-0.7"
    }
  ],
  "analisis": {
    "ltv_cac_ratio": {
      "Enero": 8.08,
      "Febrero": 10.15,
      "Marzo": 12.51
    },
    "metrica_mayor_mejora_porcentual": {
      "metrica": "Active Users",
      "cambio_febrero_a_marzo": "+15.3%",
      "nota": "Mejor variación mensual porcentual reportada en el dashboard"
    },
    "proyeccion_abril_2026": {
      "metodo": "Extrapolación basada en la variación mensual (M/M) de Febrero a Marzo",
      "valores_estimados": {
        "MRR": 55747,
        "Churn Rate": 2.4,
        "NPS": 57,
        "CAC": 176,
        "LTV": 2670,
        "Active Users": 1935,
        "Support Tickets": 52,
        "Avg Response (h)": 1.7
      },
      "notas": {
        "MRR": "Aplicado +7.0% sobre $52.1K",
        "Churn Rate": "Reducción de 0.7pp sobre 3.1%",
        "NPS": "Incremento de +6 puntos sobre 51",
        "CAC": "Reducción de $11 sobre $187",
        "LTV": "Incremento de $330 sobre $2,340",
        "Active Users": "Aplicado +15.3% sobre 1,678",
        "Support Tickets": "Reducción del 17.1% sobre 63",
        "Avg Response (h)": "Reducción de 0.7h sobre 2.4h"
      }
    }
  }
}
```