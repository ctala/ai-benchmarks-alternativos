# Muse Glimmer 30B — content_verificable/audiencia_que_ya_sabe

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 6.01 | quality: 6.0
- latency_total: 12.788s | tokens_per_second: 157.6
- input_tokens: 118 | output_tokens: 2015

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

Te ha pasado. El workflow termina en verde, el webhook responde 200, Slack te dice 'success' y en la base de datos no hay nada nuevo. El peor bug es el silencioso.

En n8n un 'success' solo significa que no hubo excepción, no que hizo lo que esperabas.

Los culpables habituales:
1. Entrada vacía. Un IF filtra todo el payload y la rama verdadera no recibe items. El workflow sigue, sin error, sin trabajo.
2. Respuesta vacía con código 200. La API devuelve [] o {} y el siguiente nodo no itera. Para n8n es un éxito.
3. Try/Catch demasiado generoso. Capturas el error, logueas y dejas pasar un flujo vacío.
4. Deduplicación implícita. Un nodo de upsert no crea nada porque todo ya existe.

Cómo detectarlo sin volverte loco:
Empieza contando. Un Function al inicio guarda `itemsIn = $items().length`. Al final otro Function compara con `itemsOut`. Si es cero, lanza error explícito.

Usa la ruta 'No Items' del nodo IF para disparar una alerta a #ops en lugar de morir en silencio.

Añade un nodo Set de auditoría final que siempre emita un objeto con métricas: items_in, items_out, registros_creados, timestamp. Conviértelo en tu contrato de éxito.

Y revisa las ejecuciones con Execution Data > Output, no solo el status verde.

Un workflow que no hace nada debería fallar ruidosamente. Haz que el silencio sea un error. Si tu métrica es cero dos veces seguidas, algo está roto, no optimizado.