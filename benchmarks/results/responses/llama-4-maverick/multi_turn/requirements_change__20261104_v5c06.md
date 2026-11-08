# Llama 4 Maverick — multi_turn/requirements_change

- model_id: `meta-llama/llama-4-maverick`
- success: True  | final: 5.2 | quality: 4.0
- latency_total: 2.695s | tokens_per_second: 86.8
- input_tokens: 230 | output_tokens: 234

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

Excelente elección! Notion es una herramienta muy versátil.

Te propongo el siguiente workflow:

1. **Trigger**: Gmail Trigger (se activa con cada email nuevo)
2. **Filtro**: IF node para filtrar emails con 'propuesta' o 'cotizacion' en el asunto
3. **Extraer datos**: Function node para parsear remitente, asunto, fecha
4. **Notion**: Notion node para crear una nueva página con los datos extraídos
5. **Notificación**: Slack node para enviar una notificación cuando llegue un email que pase el filtro

Para el IF node, puedes usar la siguiente condición:
```
{{$json["subject"]}} contains "propuesta" || {{$json["subject"]}} contains "cotizacion"
```
Esto verificará si el asunto del email contiene alguna de esas palabras.

En el Notion node, deberás configurar la conexión con tu cuenta de Notion y especificar la página y los campos que deseas crear.

En el Slack node, puedes personalizar el mensaje de notificación con los datos del email.

¿Quieres que te ayude con la configuración de alguno de estos nodos?