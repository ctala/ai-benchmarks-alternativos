# Claude Fable 5 (suscripción) — ocr_extraction/screenshot_table_extraction

- model_id: `claude-fable-5`
- success: True  | final: 3.87 | quality: 4.4
- latency_total: 30.678s | tokens_per_second: 84.6
- input_tokens: 2 | output_tokens: 2594

## Respuesta completa

```json
{
  "dashboard": {
    "titulo": "KPIs Marzo 2026",
    "tendencia_general": "positiva",
    "metricas": [
      { "metrica": "MRR", "enero": 45200, "febrero": 48700, "marzo": 52100, "var_mm": "+7.0%", "unidad": "USD" },
      { "metrica": "Churn Rate", "enero": 4.2, "febrero": 3.8, "marzo": 3.1, "var_mm": "-0.7pp", "unidad": "%" },
      { "metrica": "NPS", "enero": 42, "febrero": 45, "marzo": 51, "var_mm": "+6", "unidad": "puntos" },
      { "metrica": "CAC", "enero": 234, "febrero": 198, "marzo": 187, "var_mm": "-$11", "unidad": "USD" },
      { "metrica": "LTV", "enero": 1890, "febrero": 2010, "marzo": 2340, "var_mm": "+$330", "unidad": "USD" },
      { "metrica": "Active Users", "enero": 1234, "febrero": 1456, "marzo": 1678, "var_mm": "+15.3%", "unidad": "usuarios" },
      { "metrica": "Support Tickets", "enero": 89, "febrero": 76, "marzo": 63, "var_mm": "-17.1%", "unidad": "tickets" },
      { "metrica": "Avg Response Time", "enero": 4.2, "febrero": 3.1, "marzo": 2.4, "var_mm": "-0.7h", "unidad": "horas" }
    ]
  },

  "analisis": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "nota": "Benchmark saludable SaaS es >3. Un ratio de 12.5 es excelente, pero también puede indicar sub-inversión en adquisición: hay espacio para subir gasto en growth manteniendo unit economics sanas."
    },

    "mayor_mejora_porcentual_feb_marzo": {
      "metrica": "Avg Response Time",
      "mejora_pct": -22.6,
      "detalle": "De 3.1h a 2.4h. Le siguen Churn Rate (-18.4%), Support Tickets (-17.1%) y LTV (+16.4%).",
      "ranking_mejoras": [
        { "metrica": "Avg Response Time", "mejora": "22.6%" },
        { "metrica": "Churn Rate", "mejora": "18.4%" },
        { "metrica": "Support Tickets", "mejora": "17.1%" },
        { "metrica": "LTV", "mejora": "16.4%" },
        { "metrica": "Active Users", "mejora": "15.3%" },
        { "metrica": "NPS", "mejora": "13.3%" },
        { "metrica": "MRR", "mejora": "7.0%" },
        { "metrica": "CAC", "mejora": "5.6%" }
      ]
    },

    "proyeccion_abril_2026": {
      "metodo": "Extrapolación lineal de la variación Feb→Marzo (último período). No es un forecast estadístico — con solo 3 puntos de data, tomar como estimación direccional.",
      "valores": {
        "mrr": { "proyectado": 55750, "supuesto": "+7.0% M/M" },
        "churn_rate": { "proyectado": 2.5, "supuesto": "-18.4% relativo (≈ -0.6pp)" },
        "nps": { "proyectado": 57, "supuesto": "+6 puntos" },
        "cac": { "proyectado": 176, "supuesto": "-$11" },
        "ltv": { "proyectado": 2670, "supuesto": "+$330" },
        "active_users": { "proyectado": 1935, "supuesto": "+15.3%" },
        "support_tickets": { "proyectado": 52, "supuesto": "-17.1%" },
        "avg_response_h": { "proyectado": 1.7, "supuesto": "-0.7h" }
      },
      "ltv_cac_proyectado": 15.17,
      "advertencias": [
        "Churn, tickets y response time tienen piso natural — la mejora lineal no se sostiene indefinidamente.",
        "La caída de tickets junto al alza de usuarios activos (+36% acumulado Ene→Mar) sugiere mejora real de producto u onboarding, no solo soporte más rápido."
      ]
    }
  }
}
```

Un dato a verificar en tu fuente: el dashboard marca "Avg Response Var M/M: -0.7" — es correcto en horas absolutas, pero en términos porcentuales es la mejora más grande del trimestre (-22.6%), no la menor como podría parecer a simple vista.