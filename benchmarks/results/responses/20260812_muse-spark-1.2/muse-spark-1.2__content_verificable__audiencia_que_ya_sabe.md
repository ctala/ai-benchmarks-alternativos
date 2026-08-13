# Muse Spark 1.2 — content_verificable/audiencia_que_ya_sabe

- model_id: `meta/muse-spark-1.2`
- success: True  | final: 8.55 | quality: 10.0
- latency_total: 10.544s | tokens_per_second: 251.2
- input_tokens: 102 | output_tokens: 2649

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**El "success" mentiroso**

Ese verde te está mintiendo.

En n8n, `success` no significa "hice el trabajo". Significa "no exploté". Si ningún item llegó al nodo final, no hay error que lanzar. Solo silencio.

Y pasa más de lo que crees:

**1. El filtro fantasma.** Un IF, Switch o Filter que deja 0 items. La rama siguiente simplemente no se ejecuta. Para n8n, todo ok. Para tu negocio, un pedido sin procesar, un lead sin guardar.

**2. El HTTP que traga errores.** Tienes `Continue On Fail` o `Always Output Data` activado. Tu API devuelve un 404 o un `[]` vacío y tu workflow lo abraza como si fuera un 200 válido. El siguiente nodo recibe `{}` y no hace nada.

**3. El Merge / Loop vacío.** Un Merge en modo Combine esperando dos inputs donde uno nunca llega. O un Loop Over Items iterando sobre un array vacío. Cero iteraciones, cero errores.

### ¿Cómo lo cazas?

Deja de confiar en el color. Confía en los datos.

**Pon guardias.** Después de cada punto crítico, un Code node de una línea:

`if ($input.all.length === 0) throw new Error('Guard: 0 items tras [NombreNodo]');`

Obliga al workflow a fallar de verdad. Ahora sí lo verás en rojo y disparará tu Error Workflow.

**Segundo:** desactiva `Always Output Data` en nodos donde un vacío DEBE ser un error. Si no hay dato, que no haya output.

**Tercero:** audita. Si un workflow debe mover X items, añade un IF final: `{{$('Nodo Inicial').all.length}} !== {{$('Nodo Final').all.length}}` -> notifícate a Slack/Telegram.

El verde no es éxito. Que los datos lleguen al final, sí.