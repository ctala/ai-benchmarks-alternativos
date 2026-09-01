# Qwen 3.8 Flash — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.56 | quality: 10.0
- latency_total: 156.726s | tokens_per_second: 65.8
- input_tokens: 478 | output_tokens: 10310

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
  "extraccion": {
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "periodos": ["Enero", "Febrero", "Marzo"],
    "tendencia_general": "↑ Positiva en todas las metricas",
    "metricas": [
      {
        "metrica": "MRR",
        "valores": {
          "Enero": 45.2,
          "Febrero": 48.7,
          "Marzo": 52.1
        },
        "var_mm": "+7.0%",
        "unidad": "K USD",
        "direccion_ideal": "mayor_es_mejor"
      },
      {
        "metrica": "Churn Rate",
        "valores": {
          "Enero": 4.2,
          "Febrero": 3.8,
          "Marzo": 3.1
        },
        "var_mm": "-0.7pp",
        "unidad": "%",
        "direccion_ideal": "menor_es_mejor"
      },
      {
        "metrica": "NPS",
        "valores": {
          "Enero": 42,
          "Febrero": 45,
          "Marzo": 51
        },
        "var_mm": "+6",
        "unidad": "puntos",
        "direccion_ideal": "mayor_es_mejor"
      },
      {
        "metrica": "CAC",
        "valores": {
          "Enero": 234,
          "Febrero": 198,
          "Marzo": 187
        },
        "var_mm": "-$11",
        "unidad": "USD",
        "direccion_ideal": "menor_es_mejor"
      },
      {
        "metrica": "LTV",
        "valores": {
          "Enero": 1890,
          "Febrero": 2010,
          "Marzo": 2340
        },
        "var_mm": "+$330",
        "unidad": "USD",
        "direccion_ideal": "mayor_es_mejor"
      },
      {
        "metrica": "Active Users",
        "valores": {
          "Enero": 1234,
          "Febrero": 1456,
          "Marzo": 1678
        },
        "var_mm": "+15.3%",
        "unidad": "usuarios",
        "direccion_ideal": "mayor_es_mejor"
      },
      {
        "metrica": "Support Tickets",
        "valores": {
          "Enero": 89,
          "Febrero": 76,
          "Marzo": 63
        },
        "var_mm": "-17.1%",
        "unidad": "tickets",
        "direccion_ideal": "menor_es_mejor"
      },
      {
        "metrica": "Avg Response (h)",
        "valores": {
          "Enero": 4.2,
          "Febrero": 3.1,
          "Marzo": 2.4
        },
        "var_mm": "-0.7",
        "unidad": "horas",
        "direccion_ideal": "menor_es_mejor"
      }
    ]
  },
  "ltv_cac_ratio": {
    "calculado_como": "LTV / CAC",
    "valores": {
      "Enero": 8.08,
      "Febrero": 10.15,
      "Marzo": 12.51
    }
  },
  "mayor_mejora_porcentual": {
    "criterio": "Variación relativa absoluta entre Febrero y Marzo. Para métricas donde menor es mejor, una disminución cuenta como mejora.",
    "metrica": "Avg Response (h)",
    "mejora_porcentual": 22.58,
    "cambio_signed": -22.58,
    "detalle": "Baja de 3.1 a 2.4 horas.",
    "ranking": [
      {
        "metrica": "Avg Response (h)",
        "mejora_porcentual": 22.58,
        "cambio_signed": -22.58
      },
      {
        "metrica": "Churn Rate",
        "mejora_porcentual": 18.42,
        "cambio_signed": -18.42
      },
      {
        "metrica": "Support Tickets",
        "mejora_porcentual": 17.11,
        "cambio_signed": -17.11
      },
      {
        "metrica": "LTV",
        "mejora_porcentual": 16.42,
        "cambio_signed": 16.42
      },
      {
        "metrica": "Active Users",
        "mejora_porcentual": 15.25,
        "cambio_signed": 15.25
      },
      {
        "metrica": "NPS",
        "mejora_porcentual": 13.33,
        "cambio_signed": 13.33
      },
      {
        "metrica": "MRR",
        "mejora_porcentual": 6.98,
        "cambio_signed": 6.98
      },
      {
        "metrica": "CAC",
        "mejora_porcentual": 5.56,
        "cambio_signed": -5.56
      }
    ],
    "nota_alternativa": "Si solo se consideran los cambios porcentuales visibles en la columna Var M/M, la mayor mejora visible es Support Tickets con -17.1%."
  },
  "proyeccion_abril": {
    "supuesto": "La tendencia M/M de Febrero a Marzo se mantiene en Abril. Se aplica el mismo tipo de variación indicada en la columna Var M/M: porcentajes donde hay %, pp donde hay pp, y deltas absolutos donde hay unidades monetarias o de puntos/horas.",
    "valores": {
      "MRR": {
        "abril": 55.75,
        "unidad": "K USD",
        "formula": "52.1 * 1.070"
      },
      "Churn Rate": {
        "abril": 2.4,
        "unidad": "%",
        "formula": "3.1 - 0.7"
      },
      "NPS": {
        "abril": 57,
        "unidad": "puntos",
        "formula": "51 + 6"
      },
      "CAC": {
        "abril": 176,
        "unidad": "USD",
        "formula": "187 - 11"
      },
      "LTV": {
        "abril": 2670,
        "unidad": "USD",
        "formula": "2340 + 330"
      },
      "Active Users": {
        "abril": 1935,
        "unidad": "usuarios",
        "formula": "1678 * 1.153"
      },
      "Support Tickets": {
        "abril": 52.2,
        "unidad": "tickets",
        "formula": "63 * (1 - 0.171)"
      },
      "Avg Response (h)": {
        "abril": 1.7,
        "unidad": "horas",
        "formula": "2.4 - 0.7"
      }
    },
    "ratio_ltv_cac_abril": 15.17,
    "notas": [
      "Los valores pueden redondearse según el formato original del dashboard.",
      "Para Support Tickets, un valor entero redondeado sería 52."
    ]
  }
}