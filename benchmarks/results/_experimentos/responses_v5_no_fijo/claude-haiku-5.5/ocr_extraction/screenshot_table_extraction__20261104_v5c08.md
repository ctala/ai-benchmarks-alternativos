# Claude Haiku 5.5 — ocr_extraction/screenshot_table_extraction

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 9.17 | quality: 10.0
- latency_total: 5.209s | tokens_per_second: 246.5
- input_tokens: 512 | output_tokens: 1284

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
  "dashboard": "KPIs Marzo 2026",
  "datos": {
    "MRR": {
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "variacion_mes_a_mes": "+7.0%"
    },
    "churn_rate": {
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "variacion_mes_a_mes": "-0.7pp"
    },
    "NPS": {
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "variacion_mes_a_mes": "+6"
    },
    "CAC": {
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "variacion_mes_a_mes": "-11"
    },
    "LTV": {
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "variacion_mes_a_mes": "+330"
    },
    "active_users": {
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "variacion_mes_a_mes": "+15.3%"
    },
    "support_tickets": {
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "variacion_mes_a_mes": "-17.1%"
    },
    "avg_response_hours": {
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "variacion_mes_a_mes": "-0.7"
    }
  },
  "tendencia_general": "positiva en todas las metricas",
  "analisis": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51
    },
    "mayor_mejora_porcentual": {
      "metrica": "Support Tickets",
      "variacion": "-17.1%",
      "nota": "Considerando que una reduccion en tickets es una mejora. Entre las metricas donde un aumento es positivo, Active Users (+15.3%) es la de mayor mejora."
    }
  },
  "proyeccion_abril": {
    "supuesto": "Tasas de crecimiento mensual de marzo mantenidas (MRR +7.0%, Active Users +15.3%) y variaciones absolutas de marzo mantenidas para el resto",
    "valores": {
      "MRR": 55747,
      "churn_rate": 2.4,
      "NPS": 57,
      "CAC": 176,
      "LTV": 2670,
      "active_users": 1935,
      "support_tickets": 52,
      "avg_response_hours": 1.7
    }
  }
}
```

**Notas:**
- **LTV/CAC** = LTV / CAC. Enero: 1890/234 ≈ 8.08; Febrero: 2010/198 ≈ 10.15; Marzo: 2340/187 ≈ 12.51.
- **Mayor mejora porcentual:** Support Tickets (-17.1%) es la mayor variación en magnitud, pero al ser una reducción en un indicador donde menos es mejor, la mejora real es esa. Si se excluye, Active Users (+15.3%) es la mayor mejora en métricas donde subir es bueno.
- **Proyección:** Los valores de Abril son estimaciones lineales/exponenciales simples basadas en la tendencia de marzo; no consideran estacionalidad ni factores externos. Churn, CAC y tiempo de respuesta se proyectaron con sus variaciones absolutas, y NPS/LTV igual. Los valores decimales de churn y respuesta fueron redondeados.