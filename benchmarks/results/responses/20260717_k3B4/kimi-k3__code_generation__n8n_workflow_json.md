# Kimi K3 — code_generation/n8n_workflow_json

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 5.69 | quality: 7.0
- latency_total: 227.214s | tokens_per_second: 36.1
- input_tokens: 209 | output_tokens: 8192
- judge_score: 3.0 | justificación: 

## Respuesta completa

The user wants an n8n workflow JSON that:
1. Triggers with a POST webhook
2. Extracts "email" and "message" fields from the body
3. Uses an OpenAI AI node to classify the message as "soporte", "ventas", or "otro"
4. Based on classification, sends the email to different Slack channels:
   - soporte -> #support
   - ventas -> #sales
   - otro -> #general

They want the complete JSON workflow. The user is writing in Spanish, so I should respond in Spanish.

Let me construct a proper n8n workflow JSON. n8n workflows have this structure:

```json
{
  "name": "Workflow Name",
  "nodes": [...],
  "connections": {...},
  "settings": {...}
}
```

Key nodes I need:
1. **Webhook node** (`n8n-nodes-base.webhook`) - POST method, path
2. **Set node** or **Edit Fields** (`n8n-nodes-base.set`) - to extract email and message (though this could be done inline with expressions, having an explicit extraction step is clearer as requested)
3. **OpenAI node** (`@n8n/n8n-nodes-langchain.openAi` or the older `n8n-nodes-base.openAi`) - to classify the message. Actually, for classification, a good approach is to use the OpenAI node with a chat completion that returns just the category.
4. **Switch node** (`n8n-nodes-base.switch`) - to route based on classification
5. **Three Slack nodes** (`n8n-nodes-base.slack`) - one for each channel

Let me write this carefully.

For the Webhook node:
```json
{
  "parameters": {
    "httpMethod": "POST",
    "path": "clasificar-mensaje",
    "responseMode": "responseNode",
    "options": {}
  },
  "id": "webhook-id",
  "name": "Webhook",
  "type": "n8n-nodes-base.webhook",
  "typeVersion": 2,
  "position": [240, 300],
  "webhookId": "some-uuid"
}
```

Actually, typeVersion 2 for webhook. Let me use a simpler responseMode "onReceived" or use "responseNode" with a Respond to Webhook node. To keep it simpler, I'll use default "onReceived" response mode, or maybe add a Respond to Webhook node for completeness. Let me keep it reasonably simple but complete. I'll use responseMode "onReceived" (default) to avoid needing an extra node... Actually, it's good practice to respond. But the Slack nodes are at the end of three branches, so a respond node would need to be connected to all three. That adds complexity. Let me just use "onReceived" which responds immediately with 200. That's fine.

Actually wait — if I use "lastNode" response mode, it responds with the last node's data, which works if all branches converge. But the three Slack nodes don't converge unless I connect them. Simplest: "onReceived".

For the Edit Fields (Set) node to extract email and message:
```json
{
  "parameters": {
    "assignments": {
      "assignments": [
        {
          "id": "email-field",
          "name": "email",
          "value": "={{ $json.body.email }}",
          "type": "string"
        },
        {
          "id": "message-field",
          "name": "message",
          "value": "={{ $json.body.message }}",
          "type": "string"
        }
      ]
    },
    "options": {}
  },
  "id": "set-id",
  "name": "Extraer Datos",
  "type": "n8n-nodes-base.set",
  "typeVersion": 3.4,
  "position": [460, 300]
}
```

For the OpenAI node — there are two options:
1. The newer LangChain OpenAI node: `@n8n/n8n-nodes-langchain.openAi` (typeVersion 1.8) — actually this is more of a model sub-node now.
2. The classic OpenAI node: `n8n-nodes-base.openAi` (typeVersion 1.x) — supports "Message a model" operation with chat completions.

For simplicity in a single flow, the classic OpenAI node with "message a model" works well:

```json
{
  "parameters": {
    "modelId": "gpt-4o-mini",
    "messages": {
      "values": [
        {
          "role": "system",
          "content": "Eres un clasificador de mensajes. Clasifica el mensaje del usuario en UNA de estas categorías: soporte, ventas, otro. Responde ÚNICAMENTE con la palabra de la categoría, en minúsculas, sin puntuación ni texto adicional."
        },
        {
          "role": "user",
          "content": "=Mensaje de {{ $json.email }}: {{ $json.message }}"
        }
      ]
    },
    "options": {
      "temperature": 0
    }
  },
  "id": "openai-id",
  "name": "Clasificar con OpenAI",
  "type": "n8n-nodes-base.openAi",
  "typeVersion": 1.8,
  "position": [680, 300],
  "credentials": {
    "openAiApi": {
      "id": "",
      "name": "OpenAI account"
    }
  }
}
```

Wait, for `n8n-nodes-base.openAi` typeVersion 1.8, the parameters are:
- `resource`: "chat" (default) — actually in v1.8, there's `resource` with default "chat"? Let me recall. The OpenAI node v1.8 has resource options: chat, image, assistant... Actually let me think about the actual structure.

In n8n's OpenAI node (`n8n-nodes-base.openAi`), typeVersion 1.8:
```json
{
  "parameters": {
    "resource": "chat",
    "modelId": "gpt-4o-mini",
    "messages": {
      "values": [
        {
          "role": "system",
          "content": "..."
        }
      ]
    },
    "options": {}
  }
}
```

Hmm, actually the newer versions use "operation": "message" implicitly. Let me check: OpenAI node v1.8 parameters:

```json
{
  "resource": "chat",
  "operation": "message",
  "modelId": "gpt-4o-mini",
  "messages": {...},
  "jsonOutput": false,
  "options": {}
}
```

Hmm, I'm not 100% sure of exact parameter names. In recent versions (1.8+), it's:
```json
{
  "parameters": {
    "resource": "chat",
    "modelId": {
      "__rl": true,
      "value": "gpt-4o-mini",
      "mode": "list",
      "cachedResultName": "GPT-4O-MINI"
    },
    "messages": {
      "values": [...]
    },
    "options": {}
  }
}
```

The modelId with resourceLocator is what's shown in newer versions. But simpler `"modelId": "gpt-4o-mini"` might also work for import. To be safe, I can use the resourceLocator format or plain string. n8n is fairly tolerant on import — plain string values for resourceLocator fields usually work.

Alternatively, I could use the LangChain chain approach: Basic LLM Chain (`@n8n/n8n-nodes-langchain.chainLlm`) + OpenAI Chat Model (`@n8n/n8n-nodes-langchain.lmChatOpenAi`). This is the "AI node" approach the user might be expecting ("Use un nodo de IA (OpenAI)"). The user said "nodo de IA (OpenAI)" — either works. 

The classic OpenAI node is simpler for a JSON export. But there's a subtlety: the output of the OpenAI node. With `n8n-nodes-base.openAi`, the response text is at `{{ $json.message.content }}`. 

Let me think about the output schema of n8n-nodes-base.openAi chat message operation: it returns the OpenAI API response transformed — typically `{ "message": { "role": "assistant", "content": "..." }, ... }` or with "simplify" it might differ. I believe the output includes `message.content`. Yes, for the "Message a model" operation, output is like:

```json
{
  "message": {
    "role": "assistant",
    "content": "soporte"
  },
  ...
}
```

Hmm, actually it might return the full API response with `choices[0].message.content` if simplify is off. Let me recall... The OpenAI node "Message a Model" returns a simplified output with `message.content` directly. I'm fairly confident the standard output has `message.content`. 

Alternative approach to be robust: use a Set/Code node after OpenAI to normalize the classification, then Switch. Actually, I could add a small normalization step — but the user asked for specific steps. I can include the classification extraction within the Switch node expressions.

For the Switch node (typeVersion 3.2):
```json
{
  "parameters": {
    "rules": {
      "values": [
        {
          "conditions": {
            "options": {
              "caseSensitive": false,
              "leftValue": "",
              "typeValidation": "loose"
            },
            "conditions": [
              {
                "id": "cond-soporte",
                "leftValue": "={{ $json.message.content.trim().toLowerCase() }}",
                "rightValue": "soporte",
                "operator": {
                  "type": "string",
                  "operation": "contains"
                }
              }
            ],
            "combinator": "and"
          },
          "renameOutput": true,
          "outputKey": "soporte"
        },
        ...
      ]
    },
    "options": {
      "fallbackOutput": "extra",
      "renameFallbackOutput": "otro"
    }
  },
  ...
}
```

Using "contains" with caseSensitive false is robust — if the model returns "soporte" or "Soporte." it still matches. And fallback output for "otro" is elegant: route 0 = soporte, route 1 = ventas, fallback = otro. 

Actually, let me use "equals" vs "contains"? Since we instruct the model to return only the word, "equals" with case-insensitive would work, but "contains" is safer if the model adds punctuation. However "contains" has a risk: "ventas" contains check — if model returns something weird like "no es ventas", it'd match ventas. But with a good prompt it returns one word. I'll use "contains" for robustness with case-insensitive. Or I could use equals with trimming. Let me use "equals" with `.trim().toLowerCase()` on the left value — cleaner logic. Hmm, but "caseSensitive": false makes equals case-insensitive already. I'll do trim().toLowerCase() + equals — deterministic.

Actually to keep it simpler in the JSON, I'll use "contains" with caseSensitive: false. Hmm. Let me decide: I'll use `equals` operator with leftValue `={{ $json.message.content.trim().toLowerCase() }}` and rightValue `soporte`. Clean.

For Slack nodes:
```json
{
  "parameters": {
    "resource": "message",
    "operation": "post",
    "select": "channel",
    "channelId": {
      "__rl": true,
      "value": "#support",
      "mode": "name"
    },
    "messageType": "text",
    "text": "=...",
    "otherOptions": {}
  },
  "id": "slack-support-id",
  "name": "Slack #support",
  "type": "n8n-nodes-base.slack",
  "typeVersion": 2.3,
  "position": [1150, 200],
  "credentials": {
    "slackApi": {
      "id": "",
      "name": "Slack account"
    }
  }
}
```

Slack node v2+ parameters for posting a message:
```json
{
  "select": "channel",
  "channelId": {
    "__rl": true,
    "value": "C01234567",
    "mode": "list"
  },
  "text": "...",
  "otherOptions": {}
}
```

With mode "name" you can pass "#support"? Actually in the Slack node v2, channelId modes are "list", "id", "url"... I think there's also "name" mode available? In n8n resource locator for Slack channel, modes include: list, url, id. I'm not sure "name" is a mode for Slack. Hmm. Many examples use:

```json
"channelId": {
  "__rl": true,
  "value": "support",
  "mode": "name"
}
```

Actually yes — Slack node channelId supports modes: "list", "name", "url", "id"? Let me recall the actual resourceLocator config in the Slack node... The channel resourceLocator in n8n Slack node has modes: list (from channels), name (channel name), id (channel ID). I believe "name" is indeed a supported mode because there were community posts about posting to channel names. Hmm, actually I recall modes: "list", "url", "id". But I've seen exported workflows with `"mode": "name"` and value "#channel". The Slack API method `chat.postMessage` accepts a channel name? No, it requires channel ID, but n8n can resolve names. Let me just use the simplest robust form: use `"channelId": {"__rl": true, "value": "#support", "mode": "name"}`. Even if the exact mode differs, on import the user will select their channel anyway since credentials need configuring. This is acceptable.

Alternatively use older Slack v1 style with "channel": "#support" string. Slack node typeVersion 2.3 uses resourceLocator. I'll go with v2.3 and mode "name".

For the text message in Slack:
```
🎫 *Nuevo mensaje clasificado como: soporte*
📧 *Email:* {{ $('Extraer Datos').item.json.email }}
💬 *Mensaje:* {{ $('Extraer Datos').item.json.message }}
```

Using `$('Node Name').item.json` references ensures the data is accessible regardless of the node output chain. Note: after the OpenAI node, the email/message fields may not be in $json (depends on OpenAI node output), so referencing the Set node by name is correct. 

Also for the Switch node input, referencing `{{ $json.message.content }}` — the Switch node gets input from OpenAI node directly, so $json refers to OpenAI output. Good. But to be extra safe, use `{{ $('Clasificar con OpenAI').item.json.message.content }}`. That's more explicit. I'll use that.

Connections structure:
```json
"connections": {
  "Webhook": {
    "main": [
      [
        { "node": "Extraer Datos", "type": "main", "index": 0 }
      ]
    ]
  },
  "Extraer Datos": {
    "main": [
      [
        { "node": "Clasificar con OpenAI", "type": "main", "index": 0 }
      ]
    ]
  },
  "Clasificar con OpenAI": {
    "main": [
      [
        { "node": "Switch Clasificacion", "type": "main", "index": 0 }
      ]
    ]
  },
  "Switch Clasificacion": {
    "main": [
      [
        { "node": "Slack #support", "type": "main", "index": 0 }
      ],
      [
        { "node": "Slack #sales", "type": "main", "index": 0 }
      ],
      [
        { "node": "Slack #general", "type": "main", "index": 0 }
      ]
    ]
  }
}
```

Node IDs: use UUID-like strings or simple descriptive ids. n8n accepts any string id. I'll use UUIDs for realism, or readable ids. I'll generate plausible UUIDs.

Positions: Webhook [240, 300], Set [460, 300], OpenAI [700, 300], Switch [920, 300], Slack nodes [1180, 180/300/420].

Settings: `{ "executionOrder": "v1" }`.

Let me also think about the webhook typeVersion: current is 2. Parameters: httpMethod "POST", path, responseMode. typeVersion 2 uses:
```json
{
  "httpMethod": "POST",
  "path": "clasificar-mensaje",
  "responseMode": "onReceived",
  "options": {}
}
```

Good.

Set node typeVersion 3.4 uses `assignments` structure. Good.

OpenAI node — let me double check `n8n-nodes-base.openAi` typeVersion 1.8 parameters. Looking at n8n docs for the OpenAI node "Message a model" operation:

```json
{
  "parameters": {
    "resource": "chat",
    "operation": "message",
    "modelId": "gpt-4o-mini",
    "messages": {
      "values": [
        {
          "role": "system",
          "content": "..."
        },
        {
          "content": "=..."
        }
      ]
    },
    "options": {
      "temperature": 0
    }
  },
  "type": "n8n-nodes-base.openAi",
  "typeVersion": 1.8
}
```

Hmm, does v1.8 have "operation": "message"? The chat resource has operations like "message", "classify", ... Actually I think the chat resource default operation is "message" and it's hidden/default. Let me include `"resource": "chat"` and `"operation": "message"` — wait, I need to be careful: I believe in v1.8 the chat resource's operation is called "message". Yes — "Message a Model". I'll include both resource and operation; if operation isn't a valid param, n8n import typically tolerates extra params? Actually n8n can be picky but usually it just ignores unknown params or shows defaults. It's safer to include standard ones. I'll include resource: "chat", operation: "message".

Hmm wait — actually I want to double-check the modelId resourceLocator. In exported workflows from recent n8n versions, OpenAI node shows:

```json
"modelId": {
  "__rl": true,
  "value": "gpt-4o-mini",
  "mode": "list",
  "cachedResultName": "gpt-4o-mini"
}
```

I'll use the resourceLocator format since it's what's generated, but plain string also imports fine typically. Let me use resourceLocator format to look authentic.

Output of OpenAI node: For the "message a model" operation, the output JSON includes `message: { role, content }`? Let me think again... I recall the output of OpenAI chat message in the OpenAI node v1 is:

```json
{
  "message": {
    "role": "assistant",
    "content": "soporte"
  },
  "usage": {...}
}
```

Yes, I'm fairly confident — the node's output has `message.content`. There have been community threads confirming `{{$json.message.content}}`. Good.

Alternative: I could make it more robust with an option "simplify"? Not needed.

Now, should I also handle the case where the model outputs "otro"? The Switch fallback handles it. Also maybe the model might return something unexpected — fallback catches it. Good design.

Additionally, I might add a note (sticky note) nodes explaining setup. Could add one sticky note with setup instructions. Nice touch but optional. I'll add one sticky note with brief setup notes — it makes the workflow friendlier. Sticky note type: `n8n-nodes-base.stickyNote`.

Let me also make sure the Slack text uses expressions referencing the "Extraer Datos" node:

```
=Nuevo mensaje clasificado: *soporte*
• Email: {{ $('Extraer Datos').item.json.email }}
• Mensaje: {{ $('Extraer Datos').item.json.message }}
```

For Slack markdown, bullet might be fine. Use simple text.

Credentials: include placeholder credential objects so n8n prompts to select/create. Like:

```json
"credentials": {
  "openAiApi": {
    "id": "",
    "name": "OpenAI account"
  }
}
```

Empty id might cause import issues? Usually imported workflows have credential names without ids and n8n matches by name or asks. Common practice: `"credentials": { "openAiApi": { "id": null, "name": "OpenAI account" } }`. Hmm, safest might be to omit credentials entirely or include with empty string id. When you import a workflow JSON with credentials that don't exist, n8n shows an error at import? Actually n8n handles it: it imports and marks credentials as needing setup. If the credential id doesn't exist, you may get "credential not found" warnings but it still imports. Many shared workflow JSONs include credential stubs. I'll include them with empty id — or omit? Omitting credentials means the nodes show "select credential". That's clean. But including the stub communicates which credential type is needed. I'll include stubs with `"id": ""` — hmm, actually I've seen n8n reject empty-string ids? I don't think it rejects; it just can't resolve. Let me include `"id": ""` and a name. Actually, to be safe, I'll include the credentials key with name only and id as empty string; n8n community templates do this all the time.

Also `webhookId` on the webhook node: n8n generates one; I can include a UUID. If omitted, n8n assigns. I'll include one.

Top-level structure for import:

```json
{
  "name": "Clasificador de mensajes con IA → Slack",
  "nodes": [...],
  "connections": {...},
  "settings": { "executionOrder": "v1" },
  "pinData": {},
  "meta": { "templateCredsSetupCompleted": false, "instanceId": "" }
}
```

When importing via "Import from JSON", n8n accepts { name, nodes, connections, settings, pinData }. Keep meta optional — I'll include a minimal meta or skip it. I'll skip meta to reduce noise, but include pinData: {}.

Let me write out the full JSON now.

Node list:

1. Webhook
```json
{
  "parameters": {
    "httpMethod": "POST",
    "path": "clasificar-mensaje",
    "responseMode": "onReceived",
    "options": {}
  },
  "id": "a1b2c3d4-0001-4000-8000-000000000001",
  "name": "Webhook",
  "type": "n8n-nodes-base.webhook",
  "typeVersion": 2,
  "position": [240, 300],
  "webhookId": "clasificador-webhook"
}
```

2. Extraer Datos (Set v3.4)
```json
{
  "parameters": {
    "assignments": {
      "assignments": [
        {
          "id": "f1-field-email",
          "name": "email",
          "value": "={{ $json.body.email }}",
          "type": "string"
        },
        {
          "id": "f1-field-message",
          "name": "message",
          "value": "={{ $json.body.message }}",
          "type": "string"
        }
      ]
    },
    "options": {}
  },
  "id": "a1b2c3d4-0002-4000-8000-000000000002",
  "name": "Extraer Datos",
  "type": "n8n-nodes-base.set",
  "typeVersion": 3.4,
  "position": [460, 300]
}
```

Note: Webhook v2 output: body fields are under `$json.body`. Yes, webhook node output structure: `{ headers, params, query, body, ... }`. If content type is JSON, body contains parsed fields. Good.

3. Clasificar con OpenAI
```json
{
  "parameters": {
    "resource": "chat",
    "operation": "message",
    "modelId": {
      "__rl": true,
      "value": "gpt-4o-mini",
      "mode": "list",
      "cachedResultName": "GPT-4O-MINI"
    },
    "messages": {
      "values": [
        {
          "role": "system",
          "content": "Eres un clasificador de mensajes para una empresa. Clasifica el mensaje del usuario en exactamente UNA de estas categorías:\n- soporte: problemas técnicos, errores, dudas sobre el uso del producto, ayuda\n- ventas: precios, planes, compras, demos, cotizaciones\n- otro: cualquier otro tema\n\nResponde ÚNICAMENTE con una palabra: soporte, ventas u otro. Sin puntuación ni explicaciones."
        },
        {
          "role": "user",
          "content": "=Email del remitente: {{ $json.email }}\nMensaje: {{ $json.message }}"
        }
      ]
    },
    "options": {
      "temperature": 0,
      "maxTokens": 10
    }
  },
  "id": "a1b2c3d4-0003-4000-8000-000000000003",
  "name": "Clasificar con OpenAI",
  "type": "n8n-nodes-base.openAi",
  "typeVersion": 1.8,
  "position": [700, 300],
  "credentials": {
    "openAiApi": {
      "id": "",
      "name": "OpenAI account"
    }
  }
}
```

4. Switch
```json
{
  "parameters": {
    "rules": {
      "values": [
        {
          "conditions": {
            "options": {
              "caseSensitive": true,
              "leftValue": "",
              "typeValidation": "loose",
              "version": 2
            },
            "conditions": [
              {
                "id": "cond-soporte",
                "leftValue": "={{ $('Clasificar con OpenAI').item.json.message.content.trim().toLowerCase() }}",
                "rightValue": "soporte",
                "operator": {
                  "type": "string",
                  "operation": "equals",
                  "name": "filter.operator.equals"
                }
              }
            ],
            "combinator": "and"
          },
          "renameOutput": true,
          "outputKey": "soporte"
        },
        {
          "conditions": {
            "options": {
              "caseSensitive": true,
              "leftValue": "",
              "typeValidation": "loose",
              "version": 2
            },
            "conditions": [
              {
                "id": "cond-ventas",
                "leftValue": "={{ $('Clasificar con OpenAI').item.json.message.content.trim().toLowerCase() }}",
                "rightValue": "ventas",
                "operator": {
                  "type": "string",
                  "operation": "equals",
                  "name": "filter.operator.equals"
                }
              }
            ],
            "combinator": "and"
          },
          "renameOutput": true,
          "outputKey": "ventas"
        }
      ]
    },
    "options": {
      "fallbackOutput": "extra",
      "renameFallbackOutput": "otro"
    }
  },
  "id": "a1b2c3d4-0004-4000-8000-000000000004",
  "name": "Switch Clasificacion",
  "type": "n8n-nodes-base.switch",
  "typeVersion": 3.2,
  "position": [940, 300]
}
```

5. Slack nodes x3. Slack node typeVersion 2.3:

```json
{
  "parameters": {
    "select": "channel",
    "channelId": {
      "__rl": true,
      "value": "#support",
      "mode": "name"
    },
    "messageType": "text",
    "text": "=*🔧 Nuevo mensaje de SOPORTE*\n📧 *Email:* {{ $('Extraer Datos').item.json.email }}\n💬 *Mensaje:* {{ $('Extraer Datos').item.json.message }}",
    "otherOptions": {}
  },
  "id": "...",
  "name": "Slack #support",
  "type": "n8n-nodes-base.slack",
  "typeVersion": 2.3,
  "position": [1210, 180],
  "credentials": {
    "slackApi": {
      "id": "",
      "name": "Slack account"
    }
  }
}
```

Hmm, Slack v2.3 params: resource defaults to "message", operation "post" — in v2, "resource": "message" and "operation": "post" might not be explicit params; the node has "select" (channel/user), "channelId", "text"/blocks, "otherOptions". I think for message/post, the params are:

```json
{
  "select": "channel",
  "channelId": {...},
  "messageType": "text",
  "text": "...",
  "otherOptions": {}
}
```

That matches exported workflows I've seen. I'll include `"resource": "message", "operation": "post"` too for safety — harmless if extra. Hmm, actually including unknown params could theoretically cause n8n to display them oddly, but typically they're just ignored/migrated. Many exports include them. Let me include them — actually in v2 exports I believe resource/operation ARE included: `"resource": "message", "operation": "post"`. Yes, I've seen that. Include.

For channelId mode: I've genuinely seen `"mode": "name"` with value like "#general" in Slack node exports? Hmm. The Slack node's channel resourceLocator modes are defined in its description... I recall modes: "list" (Channels), "id" (By ID), "url" (By URL)... and possibly "name" isn't there. Wait — n8n resource locator for Slack channel: modes are `list`, `url`, `id`. Hmm, but I also have a memory of `"mode": "name"` appearing in Slack exports. Let me think... In older Slack node (v1), it was just `"channel": "#general"` string. In v2, channelId RL with modes list/id/url. Hmm, but I do recall community exports with mode "name"... 

Actually, I now recall: n8n Slack v2 channel resource locator DOES support "name"? Let me think about the source: `modes: [list, url, id]`... The `url` mode extracts from Slack URL. I'm not certain about name. Given uncertainty, safest is mode "id" with a placeholder value like "C0123456789" and a comment in the sticky note that the user must select their channel. But that's less friendly. Alternatively use mode "list" with cachedResultName. On import, the user must reselect channels anyway because the channel ID differs per workspace.

I'll use mode "name" with "#support" — hmm, risk. Let me instead use "list" mode with value "#support" and cachedResultName "#support"? If mode list and value isn't a valid ID, it'll show error until user picks channel — which they'll have to do anyway. 

Decision: use `"mode": "name"`. I've seen it in real exports (e.g., `{"__rl": true, "value": "#random", "mode": "name"}`). I'm fairly confident n8n Slack node supports a "By name" mode... Hmm. Let me search memory: In n8n docs for Slack node, "Channel: choose From list, By ID, or By URL". I don't remember "By name". 

OK alternative that definitely works: skip resourceLocator complexity by... no, RL is required in v2.

Compromise: I'll use mode "name" and add a note in the sticky note: "selecciona los canales en cada nodo de Slack según tu workspace". If "name" mode isn't valid, the node will show the value anyway and user reselects. Actually you know, I've definitely seen template JSONs with:

```json
"channelId": {
  "__rl": true,
  "value": "#general",
  "mode": "name"
}
```

Yes — n8n Slack node channel RL includes mode "name" — I'm now recalling `getChannels` and the modes array includes { name: 'By name', value: 'name' }? Honestly uncertain, but community templates use it, so it imports fine (worst case it's coerced). Go with "name".

Sticky note:
```json
{
  "parameters": {
    "content": "## Configuración\n1. Activa el workflow y usa la URL del webhook (POST /webhook/clasificar-mensaje)\n2. Conecta tus credenciales de OpenAI y Slack\n3. Ajusta los canales de Slack si es necesario\n\nBody esperado: `{ \"email\": \"...\", \"message\": \"...\" }`",
    "height": 260,
    "width": 420,
    "color": 4
  },
  "id": "sticky-id",
  "name": "Sticky Note",
  "type": "n8n-nodes-base.stickyNote",
  "typeVersion": 1,
  "position": [240, 80]
}
```

Note: sticky note connections: none.

Connections keys must match node names exactly: "Webhook", "Extraer Datos", "Clasificar con OpenAI", "Switch Clasificacion". Targets: "Slack #support", "Slack #sales", "Slack #general".

Now also, should the OpenAI node output reference in Switch use `$json.message.content` — with the named reference `$('Clasificar con OpenAI').item.json.message.content` — good.

One more consideration: the OpenAI node's "simplify" — not applicable. And whether `message.content` might be under `choices`... For the OpenAI node v1.8 "Message a model", I'm confident output is `message.content`. Hmm, let me hedge: the expression could be written defensively:

```
={{ ($json.message?.content || '').trim().toLowerCase() }}
```

Optional chaining in n8n expressions works (they use a JS-like evaluator — tournament). `?.` is supported in n8n expressions. I'll keep it simpler without optional chaining but it's fine either way. I'll use the named-node reference version:

`={{ $('Clasificar con OpenAI').item.json.message.content.trim().toLowerCase() }}`

Now, response format: The user asked for the complete JSON. I should provide the JSON in a code block, plus brief explanation of how to use it (import steps, credentials, test curl). Keep prose concise per instructions. Respond in Spanish since the user wrote in Spanish.

Format: A short intro line, the JSON code block, then a compact section with: cómo importar, ejemplo de test con curl, y notas. Use headers sparingly; a small bulleted list is fine. The JSON is long — that's expected and requested.

Let me finalize IDs as UUIDs. I'll use distinct UUIDs:
- Webhook: "b7c1f2a0-3d4e-4f5a-8b9c-1a2b3c4d5e01"
- Extraer Datos: "b7c1f2a0-3d4e-4f5a-8b9c-1a2b3c4d5e02"
- OpenAI: "b7c1f2a0-3d4e-4f5a-8b9c-1a2b3c4d5e03"
- Switch: "b7c1f2a0-3d4e-4f5a-8b9c-1a2b3c4d5e04"
- Slack support: "b7c1f2a0-3d4e-4f5a-8b9c-1a2b3c4d5e05"
- Slack sales: "b7c1f2a0-3d4e-4f5a-8b9c-1a2b3c4d5e06"
- Slack general: "b7c1f2a0-3d4e-4f5a-8b9c-1a2b3c4d5e07"
- Sticky: "b7c1f2a0-3d4e-4f5a-8b9c-1a2b3c4d5e08"

webhookId: "9f8e7d6c-5b4a-3c2d-1e0f-9a8b7c6d5e4f" — hmm, actually webhookId should be a uuid; fine.

Positions:
- Webhook: [260, 360]
- Extraer Datos: [480, 360]
- OpenAI: [720, 360]
- Switch: [960, 360]
- Slack #support: [1240, 220]
- Slack