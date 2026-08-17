# MiMo-V2-Pro — ocr_extraction/screenshot_table_extraction

- model_id: `xiaomi/mimo-v2-pro`
- success: True  | final: 6.51 | quality: 7.16
- latency_total: 22.993s | tokens_per_second: 68.8
- input_tokens: 665 | output_tokens: 1581
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
      "MRR": 45200,
      "churn_rate": 4.2,
      "NPS": 42,
      "CAC": 234,
      "LTV": 1890,
      "active_users": 1234,
      "support_tickets": 89,
      "avg_response_hours": 4.2
    },
    "febrero": {
      "MRR": 48700,
      "churn_rate": 3.8,
      "NPS": 45,
      "CAC": 198,
      "LTV": 2010,
      "active_users": 1456,
      "support_tickets": 76,
      "avg_response_hours": 3.1
    },
    "marzo": {
      "MRR": 52100,
      "churn_rate": 3.1,
      "NPS": 51,
      "CAC": 187,
      "LTV": 2340,
      "active_users": 1678,
      "support_tickets": 63,
      "avg_response_hours": 2.4
    }
  },

  "ltv_cac_ratio": {
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51,
    "nota": "Ratio ideal > 3.0; crecimiento muy saludable"
  },

  "metrica_mayor_mejora_porcentual": {
    "metrica": "Support Tickets",
    "mejora_M_M": "-17.1%",
    "contexto": "Mayor reducción porcentual mes a mes (de 76 → 63 tickets). Indica mejora significativa en calidad del producto o soporte proactivo."
  },

  "proyeccion_abril": {
    "metodo": "Tendencia lineal (promedio de cambio absoluto mensual Ene-Mar)",
    "valores": {
      "MRR":              { "valor": 55567,  "cambio": "+$3,467/mes" },
      "churn_rate":       { "valor": 2.53,   "cambio": "-0.57pp/mes" },
      "NPS":              { "valor": 56,     "cambio": "+4.5 pts/mes" },
      "CAC":              { "valor": 174,    "cambio": "-$13.33/mes" },
      "LTV":              { "valor": 2620,   "cambio": "+$245/mes" },
      "active_users":     { "valor": 1900,   "cambio": "+222/mes" },
      "support_tickets":  { "valor": 49,     "cambio": "-13/mes" },
      "avg_response_hours": { "valor": 1.77, "cambio": "-0.63h/mes" }
    },
    "ltv_cac_proyectado": 15.06,
    "advertencia": "Proyección lineal simplificada. El churn no puede bajar de 0% ni el CAC de $0; valores extremos requieren modelos logísticos para mayor precisión."
  }
}
```

### Resumen rápido

| Insight | Detalle |
|---|---|
| **LTV/CAC Marzo** | **12.51** → Excelente (el estándar saludable es >3) |
| **Mayor mejora** | **Support Tickets** (−17.1% M/M) |
| **Proyección Abril** | MRR ~$55.6K, Churn ~2.5%, NPS ~56, CAC ~$174 |

> ⚠️ **Nota sobre las proyecciones:** usé tendencia lineal (promedio de cambios absolutos). En la práctica, métricas como el churn tienen un piso en 0% y el CAC un costo mínimo real, así que eventualmente la curva se aplanaría. Para proyecciones más robustas convendría un modelo logístico o exponencial con límites.