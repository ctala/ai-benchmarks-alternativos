# GLM 5.1 (NIM) — ocr_extraction/screenshot_table_extraction

- model_id: `z-ai/glm-5.1`
- success: True  | final: 6.16 | quality: 6.16
- latency_total: 74.982s | tokens_per_second: 10.1
- input_tokens: 349 | output_tokens: 757
- judge_score: 3.2 | justificación: 

## Respuesta completa

```json
{
  "dashboard_data": {
    "period": "Marzo 2026",
    "raw_data": [
      {
        "metrica": "MRR",
        "enero": "$45.2K",
        "febrero": "$48.7K",
        "marzo": "$52.1K",
        "var_m_m": "+7.0%"
      },
      {
        "metrica": "Churn Rate",
        "enero": "4.2%",
        "febrero": "3.8%",
        "marzo": "3.1%",
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
        "var_m_m": -11
      },
      {
        "metrica": "LTV",
        "enero": 1890,
        "febrero": 2010,
        "marzo": 2340,
        "var_m_m": 330
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
        "var_m_m": -0.7
      }
    ]
  },
  "analisis": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "observacion": "El ratio LTV/CAC muestra una mejora continua y significativa, indicando una mayor eficiencia y rentabilidad por cliente."
    },
    "metrica_mayor_mejora": {
      "metrica": "Support Tickets",
      "mejora_porcentual": "-17.1%",
      "justificacion": "Representa la mayor variación porcentual absoluta mes a mes. Una reducción del 17.1% en tickets de soporte es la mejora más pronunciada del periodo, indicando mayor estabilidad del producto o mejor autoservicio."
    },
    "proyeccion_abril": {
      "metodologia": "Proyección basada en la extrapolación de la tasa de crecimiento/variación observada entre Febrero y Marzo (Var M/M)",
      "valores_proyectados": {
        "MRR": "$55.7K",
        "Churn Rate": "2.4%",
        "NPS": 57,
        "CAC": "$176",
        "LTV": "$2,670",
        "Active Users": 1934,
        "Support Tickets": 52,
        "Avg Response (h)": 1.7
      }
    }
  }
}
```