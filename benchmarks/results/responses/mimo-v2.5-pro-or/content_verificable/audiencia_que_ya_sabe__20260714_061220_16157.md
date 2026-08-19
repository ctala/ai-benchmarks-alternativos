# MiMo-V2.5 Pro — content_verificable/audiencia_que_ya_sabe

- model_id: `xiaomi/mimo-v2.5-pro`
- success: True  | final: 8.56 | quality: 10.0
- latency_total: 17.622s | tokens_per_second: 41.8
- input_tokens: 107 | output_tokens: 737
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para expertos en n8n, abordando el problema específico con soluciones prácticas.

## Respuesta completa

# Tu workflow dice "success" pero no hizo nada

Lo has visto. El ejecution log marca verde, cero errores, y sin embargo... nada pasó. Ni un registro insertado, ni un mensaje enviado, ni un dato transformado. Tu workflow mintió.

Esto ocurre por una razón sencilla: **n8n no considera "sin items" como un error**. Si una ejecución recorre todos los nodos y ninguno lanza excepción, el status es success. Que el nodo final procese 0 ítems es irrelevante para el motor.

## Los culpables habituales

**El IF / Filter que descarta todo.** Tu nodo de filtrado recibe 50 items, ninguno cumple la condición, y los nodos downstream nunca se ejecutan. Pero el workflow no falla: simplemente no tiene nada que hacer downstream.

**El HTTP Request con `continueOnFail`** o un error handler que captura y no re-lanza. La llamada devuelve un 404 o un body vacío, tu nodo lo absorbe con gracia, y la ejecución sigue su curso... hacia ningún sitio.

**El SplitInBatches sobre un array vacío.** Cero elementos, cero iteraciones. El loop termina instantáneamente. Success.

**Una query SQL o un LDAP search con resultado vacío.** El nodo no falla; devuelve un array de largo 0. Y el Merge posterior dice "no tengo nada de este lado, sigo".

## Cómo detectarlo

**Revisa el item count de cada nodo** en la pestaña de output. Si el último nodo útil tiene 0 items, algo se filtró antes.

**Añade un nodo final de validación:** un IF que compruebe `$input.all().length > 0`. Si da false, lanza un error con un nodo Code o un `throw`. Convierte la mentira en un fallo visible.

**Usa el panel de executions con filtro "0 items"** para buscar patrones: ¿siempre falla a la misma hora? ¿con el mismo tipo de payload?

**Loguea el item count** en cada nodo crítico con un pequeño Code node: `console.log(items.length)` en modo `executeOnce`. Te da trazabilidad sin reescribir nada.

---

El success vacío es silencioso y caro: el workflow "funciona" durante semanas mientras los datos se pierden. Pon un centinela donde importa y duerme tranquilo.