# GPT-OSS 120B — multi_turn/requirements_change

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 6.17 | quality: 6.0
- latency_total: 36.527s | tokens_per_second: 92.1
- input_tokens: 290 | output_tokens: 3365

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

¡Claro! A continuación tienes el diseño completo de un workflow en **n8n** que:

1. **Escucha** los correos nuevos en Gmail.  
2. **Filtra** sólo aquellos cuyo asunto contenga **“propuesta”** o **“cotizacion”** (sin distinción de mayúsculas/minúsculas).  
3. **Extrae** los datos del remitente (nombre y email), asunto y fecha.  
4. **Crea** una página en **Notion** con esa información.  
5. **Envía** una notificación a **Slack** indicando que llegó un correo que cumple el criterio.

---

## 📋 Diagrama resumido del workflow

```
Gmail Trigger  →  IF (filter by subject)  →  Set (format fields)
                    │                         │
                    ├─► Notion (Create Page) └─► Slack (Send Message)
```

---

## 1️⃣ Nodo 1 – **Gmail Trigger**

| Campo | Valor / Comentario |
|-------|--------------------|
| **Resource** | `Message` |
| **Operation** | `Watch` (o `Get All` si prefieres usar un cron en vez de “watch”) |
| **Mailbox** | `INBOX` (o la etiqueta que uses) |
| **Trigger on** | `New Email` |
| **Include Attachments** | `No` (a menos que los necesites) |
| **Additional Fields → Query** | `subject:propuesta OR subject:cotizacion` <br>*(Esto ya filtra en Gmail, pero añadiremos una segunda capa de filtro por seguridad.)* |
| **Authentication** | Conecta tu cuenta de Google (OAuth) y otorga permisos a `https://mail.google.com/` y `https://www.googleapis.com/auth/gmail.readonly`. |

> **Tip:** Si prefieres usar el trigger “Watch” sin la query, simplemente déjala vacía y el filtro lo haremos en el siguiente nodo IF.

---

## 2️⃣ Nodo 2 – **IF (Filter by Subject)**  

Este nodo garantiza que sólo pasen los correos cuyo asunto contenga alguna de las palabras clave, sin importar mayúsculas/minúsculas.

| Campo | Valor |
|-------|-------|
| **Condition** | `String` → `Subject` → `Contains` → `propuesta` |
| **Add Or Condition** | `String` → `Subject` → `Contains` → `cotizacion` |
| **Case Sensitive** | `false` |

*Salida “true” → continúa al resto del flujo.*  
*Salida “false” → se descarta (no hace nada).*

---

## 3️⃣ Nodo 3 – **Set (Map & Clean Data)**  

En este nodo transformamos los datos del mensaje a un formato que Notion y Slack puedan usar fácilmente.

| Campo | Valor (Expression) |
|-------|--------------------|
| **NombreRemitente** | `{{$json["payload"]["headers"]["From"].split("<")[0].trim()}}` |
| **EmailRemitente** | `{{$json["payload"]["headers"]["From"].match(/<([^>]+)>/)[1]}}` |
| **Asunto** | `{{$json["payload"]["headers"]["Subject"]}}` |
| **Fecha** | `{{$json["payload"]["headers"]["Date"]}}` |
| **Snippet** *(opcional, resumen del cuerpo)* | `{{$json["payload"]["snippet"]}}` |

> **Explicación rápida:**  
> - `payload.headers.From` devuelve algo como `Juan Pérez <juan@email.com>`; usamos `.split("<")[0]` para obtener el nombre y una expresión regex para extraer el email.  
> - `payload.headers.Subject` y `Date` son los campos estándar del mensaje.

---

## 4️⃣ Nodo 4 – **Notion (Create Page)**  

Crea una nueva página en la base de datos que elijas.

| Campo | Valor |
|-------|-------|
| **Resource** | `Page` |
| **Operation** | `Create` |
| **Database ID** | *ID de la base de datos donde guardarás los correos* (p. ej. `c1234567‑abcd‑efgh‑ijkl‑mnopqrstuvwx`) |
| **Properties** | ```json { "Nombre": { "title": [{ "text": { "content": "{{$node["Set"].json["NombreRemitente"]}}" } }] }, "Email": { "email": "{{$node["Set"].json["EmailRemitente"]}}" }, "Asunto": { "rich_text": [{ "text": { "content": "{{$node["Set"].json["Asunto"]}}" } }] }, "Fecha": { "date": { "start": "{{$node["Set"].json["Fecha"]}}" } }, "Snippet": { "rich_text": [{ "text": { "content": "{{$node["Set"].json["Snippet"]}}" } }] } } ``` |
| **Authentication** | Conecta tu cuenta de Notion (OAuth) y otorga permiso a la base de datos. |

> **Nota:** Asegúrate de que la base de datos en Notion tenga las columnas con los mismos nombres (`Nombre`, `Email`, `Asunto`, `Fecha`, `Snippet`). Si usas otro idioma o nombres diferentes, adapta el JSON de `Properties` en consecuencia.

---

## 5️⃣ Nodo 5 – **Slack (Send Message)**  

Envía una notificación a un canal o a un usuario.

| Campo | Valor |
|-------|-------|
| **Resource** | `Message` |
| **Operation** | `Post` |
| **Channel** | `#general` (o el canal que prefieras) |
| **Text** | `Nueva propuesta/cotización recibida 📧\n*Remitente:* {{$node["Set"].json["NombreRemitente"]}} <{{$node["Set"].json["EmailRemitente"]}}>\n*Asunto:* {{$node["Set"].json["Asunto"]}}\n*Fecha:* {{$node["Set"].json["Fecha"]}}` |
| **Authentication** | Conecta tu workspace de Slack (OAuth) y otorga permiso a `chat:write`. |

---

## 📦 Export JSON completo (listo para importar)

Copia todo el bloque JSON y pégalo en **Import → From File** dentro de n8n.  
*(Asegúrate de reemplazar los valores marcados con `<< >>` por los tuyos propios.)*

```json
{
  "nodes": [
    {
      "parameters": {
        "resource": "message",
        "operation": "watch",
        "mailbox": "INBOX",
        "additionalFields": {
          "query": "subject:propuesta OR subject:cotizacion"
        }
      },
      "name": "Gmail Trigger",
      "type": "n8n-nodes-base.gmail",
      "typeVersion": 1,
      "position": [
        250,
        300
      ],
      "credentials": {
        "gmailOAuth2Api": "Gmail Account"
      }
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$json[\"payload\"][\"headers\"][\"Subject\"].toLowerCase()}}",
              "operation": "contains",
              "value2": "propuesta",
              "ignoreCase": true
            },
            {
              "value1": "={{$json[\"payload\"][\"headers\"][\"Subject\"].toLowerCase()}}",
              "operation": "contains",
              "value2": "cotizacion",
              "ignoreCase": true
            }
          ]
        }
      },
      "name": "IF (Subject filter)",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        500,
        300
      ]
    },
    {
      "parameters": {
        "values": {
          "string": [
            {
              "name": "NombreRemitente",
              "value": "={{$json[\"payload\"][\"headers\"][\"From\"].split(\"<\")[0].trim()}}"
            },
            {
              "name": "EmailRemitente",
              "value": "={{$json[\"payload\"][\"headers\"][\"From\"].match(/<([^>]+)>/)[1]}}"
            },
            {
              "name": "Asunto",
              "value": "={{$json[\"payload\"][\"headers\"][\"Subject\"]}}"
            },
            {
              "name": "Fecha",
              "value": "={{$json[\"payload\"][\"headers\"][\"Date\"]}}"
            },
            {
              "name": "Snippet",
              "value": "={{$json[\"payload\"][\"snippet\"]}}"
            }
          ]
        },
        "options": {}
      },
      "name": "Set (Clean data)",
      "type": "n8n-nodes-base.set",
      "typeVersion": 2,
      "position": [
        750,
        300
      ]
    },
    {
      "parameters": {
        "resource": "page",
        "operation": "create",
        "databaseId": "<<YOUR_NOTION_DATABASE_ID>>",
        "properties": {
          "Nombre": {
            "title": [
              {
                "text": {
                  "content": "={{$node[\"Set (Clean data)\"].json[\"NombreRemitente\"]}}"
                }
              }
            ]
          },
          "Email": {
            "email": "={{$node[\"Set (Clean data)\"].json[\"EmailRemitente\"]}}"
          },
          "Asunto": {
            "rich_text": [
              {
                "text": {
                  "content": "={{$node[\"Set (Clean data)\"].json[\"Asunto\"]}}"
                }
              }
            ]
          },
          "Fecha": {
            "date": {
              "start": "={{$node[\"Set (Clean data)\"].json[\"Fecha\"]}}"
            }
          },
          "Snippet": {
            "rich_text": [
              {
                "text": {
                  "content": "={{$node[\"Set (Clean data)\"].json[\"Snippet\"]}}"
                }
              }
            ]
          }
        }
      },
      "name": "Notion – Create Page",
      "type": "n8n-nodes-base.notion",
      "typeVersion": 1,
      "position": [
        1000,
        200
      ],
      "credentials": {
        "notionApi": "Notion Account"
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "<<SLACK_CHANNEL_ID_OR_NAME>>",
        "text": "Nueva propuesta/cotización recibida 📧\n*Remitente:* {{$node[\"Set (Clean data)\"].json[\"NombreRemitente\"]}} <{{$node[\"Set (Clean data)\"].json[\"EmailRemitente\"]}}>\n*Asunto:* {{$node[\"Set (Clean data)\"].json[\"Asunto\"]}}\n*Fecha:* {{$node[\"Set (Clean data)\"].json[\"Fecha\"]}}"
      },
      "name": "Slack – Notify",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1000,
        400
      ],
      "credentials": {
        "slackApi": "Slack Workspace"
      }
    }
  ],
  "connections": {
    "Gmail Trigger": {
      "main": [
        [
          {
            "node": "IF (Subject filter)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IF (Subject filter)": {
      "main": [
        [
          {
            "node": "Set (Clean data)",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": null,
            "type": "main",
            "index": 1
          }
        ]
      ]
    },
    "Set (Clean data)": {
      "main": [
        [
          {
            "node": "Notion – Create Page",
            "type": "main",
            "index": 0
          },
          {
            "node": "Slack – Notify",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "active": false,
  "settings": {},
  "id": "1"
}
```

### Pasos para usar el JSON

1. **Reemplaza** los marcadores `<<YOUR_NOTION_DATABASE_ID>>`, `<<SLACK_CHANNEL_ID_OR_NAME>>` y los nombres de credenciales (`Gmail Account`, `Notion Account`, `Slack Workspace`) por los valores reales de tu proyecto.  
2. En **n8n**, ve a **Workflows → Import → From JSON** y pega el contenido.  
3. Activa el workflow (`Activate`) y, si usas el trigger “Watch”, déjalo ejecutándose en modo **active** para que escuche nuevos correos en tiempo real.  

---

## 🛠️ Tips de depuración y mejoras

| Tema | Qué puedes hacer |
|------|------------------|
| **Ver logs del trigger** | Añade un nodo **Debug** después del Gmail Trigger para asegurarte de que recibes los campos esperados (`payload.headers.From`, `Subject`, etc.). |
| **Filtrado adicional** | Si en algún momento necesitas filtrar por remitente o por dominio, agrega otro nodo **IF** antes del Set. |
| **Formato de fecha** | Notion acepta ISO 8601 (`2024-08-12T14:30:00.000Z`). Si la fecha de Gmail viene en otro formato, usa un nodo **Function**: `new Date($json["payload"]["headers"]["Date"]).toISOString()` y asigna el resultado a `Fecha`. |
| **Manejo de adjuntos** | Si en el futuro quieres guardar archivos adjuntos en Notion o en otro storage (S3, Google Drive), añade un nodo **Google Drive** o **AWS S3** después del Set y pasa `{{ $json["payload"]["attachments"] }}`. |
| **Rate‑limit de Slack** | Si esperas muchos correos, puedes agrupar notificaciones usando un nodo **Merge** con “Wait” y enviar un resumen cada X minutos. |

---

## 📢 Próximos pasos

1. **Prueba** el workflow con un correo de prueba que contenga “propuesta” en el asunto.  
2. **Revisa** la página creada en Notion para confirmar que los campos se llenan correctamente.  
3. **Verifica** que el mensaje llegue al canal de Slack que elegiste.  

Si todo funciona, ¡ya tienes el proceso automatizado!  
Si necesitas ajustar algo (por ejemplo, añadir más campos, cambiar la lógica de filtrado o guardar adjuntos), dime y lo afinamos. 🚀