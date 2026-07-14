# Qwen 3.5 397B — multi_turn/requirements_change

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 5.76 | quality: 6.0
- latency_total: 37.712s | tokens_per_second: 54.3
- input_tokens: 233 | output_tokens: 2048
- judge_score: 2.0 | justificación: La respuesta no aborda los requisitos originales de usar Google Sheets, en su lugar introduce Notion y Slack, lo que la hace irrelevante para la tarea solicitada.

## Respuesta completa

¡Excelente ajuste! Esa combinación (Gmail + Notion + Slack) es mucho más potente para gestionar leads o oportunidades comerciales. Notion te sirve como CRM ligero y Slack te mantiene alerta en tiempo real.

Aquí tienes la estructura optimizada del workflow en N8N:

### 🏗️ Estructura del Workflow

1.  **Gmail Trigger** (Disparador)
2.  **Filter** (Filtro de palabras clave)
3.  **Notion** (Crear página en base de datos)
4.  **Slack** (Enviar mensaje de alerta)

---

### ⚙️ Configuración Paso a Paso

#### 1. Gmail Trigger Node
*   **Event:** `New Email`
*   **Credential:** Conecta tu cuenta de Google (OAuth2).
*   **Opción recomendada:** En el campo **Query**, puedes poner `subject:(propuesta OR cotización)` para que Gmail ya te entregue solo los correos relevantes. Esto ahorra operaciones.
    *   *Alternativa:* Si prefieres verlo visualmente en el canvas, deja el query vacío y usa el nodo **Filter** después.

#### 2. Filter Node (Si no usaste el Query de Gmail)
*   **Condition:** `String` → `Contains` (o `Matches Regex` para ser más exacto).
*   **Logic:** `OR` (Cualquiera de las condiciones).
    *   Condition 1: `Subject` contains `propuesta` (Case insensitive).
    *   Condition 2: `Subject` contains `cotización` (Case insensitive).
*   *Nota:* Si usaste el Query en el Trigger, puedes saltar este nodo.

#### 3. Notion Node
*   **Resource:** `Page`
*   **Operation:** `Create`
*   **Database ID:** Necesitas el ID de la base de datos donde quieres guardar los leads (está en la URL de la base de datos en Notion).
*   **Mapping de Propiedades:**
    *   **Name (Title):** Mapea el `Subject` del email.
    *   **Remitente (Rich Text o Email):** Mapea `From` (email del sender).
    *   **Fecha (Date):** Mapea `Date` del email.
    *   **Enlace (URL):** Mapea el `Link` del email para abrirlo directo desde Notion.
*   *Importante:* Asegúrate de que en tu Base de Datos de Notion las columnas tengan los tipos correctos (Title, Email, Date, etc.) antes de configurar el nodo.

#### 4. Slack Node
*   **Resource:** `Message`
*   **Operation:** `Post`
*   **Channel:** El ID del canal (ej. `#leads`) o el ID directo (empieza con `C0...`).
*   **Text:** Un mensaje claro, ej:
    ```
    🚨 Nueva Oportunidad Detectada
    *Asunto:* {{ $json.subject }}
    *Cliente:* {{ $json.from }}
    *Ver en Gmail:* {{ $json.link }}
    ```

---

### 💡 Consejos de Experto para Emprendedores

1.  **Permisos de Notion:** No olvides ir a tu integración de Notion (en la web de Notion > My Integrations) y darle acceso ("Connect to") a la base de datos específica donde quieres guardar los datos. Si no, N8N dará error 403.
2.  **Slack Channel ID:** Para obtener el ID de un canal, pasa el mouse sobre el nombre del canal