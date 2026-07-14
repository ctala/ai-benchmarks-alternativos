# Qwen 3-Next 80B Instruct — content_verificable/audiencia_que_ya_sabe

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 9.38 | quality: 10.0
- latency_total: 4.167s | tokens_per_second: 111.6
- input_tokens: 109 | output_tokens: 465
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para expertos en n8n, abordando el problema específico con soluciones prácticas.

## Respuesta completa

¿Tu workflow devuelve “success” pero no hizo nada? No es un bug. Es un diseño.

n8n no verifica si tus nodos *hicieron algo útil* — solo si *no fallaron*. Un Webhook recibió la petición? Success. Un HTTP Request respondió 200? Success. Un Cron se activó? Success. Pero si tu API cambió la estructura de la respuesta, tu nodo de “Set” asignó un valor vacío, o tu filtro ignoró todos los items… n8n no lo sabe. Y tú, si no lo revisas, tampoco.

El problema no es técnico. Es de *suposiciones*. Asumes que “success = acción completada”, pero en realidad significa “ejecución completada sin errores”. Y ahí es donde se escapan los workflows silenciosos: los que parecen funcionar… pero no mueven la aguja.

Cómo detectarlo:

1. **Agrega un nodo "Log" después de cada operación crítica**. No solo el output, sino el count: ¿Cuántos items salieron de tu Filter? ¿0? Eso es una alerta.
2. **Usa un nodo "Function"** para validar estados: si el campo `status` de tu respuesta no es "completed", lanza un error manual con `throw new Error('Expected status completed, got ' + status)`.
3. **Activa el “Debug Mode” en producción** (temporalmente) para ver flujos reales con datos reales.
4. **Monitorea métricas externas**: si tu workflow debe crear una tarea en Notion y no aparece en 5 minutos, activa una alerta en Datadog o Prometheus.

Success ≠ efecto.  
Efecto = validación + observabilidad.

No confíes en el green check. Confía en tus logs, tus counts y tus alertas.  
Porque lo peor que puede hacer un workflow no es fallar… es *funcionar en silencio*.

—  
[¿Quieres un template de workflow con validación automática? Responde “validación” y te lo envío.]