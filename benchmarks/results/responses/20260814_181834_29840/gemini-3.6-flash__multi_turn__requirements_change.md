# Gemini 3.6 Flash — multi_turn/requirements_change

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 4.54 | quality: 4.0
- latency_total: 8.991s | tokens_per_second: 178.3
- input_tokens: 202 | output_tokens: 1603

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

¡Excelente cambio! Guardar prospectos en Notion y notificar en Slack es una combinación muy potente para no perder ningún cliente potencial.

Aquí tienes la arquitectura del workflow optimizado y paso a paso cómo configurarlo en n8N.

---

### 🔄 Flujo del Workflow
1. **Gmail Trigger** (Lee correos recibidos)
2. **Filter / IF Node** (Filtra por palabras clave en el asunto)
3. **Notion Node** (Crea una nueva página/registro en tu base de datos)
4. **Slack Node** (Envía un mensaje al canal que elijas)

---

### ⚙️ Configuración Paso a Paso

#### 1. Gmail Trigger (Disparador)
* **Event:** `Message Received`
* **Consejo de optimización:** Puedes filtrar desde la misma API de Gmail para no gastar ejecuciones en n8n.
  * En el campo **Poll Times / Filters -> Search**: pon `subject:(propuesta OR cotización OR cotizacion)`

#### 2. Filter Node (Asegurar el filtro)
Por seguridad, agregamos un nodo **Filter** para evaluar el asunto (*Subject*):
* **Condition 1:** `{{ $json.subject.toLowerCase() }}` -> **Contains** -> `propuesta`
* **Combinador:** `OR` (O)
* **Condition 2:** `{{ $json.subject.toLowerCase() }}` -> **Contains** -> `cotizacion` (o `cotización`)

#### 3. Notion Node (Crear registro)
* **Resource:** `Database Page`
* **Operation:** `Create`
* **Database ID:** Selecciona tu base de datos de Notion (debe incluir propiedades como: Nombre, Email, Asunto, Fecha).
* **Mapeo de campos (Properties):**
  * **Nombre / Asunto (Title):** `{{ $json.subject }}`
  * **Email (Email):** `{{ $json.from.value[0].address }}`
  * **Remitente (Text):** `{{ $json.from.value[0].name }}`
  * **Fecha (Date):** `{{ $json.date }}`

*(Nota: Recuerda dar permisos a la integración de n8n dentro de la página de Notion).*

#### 4. Slack Node (Notificación)
* **Resource:** `Message`
* **Operation:** `Post`
* **Channel:** Selecciona tu canal (ej. `#ventas` o `#prospectos`)
* **Text:** Puedes formatearlo con MarkDown:
  ```text
  🚨 *¡Nueva solicitud recibida!* 🚨
  
  👤 *De:* {{ $json.from.value[0].name }} (<mailto:{{ $json.from.value[0].address }}|{{ $json.from.value[0].address }}>)
  📌 *Asunto:* {{ $json.subject }}
  📅 *Fecha:* {{ $json.date }}
  
  ✅ *Guardado automáticamente en Notion.*
  ```

---

### 💡 Requisitos previos que necesitas listos:
1. **Notion:** Tener creada la base de datos con las columnas (`Asunto`, `Email`, `Nombre`, `Fecha`).
2. **Slack:** Tener el Bot de n8n instalado en tu workspace de Slack y añadido al canal donde enviará los mensajes.

¿Quieres que te pase el **JSON del workflow** para que solo tengas que copiarlo y pegarlo en tu lienzo de n8n?