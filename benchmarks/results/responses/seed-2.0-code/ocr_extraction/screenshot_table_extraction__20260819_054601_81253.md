# Seed 2.0 Code — ocr_extraction/screenshot_table_extraction

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 6.8 | quality: 8.0
- latency_total: 167.784s | tokens_per_second: 61.8
- input_tokens: 462 | output_tokens: 10362

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
  "dashboard_metadata": {
    "titulo": "KPIs Marzo 2026",
    "tendencia_general": "↑ Positiva en todas las métricas"
  },
  "metricas_historicas": [
    {
      "metrica": "MRR",
      "valores_mensuales": {
        "enero": { "valor_numerico": 45200, "valor_formateado": "$45.2K" },
        "febrero": { "valor_numerico": 48700, "valor_formateado": "$48.7K" },
        "marzo": { "valor_numerico": 52100, "valor_formateado": "$52.1K" }
      },
      "variacion_mm": {
        "valor_numerico": 0.07,
        "valor_formateado": "+7.0%",
        "tipo": "porcentaje"
      }
    },
    {
      "metrica": "Churn Rate",
      "valores_mensuales": {
        "enero": { "valor_numerico": 0.042, "valor_formateado": "4.2%" },
        "febrero": { "valor_numerico": 0.038, "valor_formateado": "3.8%" },
        "marzo": { "valor_numerico": 0.031, "valor_formateado": "3.1%" }
      },
      "variacion_mm": {
        "valor_numerico": -0.007,
        "valor_formateado": "-0.7pp",
        "tipo": "puntos_porcentuales"
      }
    },
    {
      "metrica": "NPS",
      "valores_mensuales": {
        "enero": { "valor_numerico": 42, "valor_formateado": "42" },
        "febrero": { "valor_numerico": 45, "valor_formateado": "45" },
        "marzo": { "valor_numerico": 51, "valor_formateado": "51" }
      },
      "variacion_mm": {
        "valor_numerico": 6,
        "valor_formateado": "+6",
        "tipo": "absoluto"
      }
    },
    {
      "metrica": "CAC",
      "valores_mensuales": {
        "enero": { "valor_numerico": 234, "valor_formateado": "$234" },
        "febrero": { "valor_numerico": 198, "valor_formateado": "$198" },
        "marzo": { "valor_numerico": 187, "valor_formateado": "$187" }
      },
      "variacion_mm": {
        "valor_numerico": -11,
        "valor_formateado": "-$11",
        "tipo": "monetario"
      }
    },
    {
      "metrica": "LTV",
      "valores_mensuales": {
        "enero": { "valor_numerico": 1890, "valor_formateado": "$1,890" },
        "febrero": { "valor_numerico": 2010, "valor_formateado": "$2,010" },
        "marzo": { "valor_numerico": 2340, "valor_formateado": "$2,340" }
      },
      "variacion_mm": {
        "valor_numerico": 330,
        "valor_formateado": "+$330",
        "tipo": "monetario"
      }
    },
    {
      "metrica": "Active Users",
      "valores_mensuales": {
        "enero": { "valor_numerico": 1234, "valor_formateado": "1,234" },
        "febrero": { "valor_numerico": 1456, "valor_formateado": "1,456" },
        "marzo": { "valor_numerico": 1678, "valor_formateado": "1,678" }
      },
      "variacion_mm": {
        "valor_numerico": 0.153,
        "valor_formateado": "+15.3%",
        "tipo": "porcentaje"
      }
    },
    {
      "metrica": "Support Tickets",
      "valores_mensuales": {
        "enero": { "valor_numerico": 89, "valor_formateado": "89" },
        "febrero": { "valor_numerico": 76, "valor_formateado": "76" },
        "marzo": { "valor_numerico": 63, "valor_formateado": "63" }
      },
      "variacion_mm": {
        "valor_numerico": -0.171,
        "valor_formateado": "-17.1%",
        "tipo": "porcentaje"
      }
    },
    {
      "metrica": "Avg Response (h)",
      "valores_mensuales": {
        "enero": { "valor_numerico": 4.2, "valor_formateado": "4.2" },
        "febrero": { "valor_numerico": 3.1, "valor_formateado": "3.1" },
        "marzo": { "valor_numerico": 2.4, "valor_formateado": "2.4" }
      },
      "variacion_mm": {
        "valor_numerico": -0.7,
        "valor_formateado": "-0.7",
        "tipo": "absoluto"
      }
    }
  ],
  "calculos_adicionales": {
    "ltv_cac_ratio_mensual": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51
    },
    "metrica_mayor_mejora_porcentual": {
      "metrica": "Avg Response (h)",
      "porcentaje_mejora": 22.58,
      "explicacion": "Métrica donde MENOR valor es MEJOR. Mejora calculada normalizando la variación mes a mes a porcentaje del valor anterior: ((Valor Febrero - Valor Marzo)/Valor Febrero)*100 = ((3.1 - 2.4)/3.1)*100 ≈22.58%, superando a Churn Rate (18.42%) y Support Tickets (17.11%)"
    },
    "proyeccion_abril": [
      {
        "metrica": "MRR",
        "valor_numerico": 55747,
        "valor_formateado": "$55.7K"
      },
      {
        "metrica": "Churn Rate",
        "valor_numerico": 0.024,
        "valor_formateado": "2.4%"
      },
      {
        "metrica": "NPS",
        "valor_numerico": 57,
        "valor_formateado": "57"
      },
      {
        "metrica": "CAC",
        "valor_numerico": 176,
        "valor_formateado": "$176"
      },
      {
        "metrica": "LTV",
        "valor_numerico": 2670,
        "valor_formateado": "$2,670"
      },
      {
        "metrica": "Active Users",
        "valor_numerico": 1935,
        "valor_formateado": "1,935"
      },
      {
        "metrica": "Support Tickets",
        "valor_numerico": 52,
        "valor_formateado": "52"
      },
      {
        "metrica": "Avg Response (h)",
        "valor_numerico": 1.7,
        "valor_formateado": "1.7"
      }
    ]
  }
}

### Explicación de cálculos (incorporados en el JSON):
1. **LTV/CAC Ratio**: Calculado como `LTV (valor numérico) / CAC (valor numérico)` por mes, redondeado a 2 decimales (estándar para métricas SaaS).
2. **Métrica con mayor mejora porcentual**: Normalizada para comparar todas las métricas (independientemente de si "mayor" o "menor" es mejor) como `((Valor Anterior - Valor Actual)/Valor Anterior)*100` para métricas de reducción, o `((Valor Actual - Valor Anterior)/Valor Anterior)*100` para métricas de crecimiento. El `Avg Response (h)` tuvo la mayor mejora (22.58%).
3. **Proyección de Abril**: Se aplicó **la misma variación mes a mes (tipo y valor)** que la registrada entre Febrero y Marzo a los valores de Marzo, manteniendo el formato original de la tabla.