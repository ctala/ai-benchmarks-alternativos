# DeepSeek V4 Flash 0731 — content_verificable/audiencia_que_ya_sabe

- model_id: `deepseek/deepseek-v4-flash-0731`
- success: True  | final: 9.4 | quality: 10.0
- latency_total: 6.237s | tokens_per_second: 115.6
- input_tokens: 180 | output_tokens: 721

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**Subject: The "Success" Lie**

Your workflow just ran. Green checkmark. "Success." But the database is empty, the email never sent, and the API call was never made. Sound familiar?

Here's the dirty secret: **"success" in n8n only means the workflow finished without an unhandled error.** It says nothing about whether it actually did what you intended.

Three usual suspects:

1. **Webhook response fires too early.** You return a 200 from the first node, and the rest of the workflow runs asynchronously. If that later node fails silently (or you've got "Continue on Fail" checked), you'll see a green checkmark on the webhook node while the rest is a dumpster fire.

2. **Conditional branches that skip everything.** Your IF node routes to an empty branch or a "Do Nothing" node. The workflow completes, but no side effects occur. Success, technically.

3. **Empty inputs.** A loop over zero items, a filter that removes everything, a lookup that returns `null`. No error, no action.

**How to catch it:**

- Go to **Executions** and actually inspect the data flow. Don't trust the summary view.
- Turn on **"Save Successful Executions"** and **"Save Error Executions"** for every production workflow.
- Add a **Code node** at the end of each branch that logs the output or throws if the result is empty.
- Set up **alerts** via Slack/Telegram for "successful" executions that produce zero output.

Your workflow's job isn't to finish. It's to *do something*. Audit your critical workflows today—before the next "success" costs you a client.

— [Your Name]