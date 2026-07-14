# DeepSeek V4 Pro — content_verificable/audiencia_que_ya_sabe

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 8.68 | quality: 10.0
- latency_total: 32.125s | tokens_per_second: 44.1
- input_tokens: 100 | output_tokens: 1418
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando soluciones prácticas y detalladas para detectar workflows que devuelven 'success' sin realizar acciones.

## Respuesta completa

No te fíes del verde. En n8n, que un workflow termine en *success* solo significa que ningún nodo lanzó un error. No significa que hiciera algo. He visto demasiados flujos que pasan sin pena ni gloria y el equipo se entera cuando ya es tarde.

**¿Por qué ocurre?** Porque un flujo puede recorrer su ruta más corta sin ejecutar la lógica que importa. Los clásicos: un IF que no tiene rama *false* y cuando la condición no se cumple la ejecución se acaba; un Split In Batches que recibe cero ítems y simplemente termina; o peor, un nodo NoOp o un HTTP Request que captura el error con *Continue on Fail*, retorna ítems vacíos y nadie se entera. El workflow no ve nada mal: no hay excepción, así que pinta la palomita verde y a otra cosa.

**Cómo cazarlo:** La clave es medir cuántos ítems llegan al nodo crítico. Si la acción de negocio (Slack, DB, API) nunca se dispara, tu éxito es un fantasma.

- **Cron o webhook vacío:** Justo después del trigger, añade un nodo Code que reviente si `items.length === 0`. Un `throw new Error('Sin datos de entrada')` es mil veces mejor que un falso positivo.
- **IFs sin rama falsa:** Cierra siempre el ciclo con un Stop and Error en la rama negativa, con un mensaje descriptivo. O redirige a un nodo que loguee el vacío y luego detenga.
- **Webhooks con respuesta:** No devuelvas 200 a ciegas. Usa un Switch: si el nodo procesador generó datos, responde con el payload; si no, responde con 400 o un JSON que indique `processed: false`. Así el cliente también puede reaccionar.
- **Monitoreo en producción:** Activa el nodo Execution Data justo antes del final y fuerza un error si el conteo de ítems es cero. En el log quedará un error explícito, no un silencio cómodo.

Un éxito falso es más peligroso que un error estrepitoso, porque nadie va a revisar. Con una validación mínima de salida, conviertes la trampa del *success* vacío en una alerta temprana. Dedícale cinco minutos a cada workflow: el silencio nunca es buena noticia.