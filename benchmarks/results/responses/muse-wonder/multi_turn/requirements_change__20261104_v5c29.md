# Muse Wonder — multi_turn/requirements_change

- model_id: `meta/muse-wonder`
- success: True  | final: 5.53 | quality: 6.0
- latency_total: 15.036s | tokens_per_second: 111.4
- input_tokens: 241 | output_tokens: 1675

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

Perfecto, ese cambio tiene mucho más sentido para propuestas/cotizaciones. El workflow quedaría así:

**Gmail Trigger -> IF (Filtro) -> Code (Extraer remitente) -> Notion (Crear registro) -> Slack (Notificar)**

Te lo armo paso a paso:

### 1. Gmail Trigger
Este será el inicio. No uses un nodo normal de Gmail, usa el Trigger para que se ejecute solo.

Configuración:
- **Event:** Message Received
- **Poll Times:** Every Minute
- **Credentials:** Tu cuenta de Google

> Tip pro: En este mismo nodo, en `Options > Search` puedes poner esto para ahorrar ejecuciones:
> `subject:(propuesta OR cotizacion OR cotización)`

### 2. Nodo IF - El filtro
Por seguridad, agregamos un filtro por si llega algo raro.

- **Condition:** String
- **Value 1:** `{{ $json.subject }}`
- **Operation:** Matches Regex
- **Regex:** `(?i)(propuesta|cotizacion|cotización)`

Si es `false`, el workflow se detiene. Si es `true`, sigue.

### 3. Nodo Code - Extraer datos del remitente
El remitente viene así: `"Juan Pérez <juan@empresa.com>"`. Necesitamos separarlo.

Crea un nodo **Code** y pega esto:

```javascript
const item = $input.first().json;

const fromRaw = item.from?.text || item.from?.value?.[0]?.address || '';
let nombre = '';
let email = '';

const match = fromRaw.match(/(.*)<(.*)>/);
if (match) {
  nombre = match[1].trim().replace(/"/g, '');
  email = match[2].trim();
} else {
  email = fromRaw.trim();
  nombre = email.split('@')[0];
}

return [{
  json: {
    nombre: nombre || 'Sin nombre',
    email: email,
    asunto: item.subject || 'Sin asunto',
    fecha: new Date().toISOString(),
    gmailId: item.id
  }
}];
```

### 4. Nodo Notion - Guardar en tu base
Primero crea una base de datos en Notion con estas propiedades exactas:

| Propiedad | Tipo en Notion |
| :--- | :--- |
| **Nombre** | Title |
| **Email** | Email |
| **Asunto** | Text |
| **Fecha** | Date |
| **Estado** | Select (ponle opción: `Nuevo`) |

Luego en el nodo **Notion**:
- **Resource:** Database Page
- **Operation:** Create
- **Database ID:** Selecciona tu base (te la detecta si conectaste la credencial)
- Mapea los campos:
  - `Nombre` -> `{{ $json.nombre }}`
  - `Email` -> `{{ $json.email }}`
  - `Asunto` -> `{{ $json.asunto }}`
  - `Fecha` -> `{{ $json.fecha }}`
  - `Estado` -> `Nuevo`

### 5. Nodo Slack - Notificación
Al final, conecta un nodo **Slack**:

- **Operation:** Send a Message
- **Channel:** Elige tu canal, ej: `#ventas` o `#propuestas`
- **Message Text:**

```
:email: *Nueva propuesta recibida*

*De:* {{ $('Code').item.json.nombre }} ({{ $('Code').item.json.email }})
*Asunto:* {{ $('Code').item.json.asunto }}
*Fecha:* {{ $('Code').item.json.fecha }}

Ya fue guardada en Notion.
```

Y listo. Activa el workflow arriba a la derecha en **Active**.

¿Quieres que te genere el JSON completo para que lo importes en tu N8N con `Ctrl+V` y solo tengas que conectar tus credenciales de Gmail, Notion y Slack?