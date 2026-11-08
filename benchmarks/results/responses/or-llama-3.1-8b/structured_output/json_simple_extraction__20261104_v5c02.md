# Llama 3.1 8B Instant — structured_output/json_simple_extraction

- model_id: `meta-llama/llama-3.1-8b-instruct`
- success: True  | final: 9.7 | quality: 10.0
- latency_total: 0.597s | tokens_per_second: 92.1
- input_tokens: 112 | output_tokens: 55

## Entrada exacta (lo que recibió el modelo)

**system:**

Responde SOLO con JSON valido, sin markdown, sin explicaciones.

**user:**

Extrae los datos de este texto en JSON:

"Maria Garcia, 28 anos, ingeniera de software. Trabaja en Google Chile desde 2023. Email: maria@google.com. Salario: $95,000 USD."

Formato: {"name": "", "age": 0, "role": "", "company": "", "email": "", "salary": 0}


## Respuesta completa

{
  "name": "Maria Garcia",
  "age": 28,
  "role": "ingeniera de software",
  "company": "Google Chile",
  "email": "maria@google.com",
  "salary": 95000
}