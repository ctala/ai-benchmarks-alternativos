# Ling 3.0 Flash VL — ocr_extraction/screenshot_table_extraction

- model_id: `inclusionai/ling-3.0-flash-vl`
- success: True  | final: 7.87 | quality: 8.0
- latency_total: 29.144s | tokens_per_second: 151.6
- input_tokens: 456 | output_tokens: 4419

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
  "dashboard": "Dashboard - KPIs Marzo 2026",
  "datos_crudos": {
    "metricas": [
      {
        "nombre": "MRR",
        "unidad": "USD",
        "enero": 45200,
        "febrero": 48700,
        "marzo": 52100,
        "var_mm_pct": 7.0
      },
      {
        "nombre": "Churn Rate",
        "unidad": "%",
        "enero": 4.2,
        "febrero": 3.8,
        "marzo": 3.1,
        "var_mm_pp": -0.7
      },
      {
        "nombre": "NPS",
        "unidad": "puntos",
        "enero": 42,
        "febrero": 45,
        "marzo": 51,
        "var_mm": 6
      },
      {
        "nombre": "CAC",
        "unidad": "USD",
        "enero": 234,
        "febrero": 198,
        "marzo": 187,
        "var_mm_pct": -5.56
      },
      {
        "nombre": "LTV",
        "unidad": "USD",
        "enero": 1890,
        "febrero": 2010,
        "marzo": 2340,
        "var_mm_pct": 16.42
      },
      {
        "nombre": "Active Users",
        "unidad": "usuarios",
        "enero": 1234,
        "febrero": 1456,
        "marzo": 1678,
        "var_mm_pct": 15.3
      },
      {
        "nombre": "Support Tickets",
        "unidad": "tickets",
        "enero": 89,
        "febrero": 76,
        "marzo": 63,
        "var_mm_pct": -17.1
      },
      {
        "nombre": "Avg Response (h)",
        "unidad": "horas",
        "enero": 4.2,
        "febrero": 3.1,
        "marzo": 2.4,
        "var_mm_pct": -22.58
      }
    ]
  },
  "analisis": {
    "ltv_cac_ratio": {
      "descripcion": "Ratio LTV/CAC por mes (valor más alto = mejor eficiencia de inversión)",
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "tendencia": "↑ Creciente (mejora continua)",
      "detalle": {
        "enero": { "ltv": 1890, "cac": 234, "ratio": 8.08 },
        "febrero": { "ltv": 2010, "cac": 198, "ratio": 10.15 },
        "marzo": { "ltv": 2340, "cac": 187, "ratio": 12.51 }
      }
    },
    "mayor_mejora_porcentual": {
      "metrica": "Avg Response (h)",
      "mejora_pct": -22.58,
      "descripcion": "Reducción del tiempo de respuesta promedio de 3.1h a 2.4h (Feb → Mar)",
      "interpretacion": "Una reducción del 22.6% en el tiempo de respuesta representa la mayor mejora porcentual entre todas las métricas, indicando una eficiencia significativa en el soporte al cliente.",
      "ranking_mejoras": [
        { "metrica": "Avg Response (h)", "mejora_pct": -22.58, "tipo": "reducción favorable" },
        { "metrica": "Churn Rate", "mejora_pct": -18.42, "tipo": "reducción favorable" },
        { "metrica": "Support Tickets", "mejora_pct": -17.11, "tipo": "reducción favorable" },
        { "metrica": "LTV", "mejora_pct": 16.42, "tipo": "incremento favorable" },
        { "metrica": "Active Users", "mejora_pct": 15.30, "tipo": "incremento favorable" },
        { "metrica": "NPS", "mejora_pct": 13.33, "tipo": "incremento favorable" },
        { "metrica": "MRR", "mejora_pct": 6.98, "tipo": "incremento favorable" },
        { "metrica": "CAC", "mejora_pct": -5.56, "tipo": "reducción favorable" }
      ]
    },
    "proyeccion_abril_2026": {
      "metodo": "Promedio de las tasas de cambio de los dos últimos periodos (Ene→Feb y Feb→Mar)",
      "proyecciones": [
        {
          "metrica": "MRR",
          "valor_abril": 55940,
          "unidad": "USD",
          "tasa_promedio_pct": 7.36,
          "nota": "~$55.9K"
        },
        {
          "metrica": "Churn Rate",
          "valor_abril": 2.67,
          "unidad": "%",
          "tasa_promedio_pct": -13.97,
          "nota": "Continúa la tendencia a la baja"
        },
        {
          "metrica": "NPS",
          "valor_abril": 56,
          "unidad": "puntos",
          "tasa_promedio_pct": 14.71,
          "nota": "Redondeo al entero más cercano"
        },
        {
          "metrica": "CAC",
          "valor_abril": 167.4,
          "unidad": "USD",
          "tasa_promedio_pct": -10.47,
          "nota": "~$167"
        },
        {
          "metrica": "LTV",
          "valor_abril": 2606,
          "unidad": "USD",
          "tasa_promedio_pct": 11.38,
          "nota": "~$2,606"
        },
        {
          "metrica": "Active Users",
          "valor_abril": 1957,
          "unidad": "usuarios",
          "tasa_promedio_pct": 16.62,
          "nota": "Redondeo al entero más cercano"
        },
        {
          "metrica": "Support Tickets",
          "valor_abril": 53,
          "unidad": "tickets",
          "tasa_promedio_pct": -15.86,
          "nota": "Redondeo al entero más cercano"
        },
        {
          "metrica": "Avg Response (h)",
          "valor_abril": 1.81,
          "unidad": "horas",
          "tasa_promedio_pct": -24.39,
          "nota": "~1.8 horas"
        }
      ]
    }
  },
  "resumen_ejecutivo": {
    "tendencia_general": "Positiva en todas las métricas",
    "hallazgos_clave": [
      "El ratio LTV/CAC mejoró de 8.08 a 12.51 en solo 3 meses, indicando una salud financiera creciente",
      "Avg Response (h) muestra la mayor mejora porcentual con una reducción del 22.6%",
      "Active Users crece a +15.3% M/M, impulsando el crecimiento de MRR (+7.0%)",
      "Churn Rate baja consistentemente (4.2% → 3.8% → 3.1%)",
      "CAC se reduce mientras LTV crece: doble efecto positivo en eficiencia de adquisición"
    ],
    "proyeccion_abril": "Si la tendencia se mantiene, MRR superaría los $55.9K, Active Users llegarían a ~1,957, y el LTV/CAC ratio podría exceder 15.4"
  }
}
```