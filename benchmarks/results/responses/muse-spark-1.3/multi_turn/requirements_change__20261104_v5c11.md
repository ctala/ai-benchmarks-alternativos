# Muse Spark 1.3 — multi_turn/requirements_change

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 4.46 | quality: 4.0
- latency_total: 12.213s | tokens_per_second: 119.6
- input_tokens: 241 | output_tokens: 1461

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

Perfecto, hacemos ese cambio. Este workflow hace exactamente eso:

**Gmail -> Filtro (propuesta / cotización) -> Notion -> Slack**

Aquí tienes la estructura completa:

### 1. Gmail Trigger - Leer emails
1. Agrega un nodo **Gmail Trigger**
2. Evento: `Message Received`
3. En `Simplify` déjalo en ON para que te dé `from, subject, date` ya parseados
4. Conecta tu cuenta de Gmail con OAuth2

El output de cada email será algo así:
`from.value[0].address`, `from.value[0].name`, `subject`, `snippet`, `date`

### 2. Filter - Filtrar solo propuesta / cotizacion
Agrega un nodo **IF** (en las nuevas versiones se llama **Filter**) después del Gmail Trigger.

Condición: `OR`
1. `{{ $json.subject.toLowerCase() }}` **contains** `propuesta`
2. `{{ $json.subject.toLowerCase() }}` **contains** `cotizacion`

Usamos `.toLowerCase()` para que detecte Propuesta, PROPUESTA, Cotización, cotizacion, etc.

Conecta la salida `true` al siguiente paso. La salida `false` la dejas vacía.

### 3. Set - Extraer datos del remitente
Agrega un nodo **Set (Edit Fields)** para dejar los datos limpios:

- `nombre` = `{{ $json.from.value[0].name }}`
- `email` = `{{ $json.from.value[0].address }}`
- `asunto` = `{{ $json.subject }}`
- `fecha` = `{{ $json.date }}`
- `resumen` = `{{ $json.snippet }}`
- `gmail_id` = `{{ $json.id }}`

Esto te evita problemas si cambia el formato de Gmail.

### 4. Notion - Guardar en base de datos
Antes de esto, en Notion crea una Database con estas propiedades:
`Nombre (Title), Email (Email), Asunto (Text), Fecha (Date), Resumen (Text), GmailID (Text)`

Luego en n8n:
1. Agrega nodo **Notion**
2. Acción: `Create a database page`
3. Selecciona tu Database
4. Mapea:
   - Nombre: `{{ $json.nombre }}`
   - Email: `{{ $json.email }}`
   - Asunto: `{{ $json.asunto }}`
   - etc.

### 5. Slack - Notificación
Agrega un nodo **Slack** después de Notion:
1. Acción: `Send a message`
2. Canal: `#ventas` o el que uses
3. Mensaje:
```
:Nueva propuesta recibida:
*De:* {{ $json.nombre }} ({{ $json.email }})
*Asunto:* {{ $json.asunto }}
*Fecha:* {{ $json.fecha }}
Revisado en Notion ✅
```

Conecta: `Gmail Trigger -> IF (true) -> Set -> Notion -> Slack`

¿Quieres que te genere el JSON listo para importar a n8n con estos 5 nodos ya conectados?