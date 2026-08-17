# Kimi K2.6 — ocr_extraction/screenshot_table_extraction

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 7.05 | quality: 8.0
- latency_total: 31.146s | tokens_per_second: 174.6
- input_tokens: 386 | output_tokens: 5437
- judge_score: 3.0 | justificación: La respuesta incluye datos no presentes en la captura de pantalla original, afectando la precisión y relevancia, pero ofrece un análisis y proyecciones útiles con claridad.

## Respuesta completa

```json
{
  "dashboard": "DASHBOARD - KPIs Marzo 2026",
  "datos_extraidos": {
    "periodos": ["Enero", "Febrero", "Marzo"],
    "metricas": [
      {"nombre": "MRR", "unidad": "USD", "valores": [45200, 48700, 52100], "display": ["$45.2K", "$48.7K", "$52.1K"], "var_mom": "+7.0%"},
      {"nombre": "Churn Rate", "unidad": "%", "valores": [4.2, 3.8, 3.1], "display": ["4.2%", "3.8%", "3.1%"], "var_mom": "-0.7pp"},
      {"nombre": "NPS", "unidad": "puntos", "valores": [42, 45, 51], "display": ["42", "45", "51"], "var_mom": "+6"},
      {"nombre": "CAC", "unidad": "USD", "valores": [234, 198, 187], "display": ["$234", "$198", "$187"], "var_mom": "-$11"},
      {"nombre": "LTV", "unidad": "USD", "valores": [1890, 2010, 2340], "display": ["$1,890", "$2,010", "$2,340"], "var_mom": "+$330"},
      {"nombre": "Active Users", "unidad": "usuarios", "valores": [1234, 1456, 1678], "display": ["1,234", "1,456", "1,678"], "var_mom": "+15.3%"},
      {"nombre": "Support Tickets", "unidad": "tickets", "valores": [89, 76, 63], "display": ["89", "76", "63"], "var_mom": "-17.1%"},
      {"nombre": "Avg Response", "unidad": "horas", "valores": [4.2, 3.1, 2.4], "display": ["4.2", "3.1", "2.4"], "var_mom": "-0.7"}
    ]
  },
  "analisis": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "interpretacion": "Relación creciente; cada dólar invertido en adquisición genera 12.5x en valor de vida en marzo."
    },
    "metrica_mayor_mejora_porcentual": {
      "metrica": "Avg Response (h)",
      "mejora_marzo_vs_febrero": "-22.58%",
      "valor_febrero": 3.1,
      "valor_marzo": 2.4,
      "nota": "Mayor reducción proporcional respecto al mes anterior, superando a Churn Rate (-18.4%) y Support Tickets (-17.1%)."
    },
    "proyeccion_abril": {
      "metodologia": "Aplicación de la variación Mes/Mes (Marzo vs Febrero) sobre los valores de Marzo",
      "metricas": [
        {"nombre": "MRR", "valor": 55747, "display": "$55.7K"},
        {"nombre": "Churn Rate", "valor": 2.4, "display": "2.4%", "nota": "Resta de 0.7pp"},
        {"nombre": "NPS", "valor": 57, "display": "57"},
        {"nombre": "CAC", "valor": 176, "display": "$176"},
        {"nombre": "LTV", "valor": 2670, "display": "$2,670"},
        {"nombre": "Active Users", "valor": 1934, "display": "1,934"},
        {"nombre": "Support Tickets", "valor": 52, "display": "52"},
        {"nombre": "Avg Response", "valor": 1.7, "display": "1.7h"}
      ]
    }
  }
}
```