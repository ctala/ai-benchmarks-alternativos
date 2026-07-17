# GLM-5.1 — multi_turn/requirements_change

- model_id: `z-ai/glm-5.1`
- success: True  | final: 4.24 | quality: 4.0
- latency_total: 54.968s | tokens_per_second: 52.0
- input_tokens: 227 | output_tokens: 2861
- judge_score: 4.2 | justificación: 

## Respuesta completa

¡Entendido! Cambiamos el destino a Notion, agregamos un filtro de asunto y una notificación a Slack. Este es un flujo muy típico y útil para automatizar la captación de clientes.

Aquí tienes la arquitectura actualizada y cómo configurar cada nodo en n8n:

### Arquitectura del Workflow
1. **Gmail Trigger** (Disparador)
2. **Set** (Limpieza y extracción de datos)
3. **IF** (Filtro de asunto)
4. **Notion** (Inserción de datos)
5. **Slack** (Notificación)

---

### Configuración paso a paso:

#### 1. Gmail Trigger
* **Resource:** Message
* **Event:** Received
* Asegúrate de conectar tu cuenta de Gmail y darle los permisos necesarios.

#### 2. Set Node (Preparación de datos)
Gmail suele devolver el remitente como `"Nombre Apellido <correo@email.com>"`. Este nodo nos sirve para limpiar eso y dejar los datos listos.
Crea los siguientes campos (String):
* **nombreRemitente**: `{{ $json.from.replace(/ *<.*/, '').trim() }}`
* **emailRemitente**: `{{ $json.from.replace(/.*<|>/g, '').trim() }}`
* **asunto**: `{{ $json.subject }}`
* **fecha**: `{{ $json.date }}`

#### 3. IF Node (Filtro)
Queremos que solo pasen los emails que contengan "propuesta" o "cotizacion" en el asunto. Para evitar problemas con mayúsculas/minúsculas, convertiremos el asunto a minúsculas:
* **Condition 1 (OR):**
  * Value 1: `{{ $json.asunto.toLowerCase() }}`
  * Operation: Contains
  * Value 2: `propuesta`
* **Condition 2 (OR):**
  * Value 1: `{{ $json.asunto.toLowerCase() }}`
  * Operation: Contains
  * Value 2: `cotizacion`

*Nota: Conecta la rama `True` del IF a los nodos de Notion y Slack. La rama `False` puedes dejarla sin conexión o poner un nodo "No Operation".*

#### 4. Notion Node
Asegúrate de tener una base de datos en Notion con las columnas correspondientes.
* **Resource:** Database Page
* **Operation:** Create
* **Database ID:** Selecciona tu base de datos de Notion.
* **Properties:**
  * Mapea las columnas de tu Notion con las variables que creamos en el nodo Set. Por ejemplo:
    * Columna `Email` (Email/Text) <- `{{ $json.emailRemitente }}`
    * Columna `Nombre` (Text) <- `{{ $json.nombreRemitente }}`
    * Columna `Asunto` (Text) <- `{{ $json.asunto }}`

#### 5. Slack Node
* **Resource:** Message
* **Operation:** Send
* **Channel:** Selecciona el canal de Slack donde quieres recibir la alerta.
* **Text:** Puedes usar un mensaje formateado como este:
  `🚨 *Nuevo email importante* de *{{ $json.nombreRemitente }}* ({{ $json.emailRemitente }}). Asunto: {{ $json.asunto }}`

---

### 💡 Código de ejemplo (JSON) para que lo pegues directamente en n8n:
Si quieres ahorrarte la configuración manual, copia este código, haz clic en la pantalla de n8n y presiona `Ctrl+V` (o Cmd+V en Mac). *Nota: Tendrás que volver a seleccionar tus credenciales de Gmail, Notion y Slack, y la base de datos de Notión.*

```json
{
  "nodes": [
    {
      "parameters": {
        "pollTimes": {
          "item": [
            {
              "mode": "everyMinute"
            }
          ]
        },
        "filters": {
          "from": "",
          "subject": "",
          "label": ""
        }
      },
      "id": "1",
      "name": "Gmail Trigger",
      "type": "n8n-nodes-base.gmailTrigger",
      "typeVersion": 1,
      "position": [
        250,
        300
      ]
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "1",
              "name": "nombreRemitente",
              "value": "={{ $json.from.replace(/ *<.*/, '').trim() }}",
              "type": "string"
            },
            {
              "id": "2",
              "name": "emailRemitente",
              "value": "={{ $json.from.replace(/.*<|>/g, '').trim() }}",
              "type": "string"
            },
            {
              "id": "3",
              "name": "asunto",
              "value": "={{ $json.subject }}",
              "type": "string"
            }
          ]
        }
      },
      "id": "2",
      "name": "Preparar Datos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [
        470,
        300
      ]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.asunto.toLowerCase() }}",
              "operation": "contains",
              "value2": "propuesta"
            },
            {
              "value1": "={{ $json.asunto.toLowerCase() }}",
              "operation": "contains",
              "value2": "cotizacion"
            }
          ]
        }
      },
      "id": "3",
      "name": "Filtro Asunto",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        690,
        300
      ]
    },
    {
      "parameters": {
        "resource": "databasePage",
        "operation": "create",
        "databaseId": {
          "__rl": true,
          "value": "TU_DATABASE_ID",
          "mode": "id"
        },
        "propertiesUi": {
          "propertyValues": []
        }
      },
      "id": "4",
      "name": "Notion",
      "type": "n8n-nodes-base.notion",
      "typeVersion": 2,
      "position": [
        910,
        240
      ]
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "🚨 *Nuevo email importante* de *{{ $json.nombreRemitente }}* ({{ $json.emailRemitente }}). Asunto: {{ $json.asunto }}",
        "otherOptions": {}
      },
      "id": "5",
      "name": "Slack",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        910,
        360
      ]
    }
  ],
  "connections": {
    "Gmail Trigger": {
      "main": [
        [
          {
            "node": "Preparar Datos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Preparar Datos": {
      "main": [
        [
          {
            "node": "Filtro Asunto",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Filtro Asunto": {
      "main": [
        [
          {
            "node": "Notion",
            "type": "main",
            "index": 0
          },
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

¿Necesitas ayuda configurando los permisos de la API de Notion o te queda alguna duda con las expresiones de filtrado?