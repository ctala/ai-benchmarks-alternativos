# GPT-OSS 20B — code_generation/n8n_workflow_json

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 7.36 | quality: 7.92
- latency_total: 113.726s | tokens_per_second: 18.0
- input_tokens: 179 | output_tokens: 2048
- judge_score: 3.8 | justificación: 

## Respuesta completa

We need to generate a JSON for an n8n workflow that includes:

- Trigger node webhook (HTTP Request Trigger). Method POST.

- Node to extract body fields email and message. In n8n, you can use Set node or Function node to extract. Set node can pick data from previous node's output.

- Node for AI classification using OpenAI. In n8n, there is an "OpenAI" node. We can set the prompt to classify message. Use input "message". The node will return a text. We need to parse classification.

- Then a Switch node to route based on classification.

- For each branch, an HTTP Request (or Slack node) to send message to Slack channel. n8n has a Slack node. We'll use Slack node set to send message to channel. We need to specify channel ID or name (#support, #sales, #general). Use Slack node for each branch.

- Need to set up credentials: Webhook, OpenAI, Slack. They can be referenced by names.

- The JSON structure: root includes "name", "nodes": [...], "connections": {...}. Provide full JSON.

- Ensure correct node types: "n8n-nodes-base.httpWebhook", "n8n-nodes-base.set", "n8n-nodes-base.openAi", "n8n-nodes-base.switch", "n8n-nodes-base.slack". Provide fields.

- Provide "parameters" for each node.

- The openAI node: need to set "model" maybe "gpt-3.5-turbo" or "gpt-4". Use "prompt" as "Classify the following message as support, sales, or other: {message}". Then output is text. Use "response" field: "choices[0].message.content".

- In the Switch node: conditions on "json.response" or "json". Use "json.response" to check string. Might need to set condition to equal 'support', 'sales', 'other'.

- In Slack node: "sendMessage" type, Channel: "#support" etc. Use "Message" field: maybe include email and message. Use "text" property.

- Provide credentials names: "Webhook-1", "OpenAI-1", "Slack-1".

- For Set node: can create new fields: email, message from previous. Or use function to assign. But Set node works.

- Ensure correct field names: in the HTTP Webhook node, the incoming data is in "body" of request. In n8n, the data is in "body" object. So Set node can map: "email": "{{$json.body.email}}" and "message": "{{$json.body.message}}".

- OpenAI node: we can use "prompt" field: "Classify the following message as 'support', 'sales', or 'other': {{$json.message}}". Then "responseFormat" maybe "text".

- Slack node: There is "Send message" node: fields: "channel", "text". Provide channel string.

- Provide the "connections" mapping: Webhook -> Set -> OpenAI -> Switch. Then Switch -> Slack nodes.

- Provide "executeOnce": false etc.

- Provide "id" numeric or string? In n8n JSON, each node has "id" (string). But can be omitted? Typically include id. But we can let n8n auto generate. Provide integer IDs.

- Provide "typeVersion": 1.

- Provide "position": [x,y]. Use arbitrary coordinates.

We need to output the full JSON.

Let's construct.

Nodes:

1. HTTP Request Trigger node: name "Webhook Trigger". type "n8n-nodes-base.httpWebhook". parameters: "httpMethod": "POST", "path": "webhook". "responseMode": "onReceived". "responseString": "Received". "responseCode": 200. Provide credentials: "Webhook-1".

2. Set node: name "Extract Fields". type "n8n-nodes-base.set". parameters: "values": [{"name":"email","value":"{{$json.body.email}}"},{"name":"message","value":"{{$json.body.message}}"}]. "options": {}.

3. OpenAI node: name "Classify Message". type "n8n-nodes-base.openAi". "parameters": "model":"gpt-3.5-turbo", "temperature":0.0, "prompt":"Classify the following message as 'support', 'sales', or 'other': {{$json.message}}", "responseFormat":"text". Also "inputVariables": maybe not needed. Credentials: "OpenAI-1".

4. Switch node: name "Route by Classification". type "n8n-nodes-base.switch". parameters: "conditions": [{"json":"{{$json.response}}","equals":"support"},{"json":"{{$json.response}}","equals":"sales"},{"json":"{{$json.response}}","equals":"other"}]. But I think standard n8n Switch node uses "conditions" as mapping: key->value array. Actually in n8n, the Switch node uses "conditions" field with "json" key and then "value" array. Let's check typical structure: In n8n docs: "conditions": {"json": [{"value": "support"},{"value": "sales"},{"value":"other"}]}. But we need to map each condition to a next node. Actually n8n Switch node uses "conditions" object: keys are the condition names and values are arrays of objects with "value" and "matches". But I'm not 100% sure. Let's recall: In Switch node, you can specify "conditions" like: "conditions": {"json": [{"value":"support"},{"value":"sales"},{"value":"other"}]} and then mapping to next nodes. But the mapping is defined in "name" of next node branch. The "connections" mapping uses the condition index. Let's check typical example: In n8n, the Switch node has following structure for conditions: "conditions": {"json": [{"value":"support"},{"value":"sales"},{"value":"other"}]}. Then mapping to next nodes: In connections, you specify "Switch": {"main":[[{"node":"Support Slack","type":"n8n-nodes-base.slack","index":0}]] etc. Actually I've seen that Switch node uses "conditions" like:

```
"conditions": {
  "json": [
    {
      "value": "support"
    },
    {
      "value": "sales"
    },
    {
      "value": "other"
    }
  ]
}
```

Then the connections mapping: "Switch" -> "main" -> array of arrays of node connections. Each array corresponds to a condition. So index 0 for support, index 1 for sales, index 2 for other.

Thus we need to create connections accordingly.

5. Slack nodes: "Support Slack", "Sales Slack", "Other Slack". Each type "n8n-nodes-base.slack". parameters: "operation": "sendMessage", "channel":"support" etc. For channel names, we can use "#support". But Slack node expects channel ID or name. Use "#support".

Parameters: For Slack node: "operation":"sendMessage", "channel":"support", "text":"Hello, support! Email: {{$json.email}} Message: {{$json.message}}" etc. But we need to reference email and message from previous. Use expression: "{{$json.email}}".

- For Sales Slack: channel "#sales", text accordingly.

- For Other Slack: channel "#general".

But note: The Slack node might require "channel" as channel ID, not name. But for simplicity, we can use "#support" etc.

- Credentials: "Slack-1".

Now, the "connections" section:

HTTP Webhook -> Set: { "main":[[{"node":"Extract Fields","type":"n8n-nodes-base.set","index":0}]] }

Set -> OpenAI: same.

OpenAI -> Switch: same.

Switch -> Slack nodes: For each index: 0 -> Support Slack, 1 -> Sales Slack, 2 -> Other Slack.

So connections:

"Webhook Trigger": { "main":[[{"node":"Extract Fields","type":"n8n-nodes-base.set","index":0}]] }

"Extract Fields": {"main":[[{"node":"Classify Message","type":"n8n-nodes-base.openAi","index":0}]]}

"Classify Message": {"main":[[{"node":"Route by Classification","type":"n8n-nodes-base.switch","index":0}]]}

"Route by Classification": { "main":[[{"node":"Support Slack","type":"n8n-nodes-base.slack","index":0}],[{"node":"Sales Slack","type":"n8n-nodes-base.slack","index":0}],[{"node":"Other Slack","type":"n8n-nodes-base.slack","index":0}]] }

But we need to ensure mapping of index: first array is condition 0. n8n expects connections array of arrays matching conditions. So we need to provide three arrays inside "main" array: each inner array contains connection. So structure:

"Route by Classification": {
  "main": [
    [
      {
        "node": "Support Slack",
        "type": "n8n-nodes-base.slack",
        "index": 0
      }
    ],
    [
      {
        "node": "Sales Slack",
        "type": "n8n-nodes-base.slack",
        "index": 0
      }
    ],
    [
      {
        "node": "Other Slack",
        "type": "n8n-nodes-base.slack",
        "index": 0
      }
    ]
  ]
}

Yes.

Now each node's "parameters" must be correctly formatted