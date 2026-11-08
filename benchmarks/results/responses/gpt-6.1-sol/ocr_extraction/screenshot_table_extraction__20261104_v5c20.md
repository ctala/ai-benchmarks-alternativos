# GPT-6.1 Sol — ocr_extraction/screenshot_table_extraction

- model_id: `openai/gpt-6.1-sol`
- success: True  | final: 6.95 | quality: 8.0
- latency_total: 15.067s | tokens_per_second: 91.9
- input_tokens: 379 | output_tokens: 1384

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
  "titulo": "DASHBOARD - KPIs Marzo 2026",
  "datos": {
    "2026-01": {
      "mrr": 45200,
      "churn_rate_pct": 4.2,
      "nps": 42,
      "cac": 234,
      "ltv": 1890,
      "usuarios_activos": 1234,
      "tickets_soporte": 89,
      "tiempo_respuesta_promedio_h": 4.2
    },
    "2026-02": {
      "mrr": 48700,
      "churn_rate_pct": 3.8,
      "nps": 45,
      "cac": 198,
      "ltv": 2010,
      "usuarios_activos": 1456,
      "tickets_soporte": 76,
      "tiempo_respuesta_promedio_h": 3.1
    },
    "2026-03": {
      "mrr": 52100,
      "churn_rate_pct": 3.1,
      "nps": 51,
      "cac": 187,
      "ltv": 2340,
      "usuarios_activos": 1678,
      "tickets_soporte": 63,
      "tiempo_respuesta_promedio_h": 2.4
    }
  },
  "unidades": {
    "mrr": "moneda indicada con $; divisa no especificada",
    "churn_rate_pct": "porcentaje",
    "nps": "puntos",
    "cac": "moneda indicada con $; divisa no especificada",
    "ltv": "moneda indicada con $; divisa no especificada",
    "usuarios_activos": "usuarios",
    "tickets_soporte": "tickets",
    "tiempo_respuesta_promedio_h": "horas"
  },
  "variacion_mensual_mostrada": {
    "periodo": "2026-02 a 2026-03",
    "mrr": "+7.0%",
    "churn_rate": "-0.7pp",
    "nps": "+6",
    "cac": "-$11",
    "ltv": "+$330",
    "usuarios_activos": "+15.3%",
    "tickets_soporte": "-17.1%",
    "tiempo_respuesta_promedio_h": "-0.7"
  },
  "ltv_cac_ratio": {
    "formula": "LTV / CAC",
    "2026-01": 8.08,
    "2026-02": 10.15,
    "2026-03": 12.51
  },
  "mejora_porcentual": {
    "periodo": "2026-02 a 2026-03",
    "criterio": "Cambio relativo respecto a febrero, considerando favorable el aumento de MRR, NPS, LTV y usuarios activos, y la disminución de churn, CAC, tickets y tiempo de respuesta.",
    "formula": "100 * cambio favorable / valor de febrero",
    "por_metrica_pct": {
      "mrr": 6.98,
      "churn_rate": 18.42,
      "nps": 13.33,
      "cac": 5.56,
      "ltv": 16.42,
      "usuarios_activos": 15.25,
      "tickets_soporte": 17.11,
      "tiempo_respuesta_promedio_h": 22.58
    },
    "mayor_mejora": {
      "metrica": "tiempo_respuesta_promedio_h",
      "valor_febrero": 3.1,
      "valor_marzo": 2.4,
      "reduccion_pct": 22.58
    }
  },
  "proyeccion_abril": {
    "periodo": "2026-04",
    "metodo": "Extrapolación lineal del cambio absoluto entre febrero y marzo.",
    "formula": "abril = marzo + (marzo - febrero)",
    "valores": {
      "mrr": 55500,
      "churn_rate_pct": 2.4,
      "nps": 57,
      "cac": 176,
      "ltv": 2670,
      "usuarios_activos": 1900,
      "tickets_soporte": 50,
      "tiempo_respuesta_promedio_h": 1.7
    },
    "ltv_cac_ratio": 15.17,
    "advertencia": "Proyección mecánica basada en el último cambio mensual; no constituye un pronóstico validado."
  },
  "tendencia_general": {
    "texto_original": "↑ Positiva en todas las metricas",
    "interpretacion": "Todas las métricas evolucionan en la dirección considerada favorable."
  },
  "notas": [
    "Los importes expresados en K se han multiplicado por 1000.",
    "La mejora porcentual del churn es una reducción relativa; no debe confundirse con su caída de 0.7 puntos porcentuales.",
    "El dashboard muestra +15.3% para usuarios activos, pero los valores visibles arrojan +15.25%, equivalente a +15.2% redondeado a un decimal.",
    "Los cálculos utilizan los valores visibles, que pueden estar redondeados."
  ]
}