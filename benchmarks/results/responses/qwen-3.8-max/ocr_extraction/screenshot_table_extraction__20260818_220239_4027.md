# Qwen 3.8 Max — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3.8-max`
- success: True  | final: 6.62 | quality: 8.0
- latency_total: 239.019s | tokens_per_second: 53.4
- input_tokens: 465 | output_tokens: 12759

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
  "dashboard": "DASHBOARD - KPIs Marzo 2026",
  "tendencia_general": "↑ Positiva en todas las metricas",
  "criterios_redondeo": "Porcentajes y ratios redondeados a 2 decimales; conteos de usuarios/tickets redondeados al entero más próximo.",
  "datos_extraidos": [
    {
      "metrica": "MRR",
      "enero": 45.2,
      "febrero": 48.7,
      "marzo": 52.1,
      "unidad": "USD_miles",
      "var_m_m_original": "+7.0%",
      "var_m_m_relativa_calculada_pct": 6.98,
      "direccion_mejora": "aumento"
    },
    {
      "metrica": "Churn Rate",
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "unidad": "porcentaje",
      "var_m_m_original": "-0.7pp",
      "var_m_m_relativa_calculada_pct": -18.42,
      "direccion_mejora": "disminucion"
    },
    {
      "metrica": "NPS",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "unidad": "puntos",
      "var_m_m_original": "+6",
      "var_m_m_relativa_calculada_pct": 13.33,
      "direccion_mejora": "aumento"
    },
    {
      "metrica": "CAC",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "unidad": "USD",
      "var_m_m_original": "-$11",
      "var_m_m_relativa_calculada_pct": -5.56,
      "direccion_mejora": "disminucion"
    },
    {
      "metrica": "LTV",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "unidad": "USD",
      "var_m_m_original": "+$330",
      "var_m_m_relativa_calculada_pct": 16.42,
      "direccion_mejora": "aumento"
    },
    {
      "metrica": "Active Users",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "unidad": "usuarios",
      "var_m_m_original": "+15.3%",
      "var_m_m_relativa_calculada_pct": 15.25,
      "direccion_mejora": "aumento"
    },
    {
      "metrica": "Support Tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "unidad": "tickets",
      "var_m_m_original": "-17.1%",
      "var_m_m_relativa_calculada_pct": -17.11,
      "direccion_mejora": "disminucion"
    },
    {
      "metrica": "Avg Response (h)",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "unidad": "horas",
      "var_m_m_original": "-0.7",
      "var_m_m_relativa_calculada_pct": -22.58,
      "direccion_mejora": "disminucion"
    }
  ],
  "ltv_cac_ratio": {
    "formula": "LTV / CAC",
    "valores": [
      {
        "mes": "Enero",
        "LTV": 1890,
        "CAC": 234,
        "ratio": 8.08
      },
      {
        "mes": "Febrero",
        "LTV": 2010,
        "CAC": 198,
        "ratio": 10.15
      },
      {
        "mes": "Marzo",
        "LTV": 2340,
        "CAC": 187,
        "ratio": 12.51
      }
    ],
    "abril_proyectado": {
      "LTV_proyectado": 2670,
      "CAC_proyectado": 176,
      "ratio": 15.17
    }
  },
  "metrica_mayor_mejora_porcentual": {
    "metrica": "Avg Response (h)",
    "valor_febrero": 3.1,
    "valor_marzo": 2.4,
    "variacion_relativa_pct": -22.58,
    "mejora_pct": 22.58,
    "tipo_mejora": "reduccion",
    "explicacion": "El tiempo medio de respuesta bajó de 3.1 a 2.4 horas entre febrero y marzo; como una reducción es positiva, equivale a la mayor mejora relativa.",
    "nota": "Si solo se consideran las variaciones porcentuales ya visibles en la tabla, Support Tickets (-17.1%) sería la mayor mejora porcentual explícita; al relativizar todas las métricas, Avg Response (h) lidera."
  },
  "ranking_mejora_relativa_febrero_a_marzo": [
    {
      "metrica": "Avg Response (h)",
      "mejora_pct": 22.58,
      "tipo": "reduccion"
    },
    {
      "metrica": "Churn Rate",
      "mejora_pct": 18.42,
      "tipo": "reduccion"
    },
    {
      "metrica": "Support Tickets",
      "mejora_pct": 17.11,
      "tipo": "reduccion"
    },
    {
      "metrica": "LTV",
      "mejora_pct": 16.42,
      "tipo": "aumento"
    },
    {
      "metrica": "Active Users",
      "mejora_pct": 15.25,
      "tipo": "aumento"
    },
    {
      "metrica": "NPS",
      "mejora_pct": 13.33,
      "tipo": "aumento"
    },
    {
      "metrica": "MRR",
      "mejora_pct": 6.98,
      "tipo": "aumento"
    },
    {
      "metrica": "CAC",
      "mejora_pct": 5.56,
      "tipo": "reduccion"
    }
  ],
  "proyeccion_abril": {
    "metodo": "Se aplica la variación M/M mostrada en la tabla sobre marzo: porcentual para variaciones en %, y absoluta para pp, USD, puntos u horas.",
    "valores_proyectados": [
      {
        "metrica": "MRR",
        "abril": 55.75,
        "unidad": "USD_miles",
        "delta_aplicado": "+7.0%"
      },
      {
        "metrica": "Churn Rate",
        "abril": 2.4,
        "unidad": "porcentaje",
        "delta_aplicado": "-0.7pp"
      },
      {
        "metrica": "NPS",
        "abril": 57,
        "unidad": "puntos",
        "delta_aplicado": "+6"
      },
      {
        "metrica": "CAC",
        "abril": 176,
        "unidad": "USD",
        "delta_aplicado": "-$11"
      },
      {
        "metrica": "LTV",
        "abril": 2670,
        "unidad": "USD",
        "delta_aplicado": "+$330"
      },
      {
        "metrica": "Active Users",
        "abril": 1935,
        "unidad": "usuarios",
        "delta_aplicado": "+15.3%"
      },
      {
        "metrica": "Support Tickets",
        "abril": 52,
        "unidad": "tickets",
        "delta_aplicado": "-17.1%"
      },
      {
        "metrica": "Avg Response (h)",
        "abril": 1.7,
        "unidad": "horas",
        "delta_aplicado": "-0.7"
      }
    ]
  }
}