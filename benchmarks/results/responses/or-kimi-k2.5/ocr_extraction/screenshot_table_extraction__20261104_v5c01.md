# Kimi K2.5 — ocr_extraction/screenshot_table_extraction

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 6.86 | quality: 8.0
- latency_total: 72.281s | tokens_per_second: 29.6
- input_tokens: 387 | output_tokens: 2141

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
  "datos_extraidos": {
    "dashboard": "KPIs Marzo 2026",
    "periodos": ["Enero", "Febrero", "Marzo"],
    "metricas": {
      "MRR": {
        "valores": ["$45.2K", "$48.7K", "$52.1K"],
        "numerico": [45200, 48700, 52100],
        "unidad": "USD",
        "var_mes": "+7.0%"
      },
      "Churn_Rate": {
        "valores": ["4.2%", "3.8%", "3.1%"],
        "numerico": [4.2, 3.8, 3.1],
        "unidad": "porcentaje",
        "var_mes": "-0.7pp"
      },
      "NPS": {
        "valores": [42, 45, 51],
        "numerico": [42, 45, 51],
        "unidad": "puntos",
        "var_mes": "+6"
      },
      "CAC": {
        "valores": ["$234", "$198", "$187"],
        "numerico": [234, 198, 187],
        "unidad": "USD",
        "var_mes": "-$11"
      },
      "LTV": {
        "valores": ["$1,890", "$2,010", "$2,340"],
        "numerico": [1890, 2010, 2340],
        "unidad": "USD",
        "var_mes": "+$330"
      },
      "Active_Users": {
        "valores": [1234, 1456, 1678],
        "numerico": [1234, 1456, 1678],
        "unidad": "usuarios",
        "var_mes": "+15.3%"
      },
      "Support_Tickets": {
        "valores": [89, 76, 63],
        "numerico": [89, 76, 63],
        "unidad": "tickets",
        "var_mes": "-17.1%"
      },
      "Avg_Response_Time": {
        "valores": ["4.2h", "3.1h", "2.4h"],
        "numerico": [4.2, 3.1, 2.4],
        "unidad": "horas",
        "var_mes": "-0.7"
      }
    }
  },
  "analisis": {
    "ltv_cac_ratio": {
      "descripcion": "Ratio LTV/CAC - Indica cuánto valor genera un cliente vs costo de adquisición",
      "valores": {
        "Enero": {
          "ratio": 8.08,
          "formula": "1890 / 234",
          "evaluacion": "Excelente (>3)"
        },
        "Febrero": {
          "ratio": 10.15,
          "formula": "2010 / 198",
          "evaluacion": "Excelente (>3)"
        },
        "Marzo": {
          "ratio": 12.51,
          "formula": "2340 / 187",
          "evaluacion": "Excelente (>3)"
        }
      },
      "tendencia": "↑ Mejorando significativamente (LTV crece, CAC decrece)",
      "recomendacion": "Invertir más en adquisición mientras CAC siga bajo"
    },
    "mayor_mejora_porcentual": {
      "metodologia": "Cálculo de cambio porcentual mes a mes (Feb→Marzo), priorizando métricas donde 'mejorar' es crecer o decrecer según contexto",
      "ranking": [
        {
          "metrica": "LTV",
          "cambio_porcentual": "+16.42%",
          "calculo": "(2340 - 2010) / 2010 * 100",
          "tipo_mejora": "Crecimiento (mayor es mejor)"
        },
        {
          "metrica": "Avg_Response_Time",
          "cambio_porcentual": "-22.58%",
          "calculo": "(2.4 - 3.1) / 3.1 * 100",
          "tipo_mejora": "Reducción (menor es mejor)",
          "nota": "Mejora operativa significativa"
        },
        {
          "metrica": "Support_Tickets",
          "cambio_porcentual": "-17.11%",
          "calculo": "(63 - 76) / 76 * 100",
          "tipo_mejora": "Reducción (menor es mejor)"
        },
        {
          "metrica": "Active_Users",
          "cambio_porcentual": "+15.23%",
          "calculo": "(1678 - 1456) / 1456 * 100"
        },
        {
          "metrica": "NPS",
          "cambio_porcentual": "+13.33%",
          "calculo": "(51 - 45) / 45 * 100"
        }
      ],
      "ganador": {
        "metrica": "LTV",
        "valor_mejora": "+16.42%",
        "justificacion": "Mayor crecimiento porcentual absoluto. Sin embargo, Avg_Response_Time tuvo -22.58% que es una mejora operativa drástica. Depende del peso del negocio: LTV es más estratégico."
      }
    }
  },
  "proyeccion_abril": {
    "metodologia": "Regresión lineal simple basada en tendencia de últimos 2 meses (Feb→Marzo), asumiendo continuidad",
    "supuestos": [
      "Tendencia lineal reciente se mantiene",
      "Sin estacionalidad ni shocks de mercado",
      "Métricas con comportamiento estable"
    ],
    "valores_proyectados": {
      "MRR": {
        "valor": "$55.5K",
        "calculo": "52100 + (52100 - 48700) = 55500",
        "tendencia": "+$3.4K mensual"
      },
      "Churn_Rate": {
        "valor": "2.4%",
        "calculo": "3.1 - 0.7 = 2.4",
        "tendencia": "-0.7pp mensual (desacelerando posiblemente)"
      },
      "NPS": {
        "valor": "57",
        "calculo": "51 + (51 - 45) = 57",
        "tendencia": "+6 puntos mensuales"
      },
      "CAC": {
        "valor": "$176",
        "calculo": "187 - 11 = 176",
        "tendencia": "-$11 mensuales (piso cercano)"
      },
      "LTV": {
        "valor": "$2,670",
        "calculo": "2340 + (2340 - 2010) = 2670",
        "tendencia": "+$330 mensuales"
      },
      "Active_Users": {
        "valor": "1,900",
        "calculo": "1678 + (1678 - 1456) = 1900",
        "tendencia": "+222 usuarios mensuales"
      },
      "Support_Tickets": {
        "valor": "50",
        "calculo": "63 - 13 = 50 (aproximando tendencia -13)",
        "tendencia": "Decrecimiento, posible piso logístico"
      },
      "Avg_Response_Time": {
        "valor": "1.7h",
        "calculo": "2.4 - 0.7 = 1.7",
        "tendencia": "-0.7h mensuales (piso operativo cercano)"
      }
    },
    "ltv_cac_ratio_proyectado": 15.17,
    "alertas_proyeccion": [
      "CAC no puede decrecer indefinidamente; piso estimado ~$120-150",
      "Avg_Response_Time: piso práctico ~1h para soporte humano",
      "Churn_Rate: 0% es imposible; piso natural ~1-2% para SaaS",
      "Support_Tickets: correlacionado con usuarios; verificar si decrece por menos problemas o mejor UX"
    ]
  },
  "resumen_ejecutivo": {
    "salud_negocio": "EXCELENTE",
    "puntaje": "8/8 métricas en dirección correcta",
    "fortalezas_clave": [
      "LTV/CAC ratio creciente: 8→10→12.5 (unit economics sobresalientes)",
      "Churn decreciendo + NPS creciendo = retención y satisfacción",
      "Eficiencia operativa: menos tickets, respuesta más rápida"
    ],
    "recomendaciones": [
      "Acelerar inversión en marketing mientras CAC esté bajo",
      "Investigar causas de mejora en LTV (upsell, expansión, planes superiores)",
      "Documentar y replicar mejoras en tiempo de respuesta de soporte",
      "Preparar infraestructura para crecimiento de usuarios (+15% mensual)"
    ]
  }
}
```