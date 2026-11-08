# DeepSeek V4 Flash 0731 — code_generation/n8n_workflow_json

- model_id: `deepseek/deepseek-v4-flash-0731`
- success: True  | final: 6.25 | quality: 6.24
- latency_total: 68.54s | tokens_per_second: 252.9
- input_tokens: 206 | output_tokens: 17335
- judge_score: 2.6 | justificación: 

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

We need generate n8n workflow JSON. Need decide exact node types and parameters. Let's craft robustly.

Need maybe include "OpenAI" node type. Let's settle.

I can use "n8n-nodes-base.openAi" with resource "chat", operation "complete". Need ensure parameters. Let's recall from n8n docs for OpenAI node:
- Resource: "Chat"
- Operation: "Complete"
- Model: "gpt-4o-mini"
- Messages: array of objects with `role` and `content`.
- Options: maybe `temperature`.

The node type maybe "n8n-nodes-base.openAi" and typeVersion 1? Let's recall from n8n: In n8n, the OpenAI node type is "n8n-nodes-base.openAi" for version 1? Actually community nodes can have "n8n-nodes-base.openAi" version 1.2? Hmm.

Let's search memory: In n8n, the "OpenAI" node is in "Machine Learning" category, type "n8n-nodes-base.openAi". It has typeVersion 1? In n8n, built-in nodes have typeVersion numbers like 1, 2, 2.1. For OpenAI, maybe typeVersion 1.2? Need not exact? If wrong, import may fail.

Maybe use "n8n-nodes-base.openAi" typeVersion 2? Let's see. In n8n, "OpenAI" node was updated to typeVersion 2? Hmm.

Alternatively, use "HTTP Request" node to call OpenAI API. That is definitely valid and easier to control. But user said "Use un nodo de IA (OpenAI)" - an HTTP request to OpenAI is not "nodo de IA", but it's a request. Better to use actual OpenAI node.

Maybe use "Execute Workflow" no.

Let's find exact n8n OpenAI node parameters from memory.

I remember n8n nodes include:
- "OpenAI" node with resource "Chat" operation "Complete" has parameters:
```
{
  "resource": "chat",
  "operation": "complete",
  "model": "gpt-3.5-turbo",
  "messages": {
    "values": [
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
The output from OpenAI node for chat completion might be:
```
{
  "success": true,
  "data": {
    "choices": [
      {
        "message": {
          "role": "assistant",
          "content": "soporte"
        }
      }
    ]
  }
}
```
Actually n8n nodes often return `{ data: ... }`? Let's recall from n8n: The OpenAI node's "Complete" operation returns the API response directly, e.g., `{ "id": "chatcmpl-...", "object": "chat.completion", "choices": [...] }`. But if using "Simplify" option, it might return `{ "content": "..." }`? There is an option "Simplify" maybe. Hmm.

To be safe, in Code node, we can handle multiple output structures:
```
let content = openAiResponse.choices?.[0]?.message?.content
  || openAiResponse.data?.choices?.[0]?.message?.content
  || openAiResponse.output
  || openAiResponse.message?.content
  || '';
```
This covers.

Need maybe include "options": { "temperature": 0, "simplify": true }? If simplify true, output maybe `{ content: "..." }`? Let's handle.

Need maybe "OpenAI" node needs credentials. In JSON, credentials object:
```
"credentials": {
  "openAiApi": "OPENAI_API_KEY"
}
```
Need know credential type name. For OpenAI node, credential type is "openAiApi". In n8n, credential names: "openAiApi". Yes.

Need maybe Slack node credential type "slackApi". Slack node parameters:
```
{
  "parameters": {
    "operation": "postMessage",
    "channel": "#support",
    "text": "=Nuevo mensaje de {{ $json.email }}: {{ $json.message }}"
  },
  "type": "n8n-nodes-base.slack",
  "typeVersion": 2,
  "credentials": {
    "slackApi": "Slack_Credentials"
  }
}
```
Need "channel" can be "#support" or "support"? Slack API channel can be "#support". Good.

Need maybe "text" expression. In n8n, expressions in parameters use `={{ ... }}`. Need include.

Need maybe "Slack" node operation "postMessage" is under resource "Chat"? Let's recall: Slack node has "Resource" "Chat" and "Operation" "Post". Actually in n8n Slack node, parameters:
```
"resource": "chat",
"operation": "postMessage",
"channel": "#general",
"text": "..."
```
Need include resource. Let's set:
```
"resource": "chat",
"operation": "postMessage",
"channel": "#support",
"text": "={{ ... }}"
```
Maybe "postMessage" is operation. Good.

Need maybe Slack node typeVersion 2? Slack node typeVersion 1? Let's use typeVersion 2.2? Hmm.

Need maybe "Switch" node parameters. Let's design Switch node.

n8n Switch node type "n8n-nodes-base.switch" typeVersion 2. Parameters:
```
{
  "parameters": {
    "dataPropertyName": "classification",
    "rules": {
      "values": [
        {
          "value": "soporte",
          "type": "string",
          "output": 0
        },
        {
          "value": "ventas",
          "type": "string",
          "output": 1
        },
        {
          "value": "otro",
          "type": "string",
          "output": 2
        }
      ]
    }
  },
  "type": "n8n-nodes-base.switch",
  "typeVersion": 2,
  "position": [...]
}
```
But need understand Switch node rules. In n8n, switch node v2:
- "dataPropertyName": "field" or expression.
- "rules": { "values": [ { "value": "soporte", "type": "string", "regex": "", "ignoreCase": true? } ] }
- "options": { "fallbackOutput": "3" }? Actually to route to default, set "fallbackOutput": "2" or maybe "fallbackOutput": 3? Need.

Let's recall n8n Switch node v2. It has "Mode" "Expression" or "Rules"? There is "dataPropertyName" and "rules". Each rule has "value", "type", "regex", "ignoreCase". If a rule matches, output index equals rule index. There is "fallbackOutput" to route unmatched to a particular output. In our case, classification should be exactly one of three. But if not, fallback to "otro". Need set "fallbackOutput": 2 (third output). But if we have three outputs, fallback output index 2. Need ensure.

Maybe simpler: Use three "IF" nodes? No.

Need maybe use "Switch" with "mode": "expression" and "conditions"? Hmm.

Let's recall n8n Switch node v3? In current n8n, Switch node has "Mode" "Rules" and "Expression". For rules, parameters:
```
{
  "mode": "rules",
  "dataPropertyName": "classification",
  "rules": {
    "values": [
      { "value": "soporte", "type": "string", "regex": "" },
      { "value": "ventas", "type": "string", "regex": "" },
      { "value": "otro", "type": "string", "regex": "" }
    ]
  },
  "options": {
    "fallbackOutput": "2"
  }
}
```
Need maybe "type": "string" is default. "ignoreCase": true? Could include.

Need maybe "output" not in rule; rule index determines output. So no need "output". Let's include no "output". But if typeVersion 2, rules values maybe no output. Need.

Let's craft with typeVersion 2.2? Hmm.

Maybe use "Switch" node typeVersion 3? Need know. Let's use typeVersion 2, likely okay.

Need maybe "connections" object. Need map node connections.

Nodes and positions:
- Webhook at [0,0]
- Extraer at [200,0]
- OpenAI at [400,0]
- Normalizar (Code) at [600,0]
- Switch at [800,0]
- Slack Soporte at [1000,-200]
- Slack Ventas at [1000,0]
- Slack Otro at [1000,200]

Connections:
- Webhook -> Extraer: main output 0 -> input 0
- Extraer -> OpenAI
- OpenAI -> Normalizar
- Normalizar -> Switch
- Switch output 0 -> Slack Soporte
- Switch output 1 -> Slack Ventas
- Switch output 2 -> Slack Otro

Need include "connections" format:
```
"connections": {
  "Webhook": {
    "main": [
      [
        { "node": "Extraer email y message", "type": "main", "index": 0 }
      ]
    ]
  },
  ...
}
```
Need exact. In n8n, connections:
```
{
  "NodeName": {
    "main": [
      [ { "node": "Target", "type": "main", "index": 0 } ]
    ]
  }
}
```
For multiple outputs, each output is an array of arrays. For Switch with 3 outputs:
```
"Switch": {
  "main": [
    [
      { "node": "Slack Soporte", "type": "main", "index": 0 }
    ],
    [
      { "node": "Slack Ventas", "type": "main", "index": 0 }
    ],
    [
      { "node": "Slack Otro", "type": "main", "index": 0 }
    ]
  ]
}
```
Need if "index" is input index. Good.

Need maybe "OpenAI" node has no "main" output? It has one. Good.

Need maybe include "settings": { "executionOrder": "v1" }? In workflow JSON, top-level "settings": { "executionOrder": "v1" } maybe. Need include.

Need maybe include "pinData" no.

Need maybe include "active": false, "tags": [], "meta": { "templateCredsSetupCompleted": false }? Not necessary.

Need maybe include "id": "workflow-id" and "meta". Could include.

Need maybe include "nodes" each with "id" unique. Need generate UUIDs? Could use simple strings. n8n import may accept.

Need maybe include "webhookId" for Webhook node. Need unique.

Need maybe include "position" array.

Need maybe "typeVersion" for each node. Let's choose:
- Webhook: typeVersion 2
- Set: typeVersion 2
- OpenAI: typeVersion 1? Let's decide.
- Code: typeVersion 2
- Switch: typeVersion 2
- Slack: typeVersion 2

Need maybe OpenAI node typeVersion 2? Let's search memory. In n8n, "OpenAI" node's typeVersion is 1? I recall from n8n node source: `"type": "n8n-nodes-base.openAi", "typeVersion": 1` maybe. But there is also "n8n-nodes-base.openAi" typeVersion 2? Let's think.

n8n node versioning: Many nodes have typeVersion 1 and 2. For OpenAI, because it supports multiple resources, maybe version 1.2? Actually n8n uses typeVersion as number, e.g., 1, 1.1, 2. In workflow JSON, typeVersion can be 1.1. For OpenAI, I remember seeing `"typeVersion": 2` in n8n workflows? Let's not worry too much.

Need maybe "OpenAI" node "resource" "completion" vs "chat". Let's choose "chat" and "complete". Need "messages" parameter. In n8n, if using "Complete" operation, the node may require "Messages" as fixed collection. Need structure:
```
"messages": {
  "values": [
    {
      "role": "system",
      "content": "Clasifica el mensaje..."
    },
    {
      "role": "user",
      "content": "={{ $json.message }}"
    }
  ]
}
```
But note: The input to OpenAI node is the output of "Extraer" node, which has top-level `email` and `message`. So `$json.message` works. Need maybe include email in prompt? We can include "Mensaje: {{ $json.message }}". Good.

Need maybe "options": { "temperature": 0 }.

Need maybe "text" in Slack nodes uses `$json.email` and `$json.message` from Code node (Normalizar). Since Slack nodes receive from Switch, which passes through Code node output. So `$json.email` and `$json.message` are available. Good.

Need maybe "Slack" node text expression:
```
"text": "=Nuevo mensaje de {{ $json.email }}:\n{{ $json.message }}"
```
Need in JSON string, newline as `\n`. Good.

Need maybe "channel" parameter with "#support". Good.

Need maybe "Slack" node "resource": "chat", "operation": "postMessage". Let's include.

Need maybe "Code" node parameters:
```
"parameters": {
  "jsCode": "const openAiResponse = $input.first().json;\nlet content = openAiResponse.choices?.[0]?.message?.content || openAiResponse.data?.choices?.[0]?.message?.content || openAiResponse.content || '';\nlet classification = content.trim().toLowerCase();\nif (classification.includes('soporte')) { classification = 'soporte'; } else if (classification.includes('ventas')) { classification = 'ventas'; } else { classification = 'otro'; }\nconst original = $('Extraer email y message').first().json;\nreturn [{ json: { email: original.email, message: original.message, classification } }];"
}
```
Need ensure code node can use `$input.first().json` and `$('Extraer email y message').first().json`. In n8n Code node, `$input` is an object with `.first()`? Yes. `$('NodeName')` returns object with `.first()`? Need maybe `$('Extraer email y message').first().json` works. If not, `$node['Extraer email y message'].json`? Let's use `$('Extraer email y message').first().json` because it's documented for expressions? Actually in expressions, `$('NodeName').first()` is valid. In Code node, `$('NodeName')` returns a `NodeApi` object? Let's recall: In Code node, you can use `$('NodeName').first().json`? I have seen examples:
```
const item = $input.first().json;
const other = $('Other Node').first().json;
```
Yes.

Need maybe if "Extraer email y message" node name has spaces, expression string okay.

Need maybe "OpenAI" node output path. Need maybe if n8n OpenAI node with "Simplify" option returns `{ content: "..." }`. We handle.

Need maybe "OpenAI" node "options" includes "simplify": true? If simplify true, output might be `{ content: "soporte" }`. Let's include "options": { "temperature": 0, "simplify": true }? Need know if "simplify" option exists. It might be "Simplify" option for "Chat" operation. If set, output is simplified. But not sure. We can include "options": { "temperature": 0 } only.

Need maybe "OpenAI" node "messages" content expression. Need include system prompt:
"Eres un clasificador. Clasifica el siguiente mensaje como 'soporte', 'ventas' o 'otro'. Responde solo con una de esas palabras."
User content:
"Mensaje: {{ $json.message }}"
Need maybe include email? Not necessary.

Need maybe "OpenAI" node "model": "gpt-4o-mini" or "gpt-4o". Use "gpt-4o-mini" for low cost. Need maybe model ID accepted by n8n. Good.

Need maybe "OpenAI" node credentials:
```
"credentials": {
  "openAiApi": {
    "id": "1",
    "name": "OpenAI"
  }
}
```
In n8n workflow JSON, credentials can be:
```
"credentials": {
  "openAiApi": "OpenAI account"
}
```
Actually in n8n, node credentials are object with credential type name and a string name or object? Let's recall: In workflow JSON, node has `"credentials": { "openAiApi": { "id": "1", "name": "OpenAI" } }`? I think when exporting, credentials are:
```
"credentials": {
  "slackApi": {
    "id": "1",
    "name": "Slack"
  }
}
```
But in many JSON examples:
```
"credentials": {
  "openAiApi": "OpenAI"
}
```
Need maybe no credentials? If user imports, they'll need select. To be safe, use object with name "OpenAI" and id "OPENAI_CREDENTIAL_ID". But if user doesn't have, import may fail? Actually credentials are not imported, they are referenced by name maybe. Better to include placeholder:
```
"credentials": {
  "openAiApi": {
    "name": "OpenAI"
  }
}
```
Need maybe "openAiApi" is credential type. For Slack:
```
"credentials": {
  "slackApi": {
    "name": "Slack"
  }
}
```
This should be okay.

Need maybe "webhook" node "webhookId" unique. We can use "webhook-uuid-1234".

Need maybe "id" fields for nodes. n8n requires unique id? In workflow JSON, nodes have "id" string. We can set.

Need maybe "name" of workflow: "Clasificar y enviar a Slack".

Let's craft final JSON. Need ensure no comments, valid JSON.

Let's write nodes:

1. Webhook:
```
{
  "parameters": {
    "httpMethod": "POST",
    "path": "classify-message",
    "responseMode": "onReceived",
    "options": {}
  },
  "id": "webhook",
  "name": "Webhook",
  "type": "n8n-nodes-base.webhook",
  "typeVersion": 2,
  "position": [0, 0],
  "webhookId": "webhook-classify-message-001"
}
```

2. Extraer email y message:
```
{
  "parameters": {
    "assignments": {
      "assignments": [
        {
          "id": "assign-email",
          "name": "email",
          "value": "={{ $json.body.email }}",
          "type": "string"
        },
        {
          "id": "assign-message",
          "name": "message",
          "value": "={{ $json.body.message }}",
          "type": "string"
        }
      ]
    },
    "options": {}
  },
  "id": "set-email-message",
  "name": "Extraer email y message",
  "type": "n8n-nodes-base.set",
  "typeVersion": 2,
  "position": [200, 0]
}
```
Need if Set node v2 uses "assignments" or "values"? Let's verify. In n8n Set node v2, parameters:
```
{
  "parameters": {
    "assignments": {
      "assignments": [
        {
          "name": "field",
          "value": "value",
          "type": "string"
        }
      ]
    }
  }
}
```
I think yes. But there is also "values" in "Set" node v1. Let's use v2.

Need maybe "type" field in assignment can be "string", "number", "boolean", "array", "object". Good.

3. OpenAI:
```
{
  "parameters": {
    "resource": "chat",
    "operation": "complete",
    "model": "gpt-4o-mini",
    "messages": {
      "values": [
        {
          "role": "system",
          "content": "Eres un clasificador. Clasifica el mensaje del usuario como 'soporte', 'ventas' o 'otro'. Responde solo con una de esas palabras."
        },
        {
          "role": "user",
          "content": "Mensaje: {{ $json.message }}"
        }
      ]
    },
    "options": {
      "temperature": 0
    }
  },
  "id": "openai-classify",
  "name": "Clasificar con OpenAI",
  "type": "n8n-nodes-base.openAi",
  "typeVersion": 2,
  "position": [400, 0],
  "credentials": {
    "openAiApi": {
      "name": "OpenAI"
    }
  }
}
```
Need maybe "typeVersion" for OpenAI should be 1? Let's set 2? Hmm. If typeVersion 2 doesn't exist, import error. Let's research from memory. In n8n, "OpenAI" node has typeVersion 1? Let's recall from n8n workflow examples:
```
{
  "parameters": {
    "resource": "chat",
    "operation": "complete",
    "model": "gpt-3.5-turbo",
    "messages": {
      "values": [...]
    }
  },
  "type": "n8n-nodes-base.openAi",
  "typeVersion": 1,
  "position": [...]
}
```
Maybe typeVersion 1 is safer. But if current n8n uses version 2? Let's think. The OpenAI node was introduced in n8n 0.??. It had "resource": "text", "operation": "complete". Later updated to "chat" with typeVersion 1? Maybe no version 2. I can set typeVersion 1. But if user has n8n 1.x, typeVersion 1 still works. Let's use typeVersion 1. But "messages" parameter might not be in typeVersion 1? Hmm.

Let's recall from n8n node "OpenAI" version 1.0 parameters:
- Resource: "Completion" and "Edit" maybe.
- Operation: "Create"
- Prompt: "text-davinci-003"
- Model: "text-davinci-003"
- Max Tokens.
No "chat" resource? Actually n8n's OpenAI node originally used OpenAI's completions endpoint. Later added chat completions. In n8n, node type "openAi" with typeVersion 1 may have resource "text" and operation "complete". The "chat" resource might be typeVersion 2. Hmm.

Let's search memory from n8n docs: "OpenAI" node (n8n-nodes-base.openAi) supports:
- Resource: "Chat" (v2?) and "Image" etc.
There is "OpenAI" node "Chat" operation "Complete" introduced in n8n 0.218.0? It may be typeVersion 2. The old "OpenAI" node typeVersion 1 had "Text" resource. So typeVersion 2 for chat. Let's use typeVersion 2.

Need maybe if typeVersion 2, parameters "resource": "chat", "operation": "complete" okay.

4. Code:
```
{
  "parameters": {
    "jsCode": "const openAiResponse = $input.first().json;\nlet content = openAiResponse.choices?.[0]?.message?.content || openAiResponse.data?.choices?.[0]?.message?.content || openAiResponse.content || '';\nlet classification = content.trim().toLowerCase();\nif (classification.includes('soporte')) classification = 'soporte';\nelse if (classification.includes('ventas')) classification = 'ventas';\nelse classification = 'otro';\nconst original = $('Extraer email y message').first().json;\nreturn [{ json: { email: original.email, message: original.message, classification } }];"
  },
  "id": "code-normalize",
  "name": "Normalizar clasificación",
  "type": "n8n-nodes-base.code",
  "typeVersion": 2,
  "position": [600, 0]
}
```
Need maybe Code node typeVersion 2? In n8n, Code node typeVersion 1 and 2. TypeVersion 2 uses `jsCode` parameter? I think yes. TypeVersion 1 uses `jsCode` too. Use 2.

5. Switch:
```
{
  "parameters": {
    "mode": "rules",
    "dataPropertyName": "classification",
    "rules": {
      "values": [
        {
          "value": "soporte",
          "type": "string",
          "regex": "",
          "ignoreCase": true
        },
        {
          "value": "ventas",
          "type": "string",
          "regex": "",
          "ignoreCase": true
        },
        {
          "value": "otro",
          "type": "string",
          "regex": "",
          "ignoreCase": true
        }
      ]
    },
    "options": {
      "fallbackOutput": "2"
    }
  },
  "id": "switch-classification",
  "name": "Clasificación",
  "type": "n8n-nodes-base.switch",
  "typeVersion": 2,
  "position": [800, 0]
}
```
Need maybe "mode" parameter? In Switch node v2, there is "mode": "rules" maybe. If not, extra parameter okay? It may be ignored? Better include? Let's recall n8n Switch node v2 parameters:
- "dataPropertyName"
- "rules"
- "options"
No "mode" maybe. In v3, "mode" is "rules" or "expression". Hmm. If we include "mode", maybe okay? But if schema doesn't allow, import may fail? n8n is lenient? Not sure. Better not include unknown "mode" if not needed. But for v2, maybe "mode" is required. Let's check memory: Switch node in n8n has "Mode" field with options "Rules" and "Expression". In JSON, it's `"mode": "rules"` or `"mode": "expression"`. Yes.

Need maybe "fallbackOutput": "2" string or number? In n8n, fallbackOutput is number? Let's use number 2. But in options, maybe value should be string? Hmm. Use "2" maybe safer? Let's use number 2.

Need maybe if "fallbackOutput" is 2, then unmatched goes to output 2 (otro). Good.

6. Slack Soporte:
```
{
  "parameters": {
    "resource": "chat",
    "operation": "postMessage",
    "channel": "#support",
    "text": "=📩 Nuevo mensaje de {{ $json.email }}:\n{{ $json.message }}"
  },
  "id": "slack-support",
  "name": "Enviar a #support",
  "type": "n8n-nodes-base.slack",
  "typeVersion": 2,
  "position": [1000, -200],
  "credentials": {
    "slackApi": {
      "name": "Slack"
    }
  }
}
```
Need maybe "channel" should be "#support" or "support"? Slack API accepts "#support" maybe. Good.

7. Slack Ventas:
```
{
  "parameters": {
    "resource": "chat",
    "operation": "postMessage",
    "channel": "#sales",
    "text": "=📩 Nuevo mensaje de {{ $json.email }}:\n{{ $json.message }}"
  },
  "id": "slack-sales",
  "name": "Enviar a #sales",
  "type": "n8n-nodes-base.slack",
  "typeVersion": 2,
  "position": [1000, 0],
  "credentials": {
    "slackApi": {
      "name": "Slack"
    }
  }
}
```

8. Slack Otro:
```
{
  "parameters": {
    "resource": "chat",
    "operation": "postMessage",
    "channel": "#general",
    "text": "=📩 Nuevo mensaje de {{ $json.email }}:\n{{ $json.message }}"
  },
  "id": "slack-general",
  "name": "Enviar a #general",
  "type": "n8n-nodes-base.slack",
  "typeVersion": 2,
  "position": [1000, 200],
  "credentials": {
    "slackApi": {
      "name": "Slack"
    }
  }
}
```

Need maybe "Slack" node typeVersion 2? Slack node has typeVersion 2? I think yes. But "resource": "chat" and "operation": "postMessage" are valid. Good.

Need maybe "connections" with node names. Need include all.

Connections:
```
"connections": {
  "Webhook": {
    "main": [
      [
        {
          "node": "Extraer email y message",
          "type": "main",
          "index": 0
        }
      ]
    ]
  },
  "Extraer email y message": {
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
          "node": "Normalizar clasificación",
          "type": "main",
          "index": 0
        }
      ]
    ]
  },
  "Normalizar clasificación": {
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
          "node": "Enviar a #support",
          "type": "main",
          "index": 0
        }
      ],
      [
        {
          "node": "Enviar a #sales",
          "type": "main",
          "index": 0
        }
      ],
      [
        {
          "node": "Enviar a #general",
          "type": "main",
          "index": 0
        }
      ]
    ]
  }
}
```
Need maybe if Switch node outputs are indexed 0,1,2. Good.

Need maybe top-level "connections" includes all nodes, but nodes with no outgoing omitted. Good.

Need maybe top-level "settings": { "executionOrder": "v1" }. In n8n, "settings" can include "executionOrder": "v1" or "v0". Let's include "v1".

Need maybe "name": "Clasificar mensaje y enviar a Slack", "active": false, "createdAt": ..., "updatedAt": ... Not necessary but okay.

Need maybe "pinData": {} no.

Need maybe "meta": { "templateCredsSetupCompleted": false }.

Need maybe "nodes" array order. Good.

Need maybe "Webhook" node "responseMode" "onReceived" returns "Workflow executed successfully" but if using "responseNode" maybe need Respond to Webhook. Not necessary.

Need maybe "Webhook" node "options": { "responseData": "allHeaders" }? No.

Need maybe "Webhook" node "path": "classify-message" and "httpMethod": "POST". Good.

Potential issue: Set node expression `$json.body.email` - In Webhook output, is body at `$json.body`? Let's verify. n8n Webhook node returns item with `body`, `headers`, `query`, `params`. Yes. If the POST body is JSON, `$json.body.email` works. If body is not JSON, maybe not. Good.

Potential issue: The OpenAI node's input is the output of Set node, so `$json.message` is top-level. Good.

Potential issue: The Code node references `$('Extraer email y message').first().json`. If node name contains spaces, expression okay. Need maybe "first()" method exists? In n8n expressions, `$('NodeName').first().json` is valid. In Code node, `$('NodeName').first().json` maybe valid too. Good.

Potential issue: If OpenAI output is `openAiResponse.choices[0].message.content` but if `choices` is array and content is "soporte", good. If content includes punctuation, classification includes. We use includes.

Potential issue: If OpenAI returns "Soporte" with uppercase, toLowerCase handles.

Potential issue: If OpenAI returns "ventas" but with extra text, includes handles.

Potential issue: If OpenAI returns "otro" but with extra text, includes handles.

Potential issue: If OpenAI returns "soporte" and "ventas" both? Unlikely. We prioritize soporte then ventas.

Potential issue: If OpenAI node output is not as expected and content empty, classification "otro". Fine.

Need maybe "OpenAI" node "messages" content expression uses `$json.message` but if message contains quotes, okay.

Need maybe "Slack" text expression uses `$json.email` and `$json.message` from Code node. Good.

Need maybe "Slack" node "channel" parameter in n8n might be "channelId" not "channel". Let's recall Slack node parameters:
- Resource: "Chat"
- Operation: "Post"
- "Channel" field: "The channel to post to" (e.g., #general)
- "Text" field.
So "channel" is correct.

Need maybe "operation" value "postMessage" or "post"? In n8n Slack node, operation is "postMessage"? Let's recall: Slack API method "chat.postMessage". In n8n, operation likely "postMessage" under resource "chat". Good.

Need maybe "resource" "chat" and "operation" "postMessage" maybe accepted. If not, "operation": "post" maybe? Let's verify from memory: In n8n Slack node, operations include "postMessage", "postEphemeral", "update", "delete", etc. Yes.

Need maybe "Slack" node typeVersion 2.2? Hmm. Slack node typeVersion 2 has "resource": "chat", "operation": "postMessage". Good.

Need maybe "OpenAI" node "typeVersion" 2. Let's consider if "n8n-nodes-base.openAi" typeVersion 2 exists. If not, import error. Let's try to recall from n8n source: The OpenAI node is in "n8n-nodes-base" and has typeVersion 1.2? Actually n8n node type versions are integers or decimals. In n8n, "OpenAI" node has "typeVersion": 1.2? Let's search memory from GitHub: `packages/nodes-base/nodes/OpenAi/OpenAi.node.ts` maybe. It defines `version: 1`? Hmm.

Let's reason: n8n introduced "OpenAI" node in 2023. It had "Chat" and "Text" resources. The node type version might be 1.2 because it was updated to support new models. In workflow JSON, typeVersion can be 1.2. If I set 2, maybe invalid. To be safe, set typeVersion to 1.2? But if user's n8n expects integer? It supports decimals. Many nodes have typeVersion 1.1, 2.1. For OpenAI, I remember seeing `"typeVersion": 2` in some n8n workflow JSON? Let's google memory: In n8n, "OpenAI" node "typeVersion": 1.2? Hmm.

Let's maybe use "n8n-nodes-base.openAi" with typeVersion 1.2? But if parameters "resource": "chat" not in version 1.2? Need know.

Let's recall n8n node docs for OpenAI:
- "OpenAI" node has "Resource" "Chat" and "Operation" "Complete" in "Advanced AI" category? Actually there is "OpenAI" node in "AI" category. It uses "Chat" resource and "Complete" operation. The node type is "n8n-nodes-base.openAi". It has version 1.2? I have seen in n8n workflows:
```
{
  "type": "n8n-nodes-base.openAi",
  "typeVersion": 1.2,
  "parameters": {
    "resource": "chat",
    "operation": "complete",
    "model": "ggpt-3.5-turbo",
    "messages": { ... }
  }
}
```
This rings a bell. Let's use typeVersion 1.2. That might be more accurate.

Need maybe "OpenAI" node "model" "gpt-4o-mini" may not be available in older version, but okay.

Need maybe "Code" node typeVersion 2? In n8n, Code node typeVersion 2 uses "jsCode" and "mode": "runOnceForAllItems"? Wait Code node has typeVersion 1 and 2. TypeVersion 2 has "mode" parameter? Let's recall: Code node v2 has "mode": "runOnceForAllItems" or "runOnceForEachItem". If not set, default? Hmm. In n8n, Code node typeVersion 2 parameters:
```
{
  "parameters": {
    "mode": "runOnceForAllItems",
    "jsCode": "..."
  }
}
```
Actually Code node v2 has "mode" in parameters. If we omit, maybe default "runOnceForEachItem"? For our code, `$input.first()` works either way? If runOnceForEachItem, `$input` is a single item? Actually `$input.first()` still works. But if multiple items, our code returns one item and may duplicate? Not an issue. But to be safe, include "mode": "runOnceForAllItems". Let's include.

Need maybe Code node "mode" values: "runOnceForAllItems" and "runOnceForEachItem". In n8n, the parameter is "mode" with default "runOnceForEachItem". If we set "runOnceForAllItems", the code runs once with all items. Our code uses `$input.first()` and returns one item. That's fine. If multiple webhooks, one item. Good.

Need maybe "Code" node "jsCode" uses `$input.first().json`; if runOnceForAllItems, `$input` is array-like with `.first()`. Good.

Need maybe "Switch" node "mode" "rules" and "dataPropertyName" "classification". If "classification" is top-level in Code output. Good.

Need maybe "Switch" node "options" "fallbackOutput": 2. If "otro" rule matches, it goes to output 2. If classification "otro", rule index 2 matches. Good.

Need maybe if "fallbackOutput" is 2, unmatched also goes to #general. Good.

Need maybe "Switch" node "rules" values with "ignoreCase": true. In n8n, rule object may use "ignoreCase" under "options" not inside rule? Hmm. Let's check. Switch node v2 rule fields:
- "value": string
- "type": "string" | "number" | "boolean" | "dateTime" | "object" | "array"
- "regex": string
- "ignoreCase": boolean
Maybe yes.

Need maybe "type" in rule should be "string" and "value" should be "soporte". Good.

Need maybe "Switch" node "mode" "rules" and "dataPropertyName" "classification" but if "mode" is "expression", no. Good.

Need maybe "Webhook" node "responseMode" "onReceived" and "options": {}.

Need maybe "Webhook" node "path" without leading slash. Good.

Need maybe "active": false.

Let's now write final JSON. Need maybe wrap in code block. The user requested "Dame el JSON completo del workflow." We can provide just JSON in code block. Need maybe no extra explanation? Maybe include brief "Aquí tienes". But final answer should be code block.

Need ensure JSON is valid. Let's construct carefully.

Potential issue: In "Extraer email y message" Set node, assignment "type" could be "string" but value expression returns string. Good.

Potential issue: In "OpenAI" node, "messages" content uses `{{ $json.message }}` but if message is not string? It is. Good.

Potential issue: In "OpenAI" node, "messages" field in n8n might be an array of message objects directly, not `{ values: [...] }`. In n8n, for fixed collection, it's often `"messages": { "values": [ ... ] }`. Good.

Potential issue: In "OpenAI" node, "role" and "content" might be under "message" object? No.

Potential issue: "OpenAI" node "operation": "complete" maybe should be "message" for chat? Let's verify. In n8n, OpenAI node "Chat" resource has operations "Complete" and "Message a Model"? Hmm. Let's recall from n8n docs: The "OpenAI" node "Chat" operation "Complete" is "Create a chat completion." It uses "Messages" field. Yes.

Potential issue: "OpenAI" node "model" default "gpt-3.5-turbo" maybe. "gpt-4o-mini" okay.

Potential issue: "Slack" node "text" expression uses `=`. In n8n, to use expression in a string parameter, prefix with `=`. We did. Need escape newline: `\n` inside JSON string. Good.

Potential issue: "Slack" node "channel" "#support" maybe if Slack node expects channel ID not name? Slack API can resolve #support if bot token has permissions. Good.

Potential issue: "Slack" node "resource": "chat" and "operation": "postMessage" maybe requires "text" and "channel". Good.

Need maybe "credentials" for Slack in each node. Good.

Need maybe "credentials" for OpenAI in node. Good.

Need maybe "webhookId" in Webhook node. Good.

Need maybe "typeVersion" for "Set" node. Let's verify Set node v2. In n8n, "Set" node was renamed "Edit Fields" in newer versions. The type "n8n-nodes-base.set" typeVersion 2 has parameters:
```
{
  "parameters": {
    "assignments": {
      "assignments": [...]
    }
  }
}
```
This is valid. Good.

Need maybe "Set" node "options": {}.

Need maybe "Code" node "mode" "runOnceForAllItems" and "jsCode". Let's include:
```
"parameters": {
  "mode": "runOnceForAllItems",
  "jsCode": "..."
}
```
Need if Code node typeVersion 2 requires "mode"? Maybe optional. Include.

Need maybe "Code" node "jsCode" string with double quotes? We'll use single quotes in code. Need escape newlines. In JSON, we can have actual newline? Better use `\n` in string. We'll write as one line with `\n`. Need ensure no unescaped double quotes inside jsCode. We'll use single quotes in JS. Good.

Let's craft jsCode string:
```
const openAiResponse = $input.first().json;
let content = openAiResponse.choices?.[0]?.message?.content || openAiResponse.data?.choices?.[0]?.message?.content || openAiResponse.content || '';
let classification = content.trim().toLowerCase();
if (classification.includes('soporte')) {
  classification = 'soporte';
} else if (classification.includes('ventas')) {
  classification = 'ventas';
} else {
  classification = 'otro';
}
const original = $('Extraer email y message').first().json;
return [{ json: { email: original.email, message: original.message, classification } }];
```
Need in JSON string, newlines as `\n`. Let's encode.

Need maybe if `$('Extraer email y message')` in Code node returns undefined? If code node input is from OpenAI, and "Extraer email y message" is previous node, yes. If n8n's Code node can access previous nodes? Yes.

Alternative to avoid referencing another node: Use "Edit Fields" after OpenAI to extract classification and merge? But no.

Maybe we can avoid Code node referencing previous node by using "Merge" node to combine OpenAI output with original from Extraer. But more complex. Code node is okay.

Need maybe "OpenAI" node output includes original input? Actually n8n nodes sometimes "pass through" input data? No, output is API response. So code reference is needed.

Need maybe "Switch" node receives Code output with email/message/classification. Good.

Need maybe "Slack" nodes receive Switch output, which passes through Code output. Good.

Need maybe "Webhook" response mode "onReceived" means it doesn't wait for workflow. Good.

Need maybe "responseMode" "onReceived" is valid for Webhook node typeVersion 2. Good.

Need maybe "path" "classify-message" and "httpMethod" "POST". Good.

Need maybe "options": {} for webhook.

Let's think if there is any issue with "OpenAI" node "messages" field. In n8n, the "messages" parameter for OpenAI node is a "fixedCollection" of type "messages" with "values" array. Each item has "role" and "content". Good.

Need maybe "content" in system message should be string with no expression. Good.

Need maybe "user" content expression "Mensaje: {{ $json.message }}" - In n8n, expressions in string parameters are evaluated with `{{ }}`. Good.

Need maybe "OpenAI" node "options" "temperature": 0. Good.

Need maybe "credentials" for OpenAI "openAiApi" with object. Good.

Need maybe "credentials" for Slack "slackApi" with object. Good.

Need maybe "name" of workflow. Good.

Let's now produce final JSON.

Before final, let's consider if "n8n-nodes-base.openAi" typeVersion 2 is actually "n8n-nodes-base.openAi" or "n8n-nodes-langchain.openAi"? Hmm. In n8n, the "OpenAI" node for chat completion might be "n8n-nodes-base.openAi" but there is also "OpenAI" node in "n8n-nodes-langchain" for "Chat Model" with type "@n8n/n8n-nodes-langchain.openAi". The latter is used in AI Agent nodes and has no regular output. So our choice is correct.

Need maybe "OpenAI" node "typeVersion": 1.2? Let's decide final. I think "n8n-nodes-base.openAi" with typeVersion 2 may be accepted? Let's search memory: In n8n, node type "n8n-nodes-base.openAi" has "typeVersion": 1.2? Actually I recall from n8n workflow JSON:
```
{
  "type": "n8n-nodes-base.openAi",
  "typeVersion": 1,
  "parameters": {
    "resource": "text",
    "operation": "complete",
    "model": "text-davinci-003",
    "prompt": "..."
  }
}
```
Then later "Chat" resource added with typeVersion 1.1? Hmm.

Let's maybe use typeVersion 1.2. But if typeVersion 1.2 doesn't exist, import error. If typeVersion 2 doesn't exist, import error. Which is more likely? Let's infer from n8n versioning: Many nodes with multiple versions use integer versions (1, 2). For OpenAI, there is no v2? Wait, n8n's "OpenAI" node may have version 1.2 because it was updated with new operations but not breaking. In n8n, typeVersion can be 1.1, 1.2, 2, 2.1. For example, "Telegram" node has typeVersion 1.1, 1.2. "OpenAI" node might have typeVersion 1.2. Let's use 1.2. But if user's n8n expects 2? Hmm.

Let's search memory from n8n nodes: "OpenAI" node "typeVersion": 2? I have seen in n8n templates:
```
"type": "n8n-nodes-base.openAi",
"typeVersion": 2,
"parameters": {
  "resource": "chat",
  "operation": "complete",
  ...
}
```
This looks familiar. Let's use 2. Because the "Chat" resource is part of the newer OpenAI node version 2. The old version 1 was "text completion". So 2 is correct.

Need maybe "OpenAI" node "operation" "complete" is okay. In n8n, "Chat" resource operation "Complete" maybe "complete" or "message". Let's verify from memory of n8n OpenAI node docs:
- Resource: Chat
- Operation: Complete
- Model: gpt-3.5-turbo
- Messages: ...
Yes.

Need maybe "Slack" node "typeVersion": 2. In n8n, Slack node has typeVersion 2? I think yes. But Slack node typeVersion 2 might have "resource" and "operation" parameters. Good.

Need maybe "Switch" node "typeVersion": 2. Good.

Need maybe "Set" node "typeVersion": 2. Good.

Need maybe "Code" node "typeVersion": 2. Good.

Need maybe "Webhook" node "typeVersion": 2. Good.

Need maybe "connections" "OpenAI" node name "Clasificar con OpenAI" with accent? No, no accent. Good.

Need maybe "Normalizar clasificación" has accent in "clasificación". In JSON, Unicode okay. Need ensure node names in connections match exactly. We'll use "Normalizar clasificación" with accent. Need in Code node reference "Extraer email y message" no accent. Good.

Need maybe "Clasificación" node name has accent. Good.

Need maybe "Enviar a #support" node names with #. In connections, use exact. Good.

Let's write final JSON with indentation. Need ensure no trailing commas. Let's produce.

One more thing: In "Extraer email y message" Set node, if Webhook body is not object? It is. Good.

Maybe we should include "options": { "ignoreConversion": false }? No.

Need maybe "Webhook" node "responseMode": "onReceived" but if user wants immediate response, okay. If they want custom response, need "Respond to Webhook" node. Not necessary.

Need maybe "OpenAI" node "messages" "values" each message object might need "id" fields? In n8n fixedCollection items often have "id" to identify. Not required? Usually each item in `values` can have `id`? Actually in n8n, fixed collection values array items don't need id? In workflow JSON, they often don't have id. Good.

Need maybe "Set" node assignments each item might need "id" but not required. We include.

Need maybe "Switch" node rules values each item maybe need "id"? Not required.

Need maybe "Slack" node "channel" "#support" but if Slack node expects channel ID, user can adjust. Good.

Let's now craft final answer```json
{
  "name": "Clasificar mensaje y enviar a Slack",
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "classify-message",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "webhook",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [0, 0],
      "webhookId": "webhook-classify-message-001"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "assign-email",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "assign-message",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "set-email-message",
      "name": "Extraer email y message",
      "type": "n8n-nodes-base.set",
      "typeVersion": 2,
      "position": [200, 0]
    },
    {
      "parameters": {
        "resource": "chat",
        "operation": "complete",
        "model": "gpt-4o-mini",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador. Clasifica el mensaje del usuario como 'soporte', 'ventas' o 'otro'. Responde solo con una de esas palabras."
            },
            {
              "role": "user",
              "content": "Mensaje: {{ $json.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0
        }
      },
      "id": "openai-classify",
      "name": "Clasificar con OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 2,
      "position": [400, 0],
      "credentials": {
        "openAiApi": {
          "name": "OpenAI"
        }
      }
    },
    {
      "parameters": {
        "mode": "runOnceForAllItems",
        "jsCode": "const openAiResponse = $input.first().json;\nlet content = openAiResponse.choices?.[0]?.message?.content || openAiResponse.data?.choices?.[0]?.message?.content || openAiResponse.content || '';\nlet classification = content.trim().toLowerCase();\nif (classification.includes('soporte')) {\n  classification = 'soporte';\n} else if (classification.includes('ventas')) {\n  classification = 'ventas';\n} else {\n  classification = 'otro';\n}\nconst original = $('Extraer email y message').first().json;\nreturn [{ json: { email: original.email, message: original.message, classification } }];"
      },
      "id": "code-normalize",
      "name": "Normalizar clasificación",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [600, 0]
    },
    {
      "parameters": {
        "mode": "rules",
        "dataPropertyName": "classification",
        "rules": {
          "values": [
            {
              "value": "soporte",
              "type": "string",
              "regex": "",
              "ignoreCase": true
            },
            {
              "value": "ventas",
              "type": "string",
              "regex": "",
              "ignoreCase": true
            },
            {
              "value": "otro",
              "type": "string",
              "regex": "",
              "ignoreCase": true
            }
          ]
        },
        "options": {
          "fallbackOutput": 2
        }
      },
      "id": "switch-classification",
      "name": "Clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 2,
      "position": [800, 0]
    },
    {
      "parameters": {
        "resource": "chat",
        "operation": "postMessage",
        "channel": "#support",
        "text": "=📩 Nuevo mensaje de {{ $json.email }}:\n{{ $json.message }}"
      },
      "id": "slack-support",
      "name": "Enviar a #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1000, -200],
      "credentials": {
        "slackApi": {
          "name": "Slack"
        }
      }
    },
    {
      "parameters": {
        "resource": "chat",
        "operation": "postMessage",
        "channel": "#sales",
        "text": "=📩 Nuevo mensaje de {{ $json.email }}:\n{{ $json.message }}"
      },
      "id": "slack-sales",
      "name": "Enviar a #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1000, 0],
      "credentials": {
        "slackApi": {
          "name": "Slack"
        }
      }
    },
    {
      "parameters": {
        "resource": "chat",
        "operation": "postMessage",
        "channel": "#general",
        "text": "=📩 Nuevo mensaje de {{ $json.email }}:\n{{ $json.message }}"
      },
      "id": "slack-general",
      "name": "Enviar a #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1000, 200],
      "credentials": {
        "slackApi": {
          "name": "Slack"
        }
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extraer email y message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer email y message": {
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
            "node": "Normalizar clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Normalizar clasificación": {
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
            "node": "Enviar a #support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Enviar a #sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Enviar a #general",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```