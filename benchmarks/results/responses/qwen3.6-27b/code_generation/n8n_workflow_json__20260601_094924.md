# Qwen 3.6 27B base (OpenRouter FP8) — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3.6-27b`
- success: True  | final: 6.76 | quality: 8.12
- latency_total: 44.913s | tokens_per_second: 45.6
- input_tokens: 125 | output_tokens: 2048
- judge_score: 3.8 | justificación: 

## Respuesta completa

Here's a thinking process:

1.  **Understand User Request:**
   - **Tool:** n8n (workflow automation tool)
   - **Format:** JSON
   - **Trigger:** Webhook POST
   - **Input Extraction:** Extract `email` and `message` from the webhook body
   - **AI Classification:** Use OpenAI node to classify the `message` into one of three categories: "soporte", "ventas", or "otro"
   - **Routing/Action:** Based on classification, send the `email` to a specific Slack channel:
     - "soporte" -> `#support`
     - "ventas" -> `#sales`
     - "otro" -> `#general`
   - **Output:** Complete n8n workflow JSON

2.  **Deconstruct n8n Workflow Requirements:**
   - n8n workflows are JSON objects with specific structure: `name`, `nodes`, `connections`, `settings`, etc.
   - Need nodes:
     - Webhook (trigger)
     - Set/Code (optional, but usually Webhook extracts automatically, but I'll make sure fields are accessible)
     - OpenAI (AI agent/text generation)
     - Switch/IF (routing based on classification)
     - Slack (send message)
   - I'll use a `Switch` node for routing based on the AI's output.
   - I'll use a `Code` node or rely on Webhook's automatic parsing. Webhook in n8n automatically parses JSON body into `json` object. So `{{ $json.body.email }}` or just `{{ $json.email }}` depending on n8n version. I'll use standard `{{ $json.email }}` and `{{ $json.message }}`.
   - OpenAI node needs configuration: model, prompt, output parsing. I'll set it up to return just the category string or a JSON object. For simplicity, I'll make it return a plain string and use a `Switch` node that matches exactly. Alternatively, I can use a `Code` node to clean the output, but n8n's OpenAI node can output text. I'll configure it to output a single word.
   - Slack node needs credentials (I'll leave placeholders or use generic config), channel selection, and message formatting.

3.  **Design the Workflow Structure (Mental Draft):**
   ```
   [Webhook] -> [OpenAI] -> [Switch] -> [Slack #support]
                                       -> [Slack #sales]
                                       -> [Slack #general]
   ```
   Actually, n8n's `Switch` node can have multiple outputs. I'll set up conditions:
   - Output 1: `{{ $json.output }}` equals `soporte`
   - Output 2: `{{ $json.output }}` equals `ventas`
   - Output 3: Default (otro)

   Wait, n8n's OpenAI node typically outputs `output` or `text`. I'll standardize on `output`.
   I'll add a `Set` node after OpenAI to ensure the classification is clean (trim, lowercase) to avoid routing failures. Or I can just rely on the prompt to strictly return the word.

   Let's structure the nodes properly with n8n's JSON schema format.
   Key fields for each node: `id`, `name`, `type`, `typeVersion`, `position`, `parameters`.

   **Node 1: Webhook**
   - `type`: "n8n-nodes-base.webhook"
   - `parameters`: `httpMethod: "POST"`, `path: "classify-message"`
   - `position`: [250, 300]

   **Node 2: OpenAI**
   - `type`: "@n8n/n8n-nodes-langchain.openAi"
   - `parameters`: 
     - `model: "gpt-4o-mini"` (or similar)
     - `prompt: "Classify the following message into exactly one of these categories: soporte, ventas, or otro. Respond with ONLY the category name.\n\nMessage: {{ $json.message }}"`
     - `options.output: "text"`
   - `position`: [500, 300]

   **Node 3: Set (Clean AI Output)**
   - `type`: "n8n-nodes-base.set"
   - `parameters`: 
     - `values`: `operation: "set"`, `name: "category"`, `value: "=String($json.output).trim().toLowerCase()"`
   - `position`: [750, 300]
   - Actually, I can skip this if I'm careful, but it's safer. I'll include it.

   **Node 4: Switch**
   - `type`: "n8n-nodes-base.switch"
   - `parameters`: 
     - `conditions`: 
       - `options.allowEmpty: true`
       - `conditions`: [
           { `id: "1"`, `operator: { type: "string", operation: "equals" }`, `value1: "=String($json.category).trim().toLowerCase()"`, `value2: "soporte"` },
           { `id: "2"`, `operator: { type: "string", operation: "equals" }`, `value1: "=String($json.category).trim().toLowerCase()"`, `value2: "ventas"` }
         ]
     - `outputs`: `["soporte", "ventas", "otro"]`
   - `position`: [1000, 300]

   **Node 5, 6, 7: Slack**
   - `type`: "n8n-nodes-base.slack"
   - `parameters`: 
     - `operation: "sendMessage"`
     - `channelId: "#support"` (or `#sales`, `#general`)
     - `text: "📧 Nuevo mensaje de: {{ $json.email }}\n💬 Mensaje: {{ $json.message }}\n🤖 Clasificación: {{ $json.category }}"`
   - `position`: [1250, 200], [1250, 300], [1250, 400]

   **Connections:**
   - Webhook -> OpenAI
   - OpenAI -> Set
   - Set -> Switch
   - Switch (soporte) -> Slack #support
   - Switch (ventas) -> Slack #sales
   - Switch (otro) -> Slack #general

4.  **Construct JSON (Mental Refinement & n8n Schema Compliance):**
   I need to make sure the JSON matches n8n's expected structure exactly. I'll use recent n8n node type versions.
   Let's draft it carefully.

   ```json
   {
     "name": "Clasificar Mensaje y Enviar a Slack",
     "nodes": [
       {
         "id": "webhook_trigger",
         "name": "Webhook",
         "type": "n8n-nodes-base.webhook",
         "typeVersion": 2,
         "position": [250, 300],
         "parameters": {
           "httpMethod": "POST",
           "path": "classify-message",
           "responseMode": "responseNode",
           "options": {}
         }
       },
       {
         "id": "openai_classify",
         "name": "OpenAI",
         "type": "@n8n/n8n-nodes-langchain.openAi",
         "typeVersion": 1.3,
         "position": [500, 300],
         "parameters": {
           "model": "gpt-4o-mini",
           "prompt": {
             "value": "Clasifica el siguiente mensaje en CATEGORÍA ÚNICA: soporte, ventas, o otro. Responde SOLO con la palabra de la categoría.\n\nMensaje: {{ $json.message }}"
           },
           "options": {
             "temperature": 0
           }
         }
       },
       {
         "id": "set_category",
         "name": "Limpiar Categoría",
         "type": "n8n-nodes-base.set",
         "typeVersion": 3.3,
         "position": [750, 300],
         "parameters": {
           "values": {
             "string": [
               {
                 "name": "categoria",
                 "value": "=String($json.output).trim().toLowerCase()"
               }
             ]
           },
           "options": {}
         }
       },
       {
         "id": "switch_route",
         "name": "Ruta por Categoría",
         "type": "n8n-nodes-base.switch",
         "typeVersion": 3.1,
         "position": [1000, 300],
         "parameters": {
           "conditions": {
             "string": [
               {
                 "id": "1",
                 "name": "soporte",
                 "value1": "=String($json.categoria).trim().toLowerCase()",
                 "operation":