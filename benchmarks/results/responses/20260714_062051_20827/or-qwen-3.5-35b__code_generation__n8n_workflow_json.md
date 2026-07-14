# Qwen 3.5 35B — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3.5-35b-a3b`
- success: True  | final: 6.77 | quality: 7.2
- latency_total: 33.984s | tokens_per_second: 60.3
- input_tokens: 125 | output_tokens: 2048
- judge_score: 3.0 | justificación: La respuesta proporciona un JSON básico para un workflow de n8n, pero carece de detalles completos, especialmente en la configuración del nodo de OpenAI y el nodo de Slack, lo que afecta la precisión y profundidad.

## Respuesta completa

Aquí tienes el JSON completo del workflow de n8n.

Para que funcione, asegúrate de tener instalados los nodos de **Webhook**, **OpenAI (AI Chat)** y **Slack** en tu instancia.

### Instrucciones de instalación:
1. Crea un nuevo workflow en n8n.
2. Haz clic en el botón "Importar" (arriba a la derecha) y pega el siguiente código JSON.
3. Configura las credenciales de **OpenAI** y **Slack** en los nodos correspondientes.
4. Activa el workflow (toggle en la parte superior).

```json
{
  "name": "Clasificador de Mensajes a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "lead-classification",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "webhook-node-id",
      "name": "Webhook Trigger",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        250,
        300
      ],
      "webhookId": "webhook-test-id-123"
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "prompt": "Classifica