# Tencent Hy4 preview — orchestration/complex_workflow_decomposition

- model_id: `tencent/hy4-preview`
- success: True  | final: 6.25 | quality: 6.74
- latency_total: 26.961s | tokens_per_second: 64.4
- input_tokens: 1632 | output_tokens: 1735
- judge_score: 4.0 | justificación: La respuesta identifica correctamente las dependencias y datos faltantes, proporcionando un plan coherente para abordar el problema.

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

Antes de ejecutar, voy a hacer un reconocimiento del entorno. Tengo un problema: los 6 pasos requieren datos que no están en tu mensaje (URL base de la API, token de auth, webhook de Slack, fecha exacta del kickoff). Déjame ver qué puedo resolver solo.