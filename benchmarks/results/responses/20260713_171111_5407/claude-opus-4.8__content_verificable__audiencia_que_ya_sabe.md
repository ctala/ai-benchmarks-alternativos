# Claude Opus 4.8 — content_verificable/audiencia_que_ya_sabe

- model_id: `anthropic/claude-opus-4.8`
- success: True  | final: 8.18 | quality: 10.0
- latency_total: 13.282s | tokens_per_second: 47.5
- input_tokens: 159 | output_tokens: 631
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para la audiencia experta, proporcionando soluciones prácticas y detalladas para detectar problemas en workflows.

## Respuesta completa

## El "success" que miente

Ese `success` verde al final de la ejecución no significa lo que crees. Significa que ningún nodo lanzó una excepción. Nada más. Y esa distinción te está costando datos.

El caso clásico: un nodo HTTP Request apunta a una API que responde `200 OK` con un body tipo `{"error": "rate limit exceeded"}`. Para n8n eso es un éxito perfecto. El status code fue bueno, no hubo timeout, el workflow siguió su curso feliz. Pero no procesaste nada.

Lo mismo pasa con los nodos que iteran sobre colecciones vacías. Un `Loop Over Items` con cero items no falla: simplemente no ejecuta el interior y pasa de largo. Tu workflow reporta éxito mientras tu tabla sigue vacía. Un filtro demasiado agresivo produce exactamente el mismo silencio.

**Cómo detectarlo:**

Deja de confiar en la ausencia de errores y empieza a afirmar la presencia de resultados. Mete un nodo `If` que valide lo que *esperas*: que el body no contenga `error`, que el count sea mayor a cero, que el campo crítico exista. Si la aserción falla, dispara un `Stop and Error` explícito. Ahora sí verás rojo cuando algo va mal.

Para las APIs mentirosas, activa "Never Error" en `false` y revisa que el nodo HTTP evalúe realmente el código de respuesta según *su* contrato, no según HTTP.

Y lo más barato: loguea el count de items procesados en cada paso crítico. Un workflow que "funciona" procesando 0 registros durante tres semanas es más caro que uno que se cae el primer día.

El éxito silencioso es el peor tipo de fallo: el que no sabes que tienes.