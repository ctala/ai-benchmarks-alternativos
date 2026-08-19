# Gemini 3.6 Flash — multi_turn/requirements_change

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 4.56 | quality: 4.0
- latency_total: 8.301s | tokens_per_second: 182.3
- input_tokens: 202 | output_tokens: 1513

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

¡Excelente cambio! Conectar Gmail con Notion y Slack es un clásico de la automatización para gestionar leads o clientes potenciales. Además, filtrar desde el inicio te ahorrará ejecuciones en N8N.

Aquí tienes la arquitectura del workflow y cómo configurar cada nodo:

---

### 🗺️ Estructura del Workflow

```text
[Gmail Trigger] ➔ [Filter (Opcional)] ➔ [Notion Node] ➔ [Slack Node]
```

---

### 🛠️ Configuración Paso a Paso

#### 1. Nodo: `Gmail Trigger`
> **Tip Pro:** Puedes filtrar directamente en la consulta de Gmail para que N8N **solo se ejecute** cuando lleguen los correos que te interesan. Así optimizas las ejecuciones de tu plan de N8N.

* **Event:** `Message Received`
* **Filters / Search Query:** 
  ```text
  subject:(propuesta OR cotizacion)
  ```
  *(Esto ya hace el filtro duro desde Gmail).*

---

#### 2. Nodo: `Filter` (Opcional, para doble validación)
Si prefieres no usar la búsqueda nativa de Gmail o quieres asegurar la condición dentro de N8N:
* **Mode:** `Keep items matching ALL/ANY conditions`
* **Condition:** 
  * **Value 1:** `{{ $json.subject.toLowerCase() }}`
  * **Operation:** `Contains`
  * **Value 2:** `propuesta`
* **Agregar condición (OR):**
  * **Value 1:** `{{ $json.subject.toLowerCase() }}`
  * **Operation:** `Contains`
  * **Value 2:** `cotizacion`

---

#### 3. Nodo: `Notion`
Este nodo creará un elemento en tu Base de Datos de Notion.

* **Resource:** `Database Page`
* **Operation:** `Create`
* **Database ID:** *(Selecciona tu base de datos de Notion)*
* **Properties (Mapeo de campos):**
  * **Nombre / Título (Title):** `{{ $json.subject }}`
  * **Email (Email):** `{{ $json.from.text }}` (o usa expresiones para extraer solo el correo).
  * **Fecha (Date):** `{{ $json.date }}`
  * **Detalle / Texto (Rich Text):** `{{ $json.snippet }}` *(resumen del correo)*.

---

#### 4. Nodo: `Slack`
Envía la alerta al equipo cuando entra un correo válido.

* **Resource:** `Message`
* **Operation:** `Post`
* **Channel:** `#tu-canal-de-notificaciones` (ej. `#ventas` o `#leads`)
* **Text:**
  ```text
  📩 *¡Nueva oportunidad recibida!*

  • *De:* {{ $json.from.text }}
  • *Asunto:* {{ $json.subject }}
  • *Fecha:* {{ $json.date }}

  _Revisa la base de datos de Notion para ver más detalles._
  ```

---

### 💡 Requisitos previos que necesitarás:
1. **Credenciales en N8N:**
   * OAuth2 para **Gmail**.
   * Integración API/OAuth2 para **Notion** (asegúrate de dar permisos a la integración en tu base de datos de Notion).
   * Bot Token / OAuth2 para **Slack**.
2. **Notion:** Tener creada la base de datos con al menos las columnas: *Nombre (Title)*, *Email*, *Fecha*.

¿Quieres que te pase el **código JSON** para importar este workflow directamente en tu instancia de N8N, o prefieres ir armándolo nodo por nodo?