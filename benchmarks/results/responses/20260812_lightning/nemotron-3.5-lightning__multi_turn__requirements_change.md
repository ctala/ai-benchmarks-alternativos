# Nemotron 3.5 Lightning — multi_turn/requirements_change

- model_id: `nvidia/nemotron-3.5-lightning`
- success: True  | final: 6.38 | quality: 6.0
- latency_total: 6.027s | tokens_per_second: 428.2
- input_tokens: 248 | output_tokens: 2581
- judge_score: 4.6 | justificación: 

## Respuesta completa

¡Entendido! Cambiemos el enfoque a Notion, con filtro inteligente y notificación en Slack. Este es un workflow muy común en N8N.

A continuación te describo la estructura exacta de nodos y la expresión que necesitas. Puedes copiarla directamente o usar el generador de workflows al final.

### 📋 Estructura del Workflow en N8N

1. **Gmail Trigger** (Activado por "Nuevo correo")
   - No requiere configuración compleja; solo conecta tu cuenta de Gmail.
   - Emite los datos del email: `subject`, `from`, `date`, `id`, etc.

2. **Nodo IF** (Filtrado por asunto)
   - **Propósito**: Solo continuar si el asunto contiene "propuesta" O "cotización".
   - **Expresión de condición**:
     ```javascript
     {{ $json["subject"].toLowerCase().includes("propuesta") || $json["subject"].toLowerCase().includes("cotización") }}
     ```
   - **Configuración**: 
     - Modo: "Keep" (Mantener) items donde la condición sea `true`.
     - Si es `false`, el workflow se detiene para ese email (o puedes agregar una rama "Rechazar").

3. **Function Node** (Extraer datos del remitente)
   - **Objetivo**: Parsear el campo `from` y dejar los datos limpios.
   - **Código**:
     ```javascript
     const rawFrom = $json["from"]; // Ejemplo: "Juan Pérez <juan@empresa.com>"
     const emailMatch = rawFrom.match(/<(.+)>/);
     
     return [
       {
         json: {
           remitente_nombre: rawFrom.replace(/<.*/, "").trim(),
           remitente_email: emailMatch ? emailMatch[1] : rawFrom,
           asunto: $json["subject"],
           fecha: $json["date"],
           id_email: $json["id"]
         }
       }
     ];
     ```
   - *Nota*: Este nodo solo se ejecuta si el IF fue `true`.

4. **Notion Node** (Guardar en base de datos)
   - **Acción**: "Create Database Item" (Crear ítem en base de datos).
   - **Configuración de campos** (adáptalo a tu base de datos Notion):
     - **Nombre** (o property "Remitente"): `{{ $json["remitente_nombre"] }}`
     - **Email** (property "Email"): `{{ $json["remitente_email"] }}`
     - **Asunto** (property "Asunto"): `{{ $json["asunto"] }}`
     - **Fecha** (property "Fecha"): `{{ $json["fecha"] }}`
     - **ID Email** (puedes guardarlo en una propiedad oculta para referencia): `{{ $json["id_email"] }}`
   - Necesitarás tener ya creado un base de datos en Notion con esas propiedades (Tipo de texto, fecha, etc.).

5. **Slack Node** (Notificación)
   - **Acción**: "Send Message".
   - **Configuración**:
     - **Channel**: ID o nombre del canal (ej: `#propuestas` o `@usuario`).
     - **Texto del mensaje** (usar modo "Code Block" o expresiones):
       ```
       📥 *Nuevo email de propuesta/cotización*
       
       *Remitente*: {{ $json["remitente_nombre"] }} ({{ $json["remitente_email"] }})
       *Asunto*: {{ $json["asunto"] }}
       *Fecha*: {{ $json["fecha"] }}
       ```
   - Esto te alertará al momento en que cumpla el filtro y se guarde en Notion.

### 🔄 Flujo completo de ejecución
```
Gmail Trigger → IF (filtro asunto) → Function (extraer datos) → Notion (guardar) → Slack (notificar)
```
- Si el asunto **no** tiene "propuesta" ni "cotización", el workflow se detiene en el nodo IF y nada se envía a Notion/Slack.
- Si sí coincide, fluyen los 3 pasos siguientes.

### ⚙️ ¿Qué necesito de tu parte para armarlo 100%?
1. ¿Ya tienes una base de datos en Notion creada con propiedades específicas (nombre, email, asunto, fecha)? Si no, te digo cómo crearla rápidamente.
2. ¿El correo de Gmail que quieres capturar tiene siempre el remitente en el formato `"Nombre <email>"` o hay variaciones? (El código de la Function node maneja el estándar, pero puedo ajustarlo).
3. ¿En qué canal de Slack quieres que llegue la notificación? (Puedo usar el nombre o necesito el ID).

### 📦 Opción rápida: Importar el workflow JSON
Si prefieres no armarlo nodo por nodo, puedo generar el archivo JSON completo de N8N con todos los nodos y conexiones. Solo necesitarías:
- Importarlo en tu instancia de N8N.
- Ingresar tus credenciales de Gmail, Notion (con la DB creada) y Slack.
- Ajustar el nombre de la base de datos si difiere.

¿Te animas a que te pase el JSON completo, o prefieres que te guíe paso a paso con la configuración de cada nodo?