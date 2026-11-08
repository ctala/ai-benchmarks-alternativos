# GPT-OSS 20B — multi_turn/requirements_change

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 5.05 | quality: 4.0
- latency_total: 15.326s | tokens_per_second: 141.9
- input_tokens: 277 | output_tokens: 2175

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

**Workflow completo en N8N**  
*(Gmail → Filtro → Notion + Slack)*

> **Requisitos previos**  
> 1. **Credenciales**  
>    - Gmail (OAuth2)  
>    - Notion (API key + ID de la base de datos)  
>    - Slack (Webhook URL o Slack App con permisos “chat:write”)  
> 2. En Notion crea una base de datos (p.ej. *Emails de Clientes*) con las siguientes columnas:  
>    - `Nombre Remitente` (Tipo: Texto)  
>    - `Email Remitente` (Tipo: Email)  
>    - `Asunto` (Tipo: Texto)  
>    - `Fecha de recepción` (Tipo: Fecha)

---

## 1. Trigger – Gmail

| Propiedad | Valor |
|-----------|-------|
| **Trigger** | Gmail |
| **Trigger type** | New Email |
| **Search query** | `subject:propuesta OR subject:cotizacion` **(opcional, si quieres filtrar en el trigger mismo)** |
| **Max results** | 1 (para procesar cada email una sola vez) |
| **Fields to return** | `from`, `subject`, `date`, `snippet`, `id` |

> *Si decides usar un filtro posterior, deja el query vacío y utiliza un nodo IF.*

---

## 2. (Opcional) Nodo IF – Filtro de asunto

> Sólo se necesita si no usaste el *Search query* en el trigger.

| Propiedad | Valor |
|-----------|-------|
| **Operation** | Logic |
| **Mode** | IF |
| **Conditions** |  
> 1. `{{ $json.subject.includes('propuesta') || $json.subject.includes('cotizacion') }}` |  
> 2. **If true** → Continúa al siguiente nodo.  
> 3. **If false** → No hace nada (puedes conectarlo a un nodo “No Op” o “Terminate”).

---

## 3. Nodo Function – Parsear remitente

> Convierte el campo `from` (ej. `"Juan Pérez <juan@example.com>"`) en nombre y email separados.

```javascript
// Entrada: $json = objeto de Gmail
const fromRaw = $json.from;            // "Juan Pérez <juan@example.com>"
const regex = /(.*) <(.*)>/;           // captura “nombre” y “email”

let nombre = '';
let email = '';

const match = fromRaw.match(regex);
if (match) {
  nombre = match[1].trim();
  email = match[2].trim();
} else {
  nombre = fromRaw;
  email = '';
}

// Devolvemos los campos que necesitaremos más adelante
return {
  nombreRemitente: nombre,
  emailRemitente: email,
  asunto: $json.subject,
  fechaRecepcion: $json.date,
  snippet: $json.snippet
};
```

**Configuración del nodo**  
- **Output**: 1 (default)  
- **JSON output**: ✔️ (dejar como está)

---

## 4. Nodo Notion – Añadir página a la BD

| Propiedad | Valor |
|-----------|-------|
| **Operation** | Create |
| **Database ID** | *ID de tu base de datos de Notion* |
| **Properties** |  
> - `Nombre Remitente` → `{{$node["Function"].json.nombreRemitente}}`  
> - `Email Remitente` → `{{$node["Function"].json.emailRemitente}}`  
> - `Asunto` → `{{$node["Function"].json.asunto}}`  
> - `Fecha de recepción` → `{{$node["Function"].json.fechaRecepcion}}`  
> - `Snippet` (si quieres guardar un extracto) → `{{$node["Function"].json.snippet}}` |

> **Tip**: En el campo de la fecha, elige *Date* y pasa la cadena con formato ISO (`2024-06-01T12:34:56.000Z`). N8N lo convierte automáticamente.

---

## 5. Nodo Slack – Enviar notificación

| Propiedad | Valor |
|-----------|-------|
| **Operation** | Send Message |
| **Channel** | #tu-canal (o el ID del canal) |
| **Message** |  

```
📧 Se recibió un nuevo email:

• **Remitente**: {{$node["Function"].json.nombreRemitente}} <{{$node["Function"].json.emailRemitente}}>
• **Asunto**: {{$node["Function"].json.asunto}}
• **Fecha**: {{$node["Function"].json.fechaRecepcion}}

> Snippet: {{$node["Function"].json.snippet}}
```

> Si usas un **Webhook**: pega la URL en el campo correspondiente.  
> Si usas una **Slack App**: asegúrate de haber configurado los scopes `chat:write` y `channels:read`.

---

## 6. (Opcional) Nodo Error Handling

Conecta un **Set** o **Email** node al **Error Trigger** (o al nodo *No Op*) para avisar en caso de fallo en Notion o Slack.

---

## 7. Resumen del flujo

```
Gmail Trigger
  │
  ├─> (IF) Filtro de asunto   [solo si no filtraste en el trigger]
  │
  └─> Function → Parsear remitente
         │
         ├─> Notion → Añadir página
         └─> Slack → Enviar notificación
```

---

## 8. Consejos finales

1. **Prueba**: Envía un email con “propuesta” o “cotizacion” en el asunto y verifica que aparezca en Notion y en Slack.  
2. **Logs**: Habilita “Show Binary Data” y “Show HTTP Response” en los nodos de Notion/Slack para depurar.  
3. **Tasa de ejecuciones**: Gmail API tiene límites de 1000/mes por cuenta; si recibes muchos emails, considera usar un *Webhook* o dividir el flujo.  
4. **Seguridad**: Guarda las credenciales en variables de entorno o en el panel de credenciales de N8N, no en el flujo.  

¡Listo! Con este workflow tu Gmail se convierte en una fuente automática de datos en Notion y te avisa en Slack cada vez que un email con “propuesta” o “cotización” llegue. Si necesitas adaptar el formato de los campos o añadir más información (e.g., adjuntos), házmelo saber y lo ampliamos.