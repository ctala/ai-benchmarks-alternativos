# Llama 4 Maverick — agent_capabilities/skill_execution_complex

- model_id: `meta-llama/llama-4-maverick`
- success: True  | final: 7.43 | quality: 8.2
- latency_total: 7.177s | tokens_per_second: 19.8
- input_tokens: 1312 | output_tokens: 142
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, con un plan bien estructurado que un emprendedor podría usar directamente, aunque carece de profundidad adicional más allá de los pasos obvios.

## Respuesta completa

Mi plan es el siguiente:
1. Publicar el artículo usando el skill "publish_blog_post" con el contenido del documento compartido.
2. Buscar el link del artículo publicado en la base de conocimiento.
3. Enviar el link por Slack a @maria y @carlos usando "send_message".
4. Agendar una reunión de review para el jueves a las 3 PM con "create_calendar_event".

Primero, necesito confirmar si el artículo está listo en el doc compartido. 
[ask_human(question="¿Está listo el artículo sobre DeepSeek V4 en el doc compartido?", reason="Necesito confirmar que el artículo está listo antes de publicarlo")]