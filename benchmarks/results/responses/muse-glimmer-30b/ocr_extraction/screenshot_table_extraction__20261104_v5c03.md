# Muse Glimmer 30B — ocr_extraction/screenshot_table_extraction

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 7.27 | quality: 8.0
- latency_total: 22.431s | tokens_per_second: 177.3
- input_tokens: 411 | output_tokens: 3976

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
  "dashboard_title": "DASHBOARD - KPIs Marzo 2026",
  "tendencia_general": "↑ Positiva en todas las metricas",
  "periodos": ["Enero", "Feb", "Marzo"],
  "metricas": [
    {
      "nombre": "MRR",
      "unidad": "K USD",
      "Enero": 45.2,
      "Feb": 48.7,
      "Marzo": 52.1,
      "var_m_m": "+7.0%"
    },
    {
      "nombre": "Churn Rate",
      "unidad": "%",
      "Enero": 4.2,
      "Feb": 3.8,
      "Marzo": 3.1,
      "var_m_m": "-0.7pp"
    },
    {
      "nombre": "NPS",
      "unidad": "puntos",
      "Enero": 42,
      "Feb": 45,
      "Marzo": 51,
      "var_m_m": "+6"
    },
    {
      "nombre": "CAC",
      "unidad": "USD",
      "Enero": 234,
      "Feb": 198,
      "Marzo": 187,
      "var_m_m": "-$11"
    },
    {
      "nombre": "LTV",
      "unidad": "USD",
      "Enero": 1890,
      "Feb": 2010,
      "Marzo": 2340,
      "var_m_m": "+$330"
    },
    {
      "nombre": "Active Users",
      "unidad": "usuarios",
      "Enero": 1234,
      "Feb": 1456,
      "Marzo": 1678,
      "var_m_m": "+15.3%"
    },
    {
      "nombre": "Support Tickets",
      "unidad": "tickets",
      "Enero": 89,
      "Feb": 76,
      "Marzo": 63,
      "var_m_m": "-17.1%"
    },
    {
      "nombre": "Avg Response (h)",
      "unidad": "horas",
      "Enero": 4.2,
      "Feb": 3.1,
      "Marzo": 2.4,
      "var_m_m": "-0.7"
    }
  ],
  "analisis": {
    "ltv_cac_ratio": {
      "Enero": 8.08,
      "Feb": 10.15,
      "Marzo": 12.51
    },
    "metrica_mayor_mejora_porcentual": {
      "criterio": "Ene-Mar acumulada",
      "nombre": "Avg Response (h)",
      "tipo": "reduccion",
      "cambio_ene_mar_pct": -42.86,
      "cambio_mensual_feb_mar_pct": -22.58,
      "nota": "Mayor mejora en magnitud. Si se consideran solo mejoras positivas, Active Users +35.98% Ene-Mar y +15.3% M/M"
    },
    "proyeccion_abril_tendencia_constante": {
      "metodo": "Mantener misma variacion M/M de Feb-Mar: % para metricas porcentuales y cambio absoluto para pp / puntos / $ / horas",
      "MRR": 55.75,
      "Churn Rate": 2.4,
      "NPS": 57,
      "CAC": 176,
      "LTV": 2670,
      "Active Users": 1935,
      "Support Tickets": 52,
      "Avg Response (h)": 1.7
    }
  }
}
```

* LTV/CAC = LTV / CAC. Enero 1890/234 = 8.08, Feb 2010/198 = 10.15, Marzo 2340/187 = 12.51.
* Mayor mejora porcentual acumulada Ene-Mar es Avg Response (h) con -42.86% de reducción, 22.58% M/M Feb-Mar.
* Proyección Abril aplica la misma variación M/M observada en Marzo: +7.0% MRR, -0.7pp Churn, +6 NPS, -$11 CAC, +$330 LTV, +15.3% Active Users, -17.1% Support Tickets, -0.7h Avg Response.