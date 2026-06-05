# Qwen 3.7 Max — multi_turn/requirements_change

- model_id: `qwen/qwen3.7-max`
- success: True  | final: 6.04 | quality: 7.24
- latency_total: 41.727s | tokens_per_second: 69.1
- input_tokens: 233 | output_tokens: 2884
- judge_score: 3.8 | justificación: 

## Respuesta completa

¡Excelente cambio de rumbo! Notion es una herramienta mucho más potente para armar un mini-CRM o pipeline de ventas, y sumar Slack te dará visibilidad inmediata para que no se te escape ninguna oportunidad.

Aquí tienes la estructura exacta del workflow y cómo configurar cada nodo para que funcione a la perfección en la versión actual de n8n.

### 🛠️ Estructura del Workflow
**Gmail Trigger** ➡️ **IF (Filtro)** ➡️ **Code (Limpieza)** ➡️ **Notion (Guardado)** ➡️ **Slack (Aviso)**

---

### Paso a paso de la configuración:

#### 1. Gmail Trigger (El disparador)
*   **Event:** `Message Received`
*   **Format:** `Resolved` (Esto es importante para que te traiga el cuerpo del correo y los metadatos completos).
*   *Tip Pro:* No filtraremos desde aquí para asegurarnos de que el filtro de n8n capture variaciones como "Cotización" (con tilde) o mayúsculas.

#### 2. IF Node (El filtro)
Aquí le diremos a n8n que solo deje pasar los correos que nos interesan.
*   **Condition 1:** `String` | `Subject` | `Contains` | `propuesta`
*   **Condition 2 (con operador OR):** `String` | `Subject` | `Contains` | `cotiz` *(Usar "cotiz" en lugar de "cotizacion" es un truco para que detecte tanto "cotizacion" como "cotización" con tilde, y también "cotizaciones").*
*   **Combine:** Selecciona **OR** (Cualquiera de las dos condiciones).

#### 3. Code Node (Extracción y limpieza de datos)
El campo `From` de Gmail suele venir así: `"Juan Perez" <juan@empresa.com>`. Para que tu base de datos en Notion quede limpia, usaremos este pequeño script en JavaScript para separar el Nombre del Email:

```javascript
let results = [];

for (const item of $input.all()) {
  const fromField = item.json.From || item.json.from || '';
  let nombre = 'Desconocido';
  let email = fromField;

  // Expresión regular para separar Nombre <email@dominio.com>
  const match = fromField.match(/^(.*?)\s*<(.+?)>$/);
  if (match) {
    nombre = match[1].replace(/"/g, '').trim();
    email = match[2].trim();
  }

  results.push({
    json: {
      nombre: nombre,
      email: email,
      asunto: item.json.Subject || item.json.subject,
      fecha: item.json.Date || item.json.date,
      resumen: item.json.snippet // Las primeras líneas del correo
    }
  });
}

return results;
```

#### 4. Notion Node (Guardado en tu CRM)
*Pre-requisito:* Crea una Base de Datos en Notion con las columnas (Properties): `Nombre` (Title), `Email` (Email), `Asunto` (Text), `Fecha` (Date), y `Estado` (Status).
*   **Operation:** `Create Page` (in Database).
*   **Database:** Selecciona tu base de datos de Notion.
*   **Mapping (Mapeo de campos):**
    *   *Nombre:* Arrastra el campo `nombre` del Code Node.
    *   *Email:* Arrastra el campo `email`.
    *   *Asunto:* Arrastra el campo `asunto`.
    *   *Fecha:* Arrastra el campo `fecha`.
    *   *Estado:* Puedes hardcodear un valor como "Nueva Propuesta" o "Pendiente".

#### 5. Slack Node (La notificación)
*   **Operation:** `Send Message`.
*   **Channel:** Elige tu canal de ventas o notificaciones (ej. `#alertas-ventas`).
*   **Text / Message:** Usa expresiones de n8n para armar un mensaje atractivo. Ejemplo:
    ```text
    🚨 *Nueva Oportunidad Recibida*
    *Cliente:* {{$json.nombre}} ({{$json.email}})
    *Asunto:* {{$json.asunto}}
    *Resumen:* {{$json.resumen}}
    
    _Revisa Notion para más detalles._
    ```

---

### 💡 Consejos para Emprendedores:
1. **Manejo de Errores:** Conecta el nodo **"Error Trigger"** al workflow. Si Notion o Slack fallan (por ejemplo, se cayó la API), te llegará un correo de n8n avisándote que perdiste una propuesta.
2. **Deduplicación:** Si por error el trigger se dispara dos veces con el mismo correo, puedes agregar un nodo antes de Notion que revise si el `email` + `asunto` ya existen en la base de datos para evitar duplicados.

¿Te gustaría que te genere el **código JSON** de este workflow para que solo tengas que copiarlo y pegarlo directamente en tu lienzo de n8n (Ctrl+V / Cmd+V)?