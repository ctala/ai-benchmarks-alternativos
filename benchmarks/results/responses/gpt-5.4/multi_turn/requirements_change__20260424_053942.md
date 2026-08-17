# GPT-5.4 — multi_turn/requirements_change

- model_id: `gpt-5.4`
- success: True  | final: 6.25 | quality: 5.56
- latency_total: 16.153s | tokens_per_second: 85.1
- input_tokens: 226 | output_tokens: 1374
- judge_score: 2.6 | justificación: 

## Respuesta completa

Sí. Te propongo este flujo en n8n:

## Objetivo
- Leer emails nuevos de Gmail
- Filtrar solo los que en el asunto contengan **“propuesta”** o **“cotizacion”**
- Extraer datos del remitente
- Guardarlos en **Notion**
- Enviar notificación a **Slack**

---

## Estructura del workflow

1. **Gmail Trigger**
2. **IF** o **Filter**
3. **Set** / **Function**
4. **Notion**
5. **Slack**

---

## 1) Gmail Trigger

Usa un nodo **Gmail Trigger**.

### Configuración recomendada
- **Resource**: Message
- **Operation**: Watch / New Email
- Credenciales de Gmail conectadas
- Si quieres, puedes limitar por etiqueta o inbox principal

Este nodo traerá datos como:
- `From`
- `Subject`
- `Date`
- `Snippet`
- `Message Id`

---

## 2) Filtrar por asunto

Tienes dos formas: con **IF node** o con **Code/Function node**.  
La más simple es **IF**.

### Opción con IF
Condición basada en el campo del asunto.

Ejemplo de expresión:
```javascript
{{ 
  $json.subject && (
    $json.subject.toLowerCase().includes('propuesta') ||
    $json.subject.toLowerCase().includes('cotizacion')
  )
}}
```

### Resultado
- **True** → sigue el flujo
- **False** → termina

> Si quieres contemplar “cotización” con tilde, conviene añadirlo también.

Ejemplo mejorado:
```javascript
{{ 
  $json.subject && (
    $json.subject.toLowerCase().includes('propuesta') ||
    $json.subject.toLowerCase().includes('cotizacion') ||
    $json.subject.toLowerCase().includes('cotización')
  )
}}
```

---

## 3) Extraer datos del remitente

Puedes usar un nodo **Set** para mapear solo lo que necesitas.

### Campos sugeridos
- `subject`
- `from`
- `email`
- `name`
- `date`
- `snippet`

Si Gmail devuelve el remitente en formato:
```text
Juan Pérez <juan@empresa.com>
```

puedes separar nombre y email con un **Code node**.

### Ejemplo de Code node
```javascript
const from = $json.from || '';
const match = from.match(/^(.*)<(.+)>$/);

let name = '';
let email = from;

if (match) {
  name = match[1].trim().replace(/"/g, '');
  email = match[2].trim();
}

return [
  {
    json: {
      subject: $json.subject || '',
      from,
      name,
      email,
      date: $json.date || '',
      snippet: $json.snippet || '',
      messageId: $json.id || ''
    }
  }
];
```

---

## 4) Guardar en Notion

Usa un nodo **Notion** con operación **Create Page** en una base de datos.

### Antes de eso
En Notion crea una database con propiedades como:

- **Nombre** → Title
- **Email** → Email o Text
- **Asunto** → Text
- **Fecha Email** → Date
- **Remitente Raw** → Text
- **Snippet** → Text
- **Message ID** → Text
- **Estado** → Select (opcional)

### Configuración del nodo Notion
- **Resource**: Database Page
- **Operation**: Create
- **Database ID**: selecciona tu base

### Mapeo sugerido
- **Nombre** → `{{ $json.name || $json.email }}`
- **Email** → `{{ $json.email }}`
- **Asunto** → `{{ $json.subject }}`
- **Fecha Email** → `{{ $json.date }}`
- **Remitente Raw** → `{{ $json.from }}`
- **Snippet** → `{{ $json.snippet }}`
- **Message ID** → `{{ $json.messageId }}`

> Si la fecha da problemas de formato, puedes transformarla antes con un nodo Date & Time.

---

## 5) Notificación a Slack

Añade un nodo **Slack** después de Notion.

### Operación
- **Resource**: Message
- **Operation**: Post Message

### Canal
Ejemplo:
- `#leads`
- o un canal privado si el bot está agregado

### Mensaje sugerido
```text
📩 Nuevo email detectado

*Asunto:* {{$json.subject}}
*Nombre:* {{$json.name}}
*Email:* {{$json.email}}
*Fecha:* {{$json.date}}

Guardado en Notion correctamente.
```

Si quieres incluir enlace al registro de Notion, se puede hacer usando la salida del nodo Notion.

---

# Flujo visual

```text
Gmail Trigger
   ↓
IF (subject contiene propuesta/cotizacion)
   ↓ true
Code (extraer name/email)
   ↓
Notion (Create Page)
   ↓
Slack (Post Message)
```

---

# Recomendación importante
Para evitar duplicados, puedes guardar el **Message ID** en Notion y antes de crear la página hacer una búsqueda en Notion:
1. Buscar si ya existe ese `Message ID`
2. Si no existe → crear página
3. Si existe → no hacer nada

Eso haría el flujo más robusto.

---

# Variante de filtro más robusta

Si quieres detectar mayúsculas, tildes y variaciones, usa un **Code node** antes del IF:

```javascript
const subject = ($json.subject || '').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');

const match = subject.includes('propuesta') || subject.includes('cotizacion');

return [{ json: { ...$json, subjectNormalized: subject, match } }];
```

Luego en el **IF**:
```javascript
{{ $json.match === true }}
```

---

# Te puedo dejar también el workflow casi listo para importar

Si quieres, en el siguiente mensaje te paso una de estas dos opciones:

1. **Versión paso a paso** con la configuración exacta de cada nodo en n8n  
2. **JSON importable de n8n** para que lo pegues y solo cambies tus credenciales

Si quieres avanzar rápido, te recomiendo la opción 2.