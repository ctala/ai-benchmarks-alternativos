# Hermes 4 70B — ocr_extraction/screenshot_table_extraction

- model_id: `nousresearch/hermes-4-70b`
- success: True  | final: 5.15 | quality: 4.0
- latency_total: 5.316s | tokens_per_second: 106.7
- input_tokens: 406 | output_tokens: 567
- judge_score: 2.0 | justificación: La respuesta incluye datos no presentes en la captura de pantalla original, como 'LTV', 'Active Users', 'Support Tickets', y 'Avg Response (h)', lo que afecta la precisión y relevancia; sin embargo, está bien organizada y clara.

## Respuesta completa

{
  "dashboard": "KPIs Marzo 2026",
  "metricas": [
    {
      "nombre": "MRR",
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "variacion": "7.0%"
    },
    {
      "nombre": "Churn Rate",
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "variacion": "-0.7pp"
    },
    {
      "nombre": "NPS",
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "variacion": 6
    },
    {
      "nombre": "CAC",
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "variacion": -11
    },
    {
      "nombre": "LTV",
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "variacion": 330
    },
    {
      "nombre": "Active Users",
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "variacion": "15.3%"
    },
    {
      "nombre": "Support Tickets",
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "variacion": "-17.1%"
    },
    {
      "nombre": "Avg Response (h)",
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "variacion": -0.7
    }
  ],
  "ltv_cac_ratio": {
    "enero": 8.09,
    "febrero": 10.15,
    "marzo": 12.49
  },
  "mejora_porcentual": {
    "metrica": "Active Users",
    "porcentaje": 15.3
  },
  "proyeccion_abril": {
    "MRR": 55800,
    "Churn Rate": 2.84,
    "NPS": 57,
    "CAC": 179,
    "LTV": 25740,
    "Active Users": 1933,
    "Support Tickets": 52,
    "Avg Response (h)": 2.16
  }
}