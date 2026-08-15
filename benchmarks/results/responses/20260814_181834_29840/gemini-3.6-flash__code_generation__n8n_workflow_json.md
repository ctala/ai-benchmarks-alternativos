# Gemini 3.6 Flash — code_generation/n8n_workflow_json

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 5.29 | quality: 5.23
- latency_total: 10.477s | tokens_per_second: 195.1
- input_tokens: 116 | output_tokens: 2044
- judge_score: 2.4 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Genera un workflow de N8N en JSON que:
1. Se active con un webhook POST
2. Extraiga el campo "email" y "message" del body
3. Use un nodo de IA (OpenAI) para clasificar el mensaje como "soporte", "ventas" o "otro"
4. Segun la clasificacion, envie el email a un canal de Slack diferente:
   - soporte -> #support
   - ventas -> #sales
   - otro -> #general

Dame el JSON completo del workflow.


## Respuesta completa

Aquí tienes el código JSON completo para importar directamente en tu instancia de **n8n**. 

Este workflow:
1. Recibe un `POST` en la URL del **Webhook**.
2. Envía el mensaje a **OpenAI** (usando `gpt-4o-mini` con temperatura 0 para máxima precisión) obligándolo a responder únicamente: `soporte`, `