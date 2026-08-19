# Gemini 3.7 Flash — multi_turn/requirements_change

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 4.64 | quality: 4.0
- latency_total: 11.048s | tokens_per_second: 121.3
- input_tokens: 202 | output_tokens: 1340

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

¡Excelente cambio! Notion como base de datos y Slack para alertas en tiempo real es una combinación mucho más potente para gestionar leads y propuestas.

Aquí tienes la arquitectura del workflow y la configuración paso a paso:

---

### 🗺️ Arquitectura del Workflow

```
[Gmail Trigger] ➡️ [Filter Node]* ➡️ [Notion Node] ➡️ [Slack Node]
```
*\*Nota: Podemos filtrar directamente en el Gmail Trigger para ahorrar ejecuciones.*

---

### ⚙️ Configuración paso a paso

#### 1. Gmail Trigger (Disparador)
* **Resource**: `Message`
* **Event**: `Message Received` (o polling cada X minutos)
* **Filters / Query (Recomendado)**:
  Para ahorrar ejecuciones en N8N, puedes filtrar directamente desde Gmail usando la barra de búsqueda de la API:
  * **Search**: `subject:(propuesta OR cotizacion OR cotización)`

*(Si prefieres traer todos y filtrar dentro de N8N, usa un nodo **Filter** después del trigger).*

---

#### 2. Filter Node (Opcional, si no filtraste en el Trigger)
Si no usas la query de Gmail, agrega un nodo **Filter**:
* **Condition**:
  * `{{ $json.subject.toLowerCase() }}` -> **Contains** -> `propuesta`
  * **OR**
  * `{{ $json.subject.toLowerCase() }}` -> **Contains** -> `cotizac` *(así cubre cotizacion y cotización)*

---

#### 3. Notion Node (Crear registro)
*Crea previamente una base de datos en Notion con columnas como: Nombre, Email, Asunto, Fecha, Mensaje.*

* **Credential to connect with**: Tu conexión de Notion (Internal Integration Token)
* **Resource**: `Database Page`
* **Operation**: `Create`
* **Database ID**: Selecciona tu base de datos de Notion.
* **Mapeo de propiedades**:
  * **Nombre / Lead**: `{{ $json.from.name || $json.from.value[0].name }}`
  * **Email**: `{{ $json.from.value[0].address }}`
  * **Asunto**: `{{ $json.subject }}`
  * **Fecha**: `{{ $json.date }}`
  * **Extracto/Cuerpo**: `{{ $json.snippet }}` (o `$json.textAsHtml` si quieres el contenido)

---

#### 4. Slack Node (Notificación)
* **Resource**: `Message`
* **Operation**: `Post`
* **Channel**: Selecciona el canal (ej. `#ventas` o `#leads`)
* **Text / Message Block**: Puedes usar formato Markdown enriquecido:

```text
🚨 *¡Nueva Propuesta / Cotización Recibida!* 🚨

👤 *De:* {{ $('Gmail Trigger').item.json.from.text }}
📧 *Email:* {{ $('Gmail Trigger').item.json.from.value[0].address }}
📌 *Asunto:* {{ $('Gmail Trigger').item.json.subject }}
📅 *Fecha:* {{ $('Gmail Trigger').item.json.date }}

🔗 _Revisa los detalles guardados en Notion._
```

---

### 💡 Consejos técnicos:
1. **Permisos en Notion**: Recuerda invitar/compartir la integración de Notion con la base de datos específica (en los `...` de la página en Notion > *Connections* > Seleccionar tu bot).
2. **Campos del remitente en Gmail**: N8N suele devolver el remitente estructurado en `$json.from.value[0]`. Si viene como texto plano (`"Juan Pérez <juan@empresa.com>"`), puedes usar expresiones regulares simples si necesitas separar nombre y correo.

¿Quieres que te prepare el JSON del workflow listo para importar y pegar en tu N8N?