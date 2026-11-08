# Muse Wonder — content_verificable/audiencia_que_ya_sabe

- model_id: `meta/muse-wonder`
- success: True  | final: 8.3 | quality: 10.0
- latency_total: 16.267s | tokens_per_second: 124.9
- input_tokens: 117 | output_tokens: 2032

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

### Success, pero cero items procesados

Es el fallo que no aparece en ningún dashboard: la ejecución termina en verde, dura 1,2 s y no mueve ni un registro. Porque n8n solo marca error si un nodo lo lanza; si el flujo se vacía por el camino, para él todo fue bien.

Pasa constantemente por tres sitios:

**1. Un filtro se lo come todo.** El IF/Switch cambia por un campo que ahora llega `null`, con otro nombre o como string en vez de number. Todo cae por la rama que no conecta a nada.

**2. La API devuelve 200 vacío.** Sin items, el siguiente nodo ni se ejecuta. O devuelve un JSON sin el array que esperabas y tu Split Out procesa cero elementos sin protestar.

**3. Merge / Wait esperando una rama que nunca llega**, con `Continue On Fail` o un nodo que traga el error y sigue con un payload vacío.

Cómo lo cazo yo:

Deja de mirar el estado y empieza a afirmar el resultado. Al final del flujo, un Code mínimo:

```js
if ($input.all().length === 0) throw new Error('0 items procesados');
return $input.all();
```

Y lo mismo con contadores: guarda cuántos items entraron tras el trigger, compáralos antes de cerrar y lanza error si entran 100 y salen 0 sin una razón explícita. Esa rama vacía también merece su propio camino hacia Slack/Telegram, no un No Operation.

Regla práctica: si un workflow puede terminar sin tocar el sistema destino, no está terminado. El verde solo debería significar “hizo lo que tenía que hacer”, no “no se rompió nada por el camino”.