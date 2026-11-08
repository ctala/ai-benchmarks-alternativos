# Grok 4.7 — multi_turn/requirements_change

- model_id: `x-ai/grok-4.7`
- success: True  | final: 4.26 | quality: 4.0
- latency_total: 12.545s | tokens_per_second: 73.3
- input_tokens: 1461 | output_tokens: 919

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

Sí, se puede armar con un flujo lineal y un filtro por asunto. Queda así:

**Gmail Trigger → IF (asunto) → Notion → Slack**

### 1. Gmail Trigger
- **Event:** Message Received
- **Simplify:** activado (más fácil de mapear)
- Opcional: en **Search** pon algo como `subject:(propuesta OR cotizacion)` para filtrar ya en Gmail y no procesar el resto

Campos útiles del item:
- `{{ $json.from }}` — remitente (a veces viene como `Nombre <email@dominio.com>`)
- `{{ $json.subject }}`
- `{{ $json.date }}` o `{{ $json.internalDate }}`
- `{{ $json.snippet }}` o `{{ $json.text }}` si quieres un extracto

Si necesitas nombre y email por separado, un **Code** o **Set** antes del IF:

```javascript
const from = $json.from || '';
const match = from.match(/^(?:"?([^"]*)"?\s)?<?([^>]+)>?$/);
return [{
  json: {
    ...$json,
    senderName: (match?.[1] || from).trim(),
    senderEmail: (match?.[2] || from).trim(),
  }
}];
```

### 2. IF — solo “propuesta” o “cotización”
- **Condition:** String → **contains** (o usa dos condiciones con **OR**)
- Valor: `{{ $json.subject }}`
- Palabra 1: `propuesta`
- Palabra 2: `cotizacion` (y, si quieres, también `cotización`)

Activa **Ignore Case**. La rama **true** sigue; la **false** no conecta a nada.

### 3. Notion — Create Database Page
Conecta la credencial de Notion e invita la integración a la base.

Mapea propiedades, por ejemplo:
- **Nombre / Title:** `{{ $json.subject }}`
- **Email:** `{{ $json.senderEmail }}`
- **Remitente:** `{{ $json.senderName }}`
- **Fecha:** `{{ $json.date }}`
- **Extracto:** `{{ $json.snippet }}`

Los tipos tienen que coincidir (title, email, rich text, date). Si la fecha de Gmail no entra bien en un campo Date, guárdala como texto o normalízala en el nodo Code.

### 4. Slack — Send Message
En la misma rama true, después de Notion (o en paralelo si no te importa el orden):

- **Channel:** el canal o tu user ID para DM
- **Text:** algo como:

```
Nueva propuesta/cotización
De: {{ $json.senderName }} <{{ $json.senderEmail }}>
Asunto: {{ $json.subject }}
```

### Orden recomendado
1. Gmail Trigger  
2. Code (separar nombre/email) — opcional  
3. IF por asunto  
4. Notion  
5. Slack  

Activa el workflow y mándate un correo de prueba con “propuesta” o “cotizacion” en el asunto.

Si me pasas los nombres exactos de las propiedades de tu base de Notion (y si el título es “Name” u otro), te dejo el mapeo campo por campo.