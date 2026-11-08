# Claude Opus 5.5 — content_verificable/audiencia_que_ya_sabe

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.31 | quality: 10.0
- latency_total: 10.247s | tokens_per_second: 86.9
- input_tokens: 161 | output_tokens: 890

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

# El verde que miente

Hay un estado peor que un error en rojo: el **success** de un workflow que no tocó ni un solo registro.

**Por qué pasa:**

- **Cero items no es un error.** Si un nodo devuelve un array vacío, los siguientes simplemente no se ejecutan. n8n marca la ejecución como completada y sigue con su vida.
- **La rama que nadie conectó.** Un IF o un Switch que manda todo por la salida sin conectar termina "bien".
- **El 200 con el error en el body.** Muchas APIs responden `200 OK` con `{"error": "invalid token"}`. Para el HTTP Request eso es éxito.
- **Continue On Fail activado "por si acaso".** El nodo falla, pasa el error como dato y nadie lo revisa.
- **Credenciales que caducan suavemente.** Algunas APIs no devuelven un 401, sino una lista vacía.

**Cómo detectarlo:**

1. **Valida el volumen.** Después de cada nodo crítico, usa un IF con `{{ $input.all().length === 0 }}` que lleve a un **Stop and Error**. Si esperas datos y no llegan, es un fallo y debe verse como tal.
2. **Valida el contenido, no solo el status.** Comprueba que el body tenga los campos que esperas antes de seguir.
3. **Recuerda que tu Error Workflow no sirve aquí.** Solo se dispara cuando algo falla, y en estos casos nada falla. Necesitas convertir el silencio en error de forma explícita.
4. **Monta un dead man's switch.** Al final del flujo, haz un ping a un servicio de heartbeat. Si el ping no llega, recibes la alerta.
5. **Revisa los conteos de items en el historial de ejecuciones**, no solo el color.

Un workflow sin asserts no te dice que funciona. Solo te dice que no se ha quejado.