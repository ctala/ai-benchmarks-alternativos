# GPT-5.6 Terra Pro — content_verificable/audiencia_que_ya_sabe

- model_id: `openai/gpt-5.6-terra-pro`
- success: True  | final: 8.49 | quality: 10.0
- latency_total: 14.595s | tokens_per_second: 136.1
- input_tokens: 3391 | output_tokens: 1986

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

Un workflow puede terminar en **“success”** y, aun así, no haber producido ningún efecto útil.

No es un bug: n8n está reportando que la ejecución no encontró un error técnico no manejado. Eso no equivale a “se cumplió el objetivo de negocio”.

Los casos más comunes:

- Un nodo devuelve **0 items** y los siguientes nodos simplemente no se ejecutan.
- Un `IF` envía todos los items por la rama “false”, pero esa rama termina sin acción.
- Un filtro, búsqueda o query devuelve vacío y nadie valida que debía existir al menos un resultado.
- Un nodo tiene `Continue On Fail` activado; el workflow avanza, pero el dato crítico nunca se creó, actualizó o envió.
- Una API responde `200` o `202`, aunque el payload sea inválido, duplicado o ignorado por el sistema destino.

La solución no es mirar más a menudo el historial de ejecuciones. Es diseñar **señales explícitas de éxito**.

Empieza por definir el postcondition de cada workflow: por ejemplo, “se creó exactamente una factura”, “se enviaron N mensajes”, o “se actualizó el registro con este ID”.

Luego conviértelo en validaciones:

1. **Comprueba cardinalidad.** Si esperabas al menos un item, falla de forma intencional cuando recibas cero.
2. **Valida la respuesta de destino.** No te quedes con el código HTTP: revisa IDs, estados, campos obligatorios y errores semánticos.
3. **Cuenta entradas y salidas.** Guarda métricas como `items_received`, `items_matched`, `items_processed` e `items_failed`.
4. **No ocultes fallos silenciosos.** Si usas `Continue On Fail`, enruta los errores a una rama de alerta o persistencia.
5. **Cierra con una aserción.** Un último nodo debería decidir si el resultado cumple el contrato del workflow.

“Success” debería significar “la ejecución terminó”. Tu observabilidad debe responder otra pregunta: **“¿ocurrió realmente lo que queríamos que ocurriera?”**