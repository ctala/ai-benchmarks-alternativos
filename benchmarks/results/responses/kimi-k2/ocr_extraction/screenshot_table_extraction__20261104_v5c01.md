# Kimi K2 — ocr_extraction/screenshot_table_extraction

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 8.51 | quality: 10.0
- latency_total: 25.87s | tokens_per_second: 45.9
- input_tokens: 387 | output_tokens: 1187

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
  "datos_extraidos": {
    "dashboard": "KPIs Marzo 2026",
    "metricas": [
      {
        "nombre": "MRR",
        "unidad": "$",
        "enero": 45200,
        "febrero": 48700,
        "marzo": 52100,
        "var_mm": "+7.0%"
      },
      {
        "nombre": "Churn Rate",
        "unidad": "%",
        "enero": 4.2,
        "febrero": 3.8,
        "marzo": 3.1,
        "var_mm": "-0.7pp"
      },
      {
        "nombre": "NPS",
        "unidad": "puntos",
        "enero": 42,
        "febrero": 45,
        "marzo": 51,
        "var_mm": "+6"
      },
      {
        "nombre": "CAC",
        "unidad": "$",
        "enero": 234,
        "febrero": 198,
        "marzo": 187,
        "var_mm": "-$11"
      },
      {
        "nombre": "LTV",
        "unidad": "$",
        "enero": 1890,
        "febrero": 2010,
        "marzo": 2340,
        "var_mm": "+$330"
      },
      {
        "nombre": "Active Users",
        "unidad": "usuarios",
        "enero": 1234,
        "febrero": 1456,
        "marzo": 1678,
        "var_mm": "+15.3%"
      },
      {
        "nombre": "Support Tickets",
        "unidad": "tickets",
        "enero": 89,
        "febrero": 76,
        "marzo": 63,
        "var_mm": "-17.1%"
      },
      {
        "nombre": "Avg Response",
        "unidad": "horas",
        "enero": 4.2,
        "febrero": 3.1,
        "marzo": 2.4,
        "var_mm": "-0.7"
      }
    ]
  },
  "analisis_ltv_cac_ratio": {
    "descripcion": "LTV/CAC ratio indica cuántos dólares de valor vitalicio se generan por cada dólar invertido en adquisición. Ratio saludable: >3:1",
    "valores": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51
    },
    "interpretacion": "Excelente tendencia. El ratio mejoró de 8.08 a 12.51, indicando eficiencia creciente en adquisición de clientes."
  },
  "metrica_mayor_mejora": {
    "nombre": "Support Tickets",
    "mejora_porcentual": -29.2,
    "calculo": "(63 - 89) / 89 * 100 = -29.2% (reducción de tickets)",
    "nota": "Si se considera mejora absoluta en puntos porcentuales: Churn Rate (-1.1pp de Enero a Marzo)"
  },
  "proyeccion_abril": {
    "metodologia": "Aplicar la tendencia de crecimiento/decrecimiento observada entre Febrero y Marzo (mes más reciente)",
    "valores_proyectados": {
      "MRR": {
        "valor": 55747,
        "formato": "$55.7K",
        "logica": "Crecimiento +7.0% sobre Marzo"
      },
      "Churn Rate": {
        "valor": 2.4,
        "formato": "2.4%",
        "logica": "Reducción de -0.7pp (tendencia reciente)"
      },
      "NPS": {
        "valor": 57,
        "formato": "57 puntos",
        "logica": "Incremento de +6 puntos"
      },
      "CAC": {
        "valor": 176,
        "formato": "$176",
        "logica": "Reducción de -$11"
      },
      "LTV": {
        "valor": 2670,
        "formato": "$2,670",
        "logica": "Incremento de +$330"
      },
      "Active Users": {
        "valor": 1935,
        "formato": "1,935 usuarios",
        "logica": "Crecimiento +15.3% sobre Marzo"
      },
      "Support Tickets": {
        "valor": 52,
        "formato": "52 tickets",
        "logica": "Reducción -17.1% sobre Marzo"
      },
      "Avg Response": {
        "valor": 1.7,
        "formato": "1.7 horas",
        "logica": "Reducción -0.7 horas"
      }
    },
    "ltv_cac_ratio_proyectado": 15.17,
    "resumen": "Proyección optimista con LTV/CAC de 15.17, indicando mes excepcional si se mantiene la tendencia"
  }
}
```