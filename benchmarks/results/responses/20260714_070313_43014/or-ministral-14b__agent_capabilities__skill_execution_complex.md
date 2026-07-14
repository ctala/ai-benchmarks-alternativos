# Ministral 14B — agent_capabilities/skill_execution_complex

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 4.91 | quality: 3.37
- latency_total: 1.224s | tokens_per_second: 62.9
- input_tokens: 919 | output_tokens: 77
- judge_score: 2.0 | justificación: La respuesta ejecuta correctamente la publicación del artículo, pero no aborda los pasos adicionales de enviar el enlace por Slack o agendar la reunión, lo que afecta la relevancia y utilidad.

## Respuesta completa

[tool_call] run_skill({"skill_name": "publish_blog_post", "parameters": {"document_id": "doc_compartido_deepseek_v4", "title": "Artículo sobre DeepSeek V4", "authors": ["equipo"], "tags": ["IA", "DeepSeek", "tecnología"], "publication_date": "hoy"}})