# Grok 4.7 — ocr_extraction/screenshot_table_extraction

- model_id: `x-ai/grok-4.7`
- success: True  | final: 6.87 | quality: 8.0
- latency_total: 33.392s | tokens_per_second: 94.5
- input_tokens: 1602 | output_tokens: 3156

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
  "periodo": "Marzo 2026",
  "fuente": "dashboard_kpis",
  "metricas": [
    {
      "metrica": "MRR",
      "unidad": "USD_K",
      "enero": 45.2,
      "febrero": 48.7,
      "marzo": 52.1,
      "var_m_m": "+7.0%",
      "direccion_favorable": "alza"
    },
    {
      "metrica": "Churn Rate",
      "unidad": "porcentaje",
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "var_m_m": "-0.7pp",
      "direccion_favorable": "baja"
    },
    {
      "metrica": "NPS",
      "unidad": "puntos",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "var_m_m": "+6",
      "direccion_favorable": "alza"
    },
    {
      "metrica": "CAC",
      "unidad": "USD",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "var_m_m": "-$11",
      "direccion_favorable": "baja"
    },
    {
      "metrica": "LTV",
      "unidad": "USD",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "var_m_m": "+$330",
      "direccion_favorable": "alza"
    },
    {
      "metrica": "Active Users",
      "unidad": "usuarios",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "var_m_m": "+15.3%",
      "direccion_favorable": "alza"
    },
    {
      "metrica": "Support Tickets",
      "unidad": "tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "var_m_m": "-17.1%",
      "direccion_favorable": "baja"
    },
    {
      "metrica": "Avg Response",
      "unidad": "horas",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "var_m_m": "-0.7",
      "direccion_favorable": "baja"
    }
  ],
  "ltv_cac_ratio": {
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51,
    "detalle": {
      "enero": "1890 / 234",
      "febrero": "2010 / 198",
      "marzo": "2340 / 187"
    }
  },
  "mayor_mejora_porcentual": {
    "criterio": "mayor cambio favorable feb→mar, en valor absoluto del porcentaje",
    "metrica": "Avg Response",
    "cambio_bruto_feb_mar": "-22.6%",
    "mejora_porcentual": 22.6,
    "calculo": "(2.4 - 3.1) / 3.1",
    "ranking_mejora_feb_mar": [
      {"metrica": "Avg Response", "mejora_pct": 22.6},
      {"metrica": "Churn Rate", "mejora_pct": 18.4},
      {"metrica": "Support Tickets", "mejora_pct": 17.1},
      {"metrica": "LTV", "mejora_pct": 16.4},
      {"metrica": "Active Users", "mejora_pct": 15.3},
      {"metrica": "NPS", "mejora_pct": 13.3},
      {"metrica": "MRR", "mejora_pct": 7.0},
      {"metrica": "CAC", "mejora_pct": 5.6}
    ]
  },
  "proyeccion_abril": {
    "metodo": "se aplica a marzo la tasa de cambio feb→mar",
    "valores": {
      "MRR_USD_K": 55.7,
      "Churn_Rate_pct": 2.53,
      "NPS": 57.8,
      "CAC_USD": 177,
      "LTV_USD": 2724,
      "Active_Users": 1934,
      "Support_Tickets": 52,
      "Avg_Response_h": 1.86,
      "LTV_CAC_ratio": 15.42
    },
    "tasas_aplicadas_feb_mar": {
      "MRR": 1.0698,
      "Churn Rate": 0.8158,
      "NPS": 1.1333,
      "CAC": 0.9444,
      "LTV": 1.1642,
      "Active Users": 1.1525,
      "Support Tickets": 0.8289,
      "Avg Response": 0.7742
    }
  },
  "tendencia_general": "positiva"
}
```