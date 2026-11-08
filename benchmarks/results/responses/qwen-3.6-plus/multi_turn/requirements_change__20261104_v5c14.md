# Qwen 3.6 Plus — multi_turn/requirements_change

- model_id: `qwen/qwen3.6-plus`
- success: True  | final: 4.34 | quality: 4.0
- latency_total: 49.666s | tokens_per_second: 57.7
- input_tokens: 233 | output_tokens: 2868

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

Perfecto. Aquí tienes la arquitectura y configuración paso a paso para tu workflow en n8n. Es un flujo muy común y robusto si se configuran bien los mapeos y el filtrado.

### 🧩 Estructura del Workflow
```
Gmail Trigger → IF (Filtro de asunto) → [TRUE] → Set/Code (Formateo) → Notion (Crear página) → Slack (Notificación)
                                          → [FALSE] → (Fin del flujo)
```

---

### ⚙️ Configuración Nodo por Nodo

#### 1. **Gmail Trigger**
- **Operation:** `Trigger` (recomendado para ejecución en tiempo real vía webhooks de Google)
- **Authentication:** OAuth2 de Google (con scopes `gmail.readonly`)
- **Filters:** Déjalos vacíos. Es mejor filtrar en n8n para mayor control.
- **Nota:** Este nodo devuelve un array de emails. Cada item contiene campos como `subject`, `from`, `date`, `snippet`, `headers`, etc.

#### 2. **IF Node** (Filtro por asunto)
Configura dos condiciones en **modo OR**:
- **Condition 1:** 
  - `Value 1:` `{{ $json.subject.toLowerCase() }}`
  - `Operation:` `Contains`
  - `Value 2:` `propuesta`
- **Condition 2:** 
  - `Value 1:` `{{ $json.subject.toLowerCase() }}`
  - `Operation:` `Contains`
  - `Value 2:` `cotizacion`
- **Output:** `true` → sigue al siguiente nodo. `false` → se descarta.

#### 3. **Set Node** (Extracción y limpieza de datos)
Añade estos campos manualmente para mapear fácilmente a Notion y Slack:
| Field Name | Value |
|------------|-------|
| `remitente_nombre` | `{{ $json.from.match(/^"?(.*?)\s*<?/)?.[1] || $json.from }}` |
| `remitente_email` | `{{ $json.from.match(/<?([^>]+)>?$/)?.[1] || $json.from }}` |
| `asunto` | `{{ $json.subject }}` |
| `fecha` | `{{ $json.date }}` |
| `snippet` | `{{ $json.snippet || '' }}` |

> 💡 *Si tu versión de n8n usa el nuevo `Code` node, puedes usar este JS para extraer con más seguridad:*
> ```js
> const from = $json.from || "";
> const nameMatch = from.match(/^"?(.*?)\s*<?/);
> const emailMatch = from.match(/<?([^>]+)>?$/);
> return {
>   json: {
>     remitente_nombre: nameMatch ? nameMatch[1].trim() : from,
>     remitente_email: emailMatch ? emailMatch[1].trim() : "",
>     asunto: $json.subject,
>     fecha: $json.date,
>     snippet: $json.snippet || ""
>   }
> };
> ```

#### 4. **Notion Node**
- **Operation:** `Create a Page` (o `Add Database Item` si usas una base de datos)
- **Authentication:** Internal Integration Token (con permisos `Content` y `Database`)
- **Database ID:** Pégalo aquí (ej: `a1b2c3d4e5f6...`)
- **Properties Mapping:**
  - `Remitente` (Title) → `{{ $json.remitente_nombre }}`
  - `Email` (Email) → `{{ $json.remitente_email }}`
  - `Asunto` (Text) → `{{ $json.asunto }}`
  - `Fecha` (Date) → `{{ $json.fecha }}`
  - `Snippet` (Text) → `{{ $json.snippet }}`

> ⚠️ **Importante:** La base de datos en Notion debe existir previamente con esas propiedades creadas. Notion es estricto con los tipos de dato.

#### 5. **Slack Node**
- **Operation:** `Send Message` (o `Post Message`)
- **Authentication:** OAuth2 o Incoming Webhook
- **Channel:** `#ventas` / `#leads` / `@tuusuario`
- **Message:**
  ```
  📩 *Nueva propuesta/cotización recibida*
  👤 *De:* {{ $json.remitente_nombre }} ({{ $json.remitente_email }})
  📝 *Asunto:* {{ $json.asunto }}
  📅 *Fecha:* {{ $json.fecha }}
  🔗 [Ver en Notion](https://www.notion.so/{{ $json.id }})
  ```
  *(El `id` lo devuelve automáticamente el nodo de Notion si lo conectas correctamente)*

---

### ✅ Requisitos Previos
1. **Gmail:** Habilitar API de Gmail en Google Cloud Console y crear credenciales OAuth2.
2. **Notion:** Crear una integración interna, compartir la base de datos con ella y copiar el `Database ID`.
3. **Slack:** Crear una app con permisos `chat:write` o usar un Incoming Webhook.
4. **n8n:** Tener credenciales guardadas para cada servicio.

---

### 🛡️ Recomendaciones de Producción
- **Manejo de duplicados:** Añade un campo `Message-ID` en Notion y usa un `Filter` + `Notion Search` para evitar guardar el mismo email dos veces.
- **Rate Limits:** Notion permite ~3 req/seg. Si esperas picos, añade un `Wait` node o usa `Batch` en el trigger.
- **Errores:** Conecta un `Error Trigger` para que te avise si falla la conexión a Notion/Slack.
- **Testing:** Usa el botón `Execute Workflow` con un email de prueba o activa `Manual Trigger` para validar mapeos antes de activar el trigger real.

---

¿Quieres que te genere el **JSON exportable** de este workflow para que lo importes directamente en tu n8n? Solo dime qué versión de n8n usas (self-hosted o cloud) y te lo ajusto.