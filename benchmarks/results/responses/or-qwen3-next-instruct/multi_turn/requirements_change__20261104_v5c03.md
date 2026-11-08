# Qwen 3-Next 80B Instruct — multi_turn/requirements_change

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 7.59 | quality: 8.0
- latency_total: 6.648s | tokens_per_second: 234.8
- input_tokens: 246 | output_tokens: 1561

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

¡Perfecto! Cambio de rumbo excelente: **Gmail → Notion + Slack Notification** con filtro por palabras clave. Aquí tienes el **workflow completo en N8N**, paso a paso, listo para copiar y pegar (o configurar manualmente).

---

### ✅ **Objetivo Final**
- Escuchar nuevos emails en Gmail.
- Filtrar solo los que tengan **"propuesta"** o **"cotización"** (case-insensitive) en el asunto.
- Extraer: **Remitente, Email, Asunto, Fecha**.
- Guardar esos datos en **Notion** como una nueva página en una base de datos.
- Enviar una notificación a **Slack** con los detalles.

---

## 🛠️ **Workflow en N8N (Configuración paso a paso)**

### 🔹 **1. Gmail Trigger (Nuevo Email)**
- **Nodo**: `Gmail`
- **Operation**: `Watch Emails`
- **Filter**:
  - `Subject Contains`: `propuesta,cotización`  
    *(N8N acepta múltiples valores separados por coma, y es case-insensitive)*
- **Options**:
  - `Include Attachments`: `false` (para ahorrar recursos)
  - `Include Body`: `true` (opcional, si quieres extraer contenido)
- **Output**: Te da `email`, `from`, `subject`, `date`, etc.

> ✅ **Nota**: N8N ya extrae automáticamente `from` como objeto con `name` y `email`.

---

### 🔹 **2. Function Node (Extraer y formatear datos)**
- **Nodo**: `Function`
- **Nombre**: `Extract & Format Data`
- **Function Code**:

```js
// Extraer datos del email
const from = items[0].json.from;
const subject = items[0].json.subject;
const date = items[0].json.date;

// Formatear para Notion
const notionData = {
  "Nombre del remitente": from.name || from.email,
  "Email del remitente": from.email,
  "Asunto": subject,
  "Fecha de recepción": new Date(date).toISOString()
};

// Formatear para Slack
const slackMessage = `🆕 *Nueva propuesta/cotización recibida!* \n\n*Remitente:* ${from.name || from.email}\n*Email:* \`${from.email}\`\n*Asunto:* ${subject}\n*Fecha:* ${new Date(date).toLocaleString()}`;

// Retornar ambos objetos
return [
  {
    json: notionData,
    binary: {},
    metadata: {},
    pairedItem: { item: 0 }
  },
  {
    json: { message: slackMessage },
    binary: {},
    metadata: {},
    pairedItem: { item: 0 }
  }
];
```

> ✅ Esto crea **dos salidas**: una para Notion, otra para Slack.

---

### 🔹 **3. Notion Node (Crear página en Base de Datos)**
- **Nodo**: `Notion`
- **Operation**: `Create Page`
- **Authentication**: Conecta tu cuenta de Notion (debes tener un bot integrado y el ID de la base de datos).
- **Database ID**: 📌 *¡Importante!* Pega aquí el ID de tu base de datos de Notion (es la parte final de la URL: `https://www.notion.so/yourworkspace/...[ID]`).
- **Properties**:
  - Selecciona **"Use JSON"**.
  - En el campo JSON, pon esto:

```json
{
  "Nombre del remitente": "={{$json['Nombre del remitente']}}",
  "Email del remitente": "={{$json['Email del remitente']}}",
  "Asunto": "={{$json['Asunto']}}",
  "Fecha de recepción": "={{$json['Fecha de recepción']}}"
}
```

> ✅ **Requisito previo en Notion**:
> - Tu base de datos debe tener **4 propiedades de tipo "Title" o "Text"** con los nombres exactos:  
>   `Nombre del remitente`, `Email del remitente`, `Asunto`, `Fecha de recepción`.

---

### 🔹 **4. Slack Node (Enviar notificación)**
- **Nodo**: `Slack`
- **Operation**: `Send Message`
- **Authentication**: Conecta tu cuenta de Slack (necesitas un webhook o token de bot).
- **Channel**: Escribe el ID del canal (ej: `#notificaciones-propuestas`) o el nombre `#nombre-del-canal`.
- **Message**:  
  ```json
  {{"text": "={{$json['message']}}" }}
  ```
- **Format**: `Markdown`

> ✅ Slack acepta Markdown. El mensaje tendrá negritas, emojis y formato limpio.

---

## 🧩 **Conexión final del workflow**

```
[Gmail Trigger]
        ↓
[Function: Extract & Format Data]
        ↓         ↓
   [Notion]     [Slack]
```

> ⚠️ **Importante**: El nodo Function debe tener **dos salidas** (como se muestra en el código). N8N permite múltiples salidas en funciones. Asegúrate de que el nodo se conecte a **dos nodos diferentes**.

---

## ✅ **Requisitos previos**

| Servicio | Requisito |
|---------|-----------|
| **Gmail** | Habilitar API de Gmail en Google Cloud Console (N8N lo guía al conectar). |
| **Notion** | 1. Crear un bot en [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations) <br> 2. Compartir la base de datos con el bot <br> 3. Copiar el **Database ID** (URL). |
| **Slack** | 1. Crear un **Incoming Webhook** en [https://api.slack.com/messaging/webhooks](https://api.slack.com/messaging/webhooks) <br> 2. Pegar la URL del webhook en N8N. |

---

## 💡 Bonus: ¿Quieres que el workflow sea más robusto?

- Añade un **"Catch Error"** nodo para recibir alertas si falla.
- Usa un **"Webhook"** para activar manualmente el workflow durante pruebas.
- Si quieres **guardar el cuerpo del email**, añade `includeBody: true` en Gmail y extrae `html` o `text` en el Function node.

---

## 🚀 ¡Listo!

Con este workflow:
- Solo procesas emails con **"propuesta" o "cotización"** en el asunto.
- Los datos van limpios a **Notion**.
- Recibes una notificación **en Slack** con formato bonito.
- ¡Nada de Google Sheets! 😎

¿Quieres que te genere el **JSON exportable del workflow** para importarlo directamente en N8N? ¡Dime y te lo preparo!