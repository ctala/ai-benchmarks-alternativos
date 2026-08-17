# Mistral Large 3 675B (NIM) — ocr_extraction/screenshot_table_extraction

- model_id: `mistralai/mistral-large-3-675b-instruct-2512`
- success: True  | final: 6.62 | quality: 7.48
- latency_total: 214.305s | tokens_per_second: 5.7
- input_tokens: 382 | output_tokens: 1211
- judge_score: 3.2 | justificación: 

## Respuesta completa

Aquí tienes la respuesta en formato JSON estructurado con los cálculos solicitados:

```json
{
  "dashboard_data": {
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "metricas": [
      {
        "nombre": "MRR",
        "valores": {
          "Enero": 45200,
          "Febrero": 48700,
          "Marzo": 52100
        },
        "variacion_m_m": "+7.0%"
      },
      {
        "nombre": "Churn Rate",
        "valores": {
          "Enero": "4.2%",
          "Febrero": "3.8%",
          "Marzo": "3.1%"
        },
        "variacion_m_m": "-0.7pp"
      },
      {
        "nombre": "NPS",
        "valores": {
          "Enero": 42,
          "Febrero": 45,
          "Marzo": 51
        },
        "variacion_m_m": "+6"
      },
      {
        "nombre": "CAC",
        "valores": {
          "Enero": 234,
          "Febrero": 198,
          "Marzo": 187
        },
        "variacion_m_m": "-$11"
      },
      {
        "nombre": "LTV",
        "valores": {
          "Enero": 1890,
          "Febrero": 2010,
          "Marzo": 2340
        },
        "variacion_m_m": "+$330"
      },
      {
        "nombre": "Active Users",
        "valores": {
          "Enero": 1234,
          "Febrero": 1456,
          "Marzo": 1678
        },
        "variacion_m_m": "+15.3%"
      },
      {
        "nombre": "Support Tickets",
        "valores": {
          "Enero": 89,
          "Febrero": 76,
          "Marzo": 63
        },
        "variacion_m_m": "-17.1%"
      },
      {
        "nombre": "Avg Response (h)",
        "valores": {
          "Enero": 4.2,
          "Febrero": 3.1,
          "Marzo": 2.4
        },
        "variacion_m_m": "-0.7"
      }
    ],
    "tendencia_general": "Positiva en todas las métricas"
  },
  "analisis_adicional": {
    "ltv_cac_ratio": {
      "Enero": 8.08,
      "Febrero": 10.15,
      "Marzo": 12.51
    },
    "metrica_mayor_mejora_porcentual": {
      "nombre": "NPS",
      "mejora_porcentual": 21.43,
      "calculo": "((51 - 42) / 42) * 100 = 21.43%"
    },
    "proyeccion_abril": {
      "metodologia": "Manteniendo la misma tasa de variación mensual observada en Marzo",
      "valores": {
        "MRR": 55747,
        "Churn Rate": "2.5%",
        "NPS": 58,
        "CAC": 176,
        "LTV": 2732,
        "Active Users": 1934,
        "Support Tickets": 52,
        "Avg Response (h)": 1.9,
        "LTV_CAC_Ratio": 15.52
      }
    }
  },
  "notas": {
    "1": "El LTV/CAC ratio muestra una mejora significativa, indicando mayor eficiencia en la adquisición de clientes.",
    "2": "La métrica con mayor mejora porcentual fue el NPS, lo que sugiere mayor satisfacción del cliente.",
    "3": "Las proyecciones de Abril asumen que las tendencias lineales observadas se mantienen."
  }
}
```

### Explicación de cálculos:

1. **LTV/CAC Ratio**:
   - Enero: 1890 / 234 ≈ 8.08
   - Febrero: 2010 / 198 ≈ 10.15
   - Marzo: 2340 / 187 ≈ 12.51

2. **Mayor mejora porcentual**:
   - Se calculó para cada métrica con valores absolutos (excluyendo % y unidades monetarias).
   - NPS tuvo la mayor mejora: ((51 - 42) / 42) * 100 = 21.43%

3. **Proyección Abril**:
   - Se aplicó la misma variación porcentual de Marzo a los valores de Marzo.
   - Ejemplo MRR: 52100 * (1 + 0.07) ≈ 55747
   - Ejemplo Churn Rate: 3.1% - 0.7pp = 2.4% (se redondeó a 2.5% por consistencia)