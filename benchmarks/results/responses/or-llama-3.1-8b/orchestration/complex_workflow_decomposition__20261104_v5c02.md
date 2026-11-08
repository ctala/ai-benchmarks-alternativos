# Llama 3.1 8B Instant — orchestration/complex_workflow_decomposition

- model_id: `meta-llama/llama-3.1-8b-instruct`
- success: True  | final: 6.33 | quality: 5.4
- latency_total: 2.628s | tokens_per_second: 138.1
- input_tokens: 1378 | output_tokens: 363
- judge_score: 3.0 | justificación: La respuesta descompone el proceso de manera adecuada, pero carece de detalles críticos como la gestión de errores y la verificación de la creación exitosa de la cuenta antes de proceder con pasos posteriores.

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

{"name": "send_email", "parameters": {"to": "andres@datapulse.cl", "subject": "Onboarding - Datos de cliente", "body": "Nombre: Andres Morales\nEmpresa: DataPulse SpA\nEmail: andres@datapulse.cl", "attachments": "[]; {"name": "http_request", "parameters": {"method": "POST", "url": "https://api.example.com/api/v1/accounts", "headers": "{'Content-Type': 'application/json'}", "body": '{"name": "Andres Morales", "company": "DataPulse SpA"}"}}; {"name": "query_database", "parameters": {"query": "SELECT * FROM api_keys WHERE account_id = (SELECT id FROM accounts WHERE name = 'Andres Morales')", "database": "customer_db"}}; {"name": "send_email", "parameters": {"to": "andres@datapulse.cl", "subject": "Bienvenida a nuestra plataforma", "body": "Hola Andres, bienvenido a nuestra plataforma. Tu API key es: [API KEY]", "attachments": "[]"}}; {"name": "create_calendar_event", "parameters": {"title": "Llamada de kickoff", "date": "2023-03-01T10:00:00", "duration_minutes": "60", "attendees": "['andres@datapulse.cl']"}}; {"name": "http_request", "parameters": {"method": "POST", "url": "https://slack.com/api/chat.postMessage", "headers": "{'Content-Type': 'application/json'}", "body": '{"channel": "#customer-success", "text": "Nuevo cliente onboarding: Andres Morales"}"}}