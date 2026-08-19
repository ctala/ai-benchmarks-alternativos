# Claude Haiku 4.5 — ocr_extraction/screenshot_table_extraction

- model_id: `anthropic/claude-haiku-4.5`
- success: True  | final: 8.71 | quality: 10.0
- latency_total: 6.965s | tokens_per_second: 199.7
- input_tokens: 430 | output_tokens: 1391
- judge_score: 3.6 | justificación: 

## Respuesta completa

```json
{
  "dashboard": {
    "periodo": "Marzo 2026",
    "metricas": [
      {
        "nombre": "MRR",
        "enero": "$45.2K",
        "febrero": "$48.7K",
        "marzo": "$52.1K",
        "variacion_m_m": "+7.0%"
      },
      {
        "nombre": "Churn Rate",
        "enero": "4.2%",
        "febrero": "3.8%",
        "marzo": "3.1%",
        "variacion_m_m": "-0.7pp"
      },
      {
        "nombre": "NPS",
        "enero": 42,
        "febrero": 45,
        "marzo": 51,
        "variacion_m_m": "+6"
      },
      {
        "nombre": "CAC",
        "enero": "$234",
        "febrero": "$198",
        "marzo": "$187",
        "variacion_m_m": "-$11"
      },
      {
        "nombre": "LTV",
        "enero": "$1,890",
        "febrero": "$2,010",
        "marzo": "$2,340",
        "variacion_m_m": "+$330"
      },
      {
        "nombre": "Active Users",
        "enero": 1234,
        "febrero": 1456,
        "marzo": 1678,
        "variacion_m_m": "+15.3%"
      },
      {
        "nombre": "Support Tickets",
        "enero": 89,
        "febrero": 76,
        "marzo": 63,
        "variacion_m_m": "-17.1%"
      },
      {
        "nombre": "Avg Response (h)",
        "enero": 4.2,
        "febrero": 3.1,
        "marzo": 2.4,
        "variacion_m_m": "-0.7"
      }
    ]
  },
  "analisis": {
    "ltv_cac_ratio": {
      "enero": {
        "valor": 8.08,
        "descripcion": "LTV/CAC = 1890/234"
      },
      "febrero": {
        "valor": 10.15,
        "descripcion": "LTV/CAC = 2010/198"
      },
      "marzo": {
        "valor": 12.51,
        "descripcion": "LTV/CAC = 2340/187"
      },
      "observacion": "Mejora consistente del ratio de rentabilidad"
    },
    "metrica_mayor_mejora": {
      "nombre": "Support Tickets",
      "mejora_porcentual": "-17.1%",
      "periodo": "Febrero a Marzo",
      "valor_inicial": 76,
      "valor_final": 63,
      "nota": "Mayor reducción en valor absoluto y porcentual"
    },
    "proyecciones_abril": {
      "metodo": "Extrapolación lineal de tendencias",
      "MRR": {
        "marzo": 52.1,
        "proyeccion_abril": "$55.8K",
        "crecimiento_estimado": "+7.0%"
      },
      "Churn_Rate": {
        "marzo": 3.1,
        "proyeccion_abril": "2.4%",
        "reduccion_estimada": "-0.7pp"
      },
      "NPS": {
        "marzo": 51,
        "proyeccion_abril": 57,
        "incremento_estimado": "+6"
      },
      "CAC": {
        "marzo": 187,
        "proyeccion_abril": "$176",
        "reduccion_estimada": "-$11"
      },
      "LTV": {
        "marzo": 2340,
        "proyeccion_abril": "$2,670",
        "incremento_estimado": "+$330"
      },
      "Active_Users": {
        "marzo": 1678,
        "proyeccion_abril": 1935,
        "crecimiento_estimado": "+15.3%"
      },
      "Support_Tickets": {
        "marzo": 63,
        "proyeccion_abril": 52,
        "reduccion_estimada": "-17.1%"
      },
      "Avg_Response_h": {
        "marzo": 2.4,
        "proyeccion_abril": 1.7,
        "mejora_estimada": "-0.7h"
      }
    }
  },
  "resumen_salud": {
    "tendencia_general": "↑ Positiva",
    "metricas_mejorando": 8,
    "metricas_empeorando": 0,
    "confianza_proyeccion": "Alta - todas las métricas muestran tendencias consistentes"
  }
}
```

**Conclusiones clave:**
- ✅ **LTV/CAC ratio mejoró 55%** (8.08 → 12.51): excelente salud de rentabilidad
- 📊 **Mayor mejora**: Support Tickets (-17.1%)
- 🎯 **Proyección Abril**: continuidad de tendencias positivas si se mantienen los patrones
- 💪 **Negocio saludable**: crecimiento en ingresos, reducción de costos y mejor experiencia