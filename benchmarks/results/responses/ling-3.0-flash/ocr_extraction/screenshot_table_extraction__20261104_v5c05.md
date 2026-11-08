# Ling 3.0 Flash — ocr_extraction/screenshot_table_extraction

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 7.92 | quality: 8.0
- latency_total: 10.184s | tokens_per_second: 148.0
- input_tokens: 457 | output_tokens: 1507

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
  "dashboard": "DASHBOARD - KPIs Marzo 2026",
  "datos_crudos": {
    "metricas": [
      { "metrica": "MRR", "Enero": "$45.2K", "Feb": "$48.7K", "Marzo": "$52.1K", "Var M/M": "+7.0%" },
      { "metrica": "Churn Rate", "Enero": "4.2%", "Feb": "3.8%", "Marzo": "3.1%", "Var M/M": "-0.7pp" },
      { "metrica": "NPS", "Enero": "42", "Feb": "45", "Marzo": "51", "Var M/M": "+6" },
      { "metrica": "CAC", "Enero": "$234", "Feb": "$198", "Marzo": "$187", "Var M/M": "-$11" },
      { "metrica": "LTV", "Enero": "$1,890", "Feb": "$2,010", "Marzo": "$2,340", "Var M/M": "+$330" },
      { "metrica": "Active Users", "Enero": "1,234", "Feb": "1,456", "Marzo": "1,678", "Var M/M": "+15.3%" },
      { "metrica": "Support Tickets", "Enero": "89", "Feb": "76", "Marzo": "63", "Var M/M": "-17.1%" },
      { "metrica": "Avg Response (h)", "Enero": "4.2", "Feb": "3.1", "Marzo": "2.4", "Var M/M": "-0.7" }
    ]
  },
  "analisis": {
    "ltv_cac_ratio": {
      "descripcion": "Ratio LTV/CAC por mes (indicador de eficiencia de inversión en adquisición)",
      "Enero": { "LTV": 1890, "CAC": 234, "ratio": 8.08 },
      "Feb": { "LTV": 2010, "CAC": 198, "ratio": 10.15 },
      "Marzo": { "LTV": 2340, "CAC": 187, "ratio": 12.51 }
    },
    "mejora_porcentual_mayor": {
      "metrica": "Active Users",
      "variacion_m_m": "+15.3%",
      "justificacion": "Active Users muestra el mayor crecimiento porcentual mes a mes (+15.3%). Los demás incrementos porcentuales son: MRR +7.0%. Las métricas de Churn Rate, Support Tickets y Avg Response son negativas (mejoran al bajar, pero en términos de variación porcentual positiva, Active Users lidera)."
    },
    "proyeccion_abril": {
      "descripcion": "Proyección basada en la tendencia de crecimiento promedio de los últimos 3 meses (enero-marzo)",
      "metodos": {
        "MRR": {
          "metodo": "Crecimiento promedio M/M: (7.0% + 7.4% + 7.0%) / 3 ≈ 7.13%",
          "proyeccion": "$55.8K"
        },
        "Churn Rate": {
          "metodo": "Reducción promedio: (-0.4pp, -0.7pp, -0.7pp) / 3 ≈ -0.6pp",
          "proyeccion": "2.5%"
        },
        "NPS": {
          "metodo": "Incremento promedio: (+3, +6, +6) / 3 ≈ +5",
          "proyeccion": "56"
        },
        "CAC": {
          "metodo": "Reducción promedio: (-$36, -$11, -$11) / 3 ≈ -$19",
          "proyeccion": "$168"
        },
        "LTV": {
          "metodo": "Incremento promedio: (+$120, +$130, +$330) / 3 ≈ +$193",
          "proyeccion": "$2,533"
        },
        "Active Users": {
          "metodo": "Crecimiento promedio M/M: (18.2% + 17.3% + 15.3%) / 3 ≈ 16.9%",
          "proyeccion": "1,962"
        },
        "Support Tickets": {
          "metodo": "Reducción promedio: (-14.6%, -14.5%, -17.1%) / 3 ≈ -15.4%",
          "proyeccion": "53"
        },
        "Avg Response (h)": {
          "metodo": "Reducción promedio: (-1.1h, -0.9h, -0.7h) / 3 ≈ -0.9h",
          "proyeccion": "1.5h"
        }
      },
      "resumen_proyeccion": {
        "MRR": "$55.8K",
        "Churn Rate": "2.5%",
        "NPS": "56",
        "CAC": "$168",
        "LTV": "$2,533",
        "Active Users": "1,962",
        "Support Tickets": "53",
        "Avg Response (h)": "1.5h"
      }
    },
    "tendencia_general": "↑ Positiva en todas las métricas — Mejora sostenida en ingresos (MRR), retención (Churn ↓), satisfacción (NPS ↑), eficiencia (LTV/CAC ↑), crecimiento de base de usuarios y reducción de costos operativos (Soporte y Respuesta)."
  }
}
```