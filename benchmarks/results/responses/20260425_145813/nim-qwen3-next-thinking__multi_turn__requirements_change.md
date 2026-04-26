# Qwen 3-Next 80B Thinking (NIM) — multi_turn/requirements_change

- model_id: `qwen/qwen3-next-80b-a3b-thinking`
- success: True  | final: 6.51 | quality: 6.88
- latency_total: 17.97s | tokens_per_second: 114.0
- input_tokens: 249 | output_tokens: 2048
- judge_score: 4.2 | justificación: 

## Respuesta completa

Okay, the user changed their mind. Originally they wanted Gmail to Google Sheets, but now it's Notion, filter for 'propuesta' or 'cotizacion' in the subject, and send a Slack notification. Let me think through this step by step.

First, the workflow needs to start with a Gmail trigger. The trigger should check for new emails. But how do I filter for specific words in the subject? Maybe the Gmail trigger has a filter option. Wait, in N8N, the Gmail node might have a search query parameter. So when setting up the trigger, instead of just "new email", use a search query like "subject:(propuesta OR cotizacion)".

Then, once the email is received, extract the sender's data. The sender's info is usually in the 'from' field. Maybe the Gmail node already provides that. But to be safe, maybe a Function node to parse the 'from' field to get name and email. But sometimes the 'from' field might have "Name <email>", so splitting that could be necessary.

Next, save to Notion. So need to set up a Notion node. But Notion requires a database. The user probably needs to have a Notion database set up with specific properties. So the workflow should create a new page in the database with the extracted data. The fields would be: sender name, sender email, subject, date, maybe the email body or other details.

Then, send a Slack notification. So after saving to Notion, trigger a Slack message. Maybe the Slack node can be set to send a message to a channel with the details of the email.

Wait, but the user wants to filter only emails with 'propuesta' or 'cotizacion' in the subject. So the Gmail trigger should have a search query. Let me check how N8N's Gmail node handles that. In the Gmail trigger node, there's a "Search Query" field where you can input "subject:propuesta OR subject:cotizacion". That should filter only those emails.

Then, for extracting data: the Gmail node returns the email data, including from, subject, date, etc. Maybe the 'from' field is a string like "John Doe <john@example.com>". So in a Function node, split that to get name and email. Alternatively, maybe the Gmail node already separates them, but sometimes it's in a single string. So the Function node could process it.

For Notion, the node would need to connect to the Notion API. The user needs to have a Notion integration set up with the database. The database should have properties like "Sender Name", "Sender Email", "Subject", "Date", etc. So when adding a new page, map the extracted fields to those properties.

Then Slack notification: maybe the Slack node can be configured to send a message to a specific channel. The message could include the subject, sender, and maybe a link to the Notion page. But the Notion page might not have a public link, so maybe just the details in the message.

Wait, the Slack notification should be sent when an email is processed, so after the Notion node. So the flow would be:

Gmail trigger (with search query) → Extract data (Function node) → Save to Notion → Slack notification.

But maybe the Slack notification can be done before saving to Notion, but probably better to do after to confirm it's saved.

Let me outline the steps:

1. Gmail Trigger node: Set up with search query "subject:(propuesta OR cotizacion)". Maybe the query should be "subject:propuesta OR subject:cotizacion" to cover both.

Wait, in Gmail search syntax, it's "subject:propuesta OR subject:cotizacion". So in the search query field of the Gmail node, input that.

2. Then, the Gmail node will return the email details. The 'from' field might be a string. So a Function node to parse it. For example:

const from = items[0].json.from;
// Split the string to get name and email
// Example: "John Doe <john@example.com>"
const nameMatch = from.match(/(.+?)\s*<(.+?)>/);
if (nameMatch) {
    const name = nameMatch[1].trim();
    const email = nameMatch[2];
    return { name, email };
} else {
    // If it's just the email without name
    return { name: from, email: from };
}

But maybe the Gmail node already provides separate fields for name and email. Let me check. In N8N's Gmail node documentation, when getting emails, the 'from' field is usually an object with name and address. Wait, maybe the Gmail node's output for 'from' is structured. Let me check: in N8N, when using the Gmail trigger, the 'from' field might be an object with 'name' and 'address'. So perhaps no need for a Function node. But maybe not. Let me confirm.

Actually, when you use the Gmail trigger node in N8N, the 'from' field is typically a string like "John Doe <john@example.com>". So the Function node is needed to split it. Alternatively, maybe the node has a 'from' object. Let's see. In the N8N docs for Gmail node: the output for the 'from' field is a string. So yes, likely needs parsing.

So the Function node would process the 'from' string.

Then, for Notion: the Notion node in N8N requires a database ID and the properties to set. The user must have a Notion database with properties like "Sender Name", "Sender Email", "Subject", "Date", etc.

So the Notion node would create a new page in the database with these properties.

Then Slack: the Slack node would send a message to a channel. The message could include the subject, sender name, maybe a link to the Notion page. But for the Notion page link, the Notion node might return the page URL. So perhaps in the Notion node, the output includes the page ID or URL. Then pass that to Slack.

But the Slack node might need to be configured to send a message with the details.

So the workflow steps:

1. Gmail trigger with search query.

2. Function node to parse sender's name and email.

3. Notion node to create a new page in the database.

4. Slack node to send a notification with the data.

But maybe the Slack node can come before Notion, but probably better after to confirm it's saved. But even if Notion fails, Slack could still send, but maybe the user wants to know it was processed. So perhaps after Notion.

Now, let's outline each node configuration.

First, Gmail Trigger node:

- Action: "Watch for new emails"

- Search query: "subject:(propuesta OR cotizacion)" – wait, actually, in Gmail's search syntax, it's "subject:propuesta OR subject:cotizacion". So in the search query field of the N8N Gmail node, input that.

Alternatively, maybe "subject:propuesta OR subject:cotizacion" is correct.

Second, Function node:

Input: the email data from Gmail.

Output: extract name and email from 'from' string.

Third, Notion node: Create a page in a specific database. The user needs to have the database ID and set up the properties.

Fourth, Slack node: Send a message to a channel. The message could be something like:

"New proposal/cotizacion received!

From: {sender name} ({sender email})

Subject: {subject}

Link to Notion page: {Notion page URL}"

But the Notion node's output may include the URL of the created page. So in the Slack node, reference that.

But how does the Notion node return the URL? In N8N, when creating a page in Notion, the output includes 'id' and possibly 'url' as part of the response. So yes, the Notion node's output would have a 'url' field which can be used in Slack.

So the Slack node can take the Notion URL from the previous node's output.

Now, the steps to set up each node in N8N:

1. Gmail Trigger:

- Select "Watch for new emails" as the action.

- In "Search Query", enter "subject:(propuesta OR cotizacion)" but check the correct syntax. Maybe "subject:propuesta OR subject:cotizacion" is better. Because in Gmail search, it's "subject:propuesta OR subject:cotizacion".

Yes, that's the correct syntax.

2. Function node:

- Use JavaScript to parse the 'from' field.

Example code:

const fromString = items[0].json.from;
let name = '';
let email = '';

// Check if the string contains '<' and '>'
if (fromString.includes('<') && fromString.includes('>')) {
    const [namePart, emailPart] = fromString.split('<');
    name = namePart.trim();
    email = emailPart.replace('>', '').trim();
} else {
    name = fromString;
    email = fromString;
}

return [{
    json: {
        senderName: name,
        senderEmail: email,
        subject: items[0].json.subject,
        date: items[0].json.date,
        body: items[0].json.text // maybe body is needed?
    }
}];

Wait, but the items[0].json would have all the email data. So the Function node should extract the necessary fields.

But the user might want to save the sender name, email, subject, date, maybe the body.

But for Notion, the properties would need to be set.

But the exact fields depend on the Notion database structure. So perhaps in the Function node,