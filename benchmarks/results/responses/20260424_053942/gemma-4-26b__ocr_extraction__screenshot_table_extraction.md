# Gemma 4 26B MoE (3.8B activos) — ocr_extraction/screenshot_table_extraction

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 6.33 | quality: 5.8
- latency_total: 16.488s | tokens_per_second: 55.7
- input_tokens: 431 | output_tokens: 919
- judge_score: 3.2 | justificación: 

## Respuesta completa

```json
{
  "dashboard_info": {
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "tendencia_general": "Positiva"
  },
  "datos_extraidos": {
    "metricas": [
      {
        "metrica": "MRR",
        "unidades": "USD",
        "enero": 45200,
        "febrero": 48700,
        "marzo": 52100,
        "var_m_m_pct": 7.0
      },
      {
        "metrica": "Churn Rate",
        "unidades": "porcentaje",
        "enero": 4.2,
        "febrero": 3.8,
        "marzo": 3.1,
        "var_m_m_pp": -0.7
      },
      {
        "metrica": "NPS",
        "unidades": "puntos",
        "enero": 42,
        "febrero": 45,
        "marzo": 51,
        "var_m_m_puntos": 6
      },
      {
        "metrica": "CAC",
        "unidades": "USD",
        "enero": 234,
        "febrero": 198,
        "marzo": 187,
        "var_m_m_usd": -11
      },
      {
        "metrica": "LTV",
        "unidades": "USD",
        "enero": 1890,
        "febrero": 2010,
        "marzo": 2340,
        "var_m_m_usd": 330
      },
      {
        "metrica": "Active Users",
        "unidades": "cantidad",
        "enero": 1234,
        "febrero": 1456,
        "marzo": 1678,
        "var_m_m_pct": 15.3
      },
      {
        "metrica": "Support Tickets",
        "unidades": "cantidad",
        "enero": 89,
        "febrero": 76,
        "marzo": 63,
        "var_m_m_pct": -17.1
      },
      {
        "metrica": "Avg Response (h)",
        "unidades": "horas",
        "enero": 4.2,
        "febrero": 3.1,
        "marzo": 2.4,
        "var_m_m_h": -0.7
      }
    ]
  },
  "analisis": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51
    },
    "mayor_mejora_porcentual": {
      "metrica": "Support Tickets",
      "valor_mejora": "-17.1%"
    },
    "proyeccion_abril": {
      "metodologia": "Basada en la variación porcentual de Marzo respecto a Febrero",
      "valores_proyectados": {
        "MRR": 55747,
        "Churn Rate": 2.86,
        "NPS": 57.5,
        "CAC": 175.3,
        "LTV": 2711.4,
        "Active Users": 1935.7,
        "Support Tickets": 52.2,
        "Avg Response (h)": 1.8
      }
    }
  }
}
```