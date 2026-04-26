# Qwen 3-Next 80B Instruct (NIM) — multi_turn/requirements_change

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 6.24 | quality: 6.4
- latency_total: 23.828s | tokens_per_second: 66.8
- input_tokens: 247 | output_tokens: 1592
- judge_score: 3.2 | justificación: 

## Respuesta completa

¡Perfecto! Cambio muy lógico: **Notion** es más potente para gestión de propuestas, y agregar **Slack notifications** es clave para no perder nada. Aquí tienes el workflow completo en N8N, optimizado para tu caso de uso:

---

### ✅ **Workflow: Gmail → Notion + Slack (Filtrado por “propuesta” o “cotización”)**

#### 🔗 **Nodos requeridos** (en orden):
1. **Gmail Trigger** (Nuevo email)
2. **Function** (Filtrar y extraer datos)
3. **If** (Filtro de palabras clave en asunto)
4. **Notion** (Crear página en base de datos)
5. **Slack** (Notificación)

---

### 🛠️ **Configuración detallada de cada nodo**

---

### 1. **Gmail Trigger**  
*(Inicia el flujo cuando llega un nuevo email)*

- **Action**: `Watch Emails`  
- **Folder**: `INBOX`  
- **Only unread**: ✅ *Sí* (para evitar duplicados)  
- **Include attachments**: ❌ No (a menos que las necesites)  
- **Email query**: `is:unread` *(opcional, pero recomendado)*

> 💡 *Este nodo emite el objeto completo del email (remitente, asunto, cuerpo, etc.)*

---

### 2. **Function**  
*(Extrae y normaliza los datos que necesitas)*

```javascript
// Extrae datos del email y los prepara para Notion y Slack
const email = $input.item().json;

return [
  {
    json: {
      fromName: email.from?.name || "Desconocido",
      fromEmail: email.from?.email || "desconocido@ejemplo.com",
      subject: email.subject || "",
      date: email.date || new Date().toISOString(),
      snippet: email.snippet || "",
    },
    binary: {},
  },
];
```

> ✅ Esto crea un objeto limpio con: `fromName`, `fromEmail`, `subject`, `date`, `snippet`

---

### 3. **If**  
*(Filtra solo emails con "propuesta" o "cotización" en el asunto — sin importar mayúsculas/minúsculas)*

- **Condition**: `Expression`
- **Expression**:
  ```js
  {{ $json.subject.toLowerCase().includes('propuesta') || $json.subject.toLowerCase().includes('cotizacion') || $json.subject.toLowerCase().includes('cotización') }}
  ```
> 🔍 Incluye ambas variantes: “cotizacion” (sin tilde) y “cotización” (con tilde), por si vienen de distintos remitentes.

- ✅ **If true**: Continúa al nodo Notion  
- ❌ **If false**: Detiene el flujo (no hace nada)

---

### 4. **Notion**  
*(Crea una nueva página en tu base de datos de Notion)*

- **Authentication**: Usa tu **Notion API Key** (debe tener acceso a la base de datos)
- **Database ID**: 📌 *Pega aquí el ID de tu base de datos de Notion*  
  (Puedes obtenerlo copiando la URL de la base de datos en Notion — lo que viene después de `/` en `https://www.notion.so/.../...`)

- **Action**: `Create Page`

- **Properties** (configura según tu base de datos en Notion):

| Propiedad en Notion | Valor en N8N (Expression) |
|---------------------|----------------------------|
| `Nombre` (Title)    | `{{ $json.fromName }}` |
| `Email` (Email)     | `{{ $json.fromEmail }}` |
| `Asunto` (Title)    | `{{ $json.subject }}` |
| `Fecha` (Date)      | `{{ $json.date }}` |
| `Resumen` (Text)    | `{{ $json.snippet }}` |

> ✅ Asegúrate de que los nombres de las propiedades en Notion **coincidan exactamente** con los que usas aquí (incluyendo espacios y mayúsculas).

---

### 5. **Slack**  
*(Envía notificación cuando llega una propuesta/cotización)*

- **Authentication**: Usa tu **Slack App Token** (con permisos `chat:write`)
- **Channel**: `#propuestas` o tu canal deseado
- **Text**:
  ```text
  📩 Nueva propuesta/cotización recibida!

  👤 *Remitente*: {{ $json.fromName }}
  ✉️ *Email*: {{ $json.fromEmail }}
  📌 *Asunto*: {{ $json.subject }}
  📅 *Fecha*: {{ $json.date }}

  🔗 Ver en Notion: [Abrir en Notion](https://www.notion.so/...[tu-database-id]...)
  ```

> 💡 Puedes generar un enlace directo a la página de Notion si usas la API para devolver el `url` de la página creada (lo explico abajo).

---

### ✅ **Bonus: Enlace directo a la página en Notion (opcional pero útil)**

Si quieres que el mensaje de Slack tenga un enlace directo a la página creada en Notion, **añade un nodo `Function` después del nodo Notion**:

```javascript
// Extrae el URL de la página creada en Notion
const notionResponse = $input.item().json;
const pageUrl = notionResponse.url;

return [
  {
    json: {
      slackMessage: `📩 Nueva propuesta/cotización recibida!\n\n👤 *Remitente*: ${$json.fromName}\n✉️ *Email*: ${$json.fromEmail}\n📌 *Asunto*: ${$json.subject}\n📅 *Fecha*: ${$json.date}\n\n🔗 [Abrir en Notion](${pageUrl})`,
    },
  },
];
```

Luego, en el nodo **Slack**, en el campo **Text**, pon:
```text
{{ $json.slackMessage }}
```

---

### 📌 **Requisitos previos**

| Herramienta | Qué necesitas |
|-------------|----------------|
| **Gmail** | Acceso con OAuth (N8N te guía al conectar) |
| **Notion** | API Key + ID de base de datos (crea una base de datos con propiedades: Nombre, Email, Asunto, Fecha, Resumen) |
| **Slack** | App con token `bot:token` y permiso `chat:write` |
| **N8N** | Conectado a las 3 APIs |

---

### ✅ Resultado final:
Cuando llega un email con “propuesta” o “cotización” en el asunto:
- ✅ Se guarda en Notion como una nueva entrada
- ✅ Se envía una notificación bonita a Slack
- ❌ Los demás emails se ignoran (no saturan tu canal)

---

¿Quieres que te genere el **JSON exportable del workflow** para importarlo directamente en N8N? Solo dime y te lo paso listo para copiar-pegar.