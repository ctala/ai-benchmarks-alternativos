# Ministral 14B (NIM) — multi_turn/requirements_change

- model_id: `mistralai/ministral-14b-instruct-2512`
- success: True  | final: 6.04 | quality: 6.4
- latency_total: 81.427s | tokens_per_second: 21.9
- input_tokens: 227 | output_tokens: 1783
- judge_score: 3.2 | justificación: 

## Respuesta completa

¡Perfecto! Aquí tienes un **workflow completo en n8n** para:
1. **Leer emails de Gmail** (solo con "propuesta" o "cotización" en el asunto).
2. **Extraer datos clave** (remitente, asunto, cuerpo, adjuntos si hay).
3. **Guardarlos en Notion** (en una base de datos personalizada).
4. **Enviar notificación a Slack** cuando llegue un correo relevante.

---

### **🔧 Workflow en n8n (Pasos detallados)**

#### **1️⃣ Trigger: "Gmail - Watch Emails"** (Nodo inicial)
- **Acción**: *"Trigger"* (Para activar el workflow con nuevos emails).
- **Configuración clave**:
  - **Authenticate via OAuth2**: Usa una conexión con tu cuenta de Gmail (necesitas configurar credenciales OAuth previamente en n8n).
  - **Folder**: `"INBOX"` (o la carpeta que prefieras).
  - **Label**: (Opcional, si quieres filtrar por etiquetas).
  - **Filter Emails**: Aquí aplicamos el filtro de asunto.
    ```json
    {
      "query": "subject:propuesta OR subject:cotización",
      "queryOptions": {
        "includeSpamTrash": false
      }
    }
    ```
  - **Polling Interval**: `"30s"` (cada 30 segundos revisa si hay nuevos emails).

---

#### **2️⃣ Procesar datos: "Function Node"**
- **Acción**: *"Execute Function"* (Para extraer y estructurar los datos).
- **JavaScript a ejecutar**:
  ```javascript
  // Formateamos los datos del email para Notion y Slack
  const remitente = {
    nombre: item.rawInput.emailFrom?.name || "Sin nombre",
    email: item.rawInput.emailFrom?.email || "sin-email@example.com"
  };

  // Si el cuerpo es muy largo, truncamos para Notion (opcional)
  const cuerpoTruncado = item.rawInput?.bodyPreview?.length > 500
    ? item.rawInput.bodyPreview.substring(0, 500) + "..."
    : item.rawInput.bodyPreview;

  return {
    remitente,
    asunto: item.rawInput.subject,
    cuerpo: cuerpoTruncado,
    fecha: new Date(item.rawInput.date).toLocaleString(),
    adjuntos: item.rawInput?.attachments || [],
    linkEmail: item.rawInput.emailMessageId ? `https://mail.google.com/mail/u/0/#inbox/${item.rawInput.emailMessageId}` : null
  };
  ```
- **Salida**: Un objeto con los datos estructurados para Notion y Slack.

---

#### **3️⃣ Guardar en Notion: "Notion API - Create Database Item"**
- **Acción**: *"Create a Database Item"* (Usa la API de Notion).
- **Configuración**:
  - **Authentication**: Conecta tu base de datos de Notion (necesitas generar un *Integration Token* en [Notion Developers](https://www.notion.so/my-integrations)).
  - **Database ID**: El ID de tu tabla en Notion (ejemplo: `1234567890abcdef`).
  - **Properties**: Mapea los campos del Function Node a los de Notion. Ejemplo:
    | Campo en Notion       | Valor desde Function Node          |
    |-----------------------|------------------------------------|
    | **Remitente**         | `{{ $json["remitente"]["nombre"] }}` |
    | **Email del remitente** | `{{ $json["remitente"]["email"] }}` |
    | **Asunto**            | `{{ $json["asunto"] }}`             |
    | **Cuerpo**            | `{{ $json["cuerpo"] }}`             |
    | **Fecha**            | `{{ $json["fecha"] }}`              |
    | **Adjuntos**         | `{{ $json["adjuntos"].length }}`    |
    | **Link al email**    | `{{ $json["linkEmail"] }}`          |

  - **Opcional**: Si usas un campo de tipo *Select* o *Multi-Select* en Notion, asegúrate de que el valor coincida exactamente (ej: `"Propuesta"` en lugar de `"propuesta"`).

---

#### **4️⃣ Notificación en Slack: "Slack - Send Message"**
- **Acción**: *"Send Message to a Channel"*.
- **Configuración**:
  - **Authentication**: Usa tu token de API de Slack (de [Slack API](https://api.slack.com/apps)).
  - **Channel**: El ID o nombre del canal donde quieres las notificaciones (ej: `#alertas-propuestas`).
  - **Message**: Plantilla personalizable. Ejemplo:
    ```
    ⚡ *Nuevo email relevante en Gmail:*
    📌 **Asunto:** {{ $json["asunto"] }}
    👤 **De:** {{ $json["remitente"]["nombre"] }} <{{ $json["remitente"]["email"] }}>
    📅 **Fecha:** {{ $json["fecha"] }}
    🔗 **Ver email:** {{ $json["linkEmail"] }}
    ```
  - **Opcional**: Puedes añadir un emoji dinámico o un botón para acciones rápidas (usando *message actions* de Slack).

---

### **🔄 Ejecución del Workflow**
1. **Orden de los nodos**:
   `Gmail Trigger` → `Function Node` → **Split** (opcional, para enviar a Notion y Slack en paralelo) → `Notion API` y `Slack`.
   *(Si prefieres secuencial, puedes omitir el split y ejecutar Notion primero, luego Slack).*

2. **Split (opcional)**:
   - Usa un nodo *"Set"* o *"If"* para dividir la ejecución si quieres lógica adicional (ej: solo enviar a Slack si hay adjuntos).

---

### **⚠️ Consideraciones importantes**
1. **Notion Database**:
   - Asegúrate de que tu tabla en Notion tenga los campos correctos (ej: *Text*, *Email*, *Date*, etc.).
   - Si usas campos de tipo *Relation*, necesitarás el ID de la página relacionada.

2. **Autenticación**:
   - **Gmail**: Configura OAuth2 en n8n (necesitas habilitar "Acceso a APIs menos seguras" en la cuenta de Gmail o usar una cuenta de servicio).
   - **Slack**: Usa un *Bot Token* con permisos para enviar mensajes en el canal.
   - **Notion**: Crea una *Integration* en Notion y usa el *Internal Integration Token*.

3. **Errores**:
   - Si el workflow falla, revisa los logs de n8n (pestaña *"Execution"*).
   - Para emails con adjuntos, puedes añadir un paso para guardarlos en Google Drive y vincularlos en Notion.

4. **Frecuencia**:
   - El `Polling Interval` en Gmail no debe ser menor a 30 segundos (para evitar límites de API).

---

### **📌 Ejemplo visual del workflow**
```
Gmail Trigger (Watch Emails)
       ↓
Function Node (Parsear datos)
       ↓
[Split] → Notion API (Guardar en DB)
       ↓
[Split] → Slack (Enviar notificación)
```

---
### **🔧 ¿Necesitas ayuda con algo más?**
- ¿Quieres que el workflow **procesa los adjuntos** y los guarde en Google Drive?
- ¿Prefieres que los datos de Notion se guarden en una **página nueva** en lugar de una tabla?
- ¿Quieres añadir un **filtro por remitente específico** (ej: solo emails de "clientes@ejemplo.com")?