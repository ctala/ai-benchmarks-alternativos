# Nemotron 3 Nano Omni 30B-A3B Reasoning (NIM) — multi_turn/requirements_change

- model_id: `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning`
- success: True  | final: 6.38 | quality: 5.24
- latency_total: 4.685s | tokens_per_second: 261.7
- input_tokens: 271 | output_tokens: 1226
- judge_score: 2.6 | justificación: 

## Respuesta completa

[{"type":"text","text":"Para crear el workflow en n8n sigue estos nodos:\n1️⃣ **Gmail Trigger** (nuevo correo).\n2️⃣ **Filter**: usa la expresión `contains($json[\"subject\"], \"propuesta\") or contains($json[\"subject\"], \"cotizacion\")` para que solo pase los correos con esos términos.\n3️⃣ **Function**: extrae los datos del remitente (email y nombre), asunto y fecha. Código de ejemplo:\n```javascript\nreturn [\n  {\n    json: {\n      sender: $json[\"from\"][\"email\"],\n      name: $json[\"from\"][\"name\"],\n      subject: $json[\"subject\"],\n      date: $json[\"date\"]\n    }\n  }\n];\n```\n4️⃣ **Notion**: crea una página en tu base de datos (elige la DB, mapea los campos *Name*, *Email*, *Subject*, *Date*).\n5️⃣ **Slack**: envía una notificación al canal que prefieras, por ejemplo:\n`Nueva cotización/propuesta recibida: {{sender}} – {{subject}}`.\n\nConfigura los credenciales OAuth2 para Gmail, el token de Notion y la cuenta o webhook de Slack en n8n. Con estos nodos tendrás el flujo completo."}]