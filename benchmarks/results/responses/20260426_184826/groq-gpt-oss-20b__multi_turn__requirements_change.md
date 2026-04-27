# GPT-OSS 20B (Groq) — multi_turn/requirements_change

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 7.38 | quality: 7.24
- latency_total: 2.283s | tokens_per_second: 837.1
- input_tokens: 290 | output_tokens: 1911
- judge_score: 3.8 | justificación: 

## Respuesta completa

¡Claro! Te dejo una guía paso‑a‑paso para crear el workflow en **n8n** que:

1. Se activa con cada nuevo correo de Gmail.  
2. Filtra solo los que tengan “propuesta” o “cotización” en el asunto.  
3. Extrae los datos del remitente (nombre, email, asunto, fecha).  
4. Guarda esa información en una base de datos de **Notion**.  
5. Envía una notificación a **Slack** cuando se cumpla la condición.

---

## 1️⃣ Requisitos previos

| Herramienta | Acción a realizar |
|-------------|-------------------|
| **Gmail** | Crear una cuenta de servicio o usar OAuth 2.0 (para n8n) y conceder acceso a tu buzón. |
| **Notion** | Crear una base de datos (tabla) con los campos que quieres registrar: `Sender Name`, `Sender Email`, `Subject`, `Date`, `Body` (opcional). Obtener el **ID** de la base de datos y un **token** de integración. |
| **Slack** | Crear un *Incoming Webhook* o un bot con permisos de envío de mensajes. Obtener el **URL** del webhook o el **token** de bot. |

> **Tip:** En n8n puedes usar el nodo **Credentials** para guardar estos datos de forma segura.

---

## 2️⃣ Estructura del workflow

```
Gmail Trigger
   ├─> IF (Filtrar asunto)
   │     ├─> Function (Parsear datos)
   │     │     ├─> Notion (Crear página)
   │     │     └─> Slack (Notificar)
   └─> (else)  (No hacer nada)
```

### 2.1 Nodo: Gmail Trigger

1. Añade un nodo **Gmail Trigger**.  
2. Selecciona **Trigger** → **New Email**.  
3. En la sección *Search Query* puedes poner:
   ```
   subject:propuesta OR subject:cotizacion
   ```
   > Si prefieres filtrar en un nodo IF, deja esta sección vacía y usa el nodo IF después.

### 2.2 Nodo: IF (Filtrar asunto) – Opcional

Si no usas la búsqueda en Gmail:

1. Añade un nodo **IF**.  
2. Configura la condición:
   ```
   {{ $json["subject"] && ($json["subject"].toLowerCase().includes("propuesta") || $json["subject"].toLowerCase().includes("cotizacion")) }}
   ```
3. Conecta la salida `true` a los siguientes nodos.  
4. Conecta la salida `false` a un nodo **Noop** o simplemente déjala sin salida.

### 2.3 Nodo: Function (Parsear datos)

Este nodo transforma los datos del correo en el formato que Notion y Slack necesitan.

```javascript
// Function node: parseEmail.js
const email = $json;

const senderName = email["from"].split("<")[0].trim();
const senderEmail = email["from"].match(/[<](.*?)[>]/)[1];
const subject = email["subject"];
const date = email["date"];
const body = email["body"]?.plain || email["body"]?.html || "";

return {
  json: {
    senderName,
    senderEmail,
    subject,
    date,
    body
  }
};
```

> **Nota:** `email["from"]` suele venir en formato `"Nombre <correo@ejemplo.com>"`. Si tu Gmail devuelve otro formato, ajusta el regex.

### 2.4 Nodo: Notion (Crear página)

1. Añade un nodo **Notion** → **Create Page**.  
2. Selecciona la base de datos que creaste.  
3. Mapea los campos:

| Campo Notion | Valor |
|--------------|-------|
| `Sender Name` | `{{ $json["senderName"] }}` |
| `Sender Email` | `{{ $json["senderEmail"] }}` |
| `Subject` | `{{ $json["subject"] }}` |
| `Date` | `{{ $json["date"] }}` |
| `Body` | `{{ $json["body"] }}` (opcional) |

> Si tu tabla tiene tipos de campo diferentes (p.ej. `Date` como tipo *Date*), asegúrate de pasar el formato correcto (`YYYY-MM-DDTHH:mm:ssZ`).

### 2.5 Nodo: Slack (Notificar)

1. Añade un nodo **Slack** → **Send Message**.  
2. Selecciona tu canal o ID de conversación.  
3. Mensaje:

```
📬 Nueva propuesta recibida
• Remitente: {{ $json["senderName"] }} <{{ $json["senderEmail"] }}>
• Asunto: {{ $json["subject"] }}
• Fecha: {{ $json["date"] }}
```

> Si usas un *Incoming Webhook*, el nodo Slack será el tipo **Webhook** y solo necesitarás la URL del webhook.

---

## 3️⃣ Conexiones y flujo

```
Gmail Trigger
   │
   ├─> IF (subject contains "propuesta" or "cotizacion") ──┐
   │                                                      │
   ├─> Function (parseEmail.js)                           │
   │                                                      │
   ├─> Notion (Create Page)                               │
   │                                                      │
   └─> Slack (Send Message)                               │
```

- Si usas la búsqueda en Gmail, omite el nodo **IF** y conéctalo directamente al nodo **Function**.  
- Si decides filtrar en el nodo IF, la salida `false` simplemente no hace nada (puedes conectar a un nodo **Noop**).

---

## 4️⃣ Validación rápida

1. **Prueba** con un correo de prueba que contenga “propuesta” en el asunto.  
2. Revisa la base de datos de Notion: debería aparecer una nueva página con los datos.  
3. Verifica el canal de Slack: deberías recibir la notificación.  
4. Envía un correo sin la palabra clave y confirma que no se cree nada.

---

## 5️⃣ Tips de mejora

| Idea | Por qué |
|------|---------|
| **Uso de “Trigger: New Email Matching Search”** | Reduce tráfico de n8n, Gmail solo envía eventos que ya cumplen la condición. |
| **Añadir un nodo “Set” antes de Notion** | Puedes normalizar datos (e.g., formatear la fecha a `YYYY-MM-DD`). |
| **Manejo de errores** | Añade un nodo **Error Trigger** y envía un mensaje a Slack con el error. |
| **Logs** | Usa un nodo **Write Binary Data** o **Set** para guardar el cuerpo del correo en un bucket S3/Google Cloud Storage. |
| **Escalabilidad** | Si recibes cientos de correos, considera usar la opción “Batch” en el nodo Notion (crea varias páginas a la vez). |

---

### ¡Listo! 🎉

Con esto tendrás un workflow automático que:

- **Detecta** correos con “propuesta” o “cotización”.  
- **Extrae** remitente, asunto, fecha y cuerpo.  
- **Almacena** la información en Notion.  
- **Informa** al equipo vía Slack.

Si necesitas que te ayude a configurar los credenciales o a depurar algún paso, avísame. ¡Éxitos con tu automatización!