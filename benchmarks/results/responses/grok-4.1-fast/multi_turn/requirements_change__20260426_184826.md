# Grok 4.1 Fast — multi_turn/requirements_change

- model_id: `x-ai/grok-4.1-fast`
- success: True  | final: 7.23 | quality: 7.52
- latency_total: 16.994s | tokens_per_second: 93.8
- input_tokens: 368 | output_tokens: 1594
- judge_score: 4.0 | justificación: La respuesta es precisa y clara, con una estructura bien organizada que incluye pasos detallados para implementar el workflow en N8N. Aunque cambia los requisitos originales de Google Sheets a Notion, sigue siendo relevante al proporcionar un flujo de trabajo funcional. Ofrece profundidad al explicar configuraciones y código JavaScript, lo cual es útil para emprendedores.

## Respuesta completa

¡Genial! Cambio de plan bien tomado. Te detallo el **workflow completo paso a paso** para N8N. Este fluye así:

```
Gmail Trigger → IF (filtro asunto) → Function (extraer datos) → Notion (guardar) → Slack (notificar)
```

**Requisitos previos** (configúralos en N8N > Credentials):
- **Gmail**: OAuth2 con permisos de lectura (elige la cuenta/carpeta, ej: Inbox).
- **Notion**: API Token (Internal Integration Token de Notion). Necesitas una **Database en Notion** con propiedades:
  | Propiedad | Tipo |
  |-----------|------|
  | Remitente Email | Email |
  | Remitente Nombre | Title o Text |
  | Asunto | Rich Text |
  | Fecha | Date |
  | Cuerpo (opcional) | Rich Text |
- **Slack**: OAuth2 o Bot Token. Elige canal o usuario.

### 1. **Gmail Trigger** (nodo inicial)
   - **Resource**: Message
   - **Operation**: On message
   - **Label**: `propuesta OR cotizacion` (opcional, para filtrar en Gmail directamente, pero usaremos IF para precisión).
   - **Download Attachments**: No (a menos que quieras).
   - **Simple**: Yes (para datos básicos).
   - Activa **Polling** cada 1-5 min.

### 2. **IF Node** (filtro por asunto)
   - Conecta después de Gmail.
   - **Conditions**:
     | Value 1 | Operation | Value 2 |
     |---------|-----------|---------|
     | `{{ $json.subject.toLowerCase() }}` | **Contains** | `propuesta` |
     - **OR** otra condición: `{{ $json.subject.toLowerCase() }}` **Contains** `cotizacion`
   - **True** → siguiente nodo.
   - **False** → nada (o un NoOp).

### 3. **Function Node** (extraer y formatear datos del remitente)
   - Conecta en la rama **True** del IF.
   - **JavaScript Code**:
     ```javascript
     const emailData = $input.first().json;

     // Parsear remitente: "Nombre <email@ejemplo.com>" → {name, email}
     const fromMatch = emailData.from.match(/(.+?)\s*<(.+?)>/);
     const senderName = fromMatch ? fromMatch[1].trim() : 'Sin nombre';
     const senderEmail = fromMatch ? fromMatch[2] : emailData.from;

     return [{
       json: {
         senderName: senderName,
         senderEmail: senderEmail,
         subject: emailData.subject,
         date: emailData.date,  // ISO format
         body: emailData.textPlain || emailData.textHtml || 'Sin cuerpo'
       }
     }];
     ```
   - Esto extrae: nombre, email, asunto, fecha, cuerpo (texto plano preferido).

### 4. **Notion Node** (guardar en DB)
   - **Resource**: Database
   - **Operation**: Create
   - **Database ID**: Pega el ID de tu DB Notion (ej: `https://www.notion.so/tuworkspace/abc123?v=...` → `abc123`).
   - **Property Values** (mapear desde Function):
     | Property | Value |
     |----------|-------|
     | Remitente Email | `{{ $json.senderEmail }}` |
     | Remitente Nombre | `{{ $json.senderName }}` |
     | Asunto | `{{ $json.subject }}` |
     | Fecha | `{{ $json.date }}` (Notion lo parsea auto) |
     | Cuerpo | `{{ $json.body.substring(0, 1000) }}` (limita chars si es Rich Text) |
   - **Add Parent Page?**: No, si es DB standalone.

### 5. **Slack Node** (notificación)
   - **Resource**: Message
   - **Operation**: Post
   - **Channel**: Elige canal/usuario (ej: #propuestas).
   - **Text**:
     ```
     🆕 Nueva *propuesta/cotización*!

     📧 De: {{ $json.senderName }} <{{ $json.senderEmail }}>
     📋 Asunto: {{ $json.subject }}
     📅 Fecha: {{ $json.date }}
     🔗 [Ver en Notion] (link_a_tu_db_filtrado)
     ```
   - Opcional: **Attachments** con bloques Slack para formato rico.

### Pasos para implementarlo:
1. Crea un nuevo workflow en N8N.
2. Arrastra nodos en orden y conecta.
3. Configura credenciales y prueba con **Execute Workflow** (envía un email de prueba con "propuesta" en asunto).
4. Activa el workflow (▶️).

**Tips**:
- **Errores comunes**: Verifica permisos Notion (comparte DB con tu Integration). Gmail OAuth debe ser "Gmail API".
- **Mejoras**: Agrega **Set Node** antes de Notion para formatear fecha (`{{ new Date($json.date).toLocaleDateString('es-ES') }}`).
- **Escalabilidad**: Si llegan muchos emails, usa **Webhook** en lugar de polling.
- **Export JSON**: Si quieres, activa el workflow, ve a "Executions" > copia el JSON y pégalo aquí para debuggear.

¿Necesitas screenshots, el JSON exportado, o ajustes (ej: adjuntos, labels específicas)? ¡Dime! 🚀