# Llama 3.3 70B — multi_turn/requirements_change

- model_id: `meta-llama/llama-3.3-70b-instruct`
- success: True  | final: 8.0 | quality: 8.0
- latency_total: 3.957s | tokens_per_second: 82.6
- input_tokens: 248 | output_tokens: 327

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

Genial, podemos adaptar el workflow para que se ajuste a tus nuevos requisitos. Aquí te presento los pasos actualizados:

1. **Trigger**: Gmail Trigger (se activa con cada email nuevo)
2. **Filtro**: Function node para filtrar emails con 'propuesta' o 'cotizacion' en el asunto
3. **Extraer datos**: Function node para parsear remitente, asunto, fecha
4. **Guardar**: Notion node para agregar una página con los datos
5. **Notificación**: Slack node para enviar una notificación cuando se reciba un email que cumpla con los criterios de filtro

En el Function node de filtro, podemos utilizar una expresión regular para buscar las palabras 'propuesta' o 'cotizacion' en el asunto del email. Si se encuentra alguna de estas palabras, el workflow continuará; de lo contrario, se detendrá.

En el Notion node, debemos configurar la base de datos y la página que se creará con los datos del email. También debemos asegurarnos de que el formato de los datos sea compatible con la estructura de la base de datos de Notion.

En el Slack node, podemos personalizar el mensaje de notificación para que incluya los datos relevantes del email, como el remitente, el asunto y la fecha.

¿Quieres que te proporcione más detalles sobre la configuración de cada nodo o prefieres que te proporcione un ejemplo de workflow que puedas importar en N8N?