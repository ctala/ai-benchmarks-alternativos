# Muse Spark 1.3 — multi_turn/requirements_change

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 5.77 | quality: 6.0
- latency_total: 16.073s | tokens_per_second: 143.0
- input_tokens: 240 | output_tokens: 2299

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

Perfecto, lo actualizamos. Olvidamos Google Sheets y nos vamos con esta arquitectura:

**Gmail Trigger -> Filtro (IF) -> Extraer Datos (Code) -> Notion -> Slack**

Aquí te lo dejo listo para armar en 10 minutos:

### 0. Lo que necesitas tener listo antes

1.  **Notion:** Crea una Database con estas propiedades:
    * `Nombre` (Title)
    * `Email` (Email)
    * `Asunto` (Text)
    * `Fecha` (Date)
    * `Snippet` (Text)
    Luego crea una Integration en notion.so/my-integrations, compártela con esa database y conecta esa API Key en n8n como credencial Notion.
2.  **Credenciales en n8n:** Gmail OAuth2, Notion API, y Slack OAuth2.

### 1. Gmail Trigger - Lee emails
* Nodo: `Gmail Trigger`
* Event: `Message Received`
* Poll Times: `Every Minute`
* No pongas filtros aquí, queremos traer todo y filtrar después.

Te va a devolver un JSON con `from`, `subject`, `snippet`, `date`, `text`, etc.

### 2. IF - Filtra solo 'propuesta' o 'cotizacion'
* Nodo: `IF`
* Combinator: `OR`
* Condiciones (desactiva `Case Sensitive`):
    1. `{{ $json.subject }}` **contains** `propuesta`
    2. `{{ $json.subject }}` **contains** `cotizacion`
    3. `{{ $json.subject }}` **contains** `cotización` (para cubrir el acento)

Conecta la salida `true` al siguiente paso. La salida `false` la dejas vacía.

### 3. Code - Extrae los datos del remitente
El campo `from` a veces viene como `"Juan Perez <juan@empresa.com>"`. Usa este nodo `Code` (JavaScript) para limpiarlo:

```javascript
const item = $input.first().json;
const fromRaw = item.from?.value?.[0]?.address || item.from || "";
const nameRaw = item.from?.value?.[0]?.name || "";

// Si viene como texto, lo parseamos
let email = fromRaw;
let name = nameRaw;
const match = String(fromRaw).match(/(.*)<(.*)>/);
if (match) {
  name = name || match[1].trim().replace(/"/g, '');
  email = match[2].trim();
}

return [{
  json: {
    nombre: name || email.split('@')[0],
    email: email,
    asunto: item.subject,
    fecha: item.date,
    snippet: item.snippet || item.text?.substring(0, 200)
  }
}];
```

### 4. Notion - Guarda el lead
* Nodo: `Notion`
* Resource: `Database Page`
* Operation: `Create`
* Database: Selecciona la que creaste
* Mapea las columnas:
    * `Nombre`: `{{ $json.nombre }}`
    * `Email`: `{{ $json.email }}`
    * `Asunto`: `{{ $json.asunto }}`
    * `Fecha`: `{{ $json.fecha }}`
    * `Snippet`: `{{ $json.snippet }}`

### 5. Slack - Notifícate
Conecta este nodo DESPUÉS de Notion.
* Nodo: `Slack`
* Resource: `Message`
* Operation: `Send`
* Send to: `Channel` -> elige `#ventas` o tu canal
* Text:
```
:Nueva propuesta recibida!:
*De:* {{ $('Extraer Datos').item.json.nombre }} ({{ $('Extraer Datos').item.json.email }})
*Asunto:* {{ $('Extraer Datos').item.json.asunto }}
Ya guardado en Notion.
```

> Tip de emprendedor: Activa el workflow (toggle arriba a la derecha en `Active`) y mándate un email de prueba con asunto "propuesta de prueba" para verificar que llega a Notion y a Slack.

¿Quieres que te genere el JSON completo para que lo importes directamente con Copy/Paste en n8n?