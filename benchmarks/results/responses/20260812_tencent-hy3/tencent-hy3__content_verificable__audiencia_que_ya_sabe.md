# Tencent Hy3 — content_verificable/audiencia_que_ya_sabe

- model_id: `tencent/hy3`
- success: True  | final: 8.77 | quality: 10.0
- latency_total: 48.591s | tokens_per_second: 66.7
- input_tokens: 113 | output_tokens: 3242

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

¿El check verde te tranquiliza? No debería. En n8n, un workflow devuelve 'success' (o un 200 OK en tu webhook) simplemente porque ningún nodo lanzó una excepción. Eso no significa que haya procesado ni un solo dato.

El "éxito silencioso" es la trampa favorita de los pipelines maduros. Ocurre cuando tu nodo HTTP Request consulta una API que responde con un array vacío (`[]`), o cuando tu nodo IF descarta todos los ítems porque la condición de filtrado cambió sutilmente. n8n propaga el flujo, los nodos finales no reciben nada, pero como no hubo un `throw`, el motor cierra la ejecución con éxito. Si expones un webhook, el cliente externo recibe su 200 y asume que el trabajo está hecho.

¿Cómo cazarlo antes de que corrompa tu pipeline de datos?

1. **Asegura la salida con código:** Si el volumen es crítico, inserta un nodo "Code" justo antes del destino final. Un simple `if ($items().length === 0) { throw new Error('Silent success: 0 items'); }` fuerza un fallo real que tu Error Workflow capturará.
2. **Ruteo explícito de vacíos:** No dejes que los arrays vacíos lleguen al final silenciosamente. Conecta la salida "false" de tus nodos IF o Filter a un nodo "Stop and Error" o a un canal de alerta (Slack/Discord) dedicado a anomalías de volumen.
3. **Monitorea tendencias, no solo estados:** Un webhook que pasa de 1,000 ejecuciones diarias con payloads a 0, pero sigue en verde, es una red flag. Usa el nodo "Execute Workflow" para enviar métricas de `$execution.id` y conteo de ítems a un dashboard externo.

No confíes en el color verde. Confía en tus assertions.