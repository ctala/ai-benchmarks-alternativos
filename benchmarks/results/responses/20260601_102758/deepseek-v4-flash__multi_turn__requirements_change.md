# DeepSeek V4 Flash (OpenRouter) — multi_turn/requirements_change

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 7.4 | quality: 7.24
- latency_total: 13.013s | tokens_per_second: 110.8
- input_tokens: 244 | output_tokens: 1442
- judge_score: 3.8 | justificación: 

## Respuesta completa

Perfecto, ajusto el workflow a tus nuevos requerimientos. Aquí tienes la estructura paso a paso.

## Workflow en N8N: Gmail → Filtro → Notion + Slack

### Nodos necesarios:
1. **Gmail Trigger** (polling cada X minutos)
2. **IF** (filtro por asunto)
3. **Function** (extraer datos estructurados)
4. **Notion** (crear página en base de datos)
5. **Slack** (enviar notificación)

---

### 1. Gmail Trigger
- **Operation:** `watch` (o `poll` si prefieres polling)
- **Authentication:** OAuth2 (cuenta de Gmail)
- **Filters:**
  - `Unread only`: `true` (para solo emails nuevos)
  - `Format`: `full` (para tener cuerpo y cabeceras)
- **Polling time:** cada 5–10 minutos (ajusta según volumen)

---

### 2. Filtro con nodo IF
- **Conditions:**
  - En `Value 1`: `{{ $json.subject.toLowerCase() }}`
  - **Operation:** `Contains`
  - **Value 2:** `propuesta` (repite otra condición con OR)
  - Añade una segunda condición:
    - `{{ $json.subject.toLowerCase() }}`
    - **Contains** → `cotizacion`
  - **Combinación:** `OR` (si alguna se cumple, pasa)

---

### 3. Function Node (extraer datos)
Código para extraer remitente, asunto, fecha y enlace al email:

```javascript
// El objeto $json proviene del trigger de Gmail
const email = $json;

// Extraer nombre y email del remitente (From)
const fromHeader = email.from || email.headers?.From;
let senderName = '';
let senderEmail = '';

if (fromHeader) {
  // Formato típico: "Nombre <correo@dominio.com>"
  const match = fromHeader.match(/(.*?)<(.*?)>/);
  if (match) {
    senderName = match[1].trim();
    senderEmail = match[2].trim();
  } else {
    // Si solo es correo
    senderEmail = fromHeader.trim();
    senderName = senderEmail.split('@')[0];
  }
}

// Asunto
const subject = email.subject || email.headers?.Subject || 'Sin asunto';

// Fecha (timestamp)
const date = new Date(email.date || email.internalDate);
const formattedDate = date.toISOString().split('T')[0]; // YYYY-MM-DD

// Enlace al email en Gmail (opcional)
const messageId = email.id || email.messageId;
const gmailLink = `https://mail.google.com/mail/u/0/#inbox/${messageId}`;

// Devolver datos estructurados
return {
  senderName,
  senderEmail,
  subject,
  date: formattedDate,
  gmailLink,
  receivedAt: new Date().toISOString()
};
```

---

### 4. Notion Node (crear página)
- **Resource:** `Page`
- **Operation:** `Create`
- **Database ID:** (ID de tu base de datos en Notion)
- **Properties:** Mapea los campos:
  - **Title** → `{{ $json.subject }}`
  - **Select** → `{{ $json.senderName }}` (o un campo de texto)
  - **Email** → `{{ $json.senderEmail }}`
  - **Fecha** → `{{ $json.date }}` (tipo fecha)
  - **Enlace** → `{{ $json.gmailLink }}` (tipo URL)
- **Authentication:** Necesitarás un token de integración de Notion (crear una integración y compartir la base de datos con ella).

---

### 5. Slack Node (notificación)
- **Resource:** `Message`
- **Operation:** `Post`
- **Channel:** Elige el canal (p.ej. `#propuestas-recibidas`)
- **Text:** Un mensaje como:
  ```
  📩 Nueva propuesta/cotización recibida
  
  *Remitente:* {{ $json.senderName }} ({{ $json.senderEmail }})
  *Asunto:* {{ $json.subject }}
  *Fecha:* {{ $json.date }}
  *Ver en Gmail:* {{ $json.gmailLink }}
  ```
- **Authentication:** OAuth2 con Slack (scope `chat:write` y `channels:join`)

---

### Conexión de nodos:
```
[Gmail Trigger] → [IF] (true branch) → [Function] → [Notion] → [Slack]
                 (false branch → no hace nada, puedes poner un nodo Stop o dejarlo vacío)
```

### Consideraciones importantes:
- **Gmail trigger en modo watch** requiere que actives la API de Google Pub/Sub (un poco más complejo). Si eres principiante, usa **Poll** (ejecución cada 5 min) que es más sencillo.
- **Notion**: Asegúrate de que la base de datos tenga los campos correctos (title, texto, fecha, URL). La integración debe tener permisos de escritura.
- **Slack**: Necesitas crear una app en Slack y darle permisos para publicar en el canal.
- **Prueba**: Activa el workflow en modo "Activo" y envía un email de prueba con "propuesta" o "cotizacion" en el asunto.

¿Quieres que profundice en alguno de los pasos (autenticación, configuración de Notion, etc.)?