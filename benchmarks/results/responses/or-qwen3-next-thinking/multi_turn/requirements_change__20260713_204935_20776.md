# Qwen 3-Next 80B Thinking — multi_turn/requirements_change

- model_id: `qwen/qwen3-next-80b-a3b-thinking`
- success: True  | final: 4.73 | quality: 4.0
- latency_total: 13.538s | tokens_per_second: 151.3
- input_tokens: 248 | output_tokens: 2048
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, abordando el cambio de requisitos y proporcionando pasos detallados para implementar el flujo de trabajo en N8N, aunque hay cierta indecisión sobre el formato de salida del campo 'from' en el nodo de Gmail.

## Respuesta completa

Okay, let me see. The user changed their mind from Google Sheets to Notion, and they want to filter emails with "propuesta" or " cotizacion" in the subject, plus a Slack notification. Let me think step by step.

First, the workflow start. They need a Gmail trigger. But the Gmail trigger in N8N usually has a "new email" trigger. But they also need to filter on the subject. Wait, N8N's Gmail node might have a way to filter. Let me recall. When you set up the Gmail trigger, there's an option for "Search query" or "Filters". So maybe in the trigger node, I can set a search query to only get emails with "propuesta" or " cotizacion" in the subject. That way, the workflow only processes those specific emails.

So the first node is Gmail Trigger. The configuration should have a search query like "subject:(propuesta cotizacion)" but wait, the syntax for Gmail's search operators. To search for "propuesta" OR " cotizacion" in the subject, maybe "subject:propuesta OR subject:cotizacion". but in N8N, when you set the search query, you can use Gmail's operators. So in the trigger node, under "Search query", I can put "subject:propuesta OR subject:cotizacion". That way, the trigger only activates for emails with either word in the subject.

Then, next step is to extract the data. The user wants the sender's data, so probably the name and email address. In the Gmail node, after the trigger, the output includes the email data. So in N8N, the Gmail node's "new email" trigger outputs a JSON with fields like from, to, subject, body, etc. The 'from' field is usually an object with name and email. Or sometimes a string. So in the function node, I need to parse that.

Wait, the Gmail node's "from" field might be a string like "Name <email@example.com>". So in the function node, I can split that to get name and email. Or maybe the Gmail node already has parsed fields. Let me check. In N8N, when using the Gmail node, the "from" field is typically an array or an object. Wait, no. Let me think: in N8N's Gmail node, the "from" field is a string. For example, "John Doe <john@example.com>". So to split that, in a function node, I can use a regex or split. But maybe N8N's Gmail node has a "from" with name and email as separate fields. Wait, no. Let me check the N8N documentation for the Gmail node.

Looking at N8N's Gmail node documentation: the "new email" trigger output includes a "from" field which is a string in the format "Name <email@example.com>". So to extract name and email, you need to parse that. Alternatively, there's a "from.email" and "from.name" in some cases. Wait, no. Let me see. Actually, in N8N's Gmail node, the "from" field is an object with "name" and "email" properties. Wait, no. Let me check.

Wait, in N8N's Gmail node, when you receive an email, the "from" is a string. For example, "Sender Name <sender@example.com>". But maybe there's a separate "fromName" and "fromEmail" field. Let me confirm. 

Actually, in the N8N Gmail node, the from field is a string. But in some cases, the node might parse it. Wait, no. Let me check the actual output. For example, if I have a Gmail node, when it triggers, the item's data might have:

{
  "from": "John Doe <john@example.com>",
  "subject": "...",
  "date": "..."
}

So to parse that, in a function node, I can split the from string. For example, using a regex to extract name and email. or using string split. like:

 const from = item.json.from;
 const name = from.split('<')[0].trim();
 const email = from.split('<')[1].slice(0, -1);

But in N8N, in the function node, you can write a JavaScript function to process that.

Alternatively, maybe the Gmail node already has parsed fields. Wait, I think in some versions, the Gmail node might have "fromName" and "fromEmail" as separate fields. Let me check the N8N documentation for the Gmail node.

Looking at the N8N docs: for the Gmail node's " new email" trigger, the output fields include "from" as a string, "fromName" as a string, "fromEmail" as a string. Wait, no. Let me check. 

Actually, in the current N8N version (as of 2023), the Gmail node's " new email" trigger output has:

- from: string (e.g., "Name <email@example.com>")
- fromName: string (extracted name)
- fromEmail: string (extracted email)

Wait, I'm not sure. Let me check. If I go to the N8N docs for the Gmail node: 
https://docs.n8n.io/integrations/builtin nodes-reference nodes/n8n-nodes-base.gmail/

Looking at the " new email" trigger section. Under "Output Example", the from field is an object with name and email. Wait, no. Let me see. The example shows:

"from": "John Doe <john@example.com>",
"fromName": "John Doe",
"fromEmail": "john@example.com",

Wait, no. In the example, the fields are:

"from": "John Doe <john@example.com>",
"fromName": "John Doe",
"fromEmail": "john@example.com",
"subject": "...",

Yes, I think that's correct. So in the Gmail node output, there are separate fields for fromName and fromEmail. So maybe I don't need a function node to parse. But to confirm, in the Gmail node's configuration, when you set up the trigger, it automatically parsed fromName and fromEmail. So in the node's output, you can directly use those fields.

So in that case, the next step after the Gmail trigger is to extract the needed data: fromName, fromEmail, subject, date. But the subject is already in the output, and the date as well. So perhaps the function node isn't necessary for parsing, but maybe to format the data for Notion.

Wait, but the user wants to save to Notion. Notion has a specific API structure. So the Notion node in N8N requires certain parameters. For example, when creating a new page, you need to specify the database ID, and then the properties. So the workflow would have a Notion node to add a new page to a database.

So steps:

1. Gmail Trigger with search query for "subject:propuesta OR subject:cotizacion" (or "subject:propuesta OR subject cotizacion" but need to check syntax). Wait, in Gmail's search, it's "subject:propuesta OR subject:cotizacion". So in the Gmail node's "Search query" field, I can put "subject:propuesta OR subject:cotizacion".

2. Then, the Gmail node will output the email. Then, we need to extract the necessary data. but as per N8N's Gmail node, the fromName and fromEmail are available. So the next step is a Notion node. But first, perhaps a function node to format the data for Notion's required fields.

Notion's API expects a database item with properties. For example, if the database has "Sender Name", "Sender Email", "Subject", "Received Date" fields, then each property needs to be set.

In the Notion node, when adding a new page to a database, you need to specify the database ID, and then the properties. Each property corresponds to a field in the database. So for each property, you need to specify the type (e.g., rich text, title, etc.).

So in the Notion node, under "Property Mapping", you would map the email fields to the Notion's database fields. For example:

- "Sender Name" ( property in Notion) would be the fromName from the Gmail node.

- "Sender Email" ( property in Notion) would be fromEmail.

- "Subject" ( property in Notion) would be the subject.

- "Received Date" ( property in Notion) would be the date from the email.

But the date in Gmail node is in a string format. Notion might expect a specific format. But Notion's date property can handle ISO 8601. The Gmail node's "date" field is probably already in a standard format. But I need to check. For example, the date might be "Mon, 1 Jan 2023 12:00:00 +0000". Notion expects a date in ISO 8601. So perhaps a function node to convert the date to a proper ISO string.

Alternatively, in the Notion node, maybe the date can be automatically parsed. But to be safe, a function node to format the date.

Wait, N8N's Notion node may have a date field. Let me check. In the Notion node, when you add a new page, in the "Property Mapping", for a date property, you can provide a date string in ISO 860 format. So the date from the Gmail node needs to be converted. For example, the Gmail node's "date" field is