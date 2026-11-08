# Qwen 3-Next 80B Instruct — agent_capabilities/skill_execution_complex

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 8.5 | quality: 8.4
- latency_total: 1.514s | tokens_per_second: 144.6
- input_tokens: 1004 | output_tokens: 219
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, con una estructura lógica que un emprendedor podría usar directamente, aunque carece de profundidad adicional más allá de los pasos básicos.

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

Voy a organizar y ejecutar las tareas en orden:

1. **Publicar el artículo** – Como ya está listo y se trata de una tarea repetitiva (publicar un blog post), usaré el skill `publish_blog_post`.
2. **Enviar el link por Slack** – Una vez publicado, enviaré un mensaje a @maria y @carlos.
3. **Agendar reunión** – Crearé un evento en el calendario para el jueves a las 3 PM.

Para ejecutar el skill de publicación, necesito el link o nombre del documento donde está el artículo. Como no me lo proporcionaste, necesito aclararlo antes de continuar.

