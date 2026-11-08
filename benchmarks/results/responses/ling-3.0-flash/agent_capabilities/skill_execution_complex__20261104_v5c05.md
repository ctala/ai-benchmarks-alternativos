# Ling 3.0 Flash — agent_capabilities/skill_execution_complex

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 4.97 | quality: 4.0
- latency_total: 12.173s | tokens_per_second: 73.9
- input_tokens: 1204 | output_tokens: 900
- judge_score: 2.0 | justificación: La respuesta no aborda directamente la tarea de publicar el artículo, enviar el enlace por Slack, ni agendar la reunión, lo que resulta en baja relevancia y utilidad práctica.

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

Voy a gestionar esta tarea en varios pasos. Primero, déjame buscar información sobre el artículo de DeepSeek V4 en la base de conocimiento, y al mismo tiempo necesito aclarar algunos detalles.