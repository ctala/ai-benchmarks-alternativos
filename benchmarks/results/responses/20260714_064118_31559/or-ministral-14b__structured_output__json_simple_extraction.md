# Ministral 14B — structured_output/json_simple_extraction

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 6.05 | quality: 5.0
- latency_total: 1.195s | tokens_per_second: 81.2
- input_tokens: 109 | output_tokens: 97
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con una estructura clara y un formato JSON válido, aunque la profundidad es solo aceptable al agregar detalles no solicitados como la ubicación y el año de inicio.

## Respuesta completa

```json
{
  "name": "Maria Garcia",
  "age": 28,
  "role": "ingeniera de software",
  "company": {
    "name": "Google",
    "location": "Chile",
    "start_year": 2023
  },
  "email": "maria@google.com",
  "salary": 95000,
  "salary_currency": "USD"
}
```