# Claude Sonnet 5.5 — multi_turn/requirements_change

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 4.2 | quality: 4.0
- latency_total: 16.919s | tokens_per_second: 143.2
- input_tokens: 365 | output_tokens: 2423

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

Con esos cambios, el flujo queda así:

```
Gmail Trigger → Filter → Code (extraer datos) → Notion → Slack
```

Pongo el filtro justo después del trigger para no procesar emails que no te interesan.

## 1. Gmail Trigger
- **Poll Time**: Every Minute (o lo que prefieras)
- **Event**: Message Received
- **Simplify**: activado
- **Filters → Label Names**: `INBOX` (para evitar spam o enviados)

## 2. Filter
Agrega dos condiciones combinadas con **OR**:
- `{{ $json.subject }}` → *contains* → `propuesta`
- `{{ $json.subject }}` → *contains* → `cotiz`

Activa **Ignore Case**. Usar `cotiz` en lugar de `cotizacion` cubre "cotización", "cotizacion" y "cotizaciones", así no dependes de las tildes.

## 3. Code (Run Once for Each Item)

```javascript
const subject = $json.subject || $json.Subject || '';
const fromField = $json.from || $json.From;

let name = '';
let email = '';

if (fromField?.value?.[0]) {
  name = fromField.value[0].name;
  email = fromField.value[0].address;
} else {
  const raw = typeof fromField === 'string' ? fromField : (fromField?.text || '');
  const match = raw.match(/^(.*?)\s*<(.+?)>$/);
  if (match) {
    name = match[1].replace(/"/g, '').trim();
    email = match[2];
  } else {
    email = raw.trim();
  }
}

return {
  json: {
    name: name || email,
    email,
    subject,
    date: $json.date ? new Date($json.date).toISOString() : new Date().toISOString(),
    snippet: $json.snippet || '',
    messageId: $json.id
  }
};
```

El código contempla las dos estructuras que puede devolver el nodo de Gmail. Ejecuta el trigger una vez y revisa el output real para confirmar los nombres de los campos.

## 4. Notion
**Preparación previa:**
1. Crea una integración en notion.so/my-integrations y copia el token.
2. Crea una base de datos con estas propiedades:
   - `Nombre` (Title)
   - `Email` (Email)
   - `Asunto` (Text)
   - `Fecha` (Date)
3. En la base de datos, ve a **⋯ → Connections** y agrega tu integración. Sin esto, N8N no la verá.

**Nodo:**
- **Resource**: Database Page
- **Operation**: Create
- **Database**: selecciónala de la lista
- **Properties**:
  - Nombre → `{{ $json.name }}`
  - Email → `{{ $json.email }}`
  - Asunto → `{{ $json.subject }}`
  - Fecha → `{{ $json.date }}`

## 5. Slack
- **Resource**: Message → **Send**
- **Channel**: el canal donde quieres el aviso
- **Text**:

```
📩 *Nuevo email relevante*
*De:* {{ $('Code').item.json.name }} ({{ $('Code').item.json.email }})
*Asunto:* {{ $('Code').item.json.subject }}
```

Cambia `'Code'` por el nombre real de tu nodo si lo renombraste. Referenciar el nodo Code es necesario porque el output del nodo Notion no incluye esos campos tal cual.

Para las credenciales, usa una Slack App con el scope `chat:write` e invita el bot al canal (`/invite @tu-bot`).

## Recomendaciones
- **Duplicados**: Gmail Trigger no suele repetir emails, pero si reactivas el workflow tras una pausa puede reprocesar algunos. Guardar `messageId` en Notion como propiedad de texto te permite detectarlos.
- **Errores**: crea un Error Workflow con una notificación a Slack para enterarte si falla Notion o Slack.

¿Quieres que te arme el JSON del workflow para importarlo directamente en N8N?