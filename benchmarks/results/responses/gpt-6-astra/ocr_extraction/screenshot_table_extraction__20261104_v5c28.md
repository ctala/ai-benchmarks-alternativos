# GPT-6 Astra — ocr_extraction/screenshot_table_extraction

- model_id: `openai/gpt-6-astra`
- success: True  | final: 6.62 | quality: 8.0
- latency_total: 22.103s | tokens_per_second: 70.0
- input_tokens: 379 | output_tokens: 1548

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
  "periodo": {
    "anio": 2026,
    "meses_observados": ["enero", "febrero", "marzo"],
    "mes_proyectado": "abril"
  },
  "metodologia": {
    "normalizacion": "Los importes expresados en K se multiplican por 1000. Los porcentajes se representan en escala 0–100.",
    "ltv_cac": "LTV / CAC, redondeado a 2 decimales.",
    "mejora_porcentual": "Comparación de febrero a marzo: (marzo - febrero) / febrero × 100 para métricas donde subir es favorable; (febrero - marzo) / febrero × 100 para métricas donde bajar es favorable.",
    "proyeccion_abril": "Extrapolación lineal del último cambio mensual: abril = marzo + (marzo - febrero). No se aplica crecimiento compuesto."
  },
  "metricas": [
    {
      "nombre": "MRR",
      "unidad": "$",
      "direccion_favorable": "aumento",
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "variacion_mensual_reportada": "+7.0%",
      "mejora_porcentual_calculada": 6.98,
      "abril_proyectado": 55500
    },
    {
      "nombre": "Churn Rate",
      "unidad": "%",
      "direccion_favorable": "disminucion",
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "variacion_mensual_reportada": "-0.7pp",
      "mejora_porcentual_calculada": 18.42,
      "abril_proyectado": 2.4
    },
    {
      "nombre": "NPS",
      "unidad": "puntos",
      "direccion_favorable": "aumento",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "variacion_mensual_reportada": "+6",
      "mejora_porcentual_calculada": 13.33,
      "abril_proyectado": 57
    },
    {
      "nombre": "CAC",
      "unidad": "$",
      "direccion_favorable": "disminucion",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "variacion_mensual_reportada": "-$11",
      "mejora_porcentual_calculada": 5.56,
      "abril_proyectado": 176
    },
    {
      "nombre": "LTV",
      "unidad": "$",
      "direccion_favorable": "aumento",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "variacion_mensual_reportada": "+$330",
      "mejora_porcentual_calculada": 16.42,
      "abril_proyectado": 2670
    },
    {
      "nombre": "Active Users",
      "unidad": "usuarios",
      "direccion_favorable": "aumento",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "variacion_mensual_reportada": "+15.3%",
      "mejora_porcentual_calculada": 15.25,
      "abril_proyectado": 1900
    },
    {
      "nombre": "Support Tickets",
      "unidad": "tickets",
      "direccion_favorable": "disminucion",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "variacion_mensual_reportada": "-17.1%",
      "mejora_porcentual_calculada": 17.11,
      "abril_proyectado": 50
    },
    {
      "nombre": "Avg Response (h)",
      "unidad": "horas",
      "direccion_favorable": "disminucion",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "variacion_mensual_reportada": "-0.7",
      "mejora_porcentual_calculada": 22.58,
      "abril_proyectado": 1.7
    }
  ],
  "ratio_ltv_cac": {
    "unidad": "veces",
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51
  },
  "mayor_mejora_porcentual": {
    "metrica": "Avg Response (h)",
    "periodo": "febrero a marzo de 2026",
    "mejora_porcentual": 22.58,
    "explicacion": "El tiempo medio de respuesta disminuyó de 3.1 a 2.4 horas, una reducción de 0.7 horas."
  },
  "tendencia_general_reportada": "Positiva en todas las métricas",
  "notas": [
    "El aumento de usuarios activos calculado con los valores visibles es 15.2473%, que redondeado directamente a un decimal es 15.2%; el dashboard reporta 15.3%.",
    "La mejora porcentual del churn es una reducción relativa; su cambio absoluto es de -0.7 puntos porcentuales.",
    "La reducción de tickets se considera favorable siguiendo la interpretación del dashboard.",
    "Las proyecciones son estimaciones mecánicas basadas en el último cambio mensual, no predicciones garantizadas."
  ]
}