# Claude Sonnet 5 — code_generation/n8n_workflow_json

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 5.84 | quality: 6.3
- latency_total: 19.938s | tokens_per_second: 102.7
- input_tokens: 175 | output_tokens: 2048
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante, pero carece de detalles específicos y profundidad en la configuración del JSON.

## Entrada exacta (lo que recibió el modelo)

**user:**

Genera un workflow de N8N en JSON que:
1. Se active con un webhook POST
2. Extraiga el campo "email" y "message" del body
3. Use un nodo de IA (OpenAI) para clasificar el mensaje como "soporte", "ventas" o "otro"
4. Segun la clasificacion, envie el email a un canal de Slack diferente:
   - soporte -> #support
   - ventas -> #sales
   - otro -> #general

Dame el JSON completo del workflow.


## Respuesta completa

Estoy diseñando un flujo completo en n8n que captura datos a través de un webhook, extrae información del mensaje, usa OpenAI para clasificar el contenido, y luego enruta la respuesta a diferentes canales de Slack según la clasificación.

Voy a estructurar el JSON con los nodos necesarios: webhook como trigger inicial, un nodo para extraer los campos de email y mensaje, OpenAI para la clasificación, un nodo Switch para el enrutamiento condicional, y tres nodos Slack separados para cada canal destino. Necesito asegurarme de usar los tipos correctos de nodos de n8n y configurar los parámetros adecuados para cada uno.

Construyendo el JSON... Voy a agregar un nodo Set después de OpenAI para extraer y normalizar la clasificación en un campo "category", limpiando el contenido con trim y lowercase. Luego el Switch node usará ese campo normalizado para enrutar hacia las tres opciones. Estoy definiendo la estructura completa del workflow con los nodos conectados: Webhook, extracción de campos, clasificación con OpenAI, normalización, y el Switch para las rutas.

Escribiendo el JSON del workflow... Writing OpenAI node config...…