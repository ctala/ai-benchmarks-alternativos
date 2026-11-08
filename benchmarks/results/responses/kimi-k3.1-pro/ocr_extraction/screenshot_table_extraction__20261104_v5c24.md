# Kimi K3.1 Pro — ocr_extraction/screenshot_table_extraction

- model_id: `moonshotai/kimi-k3.1-pro`
- success: True  | final: 6.79 | quality: 8.0
- latency_total: 35.792s | tokens_per_second: 41.4
- input_tokens: 396 | output_tokens: 1482

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
  "dashboard": "KPIs Marzo 2026",
  "moneda": "USD",
  "datos_extraidos": {
    "MRR": {
      "unidad": "USD",
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "variacion_mom_reportada": "+7.0%"
    },
    "Churn Rate": {
      "unidad": "%",
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "variacion_mom_reportada": "-0.7pp"
    },
    "NPS": {
      "unidad": "puntos",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "variacion_mom_reportada": "+6"
    },
    "CAC": {
      "unidad": "USD",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "variacion_mom_reportada": "-11 USD"
    },
    "LTV": {
      "unidad": "USD",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "variacion_mom_reportada": "+330 USD"
    },
    "Active Users": {
      "unidad": "usuarios",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "variacion_mom_reportada": "+15.3%"
    },
    "Support Tickets": {
      "unidad": "tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "variacion_mom_reportada": "-17.1%"
    },
    "Avg Response": {
      "unidad": "horas",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "variacion_mom_reportada": "-0.7 horas"
    }
  },
  "ltv_cac_ratio": {
    "formula": "LTV / CAC",
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51,
    "interpretacion_marzo": "Se generan aproximadamente 12.51 USD de LTV por cada 1 USD de CAC."
  },
  "metrica_mayor_mejora_porcentual": {
    "criterio": "Comparacion porcentual marzo vs. febrero; para metricas donde menor es mejor, la reduccion se considera mejora.",
    "metrica": "Support Tickets",
    "cambio_porcentual": -17.1053,
    "mejora_porcentual": 17.1053,
    "calculo": "(76 - 63) / 76 * 100",
    "comparativo": [
      {
        "metrica": "Support Tickets",
        "mejora_porcentual": 17.1053
      },
      {
        "metrica": "LTV",
        "mejora_porcentual": 16.4179
      },
      {
        "metrica": "Active Users",
        "mejora_porcentual": 15.2473
      },
      {
        "metrica": "NPS",
        "mejora_porcentual": 13.3333
      },
      {
        "metrica": "Churn Rate",
        "mejora_porcentual": 18.4211
      },
      {
        "metrica": "Avg Response",
        "mejora_porcentual": 22.5806
      },
      {
        "metrica": "MRR",
        "mejora_porcentual": 6.9815
      },
      {
        "metrica": "CAC",
        "mejora_porcentual": 5.5556
      }
    ],
    "aclaracion": "Si se consideran todas las metricas operativas, Avg Response presenta la mayor mejora porcentual: 22.58%. Support Tickets seria la mayor solo si se excluye Avg Response."
  },
  "proyeccion_abril": {
    "metodo": "Extrapolacion de un mes usando la variacion absoluta de febrero a marzo; no constituye un pronostico estadistico.",
    "MRR": {
      "valor": 55500,
      "unidad": "USD",
      "calculo": "52100 + (52100 - 48700)"
    },
    "Churn Rate": {
      "valor": 2.4,
      "unidad": "%",
      "calculo": "3.1 + (3.1 - 3.8)"
    },
    "NPS": {
      "valor": 57,
      "unidad": "puntos",
      "calculo": "51 + (51 - 45)"
    },
    "CAC": {
      "valor": 176,
      "unidad": "USD",
      "calculo": "187 + (187 - 198)"
    },
    "LTV": {
      "valor": 2670,
      "unidad": "USD",
      "calculo": "2340 + (2340 - 2010)"
    },
    "Active Users": {
      "valor": 1900,
      "unidad": "usuarios",
      "calculo": "1678 + (1678 - 1456)"
    },
    "Support Tickets": {
      "valor": 50,
      "unidad": "tickets",
      "calculo": "63 + (63 - 76)"
    },
    "Avg Response": {
      "valor": 1.7,
      "unidad": "horas",
      "calculo": "2.4 + (2.4 - 3.1)"
    },
    "LTV_CAC_ratio_proyectado": 15.17
  },
  "advertencias": [
    "La proyeccion asume que el cambio absoluto mas reciente se repite y no incorpora estacionalidad, capacidad operativa ni saturacion.",
    "La tendencia positiva general no implica que todas las metricas deban crecer: en Churn Rate, CAC, Support Tickets y Avg Response, una disminucion representa una mejora."
  ]
}
```