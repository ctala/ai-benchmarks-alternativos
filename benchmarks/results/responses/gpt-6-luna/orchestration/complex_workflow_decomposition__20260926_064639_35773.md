# GPT-6 Luna — orchestration/complex_workflow_decomposition

- model_id: `openai/gpt-6-luna`
- success: True  | final: 7.2 | quality: 7.0
- latency_total: 5.087s | tokens_per_second: 118.7
- input_tokens: 519 | output_tokens: 604
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, identificando claramente los datos faltantes necesarios para proceder, con una estructura clara y útil para un emprendedor.

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

No puedo iniciar el proceso con seguridad porque faltan datos necesarios para los primeros pasos. **No he creado la cuenta ni he enviado correos o invitaciones.**

Por favor, compárteme:

- La URL base y la autenticación de la API para `POST /api/v1/accounts`.
- El método o endpoint para generar la API key.
- La fecha y hora de la llamada de kickoff la próxima semana, su duración y los asistentes.
- El canal de Slack o una integración disponible para notificar a Customer Success.

Con esos datos podré continuar en el orden indicado.