# Llama 3.1 8B Instant (Groq) — multi_turn/requirements_change

- model_id: `llama-3.1-8b-instant`
- success: True  | final: 7.06 | quality: 6.04
- latency_total: 1.497s | tokens_per_second: 424.8
- input_tokens: 268 | output_tokens: 636
- judge_score: 3.0 | justificación: 

## Respuesta completa

Entendido, ahora el workflow será un poco más complejo. Aquí te explico los pasos:

1. **Trigger**: Gmail Trigger (se activa con cada email nuevo)
2. **Filtro**: Function node para filtrar emails que tengan la palabra 'propuesta' o 'cotizacion' en el asunto
3. **Extraer datos**: Function node para parsear remitente, asunto, fecha
4. **Notificar**: Slack Node para enviar notificación cuando llegue un email que cumpla con el filtro
5. **Guardar**: Notion Node para agregar un nuevo elemento en Notion

Configuración de cada nodo:

1. **Trigger**: Configura el trigger para leer los correos electrónicos de tu cuenta de Gmail. Asegúrate de habilitar el acceso a la cuenta de Gmail en la configuración de N8N.
2. **Filtro**: Utiliza la función `contains()` para filtrar los emails que tengan la palabra 'propuesta' o 'cotizacion' en el asunto. Puedes configurar el nodo de la siguiente manera:

```javascript
const filtro = {
  "subject": {
    "contains": ["propuesta", "cotizacion"]
  }
};
return filtro;
```

3. **Extraer datos**: Utiliza la función `parseEmail()` para extraer los datos del remitente, asunto y fecha. Puedes configurar el nodo de la siguiente manera:

```javascript
const datos = {
  "nombre": message.payload.headers.sender.name,
  "email": message.payload.headers.sender.email,
  "asunto": message.payload.headers.subject,
  "fecha": message.payload.headers.date
};
return datos;
```

4. **Notificar**: Configura el nodo de Slack para enviar una notificación cuando llegue un email que cumpla con el filtro. Asegúrate de habilitar el acceso a la cuenta de Slack en la configuración de N8N.

```javascript
return {
  "type": "slack",
  "channel": "general",
  "message": "Llegó una nueva propuesta o cotización de: " + datos.nombre + " - " + datos.email
};
```

5. **Guardar**: Configura el nodo de Notion para agregar un nuevo elemento en Notion. Asegúrate de habilitar el acceso a la cuenta de Notion en la configuración de N8N.

```javascript
return {
  "database_id": "tu-id-de-biblioteca-de-notion",
  "properties": {
    "nombre": datos.nombre,
    "email": datos.email,
    "asunto": datos.asunto,
    "fecha": datos.fecha
  }
};
```

Recuerda reemplazar `tu-id-de-biblioteca-de-notion` con el ID de tu biblioteca de Notion.

Espero que esto te ayude a configurar el workflow. Recuerda que debes ajustar los nodos según tus necesidades y configuraciones específicas.