# Seed 2.0 Code — multi_turn/requirements_change

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 5.72 | quality: 6.0
- latency_total: 35.464s | tokens_per_second: 57.7
- input_tokens: 279 | output_tokens: 2048

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


El usuario cambió el workflow: ahora Notion en vez de Sheets, filtro por asunto (propuesta/cotización) y notificación Slack. Primero voy a estructurar el workflow paso a paso, con detalles de configuración de NODOS, TRIGGER, FILTRO, INTEGRACIONES.

Primero, el TRIGGER: Gmail Trigger, pero hay que configurar el modo (polling o webhook? En N8N el Gmail Trigger por defecto es polling cada 1 min, pero se puede habilitar el webhook si es cuenta Google Workspace? Wait, no, el Gmail Trigger de N8N usa la API de Gmail, el modo "New Email" con filtro en el trigger o después? Mejor: el trigger escucha nuevos emails, luego un NODO DE FILTRO (IF node) para filtrar el asunto, porque es más flexible.

Luego, la extracción de datos: el Gmail Trigger devuelve el remitente en `from` (campo con nombre y email, ej: "Juan Perez <juan@ejemplo.com>"). Hay que parsear eso? Sí, porque en N8N el campo `from` es un string, así que un FUNCTION node o un SET node para extraer nombre y email por separado. Wait, N8N tiene el nodo "Extract Email" o mejor usar el SET node con expresiones? O un Function node simple para dividir el string.

Después, el filtro: IF node. Condición: el asunto (de Gmail) incluye "propuesta" O "cotización". Ojo con mayúsculas/minúsculas: mejor convertir el asunto a minúsculas en la expresión, para que no importe si es "Propuesta" o "propuesta".

Luego, NOTION: Crear una página en una base de datos (database). Primero, el usuario necesita tener una base de datos en Notion con propiedades: Nombre Remitente (texto), Email Remitente (email), Asunto (texto), Fecha Email (fecha), Cuerpo Resumido (opcional, o texto completo? Mejor resumido o el campo `snippet` de Gmail). Hay que explicar cómo conectar Notion a N8N: necesitan el Token de Integración de Notion, y compartir la base de datos con la integración.

Luego, SLACK: Nodo Slack Send Message. Canal (ej: #alertas-ventas), mensaje personalizado con los datos del remitente y asunto. Necesitan conectar Slack a N8N: OAuth o Token de Bot, y agregar el bot al canal.

También, hay que agregar un ELSE en el IF node? Opcional, pero mejor dejarlo como "sin acción" si no cumple el filtro.

Voy a estructurar el workflow en ORDEN EXACTO de NODOS, con CONFIGURACIÓN DETALLADA de cada uno, incluyendo EXPRESIONES de N8N (porque eso es lo que más complica a los usuarios), y PASOS PREVIOS de configuración de integraciones.

También, agregar un paso de PRUEBA: cómo probar cada nodo, especialmente el filtro.

Wait, el usuario es emprendedor, así que no quiero términos muy técnicos, pero sí precisos. Por ejemplo, en el IF node, explicar cómo hacer la condición OR, y cómo convertir el asunto a minúsculas para no fallar por mayúsculas.

También, en el Gmail Trigger: qué campos seleccionar? "New Email" en el evento, y quizás seleccionar la carpeta INBOX, para no incluir spam.

En la extracción del remitente: el Gmail Trigger devuelve `from` como un string como "María López <maria@empresa.com>". Así que para extraer el email, usar la expresión: `{{ $json.from.match(/<([^>]+)>/)[1] }}` y para el nombre: `{{ $json.from.replace(/<[^>]+>/g, '').trim() }}`. Eso se puede poner en un SET node para crear variables limpias, o en un Function node. Mejor SET node porque es más visual para emprendedores.

En Notion: La base de datos debe tener propiedades que coincidan con los datos que vamos a enviar. Por ejemplo:
- Nombre Remitente (Tipo: Texto)
- Email Remitente (Tipo: Email)
- Asunto Email (Tipo: Texto)
- Fecha Recepcion (Tipo: Fecha)
- Enlace al Email (Tipo: URL) → Genial porque el Gmail Trigger devuelve el `id` del email, así que el enlace es `https://mail.google.com/mail/u/0/#inbox/{{ $json.id }}`

En Slack: El mensaje puede ser algo como:
> 🚨 NUEVO EMAIL DE PROPUESTA/COTIZACIÓN
> Remitente: {{ $json["Nombre Remitente"] }} ({{ $json["Email Remitente"] }})
> Asunto: {{ $json["Asunto Email"] }}
> Enlace al Email: {{ $json["Enlace Email"] }}

También, PASOS PREVIOS OBLIGATORIOS:
1. Conectar Gmail a N8N: OAuth, solo hay que iniciar sesión en la cuenta de Gmail cuando el nodo lo pida.
2. Conectar Notion a N8N:
   a. Ir a [Notion Integrations](https://www.notion.so/my-integrations) → Crear nueva integración (nombre: N8N Workflow Emails) → Copiar el **Token de Integración**.
   b. Ir a la base de datos de Notion → Compartir → Agregar la integración que creaste (buscar su nombre).
   c. En N8N, en el nodo Notion, pegar el Token de Integración.
3. Conectar Slack a N8N:
   a. Ir a [Slack Apps](https://api.slack.com/apps) → Crear nueva app (From Scratch, nombre: N8N Alertas, workspace de tu empresa).
   b. Ir a **OAuth & Permissions** → Agregar el permiso `chat:write` y `chat:write.public` (si quieres enviar a canales públicos sin agregar el bot, pero mejor agregar el bot al canal).
   c. Instalar la app en tu workspace → Copiar el **Bot User OAuth Token**.
   d. En N8N, en el nodo Slack, pegar el Token.
   e. Agregar el bot de Slack al canal donde quieres recibir la notificación (ej: en Slack, escribe `/invite @N8N Alertas` en el canal).

Ahora, estructurar el workflow en NODOS ORDENADOS:

1. **Nodo 1: Gmail Trigger (Evento: Nuevo Email)**
   - Configuración:
     - Evento: `New Email`
     - Carpeta: `INBOX` (para evitar spam)
     - Frecuencia de Polling: Dejar en `1 minuto` (o ajustar, pero es suficiente)
     - Conectar tu cuenta de Gmail (OAuth)
   - Datos que devuelve: `from`, `subject`, `id`, `snippet`, `receivedDate`, etc.

2. **Nodo 2: Set (Limpiar y estructurar datos)**
   - Propósito: Extraer nombre y email del remitente, crear enlace al email, convertir fecha a formato Notion.
   - Configuración:
     - Marcar `Keep Only Set` (para no guardar datos innecesarios)
     - Agregar los siguientes campos (usar EXPRESIONES de N8N):
       1. **Nombre Remitente**: `{{ $json.from.replace(/<[^>]+>/g, '').trim() }}` → Quita el email del string `from`
       2. **Email Remitente**: `{{ $json.from.match(/<([^>]+)>/)[1] }}` → Extrae el email entre `<` y `>`
       3. **Asunto Email**: `{{ $json.subject }}` → Asunto original
       4. **Fecha Recepcion**: `{{ $json.receivedDate }}` → Fecha de recepción (Notion acepta el formato ISO que devuelve Gmail)
       5. **Enlace Email**: `https://mail.google.com/mail/u/0/#inbox/{{ $json.id }}` → Enlace directo al email en Gmail
   - *Nota*: Si el `from` no tiene nombre (ej: solo `<juan@ejemplo.com>`), la expresión de Nombre Remitente devolverá vacío, lo cual es normal.

3. **Nodo 3: If (Filtro por asunto)**
   - Propósito: Solo pasar los emails que tengan "propuesta" O "cotización" en el asunto (sin importar mayúsculas/minúsculas)
   - Configuración:
     - Tipo de Condición: `