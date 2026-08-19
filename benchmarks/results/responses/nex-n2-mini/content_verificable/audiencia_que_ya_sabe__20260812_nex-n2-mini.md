# Nex-N2-Mini — content_verificable/audiencia_que_ya_sabe

- model_id: `nex-agi/nex-n2-mini`
- success: True  | final: 9.4 | quality: 10.0
- latency_total: 9.502s | tokens_per_second: 179.3
- input_tokens: 109 | output_tokens: 1704

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

### “Success” en n8n no siempre significa que pasó algo

En n8n, un workflow en **success** solo significa que la ejecución terminó sin errores no controlados. No significa que tu acción principal haya ocurrido.

Un caso típico: el webhook responde 200, la ejecución se ve verde, pero no se creó el ticket, no se envió el email, no se actualizó la fila ni se llamó la API destino.

¿Por qué pasa?

- Una condición falsa corta la rama y el nodo crítico nunca se ejecuta.
- Un payload entra por una ruta que no tiene acciones reales.
- Un nodo tipo **No Op** consume el evento.
- Un nodo con **Continue On Fail** absorbe el error y deja el workflow en success.
- Todo lo importante está debajo de un `When All`, `If`, o filtro que no se cumple.

Cómo detectarlo:

1. Revisa **Execution Details** y mira los `items` por nodo. Si el nodo que debería hacer el side effect quedó en 0 items, algo no llegó.
2. Marca el nodo crítico con una etiqueta como `ACTION`. Si no aparece ejecutado en el mismo minuto que el trigger, el flujo se cortó antes.
3. Añade una rama de validación. Si no se cumple la condición esperada, no termines en success: lanza un error, escribe en un log o dispara una alerta.
4. Usa **Continue On Fail** con cuidado. Si lo activas en un nodo crítico, necesitas una verificación posterior.
5. Para webhooks, prueba payloads válidos, inválidos y duplicados. Un 200 del webhook no garantiza que el caso sea procesable.
6. Si es posible, añade una “prueba de efecto”: consulta el sistema destino o guarda el id esperado. Si no aparece, marca la ejecución como fallida.

Regla práctica: si el workflow no puede demostrar que la acción ocurrió, no deberías llamarla success.