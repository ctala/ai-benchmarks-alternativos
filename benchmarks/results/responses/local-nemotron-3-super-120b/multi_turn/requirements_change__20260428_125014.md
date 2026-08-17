# Nemotron 3 Super 120B (DGX Spark Q4_K_M) — multi_turn/requirements_change

- model_id: `nemotron-3-super:120b`
- success: True  | final: 6.43 | quality: 8.36
- latency_total: 242.742s | tokens_per_second: 18.5
- input_tokens: 248 | output_tokens: 4494
- judge_score: 4.6 | justificación: 

## Respuesta completa

¡Perfecto! Aquí tienes el workflow actualizado según tus nuevas necesidades: **filtrar emails con "propuesta" o "cotizacion" en el asunto, enviar datos a Notion y notificar en Slack**. He optimizado cada paso para que sea robusto y fácil de configurar.

---

### 🔧 **Prerrequisitos (configura esto primero)**
1. **Credenciales en N8N**:
   - [Gmail](https://n8n.io/integrations/gmail/) (OAuth2, habilita `Gmail API` en Google Cloud).
   - [Notion](https://n8n.io/integrations/notion/) (Integración interna, comparte tu base de datos con la integración).
   - [Slack](https://n8n.io/integrations/slack/) (OAuth2, invita al bot a tu canal).
2. **Base de datos en Notion**:
   - Crea una base de datos tipo *Table* o *Board* con estas propiedades:
     - `Nombre` (Tipo: **Título**) → Para el nombre del remitente.
     - `Email` (Tipo: **Texto**) → Para el email del remitente.
     - `Asunto` (Tipo: **Texto**) → Para el asunto del email.
     - `Fecha` (Tipo: **Fecha**) → Para la fecha del email (formato ISO 8601).
   - Copia el **ID de la base de datos** (lo encontrarás en la URL: `https://www.notion.so/tu-workspace/.../v/ID_DE_LA_BASE`).

---

### 📐 **Workflow en N8N (4 nodos)**
#### 1. **Gmail Trigger** → *Filtrar emails relevantes*
   - **Recurso**: `Messages`  
   - **Operación**: `Get New Messages`  
   - **Búsqueda** (campo *Search*):  
     ```plain
     subject:(propuesta OR cotizacion)
     ```
     - ✅ **Por qué funciona**: Usa sintaxis de Gmail (`OR` en mayúsculas y paréntesis para agrupar). Es **case-insensitive** (ej: "Propuesta" o "COTIZACION" también coinciden).
     - ⚠️ **Nota**: Si necesitas incluir acentos (ej: "proposición"), ajusta la búsqueda manualmente (ej: `subject:(propuesta propuesta OR cotizacion)`), pero asumo que usas las palabras exactas que indicaste.
   - **Otras opciones**:
     - Marca `Only get unread messages` si quieres evitar reprocesar emails leídos.
     - Intervalo de sondeo: `Every 5 minutes` (ajusta según tu necesidad).

#### 2. **Function Node** → *Extraer y formatear datos*
   - **Propósito**: Parsear el remitente (separar nombre/email) y convertir la fecha a formato ISO para Notion.
   - **Código**:
     ```javascript
     // Extraer nombre y email del campo "from" (ej: "Juan Pérez <juan@empresa.com>")
     const from = $json.from;
     let name = "";
     let email = "";

     if (from.includes("<")) {
       const match = from.match(/^(.*) <(.+)>$/);
       if (match) {
         name = match[1].trim();
         email = match[2];
       } else {
         email = from; // Fallback si el formato es inesperado
       }
     } else {
       email = from;
       name = ""; // Si no hay nombre, dejar vacío
     }

     // Convertir fecha de Gmail (RFC 2822) a ISO 8601 para Notion
     const date = new Date($json.date).toISOString();

     return [{
       name: name,
       email: email,
       subject: $json.subject,
       date: date // Ya en formato ISO
     }];
     ```
   - **Salida**: Un array con un objeto conteniendo `{ name, email, subject, date }`.

#### 3. **Notion Node** → *Guardar en tu base de datos*
   - **Recurso**: `Page`  
   - **Operación**: `Create`  
   - **Database ID**: [Pega aquí el ID de tu base de datos de Notion]  
   - **Propiedades** (mapea cada campo):
     - `Nombre` → `{{ $json.name }}` (Tipo: Título)  
     - `Email` → `{{ $json.email }}` (Tipo: Texto)  
     - `Asunto` → `{{ $json.subject }}` (Tipo: Texto)  
     - `Fecha` → `{{ $json.date }}` (Tipo: Fecha)  
   - ✅ **Clave**: Asegúrate de que los nombres de las propiedades coincidan exactamente con los de tu base de datos (sensible a mayúsculas/minúsculas).

#### 4. **Slack Node** → *Notificar al equipo*
   - **Recurso**: `Message`  
   - **Operación**: `Post`  
   - **Canal**: Ej: `#notificaciones-propuestas` (o el canal que prefieras)  
   - **Texto del mensaje**:
     ```
     📩 Nueva propuesta/cotización recibida:
     • De: {{$json.name}} (<{{$json.email}}>)
     • Asunto: {{$json.subject}}
     • Hora: {{$json.date}} (formato ISO, pero Slack lo mostrará legible)
     ```
   - ✅ **Tip**: Usa emojis o formato markdown para destacar la notificación (Slack soporta `*negrita*`, `_cursiva_`, etc.).

---

### 🔄 **Flujo completo**
```plain
[Gmail Trigger] 
  ↓ (Solo emails con "propuesta"/"cotizacion" en asunto)
[Function Node] 
  ↓ (Extrae: name, email, subject, date→ISO)
[Notion Node] 
  ↓ (Crea fila en tu base de datos)
[Slack Node] 
  ↓ (Envía notificación al canal)
```

---

### 💡 **Consejos para evitar problemas**
1. **Prueba el filtro de Gmail primero**:  
   Usa la barra de búsqueda de Gmail con `subject:(propuesta OR cotizacion)` para verificar que capture los emails correctos antes de activar el workflow.
2. **Formato de fecha en Slack**:  
   Si prefieres una fecha más legible en Slack (ej: "21 oct 2023, 10:30"), añade un segundo Function Node antes de Slack para formatearla con `new Date($json.date).toLocaleString()`.
3. **Manejo de errores**:  
   Si quieres ser más robusto, agrega un `IF` Node después de Notion para solo enviar a Slack si la creación en Notion fue exitosa (ej: `{{ $json["success"] }}`).
4. **Límites de Notion**:  
   La API de Notion tiene límites de velocidad (~3 requests/segundo). Si esperas alto volumen, considera agregar un `Wait` Node (ej: 500ms) entre Notion y Slack.

---

### 🚀 **Pasos para activarlo**
1. Copia este workflow en N8N (usa el menú `Import` → `Workflow from JSON` si prefieres no construirlo manualmente).
2. Configura las credenciales de Gmail, Notion y Slack.
3. Crea la base de datos en Notion con las propiedades especificadas.
4. Pega el ID de la base de datos en el nodo Notion.
5. Activa el workflow (`Toggle Active` en la esquina superior derecha).

¿Necesitas que te genere el JSON listo para importar o que detalle algún nodo en específico? ¡Avísame! 😊