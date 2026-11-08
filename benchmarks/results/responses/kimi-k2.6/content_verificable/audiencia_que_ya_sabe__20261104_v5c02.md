# Kimi K2.6 — content_verificable/audiencia_que_ya_sabe

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 8.47 | quality: 10.0
- latency_total: 33.715s | tokens_per_second: 58.5
- input_tokens: 120 | output_tokens: 1973

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

 El peor fallo en producción no es el que devuelve error: es el que termina en verde y no tocó un solo registro. Y en n8n, es más común de lo que parece.

Un workflow puede devolver *success* porque el motor ejecutó nodos, no porque tu lógica de negocio haya corrido. El culpable clásico: un nodo IF que envía todo por la rama falsa hacia la nada, o un filtro que devuelve un array vacío y el siguiente nodo simplemente no hace nada con cero items. También está el *Continue On Fail* que traga errores silenciosamente, o un *Respond to Webhook* que envía 200 al cliente antes de que el HTTP Request o la inserción en base de datos terminen. El sistema externo ve OK, pero dentro no pasó nada.

Para detectarlo, olvídate del color verde. Ve a la ejecución y comprueba el output real: si un nodo crítico muestra 0 items o un array vacío, tu workflow falló sin avisar. Inserta nodos Set como checkpoints: si no llegan datos esperados, dispara una alerta explícita. No monitorees solo el estado de n8n; monitorea efectos secundarios. Si debe escribirse una fila, valida que exista. Si debe enviarse un mensaje, confirma el ID del mensaje enviado. Manda métricas de registros procesados a tu observabilidad: si el contador es cero en una ventana donde no debería, es incidente.

Un workflow que no transforma datos es un workflow roto que no lo sabe. Configura tus alertas para que griten por ausencia de output, no solo por excepciones.