# MiniMax M2.5 — ocr_extraction/screenshot_table_extraction

- model_id: `minimax/minimax-m2.5`
- success: True  | final: 7.47 | quality: 8.0
- latency_total: 17.039s | tokens_per_second: 114.2
- input_tokens: 394 | output_tokens: 1945

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

```json{
  "dashboard": {
    "titulo": "KPIs Marzo 2026",
    "tendencia_general": "Positiva en todas las metricas"
  },
  "metricas": [
    {
      "nombre": "MRR",
      "unidad": "USD",
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "variacion_mm": "+7.0%"
    },
    {
      "nombre": "Churn Rate",
      "unidad": "porcentaje",
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "variacion_mm": "-0.7pp"
    },
    {
      "nombre": "NPS",
      "unidad": "puntos",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "variacion_mm": "+6"
    },
    {
      "nombre": "CAC",
      "unidad": "USD",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "variacion_mm": "-11"
    },
    {
      "nombre": "LTV",
      "unidad": "USD",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "variacion_mm": "+330"
    },
    {
      "nombre": "Active Users",
      "unidad": "usuarios",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "variacion_mm": "+15.3%"
    },
    {
      "nombre": "Support Tickets",
      "unidad": "tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "variacion_mm": "-17.1%"
    },
    {
      "nombre": "Avg Response (h)",
      "unidad": "horas",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "variacion_mm": "-0.7"
    }
  ],
  "ltv_cac_ratio": {
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51,
    "nota": "Ratio LTV/CAC = Ingresos por cliente / Costo de adquisición. Valores > 3 son considerados saludables."
  },
  "metricas_mejora_porcentual": {
    "MRR": "+7.0%",
    "Churn Rate": "-16.67% (de 3.8% a 3.1%)",
    "NPS": "+13.33% (de 45 a 51)",
    "CAC": "-5.56% (de $198 a $187)",
    "LTV": "+16.42% (de $2,010 a $2,340)",
    "Active Users": "+15.25% (de 1,456 a 1,678)",
    "Support Tickets": "-17.11% (de 76 a 63)",
    "Avg Response (h)": "-22.58% (de 3.1h a 2.4h)"
  },
  "metrica_mayor_mejora": {
    "nombre": "Avg Response (h)",
    "mejora_porcentual": "-22.58%",
    "descripcion": "Tiempo promedio de respuesta se redujo de 3.1h a 2.4h"
  },
  "proyecciones_abril": {
    "supuesto": "Tendencia mensual se mantiene constante",
    "MRR": {
      "valor": 55750,
      "unidad": "USD",
      "calculo": "52100 * 1.07"
    },
    "Churn Rate": {
      "valor": 2.4,
      "unidad": "porcentaje",
      "calculo": "3.1 - 0.7"
    },
    "NPS": {
      "valor": 57,
      "unidad": "puntos",
      "calculo": "51 + 6"
    },
    "CAC": {
      "valor": 176,
      "unidad": "USD",
      "calculo": "187 - 11"
    },
    "LTV": {
      "valor": 2670,
      "unidad": "USD",
      "calculo": "2340 + 330"
    },
    "Active Users": {
      "valor": 1935,
      "unidad": "usuarios",
      "calculo": "1678 * 1.153"
    },
    "Support Tickets": {
      "valor": 52,
      "unidad": "tickets",
      "calculo": "63 * (1 - 0.171)"
    },
    "Avg Response (h)": {
      "valor": 1.7,
      "unidad": "horas",
      "calculo": "2.4 - 0.7"
    },
    "LTV/CAC_ratio": {
      "valor": 15.17,
      "calculo": "2670 / 176"
    }
  },
  "analisis": {
    "resumen": "Todas las métricas muestran tendencia positiva. El ratio LTV/CAC mejora significativamente de 8.08 a 12.51, indicando mayor rentabilidad por cliente.",
    "recomendacion": "Mantener las estrategias actuales ya que todas las métricas clave están mejorando mes a mes."
  }
}
```