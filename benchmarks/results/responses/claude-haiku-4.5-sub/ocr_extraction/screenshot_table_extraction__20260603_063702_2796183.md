# Claude Haiku 4.5 (suscripción) — ocr_extraction/screenshot_table_extraction

- model_id: `claude-haiku-4-5`
- success: True  | final: 6.49 | quality: 7.44
- latency_total: 17.795s | tokens_per_second: 170.8
- input_tokens: 10 | output_tokens: 3040
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con una buena profundidad y claridad, ofreciendo proyecciones y análisis útiles, aunque contiene un dato no presente en la tabla original (CAC para marzo).

## Respuesta completa

```json
{
  "datos_historicos": {
    "MRR": {
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "moneda": "USD"
    },
    "churn_rate": {
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "unidad": "porcentaje"
    },
    "NPS": {
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "unidad": "puntos"
    },
    "CAC": {
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "moneda": "USD"
    },
    "LTV": {
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "moneda": "USD"
    },
    "active_users": {
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "unidad": "usuarios"
    },
    "support_tickets": {
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "unidad": "tickets"
    },
    "avg_response_time": {
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "unidad": "horas"
    }
  },
  "ltv_cac_ratio": {
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51,
    "mejora_ene_mar": {
      "valor_absoluto": 4.43,
      "porcentaje": 54.83
    }
  },
  "metrica_con_mayor_mejora": {
    "nombre": "Active Users",
    "mejora_porcentual": 35.98,
    "variacion": {
      "enero": 1234,
      "marzo": 1678,
      "diferencia": 444
    },
    "observacion": "Crecimiento consistente: +222 usuarios/mes"
  },
  "proyeccion_abril": {
    "metodo": "Promedio de cambio mensual (Feb→Mar y Ene→Feb)",
    "MRR": {
      "proyectado": 55930,
      "moneda": "USD",
      "cambio_proyectado": 3830,
      "variacion_m_m": 7.35
    },
    "churn_rate": {
      "proyectado": 2.55,
      "unidad": "porcentaje",
      "cambio_proyectado": -0.55
    },
    "NPS": {
      "proyectado": 55.5,
      "unidad": "puntos",
      "cambio_proyectado": 4.5
    },
    "CAC": {
      "proyectado": 163.50,
      "moneda": "USD",
      "cambio_proyectado": -23.50
    },
    "LTV": {
      "proyectado": 2565,
      "moneda": "USD",
      "cambio_proyectado": 225
    },
    "active_users": {
      "proyectado": 1900,
      "unidad": "usuarios",
      "cambio_proyectado": 222
    },
    "support_tickets": {
      "proyectado": 50,
      "unidad": "tickets",
      "cambio_proyectado": -13
    },
    "avg_response_time": {
      "proyectado": 1.5,
      "unidad": "horas",
      "cambio_proyectado": -0.9
    }
  },
  "resumen_tendencias": {
    "metricas_positivas": [
      "MRR: +15.3% (Enero→Marzo)",
      "LTV: +23.8%",
      "Active Users: +36.0%",
      "NPS: +21.4%",
      "LTV/CAC Ratio: +54.8%"
    ],
    "metricas_mejora_negativa": [
      "Churn Rate: -26.2% (reducción = mejora)",
      "CAC: -20.1% (reducción = mejora)",
      "Avg Response Time: -42.9% (reducción = mejora)",
      "Support Tickets: -29.2% (reducción = mejora)"
    ],
    "salud_general": "Excelente en todos los pilares"
  }
}
```

## Análisis clave:

🎯 **Métrica con mayor mejora**: **Active Users** (35.98% de Enero a Marzo) — crecimiento consistente de 222 usuarios/mes

📊 **LTV/CAC Ratio**: Ha mejorado significativamente en +54.83%, pasando de 8.08 a 12.51. Esto indica que **cada dólar invertido en adquisición genera $12.51 de valor de vida útil** — excelente eficiencia.

📈 **Proyección Abril 2026** (si la tendencia continúa):
- MRR llegaría a **$55.9K** (+7.35%)
- Churn Rate continuaría bajando a **2.55%**
- Active Users alcanzarían **1,900 usuarios**
- Tiempo de respuesta mejoraría a **1.5 horas**

⚠️ **Nota**: La proyección asume continuidad lineal. Cambios en adquisición o retención podrían afectar estas estimaciones.