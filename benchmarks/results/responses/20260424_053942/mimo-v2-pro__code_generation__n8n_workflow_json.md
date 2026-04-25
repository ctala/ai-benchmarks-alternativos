# MiMo-V2-Pro — code_generation/n8n_workflow_json

- model_id: `xiaomi/mimo-v2-pro`
- success: True  | final: 6.17 | quality: 6.78
- latency_total: 108.58s | tokens_per_second: 18.9
- input_tokens: 364 | output_tokens: 2048
- judge_score: 3.2 | justificación: 

## Respuesta completa

# Workflow N8N - Clasificador de Emails con IA

Aquí tienes el JSON completo del workflow:

```json
{
  "name": "Email Classifier - Soporte/Ventas/Otro",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "classify-email",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "webhook-trigger",
      "name": "Webhook Trigger",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [250, 300],
      "webhookId": "classify-email-webhook"
    },
    {
      "parameters": {
        "resource": "chat",
        "model": "gpt-4o-mini",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes de clientes. Debes clasificar el mensaje en UNA de estas categorías exactas:\n\n- \"soporte\": Si el mensaje es sobre problemas técnicos, errores, bugs, ayuda con el producto, quejas, o solicitudes de asistencia.\n- \"ventas\": Si el mensaje es sobre precios, compras, cotizaciones, información comercial, planes, o interés en productos/servicios.\n- \"otro\": Si no encaja claramente en soporte o ventas.\n\nResponde SOLO con la categoría exacta (soporte, ventas u otro), sin explicaciones adicionales."
            },
            {
              "role": "user",
              "content": "=Mensaje del cliente: {{ $json.body.message }}\nEmail del cliente: {{ $json.body.email }}"
            }
          ]
        },
        "options": {
          "temperature": 0.1,
          "maxTokens": 10
        }
      },
      "id": "openai-classifier",
      "name": "OpenAI Classifier",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.1,
      "position": [470, 300],
      "credentials": {
        "openAiApi": {
          "id": "YOUR_OPENAI_CREDENTIAL_ID",
          "name": "OpenAI API"
        }
      }
    },
    {
      "parameters": {
        "mode": "rules",
        "rules": {
          "values": [
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
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
                  "leftValue": "",
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.message.content.toLowerCase().trim() }}",
                    "rightValue": "ventas",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "ventas"
            },
            {
              "conditions":