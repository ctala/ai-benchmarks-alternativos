# Granite 4.2 8B — ocr_extraction/screenshot_table_extraction

- model_id: `ibm-granite/granite-4.2-8b`
- success: True  | final: 6.57 | quality: 6.0
- latency_total: 6.777s | tokens_per_second: 132.2
- input_tokens: 417 | output_tokens: 896

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
  "data": {
    "metricas": [
      {
        "nombre": "MRR",
        "enero": "$45.2K",
        "febrero": "$48.7K",
        "marzo": "$52.1K",
        "var_mm": "+7.0%"
      },
      {
        "nombre": "Churn Rate",
        "enero": "4.2%",
        "febrero": "3.8%",
        "marzo": "3.1%",
        "var_mm": "-0.7pp"
      },
      {
        "nombre": "NPS",
        "enero": "42",
        "febrero": "45",
        "marzo": "51",
        "var_mm": "+6"
      },
      {
        "nombre": "CAC",
        "enero": "$234",
        "febrero": "$198",
        "marzo": "187",
        "var_mm": "-$11"
      },
      {
        "nombre": "LTV",
        "enero": "$1,890",
        "febrero": "$2,010",
        "marzo": "$2,340",
        "var_mm": "+$330"
      },
      {
        "nombre": "Active Users",
        "enero": "1,234",
        "febrero": "1,456",
        "marzo": "1,678",
        "var_mm": "+15.3%"
      },
      {
        "nombre": "Support Tickets",
        "enero": "89",
        "febrero": "76",
        "marzo": "63",
        "var_mm": "-17.1%"
      },
      {
        "nombre": "Avg Response (h)",
        "enero": "4.2",
        "febrero": "3.1",
        "marzo": "2.4",
        "var_mm": "-0.7"
      }
    ]
  },
  "calculos": {
    "ltv_cac_ratio": {
      "enero": 8.1,
      "febrero": 10.15,
      "marzo": 12.5
    }
  },
  "mejora_porcentual": {
    "metrica_con_mayor_mejora": "NPS",
    "mejora_enero_marzo": "+21.9%",
    "mejora_febrero_marzo": "+13.3%",
    "mejora_enero_febrero": "+7.1%",
    "metrica_maxima_mejora": "NPS"
  },
  "proyeccion_abril": {
    "metodo": "tendencia_lineal_conservadora",
    "valor_abril": {
      "MRR": "$55.6K",
      "Churn Rate": "2.9%",
      "NPS": "57",
      "CAC": "$176",
      "LTV": "$2,675",
      "Active Users": "1,902",
      "Support Tickets": "55",
      "Avg Response (h)": "2.0"
    },
    "explicacion": "Se proyecta una continuación de la tendencia positiva observada en todas las métricas, manteniendo la misma velocidad de mejora promedio observada entre febrero y marzo (aproximadamente +7% para MRR, +15% para Active Users, -17% para Support Tickets, etc.). Los valores se redondean ligeramente para mantener coherencia con unidades discretas (ej. NPS entero, tickets enteros). LTV/CAC ratio se mantiene creciente."
  }
}