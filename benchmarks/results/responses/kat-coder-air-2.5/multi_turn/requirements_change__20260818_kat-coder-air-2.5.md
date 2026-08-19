# KAT Coder Air v2.5 — multi_turn/requirements_change

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 7.72 | quality: 8.0
- latency_total: 7.545s | tokens_per_second: 191.8
- input_tokens: 233 | output_tokens: 1447

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



¡Perfecto! Vamos a ajustar el workflow con estos nuevos requisitos. Aquí te detallo la configuración paso a paso:

## Workflow Actualizado

### 1. **Gmail Trigger** (Trigger)
- **Trigger Event**: `New Email`
- **Folder**: `INBOX` (o la que prefieras)
- **Polling Interval**: 1-5 minutos
- **Auth**: Conecta tu cuenta de Gmail

> *Nota: El trigger de Gmail no permite filtrar por palabras clave de manera directa, así que haremos el filtro en el siguiente nodo.*

### 2. **Function Node** - Extraer y Filtrar
```javascript
const email = $input.first().json;

// Extraer datos
const data = {
  from_name: email.from?.name || 'Sin nombre',
  from_email: email.from?.address || email.from?.email,
  subject: email.subject || '',
  date: new Date().toISOString(),
  body: email.body || '',
  matchesFilter: false
};

// Verificar si el asunto contiene "propuesta" o "cotizacion" (case insensitive)
const subjectLower = data.subject.toLowerCase();
if (subjectLower.includes('propuesta') || subjectLower.includes('cotizacion')) {
  data.matchesFilter = true;
}

return [{ json: data }];
```

### 3. **IF Node** - Decisión
- **Condition**: `matchesFilter` equals `true`
- **True**: Continuar al siguiente nodo
- **False**: Detener workflow (o conectar a un nodo "Stop")

### 4. **Notion Node** - Guardar en Base de Datos
- **Operation**: `Create a new page`
- **Database ID**: Selecciona tu base de datos de Notion
- **Properties** (configura según tu base de datos):
  - `Nombre` o `Title`: `={{ $json.from_name }}`
  - `Email`: `={{ $json.from_email }}`
  - `Asunto`: `={{ $json.subject }}`
  - `Fecha`: `={{ $json.date }}`
  - `Cuerpo del email`: `={{ $json.body }}`

### 5. **Slack Node** - Notificación
- **Operation**: `Send a message`
- **Channel**: `#tu-canal` (o ID del canal)
- **Message**:
```
📧 Nuevo email procesado:
👤 Remitente: {{ $json.from_name }}
📧 Email: {{ $json.from_email }}
📋 Asunto: {{ $json.subject }}
📅 Fecha: {{ $json.date }}
```

## Configuración de Conexiones

### Gmail
1. Ve a **Credentials** → **Add Credential** → **Gmail**
2. Sigue el flujo OAuth2

### Notion
1. Ve a **Credentials** → **Add Credential** → **Notion**
2. Crea un token en [notion.so/my-integrations](https://www.notion.so/my-integrations)
3. Comparte la base de datos con tu integración (click en "..." → "Connect to")

### Slack
1. Ve a **Credentials** → **Add Credential** → **Slack**
2. Crea una app en [api.slack.com/apps](https://api.slack.com/apps)
3. Instala en tu workspace y copia el OAuth Token

## Flujo del Workflow
```
[Gmail Trigger] → [Function: Extraer/Filtrar] → [IF: matchesFilter?]
                                              ↓
                                    [Notion: Guardar] → [Slack: Notificar]
                                              ↓
                                          [Stop]
```

## Mejoras Opcionales

1. **Evitar duplicados**: Agrega un campo único en Notion (ej: `email_id`) y verifica antes de crear
2. **Filtro más preciso**: Puedes usar regex en el Function node para coincidencias exactas
3. **Manejo de errores**: Agrega un nodo "Error Trigger" para capturar fallos

¿Necesitas ayuda con la configuración de algún nodo específico o las conexiones?