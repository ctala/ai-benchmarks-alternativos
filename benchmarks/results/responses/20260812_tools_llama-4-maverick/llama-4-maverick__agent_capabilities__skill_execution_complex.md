# Llama 4 Maverick — agent_capabilities/skill_execution_complex

- model_id: `meta-llama/llama-4-maverick`
- success: True  | final: 8.04 | quality: 8.2
- latency_total: 2.186s | tokens_per_second: 77.3
- input_tokens: 1216 | output_tokens: 169
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, con un plan bien estructurado, aunque carece de profundidad en la ejecución de los pasos.

## Respuesta completa

Mi plan es el siguiente:

1. Usar el skill "publish_blog_post" para publicar el artículo.
2. Buscar el link del artículo publicado.
3. Enviar el link por Slack a @maria y @carlos usando "send_message".
4. Crear un evento en el calendario para la reunión de review usando "create_calendar_event".

Primero, necesito saber el título y el contenido del artículo. Como está en un doc compartido, asumiré que puedo acceder a él. Sin embargo, para asegurarme, voy a pedir confirmación sobre el título y si hay alguna instrucción específica para la publicación.

[ask_human(question='¿Cuál es el título del artículo sobre DeepSeek V4 y hay alguna instrucción específica para su publicación?', reason='Necesito confirmar los detalles del artículo antes de publicarlo')]