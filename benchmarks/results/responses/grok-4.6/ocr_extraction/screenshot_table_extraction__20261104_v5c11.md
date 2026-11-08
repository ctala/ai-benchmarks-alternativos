# Grok 4.6 — ocr_extraction/screenshot_table_extraction

- model_id: `x-ai/grok-4.6`
- success: True  | final: 6.99 | quality: 8.0
- latency_total: 39.177s | tokens_per_second: 102.7
- input_tokens: 566 | output_tokens: 4025

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
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "tendencia_general": "Positiva en todas las metricas",
    "metricas": [
      {
        "metrica": "MRR",
        "enero": 45200,
        "febrero": 48700,
        "marzo": 52100,
        "var_mm": 0.07,
        "unidad": "USD",
        "direccion_deseada": "subida"
      },
      {
        "metrica": "Churn Rate",
        "enero": 0.042,
        "febrero": 0.038,
        "marzo": 0.031,
        "var_mm_pp": -0.7,
        "unidad": "ratio",
        "direccion_deseada": "bajada"
      },
      {
        "metrica": "NPS",
        "enero": 42,
        "febrero": 45,
        "marzo": 51,
        "var_mm": 6,
        "unidad": "puntos",
        "direccion_deseada": "subida"
      },
      {
        "metrica": "CAC",
        "enero": 234,
        "febrero": 198,
        "marzo": 187,
        "var_mm": -11,
        "unidad": "USD",
        "direccion_deseada": "bajada"
      },
      {
        "metrica": "LTV",
        "enero": 1890,
        "febrero": 2010,
        "marzo": 2340,
        "var_mm": 330,
        "unidad": "USD",
        "direccion_deseada": "subida"
      },
      {
        "metrica": "Active Users",
        "enero": 1234,
        "febrero": 1456,
        "marzo": 1678,
        "var_mm": 0.153,
        "unidad": "usuarios",
        "direccion_deseada": "subida"
      },
      {
        "metrica": "Support Tickets",
        "enero": 89,
        "febrero": 76,
        "marzo": 63,
        "var_mm": -0.171,
        "unidad": "tickets",
        "direccion_deseada": "bajada"
      },
      {
        "metrica": "Avg Response (h)",
        "enero": 4.2,
        "febrero": 3.1,
        "marzo": 2.4,
        "var_mm": -0.7,
        "unidad": "horas",
        "direccion_deseada": "bajada"
      }
    ]
  },
  "ltv_cac_ratio": {
    "metodo": "LTV / CAC",
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51,
    "detalle": {
      "enero": { "ltv": 1890, "cac": 234, "ratio": 8.0769 },
      "febrero": { "ltv": 2010, "cac": 198, "ratio": 10.1515 },
      "marzo": { "ltv": 2340, "cac": 187, "ratio": 12.5134 }
    },
    "interpretacion": "El ratio mejora de ~8.1x a ~12.5x; umbral saludable habitual >= 3x"
  },
  "mayor_mejora_porcentual": {
    "criterio": "Mayor |cambio %| MoM (feb->mar) en la direccion deseada",
    "metrica": "Avg Response (h)",
    "cambio_mom_pct": -0.2258,
    "mejora_pct": 0.2258,
    "detalle": "De 3.1h a 2.4h (-22.58%)",
    "ranking_mom_mejora_pct": [
      { "metrica": "Avg Response (h)", "mejora_pct": 0.2258, "cambio": "3.1 -> 2.4" },
      { "metrica": "Churn Rate", "mejora_pct": 0.1842, "cambio": "3.8% -> 3.1%" },
      { "metrica": "Support Tickets", "mejora_pct": 0.1711, "cambio": "76 -> 63" },
      { "metrica": "LTV", "mejora_pct": 0.1642, "cambio": "2010 -> 2340" },
      { "metrica": "Active Users", "mejora_pct": 0.1525, "cambio": "1456 -> 1678" },
      { "metrica": "NPS", "mejora_pct": 0.1333, "cambio": "45 -> 51" },
      { "metrica": "MRR", "mejora_pct": 0.0698, "cambio": "48.7K -> 52.1K" },
      { "metrica": "CAC", "mejora_pct": 0.0556, "cambio": "198 -> 187" }
    ],
    "nota_ene_mar": {
      "metrica_mayor_ene_mar": "Avg Response (h)",
      "mejora_pct": 0.4286,
      "cambio": "4.2h -> 2.4h (-42.86%)",
      "segunda": { "metrica": "Active Users", "mejora_pct": 0.3598 }
    }
  },
  "proyeccion_abril": {
    "metodo": "Se mantiene el delta/tasa MoM de febrero->marzo aplicado a marzo",
    "valores": {
      "MRR": { "valor": 55747, "formato": "$55.7K", "regla": "x1.07" },
      "Churn Rate": { "valor": 0.024, "formato": "2.4%", "regla": "-0.7pp" },
      "NPS": { "valor": 57, "formato": "57", "regla": "+6 pts" },
      "CAC": { "valor": 176, "formato": "$176", "regla": "-$11" },
      "LTV": { "valor": 2670, "formato": "$2,670", "regla": "+$330" },
      "Active Users": { "valor": 1935, "formato": "1,935", "regla": "x1.153" },
      "Support Tickets": { "valor": 52, "formato": "52", "regla": "x(1-0.171)" },
      "Avg Response (h)": { "valor": 1.7, "formato": "1.7h", "regla": "-0.7h" }
    },
    "ltv_cac_abril_proyectado": 15.17,
    "supuestos_y_limites": [
      "Extrapolacion lineal/constante del ultimo MoM; no modela saturacion ni estacionalidad",
      "Churn 2.4% y respuesta 1.7h pueden no ser sostenibles al mismo ritmo absoluto",
      "CAC no puede bajar indefinidamente; LTV/CAC 15x seria excepcional",
      "Active Users 1935 asume el mismo % de crecimiento (+15.3%)"
    ],
    "alternativa_lineal_ene_mar": {
      "descripcion": "Pendiente media entre enero y marzo (2 pasos) aplicada un mes mas",
      "MRR": 55550,
      "Churn Rate": 0.0255,
      "NPS": 55.5,
      "CAC": 163.5,
      "LTV": 2565,
      "Active Users": 1900,
      "Support Tickets": 50,
      "Avg Response (h)": 1.5
    }
  }
}
```