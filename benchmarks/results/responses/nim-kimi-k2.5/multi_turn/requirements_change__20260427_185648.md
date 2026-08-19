# Kimi K2.5 (NIM) — multi_turn/requirements_change

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 5.33 | quality: 3.52
- latency_total: 95.281s | tokens_per_second: 19.0
- input_tokens: 267 | output_tokens: 1815
- judge_score: 1.4 | justificación: 

## Respuesta completa

 Aquí tienes el workflow actualizado para **Gmail → Filtro → Notion → Slack**:

## Estructura del Workflow

```
[Gmail Trigger] → [Filter] → [Notion: Create DB Item] → [Slack: Send Message]
```

---

### 1. Gmail Trigger
- **Node**: `Gmail Trigger`
- **Trigger Event**: `Message Received`
- **Label**: `INBOX` (o la etiqueta que monitorees)
- **Simplified Input**: Sí (para obtener datos limpios)

### 2. Filter Node (la clave del filtro)
Configura el nodo **IF** o **Filter** (recomiendo Filter para N8N v1+):

- **Mode**: `Filter`
- **Conditions**:
  - `Subject` **contains** `propuesta`
  - **OR** `Subject` **contains** `cotizacion`
  - **OR** `Subject` **contains** `cotización` *(con tilde, por si acaso)*

**Tip**: Marca "Ignore Case" para que detecte mayúsculas/minúsculas.

### 3. Notion (Create Database Item)
**Pre-requisito**: Crea una base de datos en Notion con estas propiedades:
- `Nombre` (Title)
- `Email` (Email)
- `Asunto` (Rich Text)
- `Fecha` (Date)
- `Estado` (Select: "Nuevo", "Contactado")

**Configuración del nodo**:
- **Resource**: `Database Page`
- **Operation**: `Create`
- **Database**: *Selecciona tu database o pega el ID*
- **Properties** (mapeo):
  - **Nombre**: `{{ $json.from.value[0].name }}` (o parsea el from si viene como string)
  - **Email**: `{{ $json.from.value[0].address }}`
  - **Asunto**: `{{ $json.subject }}`
  - **Fecha**: `{{ $json.date }}`
  - **Estado**: `Nuevo`

> **Nota**: El campo `from` suele venir como array. Si ves que no funciona, usa primero un nodo `Set` para parsear: `{{ $json.from.match(/<(.*)>/)[1] }}` para el email.

### 4. Slack Notification
- **Channel**: `#oportunidades` (o tu canal)
- **Message**:
```
📧 *Nueva oportunidad detectada*

*De:* {{ $json.from.value[0].name }} <{{ $json.from.value[0].address }}>
*Asunto:* {{ $json.subject }}
*Fecha:* {{ $json.date }}

✅ Guardado en Notion: {{ $json.url }} (si disponible)
```

---

## Credenciales necesarias

1. **Gmail**: OAuth2 (necesitas activar Gmail API en Google Cloud Console)
2. **Notion**: 
   - Crea integración en [notion.so/my-integrations](https://notion.so/my-integrations)
   - Comparte tu database con la integración (botón "Share" → "Invite" → tu app)
   - Copia el Database ID (es la parte del URL: `https://notion.so/workspace/[AQUI-EL-ID]?v=...`)
3. **Slack**: OAuth2 con scope `chat:write` y `chat:write.public` (si es canal público)

---

## Mejora opcional (Regex)

Si quieres ser más preciso con el filtro, en lugar del Filter node usa un nodo **Code** (JavaScript):

```javascript
const subject = $input.first().json.subject.toLowerCase();
const keywords = ['propuesta', 'cotizacion', 'cotización', 'presupuesto'];

if (keywords.some(k => subject.includes(k))) {
  return [$input.first()];
}
return [];
```

¿Necesitas ayuda con algún paso específico de la configuración de credenciales?