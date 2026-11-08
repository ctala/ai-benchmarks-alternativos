# Tencent Hy4 — ocr_extraction/screenshot_table_extraction

- model_id: `tencent/hy4`
- success: True  | final: 7.43 | quality: 8.0
- latency_total: 18.998s | tokens_per_second: 108.3
- input_tokens: 402 | output_tokens: 2058

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
  "metadata": {
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "periodo": "Enero - Marzo 2026",
    "tendencia_general": "↑ Positiva en todas las metricas",
    "moneda": "USD",
    "notas": {
      "pp": "puntos porcentuales",
      "K": "miles",
      "Var M/M": "Variación mes a mes (Marzo vs Febrero)"
    }
  },
  "datos_originales": [
    {
      "metrica": "MRR",
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "var_mm": "+7.0%",
      "unidad": "USD"
    },
    {
      "metrica": "Churn Rate",
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "var_mm": "-0.7pp",
      "unidad": "%"
    },
    {
      "metrica": "NPS",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "var_mm": "+6",
      "unidad": "puntos"
    },
    {
      "metrica": "CAC",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "var_mm": "-$11",
      "unidad": "USD"
    },
    {
      "metrica": "LTV",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "var_mm": "+$330",
      "unidad": "USD"
    },
    {
      "metrica": "Active Users",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "var_mm": "+15.3%",
      "unidad": "usuarios"
    },
    {
      "metrica": "Support Tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "var_mm": "-17.1%",
      "unidad": "tickets"
    },
    {
      "metrica": "Avg Response (h)",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "var_mm": "-0.7",
      "unidad": "horas"
    }
  ],
  "ltv_cac_ratio": {
    "enero": {
      "ltv": 1890,
      "cac": 234,
      "ratio": 8.08,
      "interpretacion": "Saludable (>3)"
    },
    "febrero": {
      "ltv": 2010,
      "cac": 198,
      "ratio": 10.15,
      "interpretacion": "Saludable (>3)"
    },
    "marzo": {
      "ltv": 2340,
      "cac": 187,
      "ratio": 12.51,
      "interpretacion": "Excelente (>3)"
    },
    "evolucion": "+54.8% vs Enero"
  },
  "mayor_mejora_porcentual": {
    "metrica": "LTV/CAC Ratio",
    "variacion_ene_mar": "+54.8%",
    "detalle": "De 8.08x a 12.51x (combinación de +23.8% LTV y -20.1% CAC)",
    "alternativa_entre_metricas_originales": {
      "metrica": "NPS",
      "variacion_ene_mar": "+21.4%",
      "detalle": "De 42 a 51 puntos",
      "nota": "Si se consideran solo las métricas de la tabla (excluyendo el ratio derivado), NPS lidera. Le siguen Active Users (+36.0% acumulado) y MRR (+15.3% acumulado). En var M/M, Active Users (+15.3%) es la mayor."
    },
    "ranking_var_mm_absoluta": [
      { "metrica": "Active Users", "var": "+15.3%" },
      { "metrica": "Support Tickets", "var": "-17.1% (mejora)" },
      { "metrica": "MRR", "var": "+7.0%" },
      { "metrica": "NPS", "var": "+13.3% (6/45)" },
      { "metrica": "Avg Response", "var": "-22.6% (0.7/3.1)" },
      { "metrica": "CAC", "var": "-5.6% (11/198)" },
      { "metrica": "LTV", "var": "+16.4% (330/2010)" },
      { "metrica": "Churn Rate", "var": "-18.4% (0.7pp/3.8)" }
    ]
  },
  "proyeccion_abril_2026": {
    "metodo": "Extrapolación de la variación M/M de Marzo (tendencia constante)",
    "supuestos": "Se mantiene el delta absoluto / porcentual observado entre Feb→Mar. Valores redondeados.",
    "valores": [
      {
        "metrica": "MRR",
        "abril": 55747,
        "display": "$55.7K",
        "calculo": "52,100 × 1.070"
      },
      {
        "metrica": "Churn Rate",
        "abril": 2.4,
        "display": "2.4%",
        "calculo": "3.1 - 0.7pp"
      },
      {
        "metrica": "NPS",
        "abril": 57,
        "display": "57",
        "calculo": "51 + 6"
      },
      {
        "metrica": "CAC",
        "abril": 176,
        "display": "$176",
        "calculo": "187 - 11"
      },
      {
        "metrica": "LTV",
        "abril": 2670,
        "display": "$2,670",
        "calculo": "2,340 + 330"
      },
      {
        "metrica": "Active Users",
        "abril": 1935,
        "display": "1,935",
        "calculo": "1,678 × 1.153"
      },
      {
        "metrica": "Support Tickets",
        "abril": 52,
        "display": "52",
        "calculo": "63 × 0.829"
      },
      {
        "metrica": "Avg Response (h)",
        "abril": 1.7,
        "display": "1.7",
        "calculo": "2.4 - 0.7"
      },
      {
        "metrica": "LTV/CAC Ratio (derivado)",
        "abril": 15.17,
        "display": "15.17x",
        "calculo": "2,670 / 176"
      }
    ],
    "advertencias": [
      "Churn Rate podría aproximarse a 0 en ~4 meses con delta lineal; conviene modelar decay logarítmico.",
      "Avg Response (h) llegaría a 1.0h en Mayo y a valores negativos en Junio; requiere piso operativo.",
      "CAC con descuento fijo de $11/mes tiende a 0 en ~16 meses; recomendable usar % decreciente.",
      "Support Tickets y Churn sugieren mejoras de producto/UX que suelen desacelerar (ley de rendimientos decrecientes)."
    ]
  }
}
```

**Aclaración rápida sobre el punto 2:** si hablamos estrictamente de las columnas de la tabla, el **NPS** es el que más mejora en términos relativos acumulados (+21.4% Ene→Mar) y **Active Users** lidera en Var M/M (+15.3%). Pero al incorporar el **LTV/CAC** que pediste calcular, ese ratio derivado es el verdadero ganador (**+54.8%**), porque captura simultáneamente dos mejoras (sube LTV, baja CAC). Lo dejé reflejado con ambas lecturas para que no haya ambigüedad. ¿Quieres que te lo reexporte en CSV o con un esquema para Power BI / Looker?