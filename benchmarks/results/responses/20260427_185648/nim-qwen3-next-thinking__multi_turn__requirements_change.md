# Qwen 3-Next 80B Thinking (NIM) — multi_turn/requirements_change

- model_id: `qwen/qwen3-next-80b-a3b-thinking`
- success: True  | final: 6.67 | quality: 7.64
- latency_total: 22.656s | tokens_per_second: 90.4
- input_tokens: 249 | output_tokens: 2048
- judge_score: 4.2 | justificación: 

## Respuesta completa

Okay, the user changed their mind from Google Sheets to Notion. They also want to filter emails with 'propuesta' or 'cotizacion' in the subject and send a Slack notification. Let me think through this.

First, the workflow steps. Start with Gmail trigger. Then filter the emails based on the subject containing those keywords. Then extract the data, send to Notion, and also notify Slack.

Wait, the user said "filtra solo los emails que tengan la palabra 'propuesta' o 'cotizacion' en el asunto". So the filter should check if the subject includes 'propuesta' or 'cotizacion'. Maybe using a filter node or a function node to check.

But in N8N, you can use the Gmail trigger's filter options. Wait, the Gmail trigger has a "Search Query" option. So maybe set up the trigger to only get emails with subject containing those words. Like subject:propuesta OR subject:cotizacion. That way, the trigger itself filters them. That's better than adding a filter node later. So when configuring the Gmail trigger, in the search query field, put "subject:(propuesta OR cotizacion)".

Then, once the email is received, extract the data: sender's name, email, subject, date. Then save to Notion. Then send a Slack notification.

For Notion, need to set up a database. The user needs to have a Notion database set up with the right properties. So the workflow would have a Notion node to create a page in that database.

Also, a Slack node to send a notification. Maybe the Slack message should include the subject, sender, and maybe a link to the Notion page? Or just the basic info.

Let me outline the steps:

1. Gmail Trigger: Search query to filter subject with propuesta or cotizacion. So in the trigger setup, under "Search Query", write "subject:(propuesta OR cotizacion)".

2. Then, extract data from the email. The Gmail trigger node will output the email details. So maybe need to parse the sender's email and name. In N8N, the Gmail trigger returns the sender's email in the 'from' field. But sometimes the 'from' field might be formatted as "Name <email@domain.com>", so need to parse that.

So perhaps a Function node to split the 'from' field into name and email. For example:

- If the 'from' is "John Doe <john@example.com>", then extract name as "John Doe" and email as "john@example.com".

Alternatively, the Gmail trigger might have separate fields for 'senderName' and 'senderEmail'. Wait, let me check. In N8N's Gmail trigger, the data includes 'from' which is usually a string like "Name <email>", but there might also be 'sender' or 'from' with structured data. Wait, looking at the N8N documentation for Gmail trigger: the 'from' field is a string that can be parsed. But maybe there's a 'sender' object. Hmm, perhaps better to use a function node to process the 'from' string.

So in the Function node, take the 'from' field, split it. For example:

const from = $json.from;
const nameMatch = from.match(/^(.*)<(.*)>/);
if (nameMatch) {
  return {
    senderName: nameMatch[1].trim(),
    senderEmail: nameMatch[2]
  };
} else {
  return {
    senderName: from,
    senderEmail: from
  };
}

But maybe the 'from' field in N8N's Gmail trigger already has 'name' and 'address'? Let me check. Actually, in N8N, when using the Gmail trigger, the 'from' field is an object with 'name' and 'email' properties. Wait, yes, according to the N8N docs for Gmail trigger, the 'from' field is structured as { name: string, email: string }. So maybe you don't need to parse it. For example, the trigger node's output will have 'from.name' and 'from.email' as separate fields. So that's good.

So the data needed is:

- senderName: from.name

- senderEmail: from.email

- subject: subject

- date: date (the email's date)

Then, save to Notion. For Notion, need to create a page in a database. So the Notion node would require the database ID and the properties to set. The user needs to have a Notion database set up with properties like Name, Email, Subject, Date, etc.

So in the Notion node, for each property, map the data from the previous steps. For example, Name = from.name, Email = from.email, Subject = subject, Date = date.

Then, the Slack node. The Slack message should be a notification. Maybe include the subject, sender's name, and a link to the Notion page. But first, the Notion node creates the page, so the Notion node's output might have the URL of the created page. Then in the Slack message, include that URL.

Wait, the Notion node for creating a page returns the page's URL in the response. So in the Slack node, you can reference that URL.

So the workflow steps would be:

1. Gmail Trigger (with search query)

2. Notion node to create page (but wait, maybe the Notion node needs to come after extracting data, but since the Gmail trigger already provides the data, maybe the Notion node can take the data directly)

Wait, the Gmail trigger node outputs the email data. So for the Notion node, the data needed is:

- Title (maybe the subject?), but Notion database properties need to be mapped.

Assuming the Notion database has a title field and other properties. So in the Notion node, for the 'Title' field, use the subject. Then other fields like Sender Name, Sender Email, Date.

Alternatively, the Notion database might have specific property names. The user needs to set up the database with the correct properties.

But for the workflow, the Notion node will have to map each property. So the steps:

- After the Gmail trigger, the data is in the node's output. Then, send to Notion node which creates a page in the specified database with the properties.

Then, the Slack node sends a message. The Slack message could have a message like:

"New proposal/cotización received!

Subject: [subject]

From: [senderName] ([senderEmail])

View in Notion: [Notion page URL]"

So the Slack node would use the data from the previous steps.

So the workflow steps in order:

1. Gmail Trigger: Set up with search query "subject:(propuesta OR cotizacion)" to only trigger on those emails.

2. Notion node: Create a page in the specified database. Map the properties:

- Title: subject

- Sender Name: from.name

- Sender Email: from.email

- Date: date (maybe format the date nicely)

Wait, but the Notion database properties need to be defined. For example, if the database has a 'Subject' field, then use subject; 'Sender Name' field, etc.

But the user needs to set up the database first. So in the workflow, the Notion node's configuration would have the database ID and the properties.

3. Slack node: Send a message with the relevant info, including the Notion page URL.

But wait, the Notion node might return the page URL in its output. So after the Notion node creates the page, the output includes the URL. Then the Slack node can use that.

So the order would be:

Gmail Trigger -> Notion node (create page) -> Slack node.

Yes, that makes sense. Because the Slack message needs the Notion page URL, which is generated after creating the page.

So the steps:

- Trigger on Gmail with search query.

- Then Notion node to create the page. The Notion node's output will have the page's URL.

- Then Slack node uses that URL and other data.

So in the Slack node, the message can include the URL from the Notion node's output.

Now, configuring each node.

First, Gmail Trigger:

- Authentication: need to connect Gmail account.

- Search Query: "subject:(propuesta OR cotizacion)".

- The trigger will fire when an email matches this.

Then, the data from the trigger includes 'from', 'subject', 'date', etc.

Next, Notion node:

- Need to have a Notion integration set up. The user needs to create a Notion integration, get the token, and add it to N8N's Notion credentials.

- Then, the Notion node requires the database ID (which is part of the database URL, like the part after the last slash).

- In the node configuration, select "Create Page" operation.

- Then, for each property in the database, map the data. For example:

  - Title: {{ $json.subject }}

  - Sender Name: {{ $json.from.name }}

  - Sender Email: {{ $json.from.email }}

  - Date: {{ $json.date }}

But need to check what the date format is. The Gmail trigger returns the date as a string, maybe in a standard format. But Notion might need it in a specific format. However, the Date property in Notion can be a date/time type, so the format might need to be ISO or something. But N8N's Notion node might handle it, or maybe the user needs to format the date in a function node first.

Alternatively, in the Notion node, the date field might expect a specific format. So maybe a Function node before Notion to format the date.

But maybe the Notion node can