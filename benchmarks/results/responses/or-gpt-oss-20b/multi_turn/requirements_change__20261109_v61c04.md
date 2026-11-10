# GPT-OSS 20B — multi_turn/requirements_change

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 6.42 | quality: 6.0
- latency_total: 19.47s | tokens_per_second: 135.4
- input_tokens: 290 | output_tokens: 2636

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

¡Claro! Te dejo un workflow completo de **n8n** que hace exactamente lo que pides:

1. **Lee correos nuevos de Gmail.**  
2. **Filtra** solo los que contengan “propuesta” o “cotización” en el asunto.  
3. **Extrae** los datos del remitente, asunto y fecha.  
4. **Almacena** esos datos en una base de datos de Notion.  
5. **Envía** una notificación a Slack cuando se capture el email.

---

## 1️⃣ Preparación – Credenciales

| Servicio | Requisitos |
|----------|------------|
| **Gmail** | - Una cuenta de Google.<br>- Habilitar la API de Gmail y crear credenciales OAuth 2.0.<br>- Conceder permiso a n8n para “Ver y administrar tus correos electrónicos”. |
| **Notion** | - Una cuenta de Notion.<br>- Crear una **integración** y obtener el “Internal Integration Token”.<br>- Compartir la base de datos con la integración. |
| **Slack** | - Una cuenta de Slack.<br>- Crear una “App” con permisos de `chat:write` y obtener el “Bot User OAuth Token”. |
| **n8n** | - Instalar la última versión (Docker, Cloud, etc.).<br>- Configurar los credenciales en la sección **Credentials** de n8n (Gmail, Notion, Slack). |

> **Tip:** En n8n, ve a **Credentials** → **New Credential** → selecciona el tipo (Gmail, Notion, Slack) y sigue el asistente.

---

## 2️⃣ Diseño del workflow

### 2.1 Gmail Trigger

| Configuración | Detalle |
|---------------|---------|
| **Email** | (opcional) “*” para todos los correos, o `from:yourdomain.com` para limitar a tu dominio. |
| **Subject** | Deja vacío; usaremos un **Filter** posterior. |
| **Search Query** | Puedes usar `subject:propuesta OR subject:cotizacion` para reducir la carga. |
| **Only unread** | `false` (para que no pierda correos ya leídos). |
| **Mark as read** | `true/false` según tu preferencia. |

> Si usas la búsqueda del Gmail trigger (`subject:...`), el flujo ya solo procesará los correos que coincidan, pero el **Filter** que sigue sirve como segunda capa de seguridad.

### 2.2 Filter Node (Opcional, pero recomendado)

> Usa un **Filter** para asegurarte de que el asunto contenga las palabras clave.

| Expression | Resultado |
|------------|-----------|
| `{{ $json["subject"]?.toLowerCase().includes("propuesta") || $json["subject"]?.toLowerCase().includes("cotizacion") }}` | `true` si el asunto contiene alguna de las palabras, `false` en caso contrario. |

Si el resultado es `false` el flujo se detiene y no sigue.

### 2.3 Function Node – Extraer datos

```javascript
// function node: Extract email data
const email = $json["from"]?.[0]?.email ?? '';
const name  = $json["from"]?.[0]?.name ?? '';
const subject = $json["subject"] ?? '';
const date = $json["date"] ?? '';

return {
  email,
  name,
  subject,
  date
};
```

> **Nota:** `$json` contiene el payload del Gmail trigger.  
> Si tu Gmail devuelve el remitente como un objeto con `email` y `name`, este código los extrae.

### 2.4 Notion Node – Crear ítem

1. **Operation**: `Create`  
2. **Database ID**: La ID de la base de datos de Notion donde quieres que se guarden los datos.  
3. **Properties**: Mapea los campos que creaste en la base de datos (p.ej. `Remitente`, `Email`, `Asunto`, `Fecha`).  
   ```json
   {
     "Remitente": {
       "title": [
         {
           "text": {
             "content": "{{ $json.name }}"
           }
         }
       ]
     },
     "Email": {
       "email": "{{ $json.email }}"
     },
     "Asunto": {
       "rich_text": [
         {
           "text": {
             "content": "{{ $json.subject }}"
           }
         }
       ]
     },
     "Fecha": {
       "date": {
         "start": "{{ $json.date }}"
       }
     }
   }
   ```

> Asegúrate de que los nombres de las propiedades coincidan exactamente con los definidos en Notion.

### 2.5 Slack Node – Notificar

1. **Operation**: `Post Message`  
2. **Channel**: ID del canal o nombre con `#`.  
3. **Text**: Mensaje que quieres enviar.  
   ```text
   📬 Nuevo email de **{{ $json.name }}**  
   📧 Email: {{ $json.email }}  
   🗒️ Asunto: {{ $json.subject }}  
   📅 Fecha: {{ $json.date }}
   ```

> Si quieres adjuntar un enlace al email, puedes usar la propiedad `webLink` que Gmail devuelve como `$json.webLink`.

---

## 3️⃣ Conexión de nodos

```
Gmail Trigger → Filter → Function → Notion → Slack
```

> Si prefieres filtrar directamente en el trigger, puedes saltar el nodo “Filter”.

---

## 4️⃣ Exportar workflow (JSON)

Para que puedas importarlo directamente en n8n, aquí tienes el JSON completo:

```json
[
  {
    "id": "1",
    "name": "Gmail Trigger",
    "type": "n8n-nodes-base.gmailTrigger",
    "typeVersion": 1,
    "position": [200, 300],
    "credentials": {
      "gmailOAuth2Api": {
        "id": "YOUR_GMAIL_CREDENTIAL_ID",
        "name": "Gmail OAuth2"
      }
    },
    "parameters": {
      "email": "",
      "subject": "",
      "searchQuery": "subject:propuesta OR subject:cotizacion",
      "onlyUnread": false,
      "markAsRead": true
    }
  },
  {
    "id": "2",
    "name": "Filter",
    "type": "n8n-nodes-base.if",
    "typeVersion": 1,
    "position": [400, 300],
    "parameters": {
      "conditions": {
        "boolean": [
          {
            "value1": "={{ $json[\"subject\"]?.toLowerCase().includes(\"propuesta\") || $json[\"subject\"]?.toLowerCase().includes(\"cotizacion\") }}",
            "operation": "is true"
          }
        ]
      }
    }
  },
  {
    "id": "3",
    "name": "Extract Data",
    "type": "n8n-nodes-base.function",
    "typeVersion": 1,
    "position": [600, 300],
    "parameters": {
      "functionCode": "const email = $json[\"from\"]?.[0]?.email ?? '';\nconst name  = $json[\"from\"]?.[0]?.name ?? '';\nconst subject = $json[\"subject\"] ?? '';\nconst date = $json[\"date\"] ?? '';\n\nreturn {\n  email,\n  name,\n  subject,\n  date\n};"
    }
  },
  {
    "id": "4",
    "name": "Create in Notion",
    "type": "n8n-nodes-base.notion",
    "typeVersion": 1,
    "position": [800, 300],
    "credentials": {
      "notionApi": {
        "id": "YOUR_NOTION_CREDENTIAL_ID",
        "name": "Notion"
      }
    },
    "parameters": {
      "resource": "database",
      "operation": "create",
      "databaseId": "YOUR_NOTION_DATABASE_ID",
      "properties": {
        "Remitente": {
          "title": [
            {
              "text": {
                "content": "={{ $json[\"name\"] }}"
              }
            }
          ]
        },
        "Email": {
          "email": "={{ $json[\"email\"] }}"
        },
        "Asunto": {
          "rich_text": [
            {
              "text": {
                "content": "={{ $json[\"subject\"] }}"
              }
            }
          ]
        },
        "Fecha": {
          "date": {
            "start": "={{ $json[\"date\"] }}"
          }
        }
      }
    }
  },
  {
    "id": "5",
    "name": "Notify Slack",
    "type": "n8n-nodes-base.slack",
    "typeVersion": 1,
    "position": [1000, 300],
    "credentials": {
      "slack": {
        "id": "YOUR_SLACK_CREDENTIAL_ID",
        "name": "Slack"
      }
    },
    "parameters": {
      "operation": "postMessage",
      "channelId": "#general",
      "text": "📬 Nuevo email de **={{ $json[\"name\"] }}**\\n📧 Email: {{ $json[\"email\"] }}\\n🗒️ Asunto: {{ $json[\"subject\"] }}\\n📅 Fecha: {{ $json[\"date\"] }}"
    }
  }
]
```

> **Reemplaza** los placeholders (`YOUR_GMAIL_CREDENTIAL_ID`, `YOUR_NOTION_CREDENTIAL_ID`, etc.) con los IDs reales que obtengas al crear las credenciales en n8n.

---

## 5️⃣ Prueba y depuración

1. Activa el workflow y envía un email de prueba con “propuesta” o “cotización” en el asunto.  
2. Verifica que:
   * El correo llegue al trigger.  
   * El filtro lo acepte.  
   * Los datos se guarden correctamente en Notion.  
   * Slack reciba la notificación.

Si algo falla, revisa el *Execution Log* de cada nodo para ver qué datos se recibieron y dónde pudo haber un error de mapeo.

---

## 6️⃣ Ajustes adicionales

| Necesidad | Solución |
|----------|----------|
| **Guardar más campos** | Añade más propiedades en el nodo Function y mapea en Notion. |
| **Enviar email de respuesta** | Añade un nodo **Gmail** (Send Email) después del Notion. |
| **Manejo de errores** | Usa un nodo **Error Trigger** y envía una alerta a Slack. |
| **Procesar archivos adjuntos** | En el Function node, extrae `attachments` y guarda la URL en Notion. |

---

### 🎉 ¡Listo!  
Con este workflow tendrás una automatización que:

- Solo procesa los emails relevantes.  
- Almacena la información de manera estructurada en Notion.  
- Te avisa en Slack en tiempo real.

Si necesitas ayuda para adaptar los nombres de las columnas en Notion o ajustar los filtros, avísame y lo afinamos. 🚀