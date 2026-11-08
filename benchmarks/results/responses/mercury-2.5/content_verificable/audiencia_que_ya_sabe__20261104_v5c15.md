# Mercury 2.5 — content_verificable/audiencia_que_ya_sabe

- model_id: `inception/mercury-2.5`
- success: True  | final: 9.28 | quality: 10.0
- latency_total: 5.599s | tokens_per_second: 475.1
- input_tokens: 115 | output_tokens: 2660

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa



Saben cómo montar un webhook en segundos. Pero hay un enemigo silencioso que ni el más experimentado escapa: el éxito falso.

Un workflow termina con estado 'success', pero el negocio no recibe la notificación. ¿Por qué? Porque 'success' en n8n solo confirma que el gráfico se ejecutó sin lanzar excepciones, no que los datos llegaron a su destino final.

A menudo, un nodo Filter elimina todo el payload debido a un cambio de schema no esperado. O un bloque Try-Catch captura un error, lo silencia y devuelve un objeto vacío. Incluso un nodo HTTP que recibe un 200 OK con un cuerpo vacío pasa sin aviso.

¿Cómo cazar estos fantasmas? Primero, activen el logging en cada salida crítica. Segundo, agreguen nodos de Control de Validación que lanzan errores si faltan campos requeridos. Tercero, implementen Webhooks de monitoreo externos que alerten si un workflow no produce eventos en un lapso definido.

Revisen el historial, no solo el estado final. Un nodo puede fallar internamente pero propagar un resultado vacío que el sistema considera "completado".

No confíen ciegamente en el estado verde. Validen el contenido real. La confianza es buena, la verificación sistemática es mejor. Construyan workflows que no solo corran, sino que entreguen.