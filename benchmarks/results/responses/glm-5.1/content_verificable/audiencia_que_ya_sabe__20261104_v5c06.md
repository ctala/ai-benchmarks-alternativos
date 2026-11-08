# GLM-5.1 — content_verificable/audiencia_que_ya_sabe

- model_id: `z-ai/glm-5.1`
- success: True  | final: 8.56 | quality: 10.0
- latency_total: 26.971s | tokens_per_second: 61.4
- input_tokens: 107 | output_tokens: 1655

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

¿Cuántas veces has visto el check verde de "Success" en n8n y descubres horas después que no se hizo absolutamente nada? Es la trampa más frustrante del automation engineering.

Esto suele pasar por tres razones. 

**Primera:** un HTTP Request recibe un `200 OK`, pero el payload viene vacío o con un error lógico de la API (un array sin items). El workflow sigue su curso felizmente porque no hubo excepción a nivel de transporte. 
**Segunda:** tienes activado `Continue On Fail` en un nodo crítico. Si algo revienta internamente, n8n lo enmascara añadiendo una propiedad `error` al JSON del item, pero la ejecución no se detiene. 
**Tercera:** un nodo `If` o `Switch` se evalúa a falso, la rama principal no hace nada y el flujo termina sin que tú lo hayas previsto en tu diseño.

Para cazar estos falsos positivos, necesitas validación agresiva. No confíes en el status code. Usa un nodo `Code` justo después de tus llamadas críticas para verificar la estructura: si esperabas un array y está vacío, fuerza un fallo real usando `throw new Error('Payload vacío de la API X')`.

Si dependes de `Continue On Fail`, añade un `Filter` o `If` inmediatamente después que busque la existencia de `{{$json.error}}`. Si existe, redirige ese item a un sub-workflow de alertas (Slack/Email) en lugar de dejar que avance por el pipeline.

Finalmente, acostúmbrate a inspeccionar el conteo de items en el panel de ejecución. Si entran 10 items a un nodo y salen 0 sin un `Filter` explícito de por medio, tienes un silent failure.

El check verde solo significa que el código corrió. No significa que tu lógica tenga sentido.