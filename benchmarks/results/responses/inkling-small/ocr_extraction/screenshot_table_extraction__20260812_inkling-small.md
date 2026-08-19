# Inkling Small — ocr_extraction/screenshot_table_extraction

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 6.88 | quality: 8.0
- latency_total: 171.311s | tokens_per_second: 46.6
- input_tokens: 388 | output_tokens: 7976

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
  "dashboard": "DASHBOARD - KPIs Marzo 2026",
  "datos_extraidos": {
    "metricas": [
      { "nombre": "MRR", "enero": 45200, "febrero": 48700, "marzo": 52100, "var_m_m_texto": "+7.0%", "unidad": "USD", "tipo": "moneda" },
      { "nombre": "Churn Rate", "enero": 4.2, "febrero": 3.8, "marzo": 3.1, "var_m_m_texto": "-0.7pp", "unidad": "%", "tipo": "tasa" },
      { "nombre": "NPS", "enero": 42, "febrero": 45, "marzo": 51, "var_m_m_texto": "+6", "unidad": "pts", "tipo": "puntaje" },
      { "nombre": "CAC", "enero": 234, "febrero": 198, "marzo": 187, "var_m_m_texto": "-$11", "unidad": "USD", "tipo": "moneda" },
      { "nombre": "LTV", "enero": 1890, "febrero": 2010, "marzo": 2340, "var_m_m_texto": "+$330", "unidad": "USD", "tipo": "moneda" },
      { "nombre": "Active Users", "enero": 1234, "febrero": 1456, "marzo": 1678, "var_m_m_texto": "+15.3%", "unidad": "users", "tipo": "conteo" },
      { "nombre": "Support Tickets", "enero": 89, "febrero": 76, "marzo": 63, "var_m_m_texto": "-17.1%", "unidad": "tickets", "tipo": "conteo" },
      { "nombre": "Avg Response (h)", "enero": 4.2, "febrero": 3.1, "marzo": 2.4, "var_m_m_texto": "-0.7", "unidad": "h", "tipo": "tiempo" }
    ]
  },
  "calculos": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "detalle": "LTV / CAC. Crece de 8.1x a 12.5x en el trimestre (+55%), mejorando la eficiencia unitaria y el payback."
    },
    "variacion_porcentual_m_m": {
      "MRR": "+6.98%",
      "Churn Rate": "-18.42%",
      "NPS": "+13.33%",
      "CAC": "-5.56%",
      "LTV": "+16.42%",
      "Active Users": "+15.25%",
      "Support Tickets": "-17.11%",
      "Avg Response (h)": "-22.58%"
    },
    "metrica_mayor_mejora_porcentual": {
      "metrica": "Avg Response (h)",
      "cambio_relativo": "-22.58%",
      "interpretacion": "Mayor reduccion relativa mes a mes (de 3.1h a 2.4h). Si se evalua solo crecimiento positivo, lidera LTV con +16.42% y Active Users con +15.25%."
    }
  },
  "proyeccion_abril": {
    "metodo": "Extrapolacion de la tendencia M/M (Marzo vs Febrero). Se aplica tasa relativa para variables porcentuales y diferencia absoluta para puntos/valores fijos.",
    "valores_proyectados": {
      "MRR_USD": 55700,
      "Churn_Rate_pct": 2.4,
      "NPS": 57,
      "CAC_USD": 176,
      "LTV_USD": 2670,
      "Active_Users": 1934,
      "Support_Tickets": 52,
      "Avg_Response_h": 1.7
    },
    "notas_calculo": [
      "MRR: $52.1K * 1.07 = ~$55.7K",
      "Churn: 3.1pp - 0.7pp = 2.4%",
      "NPS: 51 + 6 = 57 pts",
      "CAC: $187 - $11 = $176",
      "LTV: $2,340 + $330 = $2,670",
      "Active Users: 1,678 * 1.153 = ~1,934",
      "Support Tickets: 63 * 0.829 = ~52",
      "Avg Response: 2.4h - 0.7h = 1.7h"
    ]
  },
  "resumen": "Todas las metricas muestran tendencia positiva. El LTV/CAC paso de 8.1x a 12.5x. La mayor ganancia relativa es en tiempo de respuesta (-22.6%). Proyectando abril con la misma inercia, se espera MRR ~$55.7K, Churn ~2.4%, LTV ~$2.67K y Active Users ~1,934."
}
```