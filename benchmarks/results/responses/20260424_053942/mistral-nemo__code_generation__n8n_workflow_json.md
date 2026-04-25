# Mistral Nemo — code_generation/n8n_workflow_json

- model_id: `mistralai/mistral-nemo`
- success: True  | final: 6.41 | quality: 6.04
- latency_total: 147.44s | tokens_per_second: 6.4
- input_tokens: 120 | output_tokens: 943
- judge_score: 2.6 | justificación: 

## Respuesta completa

Aquí te dejo el JSON completo del workflow:
```json
{
  "version": "2.0.0",
  "title": "Workflow N8N para clasificar y enviar emails a Slack",
  "description": "Este workflow se activa con un webhook POST, extrae el campo 'email' y 'message' del body, clasifica el mensaje usando un nodo de IA (OpenAI) y envía el email a un canal de Slack diferente según la clasificación.",
  "flow": {
    "nodes": [
      {
        "id": "webhook",
        "type": "httpRequest",
        "name": "Webhook",
        "properties": {
          "method": "POST",
          "url": "https://your-n8n-instance/webhook",
          "body": "application/json"
        }
      },
      {
        "id": "extractEmail",
        "type": "function",
        "name": "Extraer email",
        "function": {
          "name": "GetEmail",
          "arguments": {
            "input": "$.body.email"
          }
        },
        "settings": {
          "outputField": "email"
        }
      },
      {
        "id": "extractMessage",
        "type": "function",
        "name": "Extraer message",
        "function": {
          "name": "GetMessage",
          "arguments": {
            "input": "$.body.message"
          }
        },
        "settings": {
          "outputField": "message"
        }
      },
      {
        "id": "classifyMessage",
        "type": "aiTool",
        "name": "Clasificar mensaje",
        "properties": {
          "tool": "OpenAI",
          "model": "text-classification",
          "inputs": {
            "text": "$.message"
          },
          "output": "$.classification"
        },
        "settings": {
          "outputField": "classification"
        }
      },
      {
        "id": "sendToSupport",
        "type": "slack",
        "name": "Enviar a soporte",
        "properties": {
          "method": "post",
          "token": " YOUR_SLACK_TOKEN ",
          "channel": "#support",
          "text": "Nuevo mensaje de soporte de {{email}}:\n{{message}}"
        },
        "settings": {
          "condition": {
            "field": "$.classification",
            "operator": "equals",
            "value": "soporte"
          }
        }
      },
      {
        "id": "sendToSales",
        "type": "slack",
        "name": "Enviar a ventas",
        "properties": {
          "method": "post",
          "token": " YOUR_SLACK_TOKEN ",
          "channel": "#sales",
          "text": "Nuevo mensaje de ventas de {{email}}:\n{{message}}"
        },
        "settings": {
          "condition": {
            "field": "$.classification",
            "operator": "equals",
            "value": "ventas"
          }
        }
      },
      {
        "id": "sendToGeneral",
        "type": "slack",
        "name": "Enviar a general",
        "properties": {
          "method": "post",
          "token": " YOUR_SLACK_TOKEN ",
          "channel": "#general",
          "text": "Nuevo mensaje genérico de {{email}}:\n{{message}}"
        },
        "settings": {
          "condition": {
            "field": "$.classification",
            "operator": "equals",
            "value": "otro"
          }
        }
      }
    ],
    "edges": [
      {
        "from": "webhook",
        "to": "extractEmail"
      },
      {
        "from": "extractEmail",
        "to": "extractMessage"
      },
      {
        "from": "extractMessage",
        "to": "classifyMessage"
      },
      {
        "from": "classifyMessage",
        "to": "sendToSupport"
      },
      {
        "from": "classifyMessage",
        "to": "sendToSales"
      },
      {
        "from": "classifyMessage",
        "to": "sendToGeneral"
      }
    ]
  }
}
```
Ten en cuenta que debes reemplazar " YOUR\_SLACK\_TOKEN \