# Gemini 3.8 Flash — multi_turn/requirements_change

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 4.59 | quality: 4.0
- latency_total: 9.86s | tokens_per_second: 127.9
- input_tokens: 202 | output_tokens: 1261

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

¡Excelente cambio! Notion + Slack es una combinación mucho más potente para gestionar leads y oportunidades.

Aquí tienes la arquitectura optimizada del workflow en N8N:

---

### Estructura del Workflow

```
[Gmail Trigger] ➔ [Filter Node]* ➔ [Notion Node] ➔ [Slack Node]
```
*\*Nota de pro: Podemos filtrar directamente dentro del propio nodo de Gmail para ahorrar ejecuciones en tu plan de N8N.*

---

### Configuración Paso a Paso

#### 1. Gmail Trigger
* **Resource:** Message
* **Event:** Message Received
* **Poll Times:** Cada 1 o 5 minutos (según tu plan).
* **Filtro inteligente (Query):** En el campo `Query` (búsqueda de Gmail), pon esto:
  ```text
  subject:(propuesta OR cotización OR cotizacion)
  ```
  *(Al ponerlo aquí, N8N solo se activará cuando llegue un correo que cumpla la condición, ahorrándote ejecuciones innecesarias).*

---

#### 2. Notion Node (Crear entrada en tu base de datos)
*Asegúrate de tener una base de datos en Notion con columnas como: Nombre/Asunto (Title), Email (Email), Remitente (Text), Fecha (Date).*

* **Resource:** Database Page
* **Operation:** Create
* **Database:** Selecciona tu base de datos de "Propuestas / Leads".
* **Properties (Mapeo de campos):**
  * **Nombre/Asunto:** `{{ $json.subject }}`
  * **Remitente:** `{{ $json.from.value[0].name }}`
  * **Email:** `{{ $json.from.value[0].address }}`
  * **Fecha:** `{{ $json.date }}`
  * **Contenido/Notas (opcional):** `{{ $json.snippet }}` (un resumen del mensaje).

---

#### 3. Slack Node (Notificación)
* **Resource:** Message
* **Operation:** Post
* **Send As:** Bot
* **Channel:** Selecciona tu canal (ej: `#ventas` o `#leads`).
* **Text:** Puedes armar un mensaje dinámico con formato Markdown, por ejemplo:
  ```markdown
  🚨 *¡Nueva solicitud recibida!*
  *De:* {{ $('Gmail Trigger').item.json.from.value[0].name }} ({{ $('Gmail Trigger').item.json.from.value[0].address }})
  *Asunto:* {{ $('Gmail Trigger').item.json.subject }}
  *Resumen:* {{ $('Gmail Trigger').item.json.snippet }}

  👉 _Registrado automáticamente en Notion._
  ```

---

### Siguiente paso
¿Tienes ya conectadas las credenciales de Notion y Slack en tu instancia de N8N, o necesitas ayuda con la autenticación (OAuth2 / Tokens de integración)?