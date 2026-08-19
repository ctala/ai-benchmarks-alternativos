# DeepSeek V3.2 — multi_turn/requirements_change

- model_id: `deepseek/deepseek-chat`
- success: True  | final: 6.22 | quality: 6.0
- latency_total: 13.043s | tokens_per_second: 36.6
- input_tokens: 242 | output_tokens: 478
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una estructura detallada que un emprendedor podría usar directamente, aunque la profundidad podría mejorarse con más detalles sobre la configuración de credenciales.

## Respuesta completa

¡Perfecto! Aquí tienes el diseño del workflow en N8N con las modificaciones solicitadas:

**Workflow mejorado:**
1. **Trigger**: 
   - *Gmail Trigger* (configurado para revisar emails nuevos)

2. **Filtro**:
   - *IF Node* para verificar si el asunto contiene "propuesta" o "cotización" (usando una expresión como):
     ```javascript
     ['propuesta', 'cotizacion', 'cotización'].some(word => 
       $input.all()[0].json.subject.toLowerCase().includes(word.toLowerCase())
     )
     ```

3. **Procesamiento**:
   - *Function Node* para extraer:
     ```javascript
     return {
       senderName: $input.all()[0].json.from.split('<')[0].trim(),
       senderEmail: $input.all()[0].json.from.match(/<(.+)>/)[1],
       subject: $input.all()[0].json.subject,
       date: $input.all()[0].json.date,
       bodyPreview: $input.all()[0].json.textPlain.substring(0, 200)
     };
     ```

4. **Notion**:
   - *Notion Node* (Create Database Item) mapeando los campos a tu base de datos en Notion

5. **Notificación**:
   - *Slack Node* para enviar mensaje con formato:
     ```
     📬 Nueva propuesta recibida:
     *De*: {{senderName}} ({{senderEmail}})
     *Asunto*: {{subject}}
     *Fragmento*: {{bodyPreview}}...
     ```

**Configuraciones clave:**
- En el nodo de Gmail: activar "Only Messages" y "Mark as Read"
- En el nodo IF: conectar el "true" a Notion/Slack y el "false" a un nodo de "no hacer nada"
- En Notion: necesitarás el ID de tu database y mapear los campos correctamente
- En Slack: configurar el webhook y el canal destino

¿Quieres que profundice en algún nodo en particular o necesitas ayuda con la configuración de las credenciales para Notion/Slack?