# DeepSeek V4 Flash (NIM) — multi_turn/requirements_change

- model_id: `deepseek-ai/deepseek-v4-flash`
- success: True  | final: 6.05 | quality: 5.28
- latency_total: 22.749s | tokens_per_second: 40.7
- input_tokens: 244 | output_tokens: 926
- judge_score: 2.4 | justificación: 

## Respuesta completa

Perfecto, un workflow más completo. Te detallo la configuración:

## Workflow completo en N8N:

**1. Gmail Trigger (Trigger)**

- **Authentication**: OAuth2 con tu cuenta de Gmail
- **Event**: `message received`
- **Options**: Marcar `Include attachments` si necesitas adjuntos
- **Poll Times**: Cada 1-5 minutos (según necesites)

**2. Filter Node** (Filtrar asuntos)

- **Conditions** (Modo: "Simple"):
  - Campo: `{{ $json.subject }}`
  - Operación: `Contains` (case insensitive)
  - Valor: `propuesta`
  
- **OR** (segunda condición):
  - Campo: `{{ $json.subject }}`
  - Operación: `Contains`
  - Valor: `cotizacion`

**3. Function Node** (Extraer y formatear datos)

```javascript
// Extraer datos del remitente y formatear para Notion
const email = $json;

// Parsear el remitente (formato: "Nombre <email@dominio.com>")
const fromRaw = email.from || email.sender || '';
let senderName = '';
let senderEmail = '';

if (fromRaw.includes('<')) {
  const match = fromRaw.match(/^"?([^"<]*)"?\s*<([^>]+)>/);
  if (match) {
    senderName = match[1].trim();
    senderEmail = match[2].trim();
  }
} else {
  senderEmail = fromRaw.trim();
  senderName = senderEmail.split('@')[0];
}

// Formatear fecha
const date = new Date(email.date || email.receivedDate || Date.now());
const formattedDate = date.toISOString().split('T')[0];

// Retornar objeto limpio para Notion
return {
  sender_name: senderName,
  sender_email: senderEmail,
  subject: email.subject || 'Sin asunto',
  date_received: formattedDate,
  snippet: (email.text || email.snippet || '').substring(0, 200),
  message_id: email.id || email.messageId
};
```

**4. Notion Node** (Guardar en base de datos)

- **Authentication**: Notion API Token (crear integración)
- **Operation**: `Create a database item`
- **Database ID**: ID de tu base de datos Notion
- **Properties** (mapear exactamente a tus columnas):
  - `Nombre Remitente`: `{{ $json.sender_name }}`
  - `Email`: `{{ $json.sender_email }}`
  - `Asunto`: `{{ $json.subject }}`
  - `Fecha`: `{{ $json.date_received }}`
  - `Resumen`: `{{ $json.snippet }}`
  - `ID Mensaje`: `{{ $json.message_id }}`

**5. Slack Node** (Notificación)

- **Authentication**: Slack OAuth2
- **Channel**: `#propuestas` (o el que prefieras)
- **Text**: 
```
📩 *Nueva propuesta/cotización recibida*
*De:* {{ $json.sender_name }} ({{ $json.sender_email }})
*Asunto:* {{ $json.subject }}
*Fecha:* {{ $json.date_received }}
*Resumen:* {{ $json.snippet }}
```

**6. Conectar nodos**:
```
Gmail Trigger → Filter → Function → Notion
                                    ↓
                                  Slack
```

## Configuración extra importante:

**Para Notion**:
1. Crea una base de datos en Notion con columnas: `Nombre Remitente` (texto), `Email` (email), `Asunto` (texto), `Fecha` (fecha), `Resumen` (texto), `ID Mensaje` (texto)
2. Ve a `Settings & Integrations` → `Integrations` → `Develop or manage integrations`
3. Crea una nueva integración y conecta tu base de datos

**Para Slack**:
- Necesitas crear una app en `api.slack.com` con permisos `chat:write`
- Invitar el bot al canal donde quieres las notificaciones

¿Necesitas ayuda con algún paso específico?