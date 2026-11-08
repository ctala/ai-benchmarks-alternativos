# Claude Sonnet 5.5 — ocr_extraction/screenshot_table_extraction

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 6.88 | quality: 8.0
- latency_total: 26.678s | tokens_per_second: 162.9
- input_tokens: 514 | output_tokens: 4345

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
  "nota_fuente": "Datos tomados del texto que pegaste; no veo la imagen. Verifica contra la captura original.",
  "datos": [
    {"metrica": "MRR", "unidad": "USD", "enero": 45200, "febrero": 48700, "marzo": 52100, "var_mm_reportada": "+7.0%", "var_mm_calculada": "+6.98%", "mejor_direccion": "subir"},
    {"metrica": "Churn Rate", "unidad": "%", "enero": 4.2, "febrero": 3.8, "marzo": 3.1, "var_mm_reportada": "-0.7pp", "var_mm_calculada": "-0.7pp", "mejor_direccion": "bajar"},
    {"metrica": "NPS", "unidad": "puntos", "enero": 42, "febrero": 45, "marzo": 51, "var_mm_reportada": "+6", "var_mm_calculada": "+6", "mejor_direccion": "subir"},
    {"metrica": "CAC", "unidad": "USD", "enero": 234, "febrero": 198, "marzo": 187, "var_mm_reportada": "-$11", "var_mm_calculada": "-$11", "mejor_direccion": "bajar"},
    {"metrica": "LTV", "unidad": "USD", "enero": 1890, "febrero": 2010, "marzo": 2340, "var_mm_reportada": "+$330", "var_mm_calculada": "+$330", "mejor_direccion": "subir"},
    {"metrica": "Active Users", "unidad": "usuarios", "enero": 1234, "febrero": 1456, "marzo": 1678, "var_mm_reportada": "+15.3%", "var_mm_calculada": "+15.25%", "mejor_direccion": "subir"},
    {"metrica": "Support Tickets", "unidad": "tickets", "enero": 89, "febrero": 76, "marzo": 63, "var_mm_reportada": "-17.1%", "var_mm_calculada": "-17.11%", "mejor_direccion": "bajar"},
    {"metrica": "Avg Response", "unidad": "horas", "enero": 4.2, "febrero": 3.1, "marzo": 2.4, "var_mm_reportada": "-0.7", "var_mm_calculada": "-0.7", "mejor_direccion": "bajar"}
  ],
  "validacion": "Las variaciones M/M reportadas coinciden con las calculadas (diferencias solo por redondeo).",

  "1_ltv_cac_ratio": {
    "formula": "LTV / CAC",
    "enero":   {"ltv": 1890, "cac": 234, "ratio": 8.08},
    "febrero": {"ltv": 2010, "cac": 198, "ratio": 10.15},
    "marzo":   {"ltv": 2340, "cac": 187, "ratio": 12.51},
    "tendencia": "+54.9% de enero a marzo",
    "lectura": "Muy por encima del benchmark de 3x. Es saludable, aunque un ratio tan alto puede indicar subinversión en adquisición."
  },

  "2_mayor_mejora_porcentual": {
    "criterio": "Cambio porcentual en la dirección favorable de cada métrica",
    "ranking_enero_a_marzo": [
      {"metrica": "Avg Response", "cambio": "-42.86%"},
      {"metrica": "Active Users", "cambio": "+35.98%"},
      {"metrica": "Support Tickets", "cambio": "-29.21%"},
      {"metrica": "Churn Rate", "cambio": "-26.19%"},
      {"metrica": "LTV", "cambio": "+23.81%"},
      {"metrica": "NPS", "cambio": "+21.43%"},
      {"metrica": "CAC", "cambio": "-20.09%"},
      {"metrica": "MRR", "cambio": "+15.27%"}
    ],
    "ranking_febrero_a_marzo": [
      {"metrica": "Avg Response", "cambio": "-22.58%"},
      {"metrica": "Churn Rate", "cambio": "-18.42%"},
      {"metrica": "Support Tickets", "cambio": "-17.11%"},
      {"metrica": "LTV", "cambio": "+16.42%"},
      {"metrica": "Active Users", "cambio": "+15.25%"},
      {"metrica": "NPS", "cambio": "+13.33%"},
      {"metrica": "MRR", "cambio": "+6.98%"},
      {"metrica": "CAC", "cambio": "-5.56%"}
    ],
    "ganadora": "Avg Response (tiempo de respuesta)",
    "detalle": "Es la mayor mejora tanto en el acumulado (-42.86%) como en el M/M (-22.58%). Si solo cuentas crecimientos positivos, la mayor es Active Users (+35.98% acumulado)."
  },

  "3_proyeccion_abril": {
    "supuesto": "Con solo 3 puntos de datos, la proyección es orientativa.",
    "metodo_a_lineal": "Cambio promedio mensual absoluto (Ene→Mar)/2",
    "metodo_b_geometrico": "Tasa compuesta mensual = raíz cuadrada de (Mar/Ene)",
    "valores": [
      {"metrica": "MRR", "lineal": 55550, "geometrico": 55930},
      {"metrica": "Churn Rate (%)", "lineal": 2.55, "geometrico": 2.66},
      {"metrica": "NPS", "lineal": 55.5, "geometrico": 56.2},
      {"metrica": "CAC (USD)", "lineal": 163.5, "geometrico": 167.2},
      {"metrica": "LTV (USD)", "lineal": 2565, "geometrico": 2604},
      {"metrica": "Active Users", "lineal": 1900, "geometrico": 1957},
      {"metrica": "Support Tickets", "lineal": 50, "geometrico": 53},
      {"metrica": "Avg Response (h)", "lineal": 1.5, "geometrico": 1.81},
      {"metrica": "LTV/CAC", "lineal": 15.69, "geometrico": 15.57}
    ],
    "rango_recomendado": "Usa el rango entre ambos métodos. Es más prudente el geométrico en las métricas que bajan, porque la caída se desacelera al acercarse a un piso.",
    "advertencias": [
      "Churn, CAC, tickets y tiempo de respuesta tienen pisos naturales; la mejora difícilmente se mantendrá lineal.",
      "NPS tiene techo en 100.",
      "Con 3 meses no hay estacionalidad ni intervalo de confianza fiable.",
      "Un LTV calculado con churn decreciente puede estar inflado, porque LTV depende del churn y ambos mejoran juntos."
    ]
  },

  "conclusion": "Las 8 métricas mejoran, lo que confirma la tendencia positiva. LTV/CAC pasa de 8.08 a 12.51. La mayor mejora porcentual es el tiempo de respuesta. Para abril se proyecta un MRR de unos $55.5K–55.9K y un LTV/CAC de unos 15.6–15.7."
}
```

Si quieres, puedo ajustar la proyección con otro método (por ejemplo, regresión con más meses de histórico) o con la imagen original si me das los valores exactos.