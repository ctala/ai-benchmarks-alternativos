# Claude Opus 5 Fast — content_verificable/audiencia_que_ya_sabe

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 8.33 | quality: 10.0
- latency_total: 6.91s | tokens_per_second: 148.0
- input_tokens: 159 | output_tokens: 1023

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

## El "success" que no hizo nada

Un workflow verde no significa que haya pasado algo. Significa que ningún nodo lanzó una excepción. Son cosas distintas, y la diferencia te va a morder en producción.

Los sospechosos habituales:

**Cero items.** Un nodo que recibe un array vacío no se ejecuta, y los siguientes tampoco. La ejecución termina limpia, sin insertar una sola fila. Si el filtro previo se pasó de estricto o la API devolvió `[]`, nunca te enteras.

**HTTP 200 con error dentro.** Muchas APIs responden `200` con `{"status":"error","message":"..."}`. Para el nodo HTTP Request eso es un éxito perfecto.

**`onError: continueRegularOutput`** heredado de un debug de hace tres meses. Silencia todo el nodo y sigue como si nada.

**Always Output Data** activado: te inyecta un item vacío que hace que el resto del flujo procese `undefined` sin quejarse. Un update con un WHERE que resuelve a `undefined` afecta cero filas y devuelve OK.

**Loops con cero iteraciones** y ramas IF que van a un nodo terminal que nadie mira.

Cómo detectarlo:

1. **Asserts explícitos.** Un nodo Code al final que valide `items.length > 0` y los campos críticos, con `throw` si no cuadra. Un fallo ruidoso vale más que un verde mentiroso.
2. **Contadores in/out.** Emite al final cuántos registros entraron y cuántos se escribieron. Si divergen sin motivo, alerta.
3. **Dead man's switch.** Un cron separado que revisa que el último registro procesado tenga menos de X horas. Detecta el silencio, no el error.
4. **Revisa los 200.** Valida el body, no el código de estado.

El objetivo no es que nunca falle. Es que cuando falle, se note.