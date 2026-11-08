# Seed 2.0 Code — multi_turn/requirements_change

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 5.52 | quality: 6.0
- latency_total: 73.081s | tokens_per_second: 76.2
- input_tokens: 279 | output_tokens: 5569

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

### Workflow N8N Final (Adaptado a tus Nuevos Requisitos)
Estructura de nodos **ordenada y optimizada**:
```
Gmail Trigger → Code Node (Limpiar Datos) → IF Node (Filtro Definitivo) → [RAMA VERDADERA] Notion (Crear Página) → Slack (Notificación)
                                                                         ↓
                                                                   [RAMA FALSA] NoOp (Opcional, para claridad)
```

---

## Paso 1: Configurar el **Gmail Trigger** (Filtro PREVIO para ahorrar ejecuciones)
### Por qué: Filtramos correos ANTES de que entren al workflow (evita ejecuciones innecesarias)
1. **Nodo**: `Gmail (Beta)`
2. **Evento**: `Email Received`
3. **Cuenta**: Selecciona tu cuenta de Gmail
4. **Carpeta**: `INBOX`
5. **Consulta de Búsqueda (Filtro PREVIO)** (usa sintaxis de Gmail):
   ```gmail
   subject:("propuesta" OR "cotizacion" OR "cotización")
   ```
   > Nota: Incluimos `cotización` con acento para cubrir ambos casos (Gmail no siempre distingue acentos, así que lo aseguramos)
6. **Opcional**: Activa `Fetch Attachments?` si quieres guardar adjuntos en Notion luego
7. **Modo de Ejecución**: En N8N Cloud, el *polling* es automático; en Self-Hosted, activa `Polling` y establece un intervalo (ej: 5 minutos)

---

## Paso 2: **Code Node** (Limpiar Datos de Remitente y Asunto)
### Por qué: El campo `from` de Gmail viene como `Nombre <email@dominio.com>` → extraemos nombre/email limpios, y limpiamos el asunto de acentos/mayúsculas para el filtro definitivo.
1. **Nodo**: `Code` (nuevo nombre en N8N v1+, antes `Function`)
2. **Modo**: `Run Once for All Items`
3. **Código JavaScript (cópialo tal cual)**:
   ```javascript
   return $input.all().map(item => {
     // 1. Extraer NOMBRE y EMAIL del remitente (formato: "Nombre <email@dominio.com>")
     const fromStr = item.json.from;
     const regexRemitente = /^(.*?)\s*<([^>]+)>$/;
     const matchRemitente = fromStr.match(regexRemitente);
     
     const nombreRemitente = matchRemitente ? matchRemitente[1].trim() : fromStr;
     const emailRemitente = matchRemitente ? matchRemitente[2].trim() : fromStr;

     // 2. Limpiar ASUNTO (minúsculas + sin acentos) para filtro definitivo
     const asuntoOriginal = item.json.subject || "";
     const asuntoLimpio = asuntoOriginal
       .toLowerCase()
       .normalize("NFD") // Quita acentos
       .replace(/[\u0300-\u036f]/g, "");

     // 3. Crear enlace directo al correo en Gmail
     const enlaceGmail = `https://mail.google.com/mail/u/0/#inbox/${item.json.messageId}`;

     return {
       json: {
         ...item.json, // Mantiene TODOS los datos originales de Gmail
         nombreRemitente,
         emailRemitente,
         asuntoLimpio,
         enlaceGmail
       }
     };
   });
   ```
4. **Prueba**: Ejecuta el nodo para ver que los campos `nombreRemitente`, `emailRemitente` y `asuntoLimpio` aparezcan correctamente.

---

## Paso 3: **IF Node** (Filtro DEFINITIVO)
### Por qué: Doble seguridad para asegurarnos de que solo pasen correos con `propuesta` o `cotizacion` (incluso si el filtro de Gmail falla por espacios o caracteres extraños)
1. **Nodo**: `IF`
2. **Condiciones** (usa el campo `asuntoLimpio` del Code Node):
   - **Condición 1**: `asuntoLimpio` → `Contains` → `propuesta`
   - **Operador**: `OR`
   - **Condición 2**: `asuntoLimpio` → `Contains` → `cotizacion`
3. **Resultado**:
   - 🟢 **Rama Verdadera**: Correos que cumplen el filtro → conecta a **Notion**
   - 🔴 **Rama Falsa**: Correos que no cumplen → conecta a un nodo `NoOp` (No Operation) o deja vacío (no pasa nada)

---

## Paso 4: **Notion (Beta)** (Crear Página con Datos del Correo)
### Pre-requisito ANTES de configurar el nodo:
1. Crea una **Base de Datos en Notion** con estas **propiedades** (exactamente los nombres, sino N8N no mapea):
   | Nombre Propiedad | Tipo de Propiedad |
   |------------------|-------------------|
   | Nombre Remitente | Texto             |
   | Email Remitente  | Email             |
   | Asunto           | Texto             |
   | Fecha Recibido   | Fecha             |
   | Enlace Gmail     | URL               |
2. Crea una **Integración en Notion**:
   - Ve a **Settings & Members → Integrations → Develop your own integrations → Create new integration**
   - Copia el **Token de la Integración** (lo necesitarás en N8N)
3. **Comparte la Base de Datos con la Integración**:
   - Abre tu base de datos de Notion → Haz clic en **Share** → Busca el nombre de tu integración → Agrega permisos de **Editar**

---

### Configuración del Nodo Notion en N8N:
1. **Nodo**: `Notion (Beta)`
2. **Conexión**: Pega el Token de la Integración de Notion
3. **Acción**: `Create a Page`
4. **Base de Datos**: Selecciona tu base de datos (debe aparecer si la compartiste correctamente)
5. **Mapeo de Campos (Propiedades de Notion ↔ Datos de N8N)**:
   - **Título de la Página**: Usa el asunto del correo → `Asunto: {{$json.subject}}`
   - **Propiedades**:
     | Propiedad Notion       | Valor N8N (Expresión)                          |
     |------------------------|------------------------------------------------|
     | Nombre Remitente       | `{{$json.nombreRemitente}}`                    |
     | Email Remitente        | `{{$json.emailRemitente}}`                     |
     | Asunto                 | `{{$json.subject}}`                            |
     | Fecha Recibido         | `{{$json.receivedDate}}`                       |
     | Enlace Gmail           | `{{$json.enlaceGmail}}`                        |
6. **Opcional**: Agrega el **cuerpo del correo** como contenido de la página de Notion:
   - En el campo **Content** del nodo Notion, usa `{{$json.body}}` (pero `body` es HTML; si quieres texto plano, agrega un nodo `HTML to Text` entre el Code Node y el IF Node)

---

## Paso 5: **Slack Node** (Notificación Personalizada)
### Pre-requisito:
- Autoriza N8N para acceder a tu workspace de Slack (usa **OAuth** en vez de Webhooks: es más fácil y seguro → N8N te redirige a Slack para autorizar)

---

### Configuración del Nodo Slack:
1. **Nodo**: `Slack`
2. **Conexión**: Conecta tu workspace de Slack vía OAuth
3. **Acción**: `Post Message`
4. **Canal**: Selecciona el canal (ej: `#ventas` o `#general`) → si es un canal privado, **agrega la app de N8N al canal** (Slack → Canal → Integrations → Add apps)
5. **Mensaje (Personalizado, usa Markdown de Slack)**:
   ```slack
   📩 *NUEVA PROPUESTA/COTIZACIÓN RECIBIDA*
   👤 Remitente: {{$json.nombreRemitente}} ({{$json.emailRemitente}})
   📌 Asunto: {{$json.subject}}
   📅 Fecha: {{$json.receivedDate}}
   🔗 [Ver en Gmail]({{$json.enlaceGmail}}) | [Ver en Notion]({{$json.url}})
   ```
   > Nota: `{{$json.url}}` es el **enlace directo a la página de Notion** (devuelto automáticamente por el nodo Notion al crear la página)

---

## Paso 6: Prueba y Ajustes
1. **Prueba con un correo de prueba**: Envía un correo a tu cuenta con asunto `Propuesta de servicio` (o `Cotización de producto`)
2. **Verifica flujos**:
   - El correo pasa por el Gmail Trigger
   - El Code Node extrae los datos correctamente
   - El IF Node lo envía a la Rama Verdadera
   - Notion crea la página
   - Slack envía la notificación
3. **Ajustes opcionales**:
   - Agrega un filtro por remitente (ej: solo correos de `@dominiocliente.com`) en el IF Node
   - Guarda adjuntos de Gmail en Notion (usa el campo `attachments` del Gmail Trigger y el nodo `Notion Upload File`)
   - Activa **Workflow Settings → Save Execution** para depurar errores

---

## Errores Comunes a Evitar
1. **No compartiste la base de datos de Notion con la integración**: El nodo Notion no verá la base de datos.
2. **Nombres de propiedades de Notion incorrectos**: Asegúrate de que sean exactamente `Nombre Remitente`, `Email Remitente`, etc.
3. **Canal de Slack privado sin la app de N8N**: La notificación no se enviará.
4. **Filtro de Gmail sin comillas**: Sin `""`, Gmail busca coincidencias parciales (ej: `propuestas` también pasaría).

¿Necesitas que te explique cómo agregar adjuntos o filtrar por remitente específico?