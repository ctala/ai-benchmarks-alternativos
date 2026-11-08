# GPT-6 Luna — multi_turn/requirements_change

- model_id: `openai/gpt-6-luna`
- success: True  | final: 4.76 | quality: 4.0
- latency_total: 13.139s | tokens_per_second: 93.1
- input_tokens: 226 | output_tokens: 1223

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

Configúralo así:

**Gmail Trigger → Edit Fields/Code → Notion → Slack**

### 1. Gmail Trigger

- Conecta tu cuenta de Gmail y elige el evento de correo nuevo.
- Configura la frecuencia de comprobación.
- En el campo **Search/Query**, usa:

```text
{subject:propuesta subject:cotizacion subject:cotización}
```

Las llaves indican que Gmail debe buscar cualquiera de esos términos en el asunto. Incluí las dos formas de “cotización” por si los correos llegan con o sin tilde.

### 2. Extraer los datos del remitente

Añade un nodo **Code** después del trigger. Este código contempla tanto una salida simplificada como los encabezados habituales de Gmail:

```javascript
const data = $json;

function getHeader(name) {
  const headers = data.payload?.headers ?? [];
  return headers.find(h => h.name?.toLowerCase() === name.toLowerCase())?.value ?? '';
}

const from = data.from ?? getHeader('From');
const match = from.match(/^(.*?)\s*<([^>]+)>$/);

return [{
  json: {
    senderName: match ? match[1].replace(/^"|"$/g, '').trim() : from,
    senderEmail: match ? match[2].trim() : from,
    subject: data.subject ?? getHeader('Subject'),
    receivedAt: data.date ?? getHeader('Date') ?? '',
    gmailId: data.id ?? ''
  }
}];
```

Ejecuta el workflow una vez y revisa la salida del Gmail Trigger; si los datos aparecen con una estructura distinta, habrá que ajustar las rutas del código.

### 3. Crear el registro en Notion

1. Crea una base de datos en Notion con propiedades como:
   - **Nombre** — título
   - **Email** — texto
   - **Asunto** — texto
   - **Fecha de recepción** — fecha
   - **Gmail ID** — texto
2. Comparte esa base de datos con la integración de Notion que uses en n8n.
3. Añade un nodo **Notion** y selecciona la operación para crear una página en una base de datos.
4. Mapea las propiedades con estos valores:

```text
Nombre:             {{ $json.senderName }}
Email:              {{ $json.senderEmail }}
Asunto:             {{ $json.subject }}
Fecha de recepción: {{ $json.receivedAt }}
Gmail ID:           {{ $json.gmailId }}
```

Los nombres deben coincidir con las propiedades de tu base de datos.

### 4. Enviar la notificación a Slack

Añade un nodo **Slack** después de Notion, con la operación de enviar un mensaje. Elige el canal y usa un mensaje como:

```text
Nuevo email de propuesta/cotización

Remitente: {{ $('Code').item.json.senderName }} <{{ $('Code').item.json.senderEmail }}>
Asunto: {{ $('Code').item.json.subject }}
Recibido: {{ $('Code').item.json.receivedAt }}
```

Sustituye `Code` por el nombre real de tu nodo si lo cambiaste. Si prefieres que Slack avise aunque falle la creación en Notion, conecta Gmail/Code a Notion y Slack en ramas separadas.