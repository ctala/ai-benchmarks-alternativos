# Claude Opus 4.8 (suscripción) — ocr_extraction/screenshot_table_extraction

- model_id: `claude-opus-4-8`
- success: True  | final: 5.69 | quality: 7.08
- latency_total: 41.861s | tokens_per_second: 78.2
- input_tokens: 2028 | output_tokens: 3275
- judge_score: 3.8 | justificación: 

## Respuesta completa

No necesito el tool, ya tengo los cálculos. Aquí está el resultado:

```json
{
  "dashboard": {
    "titulo": "KPIs Marzo 2026",
    "metricas": {
      "MRR": { "enero": 45200, "febrero": 48700, "marzo": 52100, "var_mom_pct": 7.0, "unidad": "USD" },
      "churn_rate": { "enero": 4.2, "febrero": 3.8, "marzo": 3.1, "var_mom_pp": -0.7, "unidad": "%" },
      "NPS": { "enero": 42, "febrero": 45, "marzo": 51, "var_mom": 6, "unidad": "puntos" },
      "CAC": { "enero": 234, "febrero": 198, "marzo": 187, "var_mom_usd": -11, "unidad": "USD" },
      "LTV": { "enero": 1890, "febrero": 2010, "marzo": 2340, "var_mom_usd": 330, "unidad": "USD" },
      "active_users": { "enero": 1234, "febrero": 1456, "marzo": 1678, "var_mom_pct": 15.3, "unidad": "usuarios" },
      "support_tickets": { "enero": 89, "febrero": 76, "marzo": 63, "var_mom_pct": -17.1, "unidad": "tickets" },
      "avg_response_h": { "enero": 4.2, "febrero": 3.1, "marzo": 2.4, "var_mom_h": -0.7, "unidad": "horas" }
    }
  },

  "1_ltv_cac_ratio": {
    "enero":  { "calculo": "1890 / 234", "ratio": 8.08 },
    "febrero":{ "calculo": "2010 / 198", "ratio": 10.15 },
    "marzo":  { "calculo": "2340 / 187", "ratio": 12.51 },
    "interpretacion": "Mejora sostenida y saludable. Un ratio >3 ya se considera bueno; 12.5x indica una economía unitaria excelente (posiblemente sub-inversión en adquisición — hay espacio para gastar más en CAC y acelerar crecimiento)."
  },

  "2_mayor_mejora_porcentual": {
    "metrica_ganadora": "Avg Response Time",
    "mejora_pct": -22.6,
    "detalle": "De 3.1h a 2.4h (Mar vs Feb)",
    "ranking_mar_vs_feb": [
      { "metrica": "Avg Response (h)", "cambio_pct": -22.6, "direccion": "mejora" },
      { "metrica": "Churn Rate",       "cambio_pct": -18.4, "direccion": "mejora" },
      { "metrica": "Support Tickets",  "cambio_pct": -17.1, "direccion": "mejora" },
      { "metrica": "LTV",              "cambio_pct": 16.4,  "direccion": "mejora" },
      { "metrica": "Active Users",     "cambio_pct": 15.3,  "direccion": "mejora" },
      { "metrica": "NPS",              "cambio_pct": 13.3,  "direccion": "mejora" },
      { "metrica": "MRR",              "cambio_pct": 7.0,   "direccion": "mejora" },
      { "metrica": "CAC",              "cambio_pct": -5.6,  "direccion": "mejora" }
    ],
    "nota": "Se midió la magnitud del cambio porcentual M/M (Mar vs Feb). El churn y avg-response se cuentan como mejora porque bajar es positivo. Si se considera la métrica derivada LTV/CAC, esta subió +23.3% (la mayor de todas)."
  },

  "3_proyeccion_abril": {
    "metodo": "Extrapolación de la tasa de cambio M/M observada en Marzo (aditiva para pp/puntos/$, multiplicativa para %).",
    "valores": {
      "MRR":             { "proyectado": 55750, "regla": "+7.0%",  "unidad": "USD" },
      "churn_rate":      { "proyectado": 2.4,   "regla": "-0.7pp", "unidad": "%" },
      "NPS":             { "proyectado": 57,    "regla": "+6",     "unidad": "puntos" },
      "CAC":             { "proyectado": 176,   "regla": "-$11",   "unidad": "USD" },
      "LTV":             { "proyectado": 2670,  "regla": "+$330",  "unidad": "USD" },
      "active_users":    { "proyectado": 1935,  "regla": "+15.3%", "unidad": "usuarios" },
      "support_tickets": { "proyectado": 52,    "regla": "-17.1%", "unidad": "tickets" },
      "avg_response_h":  { "proyectado": 1.7,   "regla": "-0.7h",  "unidad": "horas" },
      "ltv_cac_ratio":   { "proyectado": 15.17, "calculo": "2670 / 176" }
    },
    "advertencia": "Proyección lineal simple basada en 1 mes de variación. Métricas como churn, avg-response y tickets tienen piso natural (no bajan indefinidamente); esperar saturación. Útil como referencia, no como forecast robusto — para eso se necesitarían más periodos y estacionalidad."
  }
}
```

**Resumen rápido:** la economía unitaria (LTV/CAC) pasó de 8.1x a 12.5x — excelente. La métrica de mayor mejora % fue el **tiempo de respuesta** (-22.6%), aunque churn, tickets y LTV están muy cerca. Las proyecciones de Abril asumen continuidad lineal de la tendencia; ojo con los pisos naturales en churn y tiempos de respuesta.