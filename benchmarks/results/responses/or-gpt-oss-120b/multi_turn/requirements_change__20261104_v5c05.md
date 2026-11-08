# GPT-OSS 120B — multi_turn/requirements_change

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 4.61 | quality: 4.0
- latency_total: 90.51s | tokens_per_second: 38.5
- input_tokens: 277 | output_tokens: 3482

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

¡Claro! Vamos a diseñar un flujo en **n8n** que haga exactamente lo que pides:

1. **Escuchar nuevos correos en Gmail**.  
2. **Filtrar solo los que tengan “propuesta” o “cotización” en el asunto**.  
3. **Extraer los datos del remitente (nombre, email), asunto y fecha**.  
4. **Crear una página en una base de datos de Notion con esos datos**.  
5. **Enviar una notificación a Slack**.

A continuación tienes la arquitectura del workflow y, después, la configuración paso‑a‑paso de cada nodo (incluyendo los campos que debes rellenar y los expresiones que usar). Al final, también te dejo el JSON exportable del workflow para que lo importes directamente en n8n.

---

## 🗂️ Arquitectura del workflow

| # | Nodo | Tipo | Qué hace |
|---|------|------|----------|
| 1 | **Gmail Trigger** | Trigger | Detecta cada email nuevo que llega a la cuenta. |
| 2 | **IF (Filtro asunto)** | IF | Comprueba si el asunto contiene “propuesta” o “cotización”. |
| 3 | **Set (Extraer datos)** | Set | Normaliza los campos que vamos a enviar a Notion y Slack. |
| 4 | **Notion – Create Page** | Notion | Crea una nueva página en la base de datos especificada. |
| 5 | **Slack – Send Message** | Slack | Notifica en el canal que desees. |
| 6 (opcional) | **Error handling** | No Op / Set | Captura cualquier error y lo envía a Slack o a un webhook. |

---

## ⚙️ Configuración paso a paso

### 1️⃣ Gmail Trigger

| Campo | Valor |
|-------|-------|
| **Resource** | `Message` |
| **Operation** | `Watch` (o `New Email` si prefieres polling) |
| **Mailbox** | `INBOX` (por defecto) |
| **Search** | `is:unread` (opcional, para procesar solo no leídos) |
| **Trigger on** | `New` |
| **Polling Interval** | `5 min` (ajusta según tu plan) |
| **Authentication** | Conecta tu cuenta de Google con OAuth2 (debes crear una credencial en Google Cloud con scopes `https://www.googleapis.com/auth/gmail.readonly`). |

> **Tip:** Si usas la opción *Watch* (webhook), n8n crea un endpoint que Google llamará cuando llegue un nuevo mensaje. Si tu plan no permite webhooks, usa *New Email* (polling) y ajusta el intervalo.

---

### 2️⃣ IF – Filtrar por asunto

1. Arrastra un nodo **IF** y conéctalo al Gmail Trigger.  
2. En la pestaña **Rules** configura una regla **OR** con dos condiciones:

| Operador | Valor |
|----------|-------|
| **Expression** | `{{$json["subject"]?.toLowerCase().includes("propuesta")}}` |
| **OR** | `{{$json["subject"]?.toLowerCase().includes("cotizacion")}}` |

> **Explicación:** Convertimos el asunto a minúsculas y usamos `includes()` para buscar ambas palabras. Si cualquiera de las dos coincide, el flujo sigue por la rama **true**; si no, se descarta.

---

### 3️⃣ Set – Normalizar datos

Este nodo nos permite crear variables con nombres claros para usarlos después.

| Campo | Valor / Expresión |
|-------|-------------------|
| **Name** | `extractedData` (puedes dejar el nombre por defecto) |
| **Values to Set** |  |
| `senderName` | `{{$json["from"]?.split("<")[0].trim()}}` |
| `senderEmail` | `{{$json["from"]?.match(/<(.+?)>/)[1]}}` |
| `subject` | `{{$json["subject"]}}` |
| `date` | `{{$json["date"]}}` |
| `gmailMessageId` | `{{$json["id"]}}` (por si quieres guardarlo) |

> **Nota:** El campo `from` de Gmail tiene formato `Nombre Apellido <email@dominio.com>`. Con `split("<")[0]` obtenemos el nombre y con la expresión regex extraemos el email.

---

### 4️⃣ Notion – Create Page

1. Añade un nodo **Notion** → **Operation**: `Create Page`.  
2. **Authentication**: conecta tu cuenta de Notion (OAuth2) y otorga permiso a la base de datos donde quieres guardar los datos.  
3. **Database ID**: copia el ID de la base de datos (URL de Notion: `https://www.notion.so/<workspace>/<DATABASE_ID>?v=...`).  
4. **Properties**: mapea cada campo a una propiedad de tu base de datos. Supongamos que la tabla tiene las siguientes columnas:

| Notion Property | Tipo | Valor (expresión) |
|-----------------|------|-------------------|
| `Nombre` | Title | `{{$node["Set"].json["senderName"]}}` |
| `Email` | Email | `{{$node["Set"].json["senderEmail"]}}` |
| `Asunto` | Text | `{{$node["Set"].json["subject"]}}` |
| `Fecha` | Date | `{{$node["Set"].json["date"]}}` |
| `Gmail Message ID` | Text | `{{$node["Set"].json["gmailMessageId"]}}` |

> Si alguna columna es de tipo **Select**, **Multi‑Select**, **Number**, etc., ajusta la expresión al formato que Notion espera (por ejemplo, `{"select": {"name": "Propuesta"}}`).

5. **Options** (opcional): marca **"Return All"** para que el nodo devuelva la página creada (útil para depuración).

---

### 5️⃣ Slack – Send Message

1. Añade **Slack** → **Operation**: `Send Message`.  
2. **Authentication**: conecta tu workspace de Slack (OAuth2) y elige el canal donde quieres recibir la alerta.  
3. **Channel**: `#general` (o el que prefieras).  
4. **Message Text**: usa una plantilla con los datos extraídos:

```markdown
📧 *Nuevo email filtrado*  
*Remitente:* {{ $node["Set"].json["senderName"] }} <{{ $node["Set"].json["senderEmail"] }}>  
*Asunto:* {{ $node["Set"].json["subject"] }}  
*Fecha:* {{ $node["Set"].json["date"] }}  
<https://mail.google.com/mail/u/0/#inbox/{{ $node["Set"].json["gmailMessageId"] }}|Ver en Gmail>
```

> **Tip:** El enlace al mensaje de Gmail se construye con `https://mail.google.com/mail/u/0/#inbox/<MESSAGE_ID>`.

---

### 6️⃣ (Opcional) Manejo de errores

Puedes añadir un **Error Trigger** o conectar la salida **Error** de cualquier nodo a un **Slack** o **Webhook** para recibir alertas cuando algo falle. Por ejemplo:

- **Error Trigger** → **Slack – Send Message** con texto: `"⚠️ Error en el workflow: {{ $json["error"] }}"`.

---

## 📦 JSON exportable (lista para importar)

Copia todo el bloque JSON y, en n8n, ve a **Workflows → Import** → pega el contenido → **Import**. El workflow quedará listo; solo tendrás que:

1. Reemplazar los **IDs** de Notion (Database ID) y Slack (Channel ID).  
2. Volver a conectar las credenciales de Gmail, Notion y Slack (si no se importan automáticamente).  

```json
{
  "nodes": [
    {
      "parameters": {
        "resource": "message",
        "operation": "watch",
        "mailbox": "INBOX",
        "search": "is:unread",
        "triggerOn": "new",
        "pollingTimespan": 5,
        "pollingInterval": 5
      },
      "name": "Gmail Trigger",
      "type": "n8n-nodes-base.gmailTrigger",
      "typeVersion": 1,
      "position": [
        250,
        300
      ],
      "credentials": {
        "gmailOAuth2Api": {
          "id": "gmailOAuth2",
          "name": "Gmail OAuth2 API"
        }
      }
    },
    {
      "parameters": {
        "conditions": {
          "boolean": [
            {
              "value1": "={{$json[\"subject\"]?.toLowerCase().includes(\"propuesta\")}}",
              "operation": "true"
            },
            {
              "value1": "={{$json[\"subject\"]?.toLowerCase().includes(\"cotizacion\")}}",
              "operation": "true"
            }
          ]
        }
      },
      "name": "IF Subject Filter",
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
              "name": "senderName",
              "value": "={{$json[\"from\"]?.split(\"<\")[0].trim()}}"
            },
            {
              "name": "senderEmail",
              "value": "={{$json[\"from\"]?.match(/<(.+?)>/)[1]}}"
            },
            {
              "name": "subject",
              "value": "={{$json[\"subject\"]}}"
            },
            {
              "name": "date",
              "value": "={{$json[\"date\"]}}"
            },
            {
              "name": "gmailMessageId",
              "value": "={{$json[\"id\"]}}"
            }
          ]
        },
        "options": {}
      },
      "name": "Set Extracted Data",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [
        750,
        300
      ]
    },
    {
      "parameters": {
        "operation": "createPage",
        "databaseId": "<TU_DATABASE_ID_DE_NOTION>",
        "properties": {
          "Nombre": {
            "title": [
              {
                "text": {
                  "content": "={{$node[\"Set Extracted Data\"].json[\"senderName\"]}}"
                }
              }
            ]
          },
          "Email": {
            "email": "={{$node[\"Set Extracted Data\"].json[\"senderEmail\"]}}"
          },
          "Asunto": {
            "rich_text": [
              {
                "text": {
                  "content": "={{$node[\"Set Extracted Data\"].json[\"subject\"]}}"
                }
              }
            ]
          },
          "Fecha": {
            "date": {
              "start": "={{$node[\"Set Extracted Data\"].json[\"date\"]}}"
            }
          },
          "Gmail Message ID": {
            "rich_text": [
              {
                "text": {
                  "content": "={{$node[\"Set Extracted Data\"].json[\"gmailMessageId\"]}}"
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
        300
      ],
      "credentials": {
        "notionApi": {
          "id": "notionOAuth2",
          "name": "Notion OAuth2 API"
        }
      }
    },
    {
      "parameters": {
        "channel": "<CANAL_ID_DE_SLACK>",
        "text": "📧 *Nuevo email filtrado*\n*Remitente:* {{ $node[\"Set Extracted Data\"].json[\"senderName\"] }} <{{ $node[\"Set Extracted Data\"].json[\"senderEmail\"] }}>\n*Asunto:* {{ $node[\"Set Extracted Data\"].json[\"subject\"] }}\n*Fecha:* {{ $node[\"Set Extracted Data\"].json[\"date\"] }}\n<https://mail.google.com/mail/u/0/#inbox/{{ $node[\"Set Extracted Data\"].json[\"gmailMessageId\"] }}|Ver en Gmail>"
      },
      "name": "Slack – Notify",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1250,
        300
      ],
      "credentials": {
        "slackApi": {
          "id": "slackOAuth2",
          "name": "Slack OAuth2 API"
        }
      }
    }
  ],
  "connections": {
    "Gmail Trigger": {
      "main": [
        [
          {
            "node": "IF Subject Filter",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IF Subject Filter": {
      "main": [
        [
          {
            "node": "Set Extracted Data",
            "type": "main",
            "index": 0
          }
        ]
      ],
      "true": [
        [
          {
            "node": "Set Extracted Data",
            "type": "main",
            "index": 0
          }
        ]
      ],
      "false": []
    },
    "Set Extracted Data": {
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

> **Reemplaza**:
> - `<TU_DATABASE_ID_DE_NOTION>` → ID real de tu tabla Notion.  
> - `<CANAL_ID_DE_SLACK>` → ID del canal (puedes usar `#general` o el nombre del canal si ya tienes la credencial configurada).  
> - Los IDs de credenciales (`gmailOAuth2`, `notionOAuth2`, `slackOAuth2`) deben coincidir con los que tengas creados en **Credenciales** de n8n.

---

## 🚀 Próximos pasos

1. **Importa** el JSON en n8n.  
2. **Actualiza** los IDs y verifica que las credenciales estén activas.  
3. **Ejecuta** el workflow en modo *Manual* una vez para validar que:
   - Se detecte un email que cumpla el filtro.  
   - Se cree la página en Notion con los campos correctos.  
   - Llegue la notificación a Slack.  
4. Si todo funciona, **activa** el trigger (pon el workflow en “Active”).  

¡Listo! Ahora cada correo que contenga “propuesta” o “cotización” será registrado automáticamente en Notion y recibirás una alerta inmediata en Slack. Si tienes alguna duda al configurar alguna credencial o al adaptar los nombres de columnas en Notion, avísame y lo afinamos. 🎉