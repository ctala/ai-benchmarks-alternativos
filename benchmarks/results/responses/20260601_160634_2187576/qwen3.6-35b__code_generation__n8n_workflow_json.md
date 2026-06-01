# Qwen 3.6 35B base (OpenRouter FP8) — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3.6-35b-a3b`
- success: True  | final: 6.92 | quality: 7.84
- latency_total: 10.41s | tokens_per_second: 196.7
- input_tokens: 125 | output_tokens: 2048
- judge_score: 3.6 | justificación: 

## Respuesta completa

Here's a thinking process:

1.  **Understand User Requirements:**
   - **Tool:** n8n (workflow automation tool)
   - **Format:** JSON
   - **Trigger:** Webhook POST
   - **Input Fields:** `email`, `message` from the request body
   - **AI Node:** OpenAI to classify the `message` into "soporte", "ventas", or "otro"
   - **Routing Logic:** Based on classification, send to different Slack channels:
     - "soporte" -> `#support`
     - "ventas" -> `#sales`
     - "otro" -> `#general`
   - **Output:** Complete JSON workflow

2.  **Identify Key n8n Nodes Needed:**
   - `n8n-nodes-base.webhook` (Trigger)
   - `n8n-nodes-base.set` or `n8n-nodes-base.code` (Extract fields - though webhook node can handle this, or I can use a Set node for clarity)
   - `n8n-nodes-base.openAi` (AI Classification)
   - `n8n-nodes-base.switch` or `n8n-nodes-base.if` (Routing logic)
   - `n8n-nodes-base.slack` (Send message to Slack) - Need 3 instances or use dynamic channel in one node with routing
   - Actually, n8n's Slack node can send to different channels based on expressions, but for clarity and reliability, I'll use a `Switch` node to route to 3 separate Slack nodes, or use a single Slack node with dynamic channel selection via an `If` or `Switch` node. n8n's `Switch` node is perfect for this.

3.  **Determine Node Structure & Connections:**
   - Webhook -> Set/Extract -> OpenAI -> Switch -> Slack (support)
   - Switch -> Slack (sales)
   - Switch -> Slack (general)
   - All Slack nodes connect to `End` (or just end, n8n handles it)

   Let's map it out:
   - Node 0: Webhook (POST, path: `/classify`, wait for payload: true)
   - Node 1: Set (Extract email and message, or just pass through. Actually, webhook node returns JSON, I can just reference fields directly. But to be safe, I'll use a `Set` node or just rely on expression in subsequent nodes. I'll skip a dedicated Set node and use expressions in OpenAI and Slack nodes for simplicity, or add a `Code` node if needed. Actually, n8n's webhook node returns the whole body, so `{{ $json.email }}` and `{{ $json.message }}` work fine.)
   - Node 2: OpenAI (Chat/Completion) - Prompt to classify message into exactly one of the three categories.
   - Node 3: Switch (Route based on OpenAI output)
   - Node 4: Slack (Channel: #support)
   - Node 5: Slack (Channel: #sales)
   - Node 6: Slack (Channel: #general)

4.  **Draft Node Definitions (Mental Refinement):**

   *Webhook Node:*
   ```json
   {
     "parameters": {
       "httpMethod": "POST",
       "path": "classify",
       "responseMode": "responseNode",
       "options": {}
     },
     "name": "Webhook",
     "type": "n8n-nodes-base.webhook",
     "typeVersion": 2,
     "position": [250, 300]
   }
   ```

   *OpenAI Node:*
   Need to configure it to classify. I'll use `n8n-nodes-base.openAi` with operation `Chat`. Prompt should instruct it to output exactly the category.
   ```json
   {
     "parameters": {
       "model": "gpt-4o-mini",
       "prompt": "Classify the following message into exactly one of these categories: 'soporte', 'ventas', or 'otro'. Only return the category name, nothing else.\n\nMessage: {{ $json.message }}",
       "options": {}
     },
     "name": "Classify Message",
     "type": "n8n-nodes-base.openAi",
     "typeVersion": 3,
     "position": [470, 300]
   }
   ```
   Wait, OpenAI node in n8n returns the response in `data.choices[0].message.content`. I need to make sure the expression in the Switch node references it correctly. Usually, n8n's OpenAI node puts the text in `{{ $json.message }}` or `{{ $json.content }}` depending on version. Let's check n8n's OpenAI node structure. Actually, it's safer to use a `Set` node after OpenAI to extract the classification, or just use the standard path. I'll assume `{{ $json.message }}` or `{{ $json.content }}`. To be robust, I'll add a `Set` node to extract it, or just use the exact field n8n uses. In n8n v1+, OpenAI returns `{{ $json.message }}` for chat. I'll stick with that, but I'll add a `Code` or `Set` node if needed. Actually, I'll use a `Switch` node with expression `{{ $json.message }}`.

   Let's verify n8n OpenAI node output: It typically returns `{ "message": "text", "role": "assistant", ... }`. So `{{ $json.message }}` is correct.

   *Switch Node:*
   ```json
   {
     "parameters": {
       "conditions": {
         "string": [
           {
             "value1": "={{ $json.message }}",
             "operation": "equals",
             "value2": "soporte"
           },
           {
             "value1": "={{ $json.message }}",
             "operation": "equals",
             "value2": "ventas"
           },
           {
             "value1": "={{ $json.message }}",
             "operation": "equals",
             "value2": "otro"
           }
         ]
       },
       "options": {}
     },
     "name": "Route Classification",
     "type": "n8n-nodes-base.switch",
     "typeVersion": 3,
     "position": [690, 300]
   }
   ```

   *Slack Nodes:*
   Need 3 Slack nodes. Each needs credential placeholder. I'll use generic credential references.
   Channel names: `#support`, `#sales`, `#general`. Note: Slack channels in n8n usually don't include the `#` in the channel name field, or they do. I'll use `support`, `sales`, `general` and let n8n handle it, or include `#` if preferred. I'll stick to `#support` as requested, but n8n's Slack node usually expects just the name. I'll use `support`, `sales`, `general` and add a note, or just follow the prompt exactly: `#support`. Actually, n8n's Slack node channel field accepts names with or without `#`. I'll use `#support`.

   Message to send: I should include the email and the original message.
   Text: `Nuevo mensaje de {{ $json.email }}: {{ $json.message }}`

   Slack 1 (Support):
   ```json
   {
     "parameters": {
       "channelId": "#support",
       "text": "📧 Nuevo ticket de soporte:\nDe: {{ $json.email }}\nMensaje: {{ $json.message }}"
     },
     "name": "Slack Support",
     "type": "n8n-nodes-base.slack",
     "typeVersion": 2,
     "position": [910, 100]
   }
   ```

   Slack 2 (Sales):
   ```json
   {
     "parameters": {
       "channelId": "#sales",
       "text": "💰 Nuevo lead de ventas:\nDe: {{ $json.email }}\nMensaje: {{ $json.message }}"
     },
     "name": "Slack Sales",
     "type": "n8n-nodes-base.slack",
     "typeVersion": 2,
     "position": [910, 300]
   }
   ```

   Slack 3 (General):
   ```json
   {
     "parameters": {
       "channelId": "#general",
       "text": "📝 Mensaje clasificado como otro:\nDe: {{ $json.email }}\nMensaje: {{ $json.message }}"
     },
     "name": "Slack General",
     "type": "n8n-nodes-base.slack",
     "typeVersion": 2,
     "position": [910, 500]
   }
   ```

5.  **Assemble Connections:**
   n8n uses `connections` array. I need to