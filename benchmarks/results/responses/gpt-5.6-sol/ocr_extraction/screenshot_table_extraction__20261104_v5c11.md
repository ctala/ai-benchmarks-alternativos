# GPT-5.6 Sol — ocr_extraction/screenshot_table_extraction

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 7.43 | quality: 8.0
- latency_total: 4.364s | tokens_per_second: 178.3
- input_tokens: 379 | output_tokens: 778

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

{
  "dashboard": {
    "titulo": "KPIs Marzo 2026",
    "tendencia_general": "positiva",
    "datos": {
      "enero": {
        "MRR_USD": 45200,
        "churn_rate_pct": 4.2,
        "NPS": 42,
        "CAC_USD": 234,
        "LTV_USD": 1890,
        "active_users": 1234,
        "support_tickets": 89,
        "avg_response_hours": 4.2
      },
      "febrero": {
        "MRR_USD": 48700,
        "churn_rate_pct": 3.8,
        "NPS": 45,
        "CAC_USD": 198,
        "LTV_USD": 2010,
        "active_users": 1456,
        "support_tickets": 76,
        "avg_response_hours": 3.1
      },
      "marzo": {
        "MRR_USD": 52100,
        "churn_rate_pct": 3.1,
        "NPS": 51,
        "CAC_USD": 187,
        "LTV_USD": 2340,
        "active_users": 1678,
        "support_tickets": 63,
        "avg_response_hours": 2.4
      }
    },
    "variacion_marzo_vs_febrero": {
      "MRR": {
        "valor": 7.0,
        "unidad": "porcentaje"
      },
      "churn_rate": {
        "valor": -0.7,
        "unidad": "puntos_porcentuales"
      },
      "NPS": {
        "valor": 6,
        "unidad": "puntos"
      },
      "CAC": {
        "valor": -11,
        "unidad": "USD"
      },
      "LTV": {
        "valor": 330,
        "unidad": "USD"
      },
      "active_users": {
        "valor": 15.3,
        "unidad": "porcentaje"
      },
      "support_tickets": {
        "valor": -17.1,
        "unidad": "porcentaje"
      },
      "avg_response": {
        "valor": -0.7,
        "unidad": "horas"
      }
    },
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51
    },
    "mayor_mejora_porcentual": {
      "metrica": "avg_response_hours",
      "variacion_pct_febrero_a_marzo": -22.58,
      "mejora_pct": 22.58,
      "criterio": "Mayor mejora relativa; una reducción del tiempo de respuesta se considera positiva"
    },
    "proyeccion_abril": {
      "metodo": "Se mantiene la variación relativa observada entre febrero y marzo para cada métrica",
      "valores": {
        "MRR_USD": 55743,
        "churn_rate_pct": 2.57,
        "NPS": 57.8,
        "CAC_USD": 176.61,
        "LTV_USD": 2724.18,
        "active_users": 1933.85,
        "support_tickets": 52.22,
        "avg_response_hours": 1.86
      },
      "ltv_cac_ratio_estimado": 15.42
    }
  }
}