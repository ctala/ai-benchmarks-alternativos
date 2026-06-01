# Qwen 3.6 27B base (OpenRouter FP8) — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3.6-27b`
- success: True  | final: 6.81 | quality: 7.92
- latency_total: 36.08s | tokens_per_second: 56.8
- input_tokens: 125 | output_tokens: 2048
- judge_score: 3.8 | justificación: 

## Respuesta completa

The user wants an n8n workflow in JSON format that:
1. Activates with a webhook POST
2. Extracts "email" and "message" fields from the body
3. Uses an AI node (OpenAI) to classify the message as "soporte", "ventas", or "otro"
4. Based on the classification, sends the email to different Slack channels:
   - soporte -> #support
   - ventas -> #sales
   - otro -> #general

I need to create a complete n8n workflow JSON. Let me think about the structure:

1. Webhook node (POST method)
2. An AI agent or OpenAI node to classify the message
3. A Switch node to route based on classification
4. Three Slack nodes to send messages to different channels

Let me construct this properly. I'll use the current n8n JSON structure format.

For the OpenAI node, I'll use the "OpenAI" node with a prompt to classify the message. I need to make sure the output is parseable.

Let me think about the exact structure:

- Webhook: POST, path "classify-message", respond with JSON
- OpenAI (AI Agent or basic OpenAI node): I'll use the basic OpenAI node with a prompt
- Switch: Route based on the classification result
- Slack nodes: One for each channel

I'll use the n8n JSON schema structure with nodes and connections.

Let me build this carefully:

```json
{
  "name": "Clasificador de mensajes con IA",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "classify-message",
        "responseMode": "responseNode",
        "options": {}
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [250, 300]
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "options": {
          "temperature": 0
        },
        "prompt": {
          "value": "Clasifica el siguiente mensaje en una de estas categorías: 'soporte', 'ventas' o 'otro'. Solo responde con una de estas tres palabras, nada más.\n\nMensaje: {{ $json.message }}"
        }
      },
      "name": "OpenAI - Clasificar",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1,
      "position": [500, 300]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.output }}",
              "operation": "equals",
              "value2": "soporte"
            }
          ]
        }
      },
      "name": "Clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [750, 300]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "📧 Nuevo ticket de soporte\n\nDe: {{ $json.email }}\nMensaje: {{ $('Webhook').item.json.message }}"
      },
      "name": "Slack - Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1000, 150]
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "📧 Nuevo lead de ventas\n\nDe: {{ $json.email }}\nMensaje: {{ $('Webhook').item.json.message }}"
      },
      "name": "Slack - Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1000, 300]
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "📧 Mensaje general\n\nDe: {{ $json.email }}\nMensaje: {{ $('Webhook').item.json.message }}"
      },
      "name": "Slack - General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1000, 450]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "OpenAI - Clasificar",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI - Clasificar": {
      "main": [
        [
          {
            "node": "Clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificación": {
      "main": [
        [
          {
            "node": "Slack - Soporte",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - Ventas",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - General",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

Wait, I need to reconsider the structure. The Switch node in n8n has multiple outputs, and each output corresponds to a different condition. Let me revise the Switch node configuration to have three conditions.

Also, I should use the correct node types. Let me use the standard n8n nodes:
- Webhook: `n8n-nodes-base.webhook`
- OpenAI: `n8n-nodes-base.openAi` (basic OpenAI node) or `@n8n/n8n-nodes-langchain.openAi` for AI Agent
- Switch: `n8n-nodes-base.switch`
- Slack: `n8n-nodes-base.slack`

For the OpenAI node, I'll use a simpler approach with the basic OpenAI Chat node, which is more common.

Let me also make sure the Switch node has the correct structure for multiple outputs.

Actually, let me reconsider. The user wants a complete JSON workflow. I should make sure it's valid and can be imported directly into n8n.

Let me revise:

For the Switch node, I need to define three conditions for the three outputs. The structure should be:

```json
{
  "parameters": {
    "conditions": {
      "string": [
        {
          "value1": "={{ $json.output }}",
          "operation": "equals",
          "value2": "soporte"
        },
        {
          "value1": "={{ $json.output }}",
          "operation": "equals",
          "value2": "ventas"
        }
      ]
    }
  }
}
```

The third output would be the "default" case.

Also, I need to make sure the OpenAI node returns a clean output. Let me use a more robust prompt and maybe use JSON mode or parsing.

Let me also add a Set node to clean up the AI output before the Switch, to ensure it's trimmed and lowercase.

Actually, let me keep it simple but robust. I'll add a Set node to clean the output, and use the Switch node with proper conditions.

Let me also make sure the Slack nodes reference the correct data. The email and message come from the Webhook, so I should reference them properly.

Here's a revised version:

```json
{
  "name": "Clasificador de mensajes con IA",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "classify-message",
        "responseMode": "responseNode",
        "options": {}
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [250, 300]
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "options": {
          "temperature": 0
        },
        "prompt": {
          "value": "Clasifica el siguiente mensaje en una de estas categorías: 'soporte', 'ventas' o 'otro'. Solo responde con una de estas tres palabras, nada más.\n\nMensaje: {{ $json.message }}"
        }
      },
      "name": "OpenAI - Clasificar",
     