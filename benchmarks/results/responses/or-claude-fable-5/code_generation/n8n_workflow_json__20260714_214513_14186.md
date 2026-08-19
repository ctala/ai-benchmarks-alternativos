# Claude Fable 5 — code_generation/n8n_workflow_json

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 6.65 | quality: 8.12
- latency_total: 26.599s | tokens_per_second: 77.0
- input_tokens: 175 | output_tokens: 2048
- judge_score: 3.8 | justificación: 

## Respuesta completa

# Workflow N8N: Clasificador de Mensajes con IA

Aquí tienes el JSON completo. Puedes importarlo directamente en n8n con **Workflow → Import from File/Clipboard**:

```json
{
  "name": "Clasificador de Mensajes con IA a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "a1b2c3d4-0001-4000-8000-000000000001",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [0, 0],
      "webhookId": "clasificar-mensaje"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "field-email",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "field-message",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "a1b2c3d4-0002-4000-8000-000000000002",
      "name": "Extraer Datos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [220, 0]
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
              "content": "Eres un clasificador de mensajes. Clasifica el mensaje del usuario en una de estas tres categorias exactas: soporte, ventas, otro. Responde UNICAMENTE con una de esas tres palabras en minusculas, sin puntuacion ni texto adicional.",
              "role": "system"
            },
            {
              "content": "={{ $json.message }}",
              "role": "user"
            }
          ]
        },
        "options": {
          "temperature": 0
        }
      },
      "id": "a1b2c3d4-0003-4000-8000-000000000003",
      "name": "Clasificar con OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [440, 0],
      "credentials": {
        "openAiApi": {
          "id": "REEMPLAZAR_CREDENCIAL_OPENAI",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "cond-soporte",
                    "leftValue": "={{ $json.message.content.toLowerCase().trim() }}",
                    "rightValue": "soporte",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "soporte"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "cond-ventas",
                    "leftValue": "={{ $json.message.content.toL