# Muse Spark 1.2 — multi_turn/requirements_change

- model_id: `meta/muse-spark-1.2`
- success: True  | final: 5.98 | quality: 6.0
- latency_total: 9.468s | tokens_per_second: 123.0
- input_tokens: 226 | output_tokens: 1165

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

Perfecto, aquí tienes el workflow actualizado con Notion + Filtro + Slack.

Te dejo la estructura de 4 nodos:

### Estructura del Workflow

`[1. Gmail Trigger] -> [2. IF - Filtro] -> [3. Notion] -> [4. Slack]`

---

### 1. Gmail Trigger
Este es el que inicia todo.

* **Nodo:** `Gmail Trigger`
* **Credencial:** Conecta tu cuenta de Google OAuth2
* **Event:** `Message Received`
* **Simplify:** `Activado` - para que te devuelva los campos limpios

Te devolverá campos como: `from`, `subject`, `text`, `date`.

### 2. IF - Para filtrar por asunto
Solo deja pasar si el asunto contiene "propuesta" o "cotización".

* **Nodo:** `IF`
* **Condición:** `String` -> `Contains`
* **Valor 1:** `={{ $json.subject.toLowerCase() }}`
* **Operación:** `Contains`
* **Valor 2:** `propuesta`

Haz click en `Add Condition` y cambia a `OR`:

* **Valor 1:** `={{ $json.subject.toLowerCase() }}`
* **Operación:** `Contains`
* **Valor 2:** `cotizacion`

> Con `.toLowerCase()` nos aseguramos que detecte Propuesta, PROPUESTA, Cotización, COTIZACION, etc.

Conecta la salida `true` al siguiente nodo. La salida `false` la dejas vacía, así ignora el resto de emails.

### 3. Extraer datos y Guardar en Notion

Primero necesitas una Database en Notion con estas propiedades:
* `Nombre` - Title
* `Email` - Email
* `Asunto` - Text
* `Fecha` - Date
* `Snippet` - Text

* **Nodo:** `Notion` -> `Create a database page`
* **Credencial:** Conecta tu API Key de Notion y comparte la database con tu integración
* **Database:** Selecciona la que creaste

Mapea los campos así con expresiones:

* **Nombre:** `={{ $json.from.match(/(.*) <.*>/) ? $json.from.match(/(.*) <.*>/)[1].replace(/"/g, '') : $json.from }}`
* **Email:** `={{ $json.from.match(/<(.*)>/) ? $json.from.match(/<(.*)>/) [1] : $json.from }}`
* **Asunto:** `={{ $json.subject }}`
* **Fecha:** `={{ $json.date }}`
* **Snippet:** `={{ $json.snippet }}`

### 4. Slack - Notificación

* **Nodo:** `Slack` -> `Send a message`
* **Credencial:** Conecta tu Slack OAuth
* **Channel:** Selecciona tu canal, ej: `#ventas` o `#notificaciones`
* **Text:**
```
:Nueva Propuesta Recibida:
*De:* {{ $('Gmail Trigger').item.json.from }}
*Asunto:* {{ $('Gmail Trigger').item.json.subject }}
Ya está guardado en Notion.
```

> Importante: Conecta este nodo a la salida del nodo de Notion, así solo te notifica si se guardó correctamente.

¿Quieres que te genere el archivo `.json` del workflow listo para que lo importes directamente en N8N con un click?