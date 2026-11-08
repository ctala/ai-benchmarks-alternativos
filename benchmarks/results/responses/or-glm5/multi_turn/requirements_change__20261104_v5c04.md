# GLM 5 — multi_turn/requirements_change

- model_id: `z-ai/glm-5`
- success: True  | final: 4.45 | quality: 4.0
- latency_total: 27.535s | tokens_per_second: 57.1
- input_tokens: 235 | output_tokens: 1573

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

¡Me encanta el cambio! Es un workflow excelente para automatizar la captación de clientes. Ahora tu flujo será: **Gmail ➔ Filtro (IF) ➔ Notion ➔ Slack**.

Aquí tienes el paso a paso para configurarlo en n8n:

### 1. Nodo Trigger: Gmail
* **Acción:** `On new email` (Se activa con cada correo nuevo).
* **Configuración:** 
  * Conecta tu cuenta de Gmail.
  * En "Label", puedes dejar `INBOX` o crear una etiqueta específica en Gmail (ej. "Clientes") y seleccionarla aquí para que el workflow se active solo con esos correos y ahorres procesamiento.

### 2. Nodo Filtro: IF
Aquí vamos a filtrar para que solo pasen los correos que te interesan.
* **Condition 1:** 
  * Value 1: `{{$json["subject"]}}` (Arrastra el asunto desde el nodo de Gmail).
  * Operation: `contains`
  * Value 2: `propuesta`
* **Lógica:** Cambia la condición a **OR**.
* **Condition 2:**
  * Value 1: `{{$json["subject"]}}`
  * Operation: `contains`
  * Value 2: `cotizacion`

*Tip pro:* Para no tener problemas con mayúsculas/minúsculas (ej. "Propuesta" vs "propuesta"), puedes usar esta expresión en el Value 1: `{{ $json.subject.toLowerCase() }}` y en el Value 2 escribir `propuesta`. Así filtra sin importar cómo lo hayan escrito.

### 3. Nodo Acción: Notion (Rama "True" del IF)
Solo llegará aquí si el asunto tenía las palabras clave.
* **Acción:** `Create a database page` (Crear una página en una base de datos).
* **Configuración:**
  * Conecta tu cuenta de Notion (necesitarás darle permisos a n8n para acceder a la base de datos).
  * **Database ID:** Selecciona la base de datos donde quieres guardar los leads (ej. "Propuestas y Cotizaciones").
  * **Properties (Propiedades):** Aquí mapeamos los datos. Asegúrate de que las columnas en Notion coincidan con esto:
    * *Title (Título):* `{{$json["subject"]}}` (El asunto del correo).
    * *Email:* `{{$json["from"]["address"]}}` (El email del remitente).
    * *Nombre:* `{{$json["from"]["name"]}}` (El nombre del remitente).
    * *Fecha:* `{{$json["date"]}}` (La fecha de recepción).

### 4. Nodo Acción: Slack (Después de Notion)
* **Acción:** `Send a message` (Enviar mensaje).
* **Configuración:**
  * Conecta tu cuenta de Slack (necesitarás el token de bot o las credenciales OAuth).
  * **Channel:** Selecciona el canal donde quieres recibir la alerta (ej. `#ventas` o tu canal de mensajes directos).
  * **Message:** Puedes usar HTML o texto plano. Te recomiendo algo dinámico así:
    ```text
    🚨 ¡Nueva solicitud de cotización/propuesta! 🚨
    *Cliente:* {{$json["from"]["name"]}} ({{$json["from"]["address"]}})
    *Asunto:* {{$json["subject"]}}
    Ya está guardada en Notion. ¡A revisar!
    ```

### Resumen de la conexión visual:
`Gmail Trigger` ➔ `IF` 
*(Rama True)* ➔ `Notion` ➔ `Slack`
*(Rama False)* ➔ (Se deja vacía, no hace nada con los correos que no coinciden).

¿Tienes ya creada la base de datos en Notion con esas columnas? Si necesitas ayuda configurando las credenciales de Slack o Notion, te lo explico sin problema.