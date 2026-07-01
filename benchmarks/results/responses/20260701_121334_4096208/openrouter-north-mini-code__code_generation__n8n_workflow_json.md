# North Mini Code — code_generation/n8n_workflow_json

- model_id: `cohere/north-mini-code:free`
- success: True  | final: 7.47 | quality: 8.0
- latency_total: 69.56s | tokens_per_second: 29.4
- input_tokens: 113 | output_tokens: 2048

## Respuesta completa

The user asks for an N8N workflow JSON that meets several steps: triggered by POST webhook, extract email and message fields, use OpenAI node to classify message into categories, then route to different Slack channels based on classification.

We need to produce a valid N8N workflow JSON. The format: Node objects with id, name, type, typeVersion, position, etc. Should include webhook node, AI node (OpenAI), and multiple Slack nodes (or conditional routing using IF node). Could use IF node with conditions to route to different Slack nodes.

We need to include credentials placeholders (like "openAiApi", "slackApi") but not real keys.

The JSON should be a complete workflow that can be imported into N8N. We need to define nodes:

- Webhook node: type "n8n-nodes-base.webhook". Set HTTP Method POST, path maybe "/webhook". Use "respondToBody": true? Not necessary.

- AI node: type "n8n-nodes-base.openAi". Set model "gpt-4o-mini" (or similar). Prompt: "Classify the following message as 'support', 'sales', or 'other'." Provide input from previous node: maybe combine email and message: "Email: {{ $json.email }}, Message: {{ $json.message }}". Then extract output: maybe use "classification" field.

- IF node: type "n8n-nodes-base.if". Condition: check $json.classification equals "support", "sales", or "other". Could be multiple branches.

- Then Slack nodes: three Slack nodes each sending to different channel. Use "n8n-nodes-base.slack". Set channel as "#support", "#sales", "#general". Message content includes email and message.

Alternatively, could use a "Switch" node with conditions.

We need to ensure the JSON is valid. Provide necessary fields: id (UUID), name, type, typeVersion, position, parameters, etc.

We need to include credentials references: e.g., "openAiApi": {"id":"some credential id","name":"OpenAI API"}.

Probably easier to use placeholder references: "openAiApi": {"mode":"raw","value":"your_openai_api_key"}? But N8N expects credential ID. Could use "openAiApi": {"id":"1","name":"OpenAI API"} but not necessary for static JSON. Usually they have "credentials" property.

We can include generic placeholder: "credentials": {"openAiApi": {"id":"<OPENAI_CREDENTIAL_ID>","name":"OpenAI API"}}.

Better to give generic placeholder like "openAiApi": {"id":"<CREDENTIAL_ID>"}.

But for completeness, we can include example values like "value": "your_openai_api_key". However, N8N's node expects credential object, not raw key.

We can include "openAiApi": {"id":"1","name":"OpenAI API"}.

For Slack, need "slackApi": {"id":"<SLACK_CREDENTIAL_ID>"}.

Also need to set "channel" field for each Slack node.

We also need to set the "authentication" type for Slack, probably "OAuth Token".

Thus, each Slack node's parameters: "authentication": "credential", "nodeCredentialType": "slackApi", "credentials": {"slackApi": {"id":"<SLACK_CREDENTIAL_ID>"}}, "channel": "#support", "text": "Email: {{ $json.email }}\nMessage: {{ $json.message }}\nClassification: {{ $json.classification }}"

Similarly for other channels.

We need to ensure correct quoting and commas.

We'll produce JSON with nodes array. Each node has:

{
  "id": "nodeId",
  "name": "Webhook",
  "type": "n8n-nodes-base.webhook",
  "typeVersion": 1,
  "position": [240,300],
  "parameters": {
    "httpMethod": "POST",
    "path": "webhook",
    "responseMode": "responseNode",
    "options": {}
  }
}

But "responseMode" maybe not needed.

For AI node:

{
  "id": "nodeId",
  "name": "OpenAI Classification",
  "type": "n8n-nodes-base.openAi",
  "typeVersion": 1,
  "position": [460,300],
  "parameters": {
    "model": "gpt-4o-mini",
    "temperature": 0,
    "prompt": "Classify the following message as 'support', 'sales', or 'other'.\nEmail: {{ $json.email }}\nMessage: {{ $json.message }}",
    "options": {}
  },
  "credentials": {
    "openAiApi": {
      "id": "<OPENAI_CREDENTIAL_ID>",
      "name": "OpenAI API"
    }
  }
}

The AI node output: might output a "text" field with classification. Might need to map output to JSON path: $json.text. N8N uses auto mapping.

Then IF node:

{
  "id": "nodeId",
  "name": "If Classification",
  "type": "n8n-nodes-base.if",
  "typeVersion": 1,
  "position": [680,300],
  "parameters": {
    "conditions": {
      "options": {
        "caseSensitive": true,
        "leftValue": "",
        "typeValidation": "strict"
      },
      "conditions": [
        {
          "id": "someId",
          "leftValue": "={{ $json.classification }}",
          "rightValue": "support",
          "operator": {
            "type": "string",
            "operation": "equals"
          }
        }
      ],
      "combinator": "or"
    },
    "options": {}
  }
}

But IF node can have multiple branches. Actually IF node has two output: true and false. But we need three branches. Better to use Switch node with multiple cases.

Switch node type: "n8n-nodes-base.switch". It has "cases" array each with condition and "output": maybe "true"? Actually Switch node has "switch" field: "cases": [{"value1":"support","type":"string","operation":"equals","case":"support"}], and "options". It outputs to multiple nodes.

Thus we can use Switch node to route to three Slack nodes.

Switch node:

{
  "id": "nodeId",
  "name": "Switch Classification",
  "type": "n8n-nodes-base.switch",
  "typeVersion": 1,
  "position": [900,300],
  "parameters": {
    "switch": {
      "options": {
        "caseSensitive": true
      },
      "values": [
        {
          "id": "case1",
          "name": "support",
          "conditions": [
            {
              "id": "cond1",
              "leftValue": "={{ $json.classification }}",
              "rightValue": "support",
              "operator": {
                "type": "string",
                "operation": "equals"
              }
            }
          ]
        },
        {
          "id": "case2",
          "name": "sales",
          "conditions": [
            {
              "id": "cond2",
              "leftValue": "={{ $json.classification }}",
              "rightValue": "sales",
              "operator": {
                "type": "string",
                "operation": "equals"
              }
            }
          ]
        },
        {
          "id": "case3",
          "name": "other",
          "conditions": [
            {
              "id": "cond3",
              "leftValue": "={{ $json.classification }}",
              "rightValue": "other",
              "operator": {
                "type": "string",
                "operation": "equals"
              }
            }
          ]
        }
      ]
    },
    "options": {}
  }
}

Then three Slack nodes after switch, each connected to respective case.

Slack node example:

{
  "id": "nodeId",
  "name": "Slack Support",
  "type": "n8n-nodes-base.slack",
  "typeVersion": 2,
  "position": [1120,200],
  "parameters": {
    "authentication": "credential",
    "nodeCredentialType": "slackApi",
    "channel": "#support",
    "text": "Email: {{ $json.email }}\nMessage: {{ $json.message }}\nClassification: {{ $json.classification }}"
  },
  "credentials": {
    "slackApi": {
      "id": "<SLACK_CREDENTIAL_ID>",
      "name": "Slack API"
    }
  }
}

Similarly for #sales and #general.

Now we need to define connections. In N8N workflow JSON, there is a "connections" property mapping node IDs to next nodes. For each node, there is "connections": {"main": [[{nodeId:..., type:'main', index:0}]]}.

We need to build connections:

- Webhook node -> OpenAI node: Webhook's main output to OpenAI.

- OpenAI node -> Switch node.

- Switch node -> three Slack nodes: Each case leads to its own Slack node.

Thus connections:

{
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "OpenAI Classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Classification": {
      "main": [
        [
          {
            "node": "Switch Classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch Classification": {
      "main": [
        [
          {
            "node": "Slack Support",
            "type": "main",
            "index