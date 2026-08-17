# Gemini 3.1 Flash Lite — ocr_extraction/screenshot_table_extraction

- model_id: `google/gemini-3.1-flash-lite-preview`
- success: True  | final: 7.08 | quality: 7.24
- latency_total: 3.139s | tokens_per_second: 262.5
- input_tokens: 419 | output_tokens: 824
- judge_score: 3.8 | justificación: 

## Respuesta completa

Aquí tienes el análisis solicitado en formato JSON.

Para la proyección de abril, se ha calculado utilizando la **tasa de crecimiento promedio (CAGR mensual)** observada en el trimestre para métricas de crecimiento, y la **variación absoluta promedio** para métricas de eficiencia y soporte.

```json
{
  "dashboard_data": {
    "periodo": "Marzo 2026",
    "metricas": {
      "enero": {
        "mrr": 45200,
        "churn_rate": 0.042,
        "nps": 42,
        "cac": 234,
        "ltv": 1890,
        "active_users": 1234,
        "support_tickets": 89,
        "avg_response_h": 4.2
      },
      "febrero": {
        "mrr": 48700,
        "churn_rate": 0.038,
        "nps": 45,
        "cac": 198,
        "ltv": 2010,
        "active_users": 1456,
        "support_tickets": 76,
        "avg_response_h": 3.1
      },
      "marzo": {
        "mrr": 52100,
        "churn_rate": 0.031,
        "nps": 51,
        "cac": 187,
        "ltv": 2340,
        "active_users": 1678,
        "support_tickets": 63,
        "avg_response_h": 2.4
      }
    },
    "analisis": {
      "ltv_cac_ratio": {
        "enero": 8.08,
        "febrero": 10.15,
        "marzo": 12.51
      },
      "metrica_mayor_mejora_porcentual": {
        "nombre": "Support Tickets",
        "mejora_marzo_vs_feb": "-17.1%"
      },
      "proyeccion_abril_estimada": {
        "mrr": 55747,
        "churn_rate": 0.024,
        "nps": 54,
        "cac": 176,
        "ltv": 2570,
        "active_users": 1935,
        "support_tickets": 50,
        "avg_response_h": 1.7
      }
    }
  }
}
```

### Notas sobre el cálculo:
1.  **LTV/CAC Ratio:** Se observa una mejora constante en la eficiencia del capital, pasando de 8.08x en enero a 12.51x en marzo.
2.  **Mayor mejora:** Aunque el NPS y el LTV tienen crecimientos porcentuales altos, la reducción de **Support Tickets (-17.1%)** representa la optimización operativa más agresiva del periodo.
3.  **Proyección Abril:**
    *   Para métricas de crecimiento (MRR, Usuarios), se aplicó el crecimiento promedio mensual del periodo (~7% para MRR, ~15% para Usuarios).
    *   Para métricas de reducción (Churn, CAC, Tickets, Response Time), se proyectó manteniendo la tendencia de reducción constante observada en los últimos dos meses.