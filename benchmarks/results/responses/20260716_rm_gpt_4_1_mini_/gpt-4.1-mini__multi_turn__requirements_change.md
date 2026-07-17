# GPT-4.1 Mini — multi_turn/requirements_change

- model_id: `gpt-4.1-mini`
- success: True  | final: 6.17 | quality: 6.0
- latency_total: 5.326s | tokens_per_second: 96.3
- input_tokens: 225 | output_tokens: 513
- judge_score: 3.0 | justificación: La respuesta es precisa y clara, pero no cumple con el requisito original de guardar los datos en un Google Sheet, en su lugar, guarda en Notion, lo que afecta la relevancia y coherencia contextual.

## Respuesta completa

Perfecto, te armo el flujo actualizado con esos requisitos:

### Flujo general:

1. **Gmail Trigger**: Detecta emails nuevos
2. **Filtrado**: Un nodo IF que verifica si el asunto contiene "propuesta" o "cotizacion" (case insensitive)
3. **Extraer datos**: Nodo Function para extraer nombre, email, asunto, fecha
4. **Guardar en Notion**: Nodo Notion para crear una página o entrada con los datos extraídos
5. **Notificación en Slack**: Nodo Slack para enviarte un mensaje notificando la llegada del email filtrado

---

### Paso a paso en N8N:

1. **Gmail Trigger**  
   - Configura la conexión con tu cuenta Gmail  
   - Opcional: configura para que solo traiga emails nuevos desde el momento que se activa

2. **IF Node**  
   - Condición:  
     - `{{$json["subject"].toLowerCase().includes("propuesta") || $json["subject"].toLowerCase().includes("cotizacion")}}`  
   - Solo continúa si es true

3. **Function Node** (Extraer datos)  
   Código ejemplo:  
   ```javascript
   return items.map(item => {
     const from = item.json.from;
     // El campo from suele venir como "Nombre <email>", parseamos:
     const match = from.match(/(.*) <(.*)>/);
     const nombre = match ? match[1] : from;
     const email = match ? match[2] : "";
     return {
       json: {
         nombre,
         email,
         asunto: item.json.subject,
         fecha: item.json.date,
       }
     }
   });
   ```

4. **Notion Node**  
   - Configura conexión con tu cuenta Notion (requiere token y base de datos)  
   - Acción: Crear una nueva página o entrada  
   - Mapear los campos: nombre, email, asunto, fecha a las propiedades de la base de datos Notion

5. **Slack Node**  
   - Configura conexión con Slack (token, canal)  
   - Mensaje ejemplo:  
     `"Nuevo email filtrado de *{{ $json.nombre }}* ({{ $json.email }}) con asunto: *{{ $json.asunto }}*"`

---

Si quieres, puedo ayudarte configurando cada nodo con más detalle o con ejemplos JSON para importar el workflow. ¿Quieres?