# Qwen 3.6 35B base (OpenRouter FP8) — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3.6-35b-a3b`
- success: True  | final: 7.06 | quality: 8.12
- latency_total: 13.882s | tokens_per_second: 147.5
- input_tokens: 125 | output_tokens: 2048
- judge_score: 3.8 | justificación: 

## Respuesta completa

Here's a thinking process:

1.  **Understand User Requirements:**
   - **Tool:** n8n workflow in JSON format
   - **Trigger:** Webhook (POST)
   - **Input Fields:** Extract `email` and `message` from the request body
   - **AI Node:** Use OpenAI to classify the message into "soporte", "ventas", or "otro"
   - **Routing/Slack Integration:** Based on classification, send the email to different Slack channels:
     - `soporte` -> `#support`
     - `ventas` -> `#sales`
     - `otro` -> `#general`
   - **Output:** Complete JSON workflow

2.  **Deconstruct n8n Workflow Structure:**
   An n8n workflow JSON typically contains:
   - `nodes`: Array of node definitions
   - `connections`: Object mapping node IDs to their connections
   - `settings`: Optional global settings
   - `id`/`name`: Workflow metadata

   Each node has:
   - `id`: Unique identifier
   - `name`: Display name
   - `type`: Node type (e.g., `n8n-nodes-base.webhook`, `n8n-nodes-base.openai`, `n8n-nodes-base.slack`)
   - `typeVersion`: Version number
   - `position`: [x, y] coordinates
   - `parameters`: Node-specific settings
   - `credentials`: If needed (for OpenAI, Slack)
   - `triggerWhenAvailable`: For webhooks

3.  **Design Nodes & Connections:**
   - **Node 1: Webhook Trigger**
     - Type: `n8n-nodes-base.webhook`
     - HTTP Method: POST
     - Path: e.g., `classify-message`
     - Authentication: None (or API key, but keep simple)
     - Response Mode: Wait until received, or Use Webhook Node's Response Mode (default is fine)
     - Parameters: Enable "Webhook URL" for POST
   - **Node 2: Extract/Parse (Optional but good practice)**
     - Actually, n8n webhooks automatically parse JSON bodies. I can directly access `email` and `message` via `{{ $json.email }}` and `{{ $json.message }}`. No extra node needed unless I want to set defaults or handle errors. I'll keep it simple.
   - **Node 3: OpenAI (Classification)**
     - Type: `n8n-nodes-base.openai`
     - Operation: Chat
     - Model: gpt-3.5-turbo or gpt-4o-mini
     - Prompt: System prompt to classify into exactly "soporte", "ventas", or "otro". Use JSON mode or structured output if possible, but a simple prompt with instructions is fine. I'll use a structured response format like JSON for reliability.
     - Input: `{{ $json.message }}`
     - Parameters: Set up prompt, model, temperature=0, response format=JSON (if available in node version)
   - **Node 4: Switch/IF (Routing)**
     - Actually, n8n has a `Switch` node or `IF` node. `Switch` is better for multi-way routing.
     - Type: `n8n-nodes-base.switch`
     - Conditions: 
       1. `{{ $json.classification }}` equals `soporte`
       2. `{{ $json.classification }}` equals `ventas`
       3. `{{ $json.classification }}` equals `otro` (default/else)
   - **Nodes 5, 6, 7: Slack (Send Message)**
     - Type: `n8n-nodes-base.slack`
     - Operation: Send Message
     - Channel: `#support`, `#sales`, `#general`
     - Message: `Email: {{ $json.email }}\nMessage: {{ $json.message }}\nClassification: {{ $json.classification }}`
     - Each Slack node connects to one branch of the Switch node.

4.  **Map to n8n JSON Structure (Mental Draft & Refinement):**
   I need to be careful with n8n's exact node structure, especially version numbers and parameter paths. I'll use common stable versions (v2 for webhook, v4 for openai, v3 for slack, v2 for switch). I'll construct the JSON carefully.

   Let's draft node by node:

   **Webhook Node:**
   ```json
   {
     "id": "webhook-trigger",
     "name": "Webhook Trigger",
     "type": "n8n-nodes-base.webhook",
     "typeVersion": 2,
     "position": [240, 300],
     "webhookId": "custom-webhook-id",
     "parameters": {
       "httpMethod": "POST",
       "path": "classify-email",
       "responseMode": "responseNode",
       "options": {}
     },
     "credentials": {}
   }
   ```

   **OpenAI Node:**
   Need to extract classification. I'll use a system prompt that forces JSON output: `{"category": "soporte|ventas|otro"}`. Then in the output, I'll reference `{{ $json.choices[0].message.content }}` and parse it, OR use n8n's built-in JSON parsing if available. Actually, n8n's OpenAI node has a "Response Format" option in newer versions. I'll stick to a simpler approach: use a prompt that returns just the word, or use JSON mode if possible. To be safe across versions, I'll use a prompt that returns exactly the category, and maybe add a "Code" node to parse JSON if needed. But n8n's OpenAI node v4 supports `responseFormat: { type: "json_object" }`. I'll use that.
   Actually, to keep it robust, I'll use a simple prompt and rely on n8n's expression. I'll set the prompt to: "Classify the following message into exactly one of these categories: soporte, ventas, otro. Return only the category name."
   Wait, n8n's OpenAI node parameters structure for Chat:
   ```json
   "parameters": {
     "model": "gpt-3.5-turbo",
     "messages": {
       "values": [
         {
           "role": "system",
           "content": "You are a classifier. Return only one of these words: soporte, ventas, otro."
         },
         {
           "role": "user",
           "content": "={{ $json.message }}"
         }
       ]
     },
     "options": {
       "temperature": 0
     }
   }
   ```
   The output will be in `{{ $json.choices[0].message.content }}`.

   **Switch Node:**
   ```json
   {
     "id": "switch-classification",
     "name": "Switch Classification",
     "type": "n8n-nodes-base.switch",
     "typeVersion": 2,
     "position": [560, 300],
     "parameters": {
       "conditions": {
         "string": [
           {
             "value1": "={{ $json.choices[0].message.content }}",
             "operation": "equals",
             "value2": "soporte"
           },
           {
             "value1": "={{ $json.choices[0].message.content }}",
             "operation": "equals",
             "value2": "ventas"
           },
           {
             "value1": "={{ $json.choices[0].message.content }}",
             "operation": "equals",
             "value2": "otro"
           }
         ]
       },
       "options": {}
     }
   }
   ```

   **Slack Nodes (3 of them):**
   Each will have:
   ```json
   {
     "id": "slack-support",
     "name": "Send to #support",
     "type": "n8n-nodes-base.slack",
     "typeVersion": 3,
     "position": [800, 150],
     "parameters": {
       "channelId": "#support",
       "text": "Email: {{ $json.email }}\nMessage: {{ $json.message }}\nClassified as: {{ $json.choices[0].message.content }}"
     },
     "credentials": {
       "slackApi": { "id": "your-slack-credentials-id", "name": "Slack Account" }
     }
   }
   ```
   I'll create three identical structures with different channels and IDs.

   **Connections:**
   ```json
   "connections": {
     "Webhook Trigger": {
       "main": [
         [
           { "node": "OpenAI Classifier", "type": "main", "index": 0 }
         ]
       ]
     },
     "OpenAI Classifier": {
       "main": [
         [
           { "node": "Switch Classification",