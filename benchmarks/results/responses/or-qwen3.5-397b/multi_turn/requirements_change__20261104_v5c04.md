# Qwen 3.5 397B — multi_turn/requirements_change

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 7.0 | quality: 8.0
- latency_total: 52.349s | tokens_per_second: 60.7
- input_tokens: 233 | output_tokens: 3177

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un asistente tecnico para emprendedores que trabajan con N8N.

**user:**

Necesito un workflow en N8N que lea emails de Gmail, extraiga los datos del remitente, y los guarde en un Google Sheet.

**assistant:**

Perfecto, ese workflow es bastante directo. Te explico los pasos:

1. **Trigger**: Gmail Trigger (se activa con cada email nuevo)
2. **Extraer datos**: Function node para parsear remitente, asunto, fecha
3. **Guardar**: Google Sheets node para agregar una fila

Los campos a extraer serian: nombre del remitente, email, asunto, fecha. Quieres que te detalle la configuracion de cada nodo?

**user:**

En realidad, cambio de idea. No quiero Google Sheets, quiero que los datos vayan a Notion. Ademas, quiero que el workflow filtre solo los emails que tengan la palabra 'propuesta' o 'cotizacion' en el asunto. Y que me mande una notificacion a Slack cuando llegue uno.


## Respuesta completa

¡Excelente ajuste! Esa combinación (Gmail + Notion + Slack) es muy potente para gestionar leads o oportunidades comerciales sin perder nada en una hoja de cálculo aburrida.

Aquí tienes la estructura detallada del workflow y los puntos clave de configuración para que funcione perfectamente:

### 🏗️ Estructura del Workflow

1.  **Gmail Trigger:** Escucha nuevos emails.
2.  **IF (Filtro):** Verifica si el asunto contiene 'propuesta' O 'cotización'.
3.  **Notion:** Crea una página en tu base de datos con los datos del email.
4.  **Slack:** Envía un mensaje al canal informado.

---

### ⚙️ Configuración Paso a Paso

#### 1. Gmail Trigger Node
*   **Event:** `New Email` (o `New Email Matching Search` si quieres filtrar antes, pero lo haremos en el IF para mayor control).
*   **Credentials:** Conecta tu cuenta de Google (OAuth2).
*   **Limit:** Pon `1` o `5` para pruebas.
*   **Download Attachments:** `false` (a menos que necesites los adjuntos).

#### 2. IF Node (El Filtro)
Este es el cerebro del flujo. Usaremos una expresión para validar el asunto.
*   **Condition:** `String` -> `Contains` (o expresión personalizada).
*   **Expresión recomendada (Case Insensitive):**
    ```javascript
    {{ $json.subject.toLowerCase().includes('propuesta') || $json.subject.toLowerCase().includes('cotizacion') }}
    ```
*   **Ruta True:** Conecta hacia Notion.
*   **Ruta False:** Déjala vacía (el workflow termina aquí si no coincide).

#### 3. Notion Node
*   **Resource:** `Page`
*   **Operation:** `Create`
*   **Database ID:** Necesitas el ID de la base de datos donde se guardarán los leads.
    *   *Tip:* Ve a tu DB en Notion, mira la URL, el ID es la cadena de caracteres después de `/` y antes de `?`.
*   **Properties (Mapeo):**
    *   **Name (Title):** `{{ $json.from }}` (o un campo personalizado).
    *   **Email:** `{{ $json.email }}` (Asegúrate de tener una propiedad tipo "Email" en Notion).
    *   **Subject:** `{{ $json.subject }}` (Propiedad tipo "Text").
    *   **Date:** `{{ $json.date }}` (Propiedad tipo "Date").
    *   **Link:** `{{ $json.messageId }}` o un link directo a Gmail.

#### 4. Slack Node
*   **Resource:** `Message`
*   **Operation:** `Post`
*   **Channel:** Selecciona el canal (ej. `#ventas` o `#leads`).
*   **Text:**
    ```text
    🚨 Nueva Oportunidad Detectada
    *De:* {{ $json.from }}
    *Asunto:* {{ $json.subject }}
    *Fecha:* {{ $json.date }}
    _Revisar en Notion para detalles_
    ```

---

### 📋 Código JSON para Importar
Puedes copiar este código, ir a tu N8N, hacer `Ctrl+V` (o importar desde URL) y solo tendrás que configurar las credenciales.

```json
{
  "name": "Gmail a Notion + Slack (Propuestas)",
  "nodes": [
    {
      "parameters": {
        "event": "messageAdded",
        "limit": 5
      },
      "id": "gmail-trigger",
      "name": "Gmail Trigger",
      "type": "n8n-nodes-base.gmailTrigger",
      "typeVersion": 1,
      "position": [250, 300],
      "credentials": {
        "gmailOAuth2": {
          "id": "TU_CREDENTIAL_ID_GMAIL",
          "name": "Gmail account"
        }
      }
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.subject.toLowerCase() }}",
              "operation": "contains",
              "value2": "propuesta"
            },
            {
              "value1": "={{ $json.subject.toLowerCase() }}",
              "operation": "contains",
              "value2": "cotizacion"
            }
          ],
          "combineConditions": "or"
        }
      },
      "id": "if-filter",
      "name": "Filtrar Asunto",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [450, 300]
    },
    {
      "parameters": {
        "databaseId": "TU_DATABASE_ID_NOTION",
        "properties": {
          "title": [
            {
              "key": "Nombre",
              "value": "={{ $json.from }}"
            }
          ],
          "text": [
            {
              "key": "Asunto",
              "value": "={{ $json.subject }}"
            }
          ],
          "email": [
            {
              "key": "Email",
              "value": "={{ $json.email }}"
            }
          ],
          "date": [
            {
              "key": "Fecha",
              "value": "={{ $json.date }}"
            }
          ]
        }
      },
      "id": "notion-create",
      "name": "Guardar en Notion",
      "type": "n8n-nodes-base.notion",
      "typeVersion": 1,
      "position": [650, 300],
      "credentials": {
        "notionApi": {
          "id": "TU_CREDENTIAL_ID_NOTION",
          "name": "Notion account"
        }
      }
    },
    {
      "parameters": {
        "channelId": "TU_CANAL_SLACK",
        "text": "🚨 *Nueva Propuesta/Cotización*\n*De:* {{ $json.from }}\n*Asunto:* {{ $json.subject }}\n*Email:* {{ $json.email }}"
      },
      "id": "slack-notify",
      "name": "Notificar Slack",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [850, 300],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENTIAL_ID_SLACK",
          "name": "Slack account"
        }
      }
    }
  ],
  "connections": {
    "Gmail Trigger": {
      "main": [
        [
          {
            "node": "Filtrar Asunto",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Filtrar Asunto": {
      "main": [
        [
          {
            "node": "Guardar en Notion",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Guardar en Notion": {
      "main": [
        [
          {
            "node": "Notificar Slack",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

### ⚠️ Puntos Críticos a Revisar

1.  **Propiedades en Notion:** Antes de activar el nodo de Notion, asegúrate de que tu Base de Datos en Notion tenga las columnas exactas que mapeas (ej. una columna llamada "Email" de tipo *Email*, otra "Asunto" de tipo *Text*, etc.). Si los nombres no coinciden, el nodo fallará.
2.  **Permisos de Gmail:** Al conectar Gmail, asegúrate de autorizar el acceso a leer los mensajes.
3.  **Permisos de Notion:** Cuando conectes Notion, debes darle acceso a la **Base de Datos específica** (ve a los 3 puntos de la DB en Notion -> Connections -> Add connection -> Tu bot de N8N).
4.  **Slack Channel ID:** El ID del canal suele empezar con `C0...`. Si no lo sabes, usa el nodo de Slack para "Get Channels" y búscalo.

¿Quieres que te explique cómo configurar las credenciales de alguna de estas apps en específico?