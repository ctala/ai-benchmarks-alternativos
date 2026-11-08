# Solar Pro 4 — multi_turn/requirements_change

- model_id: `upstage/solar-pro4`
- success: True  | final: 4.83 | quality: 4.0
- latency_total: 13.589s | tokens_per_second: 38.5
- input_tokens: 293 | output_tokens: 523

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

Entendido, ese flujo es más completo pero muy útil. Aquí te va la estructura:

**Nodos del workflow:**

1. **Gmail Trigger**  
   - Configura para leer correos nuevos.  
   - Opcional: filtra directamente en el trigger si tu versión lo permite, pero es más seguro hacerlo después.

2. **Filter Node**  
   - Condición: `{{ $json.subject }}` contiene "propuesta" O "cotizacion"  
   - Usa Case-insensitive para no discriminar mayúsculas.

3. **Function Node (o Code Node)**  
   - Extrae los datos que necesitas de `$json`:  
     - Remitente (nombre o email)  
     - Asunto  
     - Fecha  
     - Cuerpo (si lo necesitas)  
   - Devuelve un objeto limpio para pasarlo a Notion.

4. **Notion Node**  
   - Usa el método "Create Page" o "Append to Database" según cómo tengas tu base de datos.  
   - Mapea los campos:  
     - Propiedad de email → email del remitente  
     - Propiedad de asunto → asunto  
     - Propiedad de fecha → fecha del email  
     - Opcional: cuerpo del mensaje en un campo de texto largo.

5. **Slack Node**  
   - Usa "Send Message" a un canal o DM.  
   - Mensaje sugerido:  
     ```
     Nueva propuesta/cotización de {{ remitente }}  
     Asunto: {{ asunto }}  
     Fecha: {{ fecha }}
     ```  
   - Opcional: puedes agregar un link al email o a la página de Notion si la creaste.

**Consideraciones:**

- **Notion**: necesitas una base de datos con propiedades que coincidan (email, texto, fecha). Si usas una página libre, mapea el title y el body.
- **Slack**: necesitas un token de bot con permisos para escribir en el canal.
- **Filtro**: si usas Gmail Trigger, también puedes configurar una consulta de Gmail directamente (`subject:(propuesta OR cotizacion)`) para reducir procesamiento, pero el filter node da más control.

¿Quieres que te pase un ejemplo de la estructura del JSON que debería salir del Function Node para que lo mapees fácil a Notion?