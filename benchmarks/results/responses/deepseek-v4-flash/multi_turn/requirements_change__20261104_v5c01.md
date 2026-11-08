# DeepSeek V4 Flash (OpenRouter) — multi_turn/requirements_change

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 6.22 | quality: 6.0
- latency_total: 25.125s | tokens_per_second: 44.4
- input_tokens: 244 | output_tokens: 1115

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

Perfecto, rediseñamos el workflow con Notion en lugar de Google Sheets, filtro por asunto y notificación a Slack. Aquí tienes la estructura completa:

## Workflow N8N: Gmail → Filtro → Notion + Slack

### Nodos y configuración

1. **Gmail Trigger** (nodo de disparo)
   - Evento: `message received`
   - Conexión: cuenta Gmail (OAuth2)
   - Opciones: `Include body` (para tener el asunto)
   - Frecuencia: cada 1 minuto (o la que prefieras)

2. **Set** (opcional pero recomendado para normalizar datos)
   - Asignar variables: `subject`, `from`, `date`, `body` (puedes usar `$json.subject` etc.)

3. **IF** (nodo de filtro)
   - Condición 1: `{{ $json.subject.toLowerCase().includes('propuesta') }}` → Output true
   - Condición 2: `{{ $json.subject.toLowerCase().includes('cotizacion') }}` → Output true
   - Combinar con OR: en *Mode* selecciona `Logical Operator` y pon `OR`
   - Si true → continuar, si false → detener (no conectar nada)

4. **Notion** (nodo de creación)
   - Operación: `Create a database item`
   - Conexión: API Key de Notion
   - Database ID: el ID de tu base de datos (se obtiene de la URL de la página)
   - Mapear campos (ejemplo):
     - `Remitente`: `{{ $json.from }}`
     - `Email`: `{{ $json.from }}` (si quieres extraer solo el email, usa una expresión)
     - `Asunto`: `{{ $json.subject }}`
     - `Fecha`: `{{ $json.date }}` (formatear si es necesario)
     - `Cuerpo` (opcional): `{{ $json.body }}`

5. **Slack** (nodo de notificación)
   - Operación: `Send a message to a channel`
   - Conexión: Slack App (OAuth2)
   - Channel: `#nombre-del-canal` (ej. `#propuestas`)
   - Text: 
     ```
     📩 *Nueva propuesta/cotización recibida*
     *Remitente:* {{ $json.from
     *Asunto:* {{ $json.subject
     *Fecha:* {{ $json.date
     ```
   - Opcional: añadir botón o enlace a la página de Notion (puedes usar `{{ $json.id }}` del nodo Notion si lo encadenas después)

### Flujo de conexión de nodos

```
Gmail Trigger → Set → IF (true) → Notion → Slack
```

### Expresiones adicionales útiles

- **Extraer solo email del remitente** (si `from` viene como "Nombre <correo@dominio.com>"):
  ```
  {{ $json.from.match(/<([^>]+)>/)?.[1] || $json.from }}
  ```
- **Formatear fecha** (si viene en ISO):
  ```
  {{ new Date($json.date).toLocaleString('es-ES') }}
  ```

### Configuración de credenciales

- **Gmail**: Usa OAuth2 con alcance `https://mail.google.com/`
- **Notion**: Crea una integración en Notion (Developers → My integrations) y comparte tu base de datos con esa integración
- **Slack**: Crea una app en Slack con permisos `chat:write` y `channels:join`

### Notas importantes

- El filtro por asunto es *case insensitive* gracias a `.toLowerCase()`
- Si quieres filtrar también el cuerpo del email, puedes agregar una tercera condición con `body.includes(...)`
- Para evitar duplicados, puedes agregar un nodo **Wait** (opcional) o usar el ID único del mensaje de Gmail como clave en Notion

¿Necesitas ayuda para configurar algún nodo en específico o con las expresiones?