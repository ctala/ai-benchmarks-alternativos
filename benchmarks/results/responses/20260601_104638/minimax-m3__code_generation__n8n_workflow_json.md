# MiniMax M3 — code_generation/n8n_workflow_json

- model_id: `minimax/minimax-m3`
- success: True  | final: 6.08 | quality: 7.0
- latency_total: 225.42s | tokens_per_second: 36.3
- input_tokens: 292 | output_tokens: 8192
- judge_score: 3.0 | justificación: 

## Respuesta completa

The user wants me to generate a complete N8N workflow in JSON format. Let me break down the requirements:

1. Webhook trigger (POST)
2. Extract "email" and "message" from body
3. AI node (OpenAI) to classify message as "soporte", "ventas" or "otro"
4. Route to different Slack channels based on classification:
   - soporte -> #support
   - ventas -> #sales
   - otro -> #general

I need to create a valid N8N workflow JSON. Let me think about the structure:

N8N workflows have a specific structure:
- `name`: workflow name
- `nodes`: array of nodes
- `connections`: connections between nodes
- `settings`: optional settings
- `staticData`: optional static data

For the routing logic, I should use a Switch node to route based on the classification. I could also use an IF node, but Switch is more appropriate for multiple branches.

Let me design the nodes:

1. **Webhook Node** - Trigger on POST
2. **OpenAI Node** - To classify the message
3. **Switch Node** - To route based on classification
4. **Slack Node x3** - One for each channel

Let me think about the OpenAI node structure. In N8N, the OpenAI node can be configured to use the chat completion API. I'll set it up to classify the message.

Actually, for better routing, I think I should use the OpenAI node with a structured output or a simple message classification. Let me design this properly.

For N8N, the OpenAI node typically uses the `@n8n/n8n-nodes-langchain.openAi` or similar. Let me use a more standard approach.

Let me write the JSON:

```json
{
  "name": "Clasificador de Mensajes con IA",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "webhook-node-id",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [240, 300],
      "webhookId": "auto-generated"
    },
    {
      "parameters": {
        "method": "POST",
        "url": "https://api.openai.com/v1/chat/completions",
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {
              "name": "Authorization",
              "value": "Bearer {{$env.OPENAI_API_KEY}}"
            },
            {
              "name": "Content-Type",
              "value": "application/json"
            }
          ]
        },
        "sendBody": true,
        "bodyParameters": {
          "parameters": [
            {
              "name": "model",
              "value": "gpt-4o-mini"
            },
            {
              "name": "messages",
              "value": "=[{\"role\": \"system\", \"content\": \"Eres un clasificador de mensajes. Debes clasificar el siguiente mensaje en una de estas categorías: 'soporte', 'ventas' u 'otro'. Responde SOLO con la palabra de la categoría, sin comillas, sin texto adicional.\"}, {\"role\": \"user\", \"content\": \"{{$json.body.message}}\"}]"
            }
          ]
        },
        "options": {}
      },
      "id": "openai-node-id",
      "name": "Clasificar con OpenAI",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.1,
      "position": [460, 300]
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "leftValue": "={{$json.choices[0].message.content}}",
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
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "leftValue": "={{$json.choices[0].message.content}}",
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
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "leftValue": "={{$json.choices[0].message.content}}",
                    "rightValue": "otro",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "otro"
            }
          ]
        },
        "options": {}
      },
      "id": "switch-node-id",
      "name": "Switch - Routing",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [680, 300]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "=?📧 Nuevo mensaje de soporte\nEmail: {{$node[\"Webhook\"].json.body.email}}\nMensaje: {{$node[\"Webhook\"].json.body.message}}",
        "otherOptions": {}
      },
      "id": "slack-support-id",
      "name": "Slack - Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [900, 100]
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "=?💰 Nuevo mensaje de ventas\nEmail: {{$node[\"Webhook\"].json.body.email}}\nMensaje: {{$node[\"Webhook\"].json.body.message}}",
        "otherOptions": {}
      },
      "id": "slack-sales-id",
      "name": "Slack - Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [900, 300]
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "=?📬 Mensaje general\nEmail: {{$node[\"Webhook\"].json.body.email}}\nMensaje: {{$node[\"Webhook\"].json.body.message}}",
        "otherOptions": {}
      },
      "id": "slack-general-id",
      "name": "Slack - General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [900, 500]
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "={\n  \"status\": \"ok\",\n  \"classification\": \"{{$json.choices[0].message.content}}\"\n}"
      },
      "id": "respond-webhook-id",
      "name": "Respond to Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1,
      "position": [1120, 300]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Clasificar con OpenAI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar con OpenAI": {
      "main": [
        [
          {
            "node": "Switch - Routing",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch - Routing": {
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
    },
    "Slack - Soporte": {
      "main": [
        [
          {
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack - Ventas": {
      "main": [
        [
          {
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack - General": {
      "main": [
        [
          {
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {
    "executionOrder": "v1"
  }
}
```

Wait, I should think about a few things:

1. The OpenAI node: I'm using the HTTP request node instead of the dedicated OpenAI node, which is more flexible. However, the dedicated `@n8n/n8n-nodes-langchain.openAi` node would be better. Let me use a more standard approach.

2. Actually, the LangChain OpenAI node in N8N is the most common one for this use case. Let me think about using that.

The LangChain OpenAI node has a simpler configuration. But using the HTTP request is more universally compatible.

Let me think about which approach is better. I think using the HTTP request is more reliable because:
- It doesn't require the LangChain nodes
- It's clearer for users to understand
- The user can easily modify the API call

But I should also consider that maybe the user expects the OpenAI node specifically. Let me use the HTTP request but make it clear that they can swap it for the OpenAI node.

Actually, let me reconsider. I'll use the `@n8n/n8n-nodes-langchain.openAi` node since that's the most direct way to use OpenAI in N8N. But this requires LangChain nodes to be installed.

Hmm, let me go with the HTTP Request node approach for maximum compatibility. I'll add comments explaining the structure.

Wait, I should also think about the response. When using `responseMode: "responseNode"`, I need a `respondToWebhook` node at the end. This is what I have.

Let me also think about error handling and the fact that the OpenAI response might need parsing. With the HTTP request node, the JSON response is automatically parsed.

Let me also think about whether to use trim() on the response to handle any whitespace the AI might add. That's a good idea.

Let me refine the workflow:

1. Webhook receives POST
2. OpenAI classifies the message
3. Switch routes based on classification
4. Each Slack node sends to its respective channel
5. Respond to webhook at the end

I'll also add a code node to extract email and message if needed, but since the body is already accessible via `$json.body.email` and `$json.body.message`, I don't strictly need it. But for cleanliness, I could add a Set node or just use the expressions.

Actually, the requirement says "Extraiga el campo email y message del body" - this could be done with a Set node or just by using the expressions. Let me add a Set node to make it explicit and to also handle any data transformation.

Wait, the Set node is optional. The expressions can directly access `$json.body.email` and `$json.body.message`. But adding a Set node makes the data flow clearer.

Let me decide: I'll keep it simple and use the expressions directly. This makes the workflow shorter and easier to understand.

But actually, let me re-read the requirements:
1. Se active con un webhook POST ✓
2. Extraiga el campo "email" y "message" del body - I should make this explicit
3. Use un nodo de IA (OpenAI) para clasificar ✓
4. Segun la clasificacion, envie el email a un canal de Slack diferente ✓

For step 2, I'll add a Set node to extract and normalize these fields. This makes the workflow more robust and easier to debug.

Let me revise:

```
Webhook -> Set (extract email, message) -> OpenAI -> Switch -> [Slack x3] -> Respond
```

Actually, looking at it again, I think using expressions directly is fine and makes the workflow more concise. The "extraction" is implicit in how we use the data. But adding a Set node would be cleaner.

Let me add a Set node to be explicit about the extraction. This also makes it easier to add validation or transformation later.

Here's my revised plan:

1. **Webhook** - Receive POST
2. **Set** - Extract email and message from body
3. **HTTP Request (OpenAI)** - Classify the message
4. **Switch** - Route based on classification
5. **Slack x3** - Send to respective channels
6. **Respond to Webhook** - Send response

Let me also think about the Slack channel names. The user said:
- soporte -> #support
- ventas -> #sales
- otro -> #general

I'll use these exact channel names.

Now, let me also think about whether to use the AI node from N8N's built-in capabilities. The user mentioned "nodo de IA (OpenAI)". This could be either:
- The OpenAI node from LangChain
- An HTTP request to OpenAI API

I'll use the HTTP request approach because it's more universally compatible and doesn't require special installations. I'll mention in a note that they can swap it for the LangChain OpenAI node if they prefer.

Actually, thinking more about this, let me use the dedicated OpenAI node from N8N if possible. The N8N OpenAI node is part of the standard installation. Let me check the exact node name...

The OpenAI node in N8N is `n8n-nodes-base.openAi` (older) or `@n8n/n8n-nodes-langchain.openAi` (newer, in LangChain integration).

For simplicity and to make the JSON cleaner, I'll use the HTTP Request node to call the OpenAI API directly. This is more verbose but more reliable.

Let me finalize the JSON:

```json
{
  "name": "Clasificador de Mensajes con IA - Slack",
  "nodes": [...],
  "connections": {...},
  "settings": {...}
}
```

I'll also add a sticky note or description explaining the workflow.

Let me think about positions in the canvas. I'll arrange them in a flow:
- Webhook: [240, 300]
- Set: [460, 300]
- OpenAI: [680, 300]
- Switch: [900, 300]
- Slack Support: [1120, 150]
- Slack Sales: [1120, 300]
- Slack General: [1120, 450]
- Respond: [1340, 300]

Actually, with the switch, the three outputs go to three different places, so I should position them at different y-coordinates.

Let me write the final JSON. I'll be thorough and include all the necessary details.

One more thing: for the OpenAI classification, I should make sure the prompt is clear and the response is parseable. I'll add `temperature: 0` for deterministic results and use a clear system prompt.

Also, I need to handle the case where the response might have extra whitespace or newlines. I'll use `.trim()` in the switch conditions.

Let me write the final version:

```json
{
  "name": "Clasificador de Mensajes con IA - Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "1a2b3c4d-5e6f-7890-abcd-ef1234567890",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [240, 300],
      "webhookId": "auto-generated"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "email-assignment",
              "name": "email",
              "value": "={{$json.body.email}}",
              "type": "string"
            },
            {
              "id": "message-assignment",
              "name": "message",
              "value": "={{$json.body.message}}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "2b3c4d5e-6f78-90ab-cdef-123456789012",
      "name": "Extraer Email y Mensaje",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.3,
      "position": [460, 300]
    },
    {
      "parameters": {
        "method": "POST",
        "url": "https://api.openai.com/v1/chat/completions",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {
              "name": "Content-Type",
              "value": "application/json"
            }
          ]
        },
        "sendBody": true,
        "specifyBody": "json",
        "jsonBody": "={\n  \"model\": \"gpt-4o-mini\",\n  \"temperature\": 0,\n  \"messages\": [\n    {\n      \"role\": \"system\",\n      \"content\": \"Eres un clasificador de mensajes. Tu única tarea es clasificar el mensaje del usuario en UNA de estas tres categorías exactas: 'soporte', 'ventas' u 'otro'. Responde SOLO con la palabra de la categoría, sin comillas, sin puntos, sin texto adicional ni explicación.\"\n    },\n    {\n      \"role\": \"user\",\n      \"content\": \"{{$json.message}}\"\n    }\n  ]\n}",
        "options": {}
      },
      "id": "3c4d5e6f-7890-abcd-ef12-345678901234",
      "name": "Clasificar con OpenAI",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.1,
      "position": [680, 300]
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "id": "cond-soporte",
                    "leftValue": "={{$json.choices[0].message.content.trim()}}",
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
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "id": "cond-ventas",
                    "leftValue": "={{$json.choices[0].message.content.trim()}}",
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
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "id": "cond-otro",
                    "leftValue": "={{$json.choices[0].message.content.trim()}}",
                    "rightValue": "otro",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "otro"
            }
          ]
        },
        "options": {}
      },
      "id": "4d5e6f78-90ab-cdef-1234-567890123456",
      "name": "Switch - Routing",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [900, 300]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "=🆘 *Nuevo mensaje de SOPORTE*\n\n*Email:* {{$node[\"Extraer Email y Mensaje\"].json.email}}\n*Mensaje:* {{$node[\"Extraer Email y Mensaje\"].json.message}}\n*Clasificación:* soporte",
        "otherOptions": {}
      },
      "id": "5e6f7890-abcd-ef12-3456-789012345678",
      "name": "Slack - Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1120, 150]
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "=💰 *Nuevo mensaje de VENTAS*\n\n*Email:* {{$node[\"Extraer Email y Mensaje\"].json.email}}\n*Mensaje:* {{$node[\"Extraer Email y Mensaje\"].json.message}}\n*Clasificación:* ventas",
        "otherOptions": {}
      },
      "id": "6f7890ab-cdef-1234-5678-901234567890",
      "name": "Slack - Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1120, 300]
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "=📬 *Mensaje GENERAL (otro)*\n\n*Email:* {{$node[\"Extraer Email y Mensaje\"].json.email}}\n*Mensaje:* {{$node[\"Extraer Email y Mensaje\"].json.message}}\n*Clasificación:* otro",
        "otherOptions": {}
      },
      "id": "7890abcd-ef12-3456-7890-123456789012",
      "name": "Slack - General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1120, 450]
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "={\n  \"status\": \"ok\",\n  \"classification\": \"{{$node[\"Switch - Routing\"].json.choices[0].message.content.trim()}}\",\n  \"email\": \"{{$node[\"Extraer Email y Mensaje\"].json.email}}\"\n}"
      },
      "id": "890abcde-1234-5678-9012-345678901234",
      "name": "Respond to Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1,
      "position": [1340, 300]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extraer Email y Mensaje",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer Email y Mensaje": {
      "main": [
        [
          {
            "node": "Clasificar con OpenAI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar con OpenAI": {
      "main": [
        [
          {
            "node": "Switch - Routing",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch - Routing": {
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
    },
    "Slack - Soporte": {
      "main": [
        [
          {
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack - Ventas": {
      "main": [
        [
          {
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack - General": {
      "main": [
        [
          {
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {
    "executionOrder": "v1"
  },
  "staticData": null,
  "tags": [],
  "triggerCount": 1,
  "updatedAt": "2024-01-15T00:00:00.000Z",
  "versionId": "1"
}
```

Wait, I need to be careful about a few things:

1. The `respondToWebhook` node is called from three different branches. N8N should handle this correctly, but I need to make sure the connections are set up properly. Each Slack node connects to the Respond node.

2. The authentication for the OpenAI HTTP request: I used `genericCredentialType` and `genericAuthType: "httpHeaderAuth"`. This means the user needs to set up a header auth credential. Alternatively, I could just put the API key directly or use an environment variable. Let me use a credential approach but also document it.

Actually, for simplicity and to make it work out of the box, I should use a header parameter with an environment variable. But the user might not have set that up. Let me use the credential approach but explain it in the notes.

Actually, let me change the approach. I'll use the header parameter with a placeholder value that the user needs to replace, or better, I'll use a credential type that's commonly supported.

Hmm, let me just use the header parameter with an expression that references an environment variable, and add a note that they need to set OPENAI_API_KEY. This is cleaner.

Let me revise:

```json
"sendHeaders": true,
"headerParameters": {
  "parameters": [
    {
      "name": "Content-Type",
      "value": "application/json"
    },
    {
      "name": "Authorization",
      "value": "Bearer {{$env.OPENAI_API_KEY}}"
    }
  ]
}
```

Wait, I can use `$env.OPENAI_API_KEY` in N8N expressions. But I need to make sure the syntax is correct. In N8N, environment variables are accessed via `$env.VARIABLE_NAME`.

Actually, looking at N8N documentation, the correct way to access env vars in expressions is `$env.VARIABLE_NAME`. But for the header, I should use the credential or just hardcode it for testing.

Let me use a cleaner approach with credentials. In N8N, you can set up HTTP Header Auth credentials. I'll set up the node to use that credential type, and the user will need to configure it.

Actually, for the most user-friendly approach, let me just use a hardcoded value in the header but add a clear comment that they need to replace it with their actual API key, or better, set up the credential properly.

Let me think... The best approach for a reusable workflow is:
1. Use the credential type "httpHeaderAuth" for the OpenAI API key
2. The user configures the credential once

But in the JSON, I can specify the credential type, and the user will need to attach the credential. Let me do that.

Actually, the simplest and most explicit approach is to use an expression with an env var. Let me do that and add a clear note.

Final approach: I'll use `$env.OPENAI_API_KEY` in the Authorization header, and add notes that the user needs to set this environment variable in their N8N instance.

Let me also reconsider the Switch node. I have three rules, each checking for a specific value. This is correct. The Switch node will route to the first matching rule. If none match, nothing happens. I should consider adding a fallback or making sure all cases are covered. Since the AI is instructed to respond with one of the three values, this should be fine, but for robustness, I could add a default branch that goes to #general for anything that doesn't match. Actually, the "otro" case should catch anything that isn't soporte or ventas, but only if the AI explicitly says "otro". If the AI says something else, the message would be lost. Let me add a "fallback" or use the "fallbackOutput" option in the Switch node to route unmatched cases to #general.

Actually, looking at the Switch node, there's a "fallbackOutput" option that can be set to "extra" or "all" or specific nodes. I should set this up to send to #general as a safety net.

But wait, if I set up the rules correctly, the AI should always respond with one of the three values. But to be safe, let me add a condition for "otro" that uses "not equals soporte" and "not equals ventas", or use a fallback.

Hmm, let me just add a "fallbackOutput" that routes to the Slack - General node. This way, if the classification doesn't match any of the three expected values, it still goes to #general.

Actually, looking at N8N Switch node documentation more carefully, the "fallbackOutput" can be set to route unmatched items to a specific output. But it's simpler to just add a condition for "otro" and assume the AI follows instructions. For the scope of this task, I think it's fine.

Let me also think about whether I need to handle the case where the OpenAI API call fails. That would be good error handling, but it adds complexity. For the basic workflow, I'll assume the API call succeeds. The user can add error handling later.

One more thing: the webhook response. I'm using `responseMode: "responseNode"` which means I need the `respondToWebhook` node. The response will be sent when that node is executed. This is correct.

Now, let me also think about the Slack node configuration. In N8N, the Slack node requires credentials. I need to make sure the node type is correct. The standard Slack node is `n8n-nodes-base.slack`. The version might vary. Let me use a recent version.

Also, the Slack node parameters: in newer versions, the channel might be specified differently. Let me use the standard `channel` parameter and `text` parameter.

Let me also add a sticky note to explain the workflow and required credentials.

Actually, sticky notes are also nodes in N8N. I could add one, but it might clutter the JSON. I'll just provide a clear explanation in the response text.

Let me finalize the JSON. I want to make sure:
1. The structure is valid N8N workflow JSON
2. All nodes are properly configured
3. Connections are correct
4. The workflow is production-ready (with clear instructions for credentials)

Here's my final plan for the response:
1. Brief explanation in Spanish
2. The complete JSON
3. Instructions for setup (credentials, environment variables, etc.)
4. Example of how to call the webhook

Let me write the final JSON carefully.

One thing I want to double-check: the Set node type. In N8N, the Set node is `n8n-nodes-base.set` with typeVersion 3.x for the newer version. The parameters structure I used should be correct for typeVersion 3.3 or similar.

Actually, looking at N8N documentation, the Set node has evolved. In the latest versions, it uses "assignments" with a specific structure. Let me verify my structure is correct.

For N8N Set node (typeVersion 3.3+):
```json
{
  "assignments": {
    "assignments": [
      {
        "id": "unique-id",
        "name": "field-name",
        "value": "value",
        "type": "string"
      }
    ]
  },
  "options": {}
}
```

This looks correct.

For the HTTP Request node (typeVersion 4.1+):
The structure with `jsonBody` should work. Alternatively, I could use `bodyParameters` but `jsonBody` is cleaner for JSON payloads.

Wait, I need to check the `specifyBody` parameter. In newer versions, it's `specifyBody: "json"` to use a JSON body. Let me make sure I have that.

Also, for the HTTP Request authentication, I should probably just use the header parameter approach and not the generic credential type, to keep it simpler. Let me just use the header parameter for Authorization.

Let me revise the HTTP Request node:

```json
{
  "parameters": {
    "method": "POST",
    "url": "https://api.openai.com/v1/chat/completions",
    "sendHeaders": true,
    "headerParameters": {
      "parameters": [
        {
          "name": "Content-Type",
          "value": "application/json"
        },
        {
          "name": "Authorization",
          "value": "Bearer {{$env.OPENAI_API_KEY}}"
        }
      ]
    },
    "sendBody": true,
    "specifyBody": "json",
    "jsonBody": "={...}",
    "options": {}
  }
}
```

This should work. The user needs to set the OPENAI_API_KEY environment variable in their N8N instance.

Actually, I just realized I should use a credential for better security rather than env var in the expression. But env var is also acceptable and more transparent for the JSON. Let me stick with env var but add a clear note.

Now, let me write the final response. I'll provide:
1. A brief introduction
2. The complete JSON in a code block
3. Setup instructions
4. Example usage

The JSON should be well-formatted and easy to read. I'll use 2-space indentation.

Let me write it out:

```json
{
  "name": "Clasificador de Mensajes con IA → Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        240,
        300
      ],
      "webhookId": "clasificar-mensaje-webhook"
    },
    ...
  ],
  ...
}
```

Actually, for the webhookId, I should use a UUID or let it be auto-generated. Let me use a UUID for clarity.

Let me generate proper UUIDs for the node IDs. Actually, I can use simple unique strings, but UUIDs are more "N8N-like". Let me use UUIDs.

One more consideration: the `staticData`, `tags`, `triggerCount`, `updatedAt`, `versionId` fields are optional and can be omitted. I'll include `tags` as an empty array and `triggerCount` as 1, but I can omit the others.

Let me write the complete final JSON. I want to make sure everything is correct and production-ready.

Actually, looking at the Slack node typeVersion, in recent N8N versions (1.0+), the Slack node might have different parameters. Let me use a safe version. typeVersion 1 or 2 should work for most installations. I'll use typeVersion 1 for compatibility, or I could omit it and let N8N default it. But specifying it is better for reproducibility.

Wait, in N8N, if you don't specify typeVersion, it uses the default for that node type. But for JSON imports, it's better to specify it. Let me check what's reasonable.

For N8N 1.x:
- Webhook: typeVersion 1 or 2 (2 is