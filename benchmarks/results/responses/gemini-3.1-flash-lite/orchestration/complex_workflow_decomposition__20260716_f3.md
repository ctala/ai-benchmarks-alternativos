# Gemini 3.1 Flash Lite — orchestration/complex_workflow_decomposition

- model_id: `google/gemini-3.1-flash-lite-preview`
- success: True  | final: 4.94 | quality: 3.51
- latency_total: 1.048s | tokens_per_second: 59.2
- input_tokens: 847 | output_tokens: 62
- judge_score: 2.0 | justificación: La respuesta ejecuta solo el primer paso de la creación de la cuenta, sin abordar los pasos restantes del proceso de onboarding, lo que resulta en una cobertura incompleta y falta de profundidad.

## Respuesta completa

[tool_call] http_request({"body":"{\"name\": \"Andres Morales\", \"company\": \"DataPulse SpA\", \"email\": \"andres@datapulse.cl\"}","method":"POST","url":"/api/v1/accounts"})