# Qwen 3.7 Max — content_verificable/audiencia_que_ya_sabe

- model_id: `qwen/qwen3.7-max`
- success: True  | final: 8.36 | quality: 10.0
- latency_total: 34.56s | tokens_per_second: 53.3
- input_tokens: 110 | output_tokens: 1841
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando soluciones prácticas y detalladas para un público experto.

## Respuesta completa

**Asunto:** 🟢 El "Success" fantasma: cuando n8n te miente

Revisas el historial de ejecuciones. Todo verde. *Success*. Pero al revisar la base de datos o el CRM, no se actualizó nada. El workflow no falló; simplemente no hizo nada y n8n lo celebró.

¿Por qué ocurre? Para el motor de n8n, una ejecución es exitosa si termina sin lanzar una excepción no controlada. Si tu *HTTP Request* devuelve `{"data": []}` y tu lógica de mapeo o iteración no tiene elementos que procesar, la rama muere en silencio. Si un *Switch* no encuentra coincidencia y no tiene ruta *fallback*, el payload se descarta y el workflow termina "feliz".

Aquí tienes tres patrones para cazar estos falsos positivos antes de que rompan algo en producción:

**1. Validación defensiva post-API:**
Nunca asumas que el endpoint traerá datos. Inmediatamente después de un *HTTP Request* crítico, pon un *Code* node:
`if ($input.all().length === 0) throw new NodeOperationError(this.getNode(), 'Payload vacío');`

**2. La ruta "Catch-All" obligatoria:**
Configura siempre una ruta por defecto en tus nodos *Switch* o *IF*. Si el payload no matchea, envía un webhook a tu canal de alertas en Slack/Discord con el `$json` original para debuggear.

**3. Alertas por "Silent Drops":**
Si usas *Wait* nodes o sub-workflows con *Execute Workflow*, verifica que el array de salida no esté huérfano. Un sub-workflow que termina sin retornar items al padre dará por buena la ejecución principal.

No confíes en el check verde. Confía en tus aserciones.