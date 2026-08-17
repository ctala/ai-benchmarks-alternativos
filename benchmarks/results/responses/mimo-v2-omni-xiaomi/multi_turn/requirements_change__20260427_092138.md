# MiMo V2-Omni (Xiaomi direct) — multi_turn/requirements_change

- model_id: `mimo-v2-omni`
- success: True  | final: 6.37 | quality: 4.64
- latency_total: 9.671s | tokens_per_second: 114.7
- input_tokens: 244 | output_tokens: 1109
- judge_score: 2.2 | justificación: 

## Respuesta completa

Perfecto, ajustemos el workflow. Ahora sería:

1. **Gmail Trigger** → 2. **IF (filtro)** → 3. **Function (extraer datos)** → 4. **Notion** → 5. **Slack**

Te detallo cada nodo:

## 1. Gmail Trigger
- **Evento**: `Message received`
- **Credenciales**: Conectar tu cuenta de Gmail
- **Opciones**: Puedes especificar `labelIds` si quieres filtrar por etiqueta (ej: INBOX)

## 2. Nodo IF (Filtro)
```
Condición: {{ $json.subject.toLowerCase().includes('propuesta') || $json.subject.toLowerCase().includes('cotización') }}
```
- Si es **TRUE** → pasa al siguiente nodo
- Si es **FALSE** → termina el flujo

## 3. Function node (Extraer datos)
```javascript
return {
  senderName: $json.from.value[0].name,
  senderEmail: $json.from.value[0].address,
  subject: $json.subject,
  date: $json.date,
  snippet: $json.snippet,
  messageId: $json.id
};
```

## 4. Notion node
- **Operación**: `Create a database item`
- **Database ID**: Tu base de datos de Notion
- **Mapeo de propiedades**:
  - `Remitente`: {{ $json.senderName }}
  - `Email`: {{ $json.senderEmail }}
  - `Asunto`: {{ $json.subject }}
  - `Fecha`: {{ $json.date }}
  - `Snippet`: {{ $json.snippet }}

## 5. Slack node
- **Operación**: `Send a message`
- **Channel**: Tu canal de Slack (ej: #prouestas)
- **Texto**:
```
:Nuevo email con propuesta/cotización:
*De:* {{ $json.senderName }} <{{ $json.senderEmail }}>
*Asunto:* {{ $json.subject }}
*Fecha:* {{ $json.date }}
```

## Configuración adicional necesaria:
1. **Notion Integration**: Crear una integración en Notion y conectarla en N8N
2. **Slack App**: Crear una app en Slack con permisos para `chat:write`
3. **Base de datos Notion**: Asegúrate de que la base tenga las propiedades con los nombres correctos

¿Quieres que te ayude con la configuración específica de alguna de estas integraciones?