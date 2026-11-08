# Inkling Small — ocr_extraction/screenshot_table_extraction

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 8.81 | quality: 10.0
- latency_total: 20.402s | tokens_per_second: 50.4
- input_tokens: 385 | output_tokens: 1028

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
  "origen": "Dashboard KPIs Marzo 2026",
  "datos_raw": [
    {"metrica": "MRR", "enero": "$45.2K", "feb": "$48.7K", "marzo": "$52.1K", "var_mm": "+7.0%"},
    {"metrica": "Churn Rate", "enero": "4.2%", "feb": "3.8%", "marzo": "3.1%", "var_mm": "-0.7pp"},
    {"metrica": "NPS", "enero": 42, "feb": 45, "marzo": 51, "var_mm": "+6"},
    {"metrica": "CAC", "enero": "$234", "feb": "$198", "marzo": "$187", "var_mm": "-$11"},
    {"metrica": "LTV", "enero": "$1,890", "feb": "$2,010", "marzo": "$2,340", "var_mm": "+$330"},
    {"metrica": "Active Users", "enero": 1234, "feb": 1456, "marzo": 1678, "var_mm": "+15.3%"},
    {"metrica": "Support Tickets", "enero": 89, "feb": 76, "marzo": 63, "var_mm": "-17.1%"},
    {"metrica": "Avg Response (h)", "enero": 4.2, "feb": 3.1, "marzo": 2.4, "var_mm": "-0.7"}
  ],
  "analisis": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "feb": 10.15,
      "marzo": 12.51,
      "nota": "Calculado como LTV / CAC con valores absolutos por mes"
    },
    "mejor_mejora_porcentual": {
      "metrica": "Support Tickets",
      "mejora": "-17.1%",
      "interpretacion": "Mayor reduccion porcentual mes a mes (mejora operativa). Si se considera solo incremento absoluto, Active Users (+15.3%) es el mayor crecimiento positivo.",
      "detalle_comparativo": {
        "MRR": "+7.0%",
        "Churn Rate": "-18.4% relativo (3.8->3.1)",
        "NPS": "+13.3% relativo",
        "CAC": "-5.6% relativo",
        "LTV": "+16.4% relativo",
        "Active Users": "+15.3%",
        "Support Tickets": "-17.1%",
        "Avg Response": "-22.6% relativo"
      }
    },
    "proyeccion_abril": {
      "metodo": "Tendencia mes a mes (Feb -> Mar) aplicada a Marzo",
      "valores_proyectados": {
        "MRR": "$55.7K",
        "Churn Rate": "2.4%",
        "NPS": 57,
        "CAC": "$176",
        "LTV": "$2,670",
        "Active Users": 1900,
        "Support Tickets": 50,
        "Avg Response (h)": 1.7
      },
      "notas": {
        "MRR": "Var M/M aplicada como +7.0% sobre $52.1K",
        "Churn Rate": "Reduccion de 0.7pp aplicada (3.1% - 0.7pp)",
        "NPS": "+6 puntos",
        "CAC": "Reduccion de $11",
        "LTV": "+$330",
        "Active Users": "+15.3% sobre 1,678",
        "Support Tickets": "-17.1% sobre 63",
        "Avg Response": "-0.7h sobre 2.4"
      },
      "ltv_cac_proyectado_abril": 15.17,
      "tendencia_general": "Positiva en todas las metricas; proyecciones mantienen la trayectoria ascendente/descendente segun corresponda"
    }
  },
  "resumen_ejecutivo": "MRR, LTV y usuarios crecen; churn, CAC, tickets y tiempo de respuesta bajan. El ratio LTV/CAC paso de 8.1x a 12.5x en dos meses. La mayor mejora porcentual mensual es la reduccion de tickets (-17.1%). Proyectando Abril con la misma tendencia M/M se espera MRR ~$55.7K, Churn ~2.4% y LTV/CAC ~15.2x."
}