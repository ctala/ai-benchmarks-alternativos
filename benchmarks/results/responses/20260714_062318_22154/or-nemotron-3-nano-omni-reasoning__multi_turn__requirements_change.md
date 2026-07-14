# Nemotron 3 Nano Omni 30B-A3B Reasoning — multi_turn/requirements_change

- model_id: `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`
- success: True  | final: 5.12 | quality: 4.0
- latency_total: 15.439s | tokens_per_second: 193.2
- input_tokens: 248 | output_tokens: 2983
- judge_score: 3.8 | justificación: 

## Respuesta completa

¡Entendido! Vamos a crear un workflow en **n8n** que cumpla con los nuevos requisitos:

| Paso | Acción | Nodo n8n recomendado |
|------|--------|----------------------|
| 1️⃣ | **Detectar nuevos correos** en Gmail | **Gmail Trigger** |
| 2️⃣ | **Filtrar** solo los mensajes cuyo asunto contenga “propuesta” o “cotizacion” | **Filter** (Expression) |
| 3️⃣ | **Extraer** datos del remitente (nombre, email, asunto, fecha) | **Function** (JavaScript) |
| 4️⃣ | **Enviar una notificación** a Slack | **Slack > Send Message** |
| 5️⃣ | **Crear / actualizar** la información en Notion | **Notion > Create Page** (o **Update Database Item**) |

A continuación te detallo la configuración paso a paso, con los campos que debes rellenar y algunos tips para que el workflow sea robusto.

---

## 1️⃣ Gmail Trigger (Nuevo correo)

- **Node**: `Gmail` → **“Watch Email”** (o “New Email” si tu cuenta lo permite).
- **Configuración**:
  - **Label ID** (opcional): puedes filtrar por una etiqueta que tú apliques en Gmail (p. ej. “Propuestas”).
  - **Search Query**: si no usas etiquetas, pon algo como `subject:"propuesta" OR subject:"cotizacion"` para que el trigger solo despierte cuando llegue un correo con esas palabras (aunque después volveremos a filtrar en n8n).
- **Salida**: `id`, `subject`, `from`, `to`, `date`, `body`, etc.

> **Tip**: Si tu cuenta tiene límites de “watch” (máx. 1000 peticiones/día), considera usar la opción **“Polling”** (consulta cada X minutos) en lugar de “IMAP push”, para evitar sobrecargar la API.

---

## 2️⃣ Filter – Sólo los correos con “propuesta” o “cotizacion”

- **Node**: `Filter` (Expression).
- **Expression** (JSONPath):  

  ```javascript
  $json["subject"] =~ /(propuesta|cotizacion)/i
  ```

  - `i` hace la búsqueda *case‑insensitive*.
  - Si prefieres usar la salida del nodo anterior (`subject`), la expresión queda:

    ```javascript
    $json["subject"] =~ /(propuesta|cotizacion)/i
    ```

- **Resultado**: El workflow solo continúa si el asunto coincide; de lo contrario, el flujo se detiene (puedes añadir un **No‑Op** para que no se genere nada).

---

## 3️⃣ Function – Extraer datos del remitente

- **Node**: `Function`.
- **Código** (JavaScript). Puedes adaptar los campos a lo que necesites:

  ```javascript
  // Salida: un objeto con los campos que vas a enviar a Notion y Slack
  return [
    {
      // Nombre del remitente (puede venir como "Nombre Apellido <email@dominio.com>")
      senderName: $json["from"].match(/<(.*)>/)?.[1] ?? $json["from"].split("<")[0].trim(),
      senderEmail: $json["from"].match(/<(.*)>/)?.[1] ?? $json["from"].split("<")[1].trim(),
      subject: $json["subject"],
      date: $json["date"], // Formato ISO 8601
      // Si quieres también el cuerpo (para referencia)
      // body: $json["body"]
    }
  ];
  ```

- **Salida**: Un array con un único objeto (el que será usado en los siguientes nodos).

---

## 4️⃣ Slack – Notificación

- **Node**: `Slack` → **“Send Message”**.
- **Configuración**:
  - **Connection**: elige tu cuenta de Slack (si no la tienes, crea una nueva conexión OAuth).
  - **Channel**: por ejemplo `#alerts-propuestas` o cualquier canal que prefieras.
  - **Message Text**:  

    ```text
    📩 Nuevo correo con *propuesta* o *cotizacion*:
    *Remitente*: {{ $json["senderName"] }}
    *Email*: {{ $json["senderEmail"] }}
    *Asunto*: {{ $json["subject"] }}
    *Fecha*: {{ $json["date"] }}
    ```

- **Opciones extra**:
  - **Link to message** (si quieres que el mensaje sea clicable, puedes usar el `ts` del trigger y crear un “thread”).
  - **Bot name** (para que aparezca como “n8n Bot” o cualquier nombre que prefieras).

> **Tip**: Si deseas que la notificación sea más visual, puedes usar “blocks” de Slack (formatting JSON) – n8n lo soporta mediante la opción “Advanced” del nodo Slack.

---

## 5️⃣ Notion – Crear página (o actualizar base de datos)

### Opción A: Base de datos de Notion (recomendado)

1. **Crea una base de datos** en Notion (por ejemplo, “Propuestas”).  
   - Columnas típicas: `Nombre`, `Email`, `Asunto`, `Fecha`, `Notas` (puedes añadir más).

2. **Node**: `Notion` → **“Create Page”** (o “Update Database Item” si ya existe un identificador único).

3. **Configuración**:
   - **Connection**: tu cuenta de Notion (OAuth).
   - **Database ID**: copia el ID de la base de datos (lo encuentras en la URL: `https://www.notion.so/xxxxxxxxxxxxxx?v=...` → la parte larga antes de `v=`).
   - **Properties** (mapea los campos):

     | Campo Notion | Valor del objeto n8n |
     |--------------|----------------------|
     | **Name** (título) | `{{ $json["subject"] }}` |
     | **Remitente** (texto) | `{{ $json["senderName"] }}` |
     | **Email** (email) | `{{ $json["senderEmail"] }}` |
     | **Fecha** (date) | `{{ $json["date"] }}` |
     | **Notas** (texto) | `{{ $json["subject"] }}` (o cualquier otro dato que quieras guardar) |

   - Si deseas que el **remitente** sea una referencia a un usuario de Notion, primero tendrás que crear o buscar ese usuario y usar su `id` en la propiedad de “Person”.

4. **Salida**: La página creada en Notion (incluye su ID). Puedes usar ese ID para posteriores actualizaciones si lo necesitas.

### Opción B: Crear una página directamente (sin base de datos)

- Si no quieres usar una base de datos, simplemente usa **“Create Page”** dentro de una página específica.
- Mapea los campos como “Properties” (título, texto, fecha, etc.) de la misma forma que en la opción A.

---

## Flujo completo (esquema)

```
[Gmail Trigger] 
   ↓
[Filter (subject contains "propuesta" OR "cotizacion")]
   ↓
[Function – extraer senderName, senderEmail, subject, date]
   ↓
[Slack – Send Message (notificación)]
   ↓
[Notion – Create Page (base de datos "Propuestas")]
```

---

## Configuración paso a paso (resumen rápido)

1. **Añade el nodo “Gmail”** → “Watch Email”.  
   - Si usas “Polling”, define el intervalo (p.ej. 5 min).  
   - Opcional: pon `subject:"propuesta" OR subject:"cotizacion"` en **Search Query** para reducir llamadas.

2. **Conecta el nodo “Filter”**.  
   - Expression: `$json["subject"] =~ /(propuesta|cotizacion)/i`.

3. **Añade “Function”**.  
   - Copia el código de extracción y devuelve el objeto con los campos que necesitas.

4. **Conecta “Slack – Send Message”**.  
   - Selecciona tu workspace y canal.  
   - Usa los placeholders `{{ $json["senderName"] }}`, etc.

5. **Añade “Notion – Create Page”** (o “Update Database Item”).  
   - Configura la conexión y el **Database ID**.  
   - Mapea los campos (Name, Email, etc.) con los valores del objeto devuelto por el Function.

6. **Prueba** el workflow con un correo de prueba que cumpla el filtro.  
   - Verifica en Slack que recibes la notificación.  
   - Verifica en Notion que se crea la fila con los datos correctos.

---

## Buenas prácticas y tips extra

| Tema | Recomendación |
|------|---------------|
| **Manejo de errores** | Añade un nodo **“Try/Catch”** (o “IF” + “Error Handling”) después del Slack para registrar fallos en un log (p.ej., Google Drive, o envío de email). |
| **Rate limits** | Gmail y Notion tienen cuotas. Si el volumen es alto, considera **agregar un “Pause”** (p.ej., 1 s) entre iteraciones o usar **“Batch”** en Notion (crea varias páginas en una sola llamada). |
| **Identificador único** | Si vas a actualizar la misma propuesta después (por ejemplo, cuando el cliente responde), guarda el `Message ID` de Gmail en una propiedad de Notion y usa “Update Page” con ese ID. |
| **Formato de fecha** | Notion acepta ISO 8601 (`2025-11-02T14:30:00Z`). El nodo Gmail ya entrega la fecha en ese formato; si no, conviértela con `moment` o `date-fns` en el Function. |
| **Seguridad** | No expongas tu token de Notion ni tu credencial de Slack en logs. Usa las **Variables de Entorno** de n8n (`{{ $env.SLACK_TOKEN }}`) para mayor seguridad. |
| **Notificaciones avanzadas** | Si quieres que el mensaje de Slack incluya un botón “Ver en Notion”, puedes crear un **link profundo** (deep link) a la página recién creada y añadirlo como “actions” en el bloque de Slack. |

---

### Código completo del nodo **Function** (para copiar y pegar)

```javascript
// Extraer datos del remitente y devolverlos como objeto
// $json contiene la respuesta del nodo anterior (Gmail Trigger)

const rawFrom = $json["from"];            // ej: "Juan Pérez <juan@example.com>"
const senderMatch = rawFrom.match(/<(.*)>/);
const senderName = senderMatch ? senderMatch[1] : rawFrom.split("<")[0].trim();
const senderEmail = senderMatch ? senderMatch[1] : rawFrom.split("<")[1].trim();

return [
  {
    senderName: senderName,
    senderEmail: senderEmail,
    subject: $json["subject"],
    date: $json["date"], // ya está en ISO 8601
    // opcional: cuerpo del mensaje
    // body: $json["body"]
  }
];
```

---

## Resumen rápido de los nodos

| Nodo | Tipo | Propósito |
|------|------|-----------|
| **Gmail** | Trigger | Detecta nuevos correos (puedes filtrar por query o etiqueta). |
| **Filter** | Condition | Mantiene solo los que tengan “propuesta” o “cotizacion” en el asunto. |
| **Function** | JavaScript | Extrae `senderName`, `senderEmail`, `subject`, `date`. |
| **Slack** | Action | Envía una notificación al canal que elijas. |
| **Notion** | Action | Crea una fila (página) en la base de datos “Propuestas”. |

---

### ¿Qué sigue?

- **Prueba** con un correo de ejemplo (asunto “Cotizacion de proyecto X”).  
- Revisa en **Slack** que la notificación llega y con los datos correctos.  
- Abre **Notion** y verifica que la página se haya creado con la información esperada.  

Si necesitas ajustar algún campo (por ejemplo, agregar un número de referencia, incluir el cuerpo del mensaje, o crear una relación con otro recurso en Notion), solo avísame y afinamos el workflow. ¡Éxitos con la automatización! 🚀