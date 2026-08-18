# Gemini 3.7 Flash — code_generation/n8n_workflow_json

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 7.78 | quality: 8.6
- latency_total: 13.005s | tokens_per_second: 157.2
- input_tokens: 115 | output_tokens: 2044
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del workflow de N8N con un JSON bien estructurado. Aunque la profundidad es adecuada, podría incluir más detalles sobre la configuración de credenciales o manejo de errores para mejorar la utilidad práctica.

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

Aquí tienes el JSON completo del workflow listo para copiar e importar en n8n.

### Cómo importarlo en n8n:
1. En n8n, crea un nuevo workflow.
2. Abre el menú de opciones (los tres puntos `...` arriba a la derecha) y selecciona **Import from JSON** (o pega el JSON directamente en el lienzo usando `Ctrl + V` / `Cmd + V`).
3. Configura tus credenciales para **OpenAI** y **Slack**.
4. Activa el workflow.

```json
{
  "name": "Clasificador de Mensajes IA a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "options": {}
      },
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        0,
        0
      ],
      "id": "webhook-trigger",
      "name": "Webhook"
    },
    {
      "parameters": {
        "modelId": {
          "__rl": true,
          "value": "gpt-4o-mini",
          "mode": "list",
          "cachedResultName": "gpt-4o-mini"
        },
        "messages": {
          "values": [
            {
              "content": "Eres un clasificador de mensajes estricto. Clasifica el mensaje del usuario en exactamente una de estas tres categorías: 'soporte', 'ventas' o 'otro'.\nResponde ÚNICAMENTE con una de esas tres palabras en minúsculas, sin puntos ni texto adicional.",
              "role": "system"
            },
            {
              "content": "={{ $json.body.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0
        }
      },
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "type