# MiMo V2.6 Pro — ocr_extraction/screenshot_table_extraction

- model_id: `xiaomi/mimo-v2.6-pro`
- success: True  | final: 8.87 | quality: 10.0
- latency_total: 13.848s | tokens_per_second: 69.9
- input_tokens: 425 | output_tokens: 968

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
  "dashboard_info": {
    "title": "KPIs Marzo 2026",
    "trend_general": "Positiva en todas las métricas"
  },
  "data": [
    {
      "metrica": "MRR",
      "valores": {
        "enero": 45200,
        "febrero": 48700,
        "marzo": 52100
      },
      "variacion_m_m": "+7.0%",
      "unidad": "USD"
    },
    {
      "metrica": "Churn Rate",
      "valores": {
        "enero": 4.2,
        "febrero": 3.8,
        "marzo": 3.1
      },
      "variacion_m_m": "-0.7pp",
      "unidad": "%"
    },
    {
      "metrica": "NPS",
      "valores": {
        "enero": 42,
        "febrero": 45,
        "marzo": 51
      },
      "variacion_m_m": "+6",
      "unidad": "puntos"
    },
    {
      "metrica": "CAC",
      "valores": {
        "enero": 234,
        "febrero": 198,
        "marzo": 187
      },
      "variacion_m_m": "-$11",
      "unidad": "USD"
    },
    {
      "metrica": "LTV",
      "valores": {
        "enero": 1890,
        "febrero": 2010,
        "marzo": 2340
      },
      "variacion_m_m": "+$330",
      "unidad": "USD"
    },
    {
      "metrica": "Active Users",
      "valores": {
        "enero": 1234,
        "febrero": 1456,
        "marzo": 1678
      },
      "variacion_m_m": "+15.3%",
      "unidad": "usuarios"
    },
    {
      "metrica": "Support Tickets",
      "valores": {
        "enero": 89,
        "febrero": 76,
        "marzo": 63
      },
      "variacion_m_m": "-17.1%",
      "unidad": "tickets"
    },
    {
      "metrica": "Avg Response (h)",
      "valores": {
        "enero": 4.2,
        "febrero": 3.1,
        "marzo": 2.4
      },
      "variacion_m_m": "-0.7",
      "unidad": "horas"
    }
  ],
  "analisis": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "nota": "Ratio excelente (>3 es saludable). Crecimiento sostenido indica eficiencia creciente en adquisición y retención."
    },
    "metrica_mayor_mejora_porcentual": {
      "nombre": "Support Tickets",
      "variacion": "-17.1%",
      "tipo": "Reducción (mejora)",
      "comentario": "La mayor mejora porcentual absoluta del periodo. Le sigue Active Users con +15.3%."
    },
    "proyeccion_abril": {
      "metodo": "Extrapolación lineal basada en variación promedio de los últimos 2 meses",
      "valores": {
        "MRR": 55600,
        "Churn Rate": 2.4,
        "NPS": 57,
        "CAC": 176,
        "LTV": 2670,
        "Active Users": 1900,
        "Support Tickets": 50,
        "Avg Response (h)": 1.7
      },
      "ltv_cac_ratio_proyectado": 15.17,
      "disclaimer": "Proyección lineal simple. No considera estacionalidad, cambios de mercado ni factores externos."
    }
  }
}
```