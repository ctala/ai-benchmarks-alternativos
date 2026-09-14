# Qwen 3.8 Max 0902 — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 8.15 | quality: 10.0
- latency_total: 126.384s | tokens_per_second: 51.8
- input_tokens: 478 | output_tokens: 6550

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
    "tendencia_general": "Positiva en todas las metricas"
  },
  "datos_extraidos": [
    {
      "metrica": "MRR",
      "unidad": "USD_miles",
      "enero": 45.2,
      "febrero": 48.7,
      "marzo": 52.1,
      "var_m_m_reportada": "+7.0%",
      "direccion_mejora": "aumento"
    },
    {
      "metrica": "Churn Rate",
      "unidad": "porcentaje",
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "var_m_m_reportada": "-0.7pp",
      "direccion_mejora": "disminucion"
    },
    {
      "metrica": "NPS",
      "unidad": "puntos",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "var_m_m_reportada": "+6",
      "direccion_mejora": "aumento"
    },
    {
      "metrica": "CAC",
      "unidad": "USD",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "var_m_m_reportada": "-$11",
      "direccion_mejora": "disminucion"
    },
    {
      "metrica": "LTV",
      "unidad": "USD",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "var_m_m_reportada": "+$330",
      "direccion_mejora": "aumento"
    },
    {
      "metrica": "Active Users",
      "unidad": "usuarios",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "var_m_m_reportada": "+15.3%",
      "direccion_mejora": "aumento"
    },
    {
      "metrica": "Support Tickets",
      "unidad": "tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "var_m_m_reportada": "-17.1%",
      "direccion_mejora": "disminucion"
    },
    {
      "metrica": "Avg Response (h)",
      "unidad": "horas",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "var_m_m_reportada": "-0.7",
      "direccion_mejora": "disminucion"
    }
  ],
  "calculos": {
    "ltv_cac_ratio": {
      "metodo": "LTV / CAC",
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51
    },
    "mejoras_porcentuales_feb_mar": [
      {
        "metrica": "MRR",
        "mejora_porcentual": 7.0,
        "tipo": "aumento"
      },
      {
        "metrica": "Churn Rate",
        "mejora_porcentual": 18.4,
        "tipo": "reduccion"
      },
      {
        "metrica": "NPS",
        "mejora_porcentual": 13.3,
        "tipo": "aumento"
      },
      {
        "metrica": "CAC",
        "mejora_porcentual": 5.6,
        "tipo": "reduccion"
      },
      {
        "metrica": "LTV",
        "mejora_porcentual": 16.4,
        "tipo": "aumento"
      },
      {
        "metrica": "Active Users",
        "mejora_porcentual": 15.3,
        "tipo": "aumento"
      },
      {
        "metrica": "Support Tickets",
        "mejora_porcentual": 17.1,
        "tipo": "reduccion"
      },
      {
        "metrica": "Avg Response (h)",
        "mejora_porcentual": 22.6,
        "tipo": "reduccion"
      }
    ],
    "mayor_mejora_porcentual": {
      "metrica": "Avg Response (h)",
      "mejora_porcentual": 22.6,
      "explicacion": "El tiempo medio de respuesta bajo de 3.1 a 2.4 horas, lo que equivale a una reduccion del 22.6%. Como una menor respuesta es mejor, es la mayor mejora relativa.",
      "base": "Febrero -> Marzo",
      "alternativa_si_solo_se_usan_porcentajes_reportados": "Support Tickets con -17.1%"
    }
  },
  "proyeccion_abril": {
    "metodo": "Se mantiene la variacion mensual observada entre febrero y marzo. Se usa variacion porcentual cuando la tabla indica %, y variacion absoluta cuando indica pp, puntos, USD o horas.",
    "valores_proyectados": [
      {
        "metrica": "MRR",
        "abril": 55.7,
        "unidad": "USD_miles",
        "calculo": "52.1 * (1 + 7.0%)"
      },
      {
        "metrica": "Churn Rate",
        "abril": 2.4,
        "unidad": "porcentaje",
        "calculo": "3.1 - 0.7pp"
      },
      {
        "metrica": "NPS",
        "abril": 57,
        "unidad": "puntos",
        "calculo": "51 + 6"
      },
      {
        "metrica": "CAC",
        "abril": 176,
        "unidad": "USD",
        "calculo": "187 - 11"
      },
      {
        "metrica": "LTV",
        "abril": 2670,
        "unidad": "USD",
        "calculo": "2340 + 330"
      },
      {
        "metrica": "Active Users",
        "abril": 1935,
        "unidad": "usuarios",
        "calculo": "1678 * (1 + 15.3%)"
      },
      {
        "metrica": "Support Tickets",
        "abril": 52,
        "unidad": "tickets",
        "calculo": "63 * (1 - 17.1%)"
      },
      {
        "metrica": "Avg Response (h)",
        "abril": 1.7,
        "unidad": "horas",
        "calculo": "2.4 - 0.7"
      }
    ],
    "ltv_cac_ratio_proyectado_abril": 15.17
  }
}