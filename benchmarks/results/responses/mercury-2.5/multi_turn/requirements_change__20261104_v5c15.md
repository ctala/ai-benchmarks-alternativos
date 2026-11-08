# Mercury 2.5 — multi_turn/requirements_change

- model_id: `inception/mercury-2.5`
- success: True  | final: 6.73 | quality: 6.0
- latency_total: 4.585s | tokens_per_second: 334.6
- input_tokens: 236 | output_tokens: 1534

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



Entendido. Aquí está la estructura ajustada:

1.  **Gmail Trigger**: Configura para revisar mensajes nuevos.
2.  **Nodo IF**: Filtra por asunto usando una expresión. Sugiero usar `toLowerCase()` para capturar mayúsculas y minúsculas.
3.  **Notion Node**: Guarda los datos en tu base de datos (remitente, asunto, fecha).
4.  **Slack Node**: Notifica al canal cuando se cumple el filtro.

Conecta Notion y Slack en paralelo tras el filtro. ¿Quieres que detalle la expresión lógica para el asunto?