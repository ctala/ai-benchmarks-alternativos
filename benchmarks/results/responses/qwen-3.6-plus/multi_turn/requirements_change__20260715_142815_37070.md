# Qwen 3.6 Plus — multi_turn/requirements_change

- model_id: `qwen/qwen3.6-plus`
- success: True  | final: 4.44 | quality: 4.0
- latency_total: 58.13s | tokens_per_second: 53.6
- input_tokens: 233 | output_tokens: 3114
- judge_score: 3.2 | justificación: 

## Respuesta completa

Excelente actualización. Este flujo es muy útil para automatizar leads o documentos importantes sin llenar hojas de cálculo. Aquí tienes la arquitectura exacta y la configuración nodo por nodo:

### 🔄 Estructura del Workflow
`Gmail Trigger` → `IF (Filtro)` → `Set (Parseo de datos)` → `Notion (Crear página/fila)` → `Slack (Notificación)`

---

### ⚙️ Configuración Paso a Paso

#### 1. **Gmail Trigger**
- **Evento:** `Message Received`
- **Credentials:** OAuth2 de Google (asegúrate de que la app tenga scope `https://www.googleapis.com/auth/gmail.readonly`)
- **Opciones clave:** 
  - ✅ `Fetch All Fields` (para tener acceso a `from`, `subject`, `date`, `headers`, etc.)
  - 📥 Limita si quieres: `Label`, `Search` (opcional)

#### 2. **IF Node (Filtro por asunto)**
- **Condición:** `Expression`
- **Expresión exacta:**
  ```javascript
  {{ ($json["subject"] || "").toLowerCase().includes("propuesta") || ($json["subject"] || "").toLowerCase().includes("cotizacion") }}
  ```
- **Salida:** Solo la rama `true` se conecta al siguiente nodo. La rama `false` puedes dejarla vacía o conectarla a `No Op` si prefieres loggear.

#### 3. **Set Node (Limpieza y parseo del remitente)**
El campo `from` de Gmail suele venir como `"Nombre <correo@dominio.com>"`. Este nodo lo divide limpiamente:
- **Fields to Set:**
  - `senderEmail`: `{{ ($json["from"] || "").match(/<([^>]+)>/)?.[1] || $json["from"] }}`
  - `senderName`: `{{ ($json["from"] || "").match(/^([^<]+)/)?.[1].trim() || "Desconocido" }}`
  - `subject`: `{{ $json["subject"] }}`
  - `receivedDate`: `{{ $json["date"] }}` (o `{{ $json["internalDate"] }}` si prefieres timestamp)
- **💡 Tip:** Usa `Keep Only Set` activado para evitar que campos basura de Gmail pasen al resto del flujo.

#### 4. **Notion Node**
- **Operation:** `Create a Page` o `Add Database Item`
- **Credentials:** Notion Integration Token + `database_id` (lo obtienes en la URL de tu base de datos)
- **Mapeo de propiedades** (ajusta según los nombres exactos de tu DB):
  - `Remitente` (Title/Text) → `{{ $json["senderName"] }}`
  - `Email` (Email) → `{{ $json["senderEmail"] }}`
  - `Asunto` (Text) → `{{ $json["subject"] }}`
  - `Fecha` (Date) → `{{ $json["receivedDate"] }}`
- **⚠️ Importante:** En Notion, las propiedades son `case-sensitive` y deben existir en la base de datos. Si usas `Date`, N8N acepta formato ISO (`YYYY-MM-DDTHH:mm:ssZ`).

#### 5. **Slack Node**
- **Operation:** `Send a Message`
- **Channel:** `#canal-lead` o `@usuario`
- **Text:**
  ```
  📨 *Nueva propuesta/cotización recibida*
  👤 De: {{ $json["senderName"] }} ({{ $json["senderEmail"] }})
  📝 Asunto: {{ $json["subject"] }}
  📅 Fecha: {{ $json["receivedDate"] }}
  🔗 Revisa en Notion: {{ $json["notionUrl"] }} (si configuras Notion para devolver URL)
  ```
- **Credentials:** Slack Bot Token (`xoxb-...`) o Legacy Token. Asegúrate de que el bot esté invitado al canal destino.

---

### 🛠️ Requisitos Previos
1. **Google Cloud Project:** OAuth 2.0 configurado y verificado (modo "Testing" basta para uso interno).
2. **Notion Integration:** Creada en `notion.so/my-integrations`, con acceso concedido a la base de datos (`Share → Invite integration`).
3. **Slack App:** Bot con scopes `chat:write` y `channels:read` (o `im:write` si es DM).

---

### 💡 Tips de Producción
- ✅ **Manejo de errores:** Añade un `Error Trigger` al workflow o usa `Continue On Fail` en Notion/Slack para que un fallo no detenga el flujo.
- 🔁 **Idempotencia:** Si un email se repite, Notion creará filas duplicadas. Puedes añadir un `Filter` o `Code` node que consulte Notion por `senderEmail + subject` antes de crear.
- 📦 **JSON Export:** Si quieres, te genero el archivo `.json` listo para importar en N8N (`Ctrl/Cmd + I` → Import Workflow). Solo dime la versión de N8N que usas.

¿Quieres que te ajuste algo (ej. extraer también attachments, validar dominios corporativos, o añadir un paso de aprobación en Slack)?