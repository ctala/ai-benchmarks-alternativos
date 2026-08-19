# Claude Opus 5 (suscripción) — content_verificable/audiencia_que_ya_sabe

- model_id: `claude-opus-5`
- success: True  | final: 8.03 | quality: 10.0
- latency_total: 34.407s | tokens_per_second: 39.8
- input_tokens: 2 | output_tokens: 1368

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

## "Success" no significa que pasó algo

El estado de una ejecución mide una sola cosa: que ningún nodo tiró una excepción. No mide que el trabajo se haya hecho. Son cosas distintas y la diferencia te puede costar semanas.

Los cuatro casos que más me han mordido:

**1. Cero items.** Un IF o un filtro deja la rama vacía. Los nodos de abajo no corren, nadie falla, la ejecución queda verde. Procesaste 0 registros y el dashboard dice que todo bien.

**2. 200 con error adentro.** La API responde 200 y el error viene en el body. Me pasó con Skool: mandé un parámetro de notificación inválido, devolvió 200, y el correo nunca salió. Si validas solo el status code, esto es invisible. Peor: un 202 con cuerpo vacío también entra en el rango 2xx y `response.ok` te dice que sí.

**3. Sub-workflows.** El nodo Execute Workflow reporta el éxito de la llamada, no del trabajo interno. Si adentro hay un continueOnFail, el padre nunca se entera.

**4. Dos workflows con el mismo nombre.** Editas uno, corre el otro. Clásico y humillante.

**Cómo detectarlo:** no confíes en el estado, verifica el efecto. Agrega un nodo final que lea de vuelta el resultado real (consulta el registro creado, lista el post, cuenta las filas) y compara contra lo esperado. Si no coincide, Stop and Error. Y alerta cuando el conteo sea 0, no solo cuando haya excepción.

Una regla sin un instrumento que la haga cumplir es una regla que ya se rompió y no te enteraste.