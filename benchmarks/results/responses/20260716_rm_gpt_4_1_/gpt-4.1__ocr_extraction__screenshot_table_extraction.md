# GPT-4.1 — ocr_extraction/screenshot_table_extraction

- model_id: `gpt-4.1`
- success: True  | final: 7.36 | quality: 8.0
- latency_total: 5.086s | tokens_per_second: 121.1
- input_tokens: 380 | output_tokens: 616
- judge_score: 4.2 | justificación: 

## Respuesta completa

```json
{
  "data": {
    "Enero": {
      "MRR": 45200,
      "Churn Rate": 0.042,
      "NPS": 42,
      "CAC": 234,
      "LTV": 1890,
      "Active Users": 1234,
      "Support Tickets": 89,
      "Avg Response (h)": 4.2
    },
    "Febrero": {
      "MRR": 48700,
      "Churn Rate": 0.038,
      "NPS": 45,
      "CAC": 198,
      "LTV": 2010,
      "Active Users": 1456,
      "Support Tickets": 76,
      "Avg Response (h)": 3.1
    },
    "Marzo": {
      "MRR": 52100,
      "Churn Rate": 0.031,
      "NPS": 51,
      "CAC": 187,
      "LTV": 2340,
      "Active Users": 1678,
      "Support Tickets": 63,
      "Avg Response (h)": 2.4
    }
  },
  "LTV_CAC_Ratio": {
    "Enero": 8.08,
    "Febrero": 10.15,
    "Marzo": 12.52
  },
  "max_improvement_metric": {
    "metric": "Active Users",
    "percentage_change": 15.3,
    "description": "Mayor mejora porcentual mensual (de febrero a marzo)"
  },
  "projection_Abril": {
    "MRR": 55747,                 // +7.0% sobre marzo
    "Churn Rate": 0.024,          // -0.7pp sobre marzo (0.031 - 0.007)
    "NPS": 57,                    // +6 sobre marzo
    "CAC": 176,                   // -$11 sobre marzo (187 - 11)
    "LTV": 2670,                  // +$330 sobre marzo (2340 + 330)
    "Active Users": 1936,         // +15.3% sobre marzo (1678 * 1.153)
    "Support Tickets": 52,        // -17.1% sobre marzo (63 * 0.829)
    "Avg Response (h)": 1.7       // -0.7 sobre marzo (2.4 - 0.7)
  }
}
```

**Notas:**
- Todas las proyecciones de abril aplican el mismo cambio absoluto o porcentual reportado de febrero a marzo.
- El ratio LTV/CAC se calcula dividiendo LTV entre CAC para cada mes, redondeado a dos decimales.
- La métrica con mayor mejora porcentual es "Active Users" (+15.3%).