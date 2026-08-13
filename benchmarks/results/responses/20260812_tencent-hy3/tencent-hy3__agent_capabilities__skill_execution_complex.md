# Tencent Hy3 — agent_capabilities/skill_execution_complex

- model_id: `tencent/hy3`
- success: True  | final: 7.69 | quality: 8.4
- latency_total: 40.329s | tokens_per_second: 60.2
- input_tokens: 1092 | output_tokens: 2428
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, con un plan estructurado que un emprendedor podría usar, aunque carece de profundidad en detalles adicionales.

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

Plan breve antes de ejecutar:

1. **Publicar** el artículo de DeepSeek V4 con el skill `publish_blog_post` (requiere la referencia del doc).
2. **Enviar por Slack** el link resultante a `@maria` y `@carlos`.
3. **Agendar** la reunión de review el jueves a las 3 PM.

Sin embargo, me faltan datos críticos para ejecutar correctamente, así que los confirmo antes de empezar.