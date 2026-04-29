# Nemotron 3 Base 33B (DGX Spark Q4_K_M) — multi_turn/requirements_change

- model_id: `nemotron3:33b-q4_K_M`
- success: True  | final: 5.28 | quality: 4.52
- latency_total: 52.813s | tokens_per_second: 65.5
- input_tokens: 249 | output_tokens: 3461
- judge_score: 1.6 | justificación: 

## Respuesta completa

¡Claro! Aquí tienes la arquitectura del workflow en **n8n** que cumple con tus requisitos:

| Paso | Nodo | Qué hace | Configuración clave |
|------|------|----------|---------------------|
| 1 | **Gmail Trigger** | Detecta nuevos correos en tu cuenta Gmail. | • Selecciona el **label** (o la cuenta) que usarás para “propuestas/cotizaciones”.<br>• Puedes activar “Only when a new email is received”. |
| 2 | **Filter** | Filtra solo los mensajes cuyo asunto contenga **“propuesta”** o **“cotizacion”** (case‑insensitive). | • En “Condition” escribe: `{{ $json["subject"] }} contains "propuesta"`.<br>• Añade un **OR** con `... contains "cotizacion"`.<br>• Si la condición no se cumple, el flujo se detiene (no pasa al siguiente nodo). |
| 3 | **Function** (JavaScript) | Extrae los datos del remitente (nombre, email, asunto, fecha, cuerpo si lo deseas). | ```javascript<br>// $json contiene el cuerpo del email recibido<br>const subject = $json["subject"];<br>const from = $json["from"]; // ej. "Juan Pérez <juan@empresa.com>"<br>// Separamos nombre y email<br>const fromMatch = from.match(/<([^>]+)>/);<br>const senderName = fromMatch ? fromMatch[1] : from;<br>const senderEmail = fromMatch ? fromMatch[1] : from;<br>// Construimos el objeto que enviaremos a Notion<br>return [ {<br>    senderName,<br>    senderEmail,<br>    subject,<br>    receivedAt: $json["internalDate"] // timestamp UNIX en milisegundos<br>] ];<br>``` |
| 4 | **Slack Notification** | Envía una alerta a un canal de Slack (puede ser #alerts, #propuestas, etc.). | • Usa el nodo **Slack > Send Channel Message**.<br>• Canal: `#alerts` (o el que prefieras).<br>• Texto del mensaje (ejemplo):<br>```text<br>🚀 *Nueva propuesta/cotización* received from *{{ $json["senderName"] }}* ({{ $json["senderEmail"] }}).<br>Asunto: `{{ $json["subject"] }}`\nHora: <{{ formatDate $json["receivedAt"] "YYYY-MM-DD HH:mm" }}> | 
| 5 | **Notion > Create Page** | Crea una página en la base de datos (tabla) que hayas preparado en Notion. | • **Database ID**: el ID de la tabla donde quieres guardar las propuestas (puedes obtenerlo de la URL de la tabla en Notion).<br>• **Properties** a mapear:<br>  - **Name** (título) → `{{ $json["subject"] }}`<br>  - **Remitente** → `{{ $json["senderName"] }}`<br>  - **Email** → `{{ $json["senderEmail"] }}`<br>  - **Fecha de recepción** → `{{ $json["receivedAt"] }}` (puedes usar la función `formatDate` si necesitas formato legible).<br>• Opcional: añade una **attachment** con el cuerpo del email (usa el campo `text` o `html`). |

---

## Paso a paso para armar el workflow en n8n

1. **Añade el nodo “Gmail”**  
   - **Authentication**: Usa la credencial OAuth2 de Gmail (n8n tiene un helper llamado *Google OAuth2*).  
   - **Trigger**: “When a new email is received”. Si quieres limitar a una etiqueta, pon el nombre de la etiqueta en *Label* (ej. `Propuestas`).  

2. **Conecta el nodo “Filter”**  
   - En la configuración del nodo Filter, elige **“Boolean” → “contains”**.  
   - Añade dos condiciones con **OR** (en la UI de n8n basta con “Add condition” y cambiar el operador a “OR”).  
   - Condición 1: `subject` **contains** `propuesta`  
   - Condición 2: `subject` **contains** `cotizacion`  

3. **Nodo “Function”**  
   - Conecta el salida del nodo Filter al nodo Function.  
   - Copia el código de arriba (ajústalo si necesitas más campos, por ejemplo el cuerpo del mensaje).  
   - El nodo Function debe devolver **un solo array** con un objeto que contenga los datos que vas a enviar a Notion y a Slack.  

4. **Nodo “Slack”**  
   - Usa la credencial *Slack API* (OAuth2).  
   - En “Channel” escribe el nombre del canal (ej. `#alerts`).  
   - En “Message” puedes usar la sintaxis de interpolación de n8n:  
     ```
     🚀 *Nueva propuesta/cotización* received from *{{ $json["senderName"] }}* ({{ $json["senderEmail"] }}).
     Asunto: `{{ $json["subject"] }}`
     Hora: <{{ $json["receivedAt"] | date:"YYYY-MM-DD HH:mm" }}>
     ```  

5. **Nodo “Notion”**  
   - Añade la credencial *Notion* (token de integración).  
   - Selecciona la **Database ID** (la parte después de `https://www.notion.so/` antes del bloque de 32 caracteres).  
   - Mapea los campos:  
     - **Name** → `{{ $json["subject"] }}`  
     - **Remitente** → `{{ $json["senderName"] }}`  
     - **Email** → `{{ $json["senderEmail"] }}`  
     - **Fecha** → `{{ $json["receivedAt"] }}` (puedes usar la expresión `{{ $json["receivedAt"] | date:"DD/MM/YYYY HH:mm" }}` si tu base de datos espera formato texto).  

6. **Prueba**  
   - Envía un correo de prueba con asunto “Cotización de proyecto X”.  
   - Verifica que el flujo se detenga si el asunto no contiene nada de los palabras clave.  
   - Revisa en Slack que llega la notificación y en Notion que se crea la página con los datos correctos.  

---

## Detalles útiles y buenas prácticas

| Tema | Recomendación |
|------|---------------|
| **Credenciales** | Guarda los tokens de Gmail, Slack y Notion en las *Credentials* de n8n (no los pongas en texto dentro del flujo). |
| **Formato de fecha** | Notion acepta timestamps Unix (ms) o strings ISO‑8601. Si usas `date` en el nodo Function, puedes convertir el timestamp a `new Date($json["receivedAt"])` y luego a `toISOString()`. |
| **Manejo de errores** | Añade un nodo **“Error Trigger”** (o “Try/Catch”) alrededor del nodo Function para capturar fallos y, por ejemplo, enviar un mensaje a Slack indicando “⚠️ Error procesando email”. |
| **Límites de API** | Gmail y Notion tienen cuotas. Si tu volumen es alto, considera agregar un **“Pause”** (100 ms) entre iteraciones o usar **“Batch”** en el nodo Gmail (opción “Batch size”). |
| **Filtro avanzado** | Si en el futuro necesitas filtrar por remitente o por adjuntos, puedes añadir más condiciones al nodo Filter o usar un nodo **“Code”** que haga la lógica completa antes de la notificación. |
| **Registro** | Usa el nodo **“Logging”** (o simplemente revisa la consola de n8n) para depurar. Puedes imprimir `console.log($json)` para ver todo el payload. |

---

### JSON de ejemplo del flujo (para que lo importes directamente)

> **Nota:** El ID de la base de Notion y los nombres exactos de los campos deben ajustarse a tu base. Copia este JSON, pégalo en *Import* → *Workflow* y luego reemplaza los valores de credenciales/IDs.

```json
{
  "nodes": [
    {
      "parameters": {
        "authentication": "credentialApiKey",
        "alwaysOn": true,
        "triggerOn": "newEmail",
        "mailbox": "primary",
        "labelIds": [],
        "searchQuery": "",
        "includeSpam": false,
        "includeTrash": false,
        "searchQuery": "",
        "maxResults": 10
      },
      "name": "Gmail Trigger",
      "type": "n8n-nodes-base.gmail",
      "typeVersion": 1,
      "position": [
        250,
        300
      ],
      "credentials": {
        "gmail": "Gmail OAuth2"
      }
    },
    {
      "parameters": {
        "conditions": {
          "bool": [
            {
              "type": "string",
              "value1": "={{ $json[\"subject\"] }}",
              "operation": "contains",
              "value2": "propuesta"
            },
            {
              "type": "boolean",
              "operator": "or",
              "valueList": [
                {
                  "type": "string",
                  "value1": "={{ $json[\"subject\"] }}",
                  "operation": "contains",
                  "value2": "cotizacion"
                }
              ]
            }
          ]
        }
      },
      "name": "Filter by Subject",
      "type": "n8n-nodes-base.helpers.condition",
      "typeVersion": 1,
      "position": [
        500,
        300
      ],
      "credentials": {}
    },
    {
      "parameters": {
        "functionCode": "// Extract sender name and email\nconst from = $json[\"from\"];\nconst fromMatch = from.match(/<([^>]+)>/);\nconst senderName = fromMatch ? fromMatch[1] : from;\nconst senderEmail = fromMatch ? fromMatch[1] : from;\n\nreturn [{\n  senderName,\n  senderEmail,\n  subject: $json[\"subject\"],\n  receivedAt: $json[\"internalDate\"]\n}];"
      },
      "name": "Extract Data",
      "type": "n8n-nodes-base.function",
      "typeVersion": 1,
      "position": [
        750,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#alerts",
        "message": "🚀 *Nueva propuesta/cotización* received from *{{ $json[\"senderName\"] }}* ({{ $json[\"senderEmail\"] }}).\nAsunto: `{{ $json[\"subject\"] }}`\nHora: <{{ $json[\"receivedAt\"] | date:\"YYYY-MM-DD HH:mm\" }}>"
      },
      "name": "Slack Notification",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1000,
        300
      ],
      "credentials": {
        "slack": "Slack API Token"
      }
    },
    {
      "parameters": {
        "databaseId": "YOUR_NOTION_DATABASE_ID",
        "title": [
          {
            "string": "={{ $json[\"subject\"] }}",
            "name": "Name"
          }
        ],
        "properties": {
          "Remitente": [
            {
              "string": "={{ $json[\"senderName\"] }}",
              "name": "Remitente"
            }
          ],
          "Email": [
            {
              "string": "={{ $json[\"senderEmail\"] }}",
              "name": "Email"
            }
          ],
          "Fecha de recepción": [
            {
              "string": "={{ $json[\"receivedAt\"] | date:\"DD/MM/YYYY HH:mm\" }}",
              "name": "Fecha de recepción"
            }
          ]
        }
      },
      "name": "Create Notion Page",
      "type": "n8n-nodes-base.notion",
      "typeVersion": 1,
      "position": [
        1250,
        300
      ],
      "credentials": {
        "notion": "Notion API Token"
      }
    }
  ],
  "connections": {
    "Gmail Trigger": {
      "main": [
        [
          {
            "node": "Filter by Subject",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Filter by Subject": {
      "main": [
        [
          {
            "node": "Extract Data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract Data": {
      "main": [
        [
          {
            "node": "Slack Notification",
            "type": "main",
            "index": 0
          },
          [
            {
              "node": "Create Notion Page",
              "type": "main",
              "index": 0
            }
          ]
        ]
      ]
    }
  },
  "active": false,
  "settings": {},
  "id": "1"
}
```

> **Reemplaza** `YOUR_NOTION_DATABASE_ID` y los nombres de credenciales (`Gmail OAuth2`, `Slack API Token`, `Notion API Token`) por los que tengas configurados en tu cuenta de n8n.

---

### Resumen rápido

1️⃣ **Gmail Trigger** → nuevo email.  
2️⃣ **Filter** → asunto contiene “propuesta” **O** “cotizacion”.  
3️⃣ **Function** → parsea nombre, email, asunto y fecha.  
4️⃣ **Slack** → aviso instantáneo.  
5️⃣ **Notion** → crea página con los datos.

¡Con esto tendrás un workflow totalmente automatizado! Si necesitas ajustar algo (por ejemplo, agregar más campos, cambiar el formato de la notificación o añadir un paso de validación), solo avísame y lo afinamos. 🚀