# DeepSeek V4.1 Flash — ocr_extraction/screenshot_table_extraction

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 7.19 | quality: 8.0
- latency_total: 121.984s | tokens_per_second: 57.6
- input_tokens: 412 | output_tokens: 7032

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
  "titulo": "DASHBOARD - KPIs Marzo 2026",
  "tendencia_general": "↑ Positiva en todas las metricas",
  "datos_extraidos": [
    {
      "metrica": "MRR",
      "unidad": "USD",
      "valores": {
        "Enero": 45200,
        "Febrero": 48700,
        "Marzo": 52100
      },
      "var_m_m": {
        "texto": "+7.0%",
        "tipo": "porcentaje"
      }
    },
    {
      "metrica": "Churn Rate",
      "unidad": "%",
      "valores": {
        "Enero": 4.2,
        "Febrero": 3.8,
        "Marzo": 3.1
      },
      "var_m_m": {
        "texto": "-0.7pp",
        "tipo": "puntos_porcentuales"
      }
    },
    {
      "metrica": "NPS",
      "unidad": "puntos",
      "valores": {
        "Enero": 42,
        "Febrero": 45,
        "Marzo": 51
      },
      "var_m_m": {
        "texto": "+6",
        "tipo": "puntos"
      }
    },
    {
      "metrica": "CAC",
      "unidad": "USD",
      "valores": {
        "Enero": 234,
        "Febrero": 198,
        "Marzo": 187
      },
      "var_m_m": {
        "texto": "-$11",
        "tipo": "USD"
      }
    },
    {
      "metrica": "LTV",
      "unidad": "USD",
      "valores": {
        "Enero": 1890,
        "Febrero": 2010,
        "Marzo": 2340
      },
      "var_m_m": {
        "texto": "+$330",
        "tipo": "USD"
      }
    },
    {
      "metrica": "Active Users",
      "unidad": "usuarios",
      "valores": {
        "Enero": 1234,
        "Febrero": 1456,
        "Marzo": 1678
      },
      "var_m_m": {
        "texto": "+15.3%",
        "tipo": "porcentaje"
      }
    },
    {
      "metrica": "Support Tickets",
      "unidad": "tickets",
      "valores": {
        "Enero": 89,
        "Febrero": 76,
        "Marzo": 63
      },
      "var_m_m": {
        "texto": "-17.1%",
        "tipo": "porcentaje"
      }
    },
    {
      "metrica": "Avg Response (h)",
      "unidad": "horas",
      "valores": {
        "Enero": 4.2,
        "Febrero": 3.1,
        "Marzo": 2.4
      },
      "var_m_m": {
        "texto": "-0.7",
        "tipo": "horas"
      }
    }
  ],
  "ltv_cac_ratio": {
    "Enero": 8.08,
    "Febrero": 10.15,
    "Marzo": 12.51
  },
  "mayor_mejora_porcentual": {
    "metrica": "Avg Response (h)",
    "cambio_porcentual_feb_mar": -22.58,
    "interpretacion": "Mayor mejora porcentual normalizada: bajó de 3.1 h a 2.4 h (-22.58%). Si se usa solo la columna Var M/M literal en formato %, la mayor es Support Tickets con -17.1%.",
    "ranking_mejora_porcentual_feb_mar": [
      {
        "metrica": "Avg Response (h)",
        "mejora_porcentual": 22.58
      },
      {
        "metrica": "Churn Rate",
        "mejora_porcentual": 18.42
      },
      {
        "metrica": "Support Tickets",
        "mejora_porcentual": 17.11
      },
      {
        "metrica": "LTV",
        "mejora_porcentual": 16.42
      },
      {
        "metrica": "Active Users",
        "mejora_porcentual": 15.25
      },
      {
        "metrica": "NPS",
        "mejora_porcentual": 13.33
      },
      {
        "metrica": "MRR",
        "mejora_porcentual": 6.98
      },
      {
        "metrica": "CAC",
        "mejora_porcentual": 5.56
      }
    ]
  },
  "proyeccion_abril": {
    "metodo": "Aplicar la variación M/M de Marzo (Feb→Mar) a los valores de Marzo.",
    "valores": {
      "MRR": 55747,
      "Churn Rate": 2.4,
      "NPS": 57,
      "CAC": 176,
      "LTV": 2670,
      "Active Users": 1935,
      "Support Tickets": 52,
      "Avg Response (h)": 1.7
    },
    "unidades": {
      "MRR": "USD",
      "Churn Rate": "%",
      "NPS": "puntos",
      "CAC": "USD",
      "LTV": "USD",
      "Active Users": "usuarios",
      "Support Tickets": "tickets",
      "Avg Response (h)": "horas"
    },
    "ltv_cac_ratio": 15.17
  }
}