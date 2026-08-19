# Nemotron 3.5 Lightning — code_generation/n8n_workflow_json

- model_id: `nvidia/nemotron-3.5-lightning`
- success: True  | final: 7.48 | quality: 8.0
- latency_total: 12.663s | tokens_per_second: 646.9
- input_tokens: 133 | output_tokens: 8192
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, proporcionando un workflow JSON funcional que cumple con los requisitos especificados, con una estructura bien organizada y utilidad práctica para un emprendedor.

## Respuesta completa

Here is a complete, valid n8n workflow JSON that fulfills all your requirements:

```json
{
  "name": "Email Classification & Slack Routing",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "email-webhook"
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [100, 300]
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "prompt": "Classify the following message as one of these categories only: soporte, ventas, otro. Return only the category name, nothing else. Message: {{ $json[\"message\"] }}",
        "temperature": 0
      },
      "name": "Classify Message",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [300, 300]
    },
    {
      "parameters": {
        "values": [
          {
            "name": "category",
            "value": "{{ $json.text }}"
          }
        ]
      },
      "name": "Set Category",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [500, 300]
    },
    {
      "parameters": {
        "conditions": {
          "boolean": [
            {
              "value1": "={{ $json[\"category\"] }}",
              "operation": "equal",
              "value2": "soporte"
            },
            {
              "value1": "={{ $json[\"category\"] }}",
              "operation": "equal",
              "value2": "ventas"
            },
            {
              "value1": "={{ $json[\"category\"] }}",
              "operation": "equal",
              "value2": "otro"
            }
          ]
        }
      },
      "name": "Router",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [700, 300]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "Nuevo ticket de soporte:\nEmail: {{ $json[\"email\"] }}\nMensaje: {{ $json[\"message\"] }}"
      },
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [900, 100]
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "Nueva consulta de ventas:\nEmail: {{ $json[\"email\"] }}\nMensaje: {{ $json[\"message\"] }}"
      },
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [900, 200]
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "Mensaje general:\nEmail: {{ $json[\"email\"] }}\nMensaje: {{ $json[\"message\"] }}"
      },
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [900, 300]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Classify Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Classify Message": {
      "main": [
        [
          {
            "node": "Set Category",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set Category": {
      "main": [
        [
          {
            "node": "Router",
            "type": "main",
