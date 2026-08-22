# GLM 5.3 — multi_turn/requirements_change

- model_id: `z-ai/glm-5.3`
- success: True  | final: 4.09 | quality: 4.0
- latency_total: 62.011s | tokens_per_second: 72.4
- input_tokens: 235 | output_tokens: 4489

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

Sin problema, actualizo la estructura. El workflow queda así:

**Gmail Trigger → IF (filtro) → Edit Fields → Notion → Slack**

### 1. Gmail Trigger
- Credential: tu cuenta de Gmail
- Trigger: **Message Received**
- Activa **Simplify** para tener una salida más limpia

### 2. IF node — filtro por asunto
Agrega dos condiciones y combínalas con **OR**:

- Condición 1: `{{ $json.subject.toLowerCase() }}` → contains → `propuesta`
- Condición 2: `{{ $json.subject.toLowerCase() }}` → contains → `cotizacion`

El `.toLowerCase()` evita que se te escape un email con "Propuesta" o "COTIZACIÓN" en mayúsculas.

### 3. Edit Fields (Set) — extraer datos del remitente
Primero ejecuta el trigger con un email de prueba y revisa el panel de output para confirmar los nombres exactos de los campos. En versiones recientes de N8N el `from` viene parseado así:

- **Nombre**: `{{ $json.from.value[0].name }}`
- **Email**: `{{ $json.from.value[0].address }}`
- **Asunto**: `{{ $json.subject }}`
- **Fecha**: `{{ $json.date }}`

Si tu `from` llega como texto plano (`"Juan Perez <juan@empresa.com>"`), usa regex:

- Email: `{{ $json.from.match(/<(.+)>/)[1] }}`
- Nombre: `{{ $json.from.replace(/\s*<.+>/, '') }}`

### 4. Notion — guardar los datos
**Importante**: la base de datos debe estar compartida con tu integración de Notion (menú `•••` de la base → Connections → tu integración). Si no, no aparecerá en el nodo.

Configuración:
- Resource: **Database Page**
- Operation: **Create**
- Database: selecciona tu base
- Mapea las propiedades:
  - Propiedad título → Asunto
  - Propiedad texto → Nombre
  - Propiedad texto → Email
  - Propiedad fecha → Fecha

### 5. Slack — notificación
- Operation: **Send Message**
- Credential: tu app de Slack necesita el scope `chat:write` y el bot agregado al canal
- Channel: tu canal (ej: `#ventas`)
- Text:

```
📬 Nueva propuesta recibida

*De:* {{ $('Edit Fields').item.json.nombre }} ({{ $('Edit Fields').item.json.email }})
*Asunto:* {{ $('Edit Fields').item.json.asunto }}
```

(Ajusta `$('Edit Fields')` si renombraste el nodo del paso 3.)

### Detalle de flujo
Conecta la salida **true** del IF al Edit Fields, y de ahí Notion → Slack en serie. Si prefieres que la notificación llegue aunque falle el guardado en Notion, conecta el Edit Fields a ambos nodos en paralelo (dos ramas separadas).

¿Ya tienes la base de Notion creada o quieres que te sugiera la estructura de propiedades? También puedo generarte el JSON del workflow completo para que lo importes directo en N8N.