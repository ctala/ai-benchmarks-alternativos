# DiffusionGemma 26B-A4B (DGX Spark Q8_0) — code_generation/n8n_workflow_json

- model_id: `hf.co/unsloth/diffusiongemma-26B-A4B-it-GGUF:Q8_0`
- success: True  | final: 6.84 | quality: 7.2
- latency_total: 46.61s | tokens_per_second: 43.9
- input_tokens: 0 | output_tokens: 2048
- judge_score: 3.0 | justificación: 

## Respuesta completa

thought

*   Platform: n8n.
*   Trigger: Webhook POST.
*   Data Extraction: Get `email` and `message` from the body.
*   Processing: AI Node (OpenAI) to classify the message into "soporte", "ventas", or "otro".
*   Routing: Switch based on classification.
*   Action: Send to specific Slack channels (#support, #sales, #general).
*   Output: Full JSON workflow.

    *   *Node 1: Webhook.*
        *   Method: POST.
        *   Path: `classify-message`.
    *   *Node 2: AI Agent / Basic LLM Chain (OpenAI).*
        *   Since it's a simple classification task, an "AI Agent" or a "Basic LLM Chain" works best. However, for simplicity and reliability in a workflow, the "OpenAI" node with a "Chat Model" component is standard. Let's use the "AI Agent" node with a specific prompt.
        *   Prompt: "Classify this message into one of these categories:'soporte','ventas', or 'otro'. Message: {{ $json.message }}. Return ONLY the word."
    *   *Node 3: Switch.*
        *   Condition: Check the output of the AI node.
        *   Rules:
            *   If equals'soporte'.
            *   If equals'ventas'.
            *   Otherwise (or if equals 'otro').
    *   *Node 4, 5, 6: Slack Nodes.*
        *   Slack 1: #support.
        *   Slack 2: #sales.
        *   Slack 3: #general.

    *   *Webhook:*
        ```json
        {
          "type": "n8n-nodes-base.webhook",
          "parameters": {
            "httpMethod": "POST",
            "path": "incoming-messages",
            "options": {}
          },
          "id": "...",
          "name": "Webhook",
          "type": "n8n-nodes-base.webhook",
          "position": [400, 300]
        }
        ```

    *   *OpenAI Node (using AI Agent for* *better control*):
        Actually, in modern n8n, we use the "AI Agent" node + "OpenAI Chat Model".
        *Wait*, to keep the JSON clean and compatible for the user, I'll use the "Basic LLM Chain" or the "AI Agent". Let's go with the "AI Agent" because it's the current standard.
        *Prompt:* "Clasifica el siguiente mensaje en una de estas categorías:'soporte','ventas' o 'otro'. Responde únicamente con la categoría. Mensaje: {{ $json.body.message }}"

    *   *Switch Node:*
        ```json
        {
          "parameters": {
            "values": "string",
            "value1": "={{ $json.output }}",
            "rules": [
              { "value": "equal", "value2": "soporte" },
              { "value": "equal", "value2": "ventas" }
            ]
          }
        }
        ```

    *   *Slack Nodes:*
        Standard Slack nodes sending a message.

    *   I need to use placeholders for credentials (OpenAI API Key, Slack Token) because I cannot provide them.
    *   I need to ensure the data mapping is correct (e.g., `{{ $json.body.email }}`).

    *   *Webhook:* POST method.
    *   *AI Node:* Needs an OpenAI model connection.
    *   *Switch:* Routes based on text.
    *   *Slack:* 3 separate nodes.

    *Self-Correction during drafting:* Using the "AI Agent" in n8n requires sub-nodes (Model, Memory). To make the JSON "copy-pasteable" and functional, a simpler "Basic LLM Chain" or just the "OpenAI" node (Chat) is often easier, but the AI Agent is more robust. I will use the **AI Agent** structure as it's the most powerful way currently.

    *Wait*, for a simple classification, the **"OpenAI" node with "Chat" action** is cleaner for a JSON export. Let's use that.

    *   *Webhook:* POST `/webhook`.
    *   *OpenAI:* Chat model. Prompt: "Clasifica...".
    *   *Switch:* On the output of OpenAI.
    *   *Slack:* 3 nodes.

    (Drafting the actual JSON structure now...)Para que este workflow funcione, necesitarás copiar el JSON de a continuación y pegarlo directamente en tu lienzo de n8n.

### Requisitos previos:
1. **OpenAI**: Necesitas una API Key de OpenAI configurada en el nodo de la IA.
2. **Slack**: Necesitas una credencial de Slack con permisos para publicar en los canales indicados.

### El JSON del Workflow

```json
{
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensajes",
        "options": {}
      },
      "id": "e7d8f9a0-2b3c-4e5f-8c9d-0e12345678ab",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        400,
        300
      ]
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "messages": {
          "message": [
            {
              "role": "system",
              "content": "Eres un asistente que clasifica mensajes. Tu salida debe ser estrictamente:'soporte','ventas' o 'otro'. Responde solo con la palabra seleccionada, sin puntos ni frases adicionales."
            },
            {
              "role": "user",
              "content": "Clasifica este mensaje: {{ $json.body.message }}"
            }
          ]
        },
        "options": {}
      },
      "id": "a1b2c3d4-e5f6-4a5b-8c9d-123456789abcdef",
      "name": "OpenAI Clasificador",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        620,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "TU_ID_CRED_OPENAI",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "values": "string",
        "value1": "={{ $json.choices.trim().toLowerCase() }}",
        "rules": [
          {
            "value": "equal",
            "value2": "soporte"
          },
          {
            "value": "equal",
            "value2": "ventas"
          }
        ],
        "fallbackOutput": "2"
      },
      "id": "f1e2d3c4-b5a6-4f5e-8d9c-1234567890ab",
      "name": "Switch Clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [
        840,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "=*Nuevo ticket de Soporte*\n*Email:* {{ $node[\"Webhook\"].json.body.email }}\n*Mensaje:* {{ $node[\"Webhook\"].json.body.message }}",
        "options": {}
      },
      "id": "b2c3d4e5-f6a7-4b5c-9d0e-234567890abc",
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1100,
        150
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_ID_CRED_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "=*Nuevo Lead de Ventas*\n*Email:* {{ $node[\"Webhook\"].json.body.email }}\n