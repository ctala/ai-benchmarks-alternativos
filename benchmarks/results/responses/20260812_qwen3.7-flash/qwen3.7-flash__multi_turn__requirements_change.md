# Qwen 3.7 Flash — multi_turn/requirements_change

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 5.04 | quality: 4.0
- latency_total: 22.762s | tokens_per_second: 107.9
- input_tokens: 233 | output_tokens: 2456

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

Excelente cambio. Integrar Gmail → Filtro → Notion → Slack es un flujo muy común para captación automática de oportunidades comerciales. Te detallo cómo estructurarlo en n8n paso a paso:

### 🧩 Estructura del Workflow
```
[Gmail Trigger] → [IF (filtro por asunto)] → [Función (limpieza)] → [Notion (crear item)] → [Slack (notificación)]
```

---

### ⚙️ Configuración Nodo a Nodo

#### 1. `Gmail` (Trigger / Polling)
- **Operation**: `Receive New Email` (o `Poll New Email`)
- **Folder**: `INBOX` (o `ALL_MAIL` si quieres revisar también archivados)
- **Polling Interval**: `5` o `10` minutos
- ✅ Guarda el JSON completo que devuelve (incluye `from`, `subject`, `date`, `snippet`, `id`, etc.)

#### 2. `IF` (Filtro inteligente)
- **Condition**: `Expression`
- **Expression**:
  ```js
  {{ $json.subject?.toLowerCase().includes('propuesta') || $json.subject?.toLowerCase().includes('cotización') }}
  ```
  💡 Esto ignora mayúsculas/minúsculas y evita fallos si el campo viene vacío.
- Conecta la rama `TRUE` al siguiente nodo. La `FALSE` puede ir a `No Operation` o cerrar el flujo.

#### 3. `Function` (Extracción y formateo)
Asegúrate de que esté conectado solo a la rama `TRUE`. Usa este código JS (adaptable según tu versión de n8n):
```javascript
const rawFrom = $json.from || {};
const nombre = rawFrom.name || rawFrom.displayName || 'Desconocido';
const email = rawFrom.email || '';
const asunto = $json.subject || '';
const fecha = new Date($json.date).toISOString();
const resumen = ($json.snippet || '').substring(0, 400);
const url = $json.id ? `https://mail.google.com/mail/u/0/#inbox/${$json.id}` : '';

return [{
  json: {
    remitente_nombre: nombre,
    remitente_email: email,
    asunto: asunto,
    fecha_creacion: fecha,
    resumen_mensaje: resumen,
    url_gmail: url
  }
}];
```

#### 4. `Notion` (Crear página en base de datos)
⚠️ **Prerrequisito**: Crea antes una Base de Datos en Notion con propiedades como:
- `Título`: Asunto
- `Texto`: Remitente Nombre, Resumen Mensaje
- `Email`: Remitente Email
- `Fecha`: Fecha Creación
- `URL` (opcional): URL Gmail

- **Operation**: `Create Item`
- **Database ID**: ID de tu base de datos (de la URL: `notion.so/tu-empresa/XXXXXXXXXXXXXXXXXXXXXX`)
- **Properties**: Mapea los campos del `Function` node a las propiedades de Notion.
- ✅ Activa `Set Content` si quieres guardar el cuerpo completo del email como Rich Text.

#### 5. `Slack` (Notificación)
- **Operation**: `Send Message`
- **Channel**: Tu canal de equipo o ventas
- **Text** (usa formato Markdown):
  ```markdown
  📩 *Nuevo correo filtrado*
  👤 *Remitente:* {{ $json.remitente_nombre }} (<{{ $json.remitente_email }}>)
  📌 *Asunto:* {{ $json.asunto }}
  🕒 *Recibido:* {{ $json.fecha_creacion }}
  🔍 *Vista rápida:* {{ $json.resumen_mensaje }}
  🔗 *Abrir en Gmail:* {{ $json.url_gmail }}
  ```
- ✅ Puedes añadir `Thread Timestamp` si quieres que todos los correos se agrupen en un hilo, pero para alertas nuevas suele ser mejor mensaje directo.

---

### 🔍 Tips Críticos para Producción
| Aspecto | Recomendación |
|--------|---------------|
| **Duplicados** | Gmail no garantiza orden cronológico perfecto. Añade un `Merge` o `Sort` por fecha si necesitas evitar procesos repetidos. |
| **Errores de Slack/Notion** | Agrega un nodo `Error Trigger` o usa `Wait` + `Webhook` para logging si algo falla. |
| **Cotización vs Cotizacion** | El filtro ya cubre `cotización` (con tilde). Si tus clientes usan sin tilde, añade `.includes('cotizacion')` a la expresión del IF. |
| **Privacidad** | En Notion, activa `Private Database` y comparte solo con miembros del workspace. No expongas emails en bases públicas. |

---

¿Quieres que te genere el **código JSON exportable** del workflow listo para importar en tu cuenta de n8n? Solo dime tu versión de n8n (cloud/self-hosted) y te lo entrego formateado. También puedo ayudarte a configurar los IDs de Notion o ajustar el mapeo de propiedades.