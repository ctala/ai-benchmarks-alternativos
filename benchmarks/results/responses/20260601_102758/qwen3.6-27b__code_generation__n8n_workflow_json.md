# Qwen 3.6 27B base (OpenRouter FP8) — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3.6-27b`
- success: True  | final: 6.35 | quality: 7.0
- latency_total: 29.785s | tokens_per_second: 68.8
- input_tokens: 125 | output_tokens: 2048
- judge_score: 3.0 | justificación: 

## Respuesta completa

Here's a thinking process:

1.  **Understand User Request:**
   - **Tool:** n8n (workflow automation platform)
   - **Format:** JSON
   - **Trigger:** Webhook POST
   - **Extract:** `email` and `message` from the request body
   - **AI Node:** OpenAI to classify `message` into "soporte", "ventas", or "otro"
   - **Routing/Action:** Send email to different Slack channels based on classification:
     - "soporte" -> #support
     - "ventas" -> #sales
     - "otro" -> #general
   - **Output:** Complete n8n workflow JSON

2.  **Identify Key n8n Nodes Needed:**
   - Webhook (trigger)
   - Set/Code/SplitOut (to extract `email` and `message`) - Actually, Webhook automatically parses JSON body, so we can just reference `{{ $json.body.email }}` and `{{ $json.body.message }}`. But to be clean, I might use a Set node or just reference directly. I'll stick to direct references or a simple Set node for clarity.
   - OpenAI (AI Agent/Text Generation) - n8n has an "OpenAI" node. I'll configure it to classify the text.
   - Switch/Routing node - to route based on classification result.
   - Slack nodes (3 instances or 1 with dynamic channel) - I'll use 3 Slack nodes for clarity, or 1 with expression. Actually, n8n's Switch node routes to different outputs, which is cleaner. I'll use a Switch node with 3 outputs, each connected to a Slack node.
   - Wait, n8n's Switch node routes based on expressions. I'll set it up to check the classification result.

3.  **Determine n8n JSON Structure:**
   n8n workflows have a specific JSON schema. Key parts:
   ```json
   {
     "name": "Workflow Name",
     "nodes": [...],
     "connections": {...},
     "settings": {...},
     "staticData": {...},
     "id": 1,
     "active": false,
     "pinData": {},
     "settings": {
       "executionOrder": "v1"
     },
     "versionId": "...",
     "meta": {
       "instanceId": "..."
     }
   }
   ```
   I need to generate valid node definitions with `id`, `name`, `type`, `typeVersion`, `position`, and `parameters`.

4.  **Draft Node Definitions (Mental Refinement):**
   - **Webhook:**
     - type: `n8n-nodes-base.webhook`
     - parameters: `httpMethod: POST`, `path: classify-message`, `responseMode: responseNode` (or `onReceived`), `options: {}`
     - position: [250, 300]
   - **Set (Extract/Clean):** Actually, I can skip this and just use expressions in the OpenAI node. But to be explicit, I'll add a `Set` node or just reference directly. I'll skip extra nodes for simplicity, n8n handles body parsing automatically. I'll just reference `{{ $json.body.email }}` and `{{ $json.body.message }}`.
   - **OpenAI:**
     - type: `@n8n/n8n-nodes-langchain.openAi` (or `n8n-nodes-base.openAi` depending on version. I'll use `n8n-nodes-base.openAi` for text generation, or `@n8n/n8n-nodes-langchain.agent` if using AI Agent. Actually, n8n has a dedicated "OpenAI" node for text completion. I'll use `n8n-nodes-base.openAi` with `operation: classify` or `textGeneration`. Wait, n8n's OpenAI node supports `operation: "completion"` or `textGeneration`. I'll use `operation: "completion"` or just standard prompt.
     - Let's check current n8n OpenAI node structure: `type: "n8n-nodes-base.openAi"`, `parameters: { operation: "completion", model: "gpt-3.5-turbo", promptTemplates: [{ values: { text: "={{ $json.body.message }}" }] } }` - Actually, n8n uses `prompt: "..."` now. I'll use a simple prompt: `Classifica el siguiente mensaje en una de estas categorías: "soporte", "ventas" o "otro". Solo responde con la categoría.\n\nMensaje: {{ $json.body.message }}`
     - I'll set `options: { responseFormat: { responseFormat: { name: "json_object" } } }` to ensure clean output, but it's fine to just parse it. Actually, simpler: just use text generation and trim output.
     - Let's use `@n8n/n8n-nodes-langchain.openAi`? No, standard is fine. I'll stick to `n8n-nodes-base.openAi` with `operation: "completion"`.
     - Actually, n8n's OpenAI node structure has evolved. I'll use a safe, modern structure:
       ```json
       {
         "id": "openai_node_id",
         "name": "OpenAI Classifier",
         "type": "n8n-nodes-base.openAi",
         "typeVersion": 103,
         "position": [500, 300],
         "parameters": {
           "operation": "completion",
           "model": "gpt-3.5-turbo",
           "prompt": "Classifica el siguiente mensaje en una de estas categorías: \"soporte\", \"ventas\" o \"otro\". Responde ÚNICAMENTE con la categoría exacta.\n\nMensaje: {{ $json.body.message }}",
           "options": {
             "temperature": 0
           }
         }
       }
       ```
   - **Switch:**
     - type: `n8n-nodes-base.switch`
     - parameters: `conditions: { string: [{ value1: "={{ $json.output }}", value2: "soporte" }, { value1: "={{ $json.output }}", value2: "ventas" }, { value1: "={{ $json.output }}", value2: "otro" }] }` (Wait, Switch node takes a list of conditions with labels)
     - Actually, n8n Switch node structure:
       ```json
       "parameters": {
         "conditions": {
           "string": [
             { "value1": "={{ $json.output.trim() }}", "value2": "soporte" },
             { "value1": "={{ $json.output.trim() }}", "value2": "ventas" },
             { "value1": "={{ $json.output.trim() }}", "value2": "otro" }
           ]
         },
         "defaultCondition": "otro"
       }
       ```
     - I'll label outputs: `soporte`, `ventas`, `otro`.
   - **Slack Nodes (3):**
     - type: `n8n-nodes-base.slack`
     - parameters: `operation: "sendChannelMessage"`, `channelId: "#support"`, `text: "={{ $json.body.email }} dice: {{ $json.body.message }}"`
     - I'll create 3 instances, positioned accordingly.

5.  **Construct JSON Structure (Mental to Actual):**
   I need to ensure positions, IDs, and connections are valid. n8n uses `id` (UUID), `name`, `type`, `typeVersion`, `position: [x, y]`, `parameters`.
   Connections map: `"node1": { "main": [ [ { "node": "node2", "type": "main", "index": 0 } ] ] } }`

   Let's draft carefully:

   **Nodes:**
   1. Webhook: id `webhook_1`, pos `[250, 300]`
   2. OpenAI: id `openai_1`, pos `[500, 300]`
   3. Switch: id `switch_1`, pos `[750, 300]`
   4. Slack Support: id `slack_support`, pos `[1000, 200]`
   5. Slack Sales: id `slack_sales`, pos `[1000, 300]`
   6. Slack General: id `slack_general`, pos `[1000, 400]`

   **Connections:**
   - Webhook -> OpenAI (main index 0)
   - OpenAI -> Switch (main index 0)
   - Switch -> Slack Support (main index 0, output index 0)
   - Switch -> Slack Sales (main index 0, output index 1)
   - Switch -> Slack General (main index 0, output index 2)

   Wait, n8n Switch node outputs are indexed by the order they are defined in conditions. So output 0 = soporte, 1