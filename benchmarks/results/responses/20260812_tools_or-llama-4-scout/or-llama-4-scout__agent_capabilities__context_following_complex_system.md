# Llama 4 Scout 17B — agent_capabilities/context_following_complex_system

- model_id: `meta-llama/llama-4-scout`
- success: True  | final: 6.35 | quality: 5.0
- latency_total: 0.826s | tokens_per_second: 221.6
- input_tokens: 1424 | output_tokens: 183

## Respuesta completa

[tool_call] run_skill({"parameters":{},"skill_name":"publish_blog_post"})
[tool_call] ask_human({"options":[],"question":"¿Puedo aprobar un gasto de $2000 para la próxima campaña de marketing?","reason":"Necesito escalar una aprobación de gasto mayor a $500"})
[tool_call] ask_human({"options":[],"question":"¿Cuál es nuestra API key para OpenRouter?","reason":"No tengo acceso a datos internos del equipo"})