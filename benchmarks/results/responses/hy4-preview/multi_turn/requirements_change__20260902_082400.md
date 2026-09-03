# Tencent Hy4 preview — multi_turn/requirements_change

- model_id: `tencent/hy4-preview`
- success: True  | final: 5.44 | quality: 6.0
- latency_total: 177.749s | tokens_per_second: 58.4
- input_tokens: 267 | output_tokens: 10383

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

¡Entendido! Actualizamos el diseño. La estructura del workflow en N8N quedaría así:

**Gmail Trigger → Filter / IF (filtro por asunto) → Edit Fields / Set (limpiar datos) → Slack + Notion**

Te detallo cada nodo:

---

## 1. Gmail Trigger
- **Credenciales:** Gmail OAuth2 (necesitas crear credenciales en Google Cloud y conectar tu cuenta).
- **Trigger On:** `Message Received` (se activa cuando entra un email nuevo).
- **Label:** opcional, puedes poner `INBOX` para solo leer la bandeja de entrada.
- **Options:** activa **Simplify** (o *Simplify Output*) para que los datos lleguen limpios: `subject`, `from`, `date`, `text`, etc.

---

## 2. Filter (o IF) — Filtrar por asunto
Queremos que solo continúen los emails cuyo asunto contenga **“propuesta”** o **“cotizacion”** (sin importar mayúsculas/minúsculas).

### Opción recomendada: Regex
Usa un nodo **Filter** (o **IF**) con esta condición:

- **Value 1:** `{{ $json.subject }}`
- **Operation:** `Matches Regex` (o `Regex`)
- **Value 2:** `/propuesta|cotizacion/i`

> La `i` al final hace que no distinga mayúsculas de minúsculas.

### Alternativa sin Regex (dos condiciones OR)
Si prefieres evitar expresiones regulares:
- **Combinator:** `OR`
- Condición 1: `{{ $json.subject.toLowerCase() }}` → `Contains` → `propuesta`
- Condición 2: `{{ $json.subject.toLowerCase() }}` → `Contains` → `cotizacion`

Si usas un nodo **IF**, conecta la salida **`true`** al siguiente nodo. Si usas **Filter**, todo lo que pase sigue automáticamente.

---

## 3. Edit Fields (Set) — Dejar los datos limpios
Este nodo sirve para no repetir expresiones complejas. Crea estos campos:

| Campo | Expresión |
|------|-----------|
| `nombre_remitente` | `{{ $json.from.value[0].name \|\| $json.from.value[0].address }}` |
| `email_remitente` | `{{ $json.from.value[0].address }}` |
| `asunto` | `{{ $json.subject }}` |
| `fecha` | `{{ $json.date }}` |
| `cuerpo` | `{{ $json.text \|\| $json.snippet }}` |

> **Nota:** dependiendo de la versión de n8n, el remitente puede venir como `{{ $json.from.text }}` (ej: `"Juan Perez <juan@email.com>"`). Si `from.value[0]` te da error, revisa el output del Gmail Trigger y usa la ruta que corresponda.

---

## 4. Slack — Notificación
- **Credenciales:** Slack API (crea una Slack App, dale el scope `chat:write` e invita al bot al canal donde quieres recibir el aviso).
- **Resource:** `Message`
- **Operation:** `Post`
- **Channel:** por ejemplo `#propuestas` o `#cotizaciones`
- **Text (mensaje):**
```text
:email: *Nueva propuesta o cotización recibida*

*De:* {{ $json.nombre_remitente }} (<{{ $json.email_remitente }}>)
*Asunto:* {{ $json.asunto }}
*Fecha:* {{ $json.fecha }}

*Resumen:*
{{ $json.cuerpo }}
```

---

## 5. Notion — Guardar el registro
Primero, en Notion crea una **base de datos** con estas propiedades (puedes usar otros nombres, pero luego debes mapearlos igual):

- `Nombre` → tipo **Title**
- `Email` → tipo **Email**
- `Asunto` → tipo **Text**
- `Fecha` → tipo **Date**
- `Mensaje` → tipo **Text**

Luego en n8n:

- **Credenciales:** Notion API (crea una *internal integration* en https://www.notion.so/my-integrations y **comparte la base de datos con esa integración**).
- **Resource:** `Database Page`
- **Operation:** `Create`
- **Database:** selecciona tu base de datos (si no aparece, asegúrate de haberla compartido con la integración).
- Mapea los campos:
  - **Nombre:** `{{ $json.nombre_remitente }}`
  - **Email:** `{{ $json.email_remitente }}`
  - **Asunto:** `{{ $json.asunto }}`
  - **Fecha:** `{{ $json.fecha }}`  
    *(si Notion rechaza el formato de fecha, cambia esto a `{{ new Date($json.fecha).toISOString() }}`)*
  - **Mensaje:** `{{ $json.cuerpo }}`

---

## Conexiones finales
1. **Gmail Trigger** → **Filter / IF**
2. **Filter / IF** (salida `true`) → **Edit Fields (Set)**
3. Desde **Edit Fields**, saca **dos conexiones**:
   - una hacia **Slack**
   - otra hacia **Notion**

Así, cuando llegue un email con “propuesta” o “cotizacion” en el asunto:
- Se filtra
- Se limpian los datos
- Se manda el aviso a Slack
- Se crea la página/registro en Notion

---

## Tip final
Antes de dejarlo corriendo, haz una prueba enviándote un email real y usa el botón **“Execute Node”** en el Gmail Trigger para ver exactamente cómo llegan `from` y `date` en tu caso.

Si quieres, dime y te preparo el **JSON listo para importar** en n8n (con los nombres de ejemplo que usamos arriba), para que solo tengas que cambiar tus credenciales, el canal de Slack y el ID de la base de Notion.