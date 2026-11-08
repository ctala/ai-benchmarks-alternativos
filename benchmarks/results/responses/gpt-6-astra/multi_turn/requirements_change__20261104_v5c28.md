# GPT-6 Astra — multi_turn/requirements_change

- model_id: `openai/gpt-6-astra`
- success: True  | final: 5.28 | quality: 6.0
- latency_total: 22.206s | tokens_per_second: 51.5
- input_tokens: 226 | output_tokens: 1144

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

Claro. Sustituimos Google Sheets por **Notion** y añadimos el filtro y la notificación a **Slack**.

### Estructura del workflow

```text
Gmail Trigger → IF: asunto válido
                 ├─ true → Extraer datos → Notion → Slack
                 └─ false → Fin
```

## 1. Gmail Trigger — detectar emails nuevos

- Conecta tus credenciales de Gmail.
- Selecciona el evento **Message Received**.
- Configura la frecuencia de comprobación, por ejemplo, cada minuto.
- Si aparece la opción **Simplify**, actívala.

Haz una prueba para ver los campos que devuelve tu versión del nodo.

## 2. IF — filtrar por asunto

Añade una condición de tipo **Boolean → is true** con esta expresión:

```javascript
{{ /propuesta|cotizaci[oó]n/i.test($json.subject ?? $json.Subject ?? '') }}
```

Acepta asuntos como:

- `Nueva propuesta comercial`
- `Solicitud de cotizacion`
- `COTIZACIÓN del servicio`

No distingue mayúsculas y admite `cotizacion` con y sin tilde. Busca las palabras dentro del asunto, no en el cuerpo del mensaje.

> Si Gmail devuelve el asunto dentro de una estructura de cabeceras, ajusta la referencia usando el campo correspondiente de la salida del trigger.

## 3. Code — extraer los datos del remitente

Conecta la salida **true** al nodo **Code**, renómbralo `Extraer datos` y selecciona **Run Once for Each Item**.

Este código contempla remitentes en texto —`Nombre <email>`— o en un objeto estructurado:

```javascript
const msg = $json;
const from = msg.from ?? msg.From ?? '';
const sender = typeof from === 'object'
  ? (from.value?.[0] ?? from)
  : null;

const raw = typeof from === 'string' ? from.trim() : '';
const email = sender?.address
  ?? raw.match(/<([^>]+)>/)?.[1]
  ?? raw;

const nombre = sender?.name
  || (raw.includes('<')
    ? raw.split('<')[0].replace(/^"|"$/g, '').trim()
    : '');

return {
  json: {
    nombre,
    email,
    asunto: msg.subject ?? msg.Subject ?? '',
    gmailId: msg.id ?? '',
    recibidoEn: new Date().toISOString()
  }
};
```

`recibidoEn` registra cuándo lo procesó el workflow, no necesariamente la fecha original del correo.

## 4. Notion — crear un registro

Crea una base de datos en Notion con estas propiedades:

| Propiedad | Tipo | Valor en n8n |
|---|---|---|
| Asunto | Title | `{{ $json.asunto }}` |
| Nombre | Rich text | `{{ $json.nombre }}` |
| Email | Email | `{{ $json.email }}` |
| Recibido en | Date | `{{ $json.recibidoEn }}` |
| Gmail ID | Rich text | `{{ $json.gmailId }}` |

En el nodo **Notion**:

- Conecta tus credenciales.
- Selecciona **Database Page → Create**, o su equivalente en tu versión.
- Elige la base de datos y mapea las propiedades.

**Importante:** comparte la base de datos con la integración de Notion; de lo contrario, n8n no podrá acceder a ella.

## 5. Slack — enviar la notificación

Conecta Slack después de Notion, selecciona la operación para enviar un mensaje y elige el canal.

Texto sugerido:

```text
📩 Nuevo correo de propuesta o cotización

👤 Remitente: {{ $('Extraer datos').item.json.nombre }}
✉️ Email: {{ $('Extraer datos').item.json.email }}
📝 Asunto: {{ $('Extraer datos').item.json.asunto }}

✅ Guardado en Notion.
```

Referenciamos `Extraer datos` porque la salida de Notion ya contiene el registro creado, no los campos originales del correo.

### Antes de activarlo

Prueba con un correo que coincida y otro que no. Para evitar registros duplicados en reprocesamientos, puedes añadir una consulta a Notion por **Gmail ID** antes de crear cada registro.