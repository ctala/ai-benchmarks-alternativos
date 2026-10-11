# Bonsai 2 27B — agent_capabilities/skill_execution_complex

- model_id: `prism-ml/ternary-bonsai-2-27b`
- success: True  | final: 5.52 | quality: 5.48
- latency_total: 53.071s | tokens_per_second: 43.2
- input_tokens: 952 | output_tokens: 2293
- judge_score: 2.2 | justificación: 

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



Plan: (1) buscar el artículo en la base de conocimiento, (2) publicarlo con el skill de publicación, (3) enviar el link por Slack a @maria y @carlos, (4) agendar la reunión del jueves a las 3 PM.

Voy a buscar el artículo ahora y, a la vez, confirmar la fecha de la reunión:


