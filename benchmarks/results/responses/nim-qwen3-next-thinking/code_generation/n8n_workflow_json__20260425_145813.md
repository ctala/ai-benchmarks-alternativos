# Qwen 3-Next 80B Thinking (NIM) — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3-next-80b-a3b-thinking`
- success: True  | final: 6.28 | quality: 6.24
- latency_total: 17.629s | tokens_per_second: 116.2
- input_tokens: 120 | output_tokens: 2048
- judge_score: 2.6 | justificación: 

## Respuesta completa

Okay, I need to create an N8N workflow in JSON that does the following: triggers on a POST webhook, extracts email and message from the body, uses OpenAI to classify the message into support, sales, or other, then sends the email to the corresponding Slack channel. Let me break this down step by step.

First, the workflow should start with a Webhook node. I remember that in N8N, the Webhook node can be set up to listen for POST requests. The node needs to have the path set to something like "/webhook" or whatever the user specifies, but maybe the default is okay. The main thing is to capture the body data.

Next, I need to extract the "email" and "message" fields from the incoming request body. So after the Webhook node, there should be a Set node or maybe just using the JSON data directly. Wait, in N8N, the Webhook node outputs the request body as part of the data. So the first node after the webhook would probably be a function node or maybe just use the Set node to extract those fields. Alternatively, maybe the Webhook node already has the data, and we can use a Set node to pick out the specific fields. But maybe the Webhook node's output already has the body, so the next step is to use a Set node to structure the data.

Wait, the Webhook node will receive the POST request, and the body is in the JSON. So for example, if the incoming data is {"email": "test@example.com", "message": "Hello"}, then the Webhook node's output will have that. So maybe we don't need a Set node for extraction; the next step is to pass that to the OpenAI node.

But OpenAI node in N8N probably needs the message as input. So perhaps after the Webhook node, we can have a node that takes the body and sends it to OpenAI for classification.

But first, the Webhook node: in N8N, when you create a Webhook node, you have to configure it. The type is "Webhook", and you set the path. Let's say the path is "/classify", but maybe the exact path isn't critical as long as it's set. The important part is that the node outputs the incoming request's body.

Then, the next step is to send the message to OpenAI for classification. So there's an OpenAI node that takes the message and processes it. The OpenAI node would need to be configured with the API key, and the prompt for classification.

For the classification prompt, I need to tell OpenAI to classify the message as support, sales, or other. So the prompt might be something like: "Classify the following message into one of the categories: 'soporte', 'ventas', or 'otro'. Message: [message]. Return only the category name."

But OpenAI's response might be in JSON or text. The node might need to extract the category from the response.

Wait, the OpenAI node in N8N: when you set it up, you can specify the prompt and the model. Then the output will have the generated text. So for example, the prompt would be:

"Classify the following message as 'soporte', 'ventas', or 'otro': {{ $json.message }}"

Then the response from OpenAI would be one of those words. So we need to parse that response.

After getting the classification, we need to route to different Slack channels based on the category. So the workflow would have a Conditional node (like a Switch node in N8N) that checks the category and routes to different Slack nodes.

Wait, N8N has a Switch node that can route based on conditions. So after the OpenAI node, a Switch node would check the value of the category field, and then send to different Slack channels.

But first, how to structure the data. Let's outline the steps:

1. Webhook node: receives POST request with body containing email and message.

2. Maybe a Set node to extract email and message into separate fields, but maybe the Webhook node already has those. So the Webhook node's output will have the body as part of the data. Let's say the body is in $json.body, but actually, in N8N, when you receive a webhook, the body is part of the JSON data. For example, if the incoming request has a JSON body, the Webhook node will have the data in $json, so $json.email and $json.message.

Wait, when you set up a Webhook node in N8N, if the request is a JSON POST, then the node will have the body as part of the JSON data. So for example, if the incoming request is {"email": "test@example.com", "message": "Hello"}, then in the Webhook node, the output will have $json.email and $json.message.

So maybe the next step is to pass this to the OpenAI node. The OpenAI node would take the message field as input. So in the OpenAI node's prompt, we can use {{ $json.message }}.

But let's check: the OpenAI node's configuration would have a prompt like "Classify this message as 'soporte', 'ventas', or 'otro': {{ $json.message }}" and then the response would be the category. Then the OpenAI node's output would have the generated text in, say, $json.response.

Then, we need to extract the category from the response. For example, if the response is "soporte", then the category is "soporte".

Then, using a Switch node to check the category. The Switch node would have conditions for each case. For example, if category is "soporte", route to Slack node for #support; if "ventas", route to #sales; else to #general.

Each Slack node would need to be configured with the channel and the message. The message to send to Slack should include the email and the original message. So for example, the Slack node would have a message like "Email: {{ $json.email }}, Message: {{ $json.message }}".

Wait, but after the OpenAI node, the data might have the category in a field, say $json.category. So after the OpenAI node, maybe we need a Set node to assign the category to a new field, or maybe the OpenAI node outputs the response in a specific way.

Alternatively, the OpenAI node's output might be a string, and then we can use a Set node to put that string into a category field.

Let me think: when the OpenAI node is configured, in the "Response" section, you can choose how the output is structured. For example, you can have it return the response as a JSON object or a string. If it's a string, then maybe the response is just "soporte", so then we can take that string and assign it to a field.

So steps:

- Webhook node: receives POST, outputs body with email and message.

- OpenAI node: uses the message to get classification. The prompt is set to return only the category name.

- Then, the OpenAI node's output will have the response (e.g., "soporte") in, say, $json.response.

- Then, a Set node to set a new field, like category = $json.response.

- Then, a Switch node to check the category field and route to different Slack nodes.

Alternatively, maybe the OpenAI node's output is already in a way that we can use directly. Let's check N8N's OpenAI node documentation.

In N8N, the OpenAI node's response is stored in the "Response" field. For example, if the prompt is set correctly, the response text is in $json.response. So after the OpenAI node, we can use a Set node to take $json.response and put it into a new field called category.

Then, the Switch node checks the category field.

Once the category is determined, each path would go to a Slack node. The Slack node would send a message to the respective channel. The Slack node needs to be configured with the channel name and the message content.

For example, for the support channel, the Slack node's message would be something like:

"New support request from {{ $json.email }}: {{ $json.message }}"

But wait, the Slack node needs to have the channel set to #support, and the text would include the email and message.

So the Slack node configuration would have:

Channel: #support

Text: "Email: {{ $json.email }}, Message: {{ $json.message }}"

But in the workflow, after the Switch node routes to the specific Slack node, each Slack node would have the correct channel and message.

Now, putting all this into the N8N JSON workflow.

Let's start building the JSON.

First, the Webhook node. In N8N, the Webhook node's type is "n8n-nodes-base.webhook".

The parameters would include the path. Let's say the path is "classify", so the webhook URL would be https://your-n8n-url/webhook/classify.

Then, the next node is the OpenAI node. The OpenAI node type is "n8n-nodes-base.openAi".

The parameters for the OpenAI node would include the API key (but in the JSON, we can't have the actual key, so probably leave it as a placeholder), model, prompt, etc.

The prompt would be: "Classify the following message into one of the categories: 'soporte', 'ventas', or 'otro'. Message: {{ $json.message }}. Return only the category name."

Wait, but in N8N, the prompt can use the data from the previous node. So if the Webhook node passes the message as $json.message, then in