# Kimi K2.6 — multi_turn/requirements_change

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 4.25 | quality: 4.0
- latency_total: 34.364s | tokens_per_second: 61.3
- input_tokens: 266 | output_tokens: 2106

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

 Aquí tienes el workflow actualizado. Es mucho más eficiente si filtras directamente en el **Gmail Trigger** usando el lenguaje de búsqueda nativo de Gmail, así N8N solo se activa cuando realmente hay un match.

### 🔧 Arquitectura del Workflow

```
[Gmail Trigger] → [Extraer Datos (Set/Code)] → [Notion: Create DB Item] → [Slack: Post Message]
```

---

### 1️⃣ Gmail Trigger
Configura el nodo para que solo "escuche" los correos correctos desde el origen:

*   **Authentication:** OAuth2 (tu cuenta de Gmail conectada).
*   **Event:** `Message Received`.
*   **Query (campo de filtro):**
    ```
    newer_than:1d (subject:propuesta OR subject:cotización)
    ```
    *Nota: Gmail ignora acentos en muchos casos, pero si quieres cubrir "cotizacion" y "cotización", usa dos OR anidados: `(subject:propuesta OR subject:cotizacion OR subject:cotización)`.*

Esto hace que Google solo envíe a N8N los correos que cumplen la condición.

---

### 2️⃣ Extraer datos del Remitente (Set Node o Code Node)
El campo `From` en Gmail viene como: `Juan Pérez <juan@empresa.com>`. Necesitas separarlo.

Usa un nodo **Set** (o **Code** si prefieres JS) para crear variables limpias:

| Nombre | Valor (Expresión N8N) |
| :--- | :--- |
| `nombreRemitente` | `{{ $json.from.replace(/ <.*>/, '').trim() }}` |
| `emailRemitente` | `{{ ($json.from.match(/<(.*)>/) \|\| [null, $json.from])[1] }}` |
| `asuntoEmail` | `{{ $json.subject }}` |
| `fechaEmail` | `{{ $json.date }}` |

*Consejo:* Si el remitente no tiene nombre y solo aparece el email, la expresión de `nombreRemitente` devolverá el email. Puedes dejarlo así o agregar una lógica extra para detectarlo.

---

### 3️⃣ Notion: Create Database Item
Antes de esto, asegúrate de:
1. Crear una base de datos en Notion.
2. Crear una integración en [notion.so/my-integrations](https://notion.so/my-integrations) y copiar el **Internal Integration Token**.
3. Compartir tu base de datos con esa integración (botón `Share` → Invite → tu integración).

Configuración del nodo **Notion → Create a Database Item**:

*   **Credential:** Tu token de integración.
*   **Database:** Selecciona tu base de datos (o pega el Database ID).
*   **Properties (mapeo):** Depende de cómo hayas nombrado las columnas en Notion. Ejemplo:
    *   `Nombre` (Title): `{{ $json.nombreRemitente }}`
    *   `Email` (Email): `{{ $json.emailRemitente }}`
    *   `Asunto` (Rich Text): `{{ $json.asuntoEmail }}`
    *   `Fecha` (Date): `{{ $json.fechaEmail }}`
    *   `Estado` (Select): `Nuevo` (o el valor por defecto que quieras).

---

### 4️⃣ Slack: Post a Message
Usa el nodo **Slack → Post a Message** (requiere credencial Slack OAuth2 o Incoming Webhook).

*   **Channel:** El nombre del canal (ej: `#leads`) o el Channel ID.
*   **Text:**
    ```
    📩 *Nueva oportunidad recibida*
    
    *De:* {{ $json.nombreRemitente }} ({{ $json.emailRemitente }})
    *Asunto:* {{ $json.asuntoEmail }}
    *Fecha:* {{ $json.fechaEmail }}
    
    Guardado en Notion ✅
    ```

---

### 🛡️ Consideraciones Importantes

1.  **Duplicados:** Gmail Trigger puede activarse más de una vez por el mismo email si se mueve entre carpetas. Si es crítico, agrega un nodo **Notion → Find Database Item** antes del paso 3 para buscar si ya existe un registro con ese `messageId` de Gmail.
2.  **Adjuntos:** Si luego quieres guardar PDFs de las cotizaciones, necesitarás agregar un nodo **Gmail → Get Message** y luego subir el adjunto a Google Drive/Notion.
3.  **Errores:** Agrega un nodo **Error Trigger** o conecta un nodo **Slack** a la rama de error de Notion para avisarte si falla el guardado.

¿Necesitas que te detalle cómo obtener el **Database ID** de Notion o cómo configurar las credenciales de Gmail/Slack paso a paso?