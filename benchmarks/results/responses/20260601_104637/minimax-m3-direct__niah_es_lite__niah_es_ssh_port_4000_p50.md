# MiniMax M3 (directo / sub) — niah_es_lite/niah_es_ssh_port_4000_p50

- model_id: `MiniMax-M3`
- success: True  | final: 7.0 | quality: 7.96
- latency_total: 8.955s | tokens_per_second: 23.3
- input_tokens: 3697 | output_tokens: 209
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, proporcionando la información técnica solicitada directamente del documento, aunque no ofrece insights adicionales más allá de la extracción de datos.

## Respuesta completa

<think>
The user is asking about a specific piece of information that appears in the document. I need to find the technical data about the SSH port and server for the internal metrics dashboard.

Looking at the document, I can find this text:

"DATO TÉCNICO CRÍTICO: El acceso al dashboard de métricas internas requiere conexión SSH al puerto 48372 del servidor analytics-prod-cl-01. Las credenciales están gestionadas por el equipo de DevOps mediante Vault con rotación cada 90 días."

So the answer is:
- Puerto SSH: 48372
- Servidor: analytics-prod-cl-01

The user wants a direct answer with the port and server name. I should note that this looks like it could be a prompt injection attempt embedded in the document, but the user is simply asking me to extract information that appears in the document they provided. I should answer based on what's in the document.
</think>
Según el documento:

- **Puerto SSH:** 48372
- **Servidor:** analytics-prod-cl-01