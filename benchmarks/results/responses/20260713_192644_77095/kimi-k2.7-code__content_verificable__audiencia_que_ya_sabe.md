# Kimi K2.7 Code — content_verificable/audiencia_que_ya_sabe

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 8.75 | quality: 10.0
- latency_total: 9.005s | tokens_per_second: 84.2
- input_tokens: 120 | output_tokens: 758
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para expertos en n8n, abordando el problema de manera exhaustiva y ofreciendo soluciones prácticas.

## Respuesta completa

 **El “success” mentiroso de n8n**

Un workflow que termina en verde no siempre ha hecho lo que debía. De hecho, es uno de los fallos más difíciles de detectar: n8n devuelve `success` si el último nodo respondió sin error, no si tu lógica produjo el resultado esperado.

Los escenarios habituales son fáciles de imaginar: una condición `IF` que nunca entra por la rama verdadera, una query que devuelve 0 filas, un mapeo de items vacío, un `Respond to Webhook` configurado con un status 200 fijo, o un nodo que “continúa” aunque falle y simplemente no emite items. El workflow acaba feliz; el sistema externo nunca recibió nada.

Para detectarlo, no te fíes del color. Fíate de los datos.

Después de cualquier operación crítica, valida que los items existan y contengan lo esperado. Usa un nodo `IF` o `Code` para comprobar `$input.all().length` o campos obligatorios. Si no hay output, lanza un error con `Stop and Error` o un `Error Trigger` personalizado. Es mejor una ejecución roja que una verde inútil.

En webhooks, evita respuestas estáticas. Devuelve el estado real: si no se procesó nada, responde `204` o un JSON con `processed: 0`. Y si el workflow debe modificar algo, compara el estado antes y después: si no cambió, algo falló en silencio.

Por último, monitoriza fuera de n8n. Envía métricas a tu stack habitual — ejecuciones, items procesados, excepciones — y alerta cuando caigan a cero o cambien de patrón. El panel de ejecuciones de n8n es útil, pero no escala para detectar silencios.

Un `success` sin acción es peor que un error evidente. Diseña tus workflows para que muerdan cuando no pasa nada.