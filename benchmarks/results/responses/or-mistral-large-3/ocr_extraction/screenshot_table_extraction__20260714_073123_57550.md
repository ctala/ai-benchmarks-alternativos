# Mistral Large 3 675B — ocr_extraction/screenshot_table_extraction

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 7.32 | quality: 8.0
- latency_total: 15.878s | tokens_per_second: 81.9
- input_tokens: 422 | output_tokens: 1301
- judge_score: 3.0 | justificación: La respuesta incluye datos extraídos correctamente y proyecciones, pero introduce métricas no presentes en la captura de pantalla original, afectando la precisión y exactitud de los datos.

## Respuesta completa

Aquí tienes la respuesta en formato JSON estructurado con los cálculos y proyecciones solicitadas:

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
        "variacion_mes_a_mes": "+7.0%"
      },
      {
        "nombre": "Churn Rate",
        "valores": {
          "Enero": "4.2%",
          "Febrero": "3.8%",
          "Marzo": "3.1%"
        },
        "variacion_mes_a_mes": "-0.7pp"
      },
      {
        "nombre": "NPS",
        "valores": {
          "Enero": 42,
          "Febrero": 45,
          "Marzo": 51
        },
        "variacion_mes_a_mes": "+6"
      },
      {
        "nombre": "CAC",
        "valores": {
          "Enero": 234,
          "Febrero": 198,
          "Marzo": 187
        },
        "variacion_mes_a_mes": "-$11"
      },
      {
        "nombre": "LTV",
        "valores": {
          "Enero": 1890,
          "Febrero": 2010,
          "Marzo": 2340
        },
        "variacion_mes_a_mes": "+$330"
      },
      {
        "nombre": "Active Users",
        "valores": {
          "Enero": 1234,
          "Febrero": 1456,
          "Marzo": 1678
        },
        "variacion_mes_a_mes": "+15.3%"
      },
      {
        "nombre": "Support Tickets",
        "valores": {
          "Enero": 89,
          "Febrero": 76,
          "Marzo": 63
        },
        "variacion_mes_a_mes": "-17.1%"
      },
      {
        "nombre": "Avg Response (h)",
        "valores": {
          "Enero": 4.2,
          "Febrero": 3.1,
          "Marzo": 2.4
        },
        "variacion_mes_a_mes": "-0.7"
      }
    ],
    "tendencia_general": "Positiva en todas las métricas"
  },
  "calculos_adicionales": {
    "ltv_cac_ratio": {
      "Enero": 8.08,
      "Febrero": 10.15,
      "Marzo": 12.51
    },
    "metrica_mayor_mejora_porcentual": {
      "nombre": "Active Users",
      "mejora": "15.3%",
      "valor": "+15.3%"
    }
  },
  "proyeccion_abril": {
    "nota": "Proyección basada en la tendencia lineal de los últimos 3 meses (enero-marzo)",
    "valores": {
      "MRR": {
        "valor": 55500,
        "variacion": "+6.5%"
      },
      "Churn Rate": {
        "valor": "2.4%",
        "variacion": "-0.7pp"
      },
      "NPS": {
        "valor": 57,
        "variacion": "+6"
      },
      "CAC": {
        "valor": 176,
        "variacion": "-$11"
      },
      "LTV": {
        "valor": 2670,
        "variacion": "+$330"
      },
      "Active Users": {
        "valor": 1900,
        "variacion": "+13.2%"
      },
      "Support Tickets": {
        "valor": 50,
        "variacion": "-20.6%"
      },
      "Avg Response (h)": {
        "valor": 1.7,
        "variacion": "-0.7"
      },
      "LTV/CAC Ratio": 15.17
    }
  },
  "observaciones": [
    "El LTV/CAC ratio muestra una mejora significativa, pasando de 8.08 en enero a 12.51 en marzo",
    "La reducción en Support Tickets y Avg Response time sugiere mejoras en la eficiencia del soporte",
    "La proyección asume que las tendencias actuales se mantendrán sin cambios disruptivos"
  ]
}
```

### Detalles de los cálculos:
1. **LTV/CAC Ratio**:
   - Enero: 1890/234 ≈ 8.08
   - Febrero: 2010/198 ≈ 10.15
   - Marzo: 2340/187 ≈ 12.51

2. **Métrica con mayor mejora porcentual**:
   - "Active Users" con +15.3% (la variación más alta entre las métricas con porcentaje)

3. **Proyección Abril**:
   - Se calculó la diferencia absoluta entre meses y se aplicó la misma variación al último valor registrado (marzo).
   - Para porcentajes (como Churn Rate), se mantuvo la misma reducción en puntos porcentuales.
   - Para LTV/CAC Ratio de abril: 2670/176 ≈ 15.17.