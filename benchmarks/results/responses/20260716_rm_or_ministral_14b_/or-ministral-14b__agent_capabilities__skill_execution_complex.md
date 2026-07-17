# Ministral 14B — agent_capabilities/skill_execution_complex

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 4.89 | quality: 3.13
- latency_total: 0.959s | tokens_per_second: 52.2
- input_tokens: 919 | output_tokens: 50
- judge_score: 2.0 | justificación: La respuesta solo ejecuta un paso del proceso requerido, omitiendo la comunicación por Slack y la programación de la reunión, lo que la hace parcialmente relevante y útil.

## Respuesta completa

[tool_call] run_skill({"skill_name": "publish_blog_post", "parameters": {"document_id": "doc_compartido_deepseek_v4", "author": "equipo", "title": "DeepSeek V4"}})