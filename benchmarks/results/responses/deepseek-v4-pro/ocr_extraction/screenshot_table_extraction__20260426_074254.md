# DeepSeek V4 Pro — ocr_extraction/screenshot_table_extraction

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 5.63 | quality: 5.8
- latency_total: 87.02s | tokens_per_second: 31.1
- input_tokens: 386 | output_tokens: 2709
- judge_score: 3.2 | justificación: 

## Respuesta completa

{
  "extracted_data": {
    "MRR": { "Enero": 45.2, "Febrero": 48.7, "Marzo": 52.1, "Var_M/M": "+7.0%" },
    "Churn_Rate": { "Enero": 4.2, "Febrero": 3.8, "Marzo": 3.1, "Var_M/M": "-0.7pp" },
    "NPS": { "Enero": 42, "Febrero": 45, "Marzo": 51, "Var_M/M": "+6" },
    "CAC": { "Enero": 234, "Febrero": 198, "Marzo": 187, "Var_M/M": "-$11" },
    "LTV": { "Enero": 1890, "Febrero": 2010, "Marzo": 2340, "Var_M/M": "+$330" },
    "Active_Users": { "Enero": 1234, "Febrero": 1456, "Marzo": 1678, "Var_M/M": "+15.3%" },
    "Support_Tickets": { "Enero": 89, "Febrero": 76, "Marzo": 63, "Var_M/M": "-17.1%" },
    "Avg_Response_h": { "Enero": 4.2, "Febrero": 3.1, "Marzo": 2.4, "Var_M/M": "-0.7" }
  },
  "ltv_cac_ratio": {
    "Enero": 8.08,
    "Febrero": 10.15,
    "Marzo": 12.51
  },
  "metrica_mayor_mejora_porcentual": {
    "metrica": "Avg Response (h)",
    "mejora_porcentual": 22.58,
    "direccion": "reducción (mejora)"
  },
  "proyeccion_abril": {
    "MRR": 55.75,
    "Churn_Rate": 2.4,
    "NPS": 57,
    "CAC": 176,
    "LTV": 2670,
    "Active_Users": 1935,
    "Support_Tickets": 52,
    "Avg_Response_h": 1.7
  }
}