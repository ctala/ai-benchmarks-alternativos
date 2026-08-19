# Kimi K2.6 — ocr_extraction/screenshot_table_extraction

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 5.53 | quality: 5.8
- latency_total: 445.114s | tokens_per_second: 18.4
- input_tokens: 386 | output_tokens: 8192
- judge_score: 3.2 | justificación: 

## Respuesta completa

 ```json
{
  "dashboard_kpis": {
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "periodos": ["Enero", "Febrero", "Marzo"],
    "metricas": {
      "MRR": {
        "valores": [45200, 48700, 52100],
        "display": ["$45.2K", "$48.7K", "$52.1K"],
        "unidad": "USD",
        "variacion_mom": "+7.0%"
      },
      "Churn Rate": {
        "valores": [4.2, 3.8, 3.1],
        "display": ["4.2%", "3.8%", "3.1%"],
        "unidad": "porcentaje",
        "variacion_mom": "-0.7pp"
      },
      "NPS": {
        "valores": [42, 45, 51],
        "display": ["42", "45", "51"],
        "unidad": "puntos",
        "variacion_mom": "+6"
      },
      "CAC": {
        "valores": [234, 198, 187],
        "display": ["$234", "$198", "$187"],
        "unidad": "USD",
        "variacion_mom": "-$11"
      },
      "LTV": {
        "valores": [1890, 2010, 2340],
        "display": ["$1,890", "$2,010", "$2,340"],
        "unidad": "USD",
        "variacion_mom": "+$330"
      },
      "Active Users": {
        "valores": [1234, 1456, 1678],
        "display": ["1,234", "1,456", "1,678"],
        "unidad": "usuarios",
        "variacion_mom": "+15.3%"
      },
      "Support Tickets": {
        "valores": [89, 76, 63],
        "display": ["89", "76", "63"],
        "unidad": "tickets",
        "variacion_mom": "-17.1%"
      },
      "Avg Response": {
        "valores": [4.2, 3.1, 2.4],
        "display": ["4.2h", "3.1h", "2.4h"],
        "unidad": "horas",
        "variacion_mom": "-0.7h"
      }
    }
  },
  "analisis": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "evaluacion": "Saludable y en crecimiento (objetivo SaaS > 3)"
    },
    "mayor_mejora_porcentual": {
      "metrica": "Avg Response (h)",
      "cambio_relativo_mom": "-22.6%",
      "contexto": "Mayor tasa de cambio favorable de Febrero a Marzo. Si se considera solo crecimiento positivo, el lider es LTV con +16.4% MoM.",
      "ranking_mom": [
        {"metrica": "Avg Response (h)", "cambio": "-22.6%"},
        {"metrica": "Churn Rate", "cambio": "-18.4%"},
        {"metrica": "Support Tickets", "cambio": "-17.1%"},
        {"metrica": "LTV", "cambio": "+16.4%"}
      ]
    },
    "proyeccion_abril_2026": {
     