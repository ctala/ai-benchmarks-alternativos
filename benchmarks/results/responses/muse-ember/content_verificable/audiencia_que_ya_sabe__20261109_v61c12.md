# Muse Ember — content_verificable/audiencia_que_ya_sabe

- model_id: `meta/muse-ember`
- success: True  | final: 8.92 | quality: 10.0
- latency_total: 8.633s | tokens_per_second: 587.4
- input_tokens: 117 | output_tokens: 5071

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**Success (0 items)**

El peor fallo en n8n no es el rojo. Es el verde.

Un workflow puede terminar en `success` sin haber tocado una API, escrito una fila ni enviado un mensaje. n8n no marca éxito porque tu objetivo se cumplió; lo marca porque ningún nodo lanzó una excepción no capturada. Confundirlas sale caro.

Las tres causas que más veo:

1. **Entrada vacía, salida vacía.** Un HTTP devuelve 200 con `[]`, una query devuelve 0 filas, un filtro elimina todo. El siguiente nodo recibe 0 items, no hace nada, y la ejecución sigue verde.
2. **Rama no tomada.** Un IF/Switch evalúa falso, no hay rama else y el workflow termina. Sin error, sin efecto.
3. **Error tragado.** `Continue On Error`, un Code node que devuelve `[]` en vez de lanzar, o una expresión que resuelve a `undefined` en vez de fallar. Todo sigue.

Detectarlo no es revisar ejecuciones a mano. Es un patrón:

Añade un nodo de aserción antes de dar por terminado. Un Code node final, o un IF que manda a `Stop and Error`:

```js
const items = $input.all();
if (!items.length) throw new Error('Ejecución vacía: 0 items procesados');
```

Y lo mismo para el efecto esperado: si debía crear un registro, verifica el ID devuelto, no solo el 200. Si debía paginar, verifica que no te quedaste en la primera vacía.

En producción, monitoriza dos señales, no una: ejecuciones fallidas *y* ejecuciones exitosas con 0 items en el último nodo con efecto. La segunda avisa de que algo dejó de llegar.

Verde no significa hecho.