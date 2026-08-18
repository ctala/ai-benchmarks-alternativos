# Gemini 3.7 Flash — structured_output/json_simple_extraction

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 9.3 | quality: 10.0
- latency_total: 3.168s | tokens_per_second: 122.1
- input_tokens: 103 | output_tokens: 387

## Entrada exacta (lo que recibió el modelo)

**system:**

Responde SOLO con JSON valido, sin markdown, sin explicaciones.

**user:**

Extrae los datos de este texto en JSON:

"Maria Garcia, 28 anos, ingeniera de software. Trabaja en Google Chile desde 2023. Email: maria@google.com. Salario: $95,000 USD."

Formato: {"name": "", "age": 0, "role": "", "company": "", "email": "", "salary": 0}


## Respuesta completa

{"name": "Maria Garcia", "age": 28, "role": "ingeniera de software", "company": "Google Chile", "email": "maria@google.com", "salary": 95000}