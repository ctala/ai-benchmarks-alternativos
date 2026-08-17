# DeepSeek V4 Pro — multi_turn/requirements_change

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 6.34 | quality: 6.96
- latency_total: 34.991s | tokens_per_second: 47.4
- input_tokens: 244 | output_tokens: 1658
- judge_score: 3.6 | justificación: 

## Respuesta completa

Perfecto, adaptamos el flujo. Tu nuevo workflow queda así:

1. **Gmail Trigger** (activación por cada nuevo correo)  
2. **Filtro condicional** (solo si el asunto contiene "propuesta" o "cotización")  
3. **Extracción de datos del remitente** (nombre, email, asunto, fecha)  
4. **Guardado en Notion** (nueva página en base de datos)  
5. **Notificación en Slack** (mensaje automático)

A continuación te detallo cada paso con la configuración necesaria.

---

## 1. Nodo Gmail Trigger

- **Nodo**: `Gmail Trigger`  
- **Evento**: `Message Received`  
- Autenticación: conecta tu cuenta de Gmail.  
- Opciones: puedes dejar la carpeta por defecto (INBOX) o especificar un label.

---

## 2. Nodo IF (filtro por palabra clave)

- **Nodo**: `IF`  
- **Condiciones** (modo "OR"):  
  1. `{{ $json["subject"].toLowerCase().includes("propuesta") }}`  
  2. `{{ $json["subject"].toLowerCase().includes("cotización") }}`  
     (si manejás tildes, incluí `cotizacion` también)  
- Si **Verdadero**: continúa al siguiente nodo.  
- Si **Falso**: podés terminar con un nodo `NoOp` o simplemente no conectar nada.

Nota: en n8n, las condiciones se escriben como expresiones. Podés armar dos ramas "true" y "false".

---

## 3. Nodo Function (extraer datos del remitente)

Este nodo parsea la cabecera `From` y estructura los datos para Notion/Slack.

```javascript
const from = $json.from; // ej: "Juan Pérez <juan@empresa.com>"
let name = "";
let email = "";

// Extraer nombre y correo con regex
const match = from.match(/^"?([^"<]*)"?\s*<?([^>]*)>?$/);
if (match) {
  name = match[1].trim();
  email = match[2];
} else {
  // Si no coincide, usar el campo completo como nombre y dejarlo así
  name = from;
}

return [{
  json: {
    name: name,
    email: email,
    subject: $json.subject,
    date: $json.date,
    snippet: $json.snippet, // opcional, primeros caracteres del cuerpo
    threadId: $json.threadId
  }
}];
```

Colocá este código en el `Function` node.

---

## 4. Nodo Notion (crear página en base de datos)

- **Nodo**: `Notion` (operación: `Create a Database Page`)  
- **Autenticación**: conectá tu integración de Notion.  
- **Database ID**: pegá el ID de la base de datos donde guardarás los correos.  
- **Propiedades**: mapeá los campos extraídos.  
  - Título (title): `{{ $json.subject }}`  
  - Name: `{{ $json.name }}`  
  - Email: `{{ $json.email }}`  
  - Date: `{{ $json.date }}`  
  - Snippet: (opcional)  
  - Podés agregar un campo "Origen" fijo con valor "Gmail automático" si querés.

Nota: la base de datos de Notion debe tener esos atributos (Name, Email, Date, etc.) creados previamente, o bien podés usar propiedades dinámicas si ya están definidas.

---

## 5. Nodo Slack (enviar notificación)

- **Nodo**: `Slack` (operación: `Send a Message`)  
- **Autenticación**: conectá tu workspace.  
- **Channel**: escribí el nombre del canal o usuario al que llegará la alerta.  
- **Text**: usa un mensaje como:  

```
📩 Nueva propuesta/cotización recibida  
Remitente: {{ $json.name }} ({{ $json.email }})  
Asunto: {{ $json.subject }}  
Fecha: {{ $json.date }}  
```

Si querés incluir un link a la página de Notion, podés generar la URL con el ID de la base de datos y el ID de la página que devuelve el nodo Notion (`{{ $json.id }}`).

---

## Diagrama del workflow

```mermaid
graph LR
    A[Gmail Trigger] --> B{IF (asunto contiene<br>propuesta o cotización?)}
    B -- true --> C[Function<br>Extraer remitente]
    B -- false --> D[NoOp / Fin]
    C --> E[Notion<br>Crear página]
    E --> F[Slack<br>Notificar]
```

---

## Credenciales necesarias

- Gmail (OAuth2)  
- Notion (API Key + conexión a la base de datos)  
- Slack (Bot Token con permisos `chat:write`)

Podés importar este diseño como template una vez que tengas las credenciales. ¿Querés que te pase el JSON del workflow para importarlo directamente en tu instancia de n8n?