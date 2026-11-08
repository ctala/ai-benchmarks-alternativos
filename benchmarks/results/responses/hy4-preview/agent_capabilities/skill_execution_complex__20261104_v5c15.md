# Tencent Hy4 preview — agent_capabilities/skill_execution_complex

- model_id: `tencent/hy4-preview`
- success: True  | final: 4.75 | quality: 4.34
- latency_total: 7.539s | tokens_per_second: 39.4
- input_tokens: 1017 | output_tokens: 297
- judge_score: 2.0 | justificación: La respuesta no sigue los pasos especificados, como publicar el artículo y enviar el enlace por Slack, y en su lugar sugiere buscar el artículo en la base de conocimiento, lo cual no es relevante para la tarea.

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

Voy a buscar primero el artículo en la base de conocimiento para identificar el documento antes de publicar.