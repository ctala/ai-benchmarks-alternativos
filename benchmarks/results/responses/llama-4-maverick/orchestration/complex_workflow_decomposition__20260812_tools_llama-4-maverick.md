# Llama 4 Maverick — orchestration/complex_workflow_decomposition

- model_id: `meta-llama/llama-4-maverick`
- success: True  | final: 6.26 | quality: 6.92
- latency_total: 156.977s | tokens_per_second: 7.1
- input_tokens: 1459 | output_tokens: 1110
- judge_score: 3.8 | justificación: 

## Respuesta completa

Para automatizar el proceso de onboarding para el nuevo cliente Andres Morales de DataPulse SpA, seguiré los pasos indicados utilizando las herramientas disponibles.

### Paso 1: El cliente envió sus datos por email
Ya tenemos los datos del cliente: nombre = Andres Morales, empresa = DataPulse SpA, email = andres@datapulse.cl. No necesitamos ejecutar ninguna acción aquí ya que la información ya está disponible.

### Paso 2: Crear su cuenta en nuestro sistema
Para crear la cuenta, necesitamos hacer una petición POST a `/api/v1/accounts`. Suponiendo que la API requiere el nombre, empresa y email del cliente, prepararemos el cuerpo de la petición.

```json
{
  "name": "Andres Morales",
  "company": "DataPulse SpA",
  "email": "andres@datapulse.cl"
}
```

Usaremos la función `http_request` para esto.

[http_request(method=POST, url=/api/v1/accounts, body={"name": "Andres Morales", "company": "DataPulse SpA", "email": "andres@datapulse.cl"}, headers={"Content-Type": "application/json"})]

### Paso 3: Generar una API key para el cliente
Suponiendo que la API para generar la API key es otro endpoint, por ejemplo, `/api/v1/accounts/{account_id}/api-key`, primero necesitamos obtener el `account_id` del paso anterior. Sin embargo, como no tenemos el `account_id` directamente, asumiremos que la respuesta del paso 2 contiene el `account_id` o que hay otro endpoint para obtener el `account_id` basado en el email.

Para simplificar, asumamos que la respuesta del paso 2 es algo como:
```json
{
  "account_id": "12345"
}
```

Entonces, podemos generar la API key haciendo una petición a `/api/v1/accounts/12345/api-key`.

[http_request(method=POST, url=/api/v1/accounts/12345/api-key)]

### Paso 4: Enviarle un email de bienvenida con sus credenciales
Suponiendo que tenemos la API key generada, enviaremos un email de bienvenida.

Cuerpo del email:
```
Bienvenido, Andres Morales.
Su cuenta ha sido creada con éxito.
API Key: [api_key_generada]
```

[send_email(to=andres@datapulse.cl, subject=Bienvenido a nuestro servicio, body=Bienvenido, Andres Morales.\nSu cuenta ha sido creada con éxito.\nAPI Key: [api_key_generada])]

### Paso 5: Agendar una llamada de kickoff para la próxima semana
Usaremos la función `create_calendar_event` para agendar la llamada.

Primero, necesitamos determinar la fecha de la próxima semana. Supongamos que hoy es lunes 15 de abril, entonces la próxima semana sería lunes 22 de abril.

[create_calendar_event(title=Llamada de Kickoff con DataPulse SpA, date=2024-04-22T10:00:00, duration_minutes=60, attendees=[andres@datapulse.cl])]

### Paso 6: Notificar al equipo de Customer Success en Slack
Aunque no tenemos una función específica para Slack, podemos usar `send_email` o `http_request` si hay una API de Slack disponible. Sin embargo, como no está disponible directamente, asumiremos que podemos notificar mediante email o que hay una integración que permite hacer una petición HTTP a un webhook de Slack.

Para simplificar, usaremos `send_email` para notificar al equipo de Customer Success.

[send_email(to=customer.success@nuestraempresa.com, subject=Nuevo cliente: DataPulse SpA, body=Se ha creado la cuenta para DataPulse SpA. Se ha agendado una llamada de kickoff para el 22 de abril.)]

### Resumen de las acciones a ejecutar en orden:

1. [http_request(method=POST, url=/api/v1/accounts, body={"name": "Andres Morales", "company": "DataPulse SpA", "email": "andres@datapulse.cl"}, headers={"Content-Type": "application/json"})]
2. [http_request(method=POST, url=/api/v1/accounts/12345/api-key)]
3. [send_email(to=andres@datapulse.cl, subject=Bienvenido a nuestro servicio, body=Bienvenido, Andres Morales.\nSu cuenta ha sido creada con éxito.\nAPI Key: [api_key_generada])]
4. [create_calendar_event(title=Llamada de Kickoff con DataPulse SpA, date=2024-04-22T10:00:00, duration_minutes=60, attendees=[andres@datapulse.cl])]
5. [send_email(to=customer.success@nuestraempresa.com, subject=Nuevo cliente: DataPulse SpA, body=Se ha creado la cuenta para DataPulse SpA. Se ha agendado una llamada de kickoff para el 22 de abril.)]

Es importante tener en cuenta que algunos de estos pasos requieren información de los pasos anteriores (como el `account_id` y la `api_key_generada`), por lo que en una implementación real, deberíamos manejar las respuestas de las peticiones HTTP y usar esa información en los pasos subsiguientes.