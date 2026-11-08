# Tencent Hy3 — multi_turn/requirements_change

- model_id: `tencent/hy3`
- success: True  | final: 5.94 | quality: 6.0
- latency_total: 33.18s | tokens_per_second: 50.0
- input_tokens: 260 | output_tokens: 1658

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

¡Cambio de planes perfecto! N8N es muy flexible para eso. 

Aquí tienes la estructura del nuevo workflow para lograr exactamente lo que pides: **Gmail → Filtro (Propuesta/Cotización) → Notion + Slack**.

### 1. Estructura del Workflow (Nodos)
1. **Gmail Trigger** (Disparador)
2. **IF** (Filtro de asunto)
3. **Notion** (Guardar datos)
4. **Slack** (Notificación)

Ambos (Notion y Slack) deben conectarse a la salida "true" del nodo IF.

---

### 2. Configuración paso a paso

#### 📥 Nodo 1: Gmail Trigger
*   **Credential:** Tu cuenta de Gmail conectada.
*   **Event:** `Message Received` (Mensaje recibido).
*   **Simplify:** Actívado (esto te da campos limpios como `subject`, `from`, `fromEmail`, `date`).
*   *Nota:* Puedes configurar el polling (ej. cada 1 minuto) según tu plan de Gmail.

#### 🔍 Nodo 2: IF (Filtro)
Arrastra un nodo **IF** y conéctalo al Gmail Trigger. En la pestaña "Conditions", selecciona **Expression** y usa este código para detectar ambas palabras (ignorando mayúsculas/minúsculas):
```javascript
{{ 
  $json.subject.toLowerCase().includes('propuesta') || 
  $json.subject.toLowerCase().includes('cotizacion') 
}}
```
*   La salida **true** irá a Notion y Slack.
*   La salida **false** puedes dejarla sin conectar (se ignoran los demás correos).

#### 📝 Nodo 3: Notion
Conéctalo a la salida "true" del IF.
*   **Credential:** Token de integración de Notion (debes crear una integración en Notion y compartir tu BD con ella).
*   **Resource:** `Database Page`
*   **Operation:** `Create`
*   **Database ID:** Pega el ID de tu base de datos de Notion.
*   **Properties:** Mapea los campos según tu base de datos. Ejemplo:
    *   **Nombre/Title:** `{{ $json.subject }}` (o el nombre del remitente)
    *   **Email del Remitente:** `{{ $json.fromEmail }}`
    *   **Remitente (Nombre):** `{{ $json.from }}`
    *   **Fecha:** `{{ $json.date }}`

#### 💬 Nodo 4: Slack
Conéctalo también a la salida "true" (puedes ponerlo después de Notion o en paralelo).
*   **Credential:** API de Slack.
*   **Resource:** `Message`
*   **Operation:** `Send`
*   **Channel:** El canal donde quieres recibir la alerta (ej. `#ventas`).
*   **Text:** Usa algo como:
```text
🚨 Nuevo email importante recibido:
De: {{ $json.from }} ({{ $json.fromEmail }})
Asunto: {{ $json.subject }}
```

---

### 3. Consejos Pro-Técnicos para Emprendedores
1. **Credenciales Notion:** Recuerda que en Notion debes ir a "Connections" en tu base de datos y autorizar la integración que creaste en [notion.so/my-integrations](https://www.notion.so/my-integrations).
2. **Probabilidad de errores:** Si el `fromEmail` a veces viene como `undefined` en el trigger de Gmail, usa una expresión de respaldo: `{{ $json.fromEmail || $json.from }}`.
3. **Acentos:** Si quieres ser súper preciso y también captar "cotización" con tilde, agrega otra condición OR en el IF: `.includes('cotización')`.

¿Quieres que te genere el JSON de importación de este workflow para que lo cargues directamente en tu N8N?