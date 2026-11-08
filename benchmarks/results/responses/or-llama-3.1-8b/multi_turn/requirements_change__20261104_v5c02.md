# Llama 3.1 8B Instant — multi_turn/requirements_change

- model_id: `meta-llama/llama-3.1-8b-instruct`
- success: True  | final: 5.35 | quality: 4.0
- latency_total: 2.171s | tokens_per_second: 134.0
- input_tokens: 249 | output_tokens: 291

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

Entendido, con N8N puedes enviar datos a Notion y enviar notificaciones a Slack. Aquí te dejo el workflow actualizado:

1. **Trigger**: Gmail Trigger (se activa con cada email nuevo)
	* Configuración: Filtro de asunto con "propuesta" o "cotización"
2. **Filtro**: Filtro de texto para asegurarse de que el email tenga "propuesta" o "cotización" en el asunto
3. **Extraer datos**: Function node para extraer los siguientes campos:
	* Nombre del remitente
	* Email del remitente
	* Asunto
	* Fecha
4. **Notificación**: Slack node para enviar una notificación cuando llegue un nuevo email que cumpla con el filtro
	* Configuración: Canal de Slack, mensaje personalizado
5. **Enviar datos a Notion**: Notion node para enviar los datos a Notion
	* Configuración: Base de datos de Notion, página o tabla donde se guardarán los datos

Recuerda que necesitarás crear una base de datos en Notion con los campos que deseas guardar (nombre del remitente, email del remitente, asunto y fecha) y un canal de Slack configurado en N8N.

¿Quieres que te detalle la configuración de cada nodo?