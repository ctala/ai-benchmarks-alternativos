# Fugu Max — ocr_extraction/screenshot_table_extraction

- model_id: `sakana/fugu-max`
- success: True  | final: 6.97 | quality: 8.0
- latency_total: 18.284s | tokens_per_second: 248.3
- input_tokens: 504 | output_tokens: 4540

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
  "dashboard": "KPIs Marzo 2026",
  "tendencia_general": "↑ Positiva en todas las métricas",
  "datos_extraidos": [
    {
      "metrica": "MRR",
      "unidad": "USD",
      "valores": {
        "Enero": 45200,
        "Feb": 48700,
        "Marzo": 52100
      },
      "var_m_m_reportada": "+7.0%",
      "mejor_direccion": "mayor_es_mejor",
      "mejora_porcentual_feb_mar": 6.98
    },
    {
      "metrica": "Churn Rate",
      "unidad": "%",
      "valores": {
        "Enero": 4.2,
        "Feb": 3.8,
        "Marzo": 3.1
      },
      "var_m_m_reportada": "-0.7pp",
      "mejor_direccion": "menor_es_mejor",
      "mejora_porcentual_feb_mar": 18.42
    },
    {
      "metrica": "NPS",
      "unidad": "puntos",
      "valores": {
        "Enero": 42,
        "Feb": 45,
        "Marzo": 51
      },
      "var_m_m_reportada": "+6",
      "mejor_direccion": "mayor_es_mejor",
      "mejora_porcentual_feb_mar": 13.33
    },
    {
      "metrica": "CAC",
      "unidad": "USD",
      "valores": {
        "Enero": 234,
        "Feb": 198,
        "Marzo": 187
      },
      "var_m_m_reportada": "-$11",
      "mejor_direccion": "menor_es_mejor",
      "mejora_porcentual_feb_mar": 5.56
    },
    {
      "metrica": "LTV",
      "unidad": "USD",
      "valores": {
        "Enero": 1890,
        "Feb": 2010,
        "Marzo": 2340
      },
      "var_m_m_reportada": "+$330",
      "mejor_direccion": "mayor_es_mejor",
      "mejora_porcentual_feb_mar": 16.42
    },
    {
      "metrica": "Active Users",
      "unidad": "usuarios",
      "valores": {
        "Enero": 1234,
        "Feb": 1456,
        "Marzo": 1678
      },
      "var_m_m_reportada": "+15.3%",
      "mejor_direccion": "mayor_es_mejor",
      "mejora_porcentual_feb_mar": 15.25
    },
    {
      "metrica": "Support Tickets",
      "unidad": "tickets",
      "valores": {
        "Enero": 89,
        "Feb": 76,
        "Marzo": 63
      },
      "var_m_m_reportada": "-17.1%",
      "mejor_direccion": "menor_es_mejor",
      "mejora_porcentual_feb_mar": 17.11
    },
    {
      "metrica": "Avg Response (h)",
      "unidad": "horas",
      "valores": {
        "Enero": 4.2,
        "Feb": 3.1,
        "Marzo": 2.4
      },
      "var_m_m_reportada": "-0.7",
      "mejor_direccion": "menor_es_mejor",
      "mejora_porcentual_feb_mar": 22.58
    }
  ],
  "ltv_cac_ratio": {
    "formula": "LTV / CAC",
    "Enero": {
      "ltv": 1890,
      "cac": 234,
      "ratio": 8.08
    },
    "Feb": {
      "ltv": 2010,
      "cac": 198,
      "ratio": 10.15
    },
    "Marzo": {
      "ltv": 2340,
      "cac": 187,
      "ratio": 12.51
    }
  },
  "metrica_con_mayor_mejora_porcentual": {
    "metrica": "Avg Response (h)",
    "mejora_porcentual_feb_mar": 22.58,
    "calculo": "(3.1 - 2.4) / 3.1 * 100",
    "direccion": "menor_es_mejor",
    "nota": "Si se toma literalmente la variación porcentual reportada en la tabla, Support Tickets muestra -17.1%. Sin embargo, al normalizar la mejora relativa de feb a mar, Avg Response (h) tiene la mayor mejora porcentual: 22.58%."
  },
  "proyeccion_abril_2026": {
    "metodo": "Aplicar a marzo la misma variación reportada de feb a mar, según la columna Var M/M",
    "supuesto": "Se mantiene la tendencia reciente y las cifras se redondean",
    "valores_proyectados": {
      "MRR_USD": 55747,
      "MRR_formateado": "$55.7K",
      "Churn_Rate_pct": 2.4,
      "NPS": 57,
      "CAC_USD": 176,
      "LTV_USD": 2670,
      "Active_Users": 1935,
      "Support_Tickets": 52,
      "Avg_Response_h": 1.7,
      "LTV_CAC_ratio": 15.17
    }
  }
}