# Nex-N2-Mini — code_generation/n8n_workflow_json

- model_id: `nex-agi/nex-n2-mini`
- success: True  | final: 6.82 | quality: 6.8
- latency_total: 39.151s | tokens_per_second: 209.2
- input_tokens: 124 | output_tokens: 8192
- judge_score: 3.0 | justificación: La respuesta proporciona una estructura básica de un workflow de N8N en JSON, pero carece de detalles específicos y precisos, como los parámetros exactos para el nodo de OpenAI y la configuración de Slack, lo que limita su utilidad práctica.

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


We need answer in Spanish likely. User asks generate N8N workflow JSON complete. Need provide JSON. Need ensure valid workflow JSON maybe n8n workflow object. Need include webhook POST, extract email/message from body, OpenAI node classify as soporte/ventas/otro, route Slack channels. Need likely include credentials placeholders. Need complete workflow. Need know n8n JSON structure. We can craft workflow JSON. Need maybe include nodes with typeVersion. Need ensure valid enough.

Need decide exact format. n8n workflows export JSON maybe top-level {"nodes":[...],"connections":...}. Need include webhook, function item extraction, openai chat model, switch routing, slack. Need maybe include webhook response. We can include "function" node to parse email and message from body. For webhook POST body, n8n webhook receives body in $json. Function code:
const email = $json.email ?? '';
const message = $json.message ?? '';
return [{json:{email,message, original: $json}}];
OpenAI node details: type "n8n-nodes-base.openAiChatModel"? Need exact node type and parameters vary by version. Need know N8N OpenAI node types. In N8N, "OpenAI" node maybe type "openAi" for old? Let's recall.

N8N node types:
- OpenAI Chat Model node type: "openAiChatModel"
- OpenAI Embeddings node type "openAiEmbeddings"
- OpenAI Image Generation "openAiImageGeneration"
- OpenAI Text Generation? "openAiTextGeneration"
Node name "OpenAI" maybe type "openAiChatModel".
Parameters:
{
"model": {
"__rl": true,
"mode": "list",
"value": "gpt-4o-mini"
},
"messages": {
"messages": [
{
"content": "Classifica el siguiente mensaje... {{ $json.message }}",
"role": "system"
},
{
"content": "{{ $json.message }}",
"role": "user"
}
],
"__rl": true,
"mode": "add",
"addTo: maybe?
}
}
But exact parameters for OpenAI Chat Model node may be tricky. Could avoid relying on exact param by using HTTP Request node to OpenAI API instead? User specifically "Use un nodo de IA (OpenAI)". HTTP Request to OpenAI might count? Better use OpenAI node. But exact schema may be not critical? They ask JSON complete. Need produce plausible.

Need know n8n Workflow JSON version maybe "nodes" with "parameters". If exact not needed maybe acceptable. But should be as close.

Need include Slack node parameters:
{
"channel": "#support",
"text": "Nuevo mensaje de soporte\nEmail: {{ $json.email }}\nMensaje: {{ $json.message }}"
}
OpenAI node output: maybe "message": { "content": "..."} or "response": {"choices": [{"message": {"content": "..."}}]}.
Need route classification:
Switch node mode: "item" or "item". Conditions:
if: "={{ $json.classification === 'soporte' }}"
Then Slack.

Need "No Error" maybe.

Need include webhook response:
Webhook node parameters:
{
"httpMethod": "POST",
"responseMode": "responseNode",
"options": {}
}
Path maybe "webhook-classificar-mensajes".

Need maybe include response code, responseBody? N8N webhook response can return JSON automatically if later response node? Need include a Response node to send result.

Need include "webhook" node credentials: webhook credentials? Node type "webhook" with credentials: { webhook: ["webhook"] }.

Need include Function node.

Need include OpenAI node credentials: { openAi: ["openAi"] }.

Need include Slack credentials.

Need maybe include "executeHook" not in export? Not needed.

Need maybe include "polling" not.

Need maybe include "operation": "chat" etc.

Need consider "n8n-nodes-base.openAiChatModel" parameters actual. Let's recall from n8n docs.

OpenAI Chat Model node:
Parameters:
- Model: Select model
- Messages: Add messages (object array)
- Temperature: number
- Max Tokens: number
- Stop Sequences: string
- User: string
- Stream: boolean
- Options: object
- Additional Fields: object
Maybe in JSON:
"model": {
"__rl": true,
"mode": "list",
"value": "gpt-4o-mini"
},
"messages": {
"messages": [
{
"content": "Eres un asistente...",
"role": "system"
},
{
"content": "={{ $json.message }}",
"role": "user"
}
],
"__rl": true,
"mode": "add"
},
"temperature": 0,
"options": {}
Maybe "messages.addTo: ???".

Older OpenAI node type "openAi" parameters:
{
"model": "gpt-3.5-turbo",
"prompt": "={{ $json.message }}",
"temperature": 0
}
Actually N8N OpenAI node (LLM) type "openAi" has parameters:
"model": { "__rl": true, "value": "gpt-3.5-turbo", "mode": "list" },
"prompt": "={{ $json.message }}",
"temperature": 0,
"options": {}
Output maybe "text" property.
But user says nodo de IA (OpenAI) not necessarily Chat Model. Could use "openAi" node with prompt. Simpler and likely valid. Node name "OpenAI". Type "openAi". It can classify with prompt. But Chat Model is more modern.

Need decide. If using "openAi" node, classification output likely $json.text. Need include a Function node after to normalize classification into $json.classification. But user specifically "Use un nodo de IA (OpenAI) para clasificar". It can output text. Then function extracts classification. Good.

But "OpenAI" node maybe "n8n-nodes-base.openAi" (older). Parameters:
"model": { "__rl": true, "mode": "list", "value": "gpt-4o-mini" },
"prompt": "={{ $json.message }}",
"temperature": 0,
"options": {}
Need maybe "systemMessage":? Hmm.

Let's search memory: N8N nodes JSON examples:
For OpenAI node:
{
"id": "openAi1",
"name": "OpenAI",
"type": "openAi",
"typeVersion": 1,
"position": [760, 240],
"parameters": {
"model": "gpt-3.5-turbo",
"prompt": "={{ $json.input }}",
"temperature": 0.5,
"options": {}
}
}
Maybe older.

OpenAI Chat Model node examples:
{
"name": "OpenAI",
"type": "openAiChatModel",
"typeVersion": 1,
"parameters": {
"model": { "__rl": true, "value": "gpt-4o-mini", "mode": "list" },
"messages": {
"messages": [
{ "content": "={{ $json.prompt }}", "role": "user" }
],
"__rl": true,
"mode": "add"
},
"options": {}
}
}
Output maybe $json.message.content.

Need produce valid JSON with no comments. Could include note after JSON about replacing credentials. Need not reveal system.

Need maybe include "credentials" field.

Need think about route Slack different channels. Need have three Slack nodes each with channel. Connections from Switch branches to each Slack. Need include all nodes and connections.

Need maybe include "Switch" node type "n8n-nodes-base.switch" or "switch". N8N node type is "switch". Parameters:
{
"mode": "item",
"options": {
"caseSensitive": true,
"additionalFields": {}
}
}
Conditions:
[
{
"name": "Soporte",
"conditions": {
"comparisons": [
{
"value1": "={{ $json.classification }}",
"type": "string",
"operation": "equals",
"value2": "soporte"
}
]
},
"topNode": "slackSupport1"
}
]
But exact Switch node parameters maybe:
{
"mode": "item",
"options": {
"caseSensitive": true,
"additionalFields": {}
},
"conditions": {
"comparisons": [
{
"operation": "equals",
"leftValue": "={{ $json.classification }}",
"rightValue": "soporte",
"name": "Soporte"
}
]
},
"topNodeIds": [
"slackSupport"
]
}
Hmm.

Switch node in n8n JSON examples. Let's recall.

N8N Switch node parameters:
{
"mode": "item",
"options": {
"caseSensitive": true,
"additionalFields": {}
},
"conditions": {
"comparisons": [
{
"name": "equals",
"operation": "equals",
"leftValue": "={{ $json.number }}",
"rightValue": 1
}
]
},
"topNodeIds": [
"0d9e..."
]
}
Maybe. It has "topNodeIds" array. In UI, for each case, topNodeIds correspond to index. I think JSON:
"topNodeIds": ["node1", "node2", "node3"].

Could use IF nodes instead of Switch? User says "Según clasificación". Could use three IF nodes in parallel to route. But to send only to one, need IF nodes conditions and no fallthrough? In n8n, IF nodes have "options": { "elseBranch": false }? Better use Switch.

Could use Function node to set "channel" and one Slack node with dynamic channel. But user asked "según clasificación, envie el email a un canal de Slack diferente: soporte -> #support..." It doesn't strictly require separate Slack nodes; can set channel dynamic. But "canal diferente" and "según clasificación" maybe dynamic channel is simpler. However they asked workflow; route to different Slack channels. Could use Function to set channel, Slack node with dynamic channel. But maybe more faithful to have 3 Slack nodes.

Need maybe include "response" node to return classification. Could include final response node.

Need maybe include "Error Trigger"? no.

Need maybe include "webhook" credentials. In n8n, each node has "credentials" with credential type. Need include:
"credentials": { "webhook": ["webhook"] }.
OpenAI credentials "openAi".
Slack credentials "slackOAuth2Api".
Maybe "slackApi".

Need maybe include "webhook" node path "clasificar-mensajes".

Need maybe include "executionTimeout"? no.

Potential issue: Function node output object with "classification" not "classificacion". User uses "clasificacion". Need choose classification. In Spanish, maybe "classificacion" no accent. N8N expressions no accents? Better use "classification". But user asks "clasificacion". We can use "classification" and maybe "clasificacion" in Slack. Let's use "classification" in internal. But to match user, maybe "clasificacion" no accent. N8N expression $json.clasificacion. Good.

Need extract email and message from body. Function node code:
const body = $json;
return [{
json: {
email: body.email ?? '',
message: body.message ?? '',
classification: '',
channel: ''
}
}];
Need maybe if body is array? If POST body has email/message fields. If body is raw JSON with top-level. Good.

OpenAI prompt:
"Clasifica el siguiente mensaje de cliente como una única etiqueta entre soporte, ventas u otro. Responde SOLO con la etiqueta, sin explicación. Mensaje: {{ $json.message }}"
Need model maybe "gpt-4o-mini".

OpenAI node output if using "openAiChatModel" might output $json.message.content. Need function node after to extract classification. But if using "openAi" node output $json.text. Need choose one.

Let's inspect n8n node details memory.

From n8n "OpenAI Chat Model" node (type openAiChatModel) parameters:
```
{
  "model": {
    "__rl": true,
    "mode": "list",
    "value": "gpt-4o-mini"
  },
  "messages": {
    "messages": [
      {
        "content": "={{ $json.message }}",
        "role": "user"
      }
    ],
    "__rl": true,
    "mode": "add"
  },
  "options": {}
}
```
Maybe "messages.addTo: "???"
Node output:
```
{
  "message": {
    "content": "...",
    "role": "assistant"
  },
  "usage": {...},
  "response": {...}
}
```
So function:
```
const text = $json.message?.content ?? $json.response?.choices?.[0]?.message?.content ?? $json.text ?? '';
return [{json:{...$json, classification: text.trim().toLowerCase()}}];
```
If using "openAiChatModel", good.

OpenAI credentials field type "openAi". In n8n credentials maybe "openAiApi".

Need maybe include "OpenAI" node "typeVersion": 3? Current? Could use 1 or 2. If not exact, maybe okay.

Need "function" node type "n8n-nodes-base.function" or "function". In n8n JSON, type maybe "function". There is also "Code" node type "n8n-nodes-base.code" in newer? In N8N, Function node type is "function"; Code node type is "code". Use "function".

Need "response" node type "response" with parameters:
{
"responseCode": 200,
"headers": [],
"options": {},
"responseBody": "={{ JSON.stringify($json) }}"
}
Actually N8N Response node parameters:
```
{
  "responseCode": 200,
  "headers": [],
  "options": {},
  "responseBody": "={{ $json }}"
}
```
I recall response node has "responseBody": "={{ $json }}" maybe. It returns JSON if object. Could set "responseBody": "={{ JSON.stringify($json) }}". N8N response node may accept object/string. Good.

Need maybe include "responseMode": "responseNode" so response node sends.

Need maybe include "webhook" node "responseBody":? no.

Potential issue: N8N workflow export includes "meta": { "instanceId": "" } optional. Include.

Need maybe include "active": true.

Need maybe include "nodes" with id unique. Need include "connections" object.

Need maybe include "executionOrder": "v1".

Need maybe include "pinData": [] optional.

Need maybe include "version": 1? Export has "version": 1.

Need maybe include "createdAt", "updatedAt"? Not necessary.

Need maybe include "tags": [].

Need maybe include "settings": { "executionTimeout": 0 } maybe.

Need maybe include "nodes": all.

Need maybe include "connections" with edges. Need map node names to ids.

Let's design workflow.

Nodes:

1. Webhook:
```
{
 "id": "webhook1",
 "name": "Webhook POST",
 "type": "webhook",
 "typeVersion": 2,
 "position": [160, 220],
 "parameters": {
   "httpMethod": "POST",
   "path": "clasificar-mensajes",
   "responseMode": "responseNode",
   "options": {}
 },
 "credentials": { "webhook": ["webhook"] }
}
```
Need maybe "webhookId" no.

2. Extract email/message:
```
{
 "id": "extract1",
 "name": "Extraer email y message",
 "type": "function",
 "typeVersion": 1,
 "position": [360, 220],
 "parameters": {
   "code": "const body = $json ?? {};\n\nreturn [{\n  json: {\n    email: body.email ?? '',\n    message: body.message ?? '',\n    classification: '',\n    channel: '',\n    rawBody: body\n  }\n}];"
 }
}
```
Need maybe if body is array? no.

3. OpenAI:
```
{
 "id": "openAi1",
 "name": "OpenAI - Clasificar",
 "type": "openAiChatModel",
 "typeVersion": 1,
 "position": [620, 220],
 "parameters": {
   "model": { "__rl": true, "mode": "list", "value": "gpt-4o-mini" },
   "messages": {
     "messages": [
       {
         "content": "Clasifica el siguiente mensaje de cliente como una única etiqueta: soporte, ventas u otro. Responde SOLO con la etiqueta, sin explicación.\n\nMensaje:\n{{ $json.message }}",
         "role": "system"
       },
       {
         "content": "={{ $json.message }}",
         "role": "user"
       }
     ],
     "__rl": true,
     "mode": "add"
   },
   "temperature": 0,
   "options": {}
 },
 "credentials": { "openAi": ["openAi"] }
}
```
Need maybe "systemMessage" separate? no.

4. Normalize classification:
```
{
 "id": "normalize1",
 "name": "Normalizar clasificación",
 "type": "function",
 "typeVersion": 1,
 "position": [860, 220],
 "parameters": {
  "code": "const text = $json.message?.content ?? $json.response?.choices?.[0]?.message?.content ?? $json.text ?? '';\nconst classification = text.trim().toLowerCase().replace(/[^a-záéíóúüñ0-9_-]/gi, '');\n\nreturn [{\n  json: {\n    ...$json,\n    classification,\n    channel: classification === 'soporte' ? '#support' : classification === 'ventas' ? '#sales' : '#general'\n  }\n}];"
 }
}
```
Need maybe if OpenAI returns "otro", classification okay. If "otro" maybe.

5. Switch:
```
{
 "id": "switch1",
 "name": "Ruta por clasificación",
 "type": "switch",
 "typeVersion": 1,
 "position": [1100, 220],
 "parameters": {
   "mode": "item",
   "options": {
     "caseSensitive": true,
     "additionalFields": {}
   },
   "conditions": {
     "comparisons": [
       {
         "name": "Soporte",
         "operation": "equals",
         "leftValue": "={{ $json.classification }}",
         "rightValue": "soporte"
       },
       {
         "name": "Ventas",
         "operation": "equals",
         "leftValue": "={{ $json.classification }}",
         "rightValue": "ventas"
       },
       {
         "name": "Otro",
         "operation": "equals",
         "leftValue": "={{ $json.classification }}",
         "rightValue": "otro"
       }
     ]
   },
   "topNodeIds": ["slackSupport1", "slackSales1", "slackGeneral1"]
 }
}
```
Need "caseSensitive" maybe under "options": { "caseSensitive": true }. Good.

6. Slack Support:
```
{
 "id": "slackSupport1",
 "name": "Slack - Soporte",
 "type": "slack",
 "typeVersion": 1,
 "position": [1360, 120],
 "parameters": {
   "channel": "#support",
   "text": "={{ 'Nuevo mensaje clasificado como soporte\\nEmail: ' + $json.email + '\\nMensaje: ' + $json.message }}",
   "options": {}
 },
 "credentials": { "slackOAuth2Api": ["slackOAuth2Api"] }
}
```
Need Slack node type maybe "slack". Parameters actual? In N8N Slack node, type "slack", parameters:
```
{
 "channel": "#my-channel",
 "text": "={{ $json.message }}",
 "options": {}
}
```
Maybe "channelId" and "text". Good.

7. Slack Sales:
position [1360, 260].
8. Slack General:
position [1360, 400].

9. Response:
Could be after switch? If switch branches end in Slack nodes, to send response after all branches, connect Slack nodes to response node. But if Slack nodes are branch leaves, connect them to response node. However if response node after switch, it will receive from whichever branch. Need connections:
- webhook -> extract
- extract -> openAi
- openAi -> normalize
- normalize -> switch
- switch -> slackSupport, slackSales, slackGeneral
- slackSupport -> response
- slackSales -> response
- slackGeneral -> response
This sends Slack then response.

Need maybe include "response" node parameters:
```
{
 "id": "response1",
 "name": "Respuesta",
 "type": "response",
 "typeVersion": 1,
 "position": [1620, 260],
 "parameters": {
   "responseCode": 200,
   "headers": [],
   "options": {},
   "responseBody": "={{ JSON.stringify($json) }}"
 },
 "credentials": {}
}
```
Need maybe "responseBody" should be object not string? If string JSON string, maybe response body is string. Could use:
```
"responseBody": "={{ $json }}"
```
N8N response node examples:
```
{
  "responseBody": "={{ $json }}"
}
```
It returns JSON. But if expression returns object, okay. If using JSON.stringify, maybe returns string. User doesn't require. Fine.

Need include "No Error Trigger"? no.

Need maybe include "executionOrder" "v1".

Need maybe include "connections":
```
"connections": {
 "webhook1": { "main": [[{ "node": "extract1", "index": 0 }]] },
 ...
}
```
In n8n JSON, connections:
```
"connections": {
 "Webhook": {
   "main": [
     [
       {
         "node": "Function",
         "type": "main",
         "index": 0
       }
     ]
   ]
 }
}
```
If using ids, maybe "node": "webhook1" enough? Actually N8N workflow JSON connections use node names or ids? It can use ids? In export, node IDs are used? I think connections use node names? Let's recall. n8n workflow JSON:
```
"connections": {
  "Node 1": {
    "main": [
      [
        {
          "node": "Node 2",
          "type": "main",
          "index": 0
        }
      ]
    ]
  }
}
```
Sometimes uses node IDs? In recent versions, "node": "Node 1" maybe names. Let's include names or ids? If names with spaces? Use ids safer? N8N uses node IDs in connections? Hmm.

I used n8n exports before. Connections:
```
"connections": {
  "Node1": {
    "main": [
      [
        {
          "node": "Node2",
          "type": "main",
          "index": 0
        }
      ]
    ]
  }
}
```
Node IDs are strings, names separate. I think yes. Use ids.

Need maybe include "type": "main" and "index": 0. Good.

Need maybe include "slackSupport1": {"main": [[{"node":"response1","index":0}]]}, etc.

Need maybe include "switch1": {"main": [[{"node":"slackSupport1","index":0}],[{"node":"slackSales1","index":0}],[{"node":"slackGeneral1","index":0}]]}. Good.

Need maybe include "active": true, "tags": [], "version": 1.

Potential issue: OpenAI Chat Model node parameter "messages.addTo" maybe missing. If n8n validates, might fail. Need maybe find exact parameter schema. Let's recall from n8n docs for OpenAI Chat Model:
Parameters UI:
- Model (Select): e.g. "gpt-4o-mini"
- Messages (Object Array): Add messages with name, content, role.
- Temperature (Number)
- Max Tokens (Number)
- Stop Sequences (String)
- User (String)
- Stream (Checkbox)
- Options (Object)
Maybe JSON for messages:
```
"messages": {
  "messages": [
    {
      "content": "={{ $json.message }}",
      "role": "user"
    }
  ],
  "__rl": false,
  "mode": "add"
}
```
I think "mode": "add" is valid for object arrays. "addTo" not needed.
Need maybe include "systemMessage": "={{ $json.systemMessage }}"? Not sure.

Maybe "OpenAI" node (non-chat) simpler. But user says "nodo de IA (OpenAI)" not "Chat". Maybe use "openAiChatModel" and include function after. It should be okay.

Need maybe include "OpenAI" credentials type "openAi". In n8n credentials type maybe "openAiApi"? Let's recall. N8N credentials:
- OpenAI API credential: name "OpenAI API", type "openAi".
I think yes.
Slack credentials type maybe "slackOAuth2Api" or "slackApi". Use "slackOAuth2Api".

Need maybe include "description"? optional.

Need maybe include "notes"? no.

Need maybe include "function" code with semicolons. Need valid JSON.

Need maybe include "options": { "classifications": ... }? no.

Need maybe include "Slack node" "channel": "#support" or channel ID? Slack node can send to channel name. Good.

Need maybe include "text": "={{ '...' }}" string. In n8n, Slack node parameter "text" maybe "={{ $json.message }}" not wrapped? Good.

Need maybe include "attachments": []? no.

Need maybe include "channel": "#support" for all.

Potential issue: if classification is "otro", Slack General. If classification empty due to error, general. Good.

Need maybe include "classification" from OpenAI; if OpenAI returns "soporte", okay. If returns "support" maybe not, but prompt Spanish. Could normalize synonyms:
```
const normalized = text.trim().toLowerCase();
const mapping = {
 'soporte': 'soporte',
 'support': 'soporte',
 'ventas': 'ventas',
 'sale': 'ventas',
 'otro': 'otro',
 'other': 'otro'
};
const classification = mapping[normalized] || 'otro';
```
But user wants only those. Maybe include to be robust. But if OpenAI returns "otro", okay. Could map.
Need not overcomplicate.

Need maybe include "OpenAI node" classification output if using "openAiChatModel": if role system and user. Good.

Need maybe include "metadata" with version.

Need maybe include "workflow" not "nodes"? User asks "workflow de N8N en JSON". Provide as top-level "nodes", "connections". Some imports expect exactly. We can wrap in ```json. Need maybe include "Aquí tienes..." and note credentials.

Need ensure JSON no comments. Final answer can include JSON only or with note. User asked "Dame el JSON completo". We can provide only JSON. Maybe include small note after about credentials. But "JSON completo" maybe no extra. Could include code block.

Need maybe consider if "OpenAI" node "messages" object array requires "messages.addTo": "content"? Let's search memory more.

N8N workflow JSON examples from n8n docs:
OpenAI Chat Model node:
```
{
  "id": "openAiChatModel1",
  "name": "OpenAI Chat Model",
  "type": "openAiChatModel",
  "typeVersion": 1,
  "position": [
    820,
    120
  ],
  "parameters": {
    "model": {
      "__rl": true,
      "mode": "list",
      "value": "gpt-4o"
    },
    "messages": {
      "messages": [
        {
          "content": "={{ $json.prompt }}",
          "role": "user"
        }
      ],
      "__rl": true,
      "mode": "add"
    },
    "options": {}
  },
  "credentials": {
    "openAi": [
      "openAi"
    ]
  }
}
```
I think.

Switch node exact maybe:
```
{
  "parameters": {
    "mode": "item",
    "options": {
      "caseSensitive": true
    },
    "conditions": {
      "comparisons": [
        {
          "name": "equals",
          "operation": "equals",
          "leftValue": "={{ $json.classification }}",
          "rightValue": "soporte"
        }
      ]
    },
    "topNodeIds": [
      "slackSupport1"
    ]
  }
}
```
Need if 3 comparisons, topNodeIds length 3. Good.

Need maybe include "function" node typeVersion 2? N8N Function node current typeVersion 2? Could use 1. No issue.

Need maybe include "response" node typeVersion 1. Good.

Potential issue: Slack node type "slack" parameters for channel maybe "channelId": "#support"? Let's recall. Slack node "Post a Message" parameters:
```
{
 "channel": "#my-channel",
 "text": "={{ $json.message }}",
 "options": {}
}
```
Good.

Need maybe include "credentials": { "slackOAuth2Api": ["slackOAuth2Api"] }.

Need maybe include "options": { "appendNewline": true }? no.

Need maybe include "operation": "send" or "chat"? Slack node may have operation parameter. In N8N Slack node, type "slack", parameters include "operation": "chat.postMessage" maybe. If omitted, default "chat.postMessage"? Maybe. To be safe, include:
```
"operation": "chat.postMessage"
```
But actual Slack node parameters maybe:
```
"operation": "chat.postMessage",
"channel": "#general",
"text": "={{ $json.message }}"
```
Could include. If operation unknown, might still work. Let's include "operation": "chat.postMessage".

Need maybe include "channel": "#support". Good.

Need maybe include "options": { "asUser": true }? no.

Need maybe include "responseBody": "={{ $json }}" or "={{ JSON.stringify($json) }}". In N8N response node, if responseBody is expression returning object, it may JSON stringify. But if string, maybe send string. Let's set:
```
"responseBody": "={{ $json }}"
```
This returns JSON object. If N8N expects string, expression object okay? In response node, parameter "responseBody" default "={{ $json }}" (I recall). Good.

Need maybe include "responseCode": 200.

Need maybe include "headers": [].

Need maybe include "options": {}.

Need maybe include "meta": {"instanceId": ""}.

Need maybe include "settings": {"executionTimeout": 0}.

Need maybe include "created_at"? not necessary.

Need maybe include "updatedAt"? no.

Potential issue: If using IDs in "credentials" arrays, okay.

Need maybe include "connections" for branch leaves to response. But in n8n, connecting Slack nodes to response means the response node receives only after Slack call. Good.

Need maybe include "Slack General" branch after switch if classification "otro". Good.

Need maybe include "classification" as property in Slack text. Good.

Need maybe include "email" extraction from body. Good.

Need maybe include "body" from webhook. Good.

Need maybe include "message" extraction. Good.

Need maybe include "OpenAI" classification. Good.

Need maybe include "N8N workflow in JSON". Good.

Let's think of exact n8n "Function" node code. In n8n Function node, `$json` refers to current item. It can use spread operator? n8n function node uses Node-RED function environment with V8, supports JS. Spread operator supported. Could avoid spread for compatibility:
```
const body = $json ?? {};
const openAiText = $json.message?.content ?? ...
const classification = ...
return [{
  json: {
    email: body.email ?? '',
    message: body.message ?? '',
    classification,
    channel,
    rawBody: body
  }
}];
```
But this loses original $json fields like body. Fine.
For OpenAI output, if we use Function before OpenAI to set classification. Then OpenAI node outputs to Function after. Function after:
```
const text = $json.message?.content ?? $json.response?.choices?.[0]?.message?.content ?? $json.text ?? '';
const normalized = text.trim().toLowerCase();
const classificationMap = {
  soporte: 'soporte',
  support: 'soporte',
  ventas: 'ventas',
  sale: 'ventas',
  ventas_o_compras: 'ventas',
  otro: 'otro',
  other: 'otro'
};
const classification = classificationMap[normalized] || 'otro';
return [{ json: { email: $json.email ?? '', message: $json.message ?? '', classification, channel: ... } }];
```
This is simpler. Need not include rawBody.

But if using OpenAI Chat Model, function before OpenAI doesn't include "messages" from previous? Fine.

Need maybe include "OpenAI node" prompt includes classification rules. Good.

Need maybe include "classify as soporte, ventas u otro". Good.

Need maybe include "Responde SOLO con la etiqueta". Good.

Need maybe include "classification" no accents.

Need maybe include "responseBody": "={{ {status:'ok', classification:$json.classification, channel:$json.channel, email:$json.email} }}"? If responseBody expression returns object, okay. Could return only relevant fields. But maybe "={{ $json }}" returns raw OpenAI metadata too, including API response. Better to return clean object. In response node, expression can return object. Use:
```
"responseBody": "={{ { status: 'ok', classification: $json.classification, channel: $json.channel, email: $json.email } }}"
```
This is valid in N8N expression? Yes. But if response node expects string, object okay. Could be "={{ JSON.stringify({ status: 'ok', ...}) }}" returns string. Maybe use object.
Need maybe include "message": $json.message? Could be long. Fine.

Need maybe include "headers": [].

Need maybe include "authentication": "predefinedCredentialType". no.

Need maybe include "webhook" path. Good.

Potential issue: OpenAI Chat Model node output might not have `$json.message?.content` because messages are in `$json.message` maybe. Good.
Alternative