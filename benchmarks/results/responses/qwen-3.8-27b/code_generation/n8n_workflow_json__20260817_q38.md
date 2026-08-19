# Qwen 3.8 27B — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 5.63 | quality: 6.32
- latency_total: 92.853s | tokens_per_second: 22.1
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

We need answer in Spanish. User asks: Generate N8N workflow JSON that: webhook POST, extract email and message, use AI OpenAI to classify message as soporte, ventas, otro; according to classification send email to different Slack channel: soporte -> #support, ventas -> #sales, otro -> #general. Complete JSON workflow.

Need produce valid n8n workflow JSON. Need think about n8n version. Could provide a workflow with Webhook, Set (extract), OpenAI (AI Agent? or OpenAI node? They say nodo de IA (OpenAI). In n8n, there is "OpenAI" node (ai_languageModelOpenAI? or openAi? Actually n8n has "OpenAI" node type: @n8n/n8n-nodes-langchain.openAi? It can complete text. There is also "AI Agent" with OpenAI Chat Model. For simple classification, can use OpenAI node with operation "textCompletion"? In current n8n, OpenAI node type is "openAi" with resources message, operation? Let's recall.

N8N nodes:
- Webhook: type "n8n-nodes-base.webhook", typeVersion 1.1? parameters: httpMethod POST, path "webhook", responseMode "onReceived" maybe.
- Set: "n8n-nodes-base.set" typeVersion 3.4? parameters: assignments? Or in Set node v3.4 use "assignments" with assignments array. Or use "Set" node to extract email/message from body: `={{ $json.body.email }}`. But if webhook returns JSON body, $json.body.email. Need handle missing? Could set email and message.
- OpenAI: Need use "OpenAI" node. Type maybe "openAi" typeVersion 1.2? Let's inspect memory.

n8n OpenAI node: In UI, node name "OpenAI", type "openAi", typeVersion 1.2? It has Resource: Message, Operation: Create? It can use model gpt-4o-mini, messages: system and user. Or there is "AI Agent" with "OpenAI Chat Model". For workflow JSON, easier to use "OpenAI" node to call API and output text. But classification needs parse. The OpenAI node outputs maybe { message: { role: assistant, content: ... } }? Need know.

Alternatively use "HTTP Request" to OpenAI, but user specifically asks use AI (OpenAI) node. We can use "AI Agent" node with OpenAI Chat Model and output text. But JSON more complex. Could use "OpenAI" node type "openAi" with operation "complete"? Let's recall exact node type and parameters.

N8N node types:
- "n8n-nodes-base.openAi"? Wait OpenAI node is in @n8n/n8n-nodes-langchain, type "openAi"? In workflows, node type often "openAi" for OpenAI? I've seen:
```
{
  "parameters": {
    "resource": "message",
    "operation": "create",
    "model": "gpt-4o-mini",
    "messages": {
      "values": [
        { "role": "system", "content": "..." },
        { "role": "user", "content": "..." }
      ]
    },
    "options": {}
  },
  "type": "openAi",
  "typeVersion": 1.2
}
```
Maybe yes. It returns item with `message.content`. Need then use Switch or IF to route. But if OpenAI returns content with extra text, need robust. We can instruct output only one word: soporte, ventas, otro. Then use Switch node with exact matches? Or use Code node to normalize and set channel. Then Slack node.

Need JSON complete. Could include nodes:
1 Webhook
2 Set (Extract fields)
3 OpenAI (classify)
4 Code (Normalize classification)
5 Switch (route)
6 Slack Support
7 Slack Sales
8 Slack General
Connections accordingly.

Need ensure JSON valid and importable. Need know node positions, id? n8n workflow JSON usually includes name, nodes, connections, settings, maybe active false. Node IDs can be UUIDs. We can generate.

Need consider Slack node type: "n8n-nodes-base.slack" typeVersion 1.2? Operation "send" or "message"? In n8n Slack node: Resource: Message, Operation: Send. Parameters: channel: "#support" or channel ID, text: "Email: ... Message: ... Class: soporte". It requires credentials. We can't include credentials. Use placeholder credentials? n8n JSON can include `"credentials": { "slackApi": { "id": "REPLACE_WITH_SLACK_CREDENTIAL_ID", "name": "Slack account" } }`. Or omit? If omit, user must select. But complete workflow maybe include placeholder. Could include `"credentials": {"slackApi": {"name": "Slack account"}}`? n8n import may complain if no id? Better to include placeholder and note replace. But user asks JSON completo; we can include placeholder credentials with id "REPLACE...". However JSON with non-numeric id may still import? n8n might ignore? It may attempt to find credential and fail? Usually credential id is number. If missing, node has no credential selected. Could include `"credentials": { "slackApi": { "id": "1", "name": "Slack account" } }` but if no credential id 1, error. Better omit credentials or include placeholder string? n8n accepts credential reference with id? It may show missing. I can include `"credentials": { "slackApi": { "id": "REPLACE_SLACK_CREDENTIAL_ID", "name": "Slack account" } }` but id should be string? In JSON, credential id can be string? In exported workflows, id is number. If string maybe invalid? Could be accepted? Hmm.

Maybe include no credentials and mention after import select Slack credential. But "JSON completo" could still be valid. For OpenAI node, also need credential. We can omit and tell select OpenAI credential. But if no credential, workflow won't run. Could include placeholder credentials for both: openAiApi and slackApi. Need decide.

Need know exact OpenAI credential type: "openAiApi" maybe. Slack: "slackApi". In node JSON:
```
"credentials": {
  "openAiApi": {
    "id": "REPLACE_OPENAI_CREDENTIAL_ID",
    "name": "OpenAI account"
  }
}
```
But id string? Could be okay? N8n may expect number. If import with string, maybe error? Could use `"id": 1`? But then may reference non-existent. Hmm.

Maybe better to provide JSON without credentials, and note: after import, add OpenAI and Slack credentials. But user asked complete JSON. We can include placeholders as strings; many examples use `"id": "REPLACE_ME"`? Not sure.

Need ensure node types and parameters correct.

Let's recall n8n Set node v3.4 parameters:
```
{
 "parameters": {
   "assignments": {
     "assignments": [
       {
         "id": "email",
         "name": "email",
         "value": "={{ $json.body.email }}",
         "type": "string"
       },
       {
         "id": "message",
         "name": "message",
         "value": "={{ $json.body.message }}",
         "type": "string"
       }
     ]
   },
   "options": {}
 },
 "type": "n8n-nodes-base.set",
 "typeVersion": 3.4
}
```
But Set node may drop other fields? It outputs only assigned fields. Good.

Webhook node: type "n8n-nodes-base.webhook" typeVersion 1.1? parameters:
```
{
  "httpMethod": "POST",
  "path": "clasificar-mensaje",
  "responseMode": "onReceived",
  "options": {}
}
```
Maybe need `webhookId`? In exported workflow, webhook node has `"webhookId": "uuid"`. Could include. If not, n8n may generate? For import, might require? Usually node has `"webhookId": "some-uuid"`. Could include.

OpenAI node: Need exact typeVersion and params. Let's recall from n8n nodes-langchain openAi:
- type: "openAi" (maybe "n8n-nodes-langchain.openAi"? In exported workflows, type often "openAi" not prefixed? For community? I think official nodes are prefixed "n8n-nodes-base." but LangChain nodes maybe "openAi"? Example:
```
{
  "parameters": {
    "model": "gpt-4o-mini",
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
    },
    "options": {}
  },
  "type": "openAi",
  "typeVersion": 1.2
}
```
But maybe there