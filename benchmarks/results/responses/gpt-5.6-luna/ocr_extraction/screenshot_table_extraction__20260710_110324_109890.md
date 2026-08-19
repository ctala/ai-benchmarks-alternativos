# GPT-5.6 Luna — ocr_extraction/screenshot_table_extraction

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 5.52 | quality: 5.52
- latency_total: 9.644s | tokens_per_second: 160.8
- input_tokens: 379 | output_tokens: 1551
- judge_score: 3.0 | justificación: La respuesta incluye datos no presentes en la tabla original, como LTV, usuarios activos y tickets de soporte, lo que afecta la precisión y exactitud de los datos; sin embargo, ofrece análisis útiles y proyecciones, con buena claridad y relevancia general.

## Respuesta completa

{
  "dashboard": {
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "periodo": "Marzo 2026",
    "tendencia_general": "Positiva en todas las métricas"
  },
  "datos": {
    "Enero": {
      "mrr_usd": 45200,
      "churn_rate_pct": 4.2,
      "nps": 42,
      "cac_usd": 234,
      "ltv_usd": 1890,
      "usuarios_activos": 1234,
      "tickets_soporte": 89,
      "tiempo_respuesta_promedio_horas": 4.2
    },
    "Febrero": {
      "mrr_usd": 48700,
      "churn_rate_pct": 3.8,
      "nps": 45,
      "cac_usd": 198,
      "ltv_usd": 2010,
      "usuarios_activos": 1456,
      "tickets_soporte": 76,
      "tiempo_respuesta_promedio_horas": 3.1
    },
    "Marzo": {
      "mrr_usd": 52100,
      "churn_rate_pct": 3.1,
      "nps": 51,
      "cac_usd": 187,
      "ltv_usd": 2340,
      "usuarios_activos": 1678,
      "tickets_soporte": 63,
      "tiempo_respuesta_promedio_horas": 2.4
    }
  },
  "variacion_marzo_vs_febrero": {
    "mrr_pct": 7.0,
    "churn_rate_pp": -0.7,
    "nps_puntos": 6,
    "cac_usd": -11,
    "ltv_usd": 330,
    "usuarios_activos_pct": 15.3,
    "tickets_soporte_pct": -17.1,
    "tiempo_respuesta_promedio_horas": -0.7
  },
  "ltv_cac_ratio": {
    "Enero": {
      "ratio": 8.08,
      "formula": "1890 / 234"
    },
    "Febrero": {
      "ratio": 10.15,
      "formula": "2010 / 198"
    },
    "Marzo": {
      "ratio": 12.51,
      "formula": "2340 / 187"
    }
  },
  "metrica_con_mayor_mejora_porcentual": {
    "metrica": "Support Tickets",
    "mejora_porcentual": 17.1,
    "interpretacion": "Reducción de tickets de soporte entre febrero y marzo, considerada una mejora operativa.",
    "nota": "Si solo se consideran incrementos positivos, la mayor mejora corresponde a Active Users, con un crecimiento del 15.3%."
  },
  "proyeccion_abril": {
    "metodo": "Aplicación de la variación observada entre febrero y marzo.",
    "mrr_usd": 55747,
    "mrr_formateado": "$55.75K",
    "churn_rate_pct": 2.4,
    "nps": 57,
    "cac_usd": 176,
    "ltv_usd": 2670,
    "usuarios_activos": 1935,
    "tickets_soporte": 52,
    "tiempo_respuesta_promedio_horas": 1.7,
    "ltv_cac_ratio": 15.17
  }
}