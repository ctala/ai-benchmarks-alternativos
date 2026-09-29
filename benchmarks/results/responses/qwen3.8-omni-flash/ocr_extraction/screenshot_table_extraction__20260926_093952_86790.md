# Qwen 3.8 Omni Flash — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3.8-omni-flash`
- success: True  | final: 7.17 | quality: 8.0
- latency_total: 165.973s | tokens_per_second: 61.1
- input_tokens: 469 | output_tokens: 10149

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
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "periodo_analizado": "Marzo 2026",
    "tendencia_general_reportada": "↑ Positiva en todas las metricas"
  },
  "datos_extraidos": [
    {
      "metrica": "MRR",
      "nombre_completo": "Monthly Recurring Revenue",
      "unidad": "USD miles",
      "sentido_deseado": "mayor_es_mejor",
      "valores": {
        "enero": 45.2,
        "febrero": 48.7,
        "marzo": 52.1
      },
      "var_m_m_reportada": "+7.0%"
    },
    {
      "metrica": "Churn Rate",
      "nombre_completo": "Tasa de cancelación",
      "unidad": "%",
      "sentido_deseado": "menor_es_mejor",
      "valores": {
        "enero": 4.2,
        "febrero": 3.8,
        "marzo": 3.1
      },
      "var_m_m_reportada": "-0.7pp"
    },
    {
      "metrica": "NPS",
      "nombre_completo": "Net Promoter Score",
      "unidad": "puntos",
      "sentido_deseado": "mayor_es_mejor",
      "valores": {
        "enero": 42,
        "febrero": 45,
        "marzo": 51
      },
      "var_m_m_reportada": "+6"
    },
    {
      "metrica": "CAC",
      "nombre_completo": "Customer Acquisition Cost",
      "unidad": "USD",
      "sentido_deseado": "menor_es_mejor",
      "valores": {
        "enero": 234,
        "febrero": 198,
        "marzo": 187
      },
      "var_m_m_reportada": "-$11"
    },
    {
      "metrica": "LTV",
      "nombre_completo": "Lifetime Value",
      "unidad": "USD",
      "sentido_deseado": "mayor_es_mejor",
      "valores": {
        "enero": 1890,
        "febrero": 2010,
        "marzo": 2340
      },
      "var_m_m_reportada": "+$330"
    },
    {
      "metrica": "Active Users",
      "nombre_completo": "Usuarios activos",
      "unidad": "usuarios",
      "sentido_deseado": "mayor_es_mejor",
      "valores": {
        "enero": 1234,
        "febrero": 1456,
        "marzo": 1678
      },
      "var_m_m_reportada": "+15.3%"
    },
    {
      "metrica": "Support Tickets",
      "nombre_completo": "Tickets de soporte",
      "unidad": "tickets",
      "sentido_deseado": "menor_es_mejor",
      "valores": {
        "enero": 89,
        "febrero": 76,
        "marzo": 63
      },
      "var_m_m_reportada": "-17.1%"
    },
    {
      "metrica": "Avg Response (h)",
      "nombre_completo": "Tiempo promedio de respuesta",
      "unidad": "horas",
      "sentido_deseado": "menor_es_mejor",
      "valores": {
        "enero": 4.2,
        "febrero": 3.1,
        "marzo": 2.4
      },
      "var_m_m_reportada": "-0.7"
    }
  ],
  "analisis": {
    "ltv_cac_ratio": {
      "formula": "LTV / CAC",
      "valores": {
        "enero": 8.08,
        "febrero": 10.15,
        "marzo": 12.51
      },
      "lectura": "El ratio mejora de 8.08x en enero a 12.51x en marzo, indicando mayor retorno por dólar invertido en adquisición."
    },
    "mejora_porcentual_marzo_vs_febrero": {
      "metodo": "Para métricas donde menor es mejor, la mejora se calcula como reducción porcentual respecto al valor de febrero y se expresa como valor positivo.",
      "por_metrica": [
        {
          "metrica": "MRR",
          "mejora_pct": 6.98,
          "tipo_cambio": "aumento"
        },
        {
          "metrica": "Churn Rate",
          "mejora_pct": 18.42,
          "tipo_cambio": "reducción"
        },
        {
          "metrica": "NPS",
          "mejora_pct": 13.33,
          "tipo_cambio": "aumento"
        },
        {
          "metrica": "CAC",
          "mejora_pct": 5.56,
          "tipo_cambio": "reducción"
        },
        {
          "metrica": "LTV",
          "mejora_pct": 16.42,
          "tipo_cambio": "aumento"
        },
        {
          "metrica": "Active Users",
          "mejora_pct": 15.25,
          "tipo_cambio": "aumento"
        },
        {
          "metrica": "Support Tickets",
          "mejora_pct": 17.11,
          "tipo_cambio": "reducción"
        },
        {
          "metrica": "Avg Response (h)",
          "mejora_pct": 22.58,
          "tipo_cambio": "reducción"
        }
      ],
      "metrica_con_mayor_mejora_porcentual": {
        "metrica": "Avg Response (h)",
        "nombre_es": "Tiempo promedio de respuesta",
        "mejora_pct": 22.58,
        "valor_febrero": 3.1,
        "valor_marzo": 2.4,
        "motivo": "Presenta la mayor reducción porcentual intermensual, que equivale a la mayor mejora cuando menor es mejor."
      }
    }
  },
  "proyeccion_abril_2026": {
    "metodo": "Tendencia lineal simple: promedio de las variaciones mensuales enero→febrero y febrero→marzo, aplicado al valor de marzo.",
    "supuesto": "Se mantiene el ritmo promedio de cambio observado durante el periodo.",
    "valores": {
      "MRR": 55.55,
      "Churn Rate": 2.55,
      "NPS": 55.5,
      "CAC": 163.5,
      "LTV": 2565,
      "Active Users": 1900,
      "Support Tickets": 50,
      "Avg Response (h)": 1.5
    },
    "unidades": {
      "MRR": "USD miles",
      "Churn Rate": "%",
      "NPS": "puntos",
      "CAC": "USD",
      "LTV": "USD",
      "Active Users": "usuarios",
      "Support Tickets": "tickets",
      "Avg Response (h)": "horas"
    },
    "ltv_cac_ratio_proyectado": 15.69
  },
  "notas": [
    "Los datos extraídos corresponden exactamente a la captura proporcionada.",
    "Las proyecciones son estimaciones basadas en tendencia histórica y no constituyen una garantía de resultados futuros."
  ]
}