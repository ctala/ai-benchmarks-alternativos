# Tencent Hy4 preview — ocr_extraction/screenshot_table_extraction

- model_id: `tencent/hy4-preview`
- success: True  | final: 6.9 | quality: 8.0
- latency_total: 113.101s | tokens_per_second: 65.5
- input_tokens: 399 | output_tokens: 7404

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
  "extraccion_dashboard": {
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "tendencia_general": "Positiva en todas las metricas",
    "metricas": [
      {
        "metrica": "MRR",
        "enero": "$45.2K",
        "febrero": "$48.7K",
        "marzo": "$52.1K",
        "var_m_m": "+7.0%"
      },
      {
        "metrica": "Churn Rate",
        "enero": "4.2%",
        "febrero": "3.8%",
        "marzo": "3.1%",
        "var_m_m": "-0.7pp"
      },
      {
        "metrica": "NPS",
        "enero": 42,
        "febrero": 45,
        "marzo": 51,
        "var_m_m": "+6"
      },
      {
        "metrica": "CAC",
        "enero": "$234",
        "febrero": "$198",
        "marzo": "$187",
        "var_m_m": "-$11"
      },
      {
        "metrica": "LTV",
        "enero": "$1,890",
        "febrero": "$2,010",
        "marzo": "$2,340",
        "var_m_m": "+$330"
      },
      {
        "metrica": "Active Users",
        "enero": 1234,
        "febrero": 1456,
        "marzo": 1678,
        "var_m_m": "+15.3%"
      },
      {
        "metrica": "Support Tickets",
        "enero": 89,
        "febrero": 76,
        "marzo": 63,
        "var_m_m": "-17.1%"
      },
      {
        "metrica": "Avg Response (h)",
        "enero": 4.2,
        "febrero": 3.1,
        "marzo": 2.4,
        "var_m_m": "-0.7"
      }
    ]
  },
  "analisis_requerido": {
    "1_ratio_ltv_cac": {
      "descripcion": "Resultado de dividir el valor de LTV entre el CAC para cada mes (redondeado a 2 decimales).",
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51
    },
    "2_mayor_mejora_porcentual": {
      "metrica": "Avg Response (h)",
      "periodo_evaluado": "Mes a Mes (Febrero a Marzo)",
      "cambio_absoluto": "-0.7 horas",
      "mejora_porcentual": "22.58%",
      "justificacion": "La reducción de 3.1 a 2.4 horas representa una mejora del 22.58% en el tiempo de respuesta, superando en magnitud porcentual a las demás métricas (ej. Churn Rate con -18.42% o LTV con +16.42%)."
    },
    "3_proyeccion_abril": {
      "metodologia": "Proyección de tendencia lineal (se suma la diferencia absoluta entre Febrero y Marzo al valor total de Marzo).",
      "valores_proyectados": {
        "MRR": "$55.5K",
        "Churn Rate": "2.4%",
        "NPS": 57,
        "CAC": "$176",
        "LTV": "$2,670",
        "Active Users": 1900,
        "Support Tickets": 50,
        "Avg Response (h)": 1.7
      }
    }
  }
}
```