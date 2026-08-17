# Nex-N2-Mini — multi_turn/requirements_change

- model_id: `nex-agi/nex-n2-mini`
- success: True  | final: 4.87 | quality: 4.0
- latency_total: 39.78s | tokens_per_second: 196.8
- input_tokens: 232 | output_tokens: 7830

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

Sí, perfecto. Te queda un workflow así:

```text
Gmail Trigger → IF filtro de asunto → Function extraer remitente → Notion
                                                       └→ Slack
```

## 1. Gmail Trigger

Crea un nodo **Gmail Trigger**.

Configuración:

- **Trigger**: `New Email`
- **Polling**: cada 1 minuto o según prefieras
- **Folder/Label**: `Inbox` o la carpeta que uses
- **OAuth2**: credencial de Gmail conectada

Este nodo capturará cada email nuevo.

---

## 2. IF node: filtrar asunto

Añade un nodo **IF**.

En **Return**, selecciona:

```text
boolean
```

En **Expression**, usa:

```js
=String($json.subject || '').toLowerCase().includes('propuesta') || String($json.subject || '').toLowerCase().includes('cotizacion') || String($json.subject || '').toLowerCase().includes('cotización')
```

Así filtra emails cuyo asunto contenga:

- `propuesta`
- `cotizacion`
- `cotización`

Si no quieres considerar la palabra con tilde, elimina esta parte:

```js
String($json.subject || '').toLowerCase().includes('cotización')
```

---

## 3. Function node: extraer remitente

Añade un nodo **Function** después del IF.

Pega este código:

```js
const rawFrom = $json.from || ($json.headers && $json.headers.from) || '';

if (typeof rawFrom === 'object') {
  rawFrom = rawFrom.address || rawFrom.email || rawFrom.name || '';
}

let senderName = rawFrom;
let senderEmail = rawFrom;

const match = rawFrom.match(/<([^>]+)>/);

if (match) {
  senderEmail = match[1];
  senderName = rawFrom.replace(/<[^>]+>/g, '').trim() || rawFrom;
}

return [
  {
    json: {
      email_id: $json.id,
      thread_id: $json.threadId,
      sender: senderName,
      sender_email: senderEmail,
      subject: $json.subject || '',
      received_date: $json.date ? new Date($json.date).toISOString() : null,
      body: $json.body || '',
      url: $json.url || `https://mail.google.com/mail/u/0/#inbox/${$json.id}`
    }
  }
];
```

Este nodo deja estos campos listos:

```text
sender
sender_email
subject
received_date
body
url
```

---

## 4. Notion: guardar datos del email

Añade un nodo **Notion** → **Create Page**.

Antes, crea una base de datos en Notion con campos como:

| Campo Notion | Tipo |
|---|---|
| Nombre remitente | Title |
| Email remitente | Email |
| Asunto | Title |
| Fecha recepción | Date |
| ID email | Rich text |
| Cuerpo email | Text |
| Link email | URL |

Luego mapea los datos así:

```text
Nombre remitente: {{$json.sender}}
Email remitente: {{$json.sender_email}}
Asunto: {{$json.subject}}
Fecha recepción: {{$json.received_date}}
ID email: {{$json.email_id}}
Cuerpo email: {{$json.body}}
Link email: {{$json.url}}
```

Si Notion te pide el campo Date en formato específico, usa algo como:

```js
{{ {"start": $json.received_date, "time_zone": "America/Mexico_City"} }}
```

---

## 5. Slack: notificación

Añade un nodo **Slack** → **Send Message**.

Configuración:

- **Channel**: por ejemplo `#notificaciones-email`
- **Message**:

```text
📨 Nuevo email detectado

Asunto: {{$json.subject}}

Remitente: {{$json.sender}} <{{$json.sender_email}}>
Fecha: {{$json.received_date}}
Link: {{$json.url}}
```

Este nodo solo se ejecutará cuando el email pase el filtro del nodo IF.

---

## Flujo final

```text
1. Gmail Trigger
2. IF
   - Filtro: asunto contiene propuesta, cotizacion o cotización
3. Function
   - Extraer sender y sender_email
4. Notion Create Page
   - Guardar email en base de datos
5. Slack Send Message
   - Enviar alerta
```

## Prueba rápida

1. Envía un email con asunto:

```text
Propuesta comercial
```

Deberías recibir:

- Una fila nueva en Notion
- Un mensaje en Slack

2. Envía otro email con asunto:

```text
Reunión mañana
```

No debería hacer nada.

Recuerda compartir la base de datos de Notion con la integración de Notion y dar permisos al Slack App para publicar mensajes en el canal.