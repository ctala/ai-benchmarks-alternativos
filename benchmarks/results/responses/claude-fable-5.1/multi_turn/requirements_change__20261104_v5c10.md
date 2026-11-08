# Claude Fable 5.1 — multi_turn/requirements_change

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 3.84 | quality: 4.0
- latency_total: 18.203s | tokens_per_second: 75.4
- input_tokens: 365 | output_tokens: 1372

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

Sin problema, el cambio es sencillo. El flujo quedaria asi:

**Gmail Trigger → IF (filtro) → Notion (crear pagina) → Slack (notificacion)**

## 1. Gmail Trigger
- Evento: *Message Received*
- Polling: cada minuto (o el intervalo que prefieras)
- Opcional: en el campo *Search* puedes poner directamente `subject:(propuesta OR cotizacion)` para que Gmail ya filtre desde el origen y ahorres ejecuciones. Si haces esto, el nodo IF se vuelve opcional, pero lo dejo por si quieres control adicional.

## 2. IF node (filtro por asunto)
- Condicion tipo *String* → *Contains*
- Valor 1: `{{ $json.subject.toLowerCase() }}`
- Valor 2: `propuesta`
- Agrega una segunda condicion igual con `cotizacion`
- Combinar con **OR**

Ojo: usa `toLowerCase()` para que detecte "Propuesta", "PROPUESTA", etc. Si quieres cubrir "cotización" con tilde, agrega una tercera condicion.

## 3. Notion node (rama *true*)
- Operacion: *Database Page → Create*
- Selecciona tu base de datos de Notion
- Mapea las propiedades:
  - **Nombre** (title): `{{ $json.from.value[0].name }}`
  - **Email**: `{{ $json.from.value[0].address }}`
  - **Asunto**: `{{ $json.subject }}`
  - **Fecha**: `{{ $json.date }}`
  - **Cuerpo** (opcional, texto): `{{ $json.text }}`

Antes de esto, crea en Notion una base de datos con esas columnas y comparte la pagina con tu integracion (en Notion: *Conexiones → agregar tu integracion*), si no, N8N no la vera.

## 4. Slack node
- Operacion: *Message → Send*
- Canal: el que quieras (ej. `#ventas`)
- Texto, por ejemplo:
```
Nueva {{ $('Gmail Trigger').item.json.subject.toLowerCase().includes('propuesta') ? 'propuesta' : 'cotizacion' }} recibida
De: {{ $('Gmail Trigger').item.json.from.value[0].name }} ({{ $('Gmail Trigger').item.json.from.value[0].address }})
Asunto: {{ $('Gmail Trigger').item.json.subject }}
Ver en Notion: {{ $json.url }}
```

Uso `$('Gmail Trigger')` porque el nodo Slack recibe la salida de Notion, no del Gmail. El `$json.url` viene de Notion y te da el link directo a la pagina creada.

## Credenciales que necesitas
- Gmail (OAuth2)
- Notion (Internal Integration Token)
- Slack (OAuth2 o Bot Token con permiso `chat:write`)

Un detalle: la estructura `from.value[0]` depende de la version del nodo Gmail. Si al ejecutar ves que el remitente viene como un string tipo `"Juan <juan@mail.com>"`, avisame y te paso una expresion para separarlo.

Quieres que te genere el JSON del workflow completo para importarlo directamente?