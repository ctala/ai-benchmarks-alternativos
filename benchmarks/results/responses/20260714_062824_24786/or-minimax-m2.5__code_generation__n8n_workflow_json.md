# MiniMax M2.5 — code_generation/n8n_workflow_json

- model_id: `minimax/minimax-m2.5`
- success: True  | final: 7.77 | quality: 8.6
- latency_total: 30.044s | tokens_per_second: 68.2
- input_tokens: 157 | output_tokens: 2048
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, proporcionando un JSON completo para el workflow de N8N que cumple con los requisitos especificados. La estructura es clara y organizada, y es prácticamente útil para un emprendedor, aunque no ofrece insights adicionales más allá de la implementación básica.

## Respuesta completa

Aquí tienes el JSON completo del workflow para N8N.

### Instrucciones de uso:
1.  Copia el código JSON abaixo.
2.  Ve a tu instancia de N8N.
3.  Haz clic en el menú (tres líneas arriba a la izquierda) -> **Importar**.
4.  Pega el JSON y haz clic en "Importar Workflow".
5.  **Importante:** Deberás configurar las credenciales:
    *   Haz doble clic en el nodo **OpenAI** y conecta tu API Key de OpenAI.
    *   Haz doble clic en los nodos de **Slack** y conecta tu cuenta de Slack.

### JSON del Workflow

```json
{
  "name": "Clasificador de Mensajes con IA y Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificador-mensajes",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "webhook-trigger",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 300],
      "webhookId": "clasificador-webhook"
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "messages": [
          {
            "role": "system",
            "content": "Eres un asistente que clasifica mensajes de clientes. Debes responder ÚNICAMENTE con una palabra en minúsculas: 'soporte', 'ventas' u 'otro'. No escribas puntuación, solo la palabra."
          },
          {
            "role": "user",
            "content": "Clasifica el siguiente mensaje del usuario: {{ $json.body.message }}"
          }
        ],
        "options": {
          "temperature": 0
        }
      },
      "id": "ai-classifier",
      "name