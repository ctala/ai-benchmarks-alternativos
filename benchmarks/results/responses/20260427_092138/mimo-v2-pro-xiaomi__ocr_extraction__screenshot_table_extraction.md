# MiMo V2-Pro (Xiaomi direct) — ocr_extraction/screenshot_table_extraction

- model_id: `mimo-v2-pro`
- success: True  | final: 7.08 | quality: 7.08
- latency_total: 32.38s | tokens_per_second: 61.2
- input_tokens: 665 | output_tokens: 1982
- judge_score: 3.8 | justificación: 

## Respuesta completa

```json
{
  "dashboard": {
    "titulo": "KPIs Marzo 2026",
    "tendencia_general": "Positiva en todas las métricas"
  },

  "datos_mensuales": {
    "enero": {
      "mrr": 45200,
      "churn_rate": 4.2,
      "nps": 42,
      "cac": 234,
      "ltv": 1890,
      "active_users": 1234,
      "support_tickets": 89,
      "avg_response_hours": 4.2
    },
    "febrero": {
      "mrr": 48700,
      "churn_rate": 3.8,
      "nps": 45,
      "cac": 198,
      "ltv": 2010,
      "active_users": 1456,
      "support_tickets": 76,
      "avg_response_hours": 3.1
    },
    "marzo": {
      "mrr": 52100,
      "churn_rate": 3.1,
      "nps": 51,
      "cac": 187,
      "ltv": 2340,
      "active_users": 1678,
      "support_tickets": 63,
      "avg_response_hours": 2.4
    }
  },

  "ltv_cac_ratio": {
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51,
    "interpretacion": "Ratio saludable >3. En marzo, cada $1 invertido en CAC genera $12.51 de LTV"
  },

  "metrica_mayor_mejora": {
    "metrica": "Tiempo de Respuesta Promedio",
    "mejora_porcentual": "42.9%",
    "detalle": {
      "valor_enero": 4.2,
      "valor_marzo": 2.4,
      "reduccion": 1.8
    },
    "ranking_mejoras": [
      {"metrica": "Avg Response Time", "mejora": "42.9%"},
      {"metrica": "Active Users", "mejora": "36.0%"},
      {"metrica": "Support Tickets", "mejora": "29.2%"},
      {"metrica": "Churn Rate", "mejora": "26.2%"},
      {"metrica": "LTV", "mejora": "23.8%"}
    ]
  },

  "proyeccion_abril": {
    "metodo": "Promedio de variación mensual (Ene-Mar)",
    "valores": {
      "mrr": 55900,
      "churn_rate": 2.6,
      "nps": 56,
      "cac": 172,
      "ltv": 2690,
      "active_users": 1956,
      "support_tickets": 53,
      "avg_response_hours": 1.7
    },
    "ltv_cac_ratio_proyectado": 15.64
  },

  "resumen_ejecutivo": "El negocio muestra una curva de crecimiento sólida. El LTV/CAC de 12.51 indica excelente retorno de inversión. La reducción del 42.9% en tiempo de respuesta sugiere optimización operativa significativa. Proyección abril: MRR ~$56K con ratio LTV/CAC ~15.6."
}
```

**Notas sobre la proyección:**
- Se usó el promedio de las variaciones mes a mes
- El Churn Rate proyectado de 2.6% es muy optimista; en la práctica tendría un piso mínimo
- El ratio LTV/CAC de 15.6 proyectado es excepcional — monitorear si es sostenible 📈