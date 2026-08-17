# Mistral Small 4 — multi_turn/requirements_change

- model_id: `mistralai/mistral-small-2603`
- success: True  | final: 6.6 | quality: 5.28
- latency_total: 8.515s | tokens_per_second: 147.5
- input_tokens: 239 | output_tokens: 1256
- judge_score: 2.4 | justificación: 

## Respuesta completa

¡Perfecto! Aquí tienes el **workflow completo** en **n8n** con todas tus especificaciones:

---

### **📌 Objetivo del Workflow:**
1. **Escuchar nuevos emails en Gmail** (Trigger).
2. **Filtrar solo emails** con *"propuesta"* o *"cotización"* en el asunto.
3. **Extraer datos del remitente** (nombre, email, asunto, fecha).
4. **Enviar notificación a Slack** cuando llegue un email que cumpla el filtro.
5. **Guardar los datos en una base de datos de Notion**.

---

## **🔧 Configuración Paso a Paso**

### **1️⃣ Nodo: Gmail Trigger (Disparador)**
- **Configuración:**
  - **Trigger:** *"On Email Received"*
  - **Gmail Account:** Conecta tu cuenta de Gmail.
  - **Options → Filter Criteria:**
    - **Subject:** `*propuesta* OR *cotización*`
    - *(Esto filtra solo emails con esas palabras clave en el asunto)*

---

### **2️⃣ Nodo: Function (Extraer datos del remitente)**
- **Código JavaScript:**
  ```javascript
  // Extraer datos del email
  const email = items[0].json.headers.from;
  const name = email.split('<')[0].trim();
  const emailAddress = email.match(/<([^>]+)>/)[1];

  // Devolver los datos estructurados
  return [{
    json: {
      remitente_nombre: name,
      remitente_email: emailAddress,
      asunto: items[0].json.headers.subject,
      fecha: new Date(items[0].json.headers.date).toISOString(),
      mensaje: items[0].json.text || "Sin cuerpo de email"
    }
  }];
  ```
- **Salida esperada:**
  ```json
  {
    "remitente_nombre": "Juan Pérez",
    "remitente_email": "juan@example.com",
    "asunto": "Propuesta de proyecto",
    "fecha": "2024-05-20T12:00:00.000Z",
    "mensaje": "Hola, te envío..."
  }
  ```

---

### **3️⃣ Nodo: Slack (Notificación en tiempo real)**
- **Configuración:**
  - **Slack Account:** Conecta tu workspace de Slack.
  - **Channel:** `#alertas-emails` (o el que prefieras).
  - **Message:**
    ```markdown
    📩 *Nuevo email filtrado:*
    - **Remitente:** `{{ $json.remitente_nombre }}` ({{ $json.remitente_email }})
    - **Asunto:** `{{ $json.asunto }}`
    - **Fecha:** `{{ $json.fecha }}`
    - **Ver email:** [Abrir en Gmail](https://mail.google.com/mail/#inbox/{{ $run.item.id }})
    ```

---

### **4️⃣ Nodo: Notion (Guardar datos en una base de datos)**
- **Configuración:**
  - **Notion Account:** Conecta tu API key de Notion.
  - **Database ID:** Copia el ID de tu base de datos en Notion (ej: `1234567890abcdef...`).
  - **Properties Mapping:**
    | Campo en Notion | Valor en n8n |
    |----------------|-------------|
    | **Nombre** | `{{ $json.remitente_nombre }}` |
    | **Email** | `{{ $json.remitente_email }}` |
    | **Asunto** | `{{ $json.asunto }}` |
    | **Fecha** | `{{ $json.fecha }}` |
    | **Mensaje** | `{{ $json.mensaje }}` |

---

## **📊 Diagrama del Workflow**
```
Gmail Trigger → Function (Extraer datos) → Slack (Notificar) → Notion (Guardar)
```

---

## **⚙️ Requisitos Previos**
1. **Gmail:** Habilitar API de Gmail en [Google Cloud Console](https://console.cloud.google.com/).
2. **Slack:** Crear un [Webhook](https://api.slack.com/messaging/webhooks) en Slack.
3. **Notion:**
   - Crear una base de datos con estos campos:
     - **Nombre** (Texto)
     - **Email** (Email)
     - **Asunto** (Texto)
     - **Fecha** (Fecha)
     - **Mensaje** (Texto largo)
   - Obtener la **API Key** en [Notion Integrations](https://www.notion.so/my-integrations).

---

## **🚀 ¿Cómo probarlo?**
1. **Activa el workflow** en n8n.
2. **Envía un email** a tu cuenta con el asunto:
   - *"Propuesta para tu negocio"*
   - *"Cotización de servicios"*
3. **Verifica en Slack** que llegue la notificación.
4. **Revisa Notion** para confirmar que se guardó el registro.

---

### **🔄 Posibles mejoras**
- **Filtrar por dominio de email** (ej: solo `@empresa.com`).
- **Enviar un resumen diario** en lugar de notificaciones en tiempo real.
- **Agregar un nodo de "Condicional"** para separar propuestas de cotizaciones.

¿Necesitas ayuda para implementar alguna de estas mejoras? 😊