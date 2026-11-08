# DeepSeek V3 — ocr_extraction/screenshot_table_extraction

- model_id: `deepseek/deepseek-v3.2`
- success: True  | final: 8.88 | quality: 10.0
- latency_total: 19.827s | tokens_per_second: 43.8
- input_tokens: 386 | output_tokens: 868

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
  "datos_dashboard": [
    {
      "metrica": "MRR",
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "var_m_m": "+7.0%"
    },
    {
      "metrica": "Churn Rate",
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "var_m_m": "-0.7pp"
    },
    {
      "metrica": "NPS",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "var_m_m": "+6"
    },
    {
      "metrica": "CAC",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "var_m_m": "-$11"
    },
    {
      "metrica": "LTV",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "var_m_m": "+$330"
    },
    {
      "metrica": "Active Users",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "var_m_m": "+15.3%"
    },
    {
      "metrica": "Support Tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "var_m_m": "-17.1%"
    },
    {
      "metrica": "Avg Response (h)",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "var_m_m": "-0.7"
    }
  ],
  "analisis": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51
    },
    "mayor_mejora_porcentual": {
      "metrica": "Support Tickets",
      "mejora_porcentual": "-17.1%",
      "explicacion": "La reducción de tickets de soporte del 17.1% entre febrero y marzo es la mayor mejora porcentual (en términos de reducción). En métricas positivas, Active Users (+15.3%) tiene la mayor mejora."
    },
    "proyeccion_abril": {
      "suposicion": "Se mantiene la variación porcentual de marzo (último dato disponible)",
      "valores": {
        "MRR": 55747,
        "Churn Rate": 2.4,
        "NPS": 57,
        "CAC": 176,
        "LTV": 2670,
        "Active Users": 1935,
        "Support Tickets": 52,
        "Avg Response (h)": 1.7
      },
      "notas": [
        "MRR: +7.0% sobre $52.1K = $55,747",
        "Churn Rate: -0.7pp sobre 3.1% = 2.4%",
        "NPS: +6 puntos sobre 51 = 57",
        "CAC: -$11 sobre $187 = $176",
        "LTV: +$330 sobre $2,340 = $2,670",
        "Active Users: +15.3% sobre 1,678 ≈ 1,935",
        "Support Tickets: -17.1% sobre 63 ≈ 52",
        "Avg Response (h): -0.7h sobre 2.4h = 1.7h"
      ]
    }
  }
}
```