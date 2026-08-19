# KAT Coder Air v2.5 — ocr_extraction/screenshot_table_extraction

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 8.97 | quality: 10.0
- latency_total: 10.444s | tokens_per_second: 196.1
- input_tokens: 427 | output_tokens: 2048

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
    "periodo": "Enero - Marzo 2026",
    "tendencia_general": "↑ Positiva en todas las métricas"
  },
  "kpis_raw": [
    {
      "metrica": "MRR",
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "var_m_m": "+7.0%"
    },
    {
      "metrica": "Churn Rate",
      "enero": "4.2%",
      "febrero": "3.8%",
      "marzo": "3.1%",
      "var_m_m": "-0.7pp"
    },
    {
      "metrica": "NPS",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "var_m_m": "+6"
    },
    {
      "metrica": "CAC",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "var_m_m": "-$11"
    },
    {
      "metrica": "LTV",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "var_m_m": "+$330"
    },
    {
      "metrica": "Active Users",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "var_m_m": "+15.3%"
    },
    {
      "metrica": "Support Tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "var_m_m": "-17.1%"
    },
    {
      "metrica": "Avg Response (h)",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "var_m_m": "-0.7"
    }
  ],
  "ltv_cac_ratio": {
    "enero": {
      "ltv": 1890,
      "cac": 234,
      "ratio": 8.08
    },
    "febrero": {
      "ltv": 2010,
      "cac": 198,
      "ratio": 10.15
    },
    "marzo": {
      "ltv": 2340,
      "cac": 187,
      "ratio": 12.51
    },
    "tendencia": "↑ Creciente: la eficiencia de adquisición mejora mes a mes",
    "var_m_m": "+23.2%"
  },
  "mayor_mejora_porcentual": {
    "metrica": "Avg Response Time",
    "mejora_relativa": "-22.6%",
    "detalle": "De 3.1h a 2.4h (reducción de 0.7h sobre base de 3.1h)",
    "nota": "Aunque Support Tickets también tuvo -17.1%, la mejora relativa en tiempo de respuesta es mayor"
  },
  "proyeccion_abril": {
    "metodo": "Tendencia M/M conservadora (misma variación absoluta o porcentual del último mes)",
    "kpis": [
      {
        "metrica": "MRR",
        "marzo": 52100,
        "abril_proyectado": 55747,
        "var_estimada": "+7.0%"
      },
      {
        "metrica": "Churn Rate",
        "marzo": "3.1%",
        "abril_proyectado": "2.4%",
        "var_estimada": "-0.7pp"
      },
      {
        "metrica": "NPS",
        "marzo": 51,
        "abril_proyectado": 57,
        "var_estimada": "+6"
      },
      {
        "metrica": "CAC",
        "marzo": 187,
        "abril_proyectado": 176,
        "var_estimada": "-$11"
      },
      {
        "metrica": "LTV",
        "marzo": 2340,
        "abril_proyectado": 2670,
        "var_estimada": "+$330"
      },
      {
        "metrica": "Active Users",
        "marzo": 1678,
        "abril_proyectado": 1939,
        "var_estimada": "+15.3%"
      },
      {
        "metrica": "Support Tickets",
        "marzo": 63,
        "abril_proyectado": 52,
        "var_estimada": "-17.1%"
      },
      {
        "metrica": "Avg Response (h)",
        "marzo": 2.4,
        "abril_proyectado": 1.7,
        "var_estimada": "-0.7h"
      }
    ],
    "ltv_cac_ratio_proyectado": {
      "abril": {
        "ltv": 2670,
        "cac": 176,
        "ratio": 15.17
      },
      "observacion": "Ratio LTV/CAC superaría 15x, muy por encima del benchmark saludable de 3x"
    }
  },
  "