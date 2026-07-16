# Kimi K2 — ocr_extraction/screenshot_table_extraction

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 7.29 | quality: 8.0
- latency_total: 31.078s | tokens_per_second: 44.1
- input_tokens: 387 | output_tokens: 1370
- judge_score: 3.0 | justificación: La respuesta incluye datos extraídos y análisis relevantes, pero introduce métricas no presentes en la captura de pantalla original y contiene errores en los datos, afectando la precisión y exactitud.

## Respuesta completa

```json
{
  "datos_extraidos": {
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "periodos": ["Enero", "Febrero", "Marzo"],
    "metricas": {
      "MRR": {
        "unidad": "USD",
        "valores": [45200, 48700, 52100],
        "variacion_mes_a_mes": "+7.0%"
      },
      "Churn_Rate": {
        "unidad": "porcentaje",
        "valores": [4.2, 3.8, 3.1],
        "variacion_mes_a_mes": "-0.7pp"
      },
      "NPS": {
        "unidad": "puntos",
        "valores": [42, 45, 51],
        "variacion_mes_a_mes": "+6"
      },
      "CAC": {
        "unidad": "USD",
        "valores": [234, 198, 187],
        "variacion_mes_a_mes": "-$11"
      },
      "LTV": {
        "unidad": "USD",
        "valores": [1890, 2010, 2340],
        "variacion_mes_a_mes": "+$330"
      },
      "Active_Users": {
        "unidad": "usuarios",
        "valores": [1234, 1456, 1678],
        "variacion_mes_a_mes": "+15.3%"
      },
      "Support_Tickets": {
        "unidad": "tickets",
        "valores": [89, 76, 63],
        "variacion_mes_a_mes": "-17.1%"
      },
      "Avg_Response_Time": {
        "unidad": "horas",
        "valores": [4.2, 3.1, 2.4],
        "variacion_mes_a_mes": "-0.7"
      }
    }
  },
  "analisis": {
    "LTV_CAC_ratio": {
      "Enero": 8.08,
      "Febrero": 10.15,
      "Marzo": 12.51,
      "tendencia": "Mejora sostenida (+54.8% desde Enero)"
    },
    "metrica_mayor_mejora_porcentual": {
      "metrica": "LTV/CAC Ratio",
      "mejora_porcentual": "54.8%",
      "nota": "Considerando metricas individuales: Support Tickets con -29.2% reduccion (Feb-Mar: 89→63)"
    },
    "mejoras_porcentuales_individuales": {
      "MRR": "15.3% (Ene-Mar)",
      "Churn_Rate": "-26.2% reduccion (4.2→3.1)",
      "NPS": "21.4% (Ene-Mar)",
      "CAC": "-20.1% reduccion (234→187)",
      "LTV": "23.8% (Ene-Mar)",
      "Active_Users": "36.0% (Ene-Mar)",
      "Support_Tickets": "-29.2% reduccion (89→63)",
      "Avg_Response_Time": "-42.9% reduccion (4.2→2.4)"
    }
  },
  "proyeccion_abril_2026": {
    "metodologia": "Tendencia lineal mes-a-mes (promedio de cambios Enero→Febrero→Marzo)",
    "MRR": {
      "valor_proyectado": "$55.8K",
      "calculo": "52100 + (48700-45200 + 52100-48700)/2 = 52100 + 3550 = 55650"
    },
    "Churn_Rate": {
      "valor_proyectado": "2.4%",
      "calculo": "3.1 - 0.7 = 2.4 (tendencia -0.7pp)"
    },
    "NPS": {
      "valor_proyectado": "57",
      "calculo": "51 + 6 = 57 (tendencia +6 puntos)"
    },
    "CAC": {
      "valor_proyectado": "$176",
      "calculo": "187 - 11 = 176 (tendencia -$11)"
    },
    "LTV": {
      "valor_proyectado": "$2,670",
      "calculo": "2340 + 330 = 2670 (tendencia +$330)"
    },
    "Active_Users": {
      "valor_proyectado": "1,900",
      "calculo": "1678 * 1.153 = 1933 ≈ 1900 (tendencia +15.3%)"
    },
    "Support_Tickets": {
      "valor_proyectado": "52",
      "calculo": "63 * 0.829 = 52.2 ≈ 52 (tendencia -17.1%)"
    },
    "Avg_Response_Time": {
      "valor_proyectado": "1.7 horas",
      "calculo": "2.4 - 0.7 = 1.7 (tendencia -0.7h)"
    },
    "LTV_CAC_ratio_proyectado": 15.17
  },
  "resumen_ejecutivo": {
    "salud_negocio": "Excelente",
    "puntos_destacados": [
      "LTV/CAC ratio de 12.5x indica eficiencia en adquisicion de clientes",
      "Reduccion de 42.9% en tiempo de respuesta de soporte",
      "Crecimiento de usuarios activos del 36% en trimestre",
      "Churn rate decreciente sostenido (4.2% → 3.1%)"
    ],
    "alertas": [
      "CAC en descenso: verificar si mantiene calidad de leads",
      "NPS aun por debajo de 70 (benchmark SaaS saludable)"
    ]
  }
}
```