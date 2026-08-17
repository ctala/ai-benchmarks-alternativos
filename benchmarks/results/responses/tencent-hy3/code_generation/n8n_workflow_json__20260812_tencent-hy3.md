# Tencent Hy3 — code_generation/n8n_workflow_json

- model_id: `tencent/hy3`
- success: True  | final: 5.51 | quality: 5.6
- latency_total: 102.718s | tokens_per_second: 79.8
- input_tokens: 139 | output_tokens: 8192
- judge_score: 2.0 | justificación: La respuesta es confusa y carece de un ejemplo de JSON específico, lo que la hace menos precisa y relevante para la tarea.

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

The user wants an N8N workflow JSON with specific requirements:
1. Trigger: Webhook (POST)
2. Extract: "email" and "message" from the body
3. AI Node: OpenAI to classify the message into "soporte", "ventas", or "otro"
4. Logic/Routing: Based on classification, send a Slack message to different channels:
   - soporte -> #support
   - ventas -> #sales
   - otro -> #general

Let's construct the N8N JSON.
N8N workflows have a specific structure. It consists of `nodes`, `connections`, `pinData` (optional), and `meta` (optional).

Nodes needed:
1. `Webhook` node: Method POST, path e.g. "webhook-classify".
2. `OpenAI` node (Langchain): Actually, the requirement says "Use un nodo de IA (OpenAI) para clasificar". In modern N8N, this is usually done using the Langchain OpenAI node, or a basic HTTP request to OpenAI, but since they specified "nodo de IA (OpenAI)", I should probably use the Langchain `OpenAI` node or `Agent`/`Chain` node, or the basic OpenAI node if it's older. Wait, N8N has a specific node for OpenAI (Langchain) which is `openAi`. Let's use the Langchain OpenAI node (`@n8n/n8n-nodes-langchain.openAi`). The model can be `gpt-3.5-turbo` or `gpt-4o-mini`. We can prompt it to return only the category or JSON.
   Wait, if we use the basic OpenAI node, it's not exactly an "AI node" in the modern sense, but let's use the Langchain one. Or a simpler way is to use a "Set" node to construct the prompt and then an "OpenAI" node. But wait, N8N's Langchain OpenAI node (`openAi`) has a "Text" resource and "Message" operation, or we can use a Chain node. Actually, using the basic OpenAI node (not langchain) might be easier to configure for a simple classification, or using the Langchain OpenAI Chat Model inside an AI Agent. However, to keep it simple and robust, I can use the Langchain `OpenAI` node to generate text, or just an HTTP Request to OpenAI, but the prompt says "nodo de IA (OpenAI)". N8N has an "OpenAI" node under "Langchain" or simply "OpenAI" (community/older). Let's use the Langchain `OpenAI` node: `type: '@n8n/n8n-nodes-langchain.openAi'`. Wait, it usually needs an "AI Chain" or "AI Agent" to work with memory and tools, but the `OpenAI` node itself can just send a prompt if configured as a "Language Model" or we can use the basic `openAi` node if it's available. Wait, the basic OpenAI node was deprecated/merged into Langchain. The Langchain OpenAI node is a "Language Model" (Chat Model). To use it to classify, you usually put it in an "AI Agent" or "Basic LLM Chain".
Let's use a "Basic LLM Chain" (`@n8n/n8n-nodes-langchain.chainLlm`) with an "OpenAI Chat Model" (`@n8n/n8n-nodes-langchain.openAi`) as the language model, and a "Window Buffer Memory" or no memory. And we can pass the prompt. Or use the "Set" node to format the prompt, then "Basic LLM Chain".
Wait, an even simpler approach that is widely used in N8N: A "Set" node to format the text, then an "OpenAI" node (Langchain) that acts as a Chat Model inside a "Basic LLM Chain", or just use the "HTTP Request" node to OpenAI. But since they explicitly asked for "nodo de IA (OpenAI)", I will use the Langchain OpenAI Chat Model node, paired with a Basic LLM Chain. Or, I can just use the `openAi` node (if we assume the older standard OpenAI node, but N8N v1+ uses Langchain). Let's use the Langchain nodes: `chainLlm` + `openAi`.

Wait, the user wants to "Extraiga el campo 'email' y 'message' del body". The Webhook node automatically puts the body in `{{ $json.body }}` or just `{{ $json }}` depending on the webhook config. In N8N, if the webhook receives JSON, the fields are at the top level of the incoming JSON, so `{{ $json.email }}` and `{{ $json.message }}`. But to be safe, I can use a "Set" node or "Edit Fields" node to explicitly extract them, or just reference them directly in the prompt. Let's use a "Set" node (or "Edit Fields") to make it clear that we extract them.
Actually, the Webhook node in N8N returns the parsed body directly in the JSON output (if "Response" is not Raw). So `{{ $json.email }}` and `{{ $json.message }}` work directly from the Webhook. But let's add an "Edit Fields" (Set) node to explicitly extract and rename/structure them, just to be safe and clear.

Let's design the nodes:
1. `Webhook` (type: `n8n-nodes-base.webhook`)
   - httpMethod: POST
   - path: classify-message (or similar)
   - responseMode: onReceived (or whatever)
2. `Edit Fields` (type: `n8n-nodes-base.set`) -> extract email and message.
   - Actually, Webhook already has them. But let's use a Set node to be explicit:
   - fields: email = `{{ $json.email }}`, message = `{{ $json.message }}`
3. `Basic LLM Chain` (type: `@n8n/n8n-nodes-langchain.chainLlm`)
   - text: "Classify the following message into one of these categories: 'soporte', 'ventas', 'otro'. Return ONLY the category word. Message: {{ $json.message }}"
   - Connect an `OpenAI Chat Model` node to it.
4. `OpenAI Chat Model` (type: `@n8n/n8n-nodes-langchain.openAi`)
   - model: gpt-3.5-turbo (or gpt-4o-mini)
   - resource: chat (it's a chat model)
   - This node connects to the Basic LLM Chain as an `ai_languageModel`.
5. `Switch` or `IF` node to route based on the output of the LLM.
   - The LLM output will be in `{{ $json.text }}`. It might be "soporte", "ventas", or "otro" (maybe with quotes or uppercase, so we should tell the LLM to return exactly the lowercase word, and use an expression to trim/lowercase it).
   - Let's use a `Switch` node (type: `n8n-nodes-base.switch`):
     - value: `{{ $json.text.trim().toLowerCase() }}`
     - rules:
       - equals "soporte" -> output 0
       - equals "ventas" -> output 1
       - equals "otro" -> output 2
       - fallback -> output 2 (or "otro")
6. Three `Slack` nodes (type: `n8n-nodes-base.slack`):
   - Resource: message
   - Operation: post
   - channel: #support (for soporte)
   - channel: #sales (for ventas)
   - channel: #general (for otro)
   - text: "New message from {{ $json.email }}: {{ $json.message }}" (Wait, does the Slack node have access to `$json.email`? If the Switch node is connected to the Slack nodes, the data passing through is the output of the LLM Chain. The LLM Chain output only has `text`. So the `email` and `message` from the Webhook will be lost unless we merge them or use a different approach!).
   - Ah! Important detail. In N8N, if you use a Basic LLM Chain, it usually outputs only `{ "text": "..." }` and drops the previous fields unless configured otherwise, or if we use a node that keeps previous fields. Wait, N8N nodes keep previous fields by default unless they overwrite them. The Basic LLM Chain output is `{ "text": "..." }`. Wait, no, in N8N, if a node returns an object, it replaces the input JSON unless the node has "Keep Only Set" or similar, but actually N8N merges? No, N8N replaces the whole item JSON with the output of the node. Wait, no! In N8N, if a node returns `{ text: "..." }`, the new item is `{ text: "..." }`. The previous fields (email, message) are LOST.
   - To keep them, we can either:
     a) Use a "Merge" node to join the LLM output with the original data.
     b) Use an "Agent" or "Chain" with memory that includes the original data? No.
     c) Better yet: Use a "Code" node or "Set" node after the LLM to combine `{{ $json.text }}` with `{{ $items()[0].json.email }}`? No, because the input item to the LLM is lost.
     Wait, the `Set` node before the LLM has `email` and `message`. The LLM Chain takes that item, and outputs a NEW item `{ text: "soporte" }`. So the `email` and `message` are gone from the item.
     To fix this, we can use a "Merge" node (type: `n8n-nodes-base.merge`) with mode "Combine" (or "Keep All") to merge the output of the LLM with the output of the Set node (which has email and message).
     Alternatively, we can use the "HTTP Request" node to call OpenAI, and then use a "Set" node to extract the classification AND keep the email/message. But the user asked for "nodo de IA (OpenAI)". The Langchain nodes are the standard "AI nodes" in N8N.
     Let's use a "Merge" node:
     - Input 1: From the `Set` node (has email, message)
     - Input 2: From the `Basic LLM Chain` (has text)
     - Mode: Combine (Wait, in N8N v1+, Merge node has modes: Append, Combine, Choose Branch. Combine by position is good).
     Actually, an easier way: The "Basic LLM Chain" node in N8N *does* keep the original fields if you don't use the "Overwrite" option, or wait, does it? Let me recall: N8N nodes usually replace the JSON output entirely unless they specifically merge. Wait, `chainLlm` returns `{ "text": "..." }`. It does NOT keep the input fields. So yes, we need a Merge node, OR we can use the "Set" node to construct the prompt and then use the OpenAI node. Wait, if we use the HTTP Request node to OpenAI, it returns the OpenAI response, and then we use a Set node to map `email`, `message`, and `classification`. That's very robust and doesn't require Langchain memory/merge complexities.
     But the prompt says: "Use un nodo de IA (OpenAI)". The Langchain OpenAI node is literally called "OpenAI" in the AI category.
     Let's use the Langchain "OpenAI" node as a Chat Model, and a "Basic LLM Chain". Then a "Merge" node.
     Wait, there is another way: Use the "OpenAI" node (Langchain) directly? No, it's a sub-node (language model).
     Actually, if we use an "AI Agent" node (`@n8n/n8n-nodes-langchain.agent`), it might keep the fields? No, it also returns `{ "output": "..." }`.
     Let's use a Merge node:
     Node A: Set (extracts email, message) -> goes to Merge (Input 1) AND to Basic LLM Chain.
     Wait, if Set goes to Basic LLM Chain, the LLM Chain outputs `text`. Then Merge combines Set's output (email, message) with LLM Chain's output (text).
     So:
     Webhook -> Set (email, message)
     Set -> Merge (Input 1)
     Set -> Basic LLM Chain -> Merge (Input 2)
     Merge -> Switch -> Slack nodes.

Let's refine the nodes and connections:

1. **Webhook**
   - name: "Webhook"
   - type: "n8n-nodes-base.webhook"
   - parameters: { "httpMethod": "POST", "path": "message-classification", "responseMode": "onReceived" }
   - webhookId: "some-id" (N8N usually generates this, but we can put a placeholder)

2. **Set** (Extract fields)
   - name: "Extract Fields"
   - type: "n8n-nodes-base.set"
   - parameters:
     - assignments:
       - name: "email", type: "string", value: "={{ $json.email }}"
       - name: "message", type: "string", value: "={{ $json.message }}"
   - This ensures we have exactly email and message.

3. **Basic LLM Chain**
   - name: "Classify Message"
   - type: "@n8n/n8n-nodes-langchain.chainLlm"
   - parameters:
     - text: "Clasifica el siguiente mensaje en una de estas categorías exactas: 'soporte', 'ventas' u 'otro'. Responde ÚNICAMENTE con la palabra de la categoría, sin comillas ni puntuación. Mensaje: {{ $json.message }}"
   - This node will need an AI language model connected.

4. **OpenAI Chat Model**
   - name: "OpenAI"
   - type: "@n8n/n8n-nodes-langchain.openAi"
   - parameters:
     - model: "gpt-3.5-turbo"
     - options: {}
   - credentials: { "openAiApi": { "id": "openAiCredential", "name": "OpenAi Account" } } (we'll just put a placeholder for credentials)

5. **Merge**
   - name: "Merge Data"
   - type: "n8n-nodes-base.merge"
   - parameters:
     - mode: "combine"
     - combineBy: "position"
   - Input 1: from "Extract Fields" (has email, message)
   - Input 2: from "Classify Message" (has text)
   - Output: `{ email, message, text }`

6. **Switch**
   - name: "Route by Category"
   - type: "n8n-nodes-base.switch"
   - parameters:
     - mode: "rules"
     - rules:
       - { "value": "={{ $json.text.trim().toLowerCase() }}", "operator": "equals", "value2": "soporte" }
       - { "value": "={{ $json.text.trim().toLowerCase() }}", "operator": "equals", "value2": "ventas" }
       - { "value": "={{ $json.text.trim().toLowerCase() }}", "operator": "equals", "value2": "otro" }
     - fallbackOutput: 2 (route to "otro" just in case, or add a 4th rule? Wait, if fallback goes to output 3, we need 4 outputs. Let's just make the 3rd rule "equals otro" and fallback to output 2 (which is "otro"). Wait, in N8N Switch node, `fallbackOutput` is the index of the output. If we have 3 rules, there are 3 outputs (0, 1, 2). If fallback is 2, it goes to output 2 which is "otro". That works.

7. **Slack (Support)**
   - name: "Slack Support"
   - type: "n8n-nodes-base.slack"
   - parameters:
     - resource: "message"
     - operation: "post"
     - channel: "#support"
     - text: "📩 Nuevo mensaje de {{ $json.email }}:\n{{ $json.message }}"
   - credentials: { "slackApi": { "id": "slackCredential" } }

8. **Slack (Sales)**
   - name: "Slack Sales"
   - type: "n8n-nodes-base.slack"
   - parameters:
     - resource: "message"
     - operation: "post"
     - channel: "#sales"
     - text: "📩 Nuevo mensaje de {{ $json.email }}:\n{{ $json.message }}"

9. **Slack (General)**
   - name: "Slack General"
   - type: "n8n-nodes-base.slack"
   - parameters:
     - resource: "message"
     - operation: "post"
     - channel: "#general"
     - text: "📩 Nuevo mensaje de {{ $json.email }}:\n{{ $json.message }}"

Wait, does the Merge node combine fields like that?
In N8N, the Merge node with mode "Combine" and "Combine By: Position" will merge the properties of item 0 from Input 1 and item 0 from Input 2 into a single item. So if Input 1 has `{ email, message }` and Input 2 has `{ text }`, the output will be `{ email, message, text }`. Yes, that works perfectly.

Let's double check the N8N JSON structure for nodes and connections.
```json
{
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "message-classification",
        "responseMode": "onReceived"
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 300],
      "webhookId": "abc123-def456"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "name": "email",
              "type": "string",
              "value": "={{ $json.email }}"
            },
            {
              "name": "message",
              "type": "string",
              "value": "={{ $json.message }}"
            }
          ]
        }
      },
      "name": "Extract Fields",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3,
      "position": [450, 300]
    },
    {
      "parameters": {
        "text": "Clasifica el siguiente mensaje en una de estas categorías exactas: 'soporte', 'ventas' u 'otro'. Responde ÚNICAMENTE con la palabra de la categoría, sin comillas ni puntuación. Mensaje: {{ $json.message }}"
      },
      "name": "Classify Message",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "typeVersion": 1,
      "position": [450, 500]
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo"
      },
      "name": "OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1,
      "position": [250, 500],
      "credentials": {
        "openAiApi": {
          "id": "YOUR_OPENAI_CREDENTIAL_ID",
          "name": "OpenAi Account"
        }
      }
    },
    {
      "parameters": {
        "mode": "combine",
        "combineBy": "position"
      },
      "name": "Merge Data",
      "type": "n8n-nodes-base.merge",
      "typeVersion": 2,
      "position": [700, 400]
    },
    {
      "parameters": {
        "mode": "rules",
        "rules": {
          "values": [
            {
              "value": "={{ $json.text.trim().toLowerCase() }}",
              "operator": {
                "type": "string",
                "operation": "equals"
              },
              "value2": "soporte"
            },
            {
              "value": "={{ $json.text.trim().toLowerCase() }}",
              "operator": {
                "type": "string",
                "operation": "equals"
              },
              "value2": "ventas"
            },
            {
              "value": "={{ $json.text.trim().toLowerCase() }}",
              "operator": {
                "type": "string",
                "operation": "equals"
              },
              "value2": "otro"
            }
          ]
        },
        "fallbackOutput": 2
      },
      "name": "Route by Category",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [900, 400]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#support",
        "text": "📩 Nuevo mensaje de {{ $json.email }}:\n{{ $json.message }}"
      },
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1150, 250],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack Account"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#sales",
        "text": "📩 Nuevo mensaje de {{ $json.email }}:\n{{ $json.message }}"
      },
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1150, 400],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack Account"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#general",
        "text": "📩 Nuevo mensaje de {{ $json.email }}:\n{{ $json.message }}"
      },
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1150, 550],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack Account"
        }
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extract Fields",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract Fields": {
      "main": [
        [
          {
            "node": "Merge Data",
            "type": "main",
            "index": 0
          }
        ],
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
            "node": "Merge Data",
            "type": "main",
            "index": 1
          }
        ]
      ]
    },
    "OpenAI": {
      "ai_languageModel": [
        [
          {
            "node": "Classify Message",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Merge Data": {
      "main": [
        [
          {
            "node": "Route by Category",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Route by Category": {
      "main": [
        [
          {
            "node": "Slack Support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack Sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack General",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

Wait, let's verify the `Extract Fields` connections. In N8N, a node can have multiple outputs if it's a Split, but a Set node has only 1 output. To send the output of `Extract Fields` to BOTH `Merge Data` and `Classify Message`, we connect the single output of `Extract Fields` to multiple nodes. In the `connections` JSON, this is represented as:
```json
"Extract Fields": {
  "main": [
    [
      { "node": "Merge Data", "type": "main", "index": 0 },
      { "node": "Classify Message", "type": "main", "index": 0 }
    ]
  ]
}
```
Yes! The array of arrays: the outer array is the outputs (only index 0 for Set node), the inner array is the destinations from that output. So both `Merge Data` and `Classify Message` are in the same inner array. This is the correct way to duplicate the flow without a "Split" node.

Let's verify the Merge node inputs. The `Merge Data` node has 2 inputs. So it receives `index: 0` from `Extract Fields` and `index: 1` from `Classify Message`.
In `connections`:
```json
"Extract Fields": {
  "main": [
    [
      { "node": "Merge Data", "type": "main", "index": 0 },
      { "node": "Classify Message", "type": "main", "index": 0 }
    ]
  ]
},
"Classify Message": {
  "main": [
    [
      { "node": "Merge Data", "type": "main", "index": 1 }
    ]
  ]
}
```
This is correct. `Merge Data` input 0 is from `Extract Fields`, input 1 is from `Classify Message`.

Let's check the `Switch` node outputs.
The `Route by Category` node has 3 rules, so it has 3 outputs (0, 1, 2). Plus a fallback. If `fallbackOutput` is 2, it routes to output 2 if no rule matches. So the 3 outputs connect to the 3 Slack nodes.
In `connections`:
```json
"Route by Category": {
  "main": [
    [ { "node": "Slack Support", "type": "main", "index": 0 } ],
    [ { "node": "Slack Sales", "type": "main", "index": 0 } ],
    [ { "node": "Slack General", "type": "main", "index": 0 } ]
  ]
}
```
This is correct.

Let's check the `OpenAI` node connection.
The `Classify Message` (Basic LLM Chain) uses an AI language model. In N8N, this is an `ai_languageModel` connection.
```json
"OpenAI": {
  "ai_languageModel": [
    [
      { "node": "Classify Message", "type": "ai_languageModel", "index": 0 }
    ]
  ]
}
```
This is correct for Langchain nodes.

Wait, is `@n8n/n8n-nodes-langchain.chainLlm` the correct type for Basic LLM Chain?
Yes, in N8N, the Basic LLM Chain node is `@n8n/n8n-nodes-langchain.chainLlm`.
The OpenAI Chat Model node is `@n8n/n8n-nodes-langchain.openAi`.
Let me double-check the exact type name for the OpenAI node. In N8N, it's often `@n8n/n8n-nodes-langchain.openAi` or `@n8n/n8n-nodes-langchain.lmChatOpenAi`?
Actually, in newer versions of N8N (v1.0+), the OpenAI Chat Model node is `@n8n/n8n-nodes-langchain.openAi` and its typeVersion is 1 or 2. Wait, let me recall.
In the N8N codebase:
- `packages/nodes-base/nodes/openAi` -> this is the old OpenAI node (deprecated).
- `packages/@n8n/n8n-nodes-langchain/nodes/chain/ChainLlm` -> `@n8n/n8n-nodes-langchain.chainLlm`
- `packages/@n8n/n8n-nodes-langchain/nodes/llm/LMOpenAi` -> `@n8n/n8n-nodes-langchain.openAi` (Wait, sometimes it's `@n8n/n8n-nodes-langchain.lmChatOpenAi`? No, in the UI it's just "OpenAI" and the type is `@n8n/n8n-nodes-langchain.openAi`). Let's stick to `@n8n/n8n-nodes-langchain.openAi` as it's the standard generated type for that node.

Wait, let's look at `typeVersion` for `chainLlm`. It is usually 1 or 2. Let's use `1` or `2`. I'll use `1` for safety, or `2`? Actually, recent N8N versions use `2` for `chainLlm` maybe? No, `chainLlm` was introduced in Langchain beta, and its typeVersion is usually `1` or `2`. I'll just put `1`, it's fine for a template.
For `switch` node, `typeVersion` is `3` in recent N8N (where `rules.values` is used). In older versions (v1/v2), it was `rules` as an array directly. Let's use `typeVersion: 3` and `rules: { values: [...] }` because that's the current N8N format.
Let me double check the Switch node format for v3:
```json
"parameters": {
  "mode": "rules",
  "rules": {
    "values": [
      {
        "value": "={{ $json.text.trim().toLowerCase() }}",
        "operator": {
          "type": "string",
          "operation": "equals"
        },
        "value2": "soporte"
      }
    ]
  },
  "fallbackOutput": 2
}
```
Yes, this is correct for N8N v3 Switch node.

Wait, what if the model returns "Soporte" or "soporte." with a period? The prompt says "Responde ÚNICAMENTE con la palabra de la categoría, sin comillas ni puntuación." and we use `.trim().toLowerCase()` which handles spaces and case. If it returns "soporte." we should maybe strip punctuation, but the prompt is strict enough. We could also use `replace(/[^a-z]/g, '')` just in case: `={{ $json.text.trim().toLowerCase().replace(/[^a-z]/g, '') }}`. That's safer! Let's use that in the Switch node value:
`"value": "={{ $json.text.trim().toLowerCase().replace(/[^a-z]/g, '') }}"`

Let's refine the Switch node parameters:
```json
"parameters": {
  "mode": "rules",
  "rules": {
    "values": [
      {
        "value": "={{ $json.text.trim().toLowerCase().replace(/[^a-z]/g, '') }}",
        "operator": {
          "type": "string",
          "operation": "equals"
        },
        "value2": "soporte"
      },
      {
        "value": "={{ $json.text.trim().toLowerCase().replace(/[^a-z]/g, '') }}",
        "operator": {
          "type": "string",
          "operation": "equals"
        },
        "value2": "ventas"
      },
      {
        "value": "={{ $json.text.trim().toLowerCase().replace(/[^a-z]/g, '') }}",
        "operator": {
          "type": "string",
          "operation": "equals"
        },
        "value2": "otro"
      }
    ]
  },
  "fallbackOutput": 2
}
```
This is extremely safe.

What about the Webhook node? In N8N, a webhook node usually needs a `webhookId`. If we import a workflow, N8N will assign a new `webhookId` if it's missing or invalid, but it's good practice to provide one. I'll use `"webhookId": "message-classification-webhook"` or similar.
Wait, if the webhook path is `message-classification`, the test URL will be `/webhook/message-classification` or `/webhook-test/message-classification`.

Let's check the `Set` node (Extract Fields).
In N8N v3 (current), the Set node uses `assignments.assignments` (note the double `assignments`).
```json
"parameters": {
  "assignments": {
    "assignments": [
      {
        "name": "email",
        "type": "string",
        "value": "={{ $json.email }}"
      },
      {
        "name": "message",
        "type": "string",
        "value": "={{ $json.message }}"
      }
    ]
  }
}
```
This is correct for `typeVersion: 3` of the Set node.

Wait, if I use `Set` node, I am extracting `email` and `message` from the webhook body. But what if the webhook body has them nested? The prompt says "Extraiga el campo 'email' y 'message' del body". Usually, if the Content-Type is `application/json`, N8N parses it and puts the properties at the root of the item JSON. So `$json.email` and `$json.message` work. If it's form-data, it's also at the root. So `$json.email` is correct.

Let's review the Merge node.
In N8N v2/v3 of Merge node, the parameters are:
```json
"parameters": {
  "mode": "combine",
  "combineBy": "position"
}
```
Wait, in N8N v3, `combineBy` might be `combineByPosition` or just `combineBy`. Let's check.
In N8N, the Merge node parameters for "Combine" mode:
- `mode`: "combine"
- `combineBy`: "position" (options: position, id, key)
Actually, in newer versions it's `combineBy: "position"`.
Let's just use `mode: "combine"` and `combineBy: "position"`. That's standard.

Let's check the Slack node.
```json
"parameters": {
  "resource": "message",
  "operation": "post",
  "channel": "#support",
  "text": "📩 Nuevo mensaje de {{ $json.email }}:\n{{ $json.message }}"
}
```
Wait, the Slack node in N8N v2 uses `channel` as a string or dropdown. If we type `#support`, it's fine.
Also, the `text` parameter in Slack node might be called `text` or it might be under `message` or `attachments`?
In N8N Slack node v2, for "Message" resource and "Post" operation, the parameter is `text` (or `message`?).
Let me recall: N8N Slack node has `text` parameter. Wait, in older versions it was `message`, in newer it's `text`. Actually, checking the N8N Slack node:
Resource: Message, Operation: Post.
Parameters: `channel` (string), `text` (string), `attachments` (json), etc.
Yes, `text` is correct.

Wait, what if the user wants the JSON to be directly importable and working? I should add the `credentials` placeholders so