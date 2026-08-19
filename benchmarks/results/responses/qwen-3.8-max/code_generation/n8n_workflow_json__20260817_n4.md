# Qwen 3.8 Max — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3.8-max`
- success: True  | final: 5.6 | quality: 6.24
- latency_total: 48.288s | tokens_per_second: 42.5
- input_tokens: 163 | output_tokens: 2050
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

We need answer in Spanish likely. User asks: Generate N8N workflow JSON complete. Need provide JSON. Need think about n8n workflow schema. Need ensure valid JSON? They ask JSON completo del workflow. We can output code block with JSON. Need include nodes and connections. Need webhook POST, extract email and message, OpenAI classify, switch, Slack nodes. Need maybe use n8n nodes: n8n-nodes-base.webhook, n8n-nodes-base.set or code? OpenAI node maybe @n8n/n8n-nodes-langchain.openAi? Or n8n-nodes-base.openAi? Need robust. Since user wants AI node OpenAI. We can use n8n-nodes-base.openAi? Let's recall n8n node types.

n8n workflow JSON has name, nodes: [{parameters, id, name, type, typeVersion, position, credentials?}], connections: {NodeName: {main: [[{node:..., type:'main', index:0}]]}}.

Webhook node: type: "n8n-nodes-base.webhook", typeVersion: 2? parameters: {httpMethod: "POST", path: "clasificar-mensaje", options: {}}. It outputs body. In newer webhook maybe responseMode etc.

Extract email/message: can use Set node (n8n-nodes-base.set) typeVersion 3.4? parameters: mode: 'manual', duplicateItem: false, assignments: {assignments: [{id:..., name:'email', value:'={{ $json.body.email }}', type:'string'}, ...]}, options: {}. But maybe simpler use Code node? But user says extraiga campo. Set node fine. Need ensure expression references body: Webhook node outputs request body as $json.body? In n8n webhook node: output includes headers, params, query, body. Yes.

OpenAI classification: Need a node. Options:
- OpenAI node: type: "@n8n/n8n-nodes-langchain.openAi" maybe typeVersion 1.8? parameters: modelId? resource? Let's recall. There is n8n-nodes-base.openAi? Old OpenAI node parameters: resource: "text", operation: "message"? Actually old node: n8n-nodes-base.openAi, typeVersion 1, parameters: resource: 'text', operation: 'message', model: 'gpt-4o-mini', messages: { values: [...] }? Hmm.

Modern n8n has @n8n/n8n-nodes-langchain.openAi (OpenAI) with parameters: modelId: { __rl: true, mode: 'list', value: 'gpt-4o-mini' }, messages: { values: [{ content: '...' }] }, outputType: 'text'? Maybe. There is also LangChain Chat Model / Agent. But simpler maybe use "n8n-nodes-base.openAi" legacy. Need JSON that can be imported? Hard to guarantee. Could use HTTP Request node to OpenAI API? But user asked Use un nodo de IA (OpenAI). Could use OpenAI node. Need likely acceptable if approximate.

Need classification then switch. Switch node: type: n8n-nodes-base.switch, typeVersion 3.2? parameters: conditions: {options: {caseSensitive: true, leftValue: '', typeValidation: 'strict'}, conditions: [{leftValue: '={{ $json.message.content }}', rightValue: 'soporte', operator: {type:'string', operation:'equals'}}, ...], combinator:'and'}? Actually Switch v3 uses rules? Let's recall.

n8n Switch node versions:
- typeVersion 1: parameters: {dataType: 'string', value1: '={{ $json.classification }}', rules: {rules: [{value2: 'soporte', output: 0}, ...]}, fallbackOutput: 2?}.
- typeVersion 3: parameters: {conditions: {...}}. Maybe easier to use older Switch typeVersion 1? But n8n may still import? Yes likely.

Maybe use IF nodes? But switch better. Need parse classification from OpenAI output. Need ensure output is only one word. Could use Set node after OpenAI to extract classification? The OpenAI output format may be object. Need know. If using legacy OpenAI text message, output maybe { choices: [{ message: { content: "soporte" } }] }? Or maybe output as text? Need robust. Could add Code node to normalize classification: const text = ($json.message?.content ?? $json.choices?.[0]?.message?.content ?? $json.text ?? $json.output ?? '').toString().trim().toLowerCase(); return [{json: {email: $('Extraer datos').item.json.email, message: $('Extraer datos').item.json.message, classification: ...}}]; Then switch on classification. That makes workflow robust to node output variations. But user asked complete JSON. We can include Code node. Need maybe use Function? Code node type: n8n-nodes-base.code, typeVersion 2, parameters: jsCode: "...". This can reference previous nodes. Need ensure expression in Switch: {{ $json.classification }}.

Slack nodes: type: n8n-nodes-base.slack, typeVersion 2.2? parameters: resource: 'message', operation: 'post', channel: {__rl: true, mode: 'name', value: 'support'}, text: '={{ $json.message }}', otherOptions: {}. Or select channel. Need include email maybe. Slack node authentication credentials not included? Could include placeholder credentials? Usually workflow JSON can omit credentials or include placeholder. We can include credentials: {slackApi: {id: 'REEMPLAZA_ID', name: 'Slack account'}} but maybe not necessary. If included may fail import if nonexistent? Usually credentials can be omitted. But nodes may need credentials. We can include placeholder? In n8n JSON, credentials property optional. If present with invalid ID, still import? It may show missing. Better omit credentials or include "credentials": {"slackApi": {"id": "PASTE_SLACK_CREDENTIAL_ID", "name": "Slack"}}? Could be okay. For OpenAI too. Maybe omit to let user attach.

Need ensure JSON valid. Could include ids as UUID? Use simple unique IDs. Need connections.

Let's design workflow:
Name: "Clasificar mensajes por email y enviar a Slack"
Nodes:
1. Webhook (type n8n-nodes-base.webhook, typeVersion 2) parameters: {httpMethod: "POST", path: "clasificar-mensaje", responseMode: "onReceived", options: {}} maybe responseMode? If not set default? To avoid hanging, set responseMode: "onReceived" or "lastNode"? For simple receive, responseMode: "onReceived" returns 200 immediately. But if want process? It can still execute. Parameters: {httpMethod: 'POST', path: 'clasificar-mensaje', options: {}}. Maybe include responseMode: 'onReceived'. In Webhook v2, parameters include responseMode? I think yes: responseMode: 'onReceived', options: {}. Use path.

2. Extraer email/message (Set node). type: n8n-nodes-base.set, typeVersion: 3.4, parameters: {mode: 'manual', assignments: {assignments: [{id: 'email', name: 'email', value: '={{ $json.body.email }}', type: 'string'}, {id:'message', name:'message', value:'={{ $json.body.message }}', type:'string'}]}, options: {}}. Need id fields maybe random. Set v3 expects assignments array objects with id, name, value, type. Could include. Maybe include "includeOtherFields": false? options.

But if body is JSON? Webhook outputs body. Good.

3. Clasificar con OpenAI. Need choose node. Let's decide. We can use @n8n/n8n-nodes-langchain.openAi? Need parameters exact? Let's search memory.

n8n OpenAI node (LangChain) type: "@n8n/n8n-nodes-langchain.openAi". parameters example:
{
  "modelId": {"__rl": true, "mode": "list", "value": "gpt-4o-mini"},
  "messages": {
    "values": [
      {
        "content": "=Clasifica el siguiente mensaje como uno de estos valores exactos: soporte, ventas, otro. Responde solo con una palabra...\nEmail: {{ $json.email }}\nMensaje: {{ $json.message }}"
      }
    ]
  },
  "outputType": "text"
}
Maybe also "jsonOutput": false. typeVersion 1.8. But not sure if this node outputs text in $json.text? Maybe. To be safe, Code node normalizes.

Alternatively use old OpenAI node: type: "n8n-nodes-base.openAi", typeVersion: 1, parameters: {resource: "text", operation: "message", model: "gpt-4o-mini", messages: {values: [{content: "..."}]}, options: {temperature: 0}}. Output? Maybe { choices: [ { message: { content } } ] } or simplified? Hmm.

Maybe use HTTP Request node to OpenAI is more deterministic but not "nodo de IA (OpenAI)". Could still call OpenAI API but they asked node. Better use OpenAI node.

Could use "AI Agent" with Chat OpenAI model, but