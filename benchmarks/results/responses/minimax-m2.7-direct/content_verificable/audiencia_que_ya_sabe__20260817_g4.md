# MiniMax M2.7 (directo) — content_verificable/audiencia_que_ya_sabe

- model_id: `MiniMax-M2.7`
- success: True  | final: 8.81 | quality: 10.0
- latency_total: 11.64s | tokens_per_second: 43.9
- input_tokens: 104 | output_tokens: 511

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

# El success silencioso

Lo has visto. Tu workflow devuelve "Success" y la pantalla se ilumina en verde. Pero nada ha pasado. La tarea sigue ahí, el cliente no recibió su email, la base de datos no se actualizó.

**El problema:** n8n marca como exitoso cualquier workflow que termina sin lanzar una excepción. Da igual si el nodo de HTTP Request получил un 404, si el Google Sheets escribió cero filas, o si tu Condition evaluó todo a false.

El nodo termina. Sin errores. Sin drama. El workflow sigue adelante y marca success.

## Cuándo pasa esto

- **Error Handler vacio:** captas el error pero no haces nada. El flujo continúa como si nada.
- **Merge donde solo llega data por una rama:** la otra rama devuelve null. Continúa feliz.
- **IF que no coincide nunca:** no es un error. Es un resultado válido. Pero tu código posterior recibe null y falla en silencio.
- **nodos con "continueOnFail" activo:** están configurados para ignorar fallos y devolver null.

## Cómo detectarlo

1. **Revisa siempre el output de cada nodo.** No solo el estado general. ¿Cuántos items llegaron? ¿Los campos que esperabas están ahí?

2. **Añade un nodo Code al final que valide data.** Si falta algo crítico, lanza un error explícito.

3. **Usa "always output data" en nodos problemáticos** o configura webhooks con respuesta dinámica basada en lo que realmente ocurrió.

4. **Logs.** Si el workflow "funciona" pero no ves el resultado esperado, probablemente está devolviendo success sobre nada.

El verde no garantiza éxito. Solo garantiza que no hubo excepciones.

Revisa tus outputs.