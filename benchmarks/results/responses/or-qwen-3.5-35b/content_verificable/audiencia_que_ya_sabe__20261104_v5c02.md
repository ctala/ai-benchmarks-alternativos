# Qwen 3.5 35B — content_verificable/audiencia_que_ya_sabe

- model_id: `qwen/qwen3.5-35b-a3b`
- success: True  | final: 8.8 | quality: 10.0
- latency_total: 13.798s | tokens_per_second: 179.5
- input_tokens: 110 | output_tokens: 2477

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**Título: El éxito silencioso: cuando n8n dice "OK" y no hace nada**

Sabemos lo frustrante que es ver ese tick verde al finalizar una ejecución, revisar los datos y darte cuenta de que no se movió ni un byte. No fue un fallo de conexión; fue un silencio operativo.

En n8n, esto suele pasar por tres razones técnicas específicas:

1.  **Condicionales estrictos:** Un nodo IF devuelve falso basándose en una comparación de tipos o valores vacíos, cortando el flujo sin lanzar excepción alguna.
2.  **Manejo de errores agresivo:** Los nodos "Catch" dentro del mismo workflow absorben el fallo y continúan con un estado exitoso artificial, ocultando el origen del problema.
3.  **Payloads nulos:** Un webhook recibe la petición HTTP, pero la estructura JSON esperada está ausente, y el siguiente nodo simplemente ignora la entrada vacía sin detenerse.

**¿Cómo detectarlo?** La inspección visual no basta. Activa el historial de ejecuciones y filtra por "Éxito". Revisa explícitamente el campo `items.length` en cada paso crítico usando el modo Debug. Implementa nodos de "Log" que escriban en tu sistema externo (Slack, DB) confirmando la existencia de datos reales antes de procesarlos. Si el payload está vacío, el log debe alertar aunque el status sea 200.

Tu dashboard de éxito puede estar mintiéndote. No confíes en el color del nodo; confía en el volumen de datos procesados. Configura alertas automáticas para ejecuciones completadas con cero items procesados. Verifica siempre que el último nodo devuelva el número esperado de registros.

Hazte esta pregunta tras cada despliegue: "¿Qué haría si este dato fuera nulo?".

Saludos,
[Tu Nombre]