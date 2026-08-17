# KAT Coder Air v2.5 — structured_output/json_simple_extraction

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 9.55 | quality: 10.0
- latency_total: 1.277s | tokens_per_second: 71.3
- input_tokens: 118 | output_tokens: 91

## Entrada exacta (lo que recibió el modelo)

**system:**

Responde SOLO con JSON valido, sin markdown, sin explicaciones.

**user:**

Extrae los datos de este texto en JSON:

"Maria Garcia, 28 anos, ingeniera de software. Trabaja en Google Chile desde 2023. Email: maria@google.com. Salario: $95,000 USD."

Formato: {"name": "", "age": 0, "role": "", "company": "", "email": "", "salary": 0}


## Respuesta completa



```json
{
  "name": "Maria Garcia",
  "age": 28,
  "role": "ingeniera de software",
  "company": "Google Chile",
  "email": "maria@google.com",
  "salary": 95000
}
```