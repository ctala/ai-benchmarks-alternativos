# Muse Wonder — ocr_extraction/screenshot_table_extraction

- model_id: `meta/muse-wonder`
- success: True  | final: 6.82 | quality: 8.0
- latency_total: 17.13s | tokens_per_second: 178.1
- input_tokens: 363 | output_tokens: 3050

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
  "dashboard": "DASHBOARD - KPIs Marzo 2026",
  "tendencia_general": "Positiva en todas las metricas",
  "datos_extraidos": [
    {
      "metrica": "MRR",
      "unidad": "USD",
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "var_m_m": "+7.0%"
    },
    {
      "metrica": "Churn Rate",
      "unidad": "%",
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "var_m_m": "-0.7pp"
    },
    {
      "metrica": "NPS",
      "unidad": "puntos",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "var_m_m": "+6"
    },
    {
      "metrica": "CAC",
      "unidad": "USD",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "var_m_m": "-11"
    },
    {
      "metrica": "LTV",
      "unidad": "USD",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "var_m_m": "+330"
    },
    {
      "metrica": "Active Users",
      "unidad": "usuarios",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "var_m_m": "+15.3%"
    },
    {
      "metrica": "Support Tickets",
      "unidad": "tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "var_m_m": "-17.1%"
    },
    {
      "metrica": "Avg Response (h)",
      "unidad": "horas",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "var_m_m": "-0.7"
    }
  ],
  "analisis": {
    "ltv_cac_ratio": {
      "formula": "LTV / CAC",
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "interpretacion": "El ratio mejora cada mes, pasando de 8.08 en enero a 12.51 en marzo."
    },
    "mejora_porcentual_febrero_marzo": {
      "MRR": 6.98,
      "Churn Rate": 18.42,
      "NPS": 13.33,
      "CAC": 5.56,
      "LTV": 16.42,
      "Active Users": 15.25,
      "Support Tickets": 17.11,
      "Avg Response (h)": 22.58
    },
    "metrica_con_mayor_mejora_porcentual": {
      "metrica": "Avg Response (h)",
      "mejora_porcentual": 22.58,
      "cambio_febrero_marzo": "-0.7 horas",
      "valores": {
        "febrero": 3.1,
        "marzo": 2.4
      },
      "nota": "Calculado como mejora favorable respecto a febrero. En metricas negativas como Churn, CAC, Support Tickets y Avg Response, una reduccion se considera mejora."
    },
    "proyeccion_abril": {
      "metodo": "Proyeccion lineal aplicando a marzo la misma variacion absoluta registrada de febrero a marzo",
      "valores_proyectados": {
        "MRR": 55500,
        "Churn Rate": 2.4,
        "NPS": 57,
        "CAC": 176,
        "LTV": 2670,
        "Active Users": 1900,
        "Support Tickets": 50,
        "Avg Response (h)": 1.7,
        "LTV/CAC Ratio": 15.17
      },
      "detalle_calculo": {
        "MRR": "52100 + (52100 - 48700) = 55500",
        "Churn Rate": "3.1 + (3.1 - 3.8) = 2.4",
        "NPS": "51 + (51 - 45) = 57",
        "CAC": "187 + (187 - 198) = 176",
        "LTV": "2340 + (2340 - 2010) = 2670",
        "Active Users": "1678 + (1678 - 1456) = 1900",
        "Support Tickets": "63 + (63 - 76) = 50",
        "Avg Response (h)": "2.4 + (2.4 - 3.1) = 1.7",
        "LTV/CAC Ratio": "2670 / 176 = 15.17"
      }
    }
  }
}
```