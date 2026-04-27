# MiMo V2.5 (Xiaomi) — ocr_extraction/screenshot_table_extraction

- model_id: `mimo-v2.5`
- success: True  | final: 6.86 | quality: 6.16
- latency_total: 18.139s | tokens_per_second: 112.9
- input_tokens: 663 | output_tokens: 2048
- judge_score: 3.2 | justificación: 

## Respuesta completa

```json
{
  "dashboard": {
    "title": "KPIs Marzo 2026",
    "period": "Enero - Marzo 2026",
    "general_trend": "Positiva"
  },
  "metrics": {
    "MRR": {
      "Enero": "$45.2K",
      "Febrero": "$48.7K",
      "Marzo": "$52.1K",
      "Var_M_M": "+7.0%"
    },
    "Churn_Rate": {
      "Enero": "4.2%",
      "Febrero": "3.8%",
      "Marzo": "3.1%",
      "Var_M_M": "-0.7pp"
    },
    "NPS": {
      "Enero": 42,
      "Febrero": 45,
      "Marzo": 51,
      "Var_M_M": "+6"
    },
    "CAC": {
      "Enero": "$234",
      "Febrero": "$198",
      "Marzo": "$187",
      "Var_M_M": "-$11"
    },
    "LTV": {
      "Enero": "$1,890",
      "Febrero": "$2,010",
      "Marzo": "$2,340",
      "Var_M_M": "+$330"
    },
    "Active_Users": {
      "Enero": 1234,
      "Febrero": 1456,
      "Marzo": 1678,
      "Var_M_M": "+15.3%"
    },
    "Support_Tickets": {
      "Enero": 89,
      "Febrero": 76,
      "Marzo": 63,
      "Var_M_M": "-17.1%"
    },
    "Avg_Response_Hours": {
      "Enero": 4.2,
      "Febrero": 3.1,
      "Marzo": 2.4,
      "Var_M_M": "-0.7"
    }
  },
  "analysis": {
    "ltv_cac_ratio": {
      "Enero": 8.08,
      "Febrero": 10.15,
      "Marzo": 12.51,
      "interpretacion": "Excelente - por cada $1 invertido en adquisición, se generan $12.51 en valor lifetime. Umbral saludable: >3:1"
    },
    "mayor_mejora_porcentual": {
      "metrica": "Avg_Response_Hours",
      "mejora": "-26.2%",
      "periodo": "Enero → Febrero",
      "detalle": "Reducción de 4.2h a 3.1h en tiempo promedio de respuesta"
    },
    "proyeccion_abril_2026": {
      "MRR": "$55.7K",
      "Churn_Rate": "2.4%",
      "NPS": 57,
      "CAC": "$176",
      "LTV": "$2,670",
      "Active_Users": 1935,
      "Support_Tickets": 52,
      "Avg_Response_Hours": 1.7,
      "metodologia": "Aplicación de la tasa de variación M/M más reciente (Feb→Mar)"
    }
  },