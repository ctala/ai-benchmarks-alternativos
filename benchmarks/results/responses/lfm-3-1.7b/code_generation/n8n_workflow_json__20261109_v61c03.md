# LFM-3 1.7B — code_generation/n8n_workflow_json

- model_id: `liquid/lfm-3-1.7b`
- success: True  | final: 6.77 | quality: 6.92
- latency_total: 27.561s | tokens_per_second: 297.2
- input_tokens: 129 | output_tokens: 8192
- judge_score: 2.8 | justificación: 

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

We need to generate a N8N workflow in JSON that matches the described steps.

Let's parse the requirements:

1. Activate with a webhook POST (probably trigger via HTTP request, so node should be a Webhook Trigger).
2. Extract fields "email" and "message" from the body.
3. Use an AI node (OpenAI) to classify the message as "soporte", "ventas" or "otro".
4. Based on classification, send email to a different Slack channel:
   - soporte -> #support
   - ventas -> #sales
   - otro -> #general

Thus we need nodes: Webhook Trigger (POST), Set / Parse fields? In N8N we can use "Parse JSON" to extract email and message fields. Then AI node for classification using OpenAI (e.g., node "OpenAI API" or "Text Classifier"). Then routing based on result. Then a Slack node: probably "Send Message" or "Post to Channel" depending on type: need to send email to Slack? But they said "enviar el email a un canal de Slack diferente". That seems like sending an email that goes to a Slack channel? Or maybe "enviar email" means sending an email to the user? Wait: The phrase "enviar el email a un canal de Slack diferente" is ambiguous. It might mean "send an email to a different Slack channel"? Actually typical N8N workflows may have a node to send an email (like Send Email). And also post to Slack. But here it says "enviar el email a un canal de Slack diferente". Might be a mistake; perhaps they want to send an email to a channel of Slack? Let's interpret: After classification, we need to send an email to a specific Slack channel. Usually you would just send an email via the email node, but also mention which Slack channel? Or maybe they want to post to Slack channel. But they wrote "enviar el email a un canal de Slack diferente". Could be they want to forward the email content to the Slack channel.

Given typical N8N tasks: There is a "Set" node to define variables, then "HTTP Request" for OpenAI classification, then "Slack" node to post a message. They might combine both.

But let's design something plausible:

- Trigger: Webhook (POST) – receives incoming webhook.

- Step 1: Parse JSON input to get fields "email" and "message".

- Step 2: Use OpenAI node to classify "message" into categories ["soporte","ventas","otro"]. For this we need to pass the text and choose model. We'll assume a default prompt: "Classify the following message: {message}. Category options: soporte, ventas, otra." The output will be label.

- Step 3: Route based on category:
    - If "soporte": send an email to support@... and post to "#support" channel.
    - If "ventas": send email to sales@... and post to "#sales".
    - Else: send email to general (maybe generic) and post to "#general".

But they ask "enviar el email a un canal de Slack diferente". This could mean: send the email to a different Slack channel. So we might treat "send email" as using "Email" node targeting a specific address, but also maybe create a post to Slack channel containing the same info. However, more likely they intend: after classification, dispatch an email to a different Slack channel, i.e., send a message to that channel about the email? I'm not entirely sure.

Nevertheless, we can produce a JSON representation of the workflow that includes nodes in order, specifying their parameters.

I will go with these nodes:

1. **Webhook Trigger**: name "Webhook Trigger", event: "post" (or "webhook"), method POST, path maybe "/n8n/trigger". Input data: empty.

2. **Parse JSON** (Extract email & message): Input: the raw payload from webhook. Output variables: "email" and "message". Use field extraction: key "body" maybe contains JSON? Typically webhook body is JSON object. So we can set "Input Data" as raw JSON string.

3. **OpenAI Node** (classification): Name "Classify" (AI). Parameters: Model: "text-classification" maybe or "gpt-3.5-turbo". Prompt: "You are a classifier. Given the following message, categorize it as 'soporte', 'ventas' or 'otro'. Message: {message}". Output: "label" (the classification).

4. **Router (Switch)**: Branch based on classification result. Options: "soporte", "ventas", "otro". Each branch leads to appropriate action.

5. **Email Send** node: Using "Send Email" node (Gmail?). Provide to email variable, subject maybe classification result, etc.

6. **Slack Post** node: Use "Slack" node to post to channel "#support", "#sales", "#general". Need channel ID or name.

Alternatively we could combine email and slack in one step, but better separate.

Simplify: For each branch:

- If label == "soporte":
    - Email to "support@example.com"
    - Slack post to "#support"

- If label == "ventas":
    - Email to "sales@example.com"
    - Slack post to "#sales"

- Else ("otro"):
    - Email to "info@example.com" or "general@example.com"
    - Slack post to "#general"

We also need to map label case-insensitively? Possibly lowercasing.

Now constructing the JSON. N8N workflow JSON uses a specific format: It's basically a list of nodes or a "workflow" definition with keys like "name", "type", etc. Not exactly known. Since the user asked "Genera un workflow de N8N en JSON que..." they expect a complete JSON representing the whole workflow.

I need to find typical N8N workflow JSON schema. Might be similar to n8n-workflow.json used by plugins. Let me recall: N8N uses a YAML-like flowchart? Actually there is a standard "node" definitions and "workflow" composition. Searching memory: In N8N UI, you can export as JSON using "Export Workflow" feature. The file structure resembles an array of "nodes" connected via "activation" and "connection". Hard to guess exact syntax without reference. However, we can provide a plausible representation, describing each node with its properties.

Better approach: Provide a structured description of each step and a simplified JSON snippet showing nodes in order, referencing them by IDs. Perhaps the user expects something like:

{
  "id": "workflowId",
  "name": "My Workflow",
  "description": "...",
  "steps": [
    {
      "step_id": 1,
      "type": "webhook",
      ...
    },
    ...
  ]
}

But lacking official spec, we can give a reasonable approximation.

Given the difficulty, I'll craft a JSON that includes:

- "trigger": { "type":"webhook", "method":"POST", "path":"/n8n/webhook/post" }

- "parseJson": ... extracting fields

- "openaiClassify": { "model":"gpt-3.5-turbo", "prompt":"...", "responseFields":["label"] }

- "switch": { "condition": {"field":"classificationResult", "operations":["equals"],"values":["soporte","ventas","otro"]} }

Actually N8N has a built-in "Switch" node where you specify branches.

Then "emailSend" and "slackPost" nodes inside each branch.

Because full details of parameters may be too verbose, we can note placeholders.

The user explicitly wants "JSON completo del workflow". So they'd want entire thing; but we can present a pretty formatted JSON with comments? Probably no comments allowed in pure JSON.

Let's try to approximate.

One way: Represent the workflow as a list of nodes:

[
  { "id": "1", "name": "Webhook Trigger", "type": "Webhook", "event": "post", "urlPath": "https://app.n8n.io/sandbox/browser/run" }, // placeholder
  { "id": "2", "name": "Parse JSON", "type": "Parse", "inputDataVars": ["rawBody"], "variablesOutputs": ["email", "message"] },
  { "id": "3", "name": "Classify (OpenAI)", "type": "OpenAI", "parameters": { "model":"gpt-3.5-turbo", "prompt":"Classify the message below. Options: soporte, ventas, otro. Message: {{$json["message"]}}" }, "outputFields":["classification"] }, 
  { "id": "4", "name": "Switch", "conditions": [{ "variable": "classification", "operator":"equal", "values":["soporte","ventas","otro"] } ], "branches": [
     { "path":"5" , "type":"Send Email (Support)" },
     { "path":"6", "type":"Send Email (Sales)" },
     { "path":"7", "type":"Send Email (General)" }
   ]}
]

This is messy.

Perhaps simpler: Provide a high-level JSON describing each node and connections. I think it's okay to give a clear mapping rather than strict N8N JSON if unknown.

User asks: "Genera un workflow de N8N en JSON que: ... Dame el JSON completo del workflow." I will aim to deliver as comprehensive as possible.

To be safe, I can include a comment block explaining that due to N8N version differences, the JSON uses typical keys. Also indicate placeholder values.

I'll propose a workflow named "WebhookPost_ClassifyAndNotify".

Structure:

{
  "workflow": [
    {
      "id": "webhookTrigger",
      "name": "Webhook Trigger",
      "type": "n8n-nodes-base.webhook",
      "parameters": {
        "eventName": "post",
        "httpMethod": "POST",
        "path": "n8n-webhook.post"
      }
    },
    {
      "id": "parseFields",
      "name": "Parse Email and Message",
      "type": "n8n-nodes-base.parse",
      "inputs": [{"nodeId":"webhookTrigger"}],
      "variables": ["email","message"],
      "outputs": []
    },
    {
      "id": "classifyAi",
      "name": "Classify with OpenAI",
      "type": "n8n-nodes-base.openaiApi",
      "parameters": {
        "model": "gpt-3.5-turbo",
        "promptTemplate": "Classify the following message.\nMessage:\n{{ $json[\"message\"] }}\nCategory options: soporte, ventas, otro.",
        "outputFormat": "json",
        "fieldsToReturn": ["label"]
      }
    },
    {
      "id": "switch",
      "name": "Route Classification",
      "type": "n8n-nodes-base.switch",
      "conditions": [
        { "field": "label", "operator": "equals", "value": "soporte" },
        { "field": "label", "operator": "equals", "value": "ventas" },
        { "field": "label", "operator": "equals", "value": "otro" }
      ],
      "branches": [
        { "branchId": "emailSoporte", "targetNodeId": "sendEmailSupport" },
        { "branchId": "emailVentas", "targetNodeId": "sendEmailVentas" },
        { "branchId": "emailOtro", "targetNodeId": "sendEmailGeneral" }
      ]
    },
    // Each target node sends email and posts to Slack
    {
      "id": "sendEmailSupport",
      "name": "Send Support Email",
      "type": "n8n-nodes-base.emailSend",
      "parameters": {
        "to": "support@example.com",
        "subject": "New message classified as soporte",
        "htmlBody": "To: {{$json.email}}\nSubject: Soporte\n..."
      }
    },
    {
      "id": "postToSlackSupport",
      "name": "Post to Slack #support",
      "type": "n8n-nodes-base.slack",
      "parameters": { "channel": "#support" }
    },
    // similarly for ventas and general...
  ]
}

But that's extremely detailed and missing many fields.

Maybe better to break down into separate sections: Steps.

Given constraints, I'll provide a reasonably full JSON with placeholder IDs and descriptions, focusing on clarity.

Potential final answer:

```json
{
  "name": "N8N Workflow: Webhook → Extract → AI Classify → Slack Email",
  "version": "1.0",
  "triggers": [
    {
      "id": "1",
      "type": "n8n-nodes-base.webhook",
      "name": "Webhook Trigger",
      "event": "post",
      "httpMethod": "POST",
      "path": "/n8n/trigger"
    }
  ],
  "steps": [
    {
      "id": "2",
      "name": "Parse JSON fields",
      "type": "n8n-nodes-base.parse",
      "inputs": "[{\"nodeId\":\"1\",\"jsonParameters\":{}}]",
      "variables": ["email","message"],
      "outputs": [],
      "keepOnlySet": false
    },
    {
      "id": "3",
      "name": "Classify message with OpenAI",
      "type": "n8n-nodes-base.openaiApi",
      "parameters": {
        "apiKey": "<YOUR_OPENAI_API_KEY>",
        "model": "gpt-3.5-turbo",
        "prompt": "Classify the following message. Choose one of: \"soporte\", \"ventas\", \"otro\".\nMessage: {{$json[\"message\"]}}",
        "maxTokens": 150
      },
      "outputs": ["label"],
      "namePrefix": "classify"
    },
    {
      "id": "4",
      "name": "Switch on classification",
      "type": "n8n-nodes-base.switch",
      "conditions": [
        { "field": "label", "operator": "equals", "value": "soporte" },
        { "field": "label", "operator": "equals", "value": "ventas" },
        { "field": "label", "operator": "equals", "value": "otro" }
      ],
      "routes": [
        {
          "id": "route_support",
          "path": "5",
          "actions": [
            { "id": "5a", "type": "n8n-nodes-base.emailSend", "parameters": { "to": "support@example.com", "subject": "Intento de soporte", "htmlBody": "{{ $json.email }} – Category: soporte" } },
            { "id": "5b", "type": "n8n-nodes-base.slack", "parameters": { "channel": "#support" } }
          ]
        },
        {
          "id": "route_ventas",
          "path": "6",
          "actions": [
            { "id": "6a", "type": "n8n-nodes-base.emailSend", "parameters": { "to": "sales@example.com", "subject": "Oferta de ventas", "htmlBody": "{{ $json.email }} – Category: ventas" } },
            { "id": "6b", "type": "n8n-nodes-base.slack", "parameters": { "channel": "#sales" } }
          ]
        },
        {
          "id": "route_other",
          "path": "7",
          "actions": [
            { "id": "7a", "type": "n8n-nodes-base.emailSend", "parameters": { "to": "general@example.com", "subject": "Información general", "htmlBody": "{{ $json.email }} – Category: otro" } },
            { "id": "7b", "type": "n8n-nodes-base.slack", "parameters": { "channel": "#general" } }
          ]
        }
      ]
    },
    {
      "id": "5a",
      "name": "Send Email (Support)",
      "type": "n8n-nodes-base.emailSend",
      "parameters": {
        "to": "support@example.com",
        "subject": "Soporte solicitado",
        "htmlBody": "Hello,\n\nMessage: {{$json.message}}\n\n---\nCategory: soporte\n\nThank you."
      }
    },
    {
      "id": "5b",
      "name": "Post to Slack #support",
      "type": "n8n-nodes-base.slack",
      "parameters": { "channel": "#support" }
    },
    {
      "id": "6a",
      "name": "Send Email (Sales)",
      "type": "n8n-nodes-base.emailSend",
      "parameters": {
        "to": "sales@example.com",
        "subject": "Ventas",
        "htmlBody": "..."
      }
    },
    {
      "id": "6b",
      "name": "Post to Slack #sales",
      "type": "n8n-nodes-base.slack",
      "parameters": { "channel": "#sales" }
    },
    {
      "id": "7a",
      "name": "Send Email (General)",
      "type": "n8n-nodes-base.emailSend",
      "parameters": { "to": "general@example.com", ... }
    },
    {
      "id": "7b",
      "name": "Post to Slack #general",
      "type": "n8n-nodes-base.slack",
      "parameters": { "channel": "#general" }
    }
  ],
  "active": true
}
```

That is huge. It mixes many node types incorrectly. But perhaps enough.

However, the proper JSON for N8N may require arrays for connections. Without exact spec it's impossible to guarantee validity. Maybe easier: Provide a concise overview in plain English plus a sample JSON that captures main components. The user didn't specify exact format.

Given the open-endedness, I'll adopt a pragmatic approach: Write a clear JSON object with top-level fields: "name", "nodes": [list], "connections": [...]. Include necessary fields: node id, type, settings. Add comments in code block style but keep valid JSON (no comments). I can embed placeholders like "<YOUR_API_KEY>", "<EMAIL>", "#support". Use double quotes only.

Alright, let's construct a manageable yet complete JSON.

Define nodes:

- node1: "Webhook Trigger (POST)". Type: "Webhook". Event: "post". URL: ... Not needed.

- node2: "Parse JSON" (extract email and message). Input: node1. Variables output: email, message.

- node3: "OpenAI Classify" (text classification). Input: node2 (variables). Model: "gpt-3.5-turbo". Prompt: "Classify the following text: {{$json.message}}. Answer should be one of: soporte, ventas, otro." Output field: result (label).

- node4: "Switch" (routing). Condition: check label equals any of three. Branches:

   * Branch A: label = "soporte". Go to node5.
   * Branch B: label = "ventas". Go to node6.
   * Branch C: label = "otro". Go to node7.

- node5: "Send Email (support)". Input: node4->branchA. To: "support@example.com". Subject: "Soporte request". Body includes email and message.

- node6: "Send Email (sales)". To: "ventas@example.com".

- node7: "Send Email (general)". To: "general@example.com".

- node8: "Post to Slack (#support)". Input: node4->branchA. Channel "#support". Text: similar.

- node9: "Post to Slack (#sales)". Input: branchB. Channel "#sales".

- node10: "Post to Slack (#general)". Input: branchC. Channel "#general".

Thus total nodes = 10.

Will represent each node with an id. Also show connections. Provide a "connections" array linking inputs/outputs.

Better to simplify: In JSON we can just describe sequentially. Realistically, N8N workflow JSON doesn't exist publicly widely.

Given the time, I'll produce a fairly complete but illustrative JSON. I'll avoid deep nesting errors.

Let’s write:

{
  "workflowName": "Webhook → Extract → AI Classify → Slack Email",
  "trigger": { "type": "webhook", "event": "post", "url": "http://yourdomain.com/n8n/webhook/post" },
  "steps": [
    {
      "id": "1",
      "name": "Parse JSON Fields",
      "type": "n8n-nodes-base.parse",
      "inputs": ["webhookTrigger"],
      "variablesOutputs": ["email","message"], 
      "outputFieldNames": ["email","message"]
    },
    {
      "id": "2",
      "name": "Classify with OpenAI",
      "type": "n8n-nodes-base.openaiApi",
      "parameters": {
        "apiKey": "YOUR_OPENAI_API_KEY",
        "model": "gpt-3.5-turbo",
        "prompt": "Classify the following message. Options: soporte, ventas, otro. Message: {{$json[\"message\"]}}",
        "max_tokens": 200
      },
      "outputFieldNames": ["result"]
    },
    {
      "id": "3",
      "name": "Switch on Classification",
      "type": "n8n-nodes-base.switch",
      "parameters": {
        "conditions": [
          { "field": "result", "operator": "equal", "value": "soporte" },
          { "field": "result", "operator": "equal", "value": "ventas" },
          { "field": "result", "operator": "equal", "value": "otro" }
        ]
      },
      "routes": [
        { "path": "4a", "nodeId": "5" },
        { "path": "4b", "nodeId": "6" },
        { "path": "4c", "nodeId": "7" }
      ]
    },
    {
      "id": "4a",
      "name": "Send Email – Soporte",
      "type": "n8n-nodes-base.emailSend",
      "parameters": {
        "to": "support@example.com",
        "subject": "Soporte solicitado",
        "htmlBody": "Hello,\nMessage: {{$json[\"message\"]}}\n\nCategory: soporte\n\nThanks."
      }
    },
    {
      "id": "4b",
      "name": "Post to Slack #support",
      "type": "n8n-nodes-base.slack",
      "parameters": { "channel": "#support" }
    },
    {
      "id": "4c",
      "name": "Send Email – Ventas",
      "type": "n8n-nodes-base.emailSend",
      "parameters": {
        "to": "sales@example.com",
        "subject": "Oferta",
        "htmlBody": "..."
      }
    },
    {
      "id": "5",
      "name": "Send Email – General",
      "type": "n8n-nodes-base.emailSend",
      "parameters": {
        "to": "general@example.com",
        "subject": "Información general",
        "htmlBody": "..."
      }
    },
    {
      "id": "6",
      "name": "Post to Slack #sales",
      "type": "n8n-nodes-base.slack",
      "parameters": { "channel": "#sales" }
    },
    {
      "id": "7",
      "name": "Post to Slack #general",
      "type": "n8n-nodes-base.slack",
      "parameters": { "channel": "#general" }
    }
  ],
  "active": true
}

But we lost some details such as connecting step outputs. For a realistic connection diagram we could give a "connections" property mapping node ids.

Given the complexity and lack of exact specification, I'll produce a cleaned-up JSON with minimal extraneous but still complete. I think it's acceptable to give a conceptual JSON and explain what each part does.

The user asked: "Dame el JSON completo del workflow." So I must supply a single JSON code block. I'll do my best.

I'll attempt to follow typical N8N "workflow export" layout. Quick search memory: N8N exports can be found at https://docs.n8n.io/en/latest/exports-workflows/ . The file looks like an array of objects with fields: "nodes": [ { "id":..., "type": ..., "position":..., "connectors": [...]}, ... ] etc. But I cannot replicate exactly.

So I'll respond acknowledging that the JSON is a simplified representation and include all required elements:

- Trigger (Webhook POST)
- Parse fields
- AI classification (OpenAI)
- Switch based on result
- Branching actions: Email + Slack per branch.

Add placeholders for secrets.

Also ensure correct Spanish terms: "soporte", "ventas", "otro". Ensure lowercase vs uppercase, classification returns maybe capitalized. We'll use lower.

Write final answer: Provide JSON with top-level "workflow" array.

### Example JSON:

```json
{
  "name": "Webhook → Extracción → Clasificación IA → Envío por email y Slack",
  "description": "Recibe un POST webhook, extrae email y mensaje, clasifica con OpenAI (soporte/ventas/otro), envía el email al canal correspondiente y publica un mensaje en Slack.",
  "triggers": [
    {
      "id": "trigger1",
      "type": "n8n-nodes-base.webhook",
      "event": "post",
      "httpMethod": "POST",
      "path": "/n8n/incoming/feed"
    }
  ],
  "steps": [
    {
      "id": "step1",
      "name": "Parse JSON fields",
      "type": "n8n-nodes-base.parse",
      "inputs": ["trigger1"],
      "parameters": {
        "inputProperties": {}
      },
      "variablesOutputs": ["email","message"],
      "outputFields": ["email","message"]
    },
    {
      "id": "step2",
      "name": "Classify with OpenAI",
      "type": "n8n-nodes-base.openaiApi",
      "parameters": {
        "apiKey": "<YOUR_OPENAI_API_KEY>",
        "model": "gpt-3.5-turbo",
        "prompt": "Clasifica el siguiente mensaje. Opciones: soporte, ventas, otro.\nMessage: {{$json[\"message\"]}}",
        "maxPromptLength": 300
      },
      "outputFields": ["classification"]
    },
    {
      "id": "step3",
      "name": "Switch on classification",
      "type": "n8n-nodes-base.switch",
      "parameters": {
        "conditions": [
          { "field": "classification", "operator": "equal", "value": "soporte" },
          { "field": "classification", "operator": "equal", "value": "ventas" },
          { "field": "classification", "operator": "equal", "value": "otro" }
        ]
      },
      "branches": [
        { "id": "branch_suporte", "targetStep": "step5" },
        { "id": "branch_ventas", "targetStep": "step6" },
        { "id": "branch_otro", "targetStep": "step7" }
      ]
    },
    {
      "id": "step4a",
      "name": "Send Email – Soporte",
      "type": "n8n-nodes-base.emailSend",
      "parameters": {
        "to": "support@example.com",
        "subject": "Soporte solicitado",
        "htmlBody": "Hola,\n\nMensaje: {{$json.message}}\n\nCategoría: soporte\n\nGracias."
      }
    },
    {
      "id": "step5",
      "name": "Post to Slack #support",
      "type": "n8n-nodes-base.slack",
      "parameters": { "channel": "#support" },
      "outputFields": [] 
    },
    {
      "id": "step4b",
      "name": "Send Email – Ventas",
      "type": "n8n-nodes-base.emailSend",
      "parameters": {
        "to": "ventas@example.com",
        "subject": "Oferta de ventas",
        "htmlBody": "..."
      }
    },
    {
      "id": "step6",
      "name": "Post to Slack #sales",
      "type": "n8n-nodes-base.slack",
      "parameters": { "channel": "#sales" }
    },
    {
      "id": "step4c",
      "name": "Send Email – General",
      "type": "n8n-nodes-base.emailSend",
      "parameters": {
        "to": "general@example.com",
        "subject": "Información general",
        "htmlBody": "..."
      }
    },
    {
      "id": "step7",
      "name": "Post to Slack #general",
      "type": "n8n-nodes-base.slack",
      "parameters": { "channel": "#general" }
    }
  ],
  "active": true
}
```

Again missing connections between steps, but overall shows IDs.

Probably better to collapse into a single root array with all nodes and "connections". However, writing everything correctly is a lot.

Given the uncertainty, I'll produce a cleaner but slightly less technical JSON, using descriptive fields, and highlight placeholders.

I'll add a section "connections" summarizing mapping:

- trigger1 -> step1
- step1 -> step2
- step2 -> step3
- step3 -> step4 (switch)
- step4 branch "soporte" -> step5 (send email) & step5a (slack)
- branch "ventas" -> step6 & step6a (slack)
- branch "otro" -> step7 & step7a (slack)

But this gets messy.

I think a good compromise is to present the workflow as a sequence of steps, not necessarily strict JSON of N8N export. The user likely expects something akin to a JSON describing nodes and connections.

I'll prepare final answer accordingly, making sure to enclose in triple backticks with ```json.

I'll include sections:

- Overview: triggers, steps.
- Node definitions (ID, name, type, main parameters).
- Connections.

All within the outer braces.

Let's draft now.

---

## Full JSON

```json
{
  "workflow": {
    "name": "Webhook-Post → Parse → AI Classification → Slack + Email",
    "description": "Receives a POST webhook, extracts email and message, classifies message with OpenAI (soporte/ventas/otro), then sends an email to the corresponding address and posts a Slack message to the matching channel.",
    "triggers": [
      {
        "id": "trigger_webhook",
        "type": "n8n-nodes-base.webhook",
        "event": "post",
        "httpMethod": "POST",
        "path": "/n8n/webhook/payload",
        "description": "External system pushes a JSON payload to this endpoint."
      }
    ],
    "steps": [
      {
        "id": "step_parse",
        "name": "Parse JSON fields",
        "type": "n8n-nodes-base.parse",
        "inputs": ["trigger_webhook"],
        "parameters": {
          "jsonPath": "$.json"   // assuming the webhook body is JSON under key "json"
        },
        "variablesOutputs": [
          { "name": "email", "type": "string" },
          { "name": "message", "type": "string" }
        ],
        "outputFields": ["email","message"]
      },
      {
        "id": "step_classify",
        "name": "Classify with OpenAI (gpt-3.5-turbo)",
        "type": "n8n-nodes-base.openaiApi",
        "parameters": {
          "apiKey": "<YOUR_OPENAI_API_KEY>",
          "model": "gpt-3.5-turbo",
          "prompt": "Classify the following message. Choose one of: \"soporte\", \"ventas\", \"otro\".\nMessage: {{$json[\"message\"]}}",
          "maxTokens": 200
        },
        "outputFields": ["classification"]
      },
      {
        "id": "step_switch",
        "name": "Route based on classification",
        "type": "n8n-nodes-base.switch",
        "parameters": {
          "conditions": [
            { "field": "classification", "operator": "equal", "value": "soporte" },
            { "field": "classification", "operator": "equal", "value": "ventas" },
            { "field": "classification", "operator": "equal", "value": "otro" }
          ]
        },
        "branches": [
          { "id": "branch_support", "target_step": "step_email_support" },
          { "id": "branch_ventas", "target_step": "step_email_ventas" },
          { "id": "branch_otro", "target_step": "step_email_general" }
        ]
      },
      {
        "id": "step_email_support",
        "name": "Send email – Soporte",
        "type": "n8n-nodes-base.emailSend",
        "parameters": {
          "to": "support@example.com",
          "subject": "Soporte solicitado",
          "htmlBody": "Hello,\n\nMessage: {{$json[\"message\"]}}\n\nCategoría: soporte\n\nThank you."
        }
      },
      {
        "id": "step_email_ventas",
        "name": "Send email – Ventas",
        "type": "n8n-nodes-base.emailSend",
        "parameters": {
          "to": "ventas@example.com",
          "subject": "Oferta de ventas",
          "htmlBody": "Hello,\n\nMessage: {{$json[\"message\"]}}\n\nCategoría: ventas\n\nBest regards."
        }
      },
      {
        "id": "step_email_general",
        "name": "Send email – General",
        "type": "n8n-nodes-base.emailSend",
        "parameters": {
          "to": "general@example.com",
          "subject": "Información general",
          "htmlBody": "Hello,\n\nMessage: {{$json[\"message\"]}}\n\nCategoría: otro\n\nRegards."
        }
      },
      {
        "id": "step_post_slack_support",
        "name": "Post to Slack #support",
        "type": "n8n-nodes-base.slack",
        "parameters": { "channel": "#support" },
        "connectionFrom": "step_email_support"
      },
      {
        "id": "step_post_slack_ventas",
        "name": "Post to Slack #sales",
        "type": "n8n-nodes-base.slack",
        "parameters": { "channel": "#sales" },
        "connectionFrom": "step_email_ventas"
      },
      {
        "id": "step_post_slack_general",
        "name": "Post to Slack #general",
        "type": "n8n-nodes-base.slack",
        "parameters": { "channel": "#general" },
        "connectionFrom": "step_email_general"
      }
    ],
    "connections": [
      { "from": "trigger_webhook", "to": "step_parse" },
      { "from": "step_parse", "to": "step_classify" },
      { "from": "step_classify", "to": "step_switch" },
      { "from": "step_switch", "to": "step_email_support" },
      { "from": "step_switch", "to": "step_email_ventas" },
      { "from": "step_switch", "to": "step_email_general" },
      { "from": "step_email_support", "to": "step_post_slack_support" },
      { "from": "step_email_ventas", "to": "step_post_slack_vent