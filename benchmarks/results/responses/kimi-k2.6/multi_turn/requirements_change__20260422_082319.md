# Kimi K2.6 — multi_turn/requirements_change

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 5.15 | quality: 4.72
- latency_total: 112.594s | tokens_per_second: 17.3
- input_tokens: 266 | output_tokens: 1949
- judge_score: 2.0 | justificación: 

## Respuesta completa

 Aquí tienes el workflow actualizado. Te lo detallo paso a paso con las configuraciones exactas para N8N:

### Flujo general
```
[Gmail Trigger] → [Filter: Asunto] → [Set/Extract Datos] → [Notion: Create DB Item] → [Slack: Send Message]
```

---

### Paso 1: Gmail Trigger
- **Node**: `Gmail` → **On Message**
- **Credential**: Conecta tu cuenta de Gmail vía OAuth 2.
- **Options**:
  - **Simplify**: Sí (recomendado para que los datos vengan limpios).
  - **Format**: `Resolved` (para obtener el texto plano ya parseado).

---

### Paso 2: Filter (Filtro por asunto)
Usa el nodo **`Filter`** o un nodo **`IF`** (el Filter es más limpio para esto).

- **Mode**: `String`
- **Condition 1**:
  - **Value 1**: `{{ $json.subject }}`
  - **Operation**: `Contains`
  - **Value 2**: `propuesta`
- **Combine Conditions**: `OR`
- **Condition 2**:
  - **Value 1**: `{{ $json.subject }}`
  - **Operation**: `Contains`
  - **Value 2**: `cotizacion`

> **Tip**: Si quieres que sea insensible a mayúsculas/minúsculas, usa en su lugar el nodo **IF** con esta expresión en **Boolean**:
> ```
> {{ $json.subject.toLowerCase().includes('propuesta') || $json.subject.toLowerCase().includes('cotizacion') }}
> ```

---

### Paso 3: Extraer datos del remitente
El nodo anterior devuelve el remitente en un array. Usa un nodo **`Set`** (o **`Code`** si prefieres) para normalizar los campos antes de enviarlos a Notion.

**En el nodo `Set` (modo Manual):**
- **Name**: `Email`
  - **Value**: `{{ $json.from.value[0].address }}`
- **Name**: `Nombre`
  - **Value**: `{{ $json.from.value[0].name || $json.from.value[0].address }}`
- **Name**: `Asunto`
  - **Value**: `{{ $json.subject }}`
- **Name**: `Fecha`
  - **Value**: `{{ $json.date }}`

---

### Paso 4: Notion (Create Database Item)
- **Node**: `Notion` → **Create a Database Item**
- **Credential**: Tu integración de Notion (Internal Integration Token).
- **Database**: Selecciona el ID de tu base de datos.

**Mapeo de propiedades** (ajusta según los tipos de columna de tu DB):

| Propiedad Notion | Tipo en Notion | Valor en N8N |
|---|---|---|
| `Nombre` o `Título` | Title | `{{ $json.Asunto }}` |
| `Email` | Email | `{{ $json.Email }}` |
| `Remitente` | Rich Text | `{{ $json.Nombre }}` |
| `Fecha de llegada` | Date | `{{ $json.Fecha }}` |

> **Importante**: La base de datos en Notion debe estar **compartida** con tu integración (bot) de Notion. Ve a `...` → `Add connections` → selecciona tu integración.

---

### Paso 5: Slack (Notificación)
- **Node**: `Slack` → **Send a Message**
- **Credential**: App de Slack conectada o Webhook URL.
- **Channel**: `#tus-leads` (o tu canal/objetivo).
- **Text**:
  ```
  📩 Nuevo email de *{{ $json.Nombre }}* ({{ $json.Email }})
  > Asunto: {{ $json.Asunto }}
  > Guardado en Notion ✅
  ```

---

### Configuraciones extra recomendadas

1. **Manejo de errores**: Agrega un nodo **`NoOp`** o **`Slack`** en la rama `false` del IF/Filter si quieres notificar otros casos, o simplemente deja que termine el flujo.
2. **Evitar duplicados**: El trigger de Gmail a veces puede ejecutarse múltiples veces por el mismo correo si usas polling. Asegúrate de que el intervalo de polling sea razonable (ej. 1 minuto) y considera usar una columna en Notion (tipo Unique ID) con el `Message ID` del email.
3. **Fechas**: Si Notion rechaza el formato de fecha de Gmail, usa la expresión:
   ```
   {{ new Date($json.Fecha).toISOString() }}
   ```

---

### Checklist de credenciales necesarias
Antes de activar el workflow:
- [ ] **Gmail API** activada en Google Cloud Console + OAuth consent screen configurado.
- [ ] **Notion Integration** creada en [notion.so/my-integrations](https://notion.so/my-integrations) y base de datos compartida.
- [ ] **Slack App** con permiso `chat:write` o Webhook URL configurada.

¿Necesitas que te ayude con alguna expresión específica o con la configuración del OAuth de Gmail?