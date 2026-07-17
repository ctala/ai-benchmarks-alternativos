# MiMo-V2.5 Pro — multi_turn/requirements_change

- model_id: `xiaomi/mimo-v2.5-pro`
- success: True  | final: 4.31 | quality: 4.0
- latency_total: 27.789s | tokens_per_second: 73.7
- input_tokens: 244 | output_tokens: 2048
- judge_score: 3.6 | justificación: 

## Respuesta completa

.We are going to create a workflow with the following steps:

1. Gmail Trigger: to start the workflow when a new email arrives.
 2. Filter: We will use a Function node (or an If node) to check the subject for the words 'propuesta' or 'cotizacion'.
 3. If the condition is met, we will extract the required data (sender name, email, subject, date).
 4. Then, we will create a page in Notion with the extracted data.
 5. Finally, send a notification to Slack.

 Let's break down each step:

 Step 1: Gmail Trigger
   - We'll set up the Gmail Trigger to watch for new emails.

 Step 2: Filtering by subject
   - We can use a Function node to check the subject. Alternatively, we can use an If node, but since we need to do a case-insensitive check for two words, a Function node might be easier.

 Step 3: Extract data
   - We can use a Function node to extract the data from the email object.

 Step 4: Create a Notion page
   - We'll use the Notion node to create a page in a database. We need to set up the Notion integration and have the database ID.

 Step 5: Slack notification
   - We'll use the Slack node to send a message to a channel.

 Let's design the workflow:

 1. Gmail Trigger (Node Type: Gmail Trigger)
 2. Function (to check the subject and extract data) - We'll call it "Filter and Extract"
 3. Notion (to create a page)
 4. Slack (to send a message)

 However, note that the Function node can both filter and extract data. We can have it output only if the condition is met, or we can have an If node after. But to keep it simple, we can do:

   Gmail Trigger -> Function (Filter and Extract) -> Notion -> Slack

 But what if the email does not contain the words? We don't want to proceed. So in the Function node, we can throw an error or return nothing? Actually, we can use an If node after the Function to check if the data was extracted. Alternatively, we can use the Function node to set a flag and then use an If node.

 Alternatively, we can use two nodes:

   Gmail Trigger -> If (subject contains 'propuesta' or 'cotizacion') -> Extract Data -> Notion -> Slack

 But the If node in N8N doesn't support multiple conditions easily for checking a string contains. We can use the Function node for that.

 Let me propose:

   Gmail Trigger -> Function (Check subject and extract data) -> If (check if data exists) -> Notion -> Slack

 However, to avoid unnecessary nodes, we can have the Function node return null if the condition is not met, and then the If node will check for the existence of the data.

 Alternatively, we can use the Function node to set the data and then use the If node to check if the subject condition was met. But note: we want to extract the data only if the condition is met.

 Let's do:

   Step 1: Gmail Trigger
   Step 2: Function node that:
        - Checks if the subject contains 'propuesta' or 'cotizacion' (case insensitive)
        - If yes, extract the data and return an object with the fields: senderName, senderEmail, subject, date.
        - If no, return an empty object or a flag to indicate no data.

   Step 3: If node that checks if the object from the Function node has the required data (e.g., if senderName exists).

   Step 4: Notion node to create a page.

   Step 5: Slack node to send a message.

 However, we can also combine the If condition in the Function node by returning null and then using an If node that checks for null.

 Alternatively, we can use the Function node to throw an error if the condition is not met, but that might not be the best.

 Let me write the Function node code:

 We assume the input from Gmail Trigger is in the variable `item[0].json`.

 Example of what the Gmail Trigger gives us:

   item[0].json has:
     - subject     - from (string like "Name <email@example.com>")
     - date

 We need to extract the name and email from the from field.

 Let's write the Function node code:

```javascript
// Get the email object from the input
const email = items[0].json;

// Check if the subject contains 'propuesta' or 'cotizacion' (case insensitive)
const subject = email.subject || '';
const lowerSubject = subject.toLowerCase();
if (!lowerSubject.includes('propuesta') && !lowerSubject.includes('cotizacion')) {
  // If condition not met, return null (or we can return an empty object)
  return null;
}

// Extract sender name and email from the from field
const from = email.from || '';
// The from field is usually in the format "Name <email@example.com>"
let senderName = '';
let senderEmail = '';
const match = from.match(/^(.*?)\s*<(.+?)>$/);
if (match) {
  senderName = match[1].trim();
  senderEmail = match[2].trim();
} else {
  // If there's no angle brackets, then the whole string is the email and the name is empty
  senderEmail = from.trim();
}

const date = email.date || '';

return [{
  json: {
    senderName,
    senderEmail,
    subject,
    date
  }
}];
```

 Then, in the If node, we check if the output from the Function node is not null and has data.

 But note: the Function node returns an array. We can set the If node to check if the first element of the array has the data.

 Alternatively, we can change the Function node to return an object with a property, say `data`, and then check for that.

 However, the If node in N8N can check the output of the previous node. We can set the If node to check if the output of the Function node is not empty and has the required fields.

 But note: the Function node returns an array. We can set the If node to check if the array is not empty and the first element has the required fields.

 However, if we return null from the Function node, the output will be null, and the If node can check for null.

 Let me adjust the Function node to return null if condition not met, otherwise return the array with the data.

 Then in the If node, we can check:

   - Condition: "Output of the Function node is not null and the array has at least one item."

 But the If node doesn't have a way to check for array length easily. We can use an expression.

 Alternatively, we can change the Function node to return an empty array if condition not met.

 Then the If node can check: `{{ $json.length }} > 0` and `{{ $json[0].senderName }}` exists.

 However, to keep it simple, let's return null when condition not met, and then in the If node, we can check if the output is null.

 But note: the If node in N8N expects a condition on the output of the previous node. We can set:

   Condition: "Output of the Function node is not null"

 Then, if the condition is met, we proceed to Notion.

 Alternatively, we can use the Function node to throw an error and then use an Error Trigger, but that's more complicated.

 Let's do:

   Gmail Trigger -> Function (as above, returns null or array with data) -> If (check if output is not null) -> Notion -> Slack

 In the If node, we set the condition to check if the output of the Function node is not null.

 How to set the If node condition:

   We can set:
     - Value1: `{{ $json }}`
     - Operation: "is not null"

 But note: if the Function node returns null, then `$json` is null. So this condition will work.

 However, if the Function node returns an array, then `$json` is an array, which is not null.

 So this condition is safe.

 Then, after the If node, we have the data in the output of the Function node (which is an array). We can access the first element.

 In the Notion node, we can set the properties to:

   - Title: subject   - Other properties: senderName, senderEmail, date

 We assume you have a Notion database with these properties.

 Let's set up the Notion node:

   - Operation: Create a page in a database.
   - Database ID: [Your database ID]
   - Map the fields:

 Title (or whatever your title field is): subject
        Sender Name: senderName
        Sender Email: senderEmail
        Date: date

 Then, the Slack node:

   - Channel: [Your channel]
   - Text: A message like: "New email with subject [subject] from [senderName] ([senderEmail]) on [date] has been added to Notion."

 Let's write the complete workflow structure:

 1. Gmail Trigger
 2. Function (as above)
 3. If (check if output of Function is not null)
 4. Notion (create page with data from Function node)
 5. Slack (send message with data from Function node)

 However, note that the If node does not change the data. So the data from the Function node (the array) is passed to the Notion node and then to the Slack node.

 We can access the data in the Notion node and Slack node as `$json[0].senderName