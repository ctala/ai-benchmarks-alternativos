# Devstral Medium — multi_turn/requirements_change

- model_id: `mistralai/devstral-medium`
- success: True  | final: 6.54 | quality: 6.96
- latency_total: 58.851s | tokens_per_second: 23.8
- input_tokens: 227 | output_tokens: 1399
- judge_score: 3.6 | justificación: 

## Respuesta completa

¡Entendido! Vamos a ajustar el workflow para que cumpla con tus nuevos requisitos. Aquí tienes los pasos detallados:

1. **Trigger**: Gmail Trigger (se activa con cada email nuevo)
2. **Filtrar**: IF node para filtrar emails con 'propuesta' o 'cotización' en el asunto
3. **Extraer datos**: Function node para parsear remitente, asunto, fecha
4. **Guardar en Notion**: Notion node para agregar una entrada
5. **Notificación en Slack**: Slack node para enviar una notificación

### Paso 1: Gmail Trigger

1. **Agrega un nodo Gmail Trigger**:
   - **Node Type**: Gmail Trigger
   - **Operation**: Watch Emails
   - **Configuration**: Configura las credenciales de Gmail y selecciona la carpeta de entrada (Inbox).

### Paso 2: Filtrar Emails

1. **Agrega un nodo IF**:
   - **Node Type**: IF
   - **Condition**: `{{ $json["subject"].toLowerCase().includes("propuesta") || $json["subject"].toLowerCase().includes("cotización") }}`

### Paso 3: Extraer Datos

1. **Agrega un nodo Function**:
   - **Node Type**: Function
   - **Code**:
     ```javascript
     return {
       from: item.from,
       subject: item.subject,
       date: item.date
     };
     ```

### Paso 4: Guardar en Notion

1. **Agrega un nodo Notion**:
   - **Node Type**: Notion
   - **Operation**: Append Block to Page
   - **Configuration**: Configura las credenciales de Notion y selecciona la página donde quieres agregar los datos.
   - **Fields**:
     - **Title**: `{{ $json["subject"] }}`
     - **Content**: `From: {{ $json["from"] }}\nDate: {{ $json["date"] }}`

### Paso 5: Notificación en Slack

1. **Agrega un nodo Slack**:
   - **Node Type**: Slack
   - **Operation**: Send Message
   - **Configuration**: Configura las credenciales de Slack y selecciona el canal donde quieres enviar la notificación.
   - **Message**: `Nuevo email recibido con el asunto: {{ $json["subject"] }}`

### Resumen del Workflow

1. **Gmail Trigger**: Se activa con cada email nuevo.
2. **IF Node**: Filtra los emails que contienen 'propuesta' o 'cotización' en el asunto.
3. **Function Node**: Extrae los datos del remitente, asunto y fecha.
4. **Notion Node**: Guarda los datos en una página de Notion.
5. **Slack Node**: Envía una notificación a Slack.

### Ejemplo de Configuración en n8n

```json
{
  "nodes": [
    {
      "parameters": {
        "operation": "watchEmails",
        "folder": "INBOX"
      },
      "name": "Gmail Trigger",
      "type": "n8n-nodes-base.gmail",
      "typeVersion": 1,
      "position": [240, 300]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json['subject'].toLowerCase() }}",
              "operation": "contains",
              "value2": "propuesta"
            },
            {
              "value1": "={{ $json['subject'].toLowerCase() }}",
              "operation": "contains",
              "value2": "cotización"
            }
          ]
        }
      },
      "name": "IF",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [440, 300]
    },
    {
      "parameters": {
        "functionCode": "return {\n  from: item.from,\n  subject: item.subject,\n  date: item.date\n};"
      },
      "name": "Function",
      "type": "n8n-nodes-base.function",
      "typeVersion": 1,
      "position": [640, 300]
    },
    {
      "parameters": {
        "operation": "appendBlockToPage",
        "pageId": "YOUR_PAGE_ID",
        "blocks": [
          {
            "type": "text",
            "text": "From: {{ $json['from'] }}\nDate: {{ $json['date'] }}"
          }
        ]
      },
      "name": "Notion",
      "type": "n8n-nodes-base.notion",
      "typeVersion": 1,
      "position": [840, 300]
    },
    {
      "parameters": {
        "channel": "YOUR_SLACK_CHANNEL",
        "text": "Nuevo email recibido con el asunto: {{ $json['subject'] }}"
      },
      "name": "Slack",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1040, 300]
    }
  ],
  "connections": {
    "Gmail Trigger": {
      "main": [
        [
          {
            "node": "IF",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IF": {
      "main": [
        [
          {
            "node": "Function",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Function": {
      "main": [
        [
          {
            "node": "Notion",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Notion": {
      "main": [
        [
          {
            "node": "Slack",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

Asegúrate de reemplazar `YOUR_PAGE_ID` y `YOUR_SLACK_CHANNEL` con los valores correspondientes de tu configuración de Notion y Slack.

¡Espero que esto te sea de ayuda! Si tienes alguna otra pregunta o necesitas más detalles, no dudes en preguntar.