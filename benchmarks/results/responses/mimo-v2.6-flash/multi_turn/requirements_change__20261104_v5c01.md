# MiMo V2.6 Flash — multi_turn/requirements_change

- model_id: `xiaomi/mimo-v2.6-flash`
- success: True  | final: 4.68 | quality: 4.0
- latency_total: 46.428s | tokens_per_second: 31.9
- input_tokens: 244 | output_tokens: 1481

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

# Workflow N8N: Gmail → Notion + Slack

## Diagrama del workflow

```
┌─────────────┐    ┌──────────────┐    ┌──────────────┐    ┌─────────┐    ┌──────────┐
│Gmail Trigger│───▶│   Filter     │───▶│   Function   │───▶│  Notion │───▶│   Slack  │
│  (Nuevo     │    │(Subject:     │    │  (Extraer    │    │(Crear   │    │(Notificar│
│   Email)    │    │propuesta/    │    │   datos      │    │registro)│    │          │
│             │    │cotizacion)   │    │   remitente) │    │         │    │          │
└─────────────┘    └──────────────┘    └──────────────┘    └─────────┘    └──────────┘
```

---

## Nodo 1: Gmail Trigger

| Campo | Valor |
|-------|-------|
| **Resource** | Email |
| **Operation** | On New Email |
| **Labels/Inbox** | INBOX (o la etiqueta que uses) |
| **Poll Times** | Every 5 minutes |
| **Simplification** | Yes (para obtener datos limpios) |

> Salida esperada: objeto con `subject`, `from`, `date`, `body`, etc.

---

## Nodo 2: Filter (Filtrar por asunto)

| Campo | Valor |
|-------|-------|
| **Operation** | Keep |
| **Conditions** | Agregar **2 condiciones** con OR |

Condición 1:
| Campo | Operador | Valor |
|-------|----------|-------|
| `subject` | contains | `propuesta` |

Condición 2:
| Campo | Operador | Valor |
|-------|----------|-------|
| `subject` | contains | `cotizacion` |

---

## Nodo 3: Function (Extraer datos del remitente)

```javascript
const item = $input.item.json;

// Extraer nombre y email del remitente
const fromField = item.from;
const emailMatch = fromField.match(/<(.+?)>/);
const nameMatch = fromField.match(/^"?([^"<]+)"?/);

return {
  json: {
    nombreRemitente: nameMatch ? nameMatch[1].trim() : "Desconocido",
    emailRemitente: emailMatch ? emailMatch[1] : fromField,
    asunto: item.subject,
    fecha: item.date,
    cuerpo: item.text || item.html || "",
    mensajeId: item.messageId || ""
  }
};
```

---

## Nodo 4: Notion (Crear registro)

| Campo | Valor |
|-------|-------|
| **Resource** | Database |
| **Operation** | Create |
| **Database ID** | `tu-database-id` |
| **Simplification** | No |

**Propiedades de la base de datos Notion:**

| Campo Notion | Tipo | Valor (del nodo anterior) |
|--------------|------|---------------------------|
| Nombre Remitente | Rich Text | `{{ $json.nombreRemitente }}` |
| Email | Email | `{{ $json.emailRemitente }}` |
| Asunto | Title | `{{ $json.asunto }}` |
| Fecha | Date | `{{ $json.fecha }}` |
| Cuerpo | Rich Text | `{{ $json.cuerpo }}` |

> **Nota:** Necesitas crear la base de datos en Notion con esos campos y conectar tu integración de N8N.

---

## Nodo 5: Slack (Notificación)

| Campo | Valor |
|-------|-------|
| **Resource** | Message |
| **Operation** | Post |
| **Channel** | `#canal-de-notificaciones` |
| **Text** | Ver abajo |

**Mensaje:**

```
:inbox_tray: *Nuevo email con propuesta/cotización*

*Remitente:* {{ $json.nombreRemitente }} ({{ $json.emailRemitente }})
*Asunto:* {{ $json.asunto }}
*Fecha:* {{ $json.fecha }}

📌 Registro guardado en Notion
```

**Opcional - Block Builder (formato más rico):**

```json
{
  "blocks": [
    {
      "type": "header",
      "text": {
        "type": "plain_text",
        "text": "Nuevo email con propuesta/cotización"
      }
    },
    {
      "type": "section",
      "fields": [
        {
          "type": "mrkdwn",
          "text": "*Remitente:*\n{{ $json.nombreRemitente }}"
        },
        {
          "type": "mrkdwn",
          "text": "*Email:*\n{{ $json.emailRemitente }}"
        }
      ]
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "*Asunto:* {{ $json.asunto }}"
      }
    }
  ]
}
```

---

## ⚙️ Configuración previa necesaria

1. **Notion**: Crear una base de datos con las columnas indicadas + crear una integración en https://www.notion.so/my-integrations
2. **Slack**: Crear un app en https://api.slack.com/apps y obtener el token
3. **Gmail**: Autorizar tu cuenta en N8N (OAuth2)

---

## ⚠️ Consideraciones

- Si los emails son **HTML** (no plain text), el campo `body` puede traer el HTML crudo. Para limpiarlo podrías usar un nodo adicional con la librería **Turndown** o extraer solo el `text` si está disponible
- Si el **filtrop** no coincide con ninguno de los dos términos, el workflow **se detiene** en ese punto y no ejecuta Notion ni Slack (que es exactamente lo que querés)

¿Querés que ajuste algo, como agregar una condición extra al filtro o modificar el formato de la notificación en Slack?