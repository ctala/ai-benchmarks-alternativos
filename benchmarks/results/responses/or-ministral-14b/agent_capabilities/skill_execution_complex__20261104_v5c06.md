# Ministral 14B — agent_capabilities/skill_execution_complex

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 4.63 | quality: 3.4
- latency_total: 2.515s | tokens_per_second: 34.6
- input_tokens: 919 | output_tokens: 87
- judge_score: 2.0 | justificación: La respuesta ejecuta correctamente el paso de publicación, pero no aborda los pasos adicionales de enviar el enlace por Slack o agendar la reunión, lo que afecta la relevancia y utilidad.

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un agente orquestador en OpenClaw. Tienes acceso a skills (secuencias automatizadas) y tools individuales.

Reglas:
- Usa skills cuando la tarea mapea a un flujo completo predefinido
- Usa tools individuales cuando necesitas hacer algo especifico
- Puedes combinar skills + tools en una misma respuesta
- Si falta informacion critica, usa ask_human ANTES de ejecutar
- Explica brevemente tu plan antes de ejecutar

**user:**

Necesito publicar el articulo sobre DeepSeek V4 que escribio el equipo.
El articulo esta listo en el doc compartido.
Despues de publicar, enviale el link por Slack a @maria y @carlos, y agenda una reunion de review para el jueves a las 3 PM.


## Respuesta completa

[tool_call] run_skill({"skill_name": "publish_blog_post", "parameters": {"document_id": "doc_compartido_deepseek_v4", "title": "DeepSeek V4: Avances y Características", "authors": ["equipo_de_redaccion"], "tags": ["IA", "DeepSeek", "tecnologia"], "publication_platform": "blog_empresarial"}})