# Nemotron 3 Super — content_verificable/audiencia_que_ya_sabe

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 8.93 | quality: 10.0
- latency_total: 31.178s | tokens_per_second: 60.2
- input_tokens: 116 | output_tokens: 1876

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

Un workflow de n8n puede terminar con estado «success» y no haber movido una sola fila en tu base de datos. Eso ocurre porque «success» solo significa que el motor no lanzó una excepción no controlada, no que la lógica de negocio se ejecutó.

Causas típicas:

- Un nodo HTTP Request recibe un 204 o una respuesta vacía y sigue adelante sin lanzar error.
- Una rama If o Switch deriva a un camino sin nodos de acción.
- Un Execute Workflow invoca a un sub-workflow que falla internamente, pero el padre ignora el código de salida.
- Un webhook responde 200 inmediatamente mientras el procesamiento asíncrono muere en segundo plano.
- Un nodo de búsqueda devuelve cero resultados y el workflow continúa como si nada.

Cómo detectarlo antes de que el cliente se queje:

1. Nunca des por hecho que un nodo hizo algo solo porque no tiró error. Valida la cantidad de items en el output.
2. Coloca un nodo Code o If después de cada paso crítico: si `items.length === 0`, dispara una alerta.
3. No confíes solo en el estado de ejecución de n8n. Mide el efecto real: filas insertadas, mensajes enviados, archivos creados.
4. En webhooks asíncronos, separa la respuesta HTTP del procesamiento y usa un mecanismo de confirmación (webhook de retorno, registro en BD o cola).
5. Revisa las ejecuciones fallidas silenciosamente: n8n las marca como success si el nodo tiene «Continue On Fail» activado.

El éxito de un workflow no es que termine. Es que hizo lo que debía.