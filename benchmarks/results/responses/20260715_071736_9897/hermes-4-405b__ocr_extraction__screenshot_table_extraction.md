# Hermes 4 405B — ocr_extraction/screenshot_table_extraction

- model_id: `nousresearch/hermes-4-405b`
- success: True  | final: 8.59 | quality: 10.0
- latency_total: 13.673s | tokens_per_second: 39.2
- input_tokens: 406 | output_tokens: 536
- judge_score: 3.6 | justificación: 

## Respuesta completa

{
  "datos_originales": {
    "MRR": {
      "Enero": 45200,
      "Febrero": 48700,
      "Marzo": 52100,
      "Var_MM": "7.0%"
    },
    "Churn_Rate": {
      "Enero": "4.2%",
      "Febrero": "3.8%",
      "Marzo": "3.1%",
      "Var_MM": "-0.7pp"
    },
    "NPS": {
      "Enero": 42,
      "Febrero": 45,
      "Marzo": 51,
      "Var_MM": "+6"
    },
    "CAC": {
      "Enero": 234,
      "Febrero": 198,
      "Marzo": 187,
      "Var_MM": "-$11"
    },
    "LTV": {
      "Enero": 1890,
      "Febrero": 2010,
      "Marzo": 2340,
      "Var_MM": "+$330"
    },
    "Active_Users": {
      "Enero": 1234,
      "Febrero": 1456,
      "Marzo": 1678,
      "Var_MM": "15.3%"
    },
    "Support_Tickets": {
      "Enero": 89,
      "Febrero": 76,
      "Marzo": 63,
      "Var_MM": "-17.1%"
    },
    "Avg_Response_h": {
      "Enero": 4.2,
      "Febrero": 3.1,
      "Marzo": 2.4,
      "Var_MM": "-0.7"
    }
  },
  "LTV_CAC_ratio": {
    "Enero": 8.08,
    "Febrero": 10.15,
    "Marzo": 12.51
  },
  "mayor_mejora_porcentual": {
    "metrica": "Support_Tickets",
    "mejora_porcentual": -17.1
  },
  "proyeccion_abril": {
    "MRR": 55718,
    "Churn_Rate": "2.5%",
    "NPS": 57,
    "CAC": 173,
    "LTV": 2733,
    "Active_Users": 1923,
    "Support_Tickets": 52,
    "Avg_Response_h": 1.9
  }
}