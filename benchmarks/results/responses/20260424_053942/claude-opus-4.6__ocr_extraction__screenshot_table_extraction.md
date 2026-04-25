# Claude Opus 4.6 — ocr_extraction/screenshot_table_extraction

- model_id: `anthropic/claude-opus-4-6`
- success: True  | final: 6.16 | quality: 6.16
- latency_total: 27.795s | tokens_per_second: 73.7
- input_tokens: 430 | output_tokens: 2048
- judge_score: 3.2 | justificación: 

## Respuesta completa



```json
{
  "dashboard": {
    "titulo": "KPIs Marzo 2026",
    "periodo": "Enero - Marzo 2026",
    "tendencia_general": "Positiva en todas las métricas"
  },

  "datos_extraidos": {
    "MRR": {
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "variacion_mom": "+7.0%",
      "unidad": "USD"
    },
    "churn_rate": {
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "variacion_mom": "-0.7pp",
      "unidad": "porcentaje"
    },
    "NPS": {
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "variacion_mom": "+6 puntos",
      "unidad": "puntos"
    },
    "CAC": {
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "variacion_mom": "-$11",
      "unidad": "USD"
    },
    "LTV": {
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "variacion_mom": "+$330",
      "unidad": "USD"
    },
    "active_users": {
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "variacion_mom": "+15.3%",
      "unidad": "usuarios"
    },
    "support_tickets": {
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "variacion_mom": "-17.1%",
      "unidad": "tickets"
    },
    "avg_response_time": {
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "variacion_mom": "-0.7h",
      "unidad": "horas"
    }
  },

  "analisis_1_ltv_cac_ratio": {
    "descripcion": "Ratio LTV/CAC por mes (objetivo saludable: >3.0)",
    "enero": {
      "LTV": 1890,
      "CAC": 234,
      "ratio": 8.08,
      "calculo": "1890 / 234 = 8.08"
    },
    "febrero": {
      "LTV": 2010,
      "CAC": 198,
      "ratio": 10.15,
      "calculo": "2010 / 198 = 10.15"
    },
    "marzo": {
      "LTV": 2340,
      "CAC": 187,
      "ratio": 12.51,
      "calculo": "2340 / 187 = 12.51"
    },
    "tendencia": "Fuertemente creciente: de 8.08x a 12.51x (+54.8% en 3 meses)",
    "interpretacion": "Todos los meses superan ampliamente el benchmark de 3x. La empresa genera un retorno excepcional por cada dólar invertido en adquisición, y la tendencia es acelerada."
  },

  "analisis_2_mayor_mejora_porcentual": {
    "metodologia": "Variación porcentual Feb→Mar para cada métrica (para métricas donde la reducción es positiva, se calcula el % de mejora)",
    "comparativa_febrero_a_marzo": {
      "MRR": {
        "variacion_porcentual": "+6.98%",
        "calculo": "(52100 - 48700) / 48700 × 100"
      },
      "churn_rate": {
        "variacion_porcentual": "-18.42% (mejora)",
        "calculo": "(3.1 - 3.8) / 3.8 × 100 = -18.42%"
      },
      "NPS": {
        "variacion_porcentual": "+13.33%",
        "calculo": "(51 - 45) / 45 × 100"
      },
      "CAC": {
        "variacion_porcentual": "-5.56% (mejora)",
        "calculo": "(187 - 198) / 198 × 100 = -5.56%"
      },
      "LTV": {
        "variacion_porcentual": "+16.42%",
        "calculo": "(2340 - 2010) / 2010 × 100"
      },
      "active_users": {
        "variacion_porcentual": "+15.25%",
        "calculo": "(1678 - 1456) / 1456 × 100"
      },
      "support_tickets": {
        "variacion_porcentual": "-17.11% (mejora)",
        "calculo": "(63 - 76) / 76 × 100 = -17.11%"
      },
      "avg_response_time": {
        "variacion_porcentual": "-22.58% (mejora)",
        "calculo": "(2.4 - 3.1) / 3.1 × 100 = -22.58%"
      }
    },
    "ranking_por_magnitud_de_mejora": [
      { "posicion": 1, "metrica": "Avg Response Time", "mejora": "22.58%" },
      { "posicion": 2, "metrica": "Churn Rate", "mejora": "18.42%" },
      { "posicion": 3, "metrica": "Support Tickets", "mejora": "17.11%" },
      { "posicion": 4, "metrica": "LTV", "mejora": "16.42%" },
      { "posicion": 5, "metrica": "Active Users", "mejora": "15.25%" },
      { "posicion": 6, "metrica": "NPS", "mejora": "13.33%" },
      { "posicion": 7, "metrica": "MRR", "mejora": "6.98%" },
      { "posicion": 8, "metrica": "CAC", "mejora": "5.56%" }
    ],
    "ganador": "Avg Response Time con una mejora del 22.58% (de 3.1h a 2.4h)",
    "insight": "La mejora en tiempo de respuesta de soporte probablemente está impulsando la reducción en churn y el aumento del NPS, creando un efecto cascada positivo."
  },

  "analisis_3_proyeccion_abril": {
    "metodologia": "Se aplican dos métodos: (A) tasa de cambio porcentual Feb→Mar mantenida, y (B) tendencia lineal promedio de los 3 meses. Se presenta el promedio ponderado favoreciendo el método más conservador.",
    "proyecciones": {
      "MRR": {
        "metodo_A_tasa_mom": "$55,737",
        "metodo_B_tendencia_lineal": "$55,550",
        "proyeccion_abril": "$55,600",
        "calculo_A": "52100 × 1.0698 = 55,737",
        "calculo_B": "Incremento promedio = (52100-45200)/2 = 3,450 → 52100 + 3450 = 55,550"
      },
      "churn_rate": {
        "metodo_A_tasa_mom": "2.53%",
        "metodo_B_tendencia_lineal": "2.55%",
        "proyeccion_abril": "2.5%",
        "calculo_B": "Reducción promedio = (4.2-3.1)/2 = 0.55pp