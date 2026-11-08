# Tencent Hy4 — orchestration/complex_workflow_decomposition

- model_id: `tencent/hy4`
- success: True  | final: 7.54 | quality: 8.4
- latency_total: 26.98s | tokens_per_second: 78.1
- input_tokens: 1063 | output_tokens: 2106
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una buena planificación que incluye una fase de descubrimiento para abordar la falta de información, lo que es útil para un emprendedor.

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un agente orquestador experto en automatizacion.
Descompone tareas complejas en pasos atomicos ejecutables.
Usa las herramientas disponibles para ejecutar cada paso.

**user:**

Automatiza este proceso de onboarding para un nuevo cliente:

1. El cliente envio sus datos por email (nombre: Andres Morales, empresa: DataPulse SpA, email: andres@datapulse.cl)
2. Hay que crear su cuenta en nuestro sistema (API endpoint: POST /api/v1/accounts)
3. Generar una API key para el
4. Enviarle un email de bienvenida con sus credenciales
5. Agendar una llamada de kickoff para la proxima semana
6. Notificar al equipo de Customer Success en Slack

Ejecuta los pasos en orden. Para cada paso, usa la herramienta apropiada.


## Respuesta completa

Voy a descomponer el flujo en pasos atómicos. Antes de ejecutar acciones con efectos externos (crear cuenta, enviar email, agendar, publicar en Slack), hago una **fase de descubrimiento** para obtener los datos que el enunciado no proporciona (URL base de la API, endpoint de API keys, canal/webhook de Slack, política de entrega de credenciales y fecha actual).