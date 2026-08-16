# Nemotron 3 Super — tool_calling/multi_tool_sequential

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 5.91 | quality: 5.98
- latency_total: 12.569s | tokens_per_second: 10.1
- input_tokens: 894 | output_tokens: 127
- judge_score: 3.2 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito que hagas lo siguiente:
1. Crea una tarea urgente titulada 'Revisar contrato cliente ABC' con fecha limite 2026-05-10
2. Envia un email a legal@empresa.com con asunto 'Contrato ABC - Revision urgente' explicando que necesitamos revision antes del 10 de mayo


## Respuesta completa

I need to create a task and send an email. Let me start with creating the task first. The task should be urgent, titled "Revisar contrato cliente ABC", with due date 2026-05-10. Priority should be "urgent". I'll use the create_task function.