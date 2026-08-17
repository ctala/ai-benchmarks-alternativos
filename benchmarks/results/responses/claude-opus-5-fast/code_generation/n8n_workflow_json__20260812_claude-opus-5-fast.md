# Claude Opus 5 Fast — code_generation/n8n_workflow_json

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 4.25 | quality: 4.38
- latency_total: 9.391s | tokens_per_second: 218.1
- input_tokens: 175 | output_tokens: 2048
- judge_score: 2.0 | justificación: La respuesta es incompleta y carece de detalles necesarios para un workflow de N8N, como los parámetros HTTP y la lógica de los nodos, lo que afecta la precisión y relevancia.

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

# Workflow N8N: Clasificador de Mensajes con IA → Slack

## JSON completo (importable)

```json
{
  "name": "Clasificador de Mensajes IA → Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod":