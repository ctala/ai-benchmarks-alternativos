# Qwen 3.8 Flash — multi_turn/requirements_change

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 6.01 | quality: 6.0
- latency_total: 33.498s | tokens_per_second: 87.0
- input_tokens: 275 | output_tokens: 2915

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

Perfecto, vamos a reestructurarlo entonces. El flujo quedaría así:

## Estructura del workflow

```
Gmail Trigger
      ↓
Filtro por asunto: propuesta / cotización
      ↓
Extraer datos del remitente
      ↓
Guardar en Notion
      ↓
Notificar en Slack
```

---

## 1. Gmail Trigger

En el nodo **Gmail Trigger**, configura:

- **Trigger**: `On Email Received`
- **Poll Interval**: por ejemplo, 1 minuto
- **Query**: puedes dejar vacío o poner algo como:

```text
is:unread
```

> Aunque Gmail permite filtrar por asunto con `subject:propuesta`, no siempre es confiable con acentos o mayúsculas. Lo más seguro es filtrar después dentro de n8n.

---

## 2. Filtro por asunto

Agrega un nodo **IF** o **Filter**.

### Opción recomendada: nodo Code

Inserta un nodo **Code** antes del IF para normalizar el asunto:

```javascript
const subject = (item.json.subject || '').toLowerCase();

const hasKeyword =
  subject.includes('propuesta') ||
  subject.includes('cotizacion') ||
  subject.includes('cotización');

return [{
  json: {
    ...item.json,
    hasKeyword
  }
}];
```

Luego, en el nodo **IF**, pon:

```text
{{ $json.hasKeyword }}
```

Es igual a:

```text
true
```

Solo continúa el flujo si el asunto contiene alguna de esas palabras.

> Importante: incluí `cotización` con tilde porque muchos emails reales sí la usan.

---

## 3. Extraer datos del remitente

El Gmail Trigger suele devolver el campo `from` con este formato:

```text
Juan Pérez <juan@empresa.com>
```

Necesitas separar nombre y correo.

Agrega un nodo **Set** o **Code**.

### Con nodo Code:

```javascript
const rawFrom = item.json.from || '';

let name = '';
let email = '';

const match = rawFrom.match(/^(.*?)<(.+?)>$/);

if (match) {
  name = match[1].trim();
  email = match[2].trim();
} else {
  email = rawFrom.trim();
  name = rawFrom.trim();
}

return [{
  json: {
    senderName: name,
    senderEmail: email,
    subject: item.json.subject,
    receivedAt: item.json.date || new Date().toISOString(),
    messageId: item.json.messageId || null,
    threadId: item.json.threadId || null
  }
}];
```

Ahora tendrás datos limpios:

- `senderName`
- `senderEmail`
- `subject`
- `receivedAt`
- `messageId`
- `threadId`

---

## 4. Guardar en Notion

Agrega un nodo **Notion**.

Configuración:

- **Resource**: `Database Page`
- **Operation**: `Create`
- **Database ID**: el ID de tu base de datos de Notion

### Base de datos sugerida en Notion

Crea una base de datos con estas propiedades:

| Campo Notion | Tipo | Valor desde n8n |
|---|---|---|
| Nombre | Title | `senderName` |
| Email | Email | `senderEmail` |
| Asunto | Text | `subject` |
| Fecha | Date | `receivedAt` |
| Estado | Select | `Nuevo` |
| Tipo | Select | `Propuesta` o `Cotización` |
| Message ID | Text | `messageId` |

### Ejemplo de mapeo en el nodo Notion

**Page Title**:

```text
{{ $json.senderName }} - {{ $json.subject }}
```

O si quieres que el título sea solo el nombre:

```text
{{ $json.senderName }}
```

**Email**:

```text
{{ $json.senderEmail }}
```

**Asunto**:

```text
{{ $json.subject }}
```

**Fecha**:

```text
{{ $json.receivedAt }}
```

---

## 5. Notificar en Slack

Agrega un nodo **Slack** después de Notion.

Configuración:

- **Resource**: `Channel`
- **Operation**: `Send Message`
- **Channel**: tu canal, por ejemplo `#ventas` o `#leads`

Mensaje sugerido:

```text
📩 Nueva propuesta/cotización recibida

👤 Remitente: {{ $json.senderName }}
✉️ Email: {{ $json.senderEmail }}
📌 Asunto: {{ $json.subject }}
📅 Recibido: {{ $json.receivedAt }}
🗂️ Guardado en Notion ✅
```

---

## Orden final de nodos

```
Gmail Trigger
      ↓
Code: normalizar asunto
      ↓
IF: hasKeyword = true
      ↓
Code: extraer nombre y email del remitente
      ↓
Notion: Create Database Page
      ↓
Slack: Send Message
```

---

## Recomendaciones importantes

### 1. Evitar duplicados

Puedes usar `messageId` de Gmail como identificador único.

En Notion, crea una propiedad:

```text
Message ID
```

Y antes de guardar, podrías hacer una búsqueda en Notion para verificar si ya existe ese `messageId`.

Si quieres, te agrego ese paso.

---

### 2. Detectar si es propuesta o cotización

En el nodo Code de extracción, puedes añadir:

```javascript
const subject = (item.json.subject || '').toLowerCase();

let tipo = 'Otro';

if (subject.includes('propuesta')) {
  tipo = 'Propuesta';
} else if (subject.includes('cotizacion') || subject.includes('cotización')) {
  tipo = 'Cotización';
}

return [{
  json: {
    ...item.json,
    tipo
  }
}];
```

Y luego guardar `{{ $json.tipo }}` en Notion.

---

### 3. Permisos de Gmail

Asegúrate de que la credencial de Gmail en n8n tenga permiso para:

- Leer emails
- Ver metadatos
- Buscar emails

Normalmente con OAuth2 de Gmail basta.

---

### 4. Notion

Necesitas:

1. Una base de datos en Notion.
2. Compartir esa base de datos con tu integración de Notion.
3. Pegar el `Database ID` en n8n.

El `Database ID` es la parte de la URL:

```text
https://www.notion.so/workspace/1234567890abcdef1234567890abcdef
```

Ese código final es el ID de la base de datos.

---

### 5. Slack

Necesitas una app de Slack con permisos para:

- Enviar mensajes a canales
- Leer canales, si quieres identificar el canal por nombre

En n8n, crea credenciales de Slack y conecta el nodo.

---

## Versión final mejorada del flujo

Yo lo dejaría así:

```
Gmail Trigger
      ↓
Code: normalizar asunto y detectar tipo
      ↓
IF: contiene propuesta o cotización
      ↓
Code: extraer nombre, email, fecha, tipo
      ↓
Notion: buscar duplicado por Message ID
      ↓
IF: no existe
      ↓
Notion: crear página
      ↓
Slack: notificar
```

---

## Próximo paso

Para dejarlo listo para importar, necesito que me confirmes:

1. ¿Qué campos exactos quieres guardar en Notion?
2. ¿Cuál es el nombre de la base de datos en Notion?
3. ¿A qué canal de Slack quieres que llegue la notificación?
4. ¿Quieres evitar duplicados usando el `messageId` de Gmail?
5. ¿Quieres que el título en Notion sea el nombre del remitente o el asunto del email?