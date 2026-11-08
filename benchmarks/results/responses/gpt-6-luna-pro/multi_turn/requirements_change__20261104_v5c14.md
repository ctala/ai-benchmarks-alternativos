# GPT-6 Luna Pro — multi_turn/requirements_change

- model_id: `openai/gpt-6-luna-pro`
- success: True  | final: 4.59 | quality: 4.0
- latency_total: 44.819s | tokens_per_second: 120.2
- input_tokens: 6285 | output_tokens: 5389

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

Puedes montarlo así:

```text
Gmail Trigger → IF (asunto válido) → Edit Fields
                                      ├→ Notion: Create Database Page
                                      └→ Slack: Send Message
```

### 1. Gmail Trigger

- Conecta tu cuenta de Gmail y configúralo para revisar mensajes nuevos.
- Si el nodo permite una consulta de búsqueda, usa:

```text
{subject:propuesta subject:cotizacion subject:cotización}
```

Esto reduce los mensajes que llegan al workflow. Añadiremos también un filtro en n8n para cubrir las variantes con y sin tilde.

### 2. IF: comprobar el asunto

Añade un nodo **IF** después del trigger y configura una condición de tipo **Boolean** con esta expresión:

```js
{{ /propuesta|cotizaci[oó]n/i.test($json.subject ?? '') }}
```

Conecta la salida **true** al siguiente nodo. La salida **false** puede quedar sin conectar.

### 3. Edit Fields: preparar los datos

Añade un nodo **Edit Fields (Set)** y crea estos campos. Los nombres disponibles pueden variar según la salida de tu Gmail Trigger; revisa su ejecución de prueba y ajusta las expresiones si hace falta.

| Campo | Expresión |
|---|---|
| `asunto` | `{{$json.subject}}` |
| `remitente` | `{{$json.from}}` |
| `fecha` | `{{$json.date}}` |
| `cuerpo` | `{{$json.text}}` |

A menudo Gmail entrega el remitente como `Nombre Apellido <correo@ejemplo.com>`. Si necesitas guardar el nombre y el email por separado, puedes añadir un nodo **Code** y extraerlos de ese campo.

### 4. Notion: guardar el email

Crea una base de datos en Notion, por ejemplo **Emails comerciales**, y añade propiedades como:

- **Asunto** — título
- **Remitente** — texto
- **Email** — texto
- **Fecha** — fecha
- **Cuerpo** — texto, opcional

Añade un nodo de Notion con la operación **Create Database Page** y asigna cada propiedad con los campos preparados en el paso anterior. Por ejemplo, para el título:

```text
{{$json.asunto}}
```

Selecciona la base de datos y verifica que la integración de Notion tenga acceso a ella.

### 5. Slack: enviar una notificación

Conecta otro nodo desde **Edit Fields** y selecciona **Send Message**. Elige el canal y usa, por ejemplo, este mensaje:

```text
Nuevo email relacionado con propuesta o cotización

De: {{$json.remitente}}
Asunto: {{$json.asunto}}
Fecha: {{$json.fecha}}
```

Configura las credenciales de Slack y asegúrate de que la app pueda publicar en el canal elegido.

Prueba el workflow con un email cuyo asunto contenga “propuesta” o “cotización”. Comprueba especialmente los nombres de los campos de Gmail antes de mapearlos en Notion y Slack, porque pueden variar según la configuración del trigger.