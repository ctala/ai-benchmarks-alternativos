# GPT-5.6 Terra — multi_turn/requirements_change

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 4.7 | quality: 4.72
- latency_total: 11.612s | tokens_per_second: 137.4
- input_tokens: 226 | output_tokens: 1595
- judge_score: 2.0 | justificación: La respuesta no cumple con los requisitos originales de leer emails de Gmail, extraer datos del remitente y guardarlos en un Google Sheet, en su lugar, propone un workflow que utiliza Notion y Slack, lo que no es relevante para la tarea especificada.

## Respuesta completa

Puedes montar el workflow así:

```text
Gmail Trigger
   ↓
IF (filtrar asunto)
   ├─ false → termina
   └─ true
        ↓
Edit Fields / Set (normalizar datos)
        ↓
Notion (crear página en base de datos)
        ↓
Slack (enviar notificación)
```

## 1. Gmail Trigger

Añade un nodo **Gmail Trigger**.

Configuración recomendada:

- **Event**: `Message Received`
- **Credentials**: conecta tu cuenta de Gmail con OAuth2.
- Opcionalmente, limita la carpeta/label a `INBOX`.

> Si el nodo permite usar una consulta de Gmail, puedes añadir:
>
> ```text
> subject:(propuesta OR cotizacion OR cotización)
> ```
>
> Aun así, recomiendo mantener el nodo `IF` posterior, ya que asegura que el filtro se aplique correctamente.

---

## 2. Nodo IF: filtrar por asunto

Añade un nodo **IF** después del Gmail Trigger.

Configúralo con una condición de tipo **Boolean** o **Expression**.

### Opción recomendada: expresión

En el campo de condición, usa esta expresión:

```javascript
{{
  /propuesta|cotizaci[oó]n/i.test($json.subject || '')
}}
```

Esto detectará asuntos como:

- `Propuesta de colaboración`
- `PROPUESTA comercial`
- `Solicitud de cotización`
- `Solicitud de cotizacion`

Conecta únicamente la salida **true** al resto del workflow.

---

## 3. Nodo Edit Fields (o Set): preparar los datos

Añade un nodo **Edit Fields** después de la salida `true` del IF.

Activa **Keep Only Set Fields** para guardar solo los datos útiles.

Crea estos campos:

| Campo | Valor / Expresión |
|---|---|
| `remitente_nombre` | `{{$json.from?.value?.[0]?.name || ''}}` |
| `remitente_email` | `{{$json.from?.value?.[0]?.address || $json.from?.email || ''}}` |
| `asunto` | `{{$json.subject || ''}}` |
| `fecha_email` | `{{$json.date || $now.toISO()}}` |
| `contenido` | `{{$json.text || $json.textPlain || $json.snippet || ''}}` |
| `message_id` | `{{$json.id || $json.messageId || ''}}` |

> Según la versión del nodo Gmail y el formato de salida, los nombres exactos pueden variar. Ejecuta una prueba con un email real y revisa el panel **Output** del nodo Gmail para confirmar las rutas.

---

## 4. Preparar la base de datos de Notion

En Notion, crea una base de datos, por ejemplo: **Propuestas recibidas**.

Añade estas propiedades:

| Propiedad en Notion | Tipo |
|---|---|
| `Asunto` | Title |
| `Nombre remitente` | Text |
| `Email remitente` | Email |
| `Fecha email` | Date |
| `Contenido` | Text |
| `ID Gmail` | Text |
| `Estado` | Select, opcional |
| `URL Gmail` | URL, opcional |

Después, crea una integración de Notion:

1. Ve a [Notion Integrations](https://www.notion.so/my-integrations).
2. Crea una integración interna.
3. Copia el token y conéctalo en las credenciales de n8n.
4. Comparte la base de datos de Notion con esa integración mediante el botón `...` → `Connections`.

---

## 5. Nodo Notion: crear una página

Añade el nodo **Notion** después del nodo Edit Fields.

Configuración:

- **Resource**: `Database Page`
- **Operation**: `Create`
- **Database**: selecciona la base de datos `Propuestas recibidas`.

Mapea las propiedades:

| Propiedad de Notion | Valor en n8n |
|---|---|
| `Asunto` | `{{$json.asunto}}` |
| `Nombre remitente` | `{{$json.remitente_nombre}}` |
| `Email remitente` | `{{$json.remitente_email}}` |
| `Fecha email` | `{{$json.fecha_email}}` |
| `Contenido` | `{{$json.contenido}}` |
| `ID Gmail` | `{{$json.message_id}}` |
| `Estado` | `Nuevo` |

Si quieres guardar el cuerpo completo del email como contenido de la página de Notion, en vez de solo como propiedad, puedes añadir después otro nodo Notion para crear bloques de texto dentro de la página creada.

---

## 6. Nodo Slack: notificación

Añade un nodo **Slack** después del nodo Notion.

Configuración:

- **Resource**: `Message`
- **Operation**: `Send`
- **Channel**: por ejemplo, `#propuestas` o `#ventas`.

Mensaje sugerido:

```text
📩 Nueva propuesta/cotización recibida

*Asunto:* {{$node["Edit Fields"].json["asunto"]}}
*Remitente:* {{$node["Edit Fields"].json["remitente_nombre"]}} <{{$node["Edit Fields"].json["remitente_email"]}}>
*Fecha:* {{$node["Edit Fields"].json["fecha_email"]}}

Se ha guardado automáticamente en Notion.
```

Si Notion devuelve la URL de la página creada, puedes añadir un enlace:

```text
🔗 Notion: {{$json.url}}
```

En ese caso, como el nodo Slack recibe la salida del nodo Notion, los datos originales del email se referencian mediante:

```javascript
{{$node["Edit Fields"].json["asunto"]}}
```

y la URL de Notion mediante:

```javascript
{{$json.url}}
```

---

## Recomendación importante: evitar duplicados

Gmail Trigger puede procesar un correo más de una vez en algunos escenarios, por ejemplo, si reinicias el workflow o cambian etiquetas.

Para evitar páginas duplicadas en Notion:

1. Guarda el `message_id` de Gmail en Notion.
2. Antes de crear la página, añade un nodo **Notion → Database Page → Get Many**.
3. Filtra por la propiedad `ID Gmail`.
4. Añade un nodo IF:
   - Si ya existe: no crear nada.
   - Si no existe: crear la página y notificar por Slack.

La versión básica quedaría:

```text
Gmail Trigger
  ↓
IF: asunto contiene propuesta o cotización
  ↓ true
Edit Fields
  ↓
Notion: Create Database Page
  ↓
Slack: Send Message
```

Y la versión robusta, con prevención de duplicados:

```text
Gmail Trigger
  ↓
IF: asunto contiene propuesta o cotización
  ↓ true
Edit Fields
  ↓
Notion: buscar por ID Gmail
  ↓
IF: ¿ya existe?
  ├─ true → terminar
  └─ false
       ↓
     Notion: crear página
       ↓
     Slack: enviar notificación
```