# Poolside Laguna XS 2.1 — multi_turn/requirements_change

- model_id: `poolside/laguna-xs-2.1`
- success: True  | final: 6.9 | quality: 6.0
- latency_total: 1.439s | tokens_per_second: 158.4
- input_tokens: 278 | output_tokens: 228

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

Entiendo el cambio. Ahora necesitamos:

1. **Gmail Trigger** (mismo que antes)
2. **Function node** para filtrar por palabras 'propuesta' o 'cotizacion' en el asunto, y extraer datos del remitente
3. **Notion node** para crear una nueva pagina con los datos
4. **Slack node** para enviar notificacion

Para el filtro, puedes usar un Function node con esta logica:
```javascript
const asunto = $json.subject.toLowerCase();
if (asunto.includes('propuesta') || asunto.includes('cotizacion')) {
  return {
    remitente: $json.from,
    asunto: $json.subject,
    fecha: $json.date,
    filtrado: true
  };
}
return { filtrado: false };
```

Luego conectar a Notion y Slack. ¿Te quedan dudas sobre la configuracion de alguno de estos nodos?