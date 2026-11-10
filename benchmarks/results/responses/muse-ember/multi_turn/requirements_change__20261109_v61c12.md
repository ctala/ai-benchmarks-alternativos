# Muse Ember — multi_turn/requirements_change

- model_id: `meta/muse-ember`
- success: True  | final: 6.2 | quality: 6.0
- latency_total: 7.207s | tokens_per_second: 457.6
- input_tokens: 241 | output_tokens: 3298

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

Perfecto, lo cambiamos. Nada de Google Sheets.

Este es el workflow actualizado:

**Gmail Trigger -> Code (normalizar asunto) -> IF (filtro) -> Set (formatear) -> Notion -> Slack**

Solo guarda y notifica si el asunto contiene `propuesta` o `cotizacion`.

### Antes de armarlo, prepara esto:

1.  **En Notion:** Crea una base de datos tipo "Database" con estas propiedades: `Nombre` (Título), `Email` (Email), `Asunto` (Texto), `Fecha` (Fecha), `Snippet` (Texto). Luego en Notion ve a `Settings > Connections` y conecta tu integración a esa base de datos.
2.  **En Slack:** Invita a tu bot de n8n al canal donde quieres recibir avisos, por ejemplo `#ventas`.

### Paso a paso en n8n

**1. Gmail Trigger**
* Resource: `Message`
* Event: `Message Received`
* Poll Times: `Every Minute`
* Conecta tu cuenta de Gmail con OAuth2

**2. Code - Normalizar asunto**
Esto es para que detecte `Propuesta`, `PROPUESTA` o `propuesta` igual.
```javascript
const subject = ($json.subject || '').toLowerCase();
return [{ json: { ...$json, subject_lower: subject } }];
```

**3. IF - Filtro**
* Condition Type: String
* `{{ $json.subject_lower }}` **contains** `propuesta`
* Combinación: **OR**
* `{{ $json.subject_lower }}` **contains** `cotizacion`

La rama `true` sigue al siguiente nodo. La rama `false` no hace nada.

*Tip: Agrega una tercera condición OR con `cotización` con acento, mucha gente lo escribe así.*

**4. Set - Formatear datos**
Agrega estos campos para que Notion y Slack los usen fácil:
* `nombre`: `{{ $json.from.value[0].name }}`
* `email`: `{{ $json.from.value[0].address }}`
* `asunto`: `{{ $json.subject }}`
* `fecha`: `{{ $json.date }}`
* `snippet`: `{{ $json.snippet }}`

**5. Notion - Guardar**
* Credential: Tu API de Notion
* Resource: `Database`
* Operation: `Create a Page`
* Database: Selecciona la que creaste

Mapea las propiedades:
* `Nombre`: `{{ $json.nombre }}`
* `Email`: `{{ $json.email }}`
* `Asunto`: `{{ $json.asunto }}`
* `Fecha`: `{{ $json.fecha }}`
* `Snippet`: `{{ $json.snippet }}`

**6. Slack - Notificar**
* Credential: Tu Slack Bot
* Resource: `Message`
* Operation: `Send Message`
* Channel: `#ventas` (el tuyo)
* Text:
```
:bell: *Nuevo email con propuesta / cotización*

*De:* {{ $json.nombre }} <{{ $json.email }}>
*Asunto:* {{ $json.asunto }}
*Fecha:* {{ $json.fecha }}

{{ $json.snippet }}
```

Activa el workflow y pruébalo enviándote un email con asunto `Propuesta comercial`. Si funciona, verás la fila en Notion y el mensaje en Slack al instante.

¿Quieres que te pase el JSON de este workflow listo para importar a n8n?