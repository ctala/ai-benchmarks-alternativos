# DeepSeek V4 Flash (OpenRouter) — ocr_extraction/screenshot_table_extraction

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 9.17 | quality: 10.0
- latency_total: 13.456s | tokens_per_second: 59.5
- input_tokens: 386 | output_tokens: 800

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

```json
{
  "datos_extraidos": {
    "MRR": { "Enero": "$45.2K", "Febrero": "$48.7K", "Marzo": "$52.1K", "Var_M_M": "+7.0%" },
    "Churn_Rate": { "Enero": "4.2%", "Febrero": "3.8%", "Marzo": "3.1%", "Var_M_M": "-0.7pp" },
    "NPS": { "Enero": 42, "Febrero": 45, "Marzo": 51, "Var_M_M": "+6" },
    "CAC": { "Enero": "$234", "Febrero": "$198", "Marzo": "$187", "Var_M_M": "-$11" },
    "LTV": { "Enero": "$1,890", "Febrero": "$2,010", "Marzo": "$2,340", "Var_M_M": "+$330" },
    "Active_Users": { "Enero": 1234, "Febrero": 1456, "Marzo": 1678, "Var_M_M": "+15.3%" },
    "Support_Tickets": { "Enero": 89, "Febrero": 76, "Marzo": 63, "Var_M_M": "-17.1%" },
    "Avg_Response_Time_h": { "Enero": 4.2, "Febrero": 3.1, "Marzo": 2.4, "Var_M_M": "-0.7" }
  },
  "LTV_CAC_ratio": {
    "Enero": 8.08,
    "Febrero": 10.15,
    "Marzo": 12.51
  },
  "mayor_mejora_porcentual": {
    "metrica": "Support_Tickets",
    "detalle": "Reducción del 17.1% intermensual en marzo (de 76 a 63 tickets)",
    "justificacion": "Considerando la magnitud del cambio relativo y que es una mejora (menos tickets), es la métrica con mayor variación porcentual absoluta."
  },
  "proyeccion_abril": {
    "MRR": { "valor_proyectado": "$55.7K", "metodo": "Crecimiento del 7% sobre $52.1K" },
    "Churn_Rate": { "valor_proyectado": "2.4%", "metodo": "Reducción de 0.7pp desde 3.1%" },
    "NPS": { "valor_proyectado": 57, "metodo": "Incremento de 6 puntos desde 51" },
    "CAC": { "valor_proyectado": "$176", "metodo": "Reducción de $11 desde $187" },
    "LTV": { "valor_proyectado": "$2,670", "metodo": "Incremento de $330 desde $2,340" },
    "Active_Users": { "valor_proyectado": 1935, "metodo": "Crecimiento del 15.3% sobre 1678" },
    "Support_Tickets": { "valor_proyectado": 52, "metodo": "Reducción del 17.1% sobre 63" },
    "Avg_Response_Time_h": { "valor_proyectado": 1.7, "metodo": "Reducción de 0.7 horas desde 2.4" }
  }
}
```