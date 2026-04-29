# Qwen 3-Next 80B Thinking (NIM) — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3-next-80b-a3b-thinking`
- success: True  | final: 6.48 | quality: 7.08
- latency_total: 21.167s | tokens_per_second: 96.8
- input_tokens: 120 | output_tokens: 2048
- judge_score: 3.2 | justificación: 

## Respuesta completa

Okay, I need to create an N8N workflow in JSON that does the following: triggers via a POST webhook, extracts email and message from the body, uses OpenAI to classify the message into support, sales, or other, then sends to different Slack channels based on that. Let me think step by step.

First, the workflow needs a Webhook node to start. The trigger should be a POST request. So the Webhook node will have a path, maybe something like /webhook. But in the JSON, I need to set up the webhook node correctly. The Webhook node in N8N has a "Webhook Path" field. Let's say the path is "support-webhook" or something, but maybe just "webhook" for simplicity. But actually, the exact path might not matter as long as it's set properly. The important part is that it's a POST method.

Next, the Webhook node will receive the body. Then, I need to extract the email and message fields. So after the Webhook node, there should be a node that processes the incoming data. Maybe a Set node to extract those fields? Or perhaps the Webhook node already outputs the body as data, and then I can use a Function node or a Set node to pick out the email and message.

Wait, the Webhook node in N8N by default has a "Response Data" option, but when using the Webhook node as a trigger, it will receive the data in the body. So the first node is the Webhook node. Let's check how N8N handles this. When you create a Webhook node, you can set the method to POST, and then the incoming data is available in the item's json. So the Webhook node's output will have the body as part of the json properties.

So for example, if the POST body is {"email": "test@example.com", "message": "Hello"}, then the Webhook node's output will have that in the json. So then, next step is to extract those fields. Maybe a Set node to take the email and message and put them into separate fields? Or perhaps the OpenAI node can access them directly from the incoming data.

Wait, the OpenAI node will need to take the message field. So maybe after the Webhook node, we pass the message to OpenAI. But first, perhaps the Webhook node already has the data. Let's see: the Webhook node, when triggered, will have the request body in the item's json. So the Webhook node's output will have the entire body. So for example, if the POST has a JSON body with email and message, then the Webhook node's output will have those as properties.

So maybe the next step is a Function node or a Set node to extract those fields. But maybe the OpenAI node can directly use the message field from the incoming data. Let's check the OpenAI node configuration. The OpenAI node in N8N has a "Prompt" field where you can input a template. So you can reference the message using {{ $json.message }} or something like that. So perhaps you don't need an extra node to extract, just reference it in the prompt.

But to be safe, maybe a Set node to explicitly set those fields, but maybe it's not necessary. Let's see.

So the workflow steps would be:

1. Webhook node (POST) to receive the data.

2. OpenAI node to process the message. The prompt would be something like: "Classify the following message as 'soporte', 'ventas', or 'otro': {{ $json.message }}". Then, the OpenAI node's output would have the classification.

Wait, but OpenAI's response might be more than just the category. So the prompt should instruct it to respond only with the category, maybe. For example: "Classify the message as 'soporte', 'ventas', or 'otro'. Only output the category name." So the response would be just one of those words.

Then, after the OpenAI node, we need to route based on the classification. So maybe a Switch node that checks the OpenAI's response. But N8N has a Switch node that can route based on conditions. Alternatively, use a Function node to set the channel based on the classification.

Wait, but the Slack node will need to know which channel to send to. So after classifying, we need to set a channel variable. For example, if the classification is "soporte", then channel is #support; "ventas" -> #sales; else #general.

So after the OpenAI node, perhaps a Function node that takes the classification result and sets a new field called 'channel' based on that. Then, the Slack node uses that channel field.

Alternatively, the Switch node can have multiple branches. For example, the Switch node checks the OpenAI response. If it's "soporte", route to one branch; "ventas" to another; else to a third. Each branch then sends to the respective Slack channel.

But maybe the Switch node is better for routing. Let's see.

So steps:

Webhook -> OpenAI (classify) -> Switch (based on classification) -> Slack nodes for each branch.

But N8N's Switch node can have multiple conditions. So the Switch node would check the value of the classification field. For example:

If the value is "soporte", go to output 1; "ventas" to output 2; else to output 3. Then each output connects to a Slack node.

But the Slack nodes would need to be configured with the respective channel.

Alternatively, use a single Slack node that takes the channel from a variable. So after the OpenAI node, a Function node that sets the channel based on classification, then send to Slack using that channel.

Let me think. Let's outline each node.

First, Webhook node:

- Type: Webhook

- Settings:

  - Method: POST

  - Path: /webhook (for example)

  - Response Mode: "On Received" (but maybe "Wait for Webhook" but for this case, probably "On Received" since we want to process immediately and return a response. Wait, for a webhook trigger, the response mode is usually set to "Send response from workflow" but in this case, maybe "On Received" would send the response immediately. But perhaps the Webhook node can be configured to return a response once processed. But for simplicity, maybe the Webhook node just triggers the workflow and the response is handled later. However, the default response for a webhook in N8N is to return a 200 OK once the workflow starts. So perhaps the Webhook node is fine as is.

Then, the Webhook node's output will have the body data.

Next, OpenAI node. Let's say the OpenAI node is configured with the API key, model (like gpt-3.5-turbo), and the prompt.

The prompt would be something like: "Classify the following message as 'soporte', 'ventas', or 'otro'. Only output the category name. Message: {{ $json.message }}"

So the prompt would reference the message field from the incoming data.

Then, the OpenAI node's output will have the response. Let's say the response is stored in a field called 'openai_response' or similar.

Then, we need to process that response to determine the channel.

So a Function node that takes the openai_response and sets a new field, say 'channel', based on the value.

For example, in the Function node:

if (item.json.openai_response === 'soporte') {
  item.json.channel = '#support';
} else if (item.json.openai_response === 'ventas') {
  item.json.channel = '#sales';
} else {
  item.json.channel = '#general';
}
return item;

But in N8N's Function node, you need to write JavaScript code. So the code would loop over items and set the channel.

Wait, in N8N, the Function node processes each item. So the code would be:

const items = $input.all();

const newItems = items.map(item => {
  const classification = item.json.openai_response;
  let channel = '#general';
  if (classification === 'soporte') {
    channel = '#support';
  } else if (classification === 'ventas') {
    channel = '#sales';
  }
  return {
    ...item,
    json: {
      ...item.json,
      channel
    }
  };
});

return newItems;

But maybe simpler to just process one item. Since the workflow is linear, maybe only one item is processed at a time.

Alternatively, the Function node code could be:

return [{
  json: {
    channel: $json.openai_response === 'soporte' ? '#support' : $json.openai_response === 'ventas' ? '#sales' : '#general'
  }
}];

But need to check how N8N's Function node works. The Function node takes the input items and returns new items. So for each item in the input, we process it.

So for example, if the input item has a field 'openai_response', then in the Function node:

return [{
  json: {
    channel: $json.openai_response === 'soporte' ? '#support' : $json.openai_response === 'ventas' ? '#sales' : '#general'
  }
}];

Wait, but the Function node in N8N uses $json to access the current item's data.

So code inside Function node:

const response = $json.openai_response;

let channel = '#general';
if (response === 'soporte') {
  channel = '#support';
} else if (response === 'ventas') {
  channel = '#sales';
}

return [{
  json: {
    channel: channel
  }
}