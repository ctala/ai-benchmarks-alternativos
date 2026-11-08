# DeepSeek V4 Pro — multi_turn/requirements_change

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 4.69 | quality: 4.0
- latency_total: 5.779s | tokens_per_second: 50.5
- input_tokens: 245 | output_tokens: 292

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

Claro, entendido. El workflow queda así:

1. **Gmail Trigger** — se activa con cada email nuevo
2. **IF Node** — filtra si el asunto contiene `propuesta` o `cotización`
3. **Notion** — guarda los datos
4. **Slack** — notifica al canal que elijas

La lógica del IF sería con condición `String contains` y un `OR` entre los dos términos. ¿Querés que te pase el JSON del workflow o prefieres que te guíe paso a paso en N8N?

También decime:
- ¿Ya tenés la base de Notion con las propiedades creadas?
- ¿Qué canal de Slack y qué mensaje te gustaría?