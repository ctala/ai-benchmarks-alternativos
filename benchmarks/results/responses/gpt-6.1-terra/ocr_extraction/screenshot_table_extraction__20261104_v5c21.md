# GPT-6.1 Terra — ocr_extraction/screenshot_table_extraction

- model_id: `openai/gpt-6.1-terra`
- success: True  | final: 7.29 | quality: 8.0
- latency_total: 8.587s | tokens_per_second: 80.8
- input_tokens: 379 | output_tokens: 694

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
  "dashboard": "KPIs Marzo 2026",
  "datos": {
    "enero": {
      "MRR_USD": 45200,
      "churn_rate_pct": 4.2,
      "NPS": 42,
      "CAC_USD": 234,
      "LTV_USD": 1890,
      "usuarios_activos": 1234,
      "tickets_soporte": 89,
      "tiempo_respuesta_medio_horas": 4.2
    },
    "febrero": {
      "MRR_USD": 48700,
      "churn_rate_pct": 3.8,
      "NPS": 45,
      "CAC_USD": 198,
      "LTV_USD": 2010,
      "usuarios_activos": 1456,
      "tickets_soporte": 76,
      "tiempo_respuesta_medio_horas": 3.1
    },
    "marzo": {
      "MRR_USD": 52100,
      "churn_rate_pct": 3.1,
      "NPS": 51,
      "CAC_USD": 187,
      "LTV_USD": 2340,
      "usuarios_activos": 1678,
      "tickets_soporte": 63,
      "tiempo_respuesta_medio_horas": 2.4
    }
  },
  "variacion_mensual_mostrada_febrero_a_marzo": {
    "MRR": "+7.0%",
    "churn_rate": "-0.7 puntos porcentuales",
    "NPS": "+6 puntos",
    "CAC": "-$11",
    "LTV": "+$330",
    "usuarios_activos": "+15.3%",
    "tickets_soporte": "-17.1%",
    "tiempo_respuesta_medio": "-0.7 horas"
  },
  "tendencia_general_mostrada": "Positiva en todas las métricas",
  "ratio_LTV_CAC": {
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51
  },
  "mayor_mejora_porcentual": {
    "metrica": "tiempo_respuesta_medio",
    "periodo": "febrero a marzo",
    "cambio_pct": -22.58,
    "interpretacion": "Reducción del 22.58%, calculada respecto al valor de febrero."
  },
  "proyeccion_abril": {
    "metodo": "Se aplica a cada métrica el mismo cambio absoluto observado entre febrero y marzo.",
    "valores": {
      "MRR_USD": 55500,
      "churn_rate_pct": 2.4,
      "NPS": 57,
      "CAC_USD": 176,
      "LTV_USD": 2670,
      "usuarios_activos": 1900,
      "tickets_soporte": 50,
      "tiempo_respuesta_medio_horas": 1.7
    },
    "advertencia": "Es una extrapolación lineal, no una predicción garantizada."
  }
}