# Kimi K2.7 Code — multi_turn/requirements_change

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 5.07 | quality: 5.2
- latency_total: 23.406s | tokens_per_second: 44.3
- input_tokens: 265 | output_tokens: 1037
- judge_score: 2.4 | justificación: 

## Respuesta completa

¡Perfecto! Ahora tienes un workflow más potente. Te lo armo con estos nodos:

## Workflow: Captura de leads desde Gmail → Notion + Slack

### 1. **Gmail Trigger**
- **Credential**: Conecta tu cuenta de Gmail.
- **Event**: `Message Received`
- **Options** (recomendado):
  - **Format**: `Resolved`
  - **Download Attachments**: `false` (a menos que los necesites)

---

### 2. **IF** (Filtro por asunto)
Configura la condición para que pase solo si el asunto contiene alguna de las palabras clave:

- **Mode**: `String`
- **Value 1**: `{{ $json.subject }}`
- **Operation**: `Contains`
- **Value 2**: `propuesta`

Luego haz clic en **"Add Condition"** con OR:
- **Value 1**: `{{ $json.subject }}`
- **Operation**: `Contains`
- **Value 2**: `cotizacion`

> 💡 **Tip**: Para evitar problemas con mayúsculas/minúsculas, puedes usar antes un nodo **Set** o **Code** para convertir el subject a minúsculas.

---

### 3. **Set** (Extraer datos del remitente)
Aquí normalizas los datos antes de enviarlos a Notion:

| Name | Value |
|------|-------|
| `nombre` | `{{ $json.from.name }}` |
| `email` | `{{ $json.from.address }}` |
| `asunto` | `{{ $json.subject }}` |
| `fecha` | `{{ $json.date }}` |
| `mensaje` | `{{ $json.text }}` |

---

### 4. **Notion** → *Create Database Item*
- **Credential**: Conecta tu integración de Notion.
- **Database**: Selecciona tu base de datos.
- **Properties** (mapea según tus columnas en Notion):

| Notion Property | Valor |
|-----------------|-------|
| `Nombre` | `{{ $json.nombre }}` |
| `Email` | `{{ $json.email }}` |
| `Asunto` | `{{ $json.asunto }}` |
| `Fecha` | `{{ $json.fecha }}` |
| `Mensaje` | `{{ $json.mensaje }}` |

Asegúrate de que los tipos de propiedad en Notion coincidan (texto, email, fecha, etc.).

---

### 5. **Slack** → *Send Message*
- **Credential**: Conecta tu Slack.
- **Channel**: el canal donde quieres recibir la alerta.
- **Text**:

```
📧 Nuevo lead por email

👤 Nombre: {{ $json.nombre }}
📩 Email: {{ $json.email }}
📝 Asunto: {{ $json.asunto }}
📅 Fecha: {{ $json.fecha }}

🔗 Ver en Notion
```

Si quieres, puedes agregar el enlace directo a la página de Notion creada usando la salida del nodo Notion.

---

## Flujo visual

```
[Gmail Trigger]
     ↓
[IF: asunto contiene "propuesta" o "cotizacion"]
     ↓ true
[Set: extraer datos]
     ↓
[Notion: Create Database Item]
     ↓
[Slack: Send Message]
```

---

## Recomendación extra
Si el Gmail trigger no te permite filtrar directamente por asunto, el nodo **IF** hace el trabajo. Pero también puedes crear una etiqueta o regla en Gmail que mueva esos correos a una carpeta específica, y luego usar el trigger sobre esa carpeta para ahorrar ejecuciones.

¿Te gustaría que te pase el JSON del workflow listo para importar, o prefieres configurarlo manualmente con estos pasos?