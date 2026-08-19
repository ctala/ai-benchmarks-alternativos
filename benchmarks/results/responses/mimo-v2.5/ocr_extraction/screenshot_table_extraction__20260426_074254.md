# MiMo-V2.5 (omnimodal) — ocr_extraction/screenshot_table_extraction

- model_id: `xiaomi/mimo-v2.5`
- success: True  | final: 6.42 | quality: 6.64
- latency_total: 14.805s | tokens_per_second: 138.3
- input_tokens: 663 | output_tokens: 2048
- judge_score: 3.8 | justificación: 

## Respuesta completa

```json
{
  "dashboard_info": {
    "titulo": "KPIs Marzo 2026",
    "periodo": "Enero - Marzo 2026",
    "tendencia_general": "Positiva en todas las métricas"
  },
  
  "datos_extraidos": {
    "MRR": {
      "enero": "$45.2K",
      "febrero": "$48.7K",
      "marzo": "$52.1K",
      "variacion_mm": "+7.0%"
    },
    "churn_rate": {
      "enero": "4.2%",
      "febrero": "3.8%",
      "marzo": "3.1%",
      "variacion_mm": "-0.7pp"
    },
    "NPS": {
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "variacion_mm": "+6"
    },
    "CAC": {
      "enero": "$234",
      "febrero": "$198",
      "marzo": "$187",
      "variacion_mm": "-$11"
    },
    "LTV": {
      "enero": "$1,890",
      "febrero": "$2,010",
      "marzo": "$2,340",
      "variacion_mm": "+$330"
    },
    "active_users": {
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "variacion_mm": "+15.3%"
    },
    "support_tickets": {
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "variacion_mm": "-17.1%"
    },
    "avg_response_horas": {
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "variacion_mm": "-0.7"
    }
  },

  "analisis_ltv_cac_ratio": {
    "enero": {
      "LTV": 1890,
      "CAC": 234,
      "ratio": 8.08
    },
    "febrero": {
      "LTV": 2010,
      "CAC": 198,
      "ratio": 10.15
    },
    "marzo": {
      "LTV": 2340,
      "CAC": 187,
      "ratio": 12.51
    },
    "tendencia": "Crecimiento sostenido del ratio (+54.8% en 3 meses)",
    "benchmark": "Ratio > 3 es saludable; ratio actual excelente (>10)"
  },

  "mayor_mejora_porcentual": {
    "metrica": "Avg Response (horas)",
    "valor_enero": 4.2,
    "valor_marzo": 2.4,
    "mejora_porcentual": "-42.86%",
    "interpretacion": "Reducción del tiempo de respuesta casi a la mitad"
  },

  "top_3_mejoras": [
    {
      "posicion": 1,
      "metrica": "Avg Response (h)",
      "mejora": "-42.86%",
      "tipo": "menor es mejor"
    },
    {
      "posicion": 2,
      "metrica": "Churn Rate",
      "mejora": "-26.19%",
      "tipo": "menor es mejor"
    },
    {
      "posicion": 3,
      "metrica": "Support Tickets",
      "mejora": "-29.21%",
      "tipo": "menor es mejor"
    }
  ],

  "proyeccion_abril_2026": {
    "metodologia": "Extrapolación basada en tendencia lineal promedio Ene-Mar",
    "MRR": {
      "valor": "$55.6K",
      "crescimiento_estimado": "+6.7%"
    },
    "churn_rate": {
      "valor": "2.5%",
      "reduccion_estimada": "-0.6pp"
    },
    "NPS": {
      "valor": 56,
      "incremento_estimado": "+5"
    },
    "CAC": {
      "valor": "$176",
      "reduccion_estimada": "-$11"
    },
    "L