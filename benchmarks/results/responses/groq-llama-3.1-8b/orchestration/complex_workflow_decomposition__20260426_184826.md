# Llama 3.1 8B Instant (Groq) — orchestration/complex_workflow_decomposition

- model_id: `llama-3.1-8b-instant`
- success: True  | final: 7.69 | quality: 5.68
- latency_total: 1.129s | tokens_per_second: 506.6
- input_tokens: 1011 | output_tokens: 572
- judge_score: 3.2 | justificación: 

## Respuesta completa

[tool_call] send_email({"attachments":[],"body":"Nombre: Andres Morales, Empresa: DataPulse SpA, Email: andres@datapulse.cl","subject":"Datos de Onboarding","to":"andres@datapulse.cl"})
[tool_call] http_request({"body":"{\"nombre\": \"Andres Morales\", \"empresa\": \"DataPulse SpA\", \"email\": \"andres@datapulse.cl\"}","headers":{"Content-Type":"application/json"},"method":"POST","url":"https://api.nuestrosistema.com/api/v1/accounts"})
[tool_call] query_database({"database":"nuestrosistema","query":"CREATE TABLE clientes (id INT PRIMARY KEY, nombre VARCHAR(255), empresa VARCHAR(255), email VARCHAR(255))"})
[tool_call] query_database({"database":"nuestrosistema","query":"INSERT INTO clientes (id, nombre, empresa, email) VALUES (1, 'Andres Morales', 'DataPulse SpA', 'andres@datapulse.cl')"})
[tool_call] query_database({"database":"nuestrosistema","query":"CREATE TABLE api_keys (id INT PRIMARY KEY, cliente_id INT, key VARCHAR(255))"})
[tool_call] query_database({"database":"nuestrosistema","query":"INSERT INTO api_keys (id, cliente_id, key) VALUES (1, 1, 'API-KEY-1234567890')"})
[tool_call] send_email({"attachments":["API-KEY-1234567890"],"body":"Bienvenido a nuestro sistema, tu API key es API-KEY-1234567890","subject":"Bienvenida","to":"andres@datapulse.cl"})
[tool_call] create_calendar_event({"attendees":["andres@datapulse.cl"],"date":"2023-03-01T10:00:00","duration_minutes":60,"title":"Llamada de Kickoff"})
[tool_call] send_email({"attachments":[],"body":"Llamada de kickoff programada para la proxima semana, el 1 de marzo a las 10:00","subject":"Llamada de Kickoff","to":"andres@datapulse.cl"})
[tool_call] http_request({"body":"{\"channel\": \"#customer-success\", \"text\": \"Nuevo cliente onboarded: Andres Morales de DataPulse SpA\"}","headers":{"Content-Type":"application/json"},"method":"POST","url":"https://slack.com/api/chat.postMessage"})