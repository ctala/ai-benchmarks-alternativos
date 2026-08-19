# Qwen 3.8 2.4T (A95B) — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3.8-2.4t-a95b`
- success: True  | final: 5.95 | quality: 6.32
- latency_total: 14.316s | tokens_per_second: 143.1
- input_tokens: 167 | output_tokens: 2048
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

We need answer user in Spanish. Need generate N8N workflow JSON. Need think through n8n workflow schema. User asks: "Genera un workflow de N8N en JSON que: 1. Se active con un webhook POST 2. Extraiga el campo "email" y "message" del body 3. Use un nodo de IA (OpenAI) para clasificar el mensaje como "soporte", "ventas" o "otro" 4. Segun la clasificacion, envie el email a un canal de Slack diferente: - soporte -> #support - ventas -> #sales - otro -> #general Dame el JSON completo del workflow."

Need provide complete JSON workflow. Need likely compatible with n8n. We can create nodes: Webhook, Set/Code extract, OpenAI (maybe @n8n/n8n-nodes-langchain.openAi or n8n-nodes-base.openAi? Need careful. "nodo de IA (OpenAI)" could use n8n's OpenAI node. But classification output needs parse. Could use OpenAI Chat Model + AI Agent? Simpler use HTTP Request to OpenAI? But asks nodo de IA (OpenAI). Need JSON workflow maybe with nodes and connections. Could include credentials placeholders. Need ensure valid JSON. Need perhaps use Switch node to route based on classification. Need Slack node to post message.

Need decide exact node types and parameters. n8n workflow JSON format:
{
  "name": "...",
  "nodes": [...],
  "connections": {...},
  "settings": {"executionOrder": "v1"},
  "pinData": {}
}

Node format:
{
  "parameters": {...},
  "id": "uuid",
  "name": "Webhook",
  "type": "n8n-nodes-base.webhook",
  "typeVersion": 2,
  "position": [x,y],
  "webhookId": "..."
}

Webhook parameters: httpMethod POST, path, responseMode maybe onReceived, options. In typeVersion 2? parameters: { httpMethod: "POST", path: "clasificar-mensaje", responseMode: "onReceived", options: {} }. Need maybe webhookId.

Extract email/message: Could use Set node typeVersion 3.4? parameters: assignments with assignment collection. But to extract from body: Webhook outputs body. Set node can map from {{ $json.body.email }} etc. But if using Set node, need mode manual? Example:
{
 "parameters": {
  "mode": "manual",
  "duplicateItem": false,
  "assignments": {
    "assignments": [
      {"id": "...", "name": "email", "value": "={{ $json.body.email }}", "type": "string"},
      {"id": "...", "name": "message", "value": "={{ $json.body.message }}", "type": "string"}
    ]
  },
  "options": {}
 },
 "type": "n8n-nodes-base.set",
 "typeVersion": 3.4
}

But Set node v3 uses "assignments" object. Could also use Code node simpler:
{
 "parameters": {
   "mode": "runOnceForAllItems",
   "jsCode": "return items.map(item => ({ json: { email: item.json.body?.email, message: item.json.body?.message } }));"
 },
 "type": "n8n-nodes-base.code",
 "typeVersion": 2
}
But user says extraiga campo; Code is robust. Maybe use Set to be no-code. But JSON complete; either fine.

OpenAI node: Need classify. There are multiple node types. n8n has OpenAI node type "@n8n/n8n-nodes-langchain.openAi" with resource "chat" maybe. Or "n8n-nodes-base.openAi"? Let's recall. In n8n, OpenAI node is @n8n/n8n-nodes-langchain.openAi, typeVersion 1.8? Parameters include modelId, messages, output. But maybe easier to use LangChain: AI Agent with OpenAI Chat Model and Structured Output Parser? But workflow JSON complex.

Could use "n8n-nodes-base.httpRequest" to call OpenAI API, but user requested nodo de IA (OpenAI). Maybe acceptable if using OpenAI node.

Need output classification exactly soporte/ventas/otro. We can use OpenAI node with prompt and then parse. If using OpenAI node, output might be in json message content. Need Switch condition.

Let's investigate from memory n8n OpenAI node parameters. There is OpenAI node (LangChain) maybe:
type: "@n8n/n8n-nodes-langchain.openAi"
parameters: {
  "modelId": { "__rl": true, "mode": "list", "value": "gpt-4o-mini" },
  "resource": "text",
  "operation": "message",
  "messages": { "values": [ { "content": "..." } ] },
  "jsonOutput": false,
  "options": {}
}
Not sure.

Alternatively use "n8n-nodes-base.openAi" with typeVersion 1? I recall old OpenAI node: type "n8n-nodes-base.openAi", parameters: resource: "text", operation: "complete", prompt: "...", model: "gpt-3.5-turbo"? But maybe deprecated.

Could design using "AI Agent" node (@n8n/n8n-nodes-langchain.agent) with connected OpenAI Chat Model (@n8n/n8n-nodes-langchain.lmChatOpenAi) and maybe output parser. But then classification output string. Switch can check $json.output. Need include connections from model to agent (ai_languageModel). For simple classification, Agent prompt can return only one word. But agent might include output property.

n8n AI Agent node type: "@n8n/n8n-nodes-langchain.agent", typeVersion maybe 1.7/2? Parameters:
{
  "promptType": "define",
  "text": "=Clasifica este mensaje...",
  "options": {
     "systemMessage": "=..."
  }
}
Connections: main from previous to agent; ai_languageModel from OpenAI Chat Model to agent.
OpenAI Chat Model node: type "@n8n/n8n-nodes-langchain.lmChatOpenAi", typeVersion 1, parameters: { "model": "gpt-4o-mini", "options": {} }, credentials. It connects via ai_languageModel.
Agent output: { "output": "soporte" } maybe.

But need ensure classification clean. Could use "Structured Output Parser" to output JSON with classification field, but more complex. Could simply instruct to return only soporte, ventas, otro. Then Switch on {{$json.output}} with contains? But agent may return extra. Better use Code node after OpenAI to normalize: lower-case, trim, match. Then Switch. Workflow: Webhook -> Extract -> AI Agent -> Normalize classification -> Switch -> Slack channels.

Need Slack node: n8n-nodes-base.slack typeVersion 2.2? Parameters: resource "message", operation "post", channel: "#support", text: "...". Need credentials placeholder. In Slack node v2, channel can be { "__rl": true, "mode": "name", "value": "#support" }? Let's recall. For Slack node, parameters maybe:
{
 "resource": "message",
 "operation": "post",
 "channel": { "__rl": true, "mode": "name", "value": "#support" },
 "text": "=Nuevo mensaje...\nEmail: {{ $json.email }}\nMensaje: {{ $json.message }}\nClasificación: {{ $json.classification }}",
 "otherOptions": {}
}
But channel parameter could be "channelId" or "select". Need check. n8n Slack node typeVersion 2.2: In parameters: authentication? "resource":"message", "operation":"post", "channel":{"__rl":true,"mode":"name","value":"#support"}, "text":"...", "otherOptions":{}. There is also "select":"channel"? Hmm.

Could use HTTP Request to Slack webhook instead easier? But user says envie email a canal Slack; could use Slack node. Need complete JSON. Credentials placeholders. We can note replace credentials.

Need maybe include response to webhook? The Webhook response mode onReceived returns 200 immediately. Good.

Need consider input to AI Agent: It needs email/message from previous node. If Extract node outputs { email, message }, Agent text expression can use {{ $json.message }}. But after Agent, original data maybe not preserved? Agent output item might only contain output. Need pass email/message to Slack. In n8n, by default AI Agent node output may replace input; but there is option "returnIntermediateSteps"? Not sure. We need include email/message in Slack text. Could either use Code node to combine after Agent? The Agent node may output only { output: '...' }, losing email/message. However in n8n, nodes can access paired item? Slack node expression could use $('Extract email/message').item.json.email. Better use expressions referencing previous node: {{ $('Extraer datos').item.json.email }} etc. But if Switch after Normalize, we can include in Normalize node original fields by using $('Extraer datos