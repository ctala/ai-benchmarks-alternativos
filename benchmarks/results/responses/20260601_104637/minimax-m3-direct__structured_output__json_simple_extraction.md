# MiniMax M3 (directo / sub) — structured_output/json_simple_extraction

- model_id: `MiniMax-M3`
- success: True  | final: 7.9 | quality: 8.86
- latency_total: 5.861s | tokens_per_second: 23.2
- input_tokens: 267 | output_tokens: 136
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y en el formato correcto, con una utilidad práctica adecuada para un emprendedor.

## Respuesta completa

<think>
The user wants me to extract data from the text and return it as JSON. Let me parse the text:

- Name: Maria Garcia
- Age: 28
- Role: ingeniera de software (software engineer)
- Company: Google Chile
- Email: maria@google.com
- Salary: $95,000 USD → 95000

I need to return ONLY valid JSON, no markdown, no explanations.
</think>
{"name": "Maria Garcia", "age": 28, "role": "ingeniera de software", "company": "Google Chile", "email": "maria@google.com", "salary": 95000}