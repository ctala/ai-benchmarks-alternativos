# Qwen 3.5 397B — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 7.83 | quality: 8.96
- latency_total: 30.452s | tokens_per_second: 67.3
- input_tokens: 125 | output_tokens: 2048
- judge_score: 4.4 | justificación: 

## Respuesta completa

Here's a thinking process that leads to the suggested n8n workflow JSON:

1.  **Analyze the Request:**
    *   **Goal:** Create an n8n workflow in JSON format.
    *   **Trigger:** Webhook (POST method).
    *   **Data Extraction:** Extract `email` and `message` from the request body.
    *   **AI Processing:** Use OpenAI to classify the message into categories: "soporte" (support), "ventas" (sales), or "otro" (other).
    *   **Routing/Action:** Send the email/message to specific Slack channels based on the classification:
        *   "soporte" -> `#support`
        *   "ventas" -> `#sales`
        *   "otro" -> `#general`
    *   **Output:** Complete JSON workflow.

2.  **Determine Necessary Nodes:**
    *   **Webhook Node:** To receive the POST request.
    *   **OpenAI Node:** To analyze the text and classify it. (Note: n8n has a specific "OpenAI" node, often used via the "AI Agent" or "Chain" structure, but for simple classification, the basic "OpenAI" node with a completion/chat request works best).
    *   **Switch/If Node:** To route based on the classification result.
    *   **Slack Node:** To send the message. Since there are three different channels, I might need three Slack nodes or one Slack node configured dynamically. Using a Switch node leading to three specific Slack nodes is clearer for a template, but a single Slack node with an expression for the channel is more efficient. However, to ensure the logic is explicit and easy to understand (and robust against typos in AI output), a Switch node is often safer. Let's use a Switch node to route to three separate Slack nodes for clarity in the JSON structure, or better yet, one Slack node where the channel is mapped via expression based on the switch. Actually, the standard pattern for this in n8n is usually: Webhook -> OpenAI -> Switch -> Slack (x3). Let's go with Switch -> Slack (x3) to make the branches explicit.
    *   **Credentials:** I need to remind the user that they need to set up credentials (OpenAI, Slack). I cannot embed real credentials in the JSON.

3.  **Drafting the Workflow Logic:**

    *   *Webhook:* Method POST, Path (e.g., `classify-message`).
    *   *OpenAI:* Model `gpt-3.5-turbo` or `gpt-4`. Prompt: "Classify the following message into one of these categories: 'soporte', 'ventas', 'otro'. Return ONLY the category name." Input: `{{ $json.body.message }}`.
    *   *Switch:* Check `{{ $json.output }}` (or wherever OpenAI puts the result).
        *   Rule 1: `soporte`
        *   Rule 2: `ventas`
        *   Rule 3: `otro` (default)
    *   *Slack:* Send message. Text: "New Message from {{ email }}: {{ message }}". Channel: mapped per branch.

4.  **Constructing the JSON (Mental or Scratchpad):**

    *   *Version:* n8n standard version (e.g., 1.0 or latest).
    *   *Nodes:*
        1.  `Webhook`
        2.  `OpenAI` (Language Model)
        3.  `Switch`
        4.  `Slack` (Support)
        5.  `Slack` (Sales)
        6.  `Slack` (General)

    *   *Refinement on OpenAI Node:* n8n has evolved. There is the "OpenAI" node (legacy/basic) and the "AI Agent" nodes. For a simple workflow like this, the basic "OpenAI" node is sufficient and less complex to export/import without missing AI chain dependencies. I will use the standard "OpenAI" node configured for "Chat" or "Completion". Let's use the "OpenAI" node with resource "Chat" to ensure it handles instructions well.
    *   *Refinement on Slack:* Need to make sure the Slack node is configured to "Post Message".
    *   *Refinement on Switch:* Use the "Switch" node (not "If") because we have 3 conditions.

5.  **Writing the JSON Content:**

    *   *Webhook:* `httpMethod: POST`, `path: incoming-message`.
    *   *OpenAI:* `resource: chat`, `operation: complete`. Prompt needs to be strict to avoid JSON parsing errors later. "Reply with exactly one word: soporte, ventas, or otro."
    *   *Switch:* Compare `{{ $json.message.content }}` (OpenAI output structure) against strings.
    *   *Slack:* Needs `channel` and `text`.

    *Self-Correction on OpenAI Output:* The OpenAI node in n8n usually returns the content in `choices[0].message.content`. I need to make sure the expression in the Switch node points to the right place.
    *Self-Correction on Slack Credentials:* The JSON will contain placeholder credential IDs. I must add a note telling the user to update them.

6.  **Finalizing the JSON Structure:**
    *   Ensure all connections (`connections` object) are correct.
    *   Ensure node parameters match n8n's schema.
    *   Add comments/notes in the workflow if possible (n8n supports sticky notes, but standard nodes are safer for copy-paste).

7.  **Review against Constraints:**
    *   Webhook POST? Yes.
    *   Extract email/message? Yes (passed through).
    *   OpenAI Classification? Yes.
    *   Slack Routing (support, sales, general)? Yes.
    *   JSON format? Yes.

8.  **Adding Explanations:**
    *   Crucial to tell the user to set up Credentials.
    *   Crucial to tell the user how to import.
    *   Crucial to mention that the OpenAI node might need specific parameter mapping depending on the n8n version (I will aim for a generic recent version structure).

    *(Self-Correction during JSON generation)*: I need to be careful with the OpenAI node output. In recent n8n versions, the OpenAI node output structure might vary slightly. I will assume the standard output where the text is in `text` or `choices[0].message.content`. To be safe and robust, I'll configure the OpenAI node to return the raw response or map the specific content field. Let's use the `text` output if available, or map `choices[0].message.content`. I will use the expression `{{ $json.choices[0].message.content }}` for the switch logic as that is standard for Chat models.

    *Wait, one detail:* The prompt asks to extract "email" and "message". The Webhook receives them. They need to be passed to OpenAI (for message) and to Slack (for both).
    *OpenAI Input:* Only needs `message`.
    *Slack Input:* Needs `email` and `message`.

    *Slack Channel IDs:* Slack API usually requires Channel IDs (e.g., `C012345`) rather than names (`#support`), though some wrappers allow names. I will use the names in the JSON but add a comment that IDs are preferred/required depending on the Slack app permissions. Actually, the n8n Slack node usually allows typing the channel name directly if the bot is invited. I will use the names `support`, `sales`, `general` (without # usually in the API, but n8n UI often handles `#channel`). I'll use just the name `support`, `sales`, `general` in the JSON parameters to be safe, but note that the user might need IDs. *Correction:* n8n Slack node typically expects the Channel ID. I will put placeholders like `C01...` or just the names and add a strong warning. Let's use the names `support`, `sales`, `general` in the JSON but warn the user to check their Slack node configuration. Actually, to be most helpful, I will set the channel parameter to the name, as n8n often resolves it, but the most robust way is ID. I'll use the names for readability but add a comment.

    *Wait, Switch Node Logic:* To make it case-insensitive (AI might return "Soporte" instead of "soporte"), I should add a "Code" node or use an expression in the Switch to lowercase the AI output. Or instruct the AI strictly. Instructing the AI is cheaper/simpler. "Respond ONLY with the lowercase word...".

    *Let's build the JSON.*

9.  **Final Polish:** Check indentation and validity. Ensure no private keys are included.

**(Self-Correction on n8n Version Compatibility):** n8n changes node structures occasionally. I will generate a JSON compatible with n8n 1.0+ (the current standard).

**(Plan for Credentials):** I will use dummy credential IDs (e.g., `YOUR_OPENAI_CREDENTIAL_ID`) so the user knows they need to update them.

**(Plan for Slack Channels):** I will use channel names in