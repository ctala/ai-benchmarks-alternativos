# Tencent Hy4 preview — agent_capabilities/skill_execution_complex

- model_id: `tencent/hy4-preview`
- success: True  | final: 7.25 | quality: 8.2
- latency_total: 17.629s | tokens_per_second: 48.4
- input_tokens: 1017 | output_tokens: 853
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, identificando pasos y datos faltantes, aunque carece de profundidad en la explicación de los pasos.

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

Voy a ejecutar este flujo en 3 pasos: **publicar** (skill `publish_blog_post`) → **enviar el link por Slack** a @maria y @carlos → **agendar** la reunion de review.

Antes de arrancar necesito dos datos que faltan:

- El enlace/identificador del doc compartido con el articulo (el skill de publicacion lo necesita como fuente).
- La fecha exacta del "jueves" (y zona horaria), para no agendar en un dia equivocado.