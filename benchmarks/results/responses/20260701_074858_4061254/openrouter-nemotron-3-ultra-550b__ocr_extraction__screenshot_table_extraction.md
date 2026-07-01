# Nemotron 3 Ultra 550B — ocr_extraction/screenshot_table_extraction

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 4.63 | quality: 4.4
- latency_total: 30.32s | tokens_per_second: 75.6
- input_tokens: 435 | output_tokens: 2292

## Respuesta completa

{
  "dashboard": {
    "periodo": "Marzo 2026",
    "metricas": {
      "MRR": { "enero": 45200, "febrero": 48700, "marzo": 52100, "var_m_m_pct": 7.0 },
      "Churn_Rate": { "enero": 4.2, "febrero": 3.8, "marzo": 3.1, "var_m_m_pp": -0.7 },
      "NPS": { "enero": 42, "febrero": 45, "marzo": 51, "var_m_m_abs": 6 },
      "CAC": { "enero": 234, "febrero": 198, "marzo": 187, "var_m_m_abs": -11 },
      "LTV": { "enero": 1890, "febrero": 2010, "marzo": 2340, "var_m_m_abs": 330 },
      "Active_Users": { "enero": 1234, "febrero": 1456, "marzo": 1678, "var_m_m_pct": 15.3 },
      "Support_Tickets": { "enero": 89, "febrero": 76, "marzo": 63, "var_m_m_pct": -17.1 },
      "Avg_Response_h": { "enero": 4.2, "febrero": 3.1, "marzo": 2.4, "var_m_m_abs": -0.7 }
    },
    "tendencia_general": "Positiva en todas las metricas"
  },
  "LTV_CAC_ratio": {
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51
  },
  "metrica_mayor_mejora_porcentual": {
    "metrica": "Avg_Response_h",
    "mejora_pct": -22.6,
    "direccion": "Reduccion de 22.6% (mejora favorable)",
    "nota": "Mayor mejora porcentual en direccion favorable. Entre metricas de crecimiento: LTV (+16.4%)"
  },
  "proyeccion_abril": {
    "metodo": "Extrapolacion tendencia mes-a-mes (Feb->Mar)",
    "valores_proyectados": {
      "MRR": 55747,
      "Churn_Rate": 2.4,
      "NPS": 57,
      "CAC": 176,
      "LTV": 2670,
      "Active_Users": 1935,
      "Support_Tickets": 52,
      "Avg_Response_h": 1.7
    },
    "LTV_CAC_ratio_proyectado": 15.17
  }
}