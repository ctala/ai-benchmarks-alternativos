# MiMo V2.6 Flash — agent_capabilities/skill_execution_complex

- model_id: `xiaomi/mimo-v2.6-flash`
- success: True  | final: 5.09 | quality: 4.4
- latency_total: 11.503s | tokens_per_second: 31.6
- input_tokens: 966 | output_tokens: 364
- judge_score: 2.0 | justificación: La respuesta reconoce la necesidad de datos adicionales, pero no proporciona una acción concreta o solución para completar la tarea, lo que la hace parcialmente relevante y útil.

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

Voy a ejecutar el skill de publicación de blog, luego enlaces por Slack y crear el evento. Pero antes necesito datos críticos que no me diste.