# Seed 2.0 Code — tool_calling/multi_tool_sequential

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 7.8 | quality: 8.5
- latency_total: 7.605s | tokens_per_second: 54.8
- input_tokens: 864 | output_tokens: 417
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una estructura bien organizada que detalla el uso de las funciones requeridas. Ofrece utilidad práctica al describir exactamente cómo se deben ejecutar las tareas, aunque no profundiza más allá de lo necesario para la tarea.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito que hagas lo siguiente:
1. Crea una tarea urgente titulada 'Revisar contrato cliente ABC' con fecha limite 2026-05-10
2. Envia un email a legal@empresa.com con asunto 'Contrato ABC - Revision urgente' explicando que necesitamos revision antes del 10 de mayo


## Respuesta completa

Let's analyze what the user needs. They want two things:

1. Create an urgent task titled 'Revisar contrato cliente ABC' with a due date of 2026-05-10
2. Send an email to legal@empresa.com with the subject 'Contrato ABC - Revision urgente' explaining that a review is needed before May 10th

First, for the task creation, I need to use the create_task function. The parameters required are:
- title: 'Revisar contrato cliente ABC'
- due_date: '2026-05-10'
- priority: 'urgent'
- assignee: Not specified, so it's optional

Second, for sending the email, I need to use the send_email function with parameters:
- to: 'legal@empresa.com'
- subject: 'Contrato ABC - Revision urgente'
- body: 'Necesitamos que revisen el contrato del cliente ABC antes del 10 de mayo de 2026. Es una revisión urgente.'

I should call both functions in sequence to fulfill the user's request.