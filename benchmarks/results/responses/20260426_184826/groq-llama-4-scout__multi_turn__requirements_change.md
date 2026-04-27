# Llama 4 Scout 17B (Groq preview) — multi_turn/requirements_change

- model_id: `meta-llama/llama-4-scout-17b-16e-instruct`
- success: True  | final: 6.96 | quality: 6.04
- latency_total: 2.18s | tokens_per_second: 246.3
- input_tokens: 230 | output_tokens: 537
- judge_score: 3.0 | justificación: 

## Respuesta completa

Genial, podemos adaptar el workflow para que se ajuste a tus nuevas necesidades.

Aquí te presento la configuración de cada nodo:

**1. Gmail Trigger**

* **Trigger Type**: New Email
* **Mailbox**: Selecciona la bandeja de entrada de Gmail que deseas monitorear
* **Filter**: Puedes dejar vacío este campo, pero más adelante vamos a agregar un filtro en el workflow

**2. Filter**

* **Type**: Function
* **Operation**: Filter
* **Code**:
```javascript
const asunto = items[0].json.asunto.toLowerCase();
const palabrasClave = ['propuesta', 'cotizacion'];
const incluyePalabraClave = palabrasClave.some(palabra => asunto.includes(palabra));

if (incluyePalabraClave) {
  return true;
} else {
  return false;
}
```
Este código verifica si el asunto del email contiene alguna de las palabras clave 'propuesta' o 'cotizacion' (sin distinguir mayúsculas y minúsculas).

**3. Extraer datos**

* **Type**: Function
* **Operation**: Extract
* **Code**:
```javascript
const remitente = items[0].json.from;
const asunto = items[0].json.asunto;
const fecha = items[0].json.date;

const datos = {
  remitente,
  asunto,
  fecha
};

return datos;
```
Este código extrae los datos del remitente, asunto y fecha del email.

**4. Notion**

* **Type**: Notion
* **Operation**: Create Page
* **Database ID**: Selecciona la base de datos de Notion donde deseas agregar la información
* **Properties**:
	+ **Remitente**: Texto (selecciona el campo "Remitente" creado anteriormente)
	+ **Asunto**: Texto (selecciona el campo "Asunto" creado anteriormente)
	+ **Fecha**: Fecha (selecciona el campo "Fecha" creado anteriormente)

**5. Slack Notification**

* **Type**: Slack
* **Operation**: Send Message
* **Channel**: Selecciona el canal de Slack donde deseas enviar la notificación
* **Message**:
```markdown
Nuevo email recibido!
* Remitente: {{ $json.remitente }}
* Asunto: {{ $json.asunto }}
* Fecha: {{ $json.fecha }}
```
Este mensaje enviará una notificación a Slack con la información del email.

**Flujo del workflow**

1. Gmail Trigger → Filter → Extraer datos → Notion → Slack Notification

Recuerda configurar cada nodo con tus credenciales y ajustes correspondientes. ¡Listo!