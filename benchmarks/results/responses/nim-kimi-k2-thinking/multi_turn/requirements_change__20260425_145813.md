# Kimi K2 Thinking (NIM) — multi_turn/requirements_change

- model_id: `moonshotai/kimi-k2-thinking`
- success: True  | final: 5.92 | quality: 5.2
- latency_total: 44.638s | tokens_per_second: 28.0
- input_tokens: 266 | output_tokens: 1251
- judge_score: 2.6 | justificación: 

## Respuesta completa

 Perfecto, aquí tienes el workflow actualizado con los filtros y Notion. Te explico cada nodo:

## **Workflow: Email Filtrado → Notion → Slack**

### **Nodo 1: Gmail Trigger**
- **Tipo**: Gmail → "On message received"
- **Configuración**:
  - **Poll Times**: Cada 5 minutos (o tu frecuencia preferida)
  - **Options**: Marcar "Mark as Read" si no quieres procesar el mismo email 2 veces

### **Nodo 2: IF (Filtro de Asunto)**
- **Condición**: `{{$json["subject"]}}` contiene "propuesta" OR "cotizacion"
- **Configuración**:
  - **Value 1**: `{{$json["subject"]}}`
  - **Operation**: Contains
  - **Value 2**: `propuesta`
  - **Add Condition**: OR
  - **Value 1**: `{{$json["subject"]}}`
  - **Operation**: Contains
  - **Value 2**: `cotizacion`

### **Nodo 3: Notion (Create Page)**
- **Conectar al output "true" del nodo IF**
- **Configuración**:
  - **Database**: Selecciona tu base de datos en Notion
  - **Page Properties**:
    - **Nombre** (title): `{{$json["from"]["name"]}} - {{$json["subject"]}}`
    - **Email** (email): `{{$json["from"]["email"]}}`
    - **Asunto** (text): `{{$json["subject"]}}`
    - **Fecha** (date): `{{$json["date"]}}`
    - **Mensaje** (text): `{{$json["text"]}}` (opcional, solo preview)

### **Nodo 4: Slack (Post Message)**
- **Conectar después del nodo Notion**
- **Configuración**:
  - **Channel**: ID del canal o nombre (#oportunidades)
  - **Text**: 
  ```
  :email: Nueva oportunidad recibida:
  *De:* {{$json["from"]["name"]}} ({{$json["from"]["email"]}})
  *Asunto:* {{$json["subject"]}}
  [Ver en Notion]({{$json["notionUrl"]}})
  ```

---

## **Campos Clave del Email (Gmail Trigger Output)**
- `{{$json["from"]["name"]}}` → Nombre del remitente
- `{{$json["from"]["email"]}}` → Email del remitente
- `{{$json["subject"]}}` → Asunto
- `{{$json["date"]}}` → Fecha
- `{{$json["text"]}}` → Cuerpo del mensaje

---

## **Configuración Previa Necesaria**

### **Notion**
1. Crea una **Database** en Notion con estas propiedades:
   - `Nombre` (Title)
   - `Email` (Email)
   - `Asunto` (Text)
   - `Fecha` (Date)
   - `Mensaje` (Text)

2. Comparte la base de datos con la integración de N8N:
   - En Notion, ve a Settings → Connections → N8N
   - O usa el token de integración interna

### **Slack**
1. Crea un Slack App en [api.slack.com](https://api.slack.com)
2. Dale permisos `chat:write` y `chat:write.public`
3. Instala la app en tu workspace
4. Copia el Bot Token (empieza con `xoxb-`)

### **Gmail**
1. Activa la API de Gmail en Google Cloud Console
2. Crea credenciales OAuth 2.0
3. En N8N, conecta usando OAuth2 y escope `https://www.googleapis.com/auth/gmail.readonly`

---

## **Tip de Optimización**
Si recibes muchos emails, considera usar **Gmail Labels**. Configura el trigger para que solo monitoree emails con la label "Procesar" que puedes aplicar con un filtro en Gmail.

¿Necesitas ayuda con algún nodo específico o la configuración de autenticación?