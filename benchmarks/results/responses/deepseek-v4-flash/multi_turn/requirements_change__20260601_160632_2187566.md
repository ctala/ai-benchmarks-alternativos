# DeepSeek V4 Flash (OpenRouter) — multi_turn/requirements_change

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 5.8 | quality: 4.44
- latency_total: 32.146s | tokens_per_second: 56.4
- input_tokens: 244 | output_tokens: 1814
- judge_score: 1.8 | justificación: 

## Respuesta completa

Perfecto, ajustemos el workflow a Notion y Slack. Aquí tienes la estructura completa:

## Workflow N8N: Emails → Notion + Slack

### Nodos necesarios:

1. **Gmail Trigger** (nuevo email)
2. **IF** (filtro por asunto)
3. **Function** (extraer datos del remitente)
4. **Notion** (crear página en base de datos)
5. **Slack** (enviar notificación)

---

## 1. Gmail Trigger

- **Event**: `message received`
- **Credenciales**: OAuth2 de Gmail (debes configurar con alcance `https://www.googleapis.com/auth/gmail.readonly`)
- **Filter**: Deja vacío para recibir todos los correos (el filtro lo hará el nodo IF)

---

## 2. Nodo IF (Filtro por asunto)

- **Condición**: `String` → `Contains`
- **Value 1**: `{{ $json.subject }}` (o `{{ $json["subject"] }}`)
- **Value 2**: `propuesta`
- **Operación**: `OR` (añadir segunda condición)
- **Segunda condición**: misma lógica con `cotizacion`

**Importante**: Para que sea case-insensitive, usa una **Function** en lugar de IF, o convierte a minúsculas. Recomiendo:

### Alternativa: Nodo Function para filtro

```javascript
const subject = $json.subject.toLowerCase();
const keywords = ['propuesta', 'cotizacion'];
if (keywords.some(k => subject.includes(k))) {
  return $json;
}
return null; // descarta
```

Luego conectas la salida al siguiente nodo.

---

## 3. Nodo Function (Extraer datos del remitente)

Objetivo: parsear `from` (ej: `"Juan Pérez" <juan@email.com>`) en nombre y email.

```javascript
const from = $json.from;
// Patrón para extraer nombre y email
const match = from.match(/^(?:"?([^"]*)"?\s*)?<?([^>]+)>?$/);
const name = match && match[1] ? match[1].trim() : (match && match[2] ? match[2] : '');
const email = match && match[2] ? match[2] : from;

return {
  ...$json,
  remitenteNombre: name,
  remitenteEmail: email,
  fecha: $json.date || new Date().toISOString(),
  asunto: $json.subject,
  snippet: $json.text || $json.snippet || '' // opcional
};
```

---

## 4. Nodo Notion (Crear página en base de datos)

- **Credenciales**: Notion API (Internal Integration Token). Debes compartir la base de datos con la integración.
- **Operación**: `Create a database page`
- **Database ID**: ID de tu base de datos Notion (de la URL: `https://www.notion.so/workspace/DB_ID?v=...`)
- **Properties** (ejemplo):

| Propiedad | Tipo | Valor |
|-----------|------|-------|
| **Título** (title) | title | `{{ $json.asunto }}` |
| **Remitente** | rich_text | `{{ $json.remitenteNombre }}` |
| **Email** | email | `{{ $json.remitenteEmail }}` |
| **Fecha** | date | `{{ $json.fecha }}` |
| **Estado** | select | `Nuevo` (valor fijo) |
| **Enlace** | url | `{{ $json.id }}` (ID del email de Gmail, puedes construir enlace: `https://mail.google.com/mail/u/0/#inbox/{{ $json.id }}`) |

---

## 5. Nodo Slack (Enviar notificación)

- **Credenciales**: Slack OAuth (alcance `chat:write`)
- **Channel**: `#propuestas` (o el que quieras)
- **Message**: Un bloque de texto con formato.

Ejemplo de mensaje simple:

```
📩 *Nueva propuesta/cotización recibida*
• *De:* {{ $json.remitenteNombre }} ({{ $json.remitenteEmail }})
• *Asunto:* {{ $json.asunto }}
• *Ver en Gmail:* <https://mail.google.com/mail/u/0/#inbox/{{ $json.id }}|Abrir>
```

O puedes usar bloques más elaborados:

```json
{
  "blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "*Nueva propuesta/cotización*"
      }
    },
    {
      "type": "section",
      "fields": [
        { "type": "mrkdwn", "text": "*Remitente:*\n{{ $json.remitenteNombre }}" },
        { "type": "mrkdwn", "text": "*Email:*\n{{ $json.remitenteEmail }}" }
      ]
    },
    {
      "type": "section",
      "text": { "type": "mrkdwn", "text": "*Asunto:*\n{{ $json.asunto }}" }
    },
    {
      "type": "actions",
      "elements": [
        {
          "type": "button",
          "text": { "type": "plain_text", "text": "Abrir en Gmail" },
          "url": "https://mail.google.com/mail/u/0/#inbox/{{ $json.id }}"
        }
      ]
    }
  ]
}
```

---

## Consideraciones adicionales

- **Rate limiting**: Gmail Trigger tiene límite de 1 consulta cada 1-5 minutos. Si necesitas tiempo real, considera usar Webhook de Gmail (Pub/Sub), pero es más complejo.
- **IDs de Gmail**: El `id` del email es único. Puedes usarlo para evitar duplicados en Notion (verificar si existe antes de crear).
- **Cuerpo del email**: Si necesitas extraer el cuerpo, usa el nodo `Gmail` con operación `Get` y pasa el `messageId`. Pero el trigger ya trae `text` (cuerpo plano) y `html` (HTML). Puedes incluirlos en Notion como campo `rich_text`.

¿Quieres que profundice en algún punto en particular, como la autenticación de Notion o la lógica anti-duplicados?