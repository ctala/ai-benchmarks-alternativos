# DeepSeek V4 Pro (0813) — multi_turn/requirements_change

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 5.77 | quality: 6.0
- latency_total: 39.583s | tokens_per_second: 58.1
- input_tokens: 323 | output_tokens: 2301

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

¡Perfecto! Cambiamos el destino a Notion, agregamos filtro por asunto y notificación a Slack. Aquí tienes el flujo completo en N8N con los nodos necesarios y su configuración básica.

---

### Estructura del workflow

1. **Gmail Trigger** (activador) – con filtro de búsqueda para solo capturar correos con “propuesta” o “cotización” en el asunto.
2. **Function** (opcional pero útil) – para extraer y limpiar los datos del remitente y del correo.
3. **Notion** – crea una nueva página en una base de datos con los datos extraídos.
4. **Slack** – envía un mensaje al canal que elijas avisando que llegó un correo relevante.

---

### Paso a paso

#### 1. Nodo Gmail Trigger

- **Tipo**: `Gmail Trigger` (puede ser “On new email” o “Polling”).
- **Autenticación**: Conéctalo a tu cuenta de Gmail mediante OAuth2.
- **Parámetro clave**: En el campo **Search** (o **Query**) escribe:
  ```
  subject:(propuesta OR cotizacion)
  ```
  Esto hará que Gmail solo devuelva los correos cuyo asunto contenga esas palabras, usando los operadores de búsqueda nativos de Gmail.
- **Opciones adicionales**: Puedes definir cada cuánto tiempo revisa (por ejemplo, cada minuto) y si quieres marcar los correos como leídos o no.

Con este filtro, no necesitas un nodo IF separado; el trigger solo traerá los correos que cumplan la condición.

#### 2. Nodo Function

Este nodo toma la salida del trigger y extrae los datos que necesitas. La salida del trigger incluye un campo `from` con formato tipo `"Nombre Apellido <email@dominio.com>"`, así que lo dividimos.

Pega este código en el nodo Function (modo “Run Once for All Items” o “Run Once for Each Item”, según prefieras; para simplificar usaré “Run Once for All Items”):

```javascript
// Recibe los items del trigger
const items = $input.all();
const newItems = [];

for (const item of items) {
  const emailData = item.json;
  
  // Extraer nombre y email del remitente
  let from = emailData.from || '';
  let senderName = '';
  let senderEmail = '';
  
  // Formato típico: "Nombre <email>" o solo "email"
  const match = from.match(/^(.*)<(.+)>$/);
  if (match) {
    senderName = match[1].trim().replace(/"/g, '');
    senderEmail = match[2].trim();
  } else {
    senderEmail = from.trim();
    senderName = senderEmail; // si no hay nombre, usamos el email
  }
  
  // Creamos un nuevo objeto con los datos limpios
  newItems.push({
    json: {
      subject: emailData.subject || '(sin asunto)',
      senderName: senderName,
      senderEmail: senderEmail,
      date: emailData.date || new Date().toISOString(),
      snippet: emailData.snippet || '',
      messageId: emailData.id || ''
    }
  });
}

return newItems;
```

**Explicación**:  
- `from` viene con formato `"Nombre <email>"`; la expresión regular lo separa.  
- Si no hay nombre, se usa el email como nombre.  
- Guardamos `subject`, `senderName`, `senderEmail`, `date` y opcionalmente `snippet` (resumen del cuerpo) y `messageId`.

#### 3. Nodo Notion

- **Tipo**: `Notion` → operación **Create Page**.
- **Credencial**: Conéctalo con tu integración de Notion (necesitas un token de integración y haber compartido la base de datos con esa integración).
- **Database ID**: Pega el ID de la base de datos donde quieres guardar los datos (puedes obtenerlo desde la URL de Notion).
- **Properties**: Mapea los campos de la base de datos con los datos del paso anterior. Por ejemplo:
  - **Title** (o propiedad de tipo título) → `{{ $json.subject }}`
  - **Sender Name** (propiedad de texto) → `{{ $json.senderName }}`
  - **Sender Email** (propiedad de email o texto) → `{{ $json.senderEmail }}`
  - **Date** (propiedad de fecha) → `{{ $json.date }}`
  - **Snippet** (propiedad de texto, opcional) → `{{ $json.snippet }}`

Asegúrate de que las propiedades en Notion ya existan con esos nombres o ajústalas.

#### 4. Nodo Slack

- **Tipo**: `Slack` → operación **Send Message**.
- **Credencial**: Conéctalo con tu workspace de Slack (Bot token o User token con permisos de escritura).
- **Channel**: El canal donde quieres recibir la notificación (ej. `#propuestas` o `@tuusuario`).
- **Text**: Mensaje que se enviará. Puedes usar expresiones para incluir datos:
  ```
  📩 Nuevo correo relevante recibido:
  *Asunto:* {{ $json.subject }}
  *Remitente:* {{ $json.senderName }} ({{ $json.senderEmail }})
  *Fecha:* {{ $json.date }}
  ```

---

### Orden de conexión

```
Gmail Trigger → Function → Notion (Create Page)
                     ↘
                       Slack (Send Message)
```

Puedes conectar el nodo Function tanto a Notion como a Slack (ambos reciben la misma salida del Function). En N8N, arrastra dos conexiones desde el Function o coloca los nodos en serie (Notion primero y Slack después). Si conectas en serie, Slack recibirá la salida de Notion, no la del Function, así que es mejor conectarlos en paralelo: el Function alimenta a ambos.

**Para conectarlos en paralelo**: haz clic en el punto de salida del Function y arrastra dos cables, uno a Notion y otro a Slack. O coloca Notion y Slack uno después del otro pero usando la salida del Function (puedes usar un nodo “Split In Batches” o simplemente mantener el flujo: Function → Notion, y luego Function → Slack como rama separada). En N8N es más fácil arrastrar dos conexiones desde el mismo nodo.

---

### Notas adicionales

- **Gmail Trigger**: Si usas “On new email” (webhook), necesitas configurar una URL de webhook y reenviar los correos desde Gmail con filtros. La opción “Polling” es más sencilla para pruebas.
- **Formato de fecha**: Notion espera formato ISO 8601. El campo `date` del correo ya viene en ese formato, pero puedes ajustarlo con `new Date(emailData.date).toISOString()`.
- **Manejo de errores**: Si algún nodo falla, puedes agregar un nodo “Error Trigger” para recibir alertas, pero no es obligatorio.

---

¿Quieres que profundice en la configuración de alguna credencial (Notion, Slack) o en el nodo Gmail Trigger? Estoy aquí para ayudarte.