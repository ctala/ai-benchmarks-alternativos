# Fugu Max — orchestration/complex_workflow_decomposition

- model_id: `sakana/fugu-max`
- success: True  | final: 7.7 | quality: 8.6
- latency_total: 7.563s | tokens_per_second: 64.3
- input_tokens: 592 | output_tokens: 486
- judge_score: 5 | justificación: La respuesta identifica con precisión los datos faltantes necesarios para completar el proceso de onboarding, proporcionando una descomposición clara y detallada de cada paso, lo que es altamente útil para un emprendedor.

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

No puedo ejecutar el onboarding todavía porque faltan datos necesarios para completar los pasos de forma segura y en orden:

1. **Crear la cuenta:** URL completa del endpoint (por ejemplo, `https://.../api/v1/accounts`), método de autenticación y esquema del payload.
2. **Generar la API key:** endpoint o procedimiento exacto para generarla.
3. **Email de bienvenida:** dirección remitente y formato deseado de las credenciales.
4. **Llamada de kickoff:** fecha y hora de la próxima semana, zona horaria, duración y asistentes.
5. **Slack:** canal de Customer Success y webhook o endpoint autorizado para publicar el mensaje.

Con esos datos podré crear la cuenta, generar la clave, enviar el email, agendar la llamada y notificar al equipo en ese orden.