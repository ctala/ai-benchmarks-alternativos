# Muse Spark 1.3 — ocr_extraction/screenshot_table_extraction

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 7.11 | quality: 8.0
- latency_total: 16.381s | tokens_per_second: 194.0
- input_tokens: 363 | output_tokens: 3178

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
  "dashboard": "KPIs Marzo 2026",
  "tendencia_general": "Positiva en todas las metricas",
  "extraccion_datos": [
    {
      "metrica": "MRR",
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "unidad": "USD",
      "var_m_m_reportada": "+7.0%"
    },
    {
      "metrica": "Churn Rate",
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "unidad": "%",
      "var_m_m_reportada": "-0.7pp"
    },
    {
      "metrica": "NPS",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "unidad": "puntos",
      "var_m_m_reportada": "+6"
    },
    {
      "metrica": "CAC",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "unidad": "USD",
      "var_m_m_reportada": "-$11"
    },
    {
      "metrica": "LTV",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "unidad": "USD",
      "var_m_m_reportada": "+$330"
    },
    {
      "metrica": "Active Users",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "unidad": "usuarios",
      "var_m_m_reportada": "+15.3%"
    },
    {
      "metrica": "Support Tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "unidad": "tickets",
      "var_m_m_reportada": "-17.1%"
    },
    {
      "metrica": "Avg Response",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "unidad": "horas",
      "var_m_m_reportada": "-0.7"
    }
  ],
  "ltv_cac_ratio": {
    "formula": "LTV / CAC",
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51,
    "calculo_detalle": {
      "enero": "1890 / 234 = 8.0769",
      "febrero": "2010 / 198 = 10.1515",
      "marzo": "2340 / 187 = 12.5134"
    }
  },
  "analisis_mejora_porcentual_m_m_feb_mar": {
    "metodo": "variacion_porcentual = (marzo - febrero) / febrero * 100. Para Churn, CAC, Tickets y Response, valor negativo es mejora.",
    "variaciones": {
      "MRR": 6.98,
      "Churn_Rate_relativa": -18.42,
      "NPS": 13.33,
      "CAC": -5.56,
      "LTV": 16.42,
      "Active_Users": 15.25,
      "Support_Tickets": -17.11,
      "Avg_Response_h": -22.58
    },
    "metrica_con_mayor_mejora_porcentual": {
      "metrica": "Avg Response (h)",
      "variacion_porcentual_m_m": -22.58,
      "mejora_en_valor_absoluto": "de 3.1h a 2.4h (-0.7h)",
      "interpretacion": "Reduccion del 22.58% en tiempo de respuesta, es la mayor mejora porcentual M/M. Le sigue Churn Rate con -18.42% relativo."
    }
  },
  "proyeccion_abril_2026": {
    "metodo": "mantener misma variacion M/M de marzo (misma diferencia absoluta para Churn, NPS, CAC, LTV, Avg Response; mismo % para MRR, Active Users, Support Tickets)",
    "valores_proyectados": {
      "MRR": 55747,
      "MRR_formato": "$55.7K",
      "MRR_calculo": "52100 * 1.07",
      "Churn_Rate": 2.4,
      "Churn_Rate_unidad": "%",
      "Churn_Rate_calculo": "3.1 - 0.7",
      "NPS": 57,
      "NPS_calculo": "51 + 6",
      "CAC": 176,
      "CAC_unidad": "USD",
      "CAC_calculo": "187 - 11",
      "LTV": 2670,
      "LTV_unidad": "USD",
      "LTV_calculo": "2340 + 330",
      "Active_Users": 1935,
      "Active_Users_calculo": "1678 * 1.153",
      "Support_Tickets": 52,
      "Support_Tickets_calculo": "63 * (1 - 0.171) = 52.23",
      "Avg_Response_h": 1.7,
      "Avg_Response_calculo": "2.4 - 0.7"
    },
    "ltv_cac_ratio_proyectado_abril": 15.17,
    "ltv_cac_calculo_abril": "2670 / 176 = 15.1705"
  }
}