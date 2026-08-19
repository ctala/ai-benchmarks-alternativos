# Seed 2.0 Code — tool_calling/multi_tool_sequential

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 5.15 | quality: 5.0
- latency_total: 15.277s | tokens_per_second: 60.7
- input_tokens: 864 | output_tokens: 927

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito que hagas lo siguiente:
1. Crea una tarea urgente titulada 'Revisar contrato cliente ABC' con fecha limite 2026-05-10
2. Envia un email a legal@empresa.com con asunto 'Contrato ABC - Revision urgente' explicando que necesitamos revision antes del 10 de mayo


## Respuesta completa

Got it, let's tackle this user's request step by step. First, they want two things: create an urgent task and send an email. 

First, the task. The parameters for create_task are title, priority, due_date, and assignee (wait, no, required are title and priority. The due_date is optional? Wait no, looking at the function definition: create_task's required parameters are title and priority. But the user specified due_date 2026-05-10, so we should include that too. The title is 'Revisar contrato cliente ABC', priority is 'urgent', due_date is '2026-05-10'. Assignee isn't mentioned, so we can omit that since it's not required.

Then the email. send_email requires to, subject, body. To is legal@empresa.com, subject is 'Contrato ABC - Revision urgente', body is 'necesitamos revision antes del 10 de mayo'. Wait, maybe make the body a bit clearer? The user said "explicando que necesitamos revision antes del 10 de mayo", so the body can be that, but maybe phrase it properly. Like "Necesitamos que revisen el contrato del cliente ABC antes del 10 de mayo de 2026, por favor." But the user's exact words are "explicando que necesitamos revision antes del 10 de mayo", so we can use that as the body, maybe adjust for clarity.

Now, we need to call both functions. Let's structure the tool calls. First create_task, then send_email. Wait, but the order might not matter, but let's do them as per the user's request order.

Check parameters for create_task: title is 'Revisar contrato cliente ABC', priority 'urgent', due_date '2026-05-10'. That's all required plus the due_date as specified.

For send_email: to 'legal@empresa.com', subject 'Contrato ABC - Revision urgente', body 'Necesitamos la revisión del contrato del cliente ABC antes del 10 de mayo de 2026.' Wait, the user said "explicando que necesitamos revision antes del 10 de mayo", so maybe keep it as per that, but make it a complete sentence. Like "Necesitamos que realicen la revisión del contrato del cliente ABC antes del 10 de mayo." That's clear.

Now, format the tool calls correctly. Each function in its own <tool_call> tag? Wait no, wait the example: if multiple functions, it's an array. Wait, looking at the system prompt: "If you want to call multiple functions, you can put them in a single JSON array." Oh right, so the tool calls should be an array of objects.

Wait let's confirm the function parameters again. create_task: required are title and priority. The user provided due_date, so we include that. Assignee is not mentioned, so we don't include it since it's not required.

So the create_task parameters: {"title": "Revisar contrato cliente ABC", "priority": "urgent", "due_date": "2026-05-10"}

send_email parameters: {"to": "legal@empresa.com", "subject": "Contrato ABC - Revision urgente", "body": "Necesitamos la revisión del contrato del cliente ABC antes del 10 de mayo."}

Now, structure the tool calls as an array. Let's make sure the JSON is valid.