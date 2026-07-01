# North Mini Code — code_generation/n8n_workflow_json

- model_id: `cohere/north-mini-code:free`
- success: True  | final: 8.24 | quality: 8.67
- latency_total: 34.019s | tokens_per_second: 60.2
- input_tokens: 113 | output_tokens: 2048

## Respuesta completa

The user asks for a N8N workflow JSON. That's permissible content. We need to generate a JSON representation of a workflow. This is not disallowed. We can provide it. The request is fairly straightforward: a webhook, extract fields, AI node classification, and conditional routing to Slack channels based on classification. We need to generate a JSON structure that N8N expects. We need to include node definitions with IDs, type, name, parameters, etc.

We need to ensure the JSON is correct. Let's outline the nodes:

1. Webhook node (trigger): type: "n8n-nodes-base.webhook". It should have a POST method. Probably "httpMethod": "POST". It will have "path" maybe empty or default.

2. Set node: to extract email and message fields. Could be a "Set" node: type "n8n-nodes-base.set". Set "values" array with two items: key email, value from "body.email". And key message, value from "body.message". Might need to use "expression" or "string". The Set node uses "setValue" sections.

Alternatively, could use "Function" node, but Set is simpler.

3. AI node: "n8n-nodes-base.openAi". Use "model" maybe "gpt-3.5-turbo". Prompt: classify the message as "support", "sales", or "other". Use a system message maybe.

The node likely has "prompt" field. We'll need to set a prompt that includes the message and asks to output classification.

Actually, the AI node in N8N has a "question" input and maybe "systemMessage". But typical usage: Use the "OpenAI" node with a "question" parameter that includes a prompt string. For example: "Classify the following message as 'support', 'sales', or 'other': {{ $json.message }}". Then output is a text.

But the node may have "options" like "responseFormat": "text". We'll need to set output to a field "classification".

4. Branch node: Use "IF" node or "Switch" node to route based on classification. Could use "Switch" node: type "n8n-nodes-base.switch". It has "values" field mapping classification to different paths.

But we can also use "IF" node: compare classification equals certain strings. But Switch is clearer. So Switch node with cases: support -> route to Slack node #support; sales -> #sales; default -> #general.

We need to set each case's "caseValue" equals "support", "sales", "other". But we can also use "conditions". Might need to set "conditions" for each case.

Alternatively, we could use three separate "IF" nodes each checking classification. But Switch is easier.

5. Slack node: type "n8n-nodes-base.slack". It will post a message to channel. Need to set channel ID or name. In N8N Slack node, you can set "channel" parameter using "#support" etc. However, Slack node uses "channelId" or "channelName". Probably "channelName". We'll set "channelName": "#support" etc.

Also need to set message content: "New message from {{ $json.email }}: {{ $json.message }}". Or something.

We need to ensure JSON is valid. The workflow JSON is a JSON array of nodes with fields: id, name, type, typeVersion, position, parameters, etc. We'll need to create unique IDs. Use something like "1", "2", "3", "4", "5". But better to use random UUID format.

We'll generate IDs:

- Webhook node: "webhook-trigger-1"
- Set node: "set-fields-2"
- OpenAI node: "openai-classify-3"
- Switch node: "switch-routing-4"
- Slack node: "slack-support-5" (but we need multiple Slack nodes? Actually Switch will have multiple output nodes; we can have a single Slack node after Switch, but we need to set the channel per route. In N8N, you can have a Switch node with multiple output connections, each connecting to the same Slack node but using different parameters? Usually you would have separate Slack nodes for each channel, or you could use a Set node to change channel based on classification then a single Slack node. But requirement: "Based on the classification, send the email to a different Slack channel". It could be done by having multiple Slack nodes each attached to separate Switch output, each configured with its channel. So we need three Slack nodes: one for support, one for sales, one for general. So after Switch we have three Slack nodes.

Thus nodes:

- Node1: Webhook trigger
- Node2: Set
- Node3: OpenAI
- Node4: Switch
- Node5: Slack support
- Node6: Slack sales
- Node7: Slack general

Switch will have three output links: support, sales, other, each connecting to respective Slack node.

Thus we need to generate JSON for all nodes. We'll need to include connections. In N8N workflow JSON, connections are defined in an "connections" property mapping node IDs to node IDs.

We need to ensure the JSON is syntactically correct.

We'll produce a JSON string.

Let's draft each node's structure.

General node format (as per N8N docs):

{
  "nodes": [
    {
      "parameters": {...},
      "id": "node-id",
      "name": "Node Name",
      "type": "node-type",
      "typeVersion": 1,
      "position": [x, y],
      "webhookId": "...", // maybe not needed
      "settings": {...},
      "continueOnFail": false,
      "onError": "stopWorkflow",
      "retryOnFail": false,
      "alwaysOutputData": false,
      "executeOnce": false,
      "lensId": "...",
      "notes": "...",
      "notesInFlow": false
    }, ...
  ],
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
    },
    ...
  },
  "name": "Workflow Name",
  "tags": [],
  "triggerCount": 1,
  "updatedAt": "...",
  "createdAt": "...",
  "versionId": "...",
  "isActive": true,
  "settings": {...},
  "staticData": null,
  "meta": {...}
}

We can produce a minimal JSON with essential fields.

Let's define positions: maybe start at top left and go down.

- Webhook: position [0,0]
- Set: position [0,100]
- OpenAI: position [0,200]
- Switch: position [0,300]
- Slack support: position [300,200] (connected from Switch support)
- Slack sales: position [600,200] (connected from Switch sales)
- Slack general: position [900,200] (connected from Switch other)

But we need to define connections from Switch to each Slack node.

Switch node connections: It has multiple outputs, each goes to a Slack node.

The connections structure in N8N uses "connections": { "NodeId": { "main": [ [ {"node": "OtherNodeId", "type": "main", "index": 0} ] ] } }

For Switch node, each output is represented by a separate array? Actually for Switch node, there are multiple outputs: each output is a branch, and you define connections accordingly.

We might need to have separate entries for each output, like:

"connections": {
  "webhook-trigger-1": {
    "main": [
      [
        {"node": "set-fields-2", "type": "main", "index": 0}
      ]
    ]
  },
  "set-fields-2": {
    "main": [
      [
        {"node": "openai-classify-3", "type": "main", "index": 0}
      ]
    ]
  },
  "openai-classify-3": {
    "main": [
      [
        {"node": "switch-routing-4", "type": "main", "index": 0}
      ]
    ]
  },
  "switch-routing-4": {
    "main": [
      [
        {"node": "slack-support-5", "type": "main", "index": 0}
      ],
      [
        {"node": "slack-sales-6", "type": "main", "index": 0}
      ],
      [
        {"node": "slack-general-7", "type": "main", "index": 0}
      ]
    ]
  },
  "slack-support-5": {
    "main": []
  },
  "slack-sales-6": {
    "main": []
  },
  "slack-general-7": {
    "main": []
  }
}

But Switch node likely has multiple output ports: "support", "sales", "other". However, in N8N, Switch node has output ports named "default" and each case. But connections might be defined using "main" array for each output. It may be okay to connect all three Slack nodes to "main" of Switch.

Alternatively, we could use "IF" nodes for each classification, but Switch is fine.

We need to set Switch node parameters: It should compare the output of OpenAI classification to strings. The Switch node parameters include "conditions": [{ "leftValue": "", "rightValue": "", "operator": { "type": "string", "operation": "equals" }, "cases": [ { "value": "support", "conditions": [ { "leftValue": "{{ $json.classification }}",