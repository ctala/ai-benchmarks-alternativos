# Muse Spark 1.3 — content_verificable/audiencia_que_ya_sabe

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.58 | quality: 10.0
- latency_total: 14.493s | tokens_per_second: 154.4
- input_tokens: 116 | output_tokens: 2238

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

Tu ejecución sale en verde. Success. Y no hizo absolutamente nada.

No es un bug. En n8n, success solo significa que ningún nodo lanzó un error. No que tu lógica de negocio se cumplió. Si no entró ningún item a un branch, si todo se filtró, si un loop iteró sobre un array vacío, el run termina limpio. Silencio verde.

Los culpables de siempre:

**1. Filtros que se comen todo.** Un IF / Filter con `{{ $json.status }}` cuando el campo real viene como `{{ $json.data.status }}` no falla. Devuelve false para todo y la rama true nunca se ejecuta. Lo mismo con Switch sin fallback, o Remove Duplicates mal configurado.

**2. Expresiones que resuelven a vacío.** `{{ $json.customers.map(c => c.id) }}` sobre un payload sin `customers` no siempre explota, devuelve `[undefined]` o `[]`. El HTTP Request siguiente hace una llamada con body vacío, recibe 200, y lo marcas como enviado.

**3. Ramas que nunca se unen.** Merge en modo Append esperando dos inputs, Code con `return []`, o un Loop que no entra porque `$input.all()` está vacío. Todo downstream simplemente no se ejecuta. Sin error.

¿Cómo detectarlo?

Deja de confiar en el color. Pon Code de guarda al final de ramas críticas: `if ($input.all().length === 0) throw new Error('0 items procesados')`. Activa 'Always Output Data' solo donde tenga sentido y añade un NoOp + Slack / Sentry para el caso vacío. Y en Settings, guarda ejecuciones de producción y crea una vista que busque success con 0 items escritos.

Verde no es hecho. Audítalo.