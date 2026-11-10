# Claude Fable 5.2 — ocr_extraction/screenshot_table_extraction

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 6.61 | quality: 8.0
- latency_total: 37.653s | tokens_per_second: 115.2
- input_tokens: 514 | output_tokens: 4336

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
  "dashboard": {
    "titulo": "KPIs Marzo 2026",
    "tendencia_general": "Positiva en todas las metricas",
    "metricas": [
      { "nombre": "MRR", "unidad": "USD (miles)", "enero": 45.2, "febrero": 48.7, "marzo": 52.1, "var_mm": "+7.0%" },
      { "nombre": "Churn Rate", "unidad": "%", "enero": 4.2, "febrero": 3.8, "marzo": 3.1, "var_mm": "-0.7pp" },
      { "nombre": "NPS", "unidad": "puntos", "enero": 42, "febrero": 45, "marzo": 51, "var_mm": "+6" },
      { "nombre": "CAC", "unidad": "USD", "enero": 234, "febrero": 198, "marzo": 187, "var_mm": "-$11" },
      { "nombre": "LTV", "unidad": "USD", "enero": 1890, "febrero": 2010, "marzo": 2340, "var_mm": "+$330" },
      { "nombre": "Active Users", "unidad": "usuarios", "enero": 1234, "febrero": 1456, "marzo": 1678, "var_mm": "+15.3%" },
      { "nombre": "Support Tickets", "unidad": "tickets", "enero": 89, "febrero": 76, "marzo": 63, "var_mm": "-17.1%" },
      { "nombre": "Avg Response", "unidad": "horas", "enero": 4.2, "febrero": 3.1, "marzo": 2.4, "var_mm": "-0.7" }
    ]
  },
  "analisis": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "variacion_feb_a_mar_pct": 23.27,
      "variacion_ene_a_mar_pct": 54.93
    },
    "mayor_mejora_porcentual": {
      "metrica": "Avg Response (h)",
      "mejora_feb_a_mar_pct": -22.58,
      "mejora_ene_a_mar_pct": -42.86,
      "detalle": "El tiempo de respuesta bajo de 3.1h a 2.4h en marzo (-22.58%) y de 4.2h a 2.4h en el trimestre (-42.86%). Es la mayor mejora relativa en ambos periodos.",
      "ranking_feb_a_mar": [
        { "metrica": "Avg Response", "cambio_pct": -22.58 },
        { "metrica": "Churn Rate", "cambio_pct": -18.42 },
        { "metrica": "Support Tickets", "cambio_pct": -17.11 },
        { "metrica": "LTV", "cambio_pct": 16.42 },
        { "metrica": "Active Users", "cambio_pct": 15.25 },
        { "metrica": "NPS", "cambio_pct": 13.33 },
        { "metrica": "MRR", "cambio_pct": 6.98 },
        { "metrica": "CAC", "cambio_pct": -5.56 }
      ],
      "ranking_ene_a_mar": [
        { "metrica": "Avg Response", "cambio_pct": -42.86 },
        { "metrica": "Active Users", "cambio_pct": 35.98 },
        { "metrica": "Support Tickets", "cambio_pct": -29.21 },
        { "metrica": "Churn Rate", "cambio_pct": -26.19 },
        { "metrica": "LTV", "cambio_pct": 23.81 },
        { "metrica": "NPS", "cambio_pct": 21.43 },
        { "metrica": "CAC", "cambio_pct": -20.09 },
        { "metrica": "MRR", "cambio_pct": 15.27 }
      ]
    },
    "proyeccion_abril": {
      "metodo_principal": "Lineal: Marzo + cambio mensual promedio de Enero a Marzo",
      "metodo_alternativo": "Tasa constante: se repite la variacion porcentual de Febrero a Marzo",
      "metricas": [
        { "nombre": "MRR (USD miles)", "lineal": 55.55, "tasa_constante": 55.74 },
        { "nombre": "Churn Rate (%)", "lineal": 2.55, "tasa_constante": 2.53 },
        { "nombre": "NPS", "lineal": 55.5, "tasa_constante": 57.8 },
        { "nombre": "CAC (USD)", "lineal": 163.5, "tasa_constante": 176.61 },
        { "nombre": "LTV (USD)", "lineal": 2565, "tasa_constante": 2724.18 },
        { "nombre": "Active Users", "lineal": 1900, "tasa_constante": 1934 },
        { "nombre": "Support Tickets", "lineal": 50, "tasa_constante": 52 },
        { "nombre": "Avg Response (h)", "lineal": 1.5, "tasa_constante": 1.86 },
        { "nombre": "LTV/CAC ratio", "lineal": 15.69, "tasa_constante": 15.42 }
      ]
    }
  },
  "notas": [
    "Las variaciones porcentuales estan recalculadas a partir de los valores de la tabla; un signo negativo es mejora en Churn, CAC, Support Tickets y Avg Response.",
    "Active Users: la variacion recalculada es +15.25% (222/1456), que redondea a +15.2% y no al +15.3% que muestra el dashboard; puede deberse a redondeo en el origen.",
    "La proyeccion se basa en solo 3 puntos de datos, por lo que es una estimacion orientativa y no un pronostico estadistico."
  ]
}
```