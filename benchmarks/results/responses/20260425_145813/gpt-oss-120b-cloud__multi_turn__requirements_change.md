# GPT-OSS 120B (Ollama Cloud) — multi_turn/requirements_change

- model_id: `gpt-oss:120b-cloud`
- success: True  | final: 7.12 | quality: 6.76
- latency_total: 28.679s | tokens_per_second: 71.4
- input_tokens: 291 | output_tokens: 2048
- judge_score: 3.2 | justificación: 

## Respuesta completa

## 🛠️ Workflow completo en **n8n**  
Objetivo:  

1. **Escuchar** nuevos correos en Gmail.  
2. **Filtrar** solo los que tengan la palabra **“propuesta”** o **“cotizacion”** (sin importar mayúsculas/minúsculas) en el asunto.  
3. **Extraer** los datos del remitente (nombre y email), asunto y fecha.  
4. **Crear** una nueva fila en una base de datos de **Notion** con esos datos.  
5. **Enviar** una notificación a **Slack** con un resumen del email.

---

### 📋 Vista general del flujo

| Nodo | Tipo | Función |
|------|------|---------|
| **1. Gmail Trigger** | Trigger | Detecta cada nuevo correo entrante. |
| **2. IF (Filtro asunto)** | IF | Evalúa si el asunto contiene “propuesta” o “cotizacion”. |
| **3. Function (Parseo)** | Function | Normaliza los datos (nombre, email, asunto, fecha). |
| **4. Notion – Create Page** | Notion | Inserta una nueva página/registro en la base de datos de Notion. |
| **5. Slack – Send Message** | Slack | Notifica al canal elegido. |
| **6. No‑Match (opcional)** | No Output | (Opcional) Puedes registrar los correos descartados en un log o simplemente dejarlos sin acción. |

---

## 1️⃣ Nodo: **Gmail Trigger**

| Campo | Valor |
|-------|-------|
| **Resource** | `Message` |
| **Operation** | `Watch` (o `New Email` según la versión) |
| **Mailbox** | `INBOX` |
| **Label** | (puedes usar una etiqueta específica si lo prefieres) |
| **Include Attachments** | `No` (no necesario) |
| **Mark As Read** | `No` (opcional) |
| **Authentication** | Conecta tu cuenta de Gmail vía OAuth2 (n8n ya trae la credencial “Google OAuth2”). |

> **Resultado del nodo**: `{{ $json["payload"] }}` contendrá un array de mensajes. Usaremos el primer elemento (`{{$json["payload"][0]}}`) en los siguientes nodos.

---

## 2️⃣ Nodo: **IF (Filtro asunto)**  

1. **Add Condition** → **String → Contains**  
2. **Value 1** → `{{$json["payload"][0].subject}}`  
3. **Value 2** → `propuesta`  

   *Marca la casilla **“or”** y agrega una segunda condición:*

4. **Value 1** → `{{$json["payload"][0].subject}}`  
5. **Value 2** → `cotizacion`  

6. **Case Sensitive** → `No` (para que sea insensible a mayúsculas).  

- **Output “true”** → continuará con los nodos 3‑5.  
- **Output “false”** → (opcional) lo puedes conectar a un nodo “No‑Match” o simplemente dejar sin salida.

---

## 3️⃣ Nodo: **Function (Parseo y normalización)**  

```javascript
// Entrada: mensaje de Gmail (el mismo objeto del trigger)
const message = items[0].json.payload[0];

// Helper para extraer nombre y email del remitente
function parseFrom(header) {
  // Gmail devuelve algo como "Nombre Apellido <email@dominio.com>"
  const match = header.match(/^(.*)<(.+)>$/);
  if (match) {
    return {
      name: match[1].trim(),
      email: match[2].trim(),
    };
  }
  // Si solo viene el email
  return { name: '', email: header.trim() };
}

const from = parseFrom(message.from);

// Formateamos la fecha a ISO (para Notion)
const date = new Date(message.internalDate).toISOString();

return [
  {
    json: {
      // Campos que usaremos después
      from_name: from.name,
      from_email: from.email,
      subject: message.subject,
      date: date,
      // Opcional: cuerpo del mensaje (texto plano)
      body: message.textPlain || '',
      // Id del mensaje (por si quieres evitar duplicados)
      message_id: message.id,
    },
  },
];
```

**Salida del nodo** (ejemplo):

```json
{
  "from_name": "Juan Pérez",
  "from_email": "juan.perez@example.com",
  "subject": "Propuesta de colaboración",
  "date": "2026-04-25T14:32:10.000Z",
  "body": "Estimado..."
}
```

---

## 4️⃣ Nodo: **Notion – Create Page**

1. **Resource** → `Database`  
2. **Operation** → `Create`  
3. **Database ID** → *ID de la base de datos donde quieres guardar los correos* (puedes copiarlo de la URL de Notion).  
4. **Authentication** → Usa la credencial “Notion API” (OAuth token).  

### Mapeo de propiedades

| Propiedad en Notion | Tipo | Valor del workflow |
|---------------------|------|---------------------|
| **Remitente** (texto) | `Title` | `{{$json["from_name"]}}` |
| **Email** (texto) | `Rich Text` | `{{$json["from_email"]}}` |
| **Asunto** (texto) | `Rich Text` | `{{$json["subject"]}}` |
| **Fecha** (date) | `Date` | `{{$json["date"]}}` |
| **ID del mensaje** (texto) | `Rich Text` (opcional) | `{{$json["message_id"]}}` |
| **Cuerpo** (texto largo) | `Rich Text` (opcional) | `{{$json["body"]}}` |

> **Tip:** Si tu base de datos tiene más columnas (p.ej. “Estado”, “Tipo”), añádelas aquí con valores estáticos o derivados.

---

## 5️⃣ Nodo: **Slack – Send Message**

1. **Resource** → `Message`  
2. **Operation** → `Send`  
3. **Channel** → `#general` (o el canal que prefieras).  
4. **Authentication** → Credencial “Slack OAuth”.  

### Texto del mensaje (ejemplo):

```json
{
  "text": "*Nuevo email filtrado* :email:\n*Remitente:* {{ $json.from_name }} <{{ $json.from_email }}>\n*Asunto:* {{ $json.subject }}\n*Fecha:* {{ $json.date }}\n\nSe ha creado una página en Notion."
}
```

Puedes usar **Markdown** (n8n lo interpreta en Slack) o **blocks** si deseas un formato más rico.

---

## 6️⃣ (Opcional) Nodo: **No‑Match / Log**  

Si deseas registrar los correos que **no** cumplen el filtro, conecta la salida **false** del nodo IF a un nodo **Set** → **Add Field** (`reason: "No contiene palabras clave"`), y luego a un **Google Sheet**, **Airtable**, o simplemente a un **Webhook** para auditoría.

---

## 📦 Exportar el workflow (JSON)

Copia el siguiente bloque JSON y pégalo en **Import → Workflow** dentro de n8n.  
*(Asegúrate de reemplazar los IDs/credenciales por los tuyos antes de activarlo.)*

```json
{
  "name": "Gmail → Notion + Slack (Filtro propuesta/cotizacion)",
  "nodes": [
    {
      "parameters": {
        "resource": "message",
        "operation": "watch",
        "mailbox": "INBOX",
        "label": "",
        "includeAttachments": false,
        "markAsRead": false
      },
      "id": "1",
      "type": "n8n-nodes-base.gmailTrigger",
      "name": "Gmail Trigger",
      "typeVersion": 1,
      "position": [
        250,
        300
      ],
      "credentials": {
        "googleApi": "Google OAuth2"
      }
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "{{$json[\"payload\"][0].subject}}",
              "operation": "contains",
              "value2": "propuesta",
              "caseSensitive": false
            },
            {
              "value1": "{{$json[\"payload\"][0].subject}}",
              "operation": "contains",
              "value2": "cotizacion",
              "caseSensitive": false
            }
          ]
        }
      },
      "id": "2",
      "type": "n8n-nodes-base.if",
      "name": "If (Filtro asunto)",
      "typeVersion": 1,
      "position": [
        500,
        300
      ]
    },
    {
      "parameters": {
        "functionCode": "const message = items[0].json.payload[0];