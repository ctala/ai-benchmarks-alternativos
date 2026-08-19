# DeepSeek V4 Pro (0813) — code_generation/n8n_workflow_json

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 5.7 | quality: 6.24
- latency_total: 117.434s | tokens_per_second: 69.8
- input_tokens: 205 | output_tokens: 8192
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

We need answer in Spanish. Need generate N8N workflow JSON. Need be careful. User asks: "Genera un workflow de N8N en JSON que:
1. Se active con un webhook POST
2. Extraiga el campo "email" y "message" del body
3. Use un nodo de IA (OpenAI) para clasificar el mensaje como "soporte", "ventas" o "otro"
4. Segun la clasificacion, envie el email a un canal de Slack diferente:
   - soporte -> #support
   - ventas -> #sales
   - otro -> #general

Dame el JSON completo del workflow."

We need produce complete n8n workflow JSON. Need likely use nodes: Webhook, Set/Function? OpenAI node, Switch, Slack nodes. Need know n8n JSON structure. Need maybe use n8n node types. OpenAI node type? "n8n-nodes-base.openAi" or "@n8n/n8n-nodes-langchain.openAi"? We need maybe use older/classic OpenAI node. Slack node type "n8n-nodes-base.slack". Need use resource "message", operation "post". For older Salesforce? Let's craft plausible workflow JSON.

Need determine n8n version? Could use n8n workflow JSON schema. Need include nodes, connections. We'll produce one valid workflow.

We need include Webhook node. For POST webhook, type "n8n-nodes-base.webhook", parameters: httpMethod: "POST", path maybe "webhook/...", responseMode "onReceived", options? We'll set.

Need extract email/message. Could use FunctionItem/Set node. Since body fields accessible via {{$json.body.email}} maybe. We can use Set node to map email and message from webhook body. Or use Function node. For simplicity use Set node? Type "n8n-nodes-base.set". parameters assignments: [{name: "email", value: "={{ $json.body.email }}"}, {name: "message", value: "={{ $json.body.message }}"}]. But in Webhook output, body fields might be in $json.body or at top level depending options. N8N webhook with body raw? The default webhook has body data under body property if using JSON. In newer versions, if "Raw Body" disabled, the body is parsed and maybe under body and fields as top-level? Let's think.

n8n webhook node default: request data is in body? In expressions, for a webhook with JSON payload, fields are available at top level? I recall: Webhook node outputs body as JSON. Example: webhook returns [{"body": {"name": "John"}}]? Actually expression {{$json.name}} might not work unless "Include Response Body" etc. In n8n, webhook node: for a POST request with JSON, the output data has a "body" property containing parsed data. In old versions, if "Raw Body" off, body is object and fields maybe at top-level? Need decide.

Could use Function item to extract regardless. E.g.:
```
return {
  json: {
    email: item.json.body?.email || item.json.email,
    message: item.json.body?.message || item.json.message
  }
}
```
This is robust. We'll use FunctionItem node type "n8n-nodes-base.functionItem" with code. But user might prefer no code? They ask extract fields. Could also use "Set" with fallback expression. But function is okay.

Next, OpenAI classification. Need use AI node. In n8n, there are multiple OpenAI node types:
- "n8n-nodes-base.openAi" (classic) for generation/completion.
- LangChain version "@n8n/n8n-nodes-langchain.openAi" maybe for LLM chain.
But to classify and output exactly classification, could use OpenAI node with action "complete" or "chat". We can craft the node with parameters. But need ensure correct node type. The user says "Use un nodo de IA (OpenAI)" likely classic OpenAI node.

Classic OpenAI node:
Type: "n8n-nodes-base.openAi"
Parameters: resource: "textComplete" maybe? version? The classic OpenAI node (n8n-nodes-base.openAi) has resource "textComplete" and operation "complete" or "chat.complete"? Let's recall n8n OpenAI node operations: The "OpenAI" node has Resource: "Text" (text), Operation: "Complete" or "Message a Model"? Actually older versions: resource "textComplete" operation "complete", uses model, prompt, etc. New versions? The node type maybe "n8n-nodes-base.openAi" with parameters:
```
"parameters": {
 "resource": "textComplete",
 "engine": "text-davinci-003",
 "prompt": "=...",
 "temperature": 0
}
```
Or chat:
```
"resource": "chatComplete",
 "model": "gpt-3.5-turbo",
 "messages": [...]
```
Need classification result. Could use a prompt like:
"Classify the following message into one of these categories: soporte, ventas, otro. Return only the category.\n\nMessage: {{ $json.message }}"
Set `temperature`: 0. For completions endpoint might return at `choices[0].text`. We need later parse it.

But user asked nodo de IA OpenAI, might expect "OpenAI" node. We can use classic OpenAI node with chat completion and a system message. Need output field `choices[0].message.content`.

Let's search memory: In n8n, OpenAI node type "n8n-nodes-base.openAi" parameters:
```
{
  "resource": "chatComplete",
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": "=Classify..."
    }
  ],
  "options": {}
}
```
I think resource can be "chatComplete" or "textComplete"? Actually in classic OpenAI node, resource values are "textComplete" and "image"?? Hmm.

There is also "OpenAI" node in n8n with "Resource" = "Text" and "Operation" = "Complete" (node version 2?). The JSON:
```
"parameters": {
  "resource": "textComplete",
  "model": "gpt-3.5-turbo-instruct",
  "prompt": "=..."
}
```
In older nodes, this was the way. Need decide. Since n8n nodes have evolved, but typical n8n workflow JSON used in templates:
```
{
  "parameters": {
    "resource": "textComplete",
    "engine": "text-davinci-003",
    "prompt": "..."
  },
  "name": "OpenAI",
  "type": "n8n-nodes-base.openAi",
  ...
}
```
Later they changed to model. But either can be plausible. Maybe produce a workflow using LangChain? The user says nodo de IA (OpenAI). In newer n8n, "OpenAI" node under "AI" is part of LangChain nodes. There is "OpenAI Chat Model" node type `@n8n/n8n-nodes-langchain.openAi`? Actually for AI workflows, you'd use an LLM Chain node plus OpenAI Chat Model. But a single node to classify might require "Basic LLM Chain" node type `@n8n/n8n-nodes-langchain.chainLlm` connected to an "OpenAI Chat Model" node as LLM. But much more complex. User asked nodo de IA OpenAI; likely they want one node. But to deliver valid JSON, maybe use classic OpenAI node directly. That's simpler and acceptable.

Need then Switch node to route based on classification. Need parse classification result from OpenAI. Could use Switch node with rules on an extracted value. We can use a FunctionItem after OpenAI to clean classification output (trim lower case). Then Switch node with conditions.

After OpenAI node, output JSON might have `result`? Need know classic node output. For completion, the result is in `choices[0].text` maybe. We can use Function item to read fields. Let's determine.

In n8n classic OpenAI node textComplete:
- Output data: JSON contains `id`, `object`, `created`, `model`, `choices` array with objects having `text`, `index`, `logprobs`, `finish_reason`.
- Alternatively depending node version, output includes `result`? Some n8n OpenAI node returns output with `choices` at top level.
So we can use FunctionItem to extract:
```
const content = item.json.choices?.[0]?.text ?? item.json.choices?.[0]?.message?.content ?? item.json.result ?? '';
const classification = content.trim().toLowerCase();
return { json: { classification } };
```
Then Switch node checks:
- Soporte: value contains "soporte"
- Ventas: value contains "ventas"
- Otro: value contains "otro" or fallback? The user says classify as one of those. We can route to three outputs. Switch node each rule can have regex or contains. If no match maybe? Switch node in n8n has "Fallback" output? Actually Switch node routes based on rules; if no rule matches, item goes to fallback? Yes in n8n Switch node has an "output" for each rule and optionally "fallback" output. Need set fallback to general perhaps. To handle "otro", we can create a rule for "otro", and Fallback to general? But then support/ventas wrong? Let's be careful.

The classification might return "otro", but if not one of three default, should go to general. But user says OpenAI must classify as "soporte", "ventas" o "otro". So likely one of those. We can set rules:
1. "={{ $json.classification.includes('soporte') }}" -> output 0 -> #support
2. "={{ $json.classification.includes('ventas') }}" -> output 1 -> #sales
3. "={{ $json.classification.includes('otro') }}" -> output 2 -> #general
But if the string includes "ventas" or "soporte" maybe okay.

N8N Switch node type "n8n-nodes-base.switch" parameters: `dataPropertyName`? The switch node has "Rules" on "Data Type" and value. Could use rules with "Conditions" on a property. The old Switch node uses "dataPropertyName": "classification", "dataType": "string", "value": "soporte", "operation": "contains", etc. The output routing is based on "rules" array? Let's recall n8n Switch node JSON.

In older n8n, Switch node type "n8n-nodes-base.switch" parameters:
```
"parameters": {
  "dataPropertyName": "classification",
  "dataType": "string",
  "value": "soporte",
  "operation": "equals",
  "rules": [
    {
      "dataType": "string",
      "value": "soporte",
      "operation": "equals"
    },
    {
      "dataType": "string",
      "value": "ventas",
      "operation": "equals"
    }
  ],
  "options": {
    "fallback": true
  }
}
```
But I think the switch node has different structure across versions. In new n8n switch node, parameters include `rules` where each rule has conditions. Let's find from memory.

Example n8n Switch node JSON:
```
{
  "name": "Switch",
  "type": "n8n-nodes-base.switch",
  "parameters": {
    "rules": [
      {
        "conditions": [
          {
            "leftValue": "={{ $json.classification }}",
            "rightValue": "soporte",
            "operator": "contains"
          }
        ]
      },
      {
        "conditions": [
          {
            "leftValue": "={{ $json.classification }}",
            "rightValue": "ventas",
            "operator": "contains"
          }
        ]
      }
    ],
    "options": {
      "fallback": true
    }
  }
}
```
Newer Switch node has `rules` with `conditions`. Old version had `dataPropertyName` and `rules` were values? Need be compatible.

N8N node version in workflow JSON uses `"typeVersion"`? Could specify. If typeVersion old, maybe structure old. We can use more recent typeVersion 3? Let's create with typeVersion 3? Need know node type versions. The Webhook typeVersion maybe 2. OpenAi typeVersion maybe 3? Slack typeVersion 2.1? Hmm.

Could omit typeVersion? In n8n workflow JSON, typeVersion is optional? It may default to latest? But if omitted, n8n uses default? I think `typeVersion` is part of node, but maybe defaults to 1. To be safe, include proper typeVersion values. Need decide.

Maybe produce workflow JSON with modern n8n (1.x) node versions. We need include typeVersion for nodes:
- Webhook: typeVersion 2 (or 1)
- FunctionItem: typeVersion 1
- OpenAI: typeVersion 3? Need know.
- Switch: typeVersion 3? Maybe typeVersion 2?
- Slack: typeVersion 2.1? maybe typeVersion 2.

Let's recall n8n nodes type versions:
- n8n-nodes-base.webhook: typeVersion 1? In latest, webhook typeVersion 2. The parameters differ? likely.
- n8n-nodes-base.functionItem: typeVersion 1.
- n8n-nodes-base.openAi: typeVersion maybe 3. Need check. Classic OpenAI node has typeVersion 3. The `resource` values differ by version. 
- n8n-nodes-base.switch: typeVersion 3? The Switch node I think is typeVersion 3, but there's typeVersion 1 old, 2? Hmm.
- n8n-nodes-base.slack: typeVersion 2.1 maybe? Actually Slack node is typeVersion 2.1 or 2.

Maybe we can avoid typeVersion mistakes by using "n8n-nodes-base.dispatcher"??? No.

Alternative: Generate workflow JSON for n8n using generic nodes with typeVersion omitted. But n8n import may infer. It is better to include typeVersion.

Let's search memory. I have seen n8n workflow JSON exports. Nodes often include `"typeVersion": 2` for Webhook, `"typeVersion": 2` for Switch, `"typeVersion": 1` for FunctionItem, `"typeVersion": 3` for OpenAI, `"typeVersion": 2.1` for Slack? Example from n8n templates:

```
{
  "name": "Webhook",
  "type": "n8n-nodes-base.webhook",
  "typeVersion": 2,
  "parameters": {
    "path": "...",
    "httpMethod": "POST",
    "responseMode": "onReceived",
    "options": {}
  }
}
```
FunctionItem:
```
"typeVersion": 1
```
Switch:
```
"type": "n8n-nodes-base.switch",
"typeVersion": 3,
"parameters": {
 "rules": [ ... ]
}
```
OpenAI:
```
"type": "n8n-nodes-base.openAi",
"typeVersion": 3,
"parameters": {
 "resource": "textComplete",
 "model": "gpt-3.5-turbo-instruct",
 "prompt": "..."
}
```
Slack:
```
"type": "n8n-nodes-base.slack",
"typeVersion": 2.1,
"parameters": {
 "authentication": "oAuth2",
 "resource": "message",
 "operation": "post",
 "channel": "#support",
 "text": "...",
 "options": {}
}
```
This seems plausible.

Need maybe include credentials placeholders? For OpenAI and Slack, users need to configure credentials. In JSON can include credentials names. Need include `"credentials"` at workflow level? Actually each node has credentials dictionary with `"openAiApi": { "id": ..., "name": "OpenAI account" }` and Slack. But IDs are instance-specific. For import, maybe use name placeholders. The workflow JSON includes a `credentials` section? Let's see n8n workflow structure:
```
{
  "name": "Workflow...",
  "nodes": [...],
  "connections": {...},
  "active": false,
  "settings": {},
  "versionId": "...",
  "meta": ...
}
```
Nodes can have `"credentials": {}`? Actually node JSON has `"credentials": { "openAiApi": { "id": "123", "name": "OpenAI account" } }`. If we put with placeholder name, user can import and select. If we omit credentials, maybe nodes won't have credential selected. The import still works? The credentials field may be required? n8n import will prompt to select credentials if missing or invalid. We can include `"credentials": { "openAiApi": { "name": "OpenAI account" } }` maybe. But if using `id` bad. Better omit or use empty? Let's think.

When you export an n8n workflow, nodes include credentials:
```
"credentials": {
  "openAiApi": {
    "id": "...",
    "name": "OpenAI"
  }
}
```
The `id` is not portable; the `name` can be used? On import, if the name exists, it uses that credential? I think yes, if name matches. If not, import may fail or prompt. We can include placeholder names "OpenAI API" and "Slack OAuth2". The user can change. However to be safe, perhaps mention "requiere configurar credenciales de OpenAI y Slack" after JSON. We can set `credentials` names to "OpenAI account" and "Slack account".

Need know credential key for OpenAI node: likely `openAiApi` (or `openAiApiV2`?). In n8n, OpenAI node credentials type is "openAiApi". The key in node JSON is `openAiApi`. 
Slack node credentials: For OAuth2, key is `slackOAuth2Api` maybe. The Slack node has several authentication methods: accessToken, oAuth2. Credential key for OAuth2 is "slackOAuth2Api". For user simplicity, maybe use "accessToken" with token parameter? But Slack node can use "accessToken" credential with key "slackAccessToken". Which type? In node parameters, `authentication` can be "oAuth2" or "accessToken". If we set `authentication` as "accessToken", credential key is `slackApi`? Let's recall.

Slack node doc:
- Credential type "Slack API" (n8n credentials) maybe key `slackApi`.
- For OAuth2, "Slack OAuth2 API" key `slackOAuth2Api`.
Node parameters:
```
"parameters": {
  "authentication": "oAuth2",
  "resource": "message",
  "operation": "post",
  "channel": "#support",
  "text": "...",
  "options": {}
}
```
Credentials:
```
"credentials": {
  "slackOAuth2Api": {
    "name": "Slack account"
  }
}
```
If user uses API token, set authentication: "accessToken" and credentials key `slackApi` maybe. Could use OAuth2 standard.

But maybe Slack node typeVersion 2.1 has parameter `authentication` values "accessToken", "oAuth2". If credentials missing, import might fail. We'll include placeholder.

Need possibly include "connection" between nodes. Connections object maps source node to target nodes. Need define connections. Webhook -> Set/Function -> OpenAI -> Function? -> Switch -> Slack nodes. We'll have:
- Webhook1 (Webhook)
- Extract1 (FunctionItem) maybe "Extract email y message"
- OpenAi1 (OpenAI)
- CleanClassification1 (FunctionItem) maybe "Normalizar clasificación"
- Switch1 (Switch)
- SlackSoporte, SlackVentas, SlackGeneral (Slack)

Connections:
```
{
  "Webhook": { "main": [[ "Extract" ]] },
  "Extract": { "main": [[ "OpenAI" ]] },
  "OpenAI": { "main": [[ "CleanClassification" ]] },
  "CleanClassification": { "main": [[ "Switch" ]] },
  "Switch": { "main": [[ "SlackSoporte" ], [ "SlackVentas" ], [ "SlackGeneral" ]] }
}
```
Need connection indexes match outputs.

Need ensure Switch rule outputs are three outputs. With fallback maybe outputs 3? For three rules and fallback maybe outputs 4? Actually Switch node: Each rule has output index. Fallback output is at last index if enabled. If 3 rules, outputs: 0,1,2 and 3 for fallback? If fallback enabled, output 3 is fallback. But we can connect fallback also to general? Need know. Could avoid fallback by making "otro" rule as third. For unclassified (shouldn't happen) we might not route. But connection can only map to three Slack nodes. Could set fallback true and connect output 3 to #general too. But n8n Switch node outputs: if fallback enabled, it creates an extra output for unmatched items. If 3 rules + fallback, there are 4 outputs. We can connect outputs 0->Soporte, 1->Ventas, 2->Otro, 3->General (fallback). But we only have three Slack nodes, with General used for both "otro" and fallback. That seems robust. Need ensure node connection can have multiple source outputs: 
```
"Switch": {
  "main": [
    [ "SlackSoporte" ],
    [ "SlackVentas" ],
    [ "SlackGeneral" ],
    [ "SlackGeneral" ]
  ]
}
```
But can the same target node be connected from two different outputs? Yes, n8n can have multiple connections to same node. We can connect output 2 and 3 to SlackGeneral. That means SlackGeneral node will execute twice for fallback and otro? Actually if items route to either output, SlackGeneral receives them, maybe combined if both outputs connect to same node? In n8n, if multiple connections from different outputs to same target node, the target node executes once per branch maybe? Actually nodes execute based on incoming items from all connections. It should be okay.

But simpler: do not enable fallback; use rules for three classes and if none match, maybe items go nowhere. The user didn't ask fallback. We can set "options": {} with no fallback. But that may drop unclassified. Better maybe set fallback to output 3 and connect to SlackGeneral. I'll include fallback true and connect both. Need ensure Switch node structure supports fallback.

Need perhaps include "Settings" maybe.

Need produce JSON. Let's craft carefully.

First, Webhook node JSON:
```
{
  "parameters": {
    "path": "webhook/email-classifier",
    "httpMethod": "POST",
    "responseMode": "onReceived",
    "options": {}
  },
  "id": "uuid1",
  "name": "Webhook",
  "type": "n8n-nodes-base.webhook",
  "typeVersion": 2,
  "position": [0, 0],
  "webhookId": "uuid-webhook"
}
```
Need id? The `id` and `webhookId` are uuids. If omitted, n8n may generate? For import, nodes usually include id. We can generate fake UUIDs. But maybe not necessary? In workflow JSON, each node needs `id`? In n8n import, if IDs are strings unique, okay. We'll include simple IDs: "node-webhook", etc. But typical n8n uses UUIDs. Could include fake valid-looking UUIDs. Need maybe `webhookId` required? Webhook node has `webhookId` maybe. If import, may generate. We can include static.

Could use simplified IDs: "webhook-node", "set-fields-node", "openai-classify-node", "clean-classifier-node", "switch-router-node", "slack-support-node", "slack-sales-node", "slack-general-node". That's okay for JSON.

Position: coordinate arrays.

But if user imports into n8n, positions don't matter. Need maybe active false.

Second, extract FunctionItem node. Type `n8n-nodes-base.functionItem`, typeVersion 1.
Parameters:
```
"jsCode": "const body = $input.first().json.body || $input.first().json;\nreturn [{ json: { email: body.email, message: body.message } }];"
```
Need function item code in n8n uses `$input.first()`? In function item node, code receives item as `item`? Actually `functionItem` node (execute once for each item) code uses `item` variable. We can write:
```
const body = item.json.body || item.json;
return {
  json: {
    email: body.email,
    message: body.message
  }
};
```
But in n8n function item, `item` is the current item. It returns an object or array? In `functionItem`, return `{ json: ... }`. So we'll use:
```
const body = item.json.body || item.json;
return {
  json: {
    email: body.email,
    message: body.message
  }
};
```
Need maybe return `item`? Actually function item node's code must return an object with "json". Good.

Need maybe use `.json.body?.email ?? $json.email`? Use optional.

But note if webhook outputs items with body nested. The function `return { json: { email: item.json.body.email, message: item.json.body.message } }` might fail if body undefined. Use robust.

Third, OpenAI node. Need configure prompt. Use expression:
```
"prompt": "=Clasifica el siguiente mensaje de cliente en una de estas categorías: soporte, ventas, otro. Devuelve únicamente la palabra de categoría.\n\nMensaje: {{ $json.message }}"
```
But in n8n JSON string, need escape newlines and quotes. Could use `{{ $json.message }}`. In JSON, this is fine. If using `=` expression, inside parameter string.

OpenAI node parameters:
```
"parameters": {
  "resource": "textComplete",
  "model": "gpt-3.5-turbo-instruct",
  "prompt": "=Clasifica el siguiente mensaje de cliente en una de estas categorías exactas: soporte, ventas, otro. Devuelve únicamente la palabra de categoría.\n\nMensaje:\n{{ $json.message }}",
  "options": {
    "temperature": 0
  }
}
```
But openAI node maybe requires "engine" not "model" for typeVersion 1? Need maybe use `model` if typeVersion 3. Let's include `model` and typeVersion 3. If older n8n, maybe won't work. But should.

Could use Chat completion instead to use gpt-3.5-turbo (more common). For OpenAI textComplete model "gpt-3.5-turbo-instruct" may not be allowed? Actually OpenAI completions endpoints support gpt-3.5-turbo-instruct (legacy). That's fine. But maybe uses "text-davinci-003" older. To be safe, maybe use chatComplete with messages. But need know exact parameters of OpenAI node typeVersion 3 supports both `textComplete` and `chatComplete`? Let's recall.

OpenAI node (classic) version 3: Resource values:
- "textComplete" or "chatComplete"? I found in n8n docs for OpenAI node: Resource includes "Text" and "Image"; Operation includes "Complete", "Message a Model", "Image Generate". The node typeVersion might be 3. The parameters for "Text" resource and "Complete" operation:
```
"resource": "textComplete",
"model": "gpt-3.5-turbo-instruct",
"prompt": "..."
```
For "Message a Model" operation:
```
"resource": "chatComplete",
"model": "gpt-3.5-turbo",
"messages": [
  { "role": "system", "content": "..." },
  { "role": "user", "content": "..." }
]
```
So either works. Chat completion might output `choices[0].message.content`.

I think using Chat completion is more modern and yields cleaner output. But we need maybe the function to extract that. Let's use OpenAI node with resource `chatComplete`, model `gpt-3.5-turbo` (or `gpt-4o-mini`), messages system + user. The system prompt can instruct to return just category. The user message is `{{ $json.message }}`. That's good.

OpenAI node parameters:
```
{
  "resource": "chatComplete",
  "model": "gpt-3.5-turbo",
  "messages": [
    {
      "role": "system",
      "content": "Clasifica el mensaje del usuario en una de estas categorías: soporte, ventas, otro. Devuelve únicamente la palabra de la categoría."
    },
    {
      "role": "user",
      "content": "={{ $json.message }}"
    }
  ],
  "options": {
    "temperature": 0
  }
}
```
This likely works with typeVersion 3. Need expression for message: `"content": "={{ $json.message }}"`. Good.

But if OpenAI node uses classic `openAi`, `messages` parameter might be `messages` with explicit role? Yes.

After OpenAI, function item to extract classification:
```
const raw = item.json.choices?.[0]?.message?.content || item.json.choices?.[0]?.text || item.json.result || '';
const classification = raw.trim().toLowerCase();
return { json: { classification, email: item.json.email, message: ... } };
```
Need preserve original email for Slack message? The output of OpenAI node may not include original email/message. The CleanClassification node receives only OpenAI output, which does not contain email or message? We need later include email/message in Slack. So we need to bring along the original fields from earlier. But our CleanClassification node loses them. We can either use FunctionItem after webhook to create `email`, `message`, then pass them through OpenAI? The OpenAI node may pass through? In n8n, nodes typically combine input with output? Hmm. OpenAI node outputs its own JSON. It may include `$json` with OpenAI output only, but maybe it passes the input items as well? In n8n, nodes generally output only the node's data; but many nodes include input item in output if using "options": {}? Actually no. The OpenAI node returns only its response. So downstream nodes would not have original `email`/`message`. That's a problem.

We need preserve email/message after OpenAI. Solutions:
- Before OpenAI, include fields in prompt but not output; no.
- Use Node "Merge" after OpenAI to merge original with classification? Or use `$json` in Slack? If Slack nodes connected after Switch receive only classification item (no email/message). We need include email/message in Slack text. We can use expressions referencing previous node's data? In n8n, downstream nodes can reference earlier nodes in the execution chain only if the data is part of the item's JSON. In n8n, items passed through nodes; you cannot access arbitrary previous nodes unless using `$('Extract').item.json` maybe? But if the node is not in the chain? Actually n8n supports referencing any node with `$('Node Name').item.json`. You can reference prior nodes even if not directly connected? In n8n, yes, `$('Extract')` expression can access data of that node from the current execution. But in Slack message text, we could write `{{ $('Extract').item.json.email }}` and `{{ $('Extract').item.json.message }}`. However, if the node executed in the same run and output is single item, this might work. But if multiple items, `$('Extract').item` refers to first item? Might be okay for single. But better to pass fields through.

Alternative: Use FunctionItem after OpenAI to combine with earlier data using `$('Extract').item.json` as fallback? But the function node only has current item as `item`, not direct access to previous node? It has access to `$items` maybe? In n8n function node (not function item) can use `$('Extract').item`. But function item could use `$('Extract').first().json` maybe. That would work. Could produce JSON with email/message/classification. Then Switch routes with JSON containing all. So CleanClassification function can return:
```
const raw = item.json.choices?.[0]?.message?.content || item.json.choices?.[0]?.text || item.json.result || '';
const classification = raw.trim().toLowerCase();
const original = $('Extract').first().json;
return {
  json: {
    email: original.email,
    message: original.message,
    classification: classification
  }
};
```
But in function item node, `$('Extract')` might not exist? In n8n expression, function nodes have access to `$('NodeName')` if node is in the same execution? Yes.

However, if nodes execute per item and you reference previous node, it may return the first item from that node. For single item, okay.

Could also use n8n's "Merge" node to combine. But easier: Use one FunctionItem after OpenAI.

But wait: OpenAI node output from a single input item may contain multiple choices? Usually one. Our CleanClassification node receives input item from OpenAI. We can refer back to "Extract" to get original. Good.

Alternatively, use a Set after Webhook and then another Set after OpenAI to copy from previous? But functions are easiest.

Need perhaps include "execute once" for Webhook? Default.

Switch node: Need check classification variable. We'll set rules with `leftValue` "={{ $json.classification }}" and operator "contains". But if `classification` includes "soporte" etc. Need ensure exact "soporte" not "soporte técnico". Use "contains". Order matters: "ventas" vs "soporte"? No conflict. But "soporte" might appear inside an unrelated phrase? The classifier returns just category, so okay.

Switch parameters with typeVersion 3:
```
"parameters": {
  "rules": [
    {
      "conditions": [
        {
          "leftValue": "={{ $json.classification }}",
          "rightValue": "soporte",
          "operator": "contains"
        }
      ]
    },
    {
      "conditions": [
        {
          "leftValue": "={{ $json.classification }}",
          "rightValue": "ventas",
          "operator": "contains"
        }
      ]
    },
    {
      "conditions": [
        {
          "leftValue": "={{ $json.classification }}",
          "rightValue": "otro",
          "operator": "contains"
        }
      ]
    }
  ],
  "options": {
    "fallback": true
  }
}
```
Need maybe `leftValue` require `dataType`? In recent switch node, `leftValue` can be expression string. The condition's `operator` can be `contains`. Right value maybe string.
Some switch versions require `leftValue` and `rightValue` not expression? I think expression works.

If fallback true, the third and fallback output? We'll connect as described.

Slack nodes:
Node type `n8n-nodes-base.slack`, typeVersion 2.1.
Parameters:
```
{
  "authentication": "oAuth2",
  "resource": "message",
  "operation": "post",
  "channel": "#support",
  "text": "=Nuevo mensaje de {{ $json.email }}\nMensaje: {{ $json.message }}\nClasificación: {{ $json.classification }}",
  "options": {}
}
```
Need maybe Slack node typeVersion 2.1 param `text` maybe should be `message`? Actually Slack node message post uses `text` parameter? In old Slack node, the parameter for message text is `text`. In newer version maybe `message`? Let's recall Slack node n8n: Resource `message`, operation `post`. Parameters: `channel`, `text`, `attachments`, `blocks`, etc. `text` is correct. The user wants "envie el email a un canal de Slack". Could send a message containing email and message. Text can include email. Maybe specify:
`"=Nuevo mensaje de {{ $json.email }}\n\nMensaje: {{ $json.message }}\n\nClasificado como: {{ $json.classification }}"`.
Use Slack channel names as #support, #sales, #general.

Credentials:
OpenAI node credentials:
```
"credentials": {
  "openAiApi": {
    "name": "OpenAI account"
  }
}
```
Slack node credentials:
```
"credentials": {
  "slackOAuth2Api": {
    "name": "Slack account"
  }
}
```
Need if using OAuth2. But if user doesn't have OAuth2, then access token? We can mention in comments. But in JSON maybe