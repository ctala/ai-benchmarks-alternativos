# Qwen 3.8 27B — content_verificable/audiencia_que_ya_sabe

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 8.36 | quality: 10.0
- latency_total: 60.434s | tokens_per_second: 40.8
- input_tokens: 148 | output_tokens: 2466

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa



Un workflow en n8n puede terminar en green sin haber tocado ningún dato. No es un bug: es el estado de ejecución, no un veredicto de efecto.

Suele pasar por varios motivos. Una condición o filtro excluye todo el payload y el nodo simplemente no produce items downstream. Un HTTP Request devuelve 200 porque el endpoint recibió la petición, aunque tu lógica interna no haga nada. Un nodo de Code, Function o If termina con success aunque no llame a nada. Un batch queda vacío por deduplicación, ventana temporal o token de cursor agotado. Y, en casos más crueles, un error se traga en un error workflow que también termina bien o en una API que responde success semánticamente pero no cambia el estado.

La detección no puede depender solo del status de n8n. Necesitas invariants de negocio: si un trigger debería generar N acciones, mide N. Añade un nodo final de assertion que valide que al menos un item sobrevivió al filtro, o que la respuesta del endpoint contiene el identificador esperado, o que el cambio en base de datos/API es observable. Si no hay items, que el workflow falle con un mensaje claro, no un success vacío.

En producción, sé paranoico: loguea conteos de entrada/salida por nodo, IDs procesados, hash del payload o estado antes/después. Compara contra un heartbeat mínimo y dispara alertas cuando la ejecución es exitosa pero el efecto es cero.

Recuerda: success significa que el grafo terminó. Efecto significa que algo cambió. No son lo mismo.