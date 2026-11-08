# Kimi K2.7 Code — agent_capabilities/skill_execution_complex

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 7.26 | quality: 8.0
- latency_total: 12.463s | tokens_per_second: 57.9
- input_tokens: 667 | output_tokens: 721
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, solicitando información necesaria para completar la tarea, y está claramente organizada, lo que la hace práctica para un emprendedor.

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

Necesito aclarar algunos datos clave antes de ejecutar, ya que no tengo acceso directo al documento compartido ni a la fecha actual:

1. **URL del documento**: ¿Cuál es el link del doc compartido con el artículo de DeepSeek V4?
2. **Fecha del jueves**: ¿A qué fecha exacta corresponde el jueves a las 3 PM?
3. **Slack**: ¿Son mensajes directos (DM) a @maria y @carlos, o a un canal? En caso de ser DM, ¿tienes sus handles completos o emails?

Una vez me confirmes estos datos, ejecuto:
- `publish_blog_post` con el contenido del doc
- `send_message` por Slack con el link publicado
- `create_calendar_event` para la reunión de review.