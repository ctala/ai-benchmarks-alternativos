# Ling 3.0 Flash — code_generation/n8n_workflow_json

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 7.84 | quality: 8.12
- latency_total: 18.952s | tokens_per_second: 432.3
- input_tokens: 149 | output_tokens: 8192
- judge_score: 3.8 | justificación: 

## Respuesta completa

The user wants a complete N8N workflow JSON that does the following:

1. Trigger: Webhook (POST)
2. Extract "email" and "message" from the body
3. Use OpenAI node to classify the message into "soporte", "ventas", or "otro"
4. Based on classification, send a message to different Slack channels:
   - soporte → #support
   - ventas → #sales
   - otro → #general

Let me think about the N8N workflow structure:

1. **Webhook Node**: POST method, receives JSON body
2. **Set Node**: Extract email and message from the webhook body
3. **OpenAI Node**: Classify the message using an LLM prompt
4. **Switch Node**: Route based on classification result
5. **Slack Nodes**: Three different Slack nodes for each channel

Let me construct the JSON carefully with proper N8N node structure.

For the OpenAI node, I need to think about how to structure the prompt so it returns just the classification label. I'll use a structured prompt asking for a single word response.

For the Switch node, I'll use the output from the OpenAI node to route to different branches.

For Slack nodes, I'll use the Slack node type with channel configuration.

Let me think about the N8N JSON structure:
- Each node has: id, name, type, typeVersion, position, parameters, etc.
- Connections between nodes

The OpenAI node in N8N uses the "n8n-nodes-base.openAi" type. The operation for chat completion would be "completion" or "chat". In newer versions, it's "chat" with "chat" operation.

Let me think about the parameters:
- OpenAI: model, messages (system + user), and we need to extract the classification from the response
- We might need a Set node after OpenAI to extract just the classification label

Actually, let me think about this more carefully. The OpenAI node returns the full response. I need to extract the classification from it. I could:
1. Use the OpenAI node with a prompt that returns just the label
2. Use a Set/Code node to extract the classification

For simplicity, I'll use a prompt that asks OpenAI to return just the classification word, and then use a Switch node on the AI response content.

Actually, in N8N, after the OpenAI node, the response is in `{{ $json.choices[0].message.content }}` or similar. Let me think about the exact structure.

In N8N, the OpenAI Chat node output would have the response in the items. The structure depends on the version. For typeVersion 1.8 or similar, the output would contain the message content.

Let me structure this properly. I'll use a Code node or Set node to extract the classification, then route with Switch.

Actually, let me keep it simpler and use the Switch node directly on the OpenAI output, checking the content.

Let me construct the full JSON now:

```json
{
  "name": "Email Classifier Workflow",
  "nodes": [...],
  "connections": {...}
}
```

Let me think about the exact node configurations:

**Webhook Node:**
- type: "n8n-nodes-base.webhook"
- httpMethod: "POST"
- path: "classify-email"

**Set Node (Extract):**
- Extract email and message from body

**OpenAI Node:**
- type: "n8n-nodes-base.openAi"
- operation: "chat"
- model: "gpt-4o-mini" or "gpt-3.5-turbo"
- messages with system prompt for classification and user message with the actual message
- I need to add the OpenAI credential reference

**Switch Node:**
- Check the classification result

**Slack Nodes (3):**
- Each sends to a different channel

Let me think about how the OpenAI node structures its output in N8N. In N8N, the OpenAI Chat node output has the structure where `{{ $json.output }}` or `{{ $json.text }}` or `{{ $json.choices[0].message.content }}` depending on the version.

For N8N typeVersion 1.8 of the OpenAI node, the output is typically at `{{ $json.output }}`.

Actually, let me be more careful. In N8N's OpenAI node (chat), the response structure for typeVersion 1.x would be:
- `{{ $json.choices[0].message.content }}` for the content

But in newer versions, it might be different. Let me just reference it properly.

I think the safest approach is to use a Set node after OpenAI to extract the classification, then use Switch on that.

Let me also think about how to handle the "otro" default case in the Switch node.

Let me now write the complete JSON. I need to be careful with all the IDs and connections.

For the OpenAI node, I'll use a prompt like:
"Clasifica el siguiente mensaje como 'soporte', 'ventas' o 'otro'. Responde solo con una de estas tres palabras. Mensaje: {{ $json.message }}"

For the Slack nodes, I'll configure them to send a message to the appropriate channel with the email and message info.

Let me also think about the Slack node configuration. In N8N, the Slack node for sending messages would use the "send" operation with channel, text, etc.

I need to be careful about the credential references - I'll use placeholder names like "OpenAI Api" and "Slack Api" which the user would need to configure.

Let me write the complete JSON now. I'll use UUIDs for node IDs.

Actually, let me reconsider the OpenAI node type version. In N8N, the OpenAI Chat node has evolved. For simplicity, I'll use a well-known configuration.

Let me also consider: should I use a Code node to extract just the classification? That might be cleaner. But a Set node with expression should work too.

Let me finalize the structure:

1. Webhook (POST /classify-email)
2. Set (extract email, message)
3. OpenAI (classify message)
4. Set (extract classification label from AI response)
5. Switch (route by classification)
6. Slack #support
7. Slack #sales
8. Slack #general

Wait, actually I can simplify by having the Switch node check the OpenAI output directly if I structure the prompt well enough that the output is just the word.

But to be safe, let me add a Set node after OpenAI to clean up the output.

Let me write this out now.

For the OpenAI node in N8N, the parameters structure for chat completion (typeVersion 1.8) would be something like:

```json
{
  "parameters": {
    "modelId": "gpt-4o-mini",
    "options": {},
    "messages": {
      "messageValues": [
        {
          "role": "system",
          "content": "Eres un clasificador de mensajes. Clasifica el mensaje de entrada en una de estas categorías: 'soporte', 'ventas' o 'otro'. Responde SOLO con la palabra de la categoría, sin explicaciones."
        },
        {
          "role": "user",
          "content": "={{ $json.message }}"
        }
      ]
    }
  }
}
```

Hmm, I need to be more careful about the exact parameter structure. N8N's node parameters can vary significantly between versions.

Let me think about what's a reasonable and accurate representation. I'll aim for a structure that's close to what N8N generates but may need some adjustments based on the exact version.

Actually, for N8N workflows exported as JSON, the parameter structure follows a specific format. Let me construct it carefully.

For the OpenAI node (n8n-nodes-base.openAi), the chat operation parameters would include:
- operation: "chat"
- model: "gpt-4o-mini"  
- messages: array of message objects
- options: optional parameters like temperature

For Slack node (n8n-nodes-base.slack), sending a message:
- operation: "post"
- channel: "#support" (or #sales, #general)
- text: the message content

Let me now write the complete workflow JSON. I'll use reasonable placeholder IDs and positions.

One more consideration: the connection structure in N8N JSON uses node names as keys, and the connections specify which output index connects to which node.

Let me finalize:

```json
{
  "name": "Email Classifier Workflow",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "classify-email",
        "responseMode": "responseNode"
      },
      "id": "...",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [250, 300]
    },
    ...
  ],
  "connections": {
    "Webhook": {
      "main": [
        [{ "node": "Extract Datos", "type": "main", "index": 0 }]
      ]
    },
    ...
  }
}
```

Let me think about the webhook response. The webhook should probably return a 200 OK response. I could add a Respond to Webhook node, or just let it default.

Actually, for simplicity, I'll not add a Respond to Webhook node - the workflow will just process and the webhook will return by default.

Let me now write the complete, detailed JSON. I need to be thorough.

For the Set node after OpenAI, I'll extract the classification from the AI response. The exact path depends on the OpenAI node version. For typeVersion 1.8, the content would be at `{{ $json.choices[0].message.content }}` or just `{{ $json.output }}`.

Actually, in N8N's OpenAI node, the output structure for chat completion is typically:
```json
{
  "id": "...",
  "object": "chat.completion",
  "choices": [{
    "message": {
      "role": "assistant",
      "content": "soporte"
    }
  }]
}
```

So to extract just the content, I'd use `{{ $json.choices[0].message.content }}`.

Let me use a Set node to create a clean `classification` field.

For the Switch node, I'll check if classification equals "soporte", "ventas", or "otro".

Let me write the final JSON now. I'll use UUIDs for node IDs.

One thing to note: in N8N workflows, the `credentials` field references credentials stored in the N8N instance. I'll add placeholder credential references.

Let me also consider the Slack node configuration more carefully. In N8N, the Slack node for sending messages has:
- resource: "message"
- operation: "post"
- channel: the channel name or ID
- text: the message text

Alright, let me construct the full JSON now.

I realize I should also think about what happens if the classification doesn't match any of the three branches - I should have a default or just let it not send anything.

Let me also make sure the positions make sense visually in the N8N canvas.

Here's my plan for positions:
- Webhook: [250, 300]
- Extract Datos: [500, 300]
- OpenAI: [750, 300]
- Limpiar Clasificación: [1000, 300]
- Switch: [1250, 300]
- Slack Soporte: [1500, 100]
- Slack Ventas: [1500, 300]
- Slack Otro: [1500, 500]

This should give a nice visual flow.

Now let me write the complete JSON carefully. I need to make sure all the parameter structures are correct for N8N.

For the OpenAI node, I need to think about the exact parameter format. In N8N, the OpenAI Chat node parameters look like:

```json
{
  "operation": "chat",
  "modelId": "gpt-4o-mini",
  "messages": {
    "messageValues": [
      {
        "role": "system",
        "content": "..."
      },
      {
        "role": "user",
        "content": "..."
      }
    ]
  }
}
```

Wait, I'm not 100% sure about the exact parameter structure for the OpenAI node in N8N. Let me think about what I know...

The OpenAI node in N8N has different typeVersions. For the chat operation:
- The `messages` parameter is typically a fixed collection or a list of message objects
- Each message has `role` and `content` fields

In newer N8N versions, the OpenAI node uses `n8n-nodes-base.openAi` with typeVersion 1.8 or similar.

Let me construct a reasonable JSON that should work. I'll include the credential placeholders.

Actually, I realize I should also think about how the Switch node parameters work in N8N. The Switch node checks conditions on input data and routes to different outputs.

For the Switch node:
```json
{
  "rules": {
    "rules": [
      {
        "conditions": {
          "conditions": [
            {
              "leftValue": "={{ $json.classification }}",
              "rightValue": "soporte",
              "operator": { "type": "string", "operation": "equals" }
            }
          ]
        }
      },
      ...
    ]
  }
}
```

Hmm, the exact structure might vary. Let me use a common pattern.

Let me now write the complete JSON. I'll try to be as accurate as possible while acknowledging that exact parameter structures might need slight adjustments based on the N8N version being used.

Actually, I just realized I should think about what the most common/current N8N format looks like. N8N workflows use a specific JSON schema. Let me construct it properly.

Let me also consider: should I use `typeVersion: 1` or `typeVersion: 2` for the webhook? In N8N v1, the webhook node uses typeVersion 1, and in newer versions, typeVersion 2. I'll use typeVersion 2 for the webhook and the latest reasonable versions for other nodes.

OK let me just write this out now. I'll create a comprehensive, well-structured JSON workflow.

Let me reconsider the structure of the OpenAI node parameters. In N8N, for the OpenAI Chat node:

```json
{
  "parameters": {
    "operation": "chat",
    "modelId": "gpt-4o-mini",
    "options": {},
    "messagesUi": {
      "messageValues": [
        {
          "role": "system",
          "content": "..."
        },
        {
          "role": "user", 
          "content": "..."
        }
      ]
    }
  }
}
```

I think the messages are passed through `messagesUi` in newer versions. But I'm not 100% sure. Let me use a more generic structure.

Actually, in N8N's actual workflow exports, the OpenAI chat node uses a structure like:

```json
"parameters": {
  "operation": "chat",
  "modelId": "gpt-4o-mini",
  "messages": {
    "messageValues": [
      {
        "role": "system",
        "content": "..."
      }
    ]
  }
}
```

I'll go with this structure and note that the user may need to adjust based on their N8N version.

Let me finalize the JSON now. I'll make it as complete and accurate as I can.

For the Slack nodes, the parameters would be:
```json
{
  "parameters": {
    "operation": "post",
    "channel": "#support",
    "text": "..."
  }
}
```

The Slack node type in N8N is `n8n-nodes-base.slack`.

Let me write the complete workflow JSON now.

I'll also add a "Respond to Webhook" node at the end to send a response back to the caller.

Actually, let me keep it simpler and not add that - the workflow will work fine without it. The webhook will return a default 200 response.

Wait, actually in N8N, if you don't add a "Respond to Webhook" node, the webhook will still return a 200 response after all nodes complete. So that's fine.

Let me also add proper error handling... actually, the user didn't ask for that, so I'll keep it simple.

Let me write the final JSON now:

```json
{
  "name": "Email Classifier Workflow",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "classify-email",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [250, 300],
      "webhookId": "classify-email"
    },
    {
      "parameters": {
        "keepOnlySet": true,
        "values": {
          "string": [
            {
              "name": "email",
              "value": "={{ $json.body.email }}"
            },
            {
              "name": "message",
              "value": "={{ $json.body.message }}"
            }
          ]
        },
        "options": {}
      },
      "id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
      "name": "Extract Datos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.3,
      "position": [500, 300]
    },
    {
      "parameters": {
        "operation": "chat",
        "modelId": "gpt-4o-mini",
        "messages": {
          "messageValues": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes de correo electrónico. Clasifica el mensaje en una de estas categorías exactas: 'soporte', 'ventas' o 'otro'. Responde ÚNICAMENTE con la palabra de la categoría, sin explicaciones ni texto adicional."
            },
            {
              "role": "user",
              "content": "={{ $json.message }}"
            }
          ]
        },
        "options": {}
      },
      "id": "c3d4e5f6-a7b8-9012-cdef-123456789012",
      "name": "OpenAI - Clasificar",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.8,
      "position": [750, 300],
      "credentials": {
        "openAiApi": {
          "id": "OPENAI_CREDENTIAL_ID",
          "name": "OpenAI Api"
        }
      }
    },
    ...
  ],
  "connections": {...}
}
```

Hmm, I need to think about the exact output structure of the OpenAI node in N8N. In N8N, the OpenAI Chat node output has the full API response. The classification result would be in `{{ $json.choices[0].message.content }}`.

For the Set node after OpenAI to extract the classification:
```json
{
  "parameters": {
    "keepOnlySet": true,
    "values": {
      "string": [
        {
          "name": "classification",
          "value": "={{ $json.choices[0].message.content.trim().toLowerCase() }}"
        },
        {
          "name": "email",
          "value": "={{ $json.email }}"
        },
        {
          "name": "message",
          "value": "={{ $json.message }}"
        }
      ]
    }
  }
}
```

Wait, actually the OpenAI node might restructure the output differently in N8N. Let me think...

In N8N, when you use the OpenAI Chat node, the output items contain the full response from the API. The structure is typically:
```json
{
  "id": "...",
  "object": "chat.completion",
  "choices": [{
    "index": 0,
    "message": {
      "role": "assistant",
      "content": "soporte"
    },
    "finish_reason": "stop"
  }],
  "usage": {...}
}
```

But N8N might also have a simplified output. I think the safest approach is to reference `{{ $json.choices[0].message.content }}`.

For the Switch node, I need to check the classification value. The Switch node in N8N has conditions that you set up.

Let me also think about the Slack node configuration more carefully. In N8N, the Slack node for posting a message:

```json
{
  "parameters": {
    "operation": "post",
    "channel": "#support",
    "text": "Nuevo mensaje clasificado como soporte.\nEmail: {{ $json.email }}\nMensaje: {{ $json.message }}",
    "options": {}
  }
}
```

OK, I think I have enough information to write the complete JSON. Let me do it now.

One more thing: for the Switch node in N8N, the conditions structure. In N8N typeVersion 3 (or similar), the Switch node has a `rules` structure.

Actually, let me look at the Switch node structure more carefully. In N8N, the Switch node (n8n-nodes-base.switch) has:

```json
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
                "id": "rule1",
                "leftValue": "={{ $json.classification }}",
                "rightValue": "soporte",
                "operator": {
                  "type": "string",
                  "operation": "equals"
                }
              }
            ],
            "combinator": "and"
          },
          "outputKey": "soporte"
        },
        ...
      ]
    },
    "options": {}
  }
}
```

Hmm, I'm not 100% sure about the exact structure. Let me use a commonly seen format.

Actually, in N8N, the Switch node parameters are structured as:

```json
{
  "parameters": {
    "rules": {
      "values": [
        {
          "conditions": {
            "options": {},
            "conditions": [
              {
                "id": "...",
                "leftValue": "={{ $json.classification }}",
                "rightValue": "soporte",
                "operator": {
                  "type": "string",
                  "operation": "equals"
                }
              }
            ],
            "combinator": "and"
          },
          "outputKey": "soporte"
        },
        {
          "conditions": {...},
          "outputKey": "ventas"
        },
        {
          "conditions": {...},
          "outputKey": "otro"
        }
      ]
    }
  }
}
```

I think I have enough to write a comprehensive JSON now. Let me do it.

Let me also consider: for the Slack nodes, I need to reference credentials. I'll use placeholder credential IDs.

Also, for the Slack node, I should check what the correct parameters are. In N8N, the Slack node for sending a message:
- resource: "message" (might be implicit in newer versions)
- operation: "post" 
- channel: "#support"
- text: "..."

In newer N8N versions, the Slack node might use a different parameter structure. I'll use a reasonable structure.

Let me also add a "Respond to Webhook" node at the end so the webhook caller gets a proper response.

OK, I think I've thought about this enough. Let me write the final JSON.

Let me also double-check: the user asked for the "complete JSON of the workflow". So I need to provide the full workflow JSON that can be imported into N8N.

Here's my final structure:

Nodes:
1. Webhook (trigger)
2. Set: Extract email and message
3. OpenAI: Classify message
4. Set: Extract classification label
5. Switch: Route by classification
6. Slack: Send to #support
7. Slack: Send to #sales
8. Slack: Send to #general
9. Respond to Webhook: Return success

Connections:
- Webhook → Extract Datos
- Extract Datos → OpenAI - Clasificar
- OpenAI - Clasificar → Limpiar Clasificación
- Limpiar Clasificación → Switch
- Switch (soporte) → Slack Soporte
- Switch (ventas) → Slack Ventas
- Switch (otro) → Slack Otro
- Slack Soporte → Respond to Webhook
- Slack Ventas → Respond to Webhook
- Slack Otro → Respond to Webhook

Actually, for the Respond to Webhook, I should add it after all branches converge. But in N8N, you can't easily merge branches... Let me think.

Actually, I can use the Respond to Webhook node and connect all three Slack nodes to it. Or I can just have the webhook return automatically.

For simplicity, let me not add a Respond to Webhook node and just let the workflow process silently. The webhook will return a 200 OK after execution.

Hmm, actually, for a POST webhook in N8N, if you want to return a response to the caller, you should add a "Respond to Webhook" node. Otherwise, the caller might not get a proper response.

Let me add it. I'll connect all three Slack nodes to a single Respond to Webhook node.

Wait, actually in N8N, the Respond to Webhook node is typically connected to the Webhook node directly, or you can have it at the end. Let me just add it and connect all three branches to it.

Actually, this is getting complex. Let me simplify: I'll add a Respond to Webhook node connected after each Slack node, all returning the same response. Or better yet, I'll just not add it and keep the workflow simple.

Let me finalize: I'll skip the Respond to Webhook node and keep it simple. The webhook will still function.

Let me write the JSON now. I'll be thorough but not overcomplicate things.

One more consideration: the Set node typeVersion. In N8N, the Set node has gone through several versions. TypeVersion 3.3 or 3.4 is common for newer versions.

For the OpenAI node, typeVersion 1.8 is a reasonable choice for the chat operation.

For the Switch node, typeVersion 3 is common.

For the Slack node, typeVersion 2.3 or similar.

Let me finalize everything now and write the complete JSON.

I realize I should also think about whether the Set node after OpenAI is necessary. If I structure the OpenAI prompt to return ONLY the classification word (which I already planned), then the Switch node could directly check `{{ $json.choices[0].message.content }}`. But having a clean field is better.

Let me go with the Set node approach for cleanliness.

OK, writing the final JSON now.

Let me also double check: the user said "Dame el JSON completo del workflow" - they want the complete workflow JSON.

I should also include the `settings` and `pinData` fields if needed, but they're optional. I'll include the essential fields.

Here's my final attempt at the complete JSON:

```json
{
  "name": "Email Classifier Workflow",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "classify-email",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "webhook-node-id-001",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [240, 300],
      "webhookId": "classify-email"
    },
    {
      "parameters": {
        "keepOnlySet": true,
        "values": {
          "string": [
            {
              "name": "email",
              "value": "={{ $json.body.email }}"
            },
            {
              "name": "message",
              "value": "={{ $json.body.message }}"
            }
          ]
        },
        "options": {}
      },
      "id": "set-node-id-002",
      "name": "Extraer Datos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.3,
      "position": [480, 300]
    },
    {
      "parameters": {
        "operation": "chat",
        "modelId": "gpt-4o-mini",
        "messages": {
          "messageValues": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes. Clasifica el mensaje en una de estas categorías exactas: 'soporte', 'ventas' o 'otro'. Responde ÚNICAMENTE con la palabra de la categoría, sin explicaciones ni texto adicional."
            },
            {
              "role": "user",
              "content": "={{ $json.message }}"
            }
          ]
        },
        "options": {}
      },
      "id": "openai-node-id-003",
      "name": "OpenAI - Clasificar",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.8,
      "position": [720, 300],
      "credentials": {
        "openAiApi": {
          "id": "OPENAI_CREDENTIAL_ID",
          "name": "OpenAI Api"
        }
      }
    },
    {
      "parameters": {
        "keepOnlySet": true,
        "values": {
          "string": [
            {
              "name": "classification",
              "value": "={{ $json.choices[0].message.content.trim().toLowerCase() }}"
            },
            {
              "name": "email",
              "value": "={{ $json.email }}"
            },
            {
              "name": "message",
              "value": "={{ $json.message }}"
            }
          ]
        },
        "options": {}
      },
      "id": "set-node-id-004",
      "name": "Limpiar Clasificación",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.3,
      "position": [960, 300]
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
                    "leftValue": "={{ $json.classification }}",
                    "rightValue": "soporte",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
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
                    "leftValue": "={{ $json.classification }}",
                    "rightValue": "ventas",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
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
                    "leftValue": "={{ $json.classification }}",
                    "rightValue": "otro",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "outputKey": "otro"
            }
          ]
        },
        "options": {}
      },
      "id": "switch-node-id-005",
      "name": "Enviar a Canal",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [1200, 300]
    },
    {
      "parameters": {
        "operation": "post",
        "channel": "#support",
        "text": "🎧 *Nuevo mensaje de Soporte*\n📧 Email: {{ $json.email }}\n💬 Mensaje: {{ $json.message }}",
        "options": {}
      },
      "id": "slack-support-id-006",
      "name": "Slack -