# GLM 5.1 (NIM) — multi_turn/requirements_change

- model_id: `z-ai/glm-5.1`
- success: True  | final: 5.85 | quality: 5.28
- latency_total: 100.164s | tokens_per_second: 9.8
- input_tokens: 228 | output_tokens: 978
- judge_score: 2.4 | justificación: 

## Respuesta completa

¡Me parece perfecto! Cambiar a Notion, añadir el filtro y la notificación de Slack le da mucho más valor a tu automatización. 

Aquí tienes el diseño actualizado de tu workflow y cómo configurarlo paso a paso:

### Estructura del Workflow (5 Nodos)

1. **Gmail Trigger** (Disparador)
2. **IF** (Filtro de asunto)
3. **Notion** (Base de datos)
4. **Slack** (Notificación)
5. **No Operation, do nothing** (Para los emails que no pasan el filtro)

---

### Configuración paso a paso:

#### 1. Gmail Trigger
* **Credenciales:** Conecta tu cuenta de Gmail.
* **Event:** `Message Received`.
* **Label:** Puedes dejarlo en `INBOX` o usar una etiqueta específica si filtras previamente en Gmail.

#### 2. IF Node (El Filtro)
Aquí vamos a evaluar si el asunto contiene las palabras clave. Como son dos palabras, usaremos una combinación de condiciones tipo "OR" (O).
* **Conditions:**
  * **Condition 1:** 
    * Value: `{{ $json.subject }}` (Arrastra el campo asunto desde el panel izquierdo).
    * Operation: `Contains` (Contiene).
    * Value: `propuesta`
  * **Condition 2:** 
    * Value: `{{ $json.subject }}`
    * Operation: `Contains`
    * Value: `cotizacion`
* **Combine Operation:** `OR` (Esto es clave para que pase si tiene cualquiera de las dos palabras).

*💡 Tip de Oráculo: Si quieres que no importe si está en mayúsculas o minúsculas (ej. "Propuesta" o "COTIZACION"), en la operación del IF elige `Contains (Case Insensitive)` en lugar de `Contains`.*

#### 3. Notion Node (Rama "True" del IF)
Conecta este nodo a la salida **True** (verdadero) del nodo IF.
* **Resource:** `Database Page` (Página de base de datos).
* **Operation:** `Create`.
* **Database:** Selecciona la base de datos de Notion donde quieres guardar los datos. (Asegúrate de haber dado permisos a tu integración de Notion sobre esa base de datos específica).
* **Mapeo de propiedades (Depende de las columnas que tengas en Notion):**
  * *Nombre/Página:* `{{ $json.subject }}`
  * *Email:* `{{ $json.from.email }}` *(Nota: a veces Gmail entrega el email en formato `"Nombre" <email@dominio.com>`. Si es así, puedes usar un Set Node antes para limpiarlo, o simplemente guardar el texto completo).*
  * *Remitente:* `{{ $json.from.name }}`
  * *Fecha:* `{{ $json.date }}`

#### 4. Slack Node (Notificación)
Conecta este nodo a la salida del nodo de Notion (así se envía solo si se guardó correctamente).
* **Resource:** `Message`.
* **Operation:** `Send`.
* **Channel:** Selecciona el canal de Slack o escribe el ID del canal.
* **Text:** Puedes usar Markdown para dejar el mensaje bonito. Ejemplo:
  ```text
  🚨 ¡Nueva propuesta recibida! 
  *De:* {{ $json.from.name }} ({{ $json.from.email }})
  *Asunto:* {{ $json.subject }}
  *Fecha:* {{ $json.date }}
  ```
* **Other Options:** Puedes activar `Markdown in text` para que los asteriscos se conviertan en negritas.

#### 5. No Operation, do nothing (Rama "False" del IF)
Conecta este nodo a la salida **False** (falso) del nodo IF. 
* **Por qué lo necesitas:** En N8N, si una rama del IF no está conectada a nada, el workflow a veces da error o se detiene. Poner este nodo en la rama "False" asegura que los correos que no son propuestas simplemente se ignoren y el workflow continúe funcionando limpiamente para el próximo email.

---

### ¿Qué te parece esta estructura? 
Si en Notion tienes propiedades específicas (como un *Select* de estado o un *Checkbox*), dime cómo se llaman y te ayudo a mapearlas correctamente.