# Claude Haiku 4.5 (suscripción) — multi_turn/requirements_change

- model_id: `claude-haiku-4-5`
- success: True  | final: 6.95 | quality: 7.44
- latency_total: 10.844s | tokens_per_second: 110.0
- input_tokens: 10 | output_tokens: 1193
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, proporcionando un flujo de trabajo detallado que aborda la tarea original con mejoras significativas. Ofrece profundidad al incluir pasos adicionales como Notion y Slack, y está claramente organizada y fácil de entender. La utilidad práctica es alta, aunque el contexto de los requisitos cambiantes no se aborda completamente.

## Respuesta completa

Perfecto, ese workflow es más robusto. Aquí está el flujo completo:

## Estructura del Workflow N8N

```
Gmail Trigger 
    ↓
[Filter] - Buscar "propuesta" O "cotización" en Subject
    ↓
[Function] - Extraer datos del remitente
    ↓
[Split en paralelo]
    ├→ Notion - Guardar registro
    └→ Slack - Enviar notificación
```

## Configuración paso a paso:

### 1. **Gmail Trigger** (ya tienes esto)
- Autenticar con tu cuenta Gmail
- Se dispara con cada email nuevo

### 2. **Filter node** - Filtrar por palabras clave
```javascript
// En el panel "Conditions":
// Tipo: String contains (case insensitive)
// Campo: email_subject
// Condición: contains "propuesta" 
// Operador lógico: OR
// Segunda condición: contains "cotización"
```

O si prefieres regex en un Function node:
```javascript
const subject = $input.first().json.subject || '';
return subject.toLowerCase().match(/(propuesta|cotización)/);
```

### 3. **Function node** - Extraer datos del remitente
```javascript
const email = $input.first().json;

return {
  remitente_nombre: email.from.name || email.from.email.split('@')[0],
  remitente_email: email.from.email,
  asunto: email.subject,
  fecha: email.receivedDate,
  preview: email.bodyText ? email.bodyText.substring(0, 200) : email.bodySnippet,
  gmail_link: `https://mail.google.com/mail/u/0/#inbox/${email.id}`
};
```

### 4. **Notion node** - Guardar en base de datos
**Configuración:**
- **Database**: Selecciona tu base de Notion (necesitas conectar primero con OAuth)
- **Properties a mapear:**
  - `Remitente` (text) → `remitente_nombre`
  - `Email` (email) → `remitente_email`
  - `Asunto` (text) → `asunto`
  - `Fecha` (date) → `fecha`
  - `Vista previa` (text) → `preview`
  - `Link` (url) → `gmail_link`

### 5. **Slack node** - Notificación
**Configuración:**
- **Channel**: `#notificaciones` (o donde prefieras)
- **Message format**:
```
📧 Nuevo email con propuesta/cotización

👤 De: {{$node["Function"].json.remitente_nombre}}
📧 Email: {{$node["Function"].json.remitente_email}}
📌 Asunto: {{$node["Function"].json.asunto}}
🔗 Ver en Gmail: {{$node["Function"].json.gmail_link}}
```

## Tips importantes:

✅ **Usa "Continue on error"** en el Notion node — si falla la BD, el Slack se ejecuta igual  
✅ **Test el workflow** con un email de prueba antes de activarlo  
✅ **Revisa los IDs de propiedades en Notion** — a veces cambian si la BD fue reorganizada  
✅ **Rate limiting**: Gmail puede ser lento — agrega un delay de 2s si tienes muchos emails  

¿Quieres que te ayude a:
- Debuguear la conexión con Notion?
- Agregar un campo de "Estado" en Notion para marcar como "Procesado"?
- Crear un segundo workflow que actualice el estado cuando respondas en Slack?