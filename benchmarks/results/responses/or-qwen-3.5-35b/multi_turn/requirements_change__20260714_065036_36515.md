# Qwen 3.5 35B — multi_turn/requirements_change

- model_id: `qwen/qwen3.5-35b-a3b`
- success: True  | final: 4.86 | quality: 4.0
- latency_total: 6.649s | tokens_per_second: 176.7
- input_tokens: 233 | output_tokens: 1175
- judge_score: 2.0 | justificación: La respuesta no es relevante ya que cambia los requisitos originales de Gmail y Google Sheets a una solución con Notion y Slack, aunque está bien estructurada y clara.

## Respuesta completa

¡Excelente cambio! La combinación de **Gmail + Notion + Slack** es muy potente para gestión de leads.

Aquí tienes la estructura detallada del workflow, paso a paso, para lograr filtrar, guardar y notificar.

### 📋 Estructura del Workflow

1.  **Gmail Trigger**: Escucha nuevos correos.
2.  **Filter**: Filtra por el asunto (contiene "propuesta" o "cotización").
3.  **Function**: Limpia y formatea los datos (opcional, pero recomendado).
4.  **Notion**: Crea la entrada en tu base de datos.
5.  **Slack**: Envía la alerta al canal.

---

### 🛠️ Configuración Paso a Paso

#### 1. Nodo Gmail Trigger
*   **Operation:** `New Email`
*   **Criteria:** Puedes dejarlo en `All` o especificar `Unread`.
*   **Important:** Asegúrate de crear las credenciales en la pestaña "Credentials" de N8N para tu cuenta de Gmail.

#### 2. Nodo Filter (El filtro clave)
Este nodo es vital para evitar guardar correos irrelevantes.
*   **Condition:** `IF`
*   **Logic:**
    ```
    $json.subject.includes('propuesta') OR $json.subject.includes('cotización')
    ```
    *Nota: Asegúrate de usar la propiedad exacta `subject` del objeto JSON que llega de Gmail.*
*   **Result:** Si es verdadero, el flujo pasa al siguiente nodo. Si es falso, se detiene.

#### 3. Nodo Function (Opcional pero recomendado)
Para asegurar que los datos estén limpios antes de enviarlos a Notion, puedes usar este nodo para formatear la fecha o unificar campos.
*   **Code:**
    ```javascript
    const email = $input.first().json;
    const asunto = email.subject;
    const remitente = email.from;
    const fecha = new Date().toISOString();

    return {
      json: {
        asunto: asunto,
        remitente: remitente,
        fecha: fecha
      }
    };
    ```

#### 4. Nodo Notion
*   **Operation:** `Create Page`
*   **Database:** Selecciona la base de datos de Notion donde quieres guardar los leads.
*   **Properties Mapping:**
    *   **Nombre del Lead:** Vincula el campo `asunto` o `remitente`.
    *   **Reunir Remitente:** Vincula el campo `remitente`.
    *   **Fecha:** Vincula el campo `fecha`.
    *   **Email:** Vincula el campo `from` de Gmail.
*   **Important:** Crea las credenciales de Notion en N8N y asegúrate de que la base de datos tenga los campos creados con antelación.

#### 5. Nodo Slack
*   **Operation:** `Send Message`
*   **Channel:** Elige el canal donde quieres la alerta (ej: `#leads-nuevos`).
*   **Message:**
    ```
    🚀 Nuevo Lead detectado:
    Asunto: {{ $json.asunto }}
    De: {{ $json.remitente }}
    Enviado a: Notion
    ```
*   **Important:** Configura las credenciales de Slack en N8N.

---

### ⚠️ Puntos Clave para el Éxito

1.  **Credenciales:** Antes de probar, configura las credenciales en la pestaña "Credentials" de N8N para **Gmail, Notion y Slack**.
2.  **Base de Datos en Notion:** Asegúrate de que tu base de datos en Notion tenga las propiedades (columnas) creadas y con el tipo de dato correcto (ej: "Fecha", "Texto", "Email").
3.  **Filtrado:** Si quieres que el filtro sea más estricto (ej: solo "propuesta" o "cotización" exactas), puedes usar la condición `equals` en lugar de `includes`.
4.  **Pruebas:**
    *   Envía un correo de prueba con el asunto "Propuesta de servicio" para validar el flujo.
    *   Envía otro con "Hola" para verificar que el filtro bloquea el flujo.

¿Te gustaría que te ayude con el código JSON del workflow para importarlo directamente en N8N?