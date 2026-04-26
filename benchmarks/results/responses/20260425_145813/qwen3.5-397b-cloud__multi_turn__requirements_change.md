# Qwen 3.5 397B (Ollama Cloud) — multi_turn/requirements_change

- model_id: `qwen3.5:397b-cloud`
- success: True  | final: 6.6 | quality: 5.56
- latency_total: 46.874s | tokens_per_second: 43.7
- input_tokens: 233 | output_tokens: 2048
- judge_score: 2.6 | justificación: 

## Respuesta completa

¡Excelente ajuste! Ese flujo es mucho más potente para gestionar leads o oportunidades de venta. Al moverlo a Notion tienes una base de datos más flexible y Slack te mantiene alerta en tiempo real.

Aquí tienes la arquitectura del workflow optimizada para N8N:

### 🏗️ Estructura del Workflow

1.  **Gmail Trigger** (Con filtro nativo)
2.  **Notion** (Crear página en Base de Datos)
3.  **Slack** (Enviar mensaje de alerta)

---

### ⚙️ Configuración Paso a Paso

#### 1. Nodo: Gmail Trigger
En lugar de leer todos los emails y filtrar luego, usaremos la query de búsqueda de Gmail para ahorrar ejecuciones.
*   **Event:** `New Email`
*   **Filter:** Usa la query de búsqueda de Gmail para filtrar antes de que entre al workflow.
    *   **Query:** `subject:(propuesta OR cotizacion) is:unread`
    *   *Nota: `is:unread` evita procesar el mismo email twice si el workflow se reinicia.*
*   **Download Attachments:** `No` (a menos que necesites los adjuntos, esto aligera la carga).
*   **Simple:** `No` (para tener acceso a headers completos si los necesitas).

#### 2. Nodo: Notion
*   **Resource:** `Database`
*   **Operation:** `Create`
*   **Database ID:** El ID de la base de datos donde quieres guardar los leads (lo sacas de la URL de Notion).
*   **Properties (Mapeo):**
    *   **Nombre (Title):** `{{ $json["from"] }}` (o extraer solo el nombre si usas un nodo Function intermedio).
    *   **Email (Email):** `{{ $json["from"] }}`
    *   **Asunto (Text):** `{{ $json["subject"] }}`
    *   **Fecha (Date):** `{{ $json["date"] }}`
    *   **Estado (Select):** `Nuevo` (Valor fijo).
    *   **Link Email (Url):** `https://mail.google.com/mail/u/0/#inbox/{{ $json["messageId"] }}` (Para ir directo al correo).

#### 3. Nodo: Slack
*   **Resource:** `Channel`
*   **Operation:** `Post`
*   **Channel:** Selecciona el canal de ventas o alertas.
*   **Text:** Usa un mensaje formateado con *mrkdwn*:
    ```text
    🚨 *Nueva Oportunidad Detectada*
    *Asunto:* {{ $json["subject"] }}
    *Remitente:* {{ $json["from"] }}
    *Fecha:* {{ $json["date"] }}
    _Revisado en Notion_
    ```

---

### 📋 Prerrequisitos Importantes

1.  **Base de Datos en Notion:**
    *   Crea una Database en Notion antes de configurar el nodo.
    *   Asegúrate de que las columnas (Properties) coincidan con lo que quieres mapear (ej. una columna tipo "Email", otra tipo "Title", etc.).
    *   **Importante:** Ve a la configuración de la integración de Notion en tu cuenta y dale acceso ("Invite") a esa base de datos específica, sino N8N no podrá escribir en ella.

2.  **Permisos de Gmail:**
    *   Asegúrate de que las credenciales de OAuth2 en N8N tengan los scopes necesarios para leer mensajes (`.../gmail.readonly`).

3.  **Slack:**
    *   Necesitas un Bot de