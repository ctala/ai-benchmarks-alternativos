# MiMo-V2.5 Pro — ocr_extraction/screenshot_table_extraction

- model_id: `xiaomi/mimo-v2.5-pro`
- success: True  | final: 7.1 | quality: 8.0
- latency_total: 25.827s | tokens_per_second: 79.3
- input_tokens: 667 | output_tokens: 2048
- judge_score: 2.6 | justificación: 

## Respuesta completa

## Análisis Completo del Dashboard

```json
{
  "dashboard": {
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "tendencia_general": "Positiva en todas las métricas",
    "periodo": "Q1 2026"
  },

  "datos_extraidos": {
    "MRR": {
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "unidad": "USD",
      "variacion_m_m": "+7.0%"
    },
    "churn_rate": {
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "unidad": "porcentaje",
      "variacion_m_m": "-0.7pp"
    },
    "NPS": {
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "unidad": "puntos",
      "variacion_m_m": "+6"
    },
    "CAC": {
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "unidad": "USD",
      "variacion_m_m": "-$11"
    },
    "LTV": {
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "unidad": "USD",
      "variacion_m_m": "+$330"
    },
    "active_users": {
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "unidad": "usuarios",
      "variacion_m_m": "+15.3%"
    },
    "support_tickets": {
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "unidad": "tickets",
      "variacion_m_m": "-17.1%"
    },
    "avg_response_hours": {
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "unidad": "horas",
      "variacion_m_m": "-0.7h"
    }
  },

  "analisis_ltv_cac": {
    "descripcion": "Ratio LTV/CAC - indica retorno sobre inversión de adquisición. Un ratio > 3 se considera saludable.",
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
    "tendencia": "Mejora acelerada del ratio (+55% en el trimestre)",
    "interpretacion": "Excelente. El negocio es altamente rentable por cada $1 invertido en adquisición."
  },

  "metrica_mayor_mejora_porcentual": {
    "metrica": "Churn Rate",
    "cambio_enero_a_marzo": "-1.1pp (de 4.2% a 3.1%)",
    "mejora_porcentual": "-26.19%",
    "metodologia": "Se compararon todas las variaciones porcentuales absolutas de Enero→Marzo:",
    "ranking_mayor_a_menor": [
      { "posicion": 1, "metrica": "Churn Rate",        "cambio_pct": "-26.19%", "detalle": "4.2% → 3.1%" },
      { "posicion": 2, "metrica": "Avg Response (h)",   "cambio_pct": "-42.86%", "detalle": "4.2 → 2.4h (mejora absoluta)" },
      { "posicion": 3, "metrica": "Support Tickets",    "cambio_pct": "-29.21%", "detalle": "89 → 63" },
      { "posicion": 4, "metrica": "LTV",                "cambio_pct": "+23.81%", "detalle": "$1,890 → $2,340" },
      { "posicion": 5, "metrica": "Active Users",       "cambio_pct": "+35.98%", "detalle": "1,234 → 1,678" },
      { "posicion": 6, "metrica": "NPS",                "cambio_pct": "+21.43%", "detalle": "42 → 51" },
      { "posicion": 7, "metrica": "CAC",                "cambio_pct": "-20.09%", "detalle": "$234 → $187" },
      { "posicion": 8, "metrica