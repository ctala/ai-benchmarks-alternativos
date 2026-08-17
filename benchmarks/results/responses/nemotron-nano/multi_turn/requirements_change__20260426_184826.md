# Nemotron 3 Nano 30B — multi_turn/requirements_change

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 6.38 | quality: 5.08
- latency_total: 28.879s | tokens_per_second: 92.0
- input_tokens: 248 | output_tokens: 2658
- judge_score: 2.0 | justificación: 

## Respuesta completa

¡Entendido! Vamos a crear un workflow que cumpla con todo lo que necesitas:

| Paso | Nodo | Qué hace | Configuración clave |
|------|------|----------|----------------------|
| 1️⃣ | **Gmail Trigger** | Detecta nuevos correos en tu bandeja | • Conecta tu cuenta Gmail (OAuth) <br>• **Label**: (opcional) `propuestas` o deja vacío <br>• **Search Query**: `subject:(propuesta OR cotización)` <br>• **Polling Interval**: 1‑2 min (según tu frecuencia de mails) |
| 2️⃣ | **IF Node** (opcional) | Filtra por palabras exactas en el asunto (por si el Trigger ya lo hace) | • `IF` → **Field**: `item.jsonSubject` <br>• **Comparison**: `contains` <br>• **Value**: `propuesta` <br>• **Boolean**: `OR` → agrega segunda condición con `contains` y `cotizacion` |
| 3️⃣ | **Extract Fields** (Function) | Toma los datos que te interesan del mensaje | ```js\n// srcFields: subject, from.name, from.email, date, messageId\nconst subject = $json[\"body\"]?.subject || $json[\"subject\"];\nconst from = $node[\"Gmail Trigger\"].json[\"from\"];\n\nreturn {\n  json: {\n    subject: subject,\n    senderName: from?.name || \"\",\n    senderEmail: from?.email || \"\",\n    date: $json[\"date\"]?.$date,\n    messageId: $json[\"messageId\"]\n  }\n};\n``` |
| 4️⃣ | **Notion** – **Create Page** | Añade una fila a una base de datos de Notion | • **Integration**: tu token de Notion <br>• **Database ID**: el ID de la tabla donde guardas las propuestas <br>• **Properties**: mapea los campos que extrajiste (ej. `Name` = `senderName`, `Email` = `senderEmail`, `Subject` = `subject`, `Date` = `date`, `Message ID` = `messageId`) |
| 5️⃣ | **Slack** – **Send Message** | Notifica en un canal de Slack | • **Channel**: `#propuestas` (o el que prefieras) <br>• **Message**: usa la misma información extraída o un mensaje breve, por ejemplo: <br>```\n📥 Nueva propuesta recibida:\n*De*: {{ $json.senderName }}\n*Asunto*: {{ $json.subject }}\n*Fecha*: {{ $json.date }}\n*Link*: https://mail.google.com/mail/u/0/#inbox/messageid/{{ $json.messageId }}\n``` <br>• **Bot Token**: `xoxb-…` con permiso para publicar mensajes |

---

## Cómo montar el workflow paso a paso en N8N

1. **Crear un nuevo workflow** → `+ New Workflow`.

2. **Añadir el nodo “Gmail Trigger”**  
   - Arrastra **Gmail Trigger** desde la barra lateral → **Configure** →  
     - **Credentials**: crea una nueva credencial *Google OAuth2* y autoriza tu cuenta.  
     - **Search Query**: `subject:(propuesta OR cotización)` (esto ya filtra por ambas palabras).  
     - **Label**: opcional, por ejemplo `propuestas`.  
     - **Polling Interval**: 60 s (ajusta según tu necesidad).  

3. **Añadir un nodo “IF”** (por si prefieres filtrar en N8N en lugar de usar la búsqueda del trigger).  
   - Conecta el **Gmail Trigger** al **IF**.  
   - Dentro del IF, configura dos condiciones:  
     - `IF (contains($json.subject, "propuesta"))` → **True path**.  
     - **Add another condition** (botón “+”) → `OR (contains($json.subject, "cotizacion"))`.  
   - Conecta la rama **True** al siguiente paso.

4. **Añadir un nodo “Function”** (para extraer datos).  
   - Configura el código anterior (o personalízalo).  
   - Conecta la salida del **IF** a este **Function**.  

5. **Añadir el nodo “Notion – Create Page”**.  
   - Conecta el **Function** a este nodo.  
   - Selecciona tu **Integration** (crea una nueva si aún no lo tienes).  
   - Mapea los campos de salida del **Function** a las propiedades de tu base de datos Notion.  
   - Guarda y prueba; deberías ver una nueva página en Notion con los datos del email.  

6. **Añadir el nodo “Slack – Send Message”**.  
   - Conecta la salida del **Function** a este nodo.  
   - Selecciona tu **Slack Integration** (token de bot).  
   - Elige el **Channel** donde quieres la notificación.  
   - En el campo **Message**, usa la plantilla de ejemplo o personalízala.  

7. **Conectar los nodos** en orden:  
   `Gmail Trigger → IF → Function → Notion Create Page → Slack Send Message`.

8. **Activar el workflow** → Cambia el interruptor a **Active**.

---

## Detalles adicionales que pueden interesarte

### a) Manejo de mensajes ya procesados  
- Si temes que el trigger vuelva a dispararse con el mismo correo, puedes **marcar el mensaje como leído** o **añadir una etiqueta** después de procesarlo (usa un nodo “Gmail – Update Message” después del paso 5).  
- Alternativamente, guarda el `messageId` en una tabla de Notion y, en cada ejecución, verifica que no se haya procesado antes.

### b) Formato de fechas en Notion  
- Notion espera timestamps ISO (`2025-11-03T12:34:56Z`). El nodo **Function** ya devuelve `date` en ese formato; si usas otro formato, conviértelo con `new Date($json.date).toISOString()`.

### c) Seguridad y permisos  
- **Gmail**: solo otorga permisos de lectura (y opcionalmente “Modify” si vas a marcar como leído).  
- **Notion**: el token debe tener acceso a la base de datos específica.  
- **Slack**: el bot necesita el permiso *chat:write* en el canal deseado.

### d) Pruebas rápidas  
- En el editor de N8N, haz clic en **Execute Node** del **Gmail Trigger** para ver el primer mensaje que captura.  
- Verifica que el **IF** devuelva `true` y que la salida del **Function** tenga los campos esperados.  
- Ejecuta el workflow completo con **Execute Workflow** y revisa en Notion y Slack la salida.

---

### Resumen rápido (JSON del workflow)

Si prefieres importar el workflow directamente, aquí tienes una versión mínima en formato JSON que puedes importar en N8N (ajusta los IDs y credenciales):

```json
[
  {
    "name": "Gmail Trigger",
    "type": "n8n-nodes-base.googleGmail",
    "typeVersion": 2,
    "position": [250, 300],
    "parameters": {
      "operation": "listMessages",
      "label": "Nuevo correo con propuesta",
      "searchQuery": "subject:(propuesta OR cotización)",
      "maxResults": 10,
      "includeSpam": false
    },
    "credentials": {
      "googleApi": "Gmail OAuth2"
    }
  },
  {
    "name": "IF Filter",
    "type": "n8n-nodes-base.if",
    "typeVersion": 1,
    "position": [500, 300],
    "parameters": {
      "conditions": [
        {
          "value1": "={{$json.subject}}",
          "operation": "contains",
          "value2": "propuesta",
          "type": "string"
        },
        {
          "boolean": "OR",
          "value2": "cotizacion",
          "operation": "contains",
          "value1": "={{$json.subject}}"
        }
      ]
    }
  },
  {
    "name": "Extract Data",
    "type": "n8n-nodes-base.function",
    "typeVersion": 2,
    "position": [750, 300],
    "parameters": {},
    "executeMethod": "run",
    "disableExecuteLocked": false,
    "runOnWorkflowAction": false,
    "alwaysOutputData": true,
    "source": "return {\n  json: {\n    subject: $json.subject,\n    senderName: $json.from.name || \"\",\n    senderEmail: $json.from.email || \"\",\n    date: $json.internalDate,\n    messageId: $json.id\n  }\n};"
  },
  {
    "name": "Notion Create Page",
    "type": "n8n-nodes-base.notion",
    "typeVersion": 1,
    "position": [1000, 300],
    "parameters": {
      "operation": "createPage",
      "databaseId": "YOUR_DATABASE_ID"
    },
    "credentials": {
      "notionApi": "Notion Integration"
    },
    "propertyName": "json"
  },
  {
    "name": "Slack Send Message",
    "type": "n8n-nodes-base.slack",
    "typeVersion": 1,
    "position": [1250, 300],
    "parameters": {
      "channel": "#propuestas",
      "text": "📥 Nueva propuesta recibida:\n*De*: {{ $json.senderName }}\n*Asunto*: {{ $json.subject }}\n*Fecha*: {{ $json.date }}\n<https://mail.google.com/mail/u/0/#inbox/messageid/{{ $json.messageId }}|Ver en Gmail>"
    },
    "credentials": {
      "slackApi": "Slack Bot Token"
    }
  }
]
```

> **Importa** este JSON → *Import Workflow* → *Paste JSON* → *Import*.  
> Después, reemplaza `YOUR_DATABASE_ID`, los IDs de credenciales y el nombre del canal según tu configuración.

---

### 🎯 Resumen rápido de lo que obtienes

1. **Solo** los correos cuyo asunto contiene *propuesta* o *cotización* disparan el flujo.  
2. Los datos relevantes (remitente, asunto, fecha, ID) se guardan en una **página de Notion**.  
3. **Automáticamente** se publica una notificación en **Slack** para que tu equipo se entere al instante.

¿Te gustaría que profundice en algún punto (por ejemplo, cómo crear la base de datos en Notion o cómo generar el token de Slack)? ¡Avísame!