# Qwen3-Coder-Next (OpenRouter FP8) — orchestration/tool_selection_precision

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 7.12 | quality: 5.85
- latency_total: 0.666s | tokens_per_second: 55.6
- input_tokens: 1408 | output_tokens: 37
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante para la tarea 1, usando una herramienta adecuada para verificar el estado del servidor, pero carece de profundidad y planificación detallada para las tareas restantes.

## Respuesta completa

[tool_call] http_request({"method": "GET", "url": "https://api.example.com/health"})