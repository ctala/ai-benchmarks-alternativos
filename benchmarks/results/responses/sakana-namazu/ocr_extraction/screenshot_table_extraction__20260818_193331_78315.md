# Sakana Namazu — ocr_extraction/screenshot_table_extraction

- model_id: `sakana/sakana-namazu`
- success: True  | final: 6.96 | quality: 8.0
- latency_total: 25.52s | tokens_per_second: 294.6
- input_tokens: 461 | output_tokens: 7519

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
    "dashboard": "DASHBOARD - KPIs Marzo 2026",
    "tendencia_general": "↑ Positiva en todas las metricas",
    "metricas": [
      { "nombre": "MRR", "unidad": "USD", "enero": 45200, "febrero": 48700, "marzo": 52100, "variacion_m_m": "+7.0%" },
      { "nombre": "Churn Rate", "unidad": "%", "enero": 4.2, "febrero": 3.8, "marzo": 3.1, "variacion_m_m": "-0.7pp" },
      { "nombre": "NPS", "unidad": "puntos", "enero": 42, "febrero": 45, "marzo": 51, "variacion_m_m": "+6" },
      { "nombre": "CAC", "unidad": "USD", "enero": 234, "febrero": 198, "marzo": 187, "variacion_m_m": "-$11" },
      { "nombre": "LTV", "unidad": "USD", "enero": 1890, "febrero": 2010, "marzo": 2340, "variacion_m_m": "+$330" },
      { "nombre": "Active Users", "unidad": "usuarios", "enero": 1234, "febrero": 1456, "marzo": 1678, "variacion_m_m": "+15.3%" },
      { "nombre": "Support Tickets", "unidad": "tickets", "enero": 89, "febrero": 76, "marzo": 63, "variacion_m_m": "-17.1%" },
      { "nombre": "Avg Response (h)", "unidad": "horas", "enero": 4.2, "febrero": 3.1, "marzo": 2.4, "variacion_m_m": "-0.7" }
    ]
  },
  "ltv_cac_ratio": {
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51,
    "comentario": "La relacion LTV/CAC mejoró de ~8x en enero a ~12.5x en marzo, indicando mayor eficiencia en la adquisicion de clientes."
  },
  "metrica_mayor_mejora_porcentual": {
    "metrica": "Avg Response (h)",
    "valor_febrero": 3.1,
    "valor_marzo": 2.4,
    "reduccion_absoluta": 0.7,
    "mejora_porcentual": "22.58%",
    "contexto": "Es la mayor mejora relativa del periodo. Al ser una metrica donde menor es mejor, la reducción del 22.6% destaca sobre las demas."
  },
  "proyeccion_abril_2026": {
    "metodologia": "Se aplica la variación mes/marzo-sobre-febrero (Var M/M) sobre los valores de marzo para estimar abril. Para métricas con variación en porcentaje (MRR, Active Users, Support Tickets) se aplica el factor multiplicativo. Para métricas con variación absoluta o en puntos porcentuales (Churn, NPS, CAC, LTV, Avg Response) se proyecta con la misma diferencia lineal.",
    "valores_proyectados": {
      "MRR": { "valor": 55747, " etiqueta": "$55.7K" },
      "Churn Rate": { "valor": 2.4, "unidad": "%" },
      "NPS": { "valor": 57, "unidad": "puntos" },
      "CAC": { "valor": 176, "unidad": "USD" },
      "LTV": { "valor": 2670, "unidad": "USD" },
      "Active Users": { "valor": 1935, "unidad": "usuarios" },
      "Support Tickets": { "valor": 52, "unidad": "tickets" },
      "Avg Response (h)": { "valor": 1.7, "unidad": "horas" }
    }
  }
}
```